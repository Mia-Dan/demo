from PyPDF2 import PdfFileWriter, PdfFileReader
from cmdUI import formatDraggedpath
# 截取pdf中，从某一页到某一页

start_page = 1 # 开始页，第一页
end_page = 489 # 截止页，最后一页
input_file_path = r"/Users/admin/Downloads/A4双面彩色喷墨\ 铜版纸胶装\ pdf首页为封面+不在内页中再次出现\ 封底书腰印红色.pdf "
output_file_path = "tmp/auto.pdf" # 默认在代码所在文件夹

input_file_path = formatDraggedpath(input_file_path)
output = PdfFileWriter()
pdf_file = PdfFileReader(open(input_file_path, "rb"))
pdf_pages_len = pdf_file.getNumPages()
 
# 若前面 start_page = 0, end_page = 5
# 保存input.pdf中的1-5页到output.pdf
start_page = start_page - 1
for i in range(start_page, end_page):
    output.addPage(pdf_file.getPage(i))
 
outputStream = open(output_file_path, "wb")
output.write(outputStream)