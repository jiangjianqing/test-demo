*** Settings ***
Library           HttpLibrary.HTTP
Resource          ../restful-api-test.txt
Variables         ../var.py

*** Variables ***
${invalid_userid}    9999999
${user_addr}      usermanage/user

*** Test Cases ***
user_notfound
    Entity Not Found    ${host}    ${site}    ${user_addr}    ${invalid_userid}

user_found
    Entity Found    ${host}    ${site}    ${user_addr}    1

user_add
    [Documentation]    使用常规的POST提交，标记为deprecated
    [Tags]    deprecated
    ${request_body}    Set Variable    username=中文测试&password=111111
    Add Entity    ${host}    ${site}    ${user_addr}    ${request_body}

用户名重复
    Entity Replicated    ${host}    ${site}    ${user_addr}    1

user_add_by_json
    ${request_body}    Set Variable    {"username":"1123","password":456}
    ${result}    Add Entity By Json    ${host}    ${site}    ${user_addr}    ${request_body}
    ${new_user_id}    Get Json Value    ${result}    /id
    Set Suite Variable    ${new_user_id}

user_delete
    Variable Should Exist    ${new_user_id}    准备删除的UserID不存在
    Delete Entity    ${host}    ${site}    ${user_addr}    ${new_user_id}
