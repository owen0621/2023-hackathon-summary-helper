import mysql.connector
import json

# 建立與MySQL資料庫的連線
connection = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_username",
    password="your_mysql_password",
    database="your_mysql_database",
)

# 解析JSON資料
json_data = """
{"court": "最高法院", "date": "2017-03-29T00:00:00+08:00", "no": "106,台上,75", "sys": "民事", "reason": "請求損害賠償等", "judgement": "最高法院民事判決", "type": "判決", "historyHash": "5d1da372ebf01cb5286c9f25", "mainText": "原判決廢棄，發回臺灣高等法院。", "opinion": "原審維持第一審所為上訴人不利之判決，駁回其上訴", "summary": "aaaaaa"}
"""
data = json.loads(json_data)

# 插入資料到資料表中
insert_query = """
INSERT INTO court_cases (court, date, no, sys, reason, judgement, type, historyHash, mainText, opinion, summary)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

values = (
    data["court"],
    data["date"],
    data["no"],
    data["sys"],
    data["reason"],
    data["judgement"],
    data["type"],
    data["historyHash"],
    data["mainText"],
    data["opinion"],
    data["summary"],
)

cursor = connection.cursor()
cursor.execute(insert_query, values)
connection.commit()

# 關閉連線
cursor.close()
connection.close()
