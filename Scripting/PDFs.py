import time

import PyPDF2 as py
import sys
input=sys.argv[1:]
water_mark=py.PdfFileReader(open(r'C:\Users\614785.old\PycharmProjects\Udemp_Practice\PDF/wtr.pdf','rb'))
water_mark_pg=water_mark.getPage(0)
output=py.PdfFileWriter()
def pdf_combiner(list1):
    merger=py.PdfFileMerger()
    for pdf in list1:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

def water_mark_merger():
    main_file = py.PdfFileReader(open(r'C:\Users\614785.old\PycharmProjects\Udemp_Practice/super.pdf', 'rb'))
    for i in range(main_file.getNumPages()):
        page=main_file.getPage(i)
        page.mergePage(water_mark_pg)
        output.addPage(page)

    with open("final_watermarkedfile.pdf",'wb') as file2:
        output.write(file2)


pdf_combiner(input)
time.sleep(20)
water_mark_merger()
