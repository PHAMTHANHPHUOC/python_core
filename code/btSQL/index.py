# kết nối sql
import sqlite3
#kết nối đên csdl bằng đường dẫn
path = "C:/sql/sqlite.db"
connection = sqlite3.connect(path)
print(connection)

# ngắt kế nối
# connection.close()


# tạo đối tượng cursor
cursor = connection.cursor()

# tạo câu lệnh sql
# sql = "SELECT * FROM Studients WHERE Studients.diemtb>5"
# cursor.execute(sql)
# connection.commit()
# result = cursor.fetchall()
# print(result)
# cursor.close()



# sql = "SELECT * FROM Studients(masv,hovaten,diemtb) VALUES ('05','PHUOCDZ','9')"
# cursor.execute(sql)
# connection.commit()




# sql = "UPDATE Studients set diemtb=diemtb+1"
# cursor.execute(sql)
# connection.commit()
# result = cursor.fetchall()
# print(result)
# cursor.close()

# sql = "DELETE FROM Studients WHERE diemtb<10"
# cursor.execute(sql)
# connection.commit()
# cursor.close()



sql = "SELECT * FROM Studients ORDER By masv DESC"
cursor.execute(sql)
connection.commit()
result = cursor.fetchall()
cursor.close()


#in dữ liệu
def printAll(result):
    for item in result:
        print(item)
printAll(result)
