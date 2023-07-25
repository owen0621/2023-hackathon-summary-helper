import mysql.connector
import json
import os

# 建立與MySQL資料庫的連線
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="HACKATHON",
)


def insert(data):
    insert_query = """
    INSERT INTO court_cases (court, date, no, sys, reason, judgement, type, historyHash, mainText, opinion)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
    )

    cursor = connection.cursor()
    cursor.execute(insert_query, values)
    connection.commit()
    # 關閉連線
    cursor.close()


if __name__ == "__main__":
    path = "../judgement/0725"
    files = list(map(lambda x: path + "/" + x, os.listdir(path)))
    for file in files:
        f = open(file, "r", encoding="utf8")
        data = json.load(f)
        f.close()
        if type(data["judgement"]) == list:
            data["judgement"] = "".join(data["judgement"])
        insert(data)

connection.close()
