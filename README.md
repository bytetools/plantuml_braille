# plantuml_braille

Convert the visible text in plantuml (`.puml`) to braille.

Defualt configuration is:

```
plain text -> Canadian (8-dot) braille [en_CA.tbl] -> Unicode braille [unicode-braille.utb]
```

You must know the exact name of the table you want to use if you want to use any other braille table.
On Linux, you can find the list of tables in: `/usr/share/liblouis/tables/`

## Usage

```bash
$ ./plantuml_braille text_test.puml > braille_test.puml
```

## Requirements

* `python` (v3.6+)
	* `louis` (python library, in `requirements.txt`)
* `liblouis` (usually called this in your repo packaes)

## Contribution

Please send a pull request to the [Github](https://github.com/bytetools/plantuml_braille/) repo unless you work with Bytetools and have permissions.
