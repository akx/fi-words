download: joukahainen.xml kotus-sanalista_v1.xml

joukahainen.xml:
	curl https://joukahainen.puimula.org/sanastot/joukahainen.xml.gz | gunzip > $@

kotus-sanalista_v1.xml:
	curl https://kaino.kotus.fi/sanat/nykysuomi/kotus-sanalista-v1.tar.gz | tar xzO kotus-sanalista_v1/kotus-sanalista_v1.xml > $@