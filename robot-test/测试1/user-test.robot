*** Settings ***
Library           HttpLibrary.HTTP
Resource          ../restful-api-test.txt

*** Variables ***
${invalid_userid}    9999999
${host}           localhost:8181
${site}           webui.springdm.springsecurity

*** Test Cases ***
user_notfound
    Entity Not Found    ${host}    ${site}    user    ${invalid_userid}

user_found
    Entity Found    ${host}    ${site}    user    1
