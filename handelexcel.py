import openpyxl


def loadexcel():
    print("load execel train.xlsx")
    wb = openpyxl.load_workbook("train.xlsx")
    trainsht = wb.get_sheet_by_name("train")
    maxrow = trainsht.max_row
    maxcol = trainsht.max_column
    tup = [[]]
    index = 0
    for row_ in range(2,maxrow+1):

        fname = trainsht.cell(row = row_, column = 3 ).value
        fdate = trainsht.cell(row = row_, column = 1 ).value
        for col_ in range (4, maxcol+1):
            tup_ = []
            if row_ -2 == 0 or ((row_ -2) % 18 ) == 0:
                tup_.append(fdate)
                tup_.append("Hour " + str(col_ - 4 ))
                tup_.append(trainsht.cell(row = row_, column = col_ ).value)
                tup.append(tup_)
            else:
                tup[index * 24 + (col_ -3) ].append(trainsht.cell(row = row_, column = col_ ).value)


        if row_ !=2 and ((row_ - 1) % 18) == 0:
            index = index + 1
    del tup[0]
    print(tup)
    return tup






