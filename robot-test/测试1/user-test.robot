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
