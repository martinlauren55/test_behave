Feature: authorization

  Scenario: open lk page and authorization
#    Given lunched chrome browser
    When open site lk
    And click on btn "Войти"
    Then I should be redirected to keykloak authorization
    And I should be see "Вход в учетную запись"
#    And close browser

#  Scenario: authorization with keykloak
#    Given lunched chrome browser
#    When open site lk
#    And click on btn "Войти"
#    Then I should be redirected to keykloak authorization
#    And I should be see "Вход в учетную запись"
#    And close browser