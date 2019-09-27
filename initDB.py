
# databaseのセットアップ用
# 最初に動かす
#####メモ：mysql -u root -p shopdb


import mysql.connector
connect = mysql.connector.connect(
        host='localhost',
        port='8889',
        user='root',
        password='root',
        database='shopdb'
    )

conn = connect.cursor()

sql = "DROP TABLE IF EXISTS shop"
conn.execute(sql)

sql = "DROP TABLE IF EXISTS reservation"
conn.execute(sql)

# テーブルの作成

sql = """
    CREATE TABLE Shop( 
        id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
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
        id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
        grade INTEGER,
        department INTEGER,
        number INTEGER,
        name VARCHAR(30),
        purchase VARCHAR(100),
        price INTEGER,
        password VARCHAR(100)
    );
    """

conn.execute(sql)
connect.commit()

# データベースを閉じる
#conn.close()




