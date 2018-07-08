"""

"""

from xml.etree import ElementTree
import codecs

from old_swedish_texts.utils import normalize_sentence

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def read_corpus():
    with codecs.open("corpora/fsv-aldrelagar.xml", "r", encoding="utf8") as f:
        text = f.read()

    root = ElementTree.fromstring(text)
    ltext = []
    for text in root:
        title = text.attrib["title"]
        lparagraph = []
        for paragraph in text:
            sentences = []
            for sentence in paragraph:
                lsentence = []
                for word in sentence:
                    lsentence.append(word.text)
                sentences.append(normalize_sentence(lsentence))
            lparagraph.append(" ".join(sentences))
        ltext.append("\n\n".join(lparagraph))
    return ltext


if __name__ == "__main__":
    print(read_corpus())
