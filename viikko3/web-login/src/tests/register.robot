*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kornyo
    Set Password  kornyo99
    Set Password Confirmation  kornyo99
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ko
    Set Password  kornyo99
    Set Password Confirmation  kornyo99
    Submit Credentials
    Page Should Contain  Username must be at least 3 letters long

Register With Valid Username And Too Short Password
    Set Username  korn
    Set Password  kor99
    Set Password Confirmation  kor99
    Submit Credentials
    Page Should Contain  Password must be at least 8 characters long and cannot contain only letters

Register With Valid Username And Invalid Password
    Set Username  korn
    Set Password  kornyolo
    Set Password Confirmation  kornyolo
    Submit Credentials
    Page Should Contain  Password must be at least 8 characters long and cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kornyo
    Set Password  kornyo99
    Set Password Confirmation  kornyo98
    Submit Credentials
    Page Should Contain  Password and confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  moro9999
    Set Password Confirmation  moro9999
    Submit Credentials
    Page Should Contain  User with username kalle already exists

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page