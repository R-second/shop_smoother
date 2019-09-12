

# password管理メソッド集

import sqlite3
from Crypto.Cipher import AES
import databaseMethod


# 売店側でshop.dbからパスワードをとってきて復号化
def decryptPassword(id):
    secret_key = '_KOSEN___shop___smoother'   # secret_keyは暗号化メソッドと共通
    crypto = AES.new(secret_key)       # secret_keyを元にしたクラスの生成
    cipher_data = databaseMethod.getDBInfo("reservation", "password", id)   # getDBInfoメソッドを使ってidのパスワード(暗号化済み)を取得
    original_password = crypto.decrypt(cipher_data[0][0])    # 復号化
    return original_password 

# 学生側でパスワードを暗号化
def encryptPassword(original_password):
    secret_key =  "_KOSEN___shop___smoother"    # secret_keyは復号化メソッドと共通
    crypto = AES.new(secret_key)     # secret_keyを元にしたクラスの生成
    cipher_data = crypto.encrypt(original_password)  # 暗号化
    return cipher_data



