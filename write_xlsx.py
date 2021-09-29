from openpyxl import Workbook
wb = Workbook()
ws = wb.active
#ws['A1'] = "Name"
testdata =[["Name","Contact Number"],["Sabbir","01714324598"],["Sunve","+880 1677-196458"],["Prionty","0184234587"]]
for data in testdata:
    ws.append(data)
wb.save("excel.xlsx")
