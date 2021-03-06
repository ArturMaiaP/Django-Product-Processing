# Created by artur at 22/10/2020
Feature: New rule
  Create a new rule and process all products

  Scenario: Valid Form
    Given I want to add a new rule with the field "cor"
    And With the value "marrom"
    When I save the rule
    Then I should see the rule registered on the database


  Scenario: Invalid Form
    Given I want to add a new rule with the field "cor"
    And With the value " "
    When I save the rule
    Then The system should return the message: "Form invalid. Please, try again!"