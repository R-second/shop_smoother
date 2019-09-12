
import sqlite3

###  データベース関連メソッド集
# shop.dbにデータを登録
def setDataShop(name, price, junre, stock, reservation):
    conn = sqlite3.connect("shop.db")  # データベースに接続
    cur = conn.cursor()
    sql = "INSERT INTO Shop (name, price, junre, stock, reservation) VALUES (?, ?, ?, ?, ?) "
    cur.execute(sql, (name, price, junre, stock, reservation))
    conn.commit()

# reservation.dbにデータを登録
def setDataReservation(grade, department, number, name, purchase, price, password):
    conn = sqlite3.connect("shop.db")  # データベースに接続
    cur = conn.cursor()
    sql = "INSERT INTO Reservation (grade, department, number, name, purchase, price, password) VALUES (?, ?, ?, ?, ?, ?, ?) "
    cur.execute(sql, (grade, department, number, name, purchase, price, password))
    conn.commit()

def deleteData(database, id):
    conn = sqlite3.connect("shop.db")  # データベースに接続
    cur = conn.cursor()
    sql = "DELETE FROM " + database + "WHERE id = " + id
    cur.execute(sql)
    conn.commit()


# databaseからcolumn列の情報を取得する
# id指定も可能
# columnの場所を * にすることで全体の取得も可能
def getDBInfo(database, column, id=None):
    conn = sqlite3.connect("shop.db")  # データベースに接続
    cur = conn.cursor()
    data = []
    if(id == None):  # idが指定されていない場合
        sql = " SELECT " + column + " FROM " + database
    else:   # idが指定されている場合
        sql = " SELECT " + column + " FROM "+database + " WHERE id= " + str(id)
    cur.execute(sql)

    conn.commit()
    for row in cur:
        data.append(row)
    return data
