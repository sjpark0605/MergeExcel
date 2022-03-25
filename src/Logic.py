import pandas as pd
from Excel import Excel

firstExcel = Excel('input.xlsx')

print(firstExcel.getColList())