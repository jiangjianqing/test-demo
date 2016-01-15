*** Settings ***
Library           HttpLibrary.HTTP

*** Keywords ***
Entity Found
    [Arguments]    ${host}    ${site}    ${entity_name}    ${entity_id}
    Create Http Context    ${host}
    ${base_addr}    Set Variable    /${site}/${entity_name}/${entity_id}
    GET    ${base_addr}
    ${response_status}=    Get Response Status
    Should Start With    ${response_status}    200
    ${user}=    Get Response Body
    ${test_status}    Set Variable    执行成功
    Log    执行成功

Entity Not Found
    [Arguments]    ${host}    ${site}    ${entity_name}    ${entity_id}
    Create Http Context    ${host}
    ${base_addr}    Set Variable    /${site}/${entity_name}/${entity_id}
    Next Request May Not Succeed
    GET    ${base_addr}
    ${response_status}=    Get Response Status
    Should Start With    ${response_status}    404
    ${user}=    Get Response Body
    ${test_status}    Set Variable    执行成功
