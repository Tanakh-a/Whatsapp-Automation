from openpyxl import Workbook


class dataWrite():
    wb = Workbook()
    ws = wb.active
    testData = [["Name", "Contact Number"], ["Krishty", "01710-653123"], ["Sunve", "+880 1677196458"],
                ["Prionty whatsapp", "01738564691"]]
    for data in testData:
        ws.append(data)
    wb.save("excel.xlsx")
