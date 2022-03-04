Feature: lk_authorization

#  Background: common steps
#    When I visit page "http://217.9.89.223"
#    And Click on btn "Войти"
#    Then I should be redirected to Keycloak authorization link started with "https://esiatest.mai.ru/auth/realms/demo/"
#    And I should be see title "Вход в учетную запись"

  Scenario: authorization on Keycloak
#    When I fill email "test_user_13@inbox.ru" and password "2ij-4ZR-Lpt-yhS"
#    And Click on Keycloak btn "Войти"

#    When Open page Url: "http://217.9.89.223/accounts/login"
#    When Sleep "5" sec
#    When Click on Button name: "Войти" element By.XPATH: "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button"
#    When Check redirect to (enter first url part) Url: "https://esiatest.mai.ru/auth/realms/demo"
#    When Find text on page Text: "Вход в учетную запись" element By.ID: "kc_loginAccountTitleForm"
#    When Input Text: "test123" element By.ID: "username"
#    When Input Text: "213" element By.ID: "password"
#    When Click on Button name: "Войти" element By.XPATH: "/html/body/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[3]/div/input[2]"
##    When Click on Button name: "Войти" element By.ID: "kc-login"
#    When Sleep "10" sec

    When Open page Url: "https://esiatest.mai.ru/auth/realms/demo/account/"
    When Sleep "3" sec
#    When Button click by element By.XPATH: "/html/body/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[3]/div/input[2]"
    When Button click by element By.ID: "kc-login"
    When Sleep "5" sec