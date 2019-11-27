import sys
import xlwt

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
    title = ['name', 'age', 'birthday', 'interest']
    colume = ['xiaoming', 'zhangsan', 'lisi']
    for i in range(0, len(title)):
        sheet.write(0,i,title[i], set_style('Times New Roman', 220, True))

    for i in range(0, len(colume)):
        sheet.write(i+1, 0, colume[i], set_style('Times New Roman', 220, True))

    f.save('test.xls')

def main():
    write_excel()
    print("hello world")

if __name__ == '__main__':
    sys.exit(main())
