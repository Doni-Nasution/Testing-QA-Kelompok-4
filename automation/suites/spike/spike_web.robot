*** Settings ***
Documentation     SPIKE D04: validasi keyword Open, Input, Click pada SUT Wave Projects.
...               Hanya baca dan ketik. Tidak ada pesan dikirim, tidak ada transaksi.
Resource          ../../resources/interface/web.resource
Suite Teardown    Close Browser

*** Variables ***
${NAV_CHAT}       css=a[href$="/chat"] >> nth=0
${CHAT_INPUT}     css=input[placeholder="Ceritakan proyek impian Anda..."]
${SAMPLE_TEXT}    Halo, ini uji otomatis QA (tidak dikirim)

*** Test Cases ***
SPIKE-01 Open Page Shows Home
    [Tags]    spike    navigation
    Open Page
    Verify URL Contains    wave-projects-center-id.vercel.app

SPIKE-02 Click Element Navigates To Chat
    [Tags]    spike    navigation
    Click Element    ${NAV_CHAT}
    Verify URL Contains    /chat

SPIKE-03 Input Text Into Field Fills Chat Input
    [Tags]    spike    navigation
    Input Text Into Field    ${CHAT_INPUT}    ${SAMPLE_TEXT}
    Verify Field Has Value    ${CHAT_INPUT}    ${SAMPLE_TEXT}
    Take Screenshot
