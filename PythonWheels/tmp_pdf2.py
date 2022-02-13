from PyPDF2 import PdfFileWriter, PdfFileReader
from cmdUI import formatDraggedpath
# 截取pdf中，从某一页到某一页

input_file_path = r"/Users/admin/Downloads/B5双面彩色喷墨\ 铜版纸胶装\ 封面封底分别为pdf首页尾页+不在内页再次出现.pdf"
output_file_path = "tmp/auto.pdf" # 默认在代码所在文件夹

input_file_path = formatDraggedpath(input_file_path)
output = PdfFileWriter()
pdf_file = PdfFileReader(open(input_file_path, "rb"))
pdf_pages_len = pdf_file.getNumPages()
pagesToDelete = [2,3,6,7]

pagesToDelete = [page-1 for page in pagesToDelete]
for i in range(pdf_pages_len):
    if i not in pagesToDelete:
        output.addPage(pdf_file.getPage(i)) # (pages begin at zero)
 
outputStream = open(output_file_path, "wb")
output.write(outputStream)