*** Settings ***
Library  ../libraries/send_email.py
Library  ../libraries/RowsCount.py
Library  ../libraries/Variables.py

*** Variables ***
${TotalCount}

*** Test Cases ***
Sending Email
    ${filepath} =  variable1
    ${TotalCount} =  rowscount  ${filepath}
    log to console  ${TotalCount}
    send_email_file  ${TotalCount}
    log to console  ${TotalCount}

