*** Settings ***
Library  Selenium2Library

*** Variables ***
${URL}  https://www.facebook.com/
${BROWSER}  Chrome

*** Tasks ***
Check boxes
    Open Browser  ${URL}  ${BROWSER}
    maximize browser window
    wait until page contains  Create an account  30s
    Click Element  //input[@type='radio' and @value='2']
    close browser
