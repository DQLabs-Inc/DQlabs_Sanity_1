Feature: Adding a new source connection

  Scenario: Login and add a new source connection
    #Given launch chrome browser
    When Open DQ labs home page
    Then login using credentials from JSON
    Then click on the profile icon
    Then navigate to settings
    Then open options icon
    Then connect drop down
    Then select source option
    Then click on the add new connections
    Then click on the search icon
    Then enter "mssql" in the search field
    Then select the mssql source
    Then enter connection name
#    Then enter server details
#    Then enter database details
#    Then enter user name
#    Then enter port id
#    Then enter password
    Then click on the validate option
    Then enter schema name
    Then click on the connect option
    Then click on the search button
    Then enter "customer" in the search name
    Then select table check
    Then click on connect button
    And close the browser



