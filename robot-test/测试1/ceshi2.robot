*** Settings ***
Library           HttpLibrary.HTTP

*** Test Cases ***
test_http
    Create Http Context    localhost:8181
    ${base_addr}    Set Variable    /webui.springdm.springsecurity/user/1
    GET    ${base_addr}
    ${response_status}=    Get Response Status
    Should Start With    ${response_status}    200
    ${user}=    Get Response Body
    ${utf8_test}    Set Variable    中文
