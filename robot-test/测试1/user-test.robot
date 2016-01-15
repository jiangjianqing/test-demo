*** Settings ***
Library           HttpLibrary.HTTP
Resource          ../restful-api-test.robot

*** Variables ***
${useraddr}       /${site}/user
${host}           localhost:8181
${site}           webui.springdm.springsecurity

*** Test Cases ***
user_notfound
    Entity Not Found    ${host}    ${site}    user    9999999

user_found
    Entity Found    ${host}    ${site}    user    1
