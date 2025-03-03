Feature: Lookup measure

  Scenario: Lookup
    Given Launch Chrome browser
    When Open the application homepage
    Then Enter valid credentials and log in
    Then Click on login
    When Navigate to libraries
    Then Create new library
    Then Navigate to the assets
    When Click on the search
    When Search for a specific asset by name
    Then Click on the selected asset
    When Click on add icon
    Then Navigate to Lookup tab
    Then Enter the measure name
    When Select a lookup type
    When Click on add_icon
    Then Select lookup value
    Then Click on save button