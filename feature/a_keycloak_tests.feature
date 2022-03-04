Feature: Tests with keycloak

  # 3 Юзер с неподтвержденной почтой не может зайти в ЛК через keycloak
#  Scenario: User with unconfirmed mail cannot log in to the personal account via Keycloak
#    When I visit page "http://217.9.89.223"
#    When Button click by element By XPATH: "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button"
#    When Check redirect to (enter first url part) Url: "https://esiatest.mai.ru/auth/realms/demo/"
#    When Input Text: "test_user_13@inbox.ru" element By ID: "username"
#    When Input Text: "2ij-4ZR-Lpt-yhS" element By ID: "password"
#    And Button click by element By ID: "kc-login"
#    And Sleep "5" sec
#    When Find text on page Text: "Подтверждение адреса E-mail" element By ID: "kc-page-title"
#    And Sleep "5" sec

#  1 Юзер без гражданства пытается попасть на страницу personal
  Scenario: A stateless user is trying to get to the personal page
    When I visit page "http://217.9.89.223"
    When Button click by element By XPATH: "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button"
    When Check redirect to (enter first url part) Url: "https://esiatest.mai.ru/auth/realms/demo/"
    When Input Text: "r-38@mail.ru" element By ID: "username"
    When Input Text: "eqE-8M4-cx5-ser" element By ID: "password"
    And Button click by element By ID: "kc-login"
    And Sleep "2" sec
    When I visit page "http://217.9.89.223/applicants/"
    And Sleep "2" sec
    When Check redirect to (enter first url part) Url: "http://217.9.89.223/applicants/citizenship"
    And Sleep "15" sec
#    When Find text on page Text: "Подтверждение адреса E-mail" element By ID: "kc-page-title"
#    And Sleep "5" sec
