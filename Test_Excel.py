from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Test"
headers = ["a", "b"]
ws.append(headers)
data = [1, 2]
ws.append(data)
wb.save("test.xlsx")