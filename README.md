# fi-words

A mechanically generated sorted list of Finnish words and given names.

## Usage

For most uses, you should probably only look at:

* words/words.txt – a list of Finnish words
* names/*.tsv – Finnish names in frequency order
* names/*.txt – Finnish names in alphabetical order

To regenerate the data, run `make` on a reasonably UNIXy system.

To regenerate the `names` data, you will need the `openpyxl` module for Python 3.

## License

* The [KOTUS word list](https://kaino.kotus.fi/sanat/nykysuomi/) is licensed under GNU LGPL / EUPL 1.1 / CC-BY 3.0.
* The [Joukahainen corpus](https://joukahainen.puimula.org/) is licensed under GNU GPL 2.0 or newer.
* The [Finnish names corpus](https://www.avoindata.fi/data/fi/dataset/none) is licensed under CC-BY 4.0.

* The glue code is licensed MIT.
