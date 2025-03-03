Feature:
  Scenario: Create and save all measures
    Given open dqlabs home page
    When login using credentials from JSON for measures creation
    Then navigate to assets main page
    Then select list view page
    Then click on icon to search
    Then enter "customer" in the search box
    Then select asset to add measures
    Then click on add button to create measures
#    Then select attribute value "FirstName"
#    Then select condition value "contains"
    Then select query measure
    Then enter_measure_name"test1"
    Then provide_query "SELECT COUNT(*) AS COUNT FROM [dqlabs].[CustomerAI].[Customer] WHERE   (cast([FirstName] as nvarchar(MAX)) like '%a%')"