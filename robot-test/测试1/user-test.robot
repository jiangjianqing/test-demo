*** Settings ***
Library           HttpLibrary.HTTP
Resource          ../restful-api-test.txt
Variables         ../var.py

*** Variables ***
${invalid_userid}    9999999
${entity_addr}    usermanage/user

*** Test Cases ***
user_notfound
    ${result}    Entity Not Found    ${host}    ${site}    ${entity_addr}    ${invalid_userid}
    ${key}    Get Json Value    ${result}    /key
    Run Keyword If    ${key}<>${invalid_userid}    FAIL    查询的id与返回的key不相同

user_found
    ${body}    Entity Found    ${host}    ${site}    ${entity_addr}    1
    ${id}    Get Json Value    ${body}    /id
    Run Keyword If    ${id}==0    Fail    id必须大于0

user_add
    [Documentation]    使用常规的POST提交，标记为deprecated
    [Tags]    deprecated
    ${request_body}    Set Variable    username=中文测试&password=111111
    Add Entity    ${host}    ${site}    ${entity_addr}    ${request_body}

user_duplicated
    ${username}    Generate Random String    15
    ${request_body}    Set Variable    {"username":"${username}","password":"test"}
    Entity Duplicated    ${host}    ${site}    ${entity_addr}    ${request_body}

user_add_by_json
    ${request_body}    Set Variable    {"username":"1123","password":456}
    ${result}    Add Entity By Json    ${host}    ${site}    ${entity_addr}    ${request_body}
    ${new_user_id}    Get Json Value    ${result}    /id
    Set Suite Variable    ${new_user_id}

user_delete
    Variable Should Exist    ${new_user_id}    准备删除的ID不存在
    Delete Entity    ${host}    ${site}    ${entity_addr}    ${new_user_id}

Default Page
    Default Page    ${host}    ${site}    ${entity_addr}

user_validate_failed
    ${request_body}    Set Variable    {"username":"1","password":456}
    ${result}    Entity Validate Failed    ${host}    ${site}    ${entity_addr}    ${request_body}

modify
    ${random_name}    Generate Random String    8    ffewttyjtyutuyryr345
    ${request_body}    Set Variable    {"username":"1123${random_name}","password":4567890}
    ${result}    Add Entity By Json    ${host}    ${site}    ${entity_addr}    ${request_body}
    ${new_user_id}    Get Json Value    ${result}    /id
    ${extendinfo_jsonstr}    Stringify Json    {"extendInfo":{"address":"测试地址","testField":"这是我的测试字段"}}
    ${request_body}    Set Variable    {"id":${new_user_id},"username":"12323423","password":"234234234","extendInfo":${extendinfo_jsonstr}}
    ${result}    Modify Entity    ${host}    ${site}    ${entity_addr}    ${new_user_id}    ${request_body}
    Delete Entity    ${host}    ${site}    ${entity_addr}    ${new_user_id}
