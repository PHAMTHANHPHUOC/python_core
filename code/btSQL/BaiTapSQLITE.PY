import sqlite3

# tạo kết nối với CSDL
conn = sqlite3.connect("C:/sql/sqlite.db")
print(conn)

# tạo thông tin về lớp học\

#tạo table
cursor = conn.cursor()

#xóa table nếu như đã tồn tại
cursor.execute("DROP TABLE IF EXISTS lop_hoc")

#Tạo mới table
sql  = """
        CREATE TABLE lop_hoc(
            ma_lop text(50) NOT NULL PRIMARY KEY,
            ten_lop text(225) NULL DEFAULT NULL
        )
"""
cursor.execute(sql)
#INSERT dữ liệu
sql = """
        INSERT INTO TABLE lop_hoc
        VALUES
            ("PYTHON","lập trình python"),
            ("jsp","lập trình jsp")
"""
cursor.execute(sql)
conn.commit()

