*** Settings ***
Library  ../Libraries/MergeExcelFileLibrary.py
Library  BuiltIn
Library  Collections
Library  ../Libraries/variables.py

#*** Variables ***
#${dir}  E:/ExcelFiles
#${merge_file_path}  E:/ExcelFiles/mergedfile.xlsx
#*** Keywords ***


*** Test Cases ***
Merge Excel File
    ${dir} =  variable1
    log to console  ${dir}
    ${merge_file_path} =  variable2
    log to console  ${merge_file_path}
    ${File} =  excel_file_merge  ${dir}  ${merge_file_path}


