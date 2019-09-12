# shop.py

import sqlite3
import databaseMethod
import password

ps = '{}************'.format("0123")
ps = password.encryptPassword(ps)


databaseMethod.setDataReservation(2, 1, 32, "d", "000000", 150, ps)

print(password.decryptPassword(1))
