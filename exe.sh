#! /bin/bash

python3 plantuml_braille.py text_diagram.puml | xclip -selection clipboard
rm text_diagram.puml
