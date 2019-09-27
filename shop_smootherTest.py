# shop.py

import sqlite3
import databaseMethod
import password

from Crypto.Cipher import AES

ps = '{}************'.format("0123")
ps = password.encryptPassword(ps)
ps_raw = repr(ps)

databaseMethod.setDataReservation(2, 1, 32, "山田", "000000", 150,  ps_raw)

print(password.decryptPassword(1))
