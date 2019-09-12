
# databaseのセットアップ用
# 最初に動かす

import sqlite3

conn = sqlite3.connect("shop.db")

sql =  "DROP TABLE shop"
conn.execute(sql)

sql = "DROP TABLE reservation"
conn.execute(sql)

# テーブルの作成

sql = """
    CREATE TABLE Shop( 
        id INTEGER PRIMARY KEY,
        name VARCHAR(20),
        price INTEGER,
        junre INTEGER,
        stock INTEGER,
        reservation INTEGER
    );
    """
conn.execute(sql)

sql = """
    CREATE TABLE Reservation(
        id INTEGER PRIMARY KEY,
        grade INTEGER,
        department INTEGER,
        number INTEGER,
        name VARCHAR(30),
        purchase VARCHAR(100),
        price INTEGER,
        password VARCHAR(20)
    );
    """

conn.execute(sql)
cur = conn.cursor()

# データベースを閉じる
conn.close()




