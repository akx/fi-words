all: words/nouns.txt words/words.txt names/first_names_sorted.txt

words/words.txt: flatten_words.py joukahainen.xml kotus-sanalista_v1.xml
	PYTHONIOENCODING=utf8 python3 flatten_words.py > $@

words/nouns.txt: flatten_nouns.py joukahainen.xml kotus-sanalista_v1.xml
	PYTHONIOENCODING=utf8 python3 flatten_nouns.py > $@

names/first_names_sorted.txt: download_names.py
	PYTHONIOENCODING=utf8 python3 download_names.py

joukahainen.xml:
	curl https://joukahainen.puimula.org/sanastot/joukahainen.xml.gz | gunzip > $@

kotus-sanalista_v1.xml:
	curl https://kaino.kotus.fi/sanat/nykysuomi/kotus-sanalista-v1.tar.gz | tar xzO kotus-sanalista_v1/kotus-sanalista_v1.xml > $@
