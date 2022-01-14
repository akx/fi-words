import xml.etree.ElementTree as et

kotus_noun_tn_classes = {
    1,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    2,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    3,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    4,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    5,
    6,
    7,
    8,
    9,
}

words = set()
for el in et.parse(open("./joukahainen.xml")).iter("word"):
    if any("noun" in wclass.text for wclass in el.find("classes").findall("wclass")):
        for form in el.find("forms").findall("form"):
            words.add(form.text)
for el in et.parse(open("./kotus-sanalista_v1.xml")).iter("st"):
    tn_node = el.find("t/tn")
    if tn_node is not None:
        tn_class = int(tn_node.text)
        word = el.find("s").text
        if tn_class in kotus_noun_tn_classes:
            words.add(word)
for word in sorted(words):
    print(word)
