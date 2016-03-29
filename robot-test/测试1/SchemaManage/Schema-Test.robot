*** Settings ***
Library           HttpLibrary.HTTP
Resource          ../../restful-api-test.txt
Variables         ../../var.py
Resource          ../../utils.txt

*** Variables ***
${entity_addr}    schemamanage/schema
${invalid_id}     999999999999

*** Test Cases ***
add
    ${abc}    Generate Random String    8    ffewttyjtyutuyryr345
    ${request_body}    Set Variable    {"schemaName":"autotest${abc}","schema":"456","description":"12323sdfsdfsdfasdf","schemaGroup_id":1}
    ${result}    Add Entity By Json    ${host}    ${site}    ${entity_addr}    ${request_body}
    ${new_schema_id}    Get Json Value    ${result}    /id
    Set Suite Variable    ${new_schema_id}

delete
    Variable Should Exist    ${new_schema_id}    准备删除的ID不存在
    Delete Entity    ${host}    ${site}    ${entity_addr}    ${new_schema_id}
