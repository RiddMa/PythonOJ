import codecs
import csv
import json

import requests

payload = {"query": "", "chief_org": [], "classify": ["1"], "selling_type": [], "status": [], "appid": 10000}
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.198 Safari/537.36",
    "x-client": "web",
    "xtbz": "xt"
}
base_url = "https://www.xuetangx.com/api/v1/lms/get_product_list/?page="


def post(page_num: int) -> dict:
    x = requests.post(base_url + str(page_num), headers=header, data=payload)
    y = json.loads(x.text)
    # print("post page"+str(page_num)+" ends")
    return y


def add2csv(json_obj: dict, csv_writer):
    class_list = json_obj["data"]["product_list"]
    for item in class_list:
        name = item['name']
        school = item["org"]['name']
        count = item['count']
        teacher_list = []
        for teacher in item['teacher']:
            teacher_list.append(teacher['name'])
        content = [name, count, school, "、".join(teacher_list)]
        csv_writer.writerow(content)
        # print(content)


def main():
    total_page_num = 37
    with codecs.open("xuetangx.csv", "w", encoding="utf-8") as csvf:
        writer = csv.writer(csvf)
        writer.writerow(["课程名称", "选课人数", "学校", "老师"])
        for i in range(1, total_page_num + 1):
            ret_json = post(i)
            add2csv(ret_json, writer)


if __name__ == "__main__":
    main()
