import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()


def mark_remove(text):
    judge = text
    judge = judge.replace(" ", "")
    judge = judge.replace("\r\n", "")
    judge = judge.replace("，", "")
    judge = judge.replace("：", "")
    judge = judge.replace("。", "")
    judge = judge.replace("、", "")
    judge = judge.replace("　　　　　　　", "")
    judge = judge.replace("　", "")
    return judge


def get_summary(judgement):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": "為一個台灣律師對以下判決做400字摘要，根據“大前提、小前提、涵攝”的三段論法結構生成回答",
            },
            {"role": "user", "content": judgement},
        ],
        temperature=0,
    )
    completed_text = response.choices[0].message.content
    return completed_text


if __name__ == "__main__":
    path = "judgement/0724"
    dirs = list(map(lambda x: path + "/" + x, os.listdir(path)))
    for dir in dirs:
        files = list(map(lambda x: dir + "/" + x, os.listdir(dir)))
        for file in files:
            inf = open(file, "r", encoding="utf8")
            data = json.load(inf)
            inf.close()

            if type(data["judgement"]) == list:
                data["judgement"] = "".join(data["judgement"])

            summary = get_summary(mark_remove(data["judgement"]))
            data["summary"] = summary
            print(data["summary"])

            outf = open(file, "w", encoding="utf8")
            json.dump(data, outf, ensure_ascii=False)
            outf.close()
            print("--------------------------------------------------")
