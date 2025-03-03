Feature:
  Scenario: Create and save all measures
    Given launch dqlabs home page
    When login using credentials from JSON for conditional measures creation
    Then switch to assets main page
    Then click list view page
    Then select icon to search
    Then enter "customer" in the search area
    Then select the asset to add conditional measure
    Then click on add button to create conditional measure
    Then enter "FirstName" in the attribute area
    Then enter "contains" in the condition area
#    Then select attribute value "FirstName"
#    Then select condition value "contains"