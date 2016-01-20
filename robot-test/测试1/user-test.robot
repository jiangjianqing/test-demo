*** Settings ***
Library           HttpLibrary.HTTP
Resource          ../restful-api-test.txt
Variables         ../var.py

*** Variables ***
${invalid_userid}    9999999

*** Test Cases ***
user_notfound
    Entity Not Found    ${host}    ${site}    user    ${invalid_userid}

user_found
    Entity Found    ${host}    ${site}    user    1

user_add
    [Documentation]    使用常规的POST提交，标记为deprecated
    [Tags]    deprecated
    ${request_body}    Set Variable    username=中文测试&password=111111
    Add Entity    ${host}    ${site}    user    ${request_body}

用户名重复
    Entity Replicated    ${host}    ${site}    user    1

user_add_by_json
    ${request_body}    Set Variable    {"username":"1123","password":456}
    Add Entity By Json    ${host}    ${site}    user    ${request_body}

user_delete
    Delete Entity    ${host}    ${site}    user    15
