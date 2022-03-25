import pandas as pd

class Excel:
    def __init__(self, path):
        self.excelDF = pd.read_excel(path)
        self.excelColList = self.excelDF.columns.values.tolist()

    def getColList(self):
        return self.excelColList