import xml.etree.ElementTree as et

words = set()
for el in et.parse(open("./joukahainen.xml")).iter("form"):
    words.add(el.text)
for el in et.parse(open("./kotus-sanalista_v1.xml")).iter("s"):
    words.add(el.text)
for word in sorted(words):
    print(word)
