import openpyxl

wb = openpyxl.load_workbook("train.xlsx")
trainsht = wb.get_sheet_by_name("train")
