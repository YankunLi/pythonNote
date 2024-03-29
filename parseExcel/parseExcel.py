import sys
import xlwt
import xlrd
import MySQLdb

class Student:
    def __init__(self, name, age, email, iq):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__iq = iq

    def show(self):
        print("Name: %s\tAge: %d\tEmail: %s\tIQ: %d\n" % (self.__name, self.__age, self.__email, self.__iq))

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

def write_excel():
    f = xlwt.Workbook()
    sheet = f.add_sheet('student', cell_overwrite_ok=True)
    title = ['name', 'age', 'email', 'iq']
    colume = ['xiaoming', 'zhangsan', 'lisi']
    for i in range(0, len(title)):
        sheet.write(0,i,title[i], set_style('Times New Roman', 220, True))

    for i in range(0, len(colume)):
        sheet.write(i+1, 0, colume[i], set_style('Times New Roman', 220, True))

    f.save('test.xls')

def read_excel():
    wb = xlrd.open_workbook(filename='./test.xls')
    print(wb.sheet_names())

    sheet = wb.sheet_by_index(0)
    print(sheet)

    contacts = []
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        dict = {}
        for j in range(0, cols):
            title = sheet.cell_value(0, j)
            value = sheet.cell_value(i, j)
            dict[title] = value
        contacts.append(dict)

    for i in range(len(contacts)):
        print(contacts[i])

def DB():
    db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8')

    cursor = db.cursor()

    sql = ''

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()

def main():
    stud = Student("xiaoming", 16, '111000@qq.com', 90)
    stud.show()
    write_excel()
    read_excel()
    print("hello world")

if __name__ == '__main__':
    sys.exit(main())
