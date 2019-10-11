import sqlite3

def getDBInfo(database, column, id=None):
    conn = sqlite3.connect("shop.db")
    cur = conn.cursor()
    data = []
    if(id == None):
        sql = "SELECT " + column + " FROM " + database
        cur.execute(sql)
    else:
        sql = "SELECT " + column +" FROM "+database + " WHERE id= " + str(id)
        cur.execute(sql)
    for row in cur:
        data.append(row)
    return data

def __getID(commodityName):
    "商品名から商品IDを検索して返す(見つからなければ-1を返す)"
    conn = sqlite3.connect("shop.db")
    cur  = conn.cursor()
    sql = "SELECT id, name FROM Shop"
    cur.execute(sql)
    for row in cur:
        if row[1] == commodityName:
            return row[0]
    return -1

def __getHexID(commodityName):
    "商品名から商品IDを検索して16進数で返す(見つからなければ-1を返す)"
    conn = sqlite3.connect("shop.db")
    cur  = conn.cursor()
    sql = "SELECT id, name FROM Shop"
    cur.execute(sql)
    for row in cur:
        if row[1] == commodityName:
            return format(row[0], "X")
    return -1

def __getCommodityName(x):
    "商品IDから商品名を検索して返す(見つからなければ-1を返す)"
    conn = sqlite3.connect("shop.db")
    cur  = conn.cursor()
    sql = "SELECT id, name FROM Shop"
    cur.execute(sql)
    for row in cur:
        if row[0] == x:
            return row[1]
    return -1

def linkCommodityID(commodityList):
    "商品のIDを16進数にして連結させて返す"
    hexCommodityID = []
    for ID in commodityList:
        if ID < 15:
            ID = format(ID, "x")
            ID = "0" + ID
        else:
            ID = format(ID, "x")
        hexCommodityID.append(ID)
    return "".join(hexCommodityID)

def unfoldCommodityID(hexCommodityID):
    "商品のIDを16進数にして連結させたものを展開してタプル型(商品ID, 商品名)のリストにして返す"
    commodityID = []
    commodityData = []
    hexID = []
    i = 0
    while len(hexCommodityID)//2 > i:
        hexID = hexCommodityID[i*2] + hexCommodityID[i*2+1]
        if hexID[0] == "0":
            commodityID.append(hexID[1])
        else:
            commodityID.append(hexID)
        i += 1
    i = 0
    while len(hexCommodityID)//4 > i:
        decID = commodityID[i*2]
        decID = int(decID, 16)
        name  = commodityID[i*2+1]
        name  = int(name, 16)
        name = __getCommodityName(name)
        commodityData.append((decID, name))
        i += 1
    return commodityData