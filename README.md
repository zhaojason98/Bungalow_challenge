# Bungalow_challenge
Bungalow Backend challenge

# Models
House:
  - Contains unique zillow_id(id) and foriegn keys for grouped information
  
Description:
  - Contains all user description involving house
  
Price:
  - Contains information on price of said house

Estimate:
  - All estimated values

Tax:
  - All tax information on the specific house

Location:
  - Location information of the house

# Content
views - returns specific information following unique zillow_id
various getter for model properties

# Migrations
Read csv row by row and populate models based off column
