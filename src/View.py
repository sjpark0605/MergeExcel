from tkinter import Tk, Label, Frame, OptionMenu, StringVar, Listbox, Button, MULTIPLE, END

from Handlers import extractCommonCol

class View:
    def __init__(self, dimension):
        self.root = Tk()
        self.root.title("엑셀 병합 프로그램")
        self.root.resizable(False, False)
        self.root.geometry(dimension)
        self.pathMap = {}
        self.listBoxMap = {}
        self.excelMap = {}

    def run(self):
        self.root.mainloop()

    def addField(self, labelContent, buttonText, action, row):
        fieldLabel = self.__generateFieldLabel(labelContent)
        pathFrame = self.__generateFrame()
        pathLabel = self.__generatePathLabel(pathFrame)
        button = self.__generateButton(buttonText, lambda: self.__fdClickHandler(labelContent, action, pathLabel))
        self.__renderFieldElements(fieldLabel, pathFrame, pathLabel, button, row)

    def addRunButton(self, row):
        print(row)

    def __renderFieldElements(self, fieldLabel, pathFrame, pathLabel, button, row):
        fieldLabel.grid(row = row, column = 0)
        pathFrame.grid(row = row, column = 1)
        pathLabel.pack()
        button.grid(row = row, column = 2)

    def __fdClickHandler(self, fileType, action, pathLabel):
        selectedPath, excelDF = action()
        
        if selectedPath == "":
            return

        self.pathMap[fileType] = selectedPath
        self.excelMap[fileType] = excelDF

        pathLabel.config(text = selectedPath)

        if len(self.excelMap) == 2:
            colList1 = self.excelMap["엑셀 파일 1"].getColList()
            colList2 = self.excelMap["엑셀 파일 2"].getColList()
            commonColList = extractCommonCol(colList1, colList2)

            if len(commonColList) > 0:
                self.__enableColSelectors(commonColList, colList1, colList2)
            else:
                # SHOW INFO
                print("No Common Columns")

    def __addColDropdown(self, labelContent, commonColList, row):
        fieldLabel = self.__generateFieldLabel(labelContent)
        dropdown = self.__generateDropdown(commonColList)

        self.__renderDropdown(fieldLabel, dropdown, row)

    def __addColSelector(self, labelContent, excelType, row):
        fieldLabel = self.__generateFieldLabel(labelContent)
        listBox = self.__generateListbox()
        self.listBoxMap[excelType] = listBox
        self.__renderSelector(fieldLabel, listBox, row)

    def __enableColSelectors(self, commonColList, colList1, colList2):
        self.__addColDropdown("기준 열", commonColList, 2)
        self.__addColSelector("포함할 열 1", "엑셀 파일 1", 3)
        self.__addColSelector("포함할 열 2", "엑셀 파일 2", 4)

        for col in colList1:
            self.listBoxMap["엑셀 파일 1"].insert(END, col)
        for col in colList2:
            self.listBoxMap["엑셀 파일 2"].insert(END, col)

    def __renderDropdown(self, fieldLabel, dropdown, row):
        fieldLabel.grid(row = row, column = 0)
        dropdown.grid(row = row, column = 1)

    def __renderSelector(self, fieldLabel, listBox, row):
        fieldLabel.grid(row = row, column = 0)
        listBox.grid(row = row, column = 1)

    def __generateFieldLabel(self, labelContent):
        return Label(
            self.root,
            text = labelContent,
            padx = 5,
            pady = 3
        )

    def __generateFrame(self):
        return Frame(
            self.root,
            bg = "black",
            padx = 1,
            pady = 1
        )

    def __generatePathLabel(self, frame):
        return Label(
            frame,
            bg = "white",
            width = 50
        )

    def __generateDropdown(self, commonColList):
        variable = StringVar(self.root)
        variable.set(commonColList[0])
        return OptionMenu(
            self.root,
            variable,
            *commonColList
        )

    def __generateListbox(self):
        return Listbox(
            self.root, 
            selectmode=MULTIPLE, 
            height=4,
            width=50
        )

    def __generateButton(self, text, action):
        return Button(
            self.root,
            text = text,
            command = action,
            padx = 10
    )