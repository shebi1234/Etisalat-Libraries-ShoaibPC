*** Settings ***
Library  Selenium2Library

*** Variables ***
${url}  https://www.facebook.com/
*** Test Cases ***
Opening Browser
#    [Arguments]    ${url}
#    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
#    Call Method    ${chrome_options}    add_argument    test-type
#    Call Method    ${chrome_options}    add_argument    --disable-infobars
#    Run Keyword If    os.sep == '/'    Create Webdriver    Chrome    my_alias    chrome_options=${chrome_options}    executable_path=/usr/lib/chromium-browser/chromedriver
#    ...    ELSE    Create Webdriver    Chrome    my_alias    chrome_options=${chrome_options}
#    Go To    ${url}

    ${options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    ${excluded}    Create List    enable-automation
    Call Method    ${options}    add_experimental_option    useAutomationExtension  ${False}
    Call Method    ${options}    add_experimental_option    excludeSwitches    ${excluded}
    create webdriver  Chrome  chrome_options=${options}
    go to  ${url}
    Maximize Browser Window




