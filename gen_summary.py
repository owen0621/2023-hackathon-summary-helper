import os
import openai
from dotenv import load_dotenv
import json

from pathlib import Path

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
                "content": "為一個台灣律師對以下判決的法院見解部分做50字摘要",
            },
            {"role": "user", "content": judgement},
        ],
        temperature=0,
    )
    completed_text = response.choices[0].message.content
    return completed_text


if __name__ == "__main__":
    DATA_DIR_NAME = os.getenv('DATA_DIR_NAME')
    path = f"judgement/{DATA_DIR_NAME}"
    dirs = list(map(lambda x: path + "/" + x, os.listdir(path)))
    count = 0
    for dir in dirs:
        # Check if we have have this data's summary already.
        filename = Path(dir).stem + '.txt'
        result_dir = Path(f'./gpt_summarized_result/{DATA_DIR_NAME}/')
        if not result_dir.exists():
            result_dir.mkdir()
        result_file = result_dir / filename
        if result_file.exists():
            # If we already have this data's summary, go to next directly.
            # To save money! That's so important!!!
            continue

        if count > 5:
            break
        count += 1
        inf = open(dir, "r", encoding="utf8")
        data = json.load(inf)
        inf.close()

        if type(data["judgement"]) == list:
            data["judgement"] = "".join(data["judgement"])

        try:  # 使用 try，測試內容是否正確
            summary = get_summary(mark_remove(data["judgement"]))
            print("no")
            print(data["no"])
            print()
            print("summary")
            print(summary)
            print("--------------------------------------------------")
            pass
        except Exception as e:  # 如果 try 的內容發生錯誤，就執行 except 裡的內容
            raise e

        # Save the summarized result.
        with open(result_file, 'w', encoding='UTF-8') as file:
            file.write(summary)

    print('All the data (under "DATA_DIR_NAME") have already summarized.')

        # outf = open(file, "w", encoding="utf8")
        # json.dump(data, outf, ensure_ascii=False)
        # outf.close()
