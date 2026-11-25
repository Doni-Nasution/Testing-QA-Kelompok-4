*** Settings ***
Documentation     Test Interface Layer (Web), SPIKE D04.
...               Keyword low-level (simple). Navigation = aksi input, Verification = pengecekan output.
...               Tidak berisi logika bisnis (itu tugas Domain Layer, D07/D10).
...               Catatan: bila SeleniumLibrary ikut di-import di suite yang sama, nama
...               "Click Element" bisa membingungkan; proyek ini memakai Browser library.
Library           Browser    auto_closing_level=SUITE

*** Variables ***
${BASE_URL}       https://wave-projects-center-id.vercel.app
${HEADLESS}       ${True}
${TIMEOUT}        30s

*** Keywords ***
Open Page
    [Documentation]    [Navigation] Membuka browser lalu halaman tertentu.
    ...    Parameter: url (default ${BASE_URL}); browser (default chromium); headless (default ${HEADLESS}).
    [Arguments]    ${url}=${BASE_URL}    ${browser}=chromium    ${headless}=${HEADLESS}
    New Browser    browser=${browser}    headless=${headless}
    New Context    viewport={'width': 1280, 'height': 720}
    Set Browser Timeout    ${TIMEOUT}
    New Page    ${url}

Input Text Into Field
    [Documentation]    [Navigation] Mengosongkan lalu mengisi sebuah field. TIDAK mengirim/submit.
    ...    Parameter: locator (wajib); text (wajib).
    [Arguments]    ${locator}    ${text}
    Fill Text    ${locator}    ${text}

Click Element
    [Documentation]    [Navigation] Mengklik sebuah elemen.
    ...    Parameter: locator (wajib), selector Browser, mis. css=a[href$="/chat"] >> nth=0
    [Arguments]    ${locator}
    Click    ${locator}

Verify URL Contains
    [Documentation]    [Verification] Memastikan URL saat ini memuat potongan teks yang diharapkan.
    ...    Parameter: expected (wajib).
    [Arguments]    ${expected}
    Get Url    *=    ${expected}

Verify Field Has Value
    [Documentation]    [Verification] Memastikan nilai sebuah field sama dengan yang diharapkan.
    ...    Parameter: locator (wajib); expected (wajib).
    [Arguments]    ${locator}    ${expected}
    Get Property    ${locator}    value    ==    ${expected}
