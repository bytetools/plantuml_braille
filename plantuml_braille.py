import sys
import re
import louis

BRAILLE_TABLES = [
    "unicode-braille.utb",
    "en_CA.tbl"
]

INVALID_CHARACTERS = [
    "\\n",
]

MATCHES_TO_REPLACE = [
    '"(.*?)"',
    '^\s+[a-zA-Z\(\) ]+$',
    '(<=?::)[a-zA-Z\(\)]+$'
]
words_regex = r'|'.join(map(re.escape, MATCHES_TO_REPLACE))

def find_words(plantuml_src):
    words_words = [re.findall(reg, plantuml_src, re.MULTILINE) for reg in MATCHES_TO_REPLACE]
    return [word.strip() for words in words_words for word in words]

def is_allowed(word):
    """
    Used to filter if a word should me allowed
    """
    return not (word.startswith("#") or word.startswith("\n") or word in INVALID_CHARACTERS)

def clean(word):
    """
    Used to clean up valid words
    """
    return ("", word)

def translate_text(string):
    return louis.translateString(BRAILLE_TABLES, string)

def translate_word(word):
    word_ = clean(word)
    return word_[0] + translate_text(word_[1])

def convert_nomnoml(nomnoml_src):
    # sort be longest to shortest length, this allows a string like "Message" to be dealt with separately from "Message Queue". The larger sections are dealt with first.
    to_replace = sorted(list(find_words(nomnoml_src)), key=len)
    to_replace.reverse()
    # translate these words into braille
    translated_words = list(map(translate_word, to_replace))
    for ic in INVALID_CHARACTERS:
        for i in range(len(translated_words)):
            translated_words[i] = translated_words[i].replace(translate_word(ic), ic)
    replacement_dict = dict(zip(to_replace, translated_words))
    for text,replace_with in replacement_dict.items():
        nomnoml_src = nomnoml_src.replace(text, replace_with)
    return nomnoml_src

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You must specify a file")
        exit(1)
    file = open(sys.argv[1])
    contents = file.read()
    file.close()
    #print(find_words(contents))
    print(convert_nomnoml(contents))
