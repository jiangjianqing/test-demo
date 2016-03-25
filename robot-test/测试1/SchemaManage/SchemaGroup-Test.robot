*** Settings ***
Library           HttpLibrary.HTTP
Resource          ../../restful-api-test.txt
Variables         ../../var.py
Resource          ../../utils.txt

*** Variables ***
${entity_addr}    schemamanage/schemagroup
${invalid_id}     99999999

*** Test Cases ***
schemagroup_add_by_json
    ${abc}    Generate Random String    8    ffewttyjtyutuyryr345
    ${request_body}    Set Variable    {"groupName":"new up323 ${abc}","description":"自动化测试添加的内容"}
    ${result}    Add Entity By Json    ${host}    ${site}    ${entity_addr}    ${request_body}
    ${new_schemagroup_id}    Get Json Value    ${result}    /id
    Set Suite Variable    ${new_schemagroup_id}

schemagroup_delete
    Variable Should Exist    ${new_schemagroup_id}    准备删除的ID不存在
    Delete Entity    ${host}    ${site}    ${entity_addr}    ${new_schemagroup_id}
