Feature: SignUp Page

  As a new CICOD customer
  I should be able to SignUp
  So that I can perform transactions.

  Background:
    Given I am on the CICOD Page

  Scenario: User with valid credentials can SignUp successfully.
    When I click on "SignUp"
    And I insert the "Email"
    And I insert the "phone number"
    And I insert the "business name"
    And I click on "Next"
    And I click on "a Plan"
    And I click on "Next Button"
    And I select an info from the list
    And I click on "Terms of use"
    And I click on "Start free trial"
    Then I should see a message display telling me to go and verify my account from my Email