
import pymysql.cursors


# Konfigurasi koneksi ke database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='iqbaljackpot',
                             database='tugas',
                             cursorclass=pymysql.cursors.DictCursor)
 