from tkinter import filedialog as fd
from Excel import Excel

def extractCommonCol(colList1, colList2):
    result = []

    for col in colList1:
        if col in colList2:
            result.append(col)

    return result

def onExcelButtonClick():
    filetypes = (
        ('엑셀 파일', '.xls .xlsx'),
        ('모든 파일', '*.*')
    )

    selectedPath = fd.askopenfilename(
        title = "엑셀 파일 불러오기",
        initialdir = '/',
        filetypes = filetypes
    )

    if (selectedPath != ""):
        excel = Excel(selectedPath)
    else:
        excel = None

    return selectedPath, excel

