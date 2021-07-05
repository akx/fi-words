import json
import logging
import os.path
import posixpath
import urllib.request as ur
from http.client import HTTPResponse

import openpyxl

log = logging.getLogger("name_downloader")


def get_json(url):
    log.info("Fetching JSON %s", url)
    resp: HTTPResponse = ur.urlopen(url)
    assert resp.status == 200
    return json.loads(resp.read())


def get_binary(url) -> bytes:
    log.info("Fetching binary %s", url)
    resp: HTTPResponse = ur.urlopen(url)
    assert resp.status == 200
    return resp.read()


def get_resource_urls():
    package_data = get_json(
        "https://www.avoindata.fi/data/api/3/action/package_show?id=none"
    )
    resource_to_url = {}
    for resource in package_data["result"]["resources"]:
        name = resource["name"].lower()
        if "etunimi" in name:
            resource_to_url["first_names"] = resource["url"]
        if "sukunimi" in name:
            resource_to_url["last_names"] = resource["url"]
    return resource_to_url


def parse_dvv_xlsx(filename: str):
    xs = openpyxl.open(filename, read_only=True)
    for sheet in xs.worksheets:
        if sheet.title == "Saate":
            continue
        rows = [[str(c.value) for c in row] for row in sheet.iter_rows()]
        yield (sheet.title, rows)


def process_resource(file_id, url):
    local_name = posixpath.basename(url)
    if not os.path.isfile(local_name):
        data = get_binary(url)
        with open(local_name, "wb") as f:
            f.write(data)
    for sheet_title, rows in parse_dvv_xlsx(local_name):
        sheet_id = sheet_title.lower().replace(" ", "_")
        all_seen = set()
        with open(f"names/{file_id}_{sheet_id}.tsv", "w") as f:
            i = 0
            for i, row in enumerate(rows, 1):
                if len(row) == 2 and row[0] and row[-1].isdigit():
                    all_seen.add(row[0])
                    print(*row, sep="\t", file=f)
            log.info("Wrote %d rows into %s", i, f.name)
        with open(f"names/{file_id}_sorted.txt", "w") as f:
            i = 0
            for i, name in enumerate(sorted(all_seen), 1):
                print(name, file=f)
            log.info("Wrote %d rows into %s", i, f.name)


def main():
    logging.basicConfig(level=logging.INFO)
    urls = get_resource_urls()
    log.info(f"Found {len(urls)} resource URLs")
    for file_id, url in urls.items():
        process_resource(file_id, url)


if __name__ == "__main__":
    main()
