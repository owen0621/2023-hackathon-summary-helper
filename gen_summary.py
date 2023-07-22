# -*- coding: UTF-8 -*-
import os
import openai
from dotenv import load_dotenv
import json 
load_dotenv()

with open("刑事_100,刑補,2_2011-11-21.json") as f:
    data = json.load(f)

judge = data["judgement"]
judge = judge.replace(" ", "")
judge = judge.replace("\r\n", "")
judge = judge.replace("，", "")
judge = judge.replace("：", "")
judge = judge.replace("。", "")
judge = judge.replace("、", "")
judge = judge.replace("　　　　　　　", "")
judge = judge.replace("　", "")

# print(judge)

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "為一個台灣律師對以下判決做200字摘要，根據“大前提、小前提、結論”的結構論述"
    },
    {
      "role": "user",
      "content" : judge
    }
  ],
  temperature=0
#   max_tokens=1024
)

completed_text = response.choices[0].message.content
print(completed_text)