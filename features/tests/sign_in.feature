# Created by porter at 6/17/25
Feature: SignIn tests

  Scenario: 'Verify user can sign in'
    Given Open Target page
    When Click Sign In
    When Click Sign In from side nav menu
    Then Verify Sign in form opens