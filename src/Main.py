from View import View
from Handlers import *

GUI = View("600x300")

GUI.addField("엑셀 파일 1", "불러오기", onExcelButtonClick, 0)
GUI.addField("엑셀 파일 2", "불러오기", onExcelButtonClick, 1)
# GUI.addColSelector("포함할 열 1", "엑셀 파일 1", 2)
# GUI.addColSelector("포함할 열 2", "엑셀 파일 2", 3)

GUI.run()