import openpyxl
wb=openpyxl.load_workbook('Test.xlsx')
#print(wb.sheetnames)
#print('***********')
k=[]
sheet=wb['Sheet1']
cell=sheet['A1']
print(cell.value)

