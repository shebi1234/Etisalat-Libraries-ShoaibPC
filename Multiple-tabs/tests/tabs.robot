*** Settings ***
Library  Selenium2Library
Library  Collections

*** Tasks ***
Manipulate Multiple Windows
    [Tags]    MultiWindow
    Open Browser  https://elemental.medium.com/  chrome
    maximize browser window
    ${Window1Title} =  get title
    log to console  ${Window1Title}
    wait until page contains  Medium  10s
    Click Element  //*[@class="svgIcon svgIcon--twitterFilled svgIcon--25px"]
    Comment  This is a new Window
    Sleep  5s
    Select Window  Elemental by Medium (@elemental) | Twitter
    Comment  Go back to the first window
    Sleep  5s
    select window  title=${Window1Title}
   Close Browser





#    add image path  E:/RobotFramework/Multiple-tabs/images
#    right click  //a[text()='Elemental']
#    sikulilibrary.click element  new-tab.png
#    wait until page contains  Rebot
#    click element  //a[text()='Rebot']
#    Comment  This is a new Window
#    Sleep  5s
#    Select Window  Title=Robot Framework documentation
#    wait until page contains  Built-in tools
#    Click Element  //button[@value='BuiltIn']
#    Sleep  5s
#    Select Window  Title=Builtin
#    ${windowtoopen} =  get from list  ${Window1Title}  -1
#    Page Should Contain Element  link=Builtin