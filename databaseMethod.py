
import mysql.connector

###  データベース関連メソッド集
def db_connect():
    connect = mysql.connector.connect(
        host='localhost',
        port='8889',
        user='root',
        password='root',
        database='shopdb'
    )
    return connect


# shop.dbにデータを登録
def setDataShop(name, price, genre, stock, reservation, picPath):
    connect = db_connect()
    cur = connect.cursor()
    sql = "INSERT INTO Shop (name, price, genre, stock, reservation, picPath) VALUES (%s, %s, %s, %s, %s, %s) "
    cur.execute(sql, (name, price, genre, stock, reservation, picPath))
    connect.commit()

# reservation.dbにデータを登録
def setDataReservation(grade, department, number, name, purchase, price, password):
    connect = db_connect()
    cur = connect.cursor()
    sql = "INSERT INTO Reservation (grade, department, number, name, purchase, price, password) VALUES (%s, %s, %s, %s, %s, %s, %s) "

    cur.execute(sql, (grade, department, number, name, purchase, price, password))
    connect.commit()

def deleteData(database, id):
    connect = db_connect()
    cur = connect.cursor()
    sql = "DELETE FROM " + database + "WHERE id = " + str(id)
    cur.execute(sql)
    connect.commit()




# databaseからcolumn列の情報を取得する
# id指定も可能
# columnの場所を * にすることで全体の取得も可能
def getDBInfo(database, column, id=None):
    connect = db_connect()
    cur = connect.cursor()
    data = []
    if(id == None):  # idが指定されていない場合
        sql = " SELECT " + column + " FROM " + database
    else:   # idが指定されている場合
        sql = " SELECT " + column + " FROM "+database + " WHERE id= " + str(id)
    cur.execute(sql)

    for row in cur:
        data.append(row)
    return data
