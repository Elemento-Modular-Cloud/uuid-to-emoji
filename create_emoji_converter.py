# -*- coding: UTF-8 -*-
import json
from lxml import html
import requests

if __name__ == "__main__":
    url = "http://unicode.org/emoji/charts/full-emoji-list.html"
    response = requests.get(url)

    tree = html.fromstring(response.text)

    rows = tree.xpath("/html/body/div[3]/table/tr")

    converter = {}

    i = 0
    for row in rows[0:]:
        try:
            number = row.xpath(".//td[contains(@class, 'rchars')]")[0].text
            code = row.xpath(".//td[contains(@class, 'code')]/a")[0].text.replace('+','000').split()
            if len(code) > 1:
                continue
            uniint = int(code[0][1:],16)
            converter[int(i)] = chr(uniint)
            i+=1
            if i==1024:
                break
        except IndexError:
            continue

    print(converter)

    with open('emoji_converter.json', 'w') as fp:
        json.dump(converter, fp, ensure_ascii=False)