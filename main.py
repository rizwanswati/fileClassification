import pandas as pd
import os
import shutil as moveTheDamnFilesMan

import numpy as np

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# dirPath = 'C:/Users/ACER/Desktop/data/maligTrue'
# source = 'C:/Users/ACER/Desktop/data/class/'
# destination = 'C:/Users/ACER/Desktop/data/maligTrue/'


def DoTheStuffForMe():
    print("Must Include '/' At the End of Directory Name")
    excelFilePath = input("Input Excel File Path::Formate ==> C:/path/to/directory/filename.xlsx :")
    ddiFilePath = input("Input DDI path::C:/path/to/DDIFolder/: ")
    dataSheet = input("Input Data Sheet Name: ")
    newDirName = input("Input New Directory Path::Formate ==> C:/path/to/ParentDirectory/NewDirctory/ :")
    fileNameCol = input("input DDI File name column :")
    trueFalse = input("Input True False Column Name :")

    prem = pd.ExcelFile(excelFilePath).parse(dataSheet)

    DDI = []
    DDI_File = {}
    Malignant = []
    index = 0

    DDI.append(prem[fileNameCol])
    Malignant.append(prem[trueFalse])

    for ddi_names in DDI[0]:
        name = ddi_names
        boolVal = Malignant[0][index]
        if boolVal == True:
            DDI_File[name] = boolVal
        index = index + 1
    try:
        if os.path.exists(newDirName):
            print('directory already exists')
        else:
            os.mkdir(newDirName)
    except OSError as error:
        print(error)

    for files in DDI_File:
        moveTheDamnFilesMan.move(ddiFilePath + files, newDirName + files)


DoTheStuffForMe()