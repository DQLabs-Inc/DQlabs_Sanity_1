Feature: Deleting an asset
  Scenario: delete the asset when not required
#    Given launch chrome browser
    When Open DQ labs home page for asset delete
    Then login using credentials from JSON file for asset deletion
    Then navigate to assets page
    Then select list view
    Then click on search icon
    Then enter "customer" in the search asset
    Then select to delete asset
    Then click more icon
    Then select delete icon
    Then confirm delete asset
    #And close the browser