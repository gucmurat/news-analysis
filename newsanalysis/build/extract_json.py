import json
from datetime import date
import os

today = str(date.today())

f1 = open(f"json_files/news{today}.json")
news_list = json.load(f1)
f1.close()

f2 = open(f"json_files/output{today}.json")
out_json = json.load(f2)
out_list = list(out_json.values())
f2.close()

def ner_labels_of(dict):
    list1 = []
    for key in dict:
        if(key != "text" and key != "label"):
            for item in dict[key]:
                list1.append({"start": item[0], "end": item[1], "label": key})
    return list1

list_json = []
for i in range(len(out_list)):
    tag=None
    if out_list[i]["label"]==2:
        tag="POSITIVE"
    elif out_list[i]["label"]==0:
        tag="NEGATIVE"
    else:
        tag="NEUTRAL"

    out_dic= {
        "tagText": tag,
        "newsHeading": news_list[i]["title"],
        "date": news_list[i]["date"],
        "newsInfo": {
            "summary": news_list[i]["summary"],
            "newsTextAndEnts": {
                "text": out_list[i]['text'],
                "ents": out_list[i]['ents'],
            },
            "newsLink": news_list[i]["link"]
        }
    }
    list_json.append(out_dic)


with open(f"json_files/last{today}.json","w") as outfile:
  json.dump(list_json, outfile, indent = 4, default=str)
