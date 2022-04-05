import json
import xml.etree.ElementTree as ET


def parse_json(filename):
    all_words = []

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for news in data["rss"]["channel"]["items"]:
            words = news["description"].split(" ")
            for word in words:
                if len(word) > 6:
                    all_words.append(word)

    return all_words


def parse_xml(filename):
    all_words = []

    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(filename, parser)
    root = tree.getroot()

    xml_items = root.findall("channel/item")
    for xml_item in xml_items:
        words = xml_item.find("description").text.split(" ")
        for word in words:
            if len(word) > 6:
                all_words.append(word)

    return all_words


def find_top(all_words):
    unique_words = set(all_words)

    words_top = []
    for word in unique_words:
        words_top.append({'word': word, 'total': all_words.count(word)})

    words_top.sort(key=lambda d: d['total'], reverse=True)

    return words_top[:10]


words_top = find_top(parse_json("files/newsafr.json"))

print("Parsed json TOP-10:")
for word_data in words_top:
    print(word_data['word'], word_data['total'])

words_top = find_top(parse_xml("files/newsafr.xml"))

print()
print("Parsed xml TOP-10:")
for word_data in words_top:
    print(word_data['word'], word_data['total'])
