# SolarApp

The purpose of this project is to retrieve the cloud coverage of tomorrows sunrise to 12pm using the API from WeatherAPI.com. Based on this data an API call will be made to FoxESS cloud to change the force battery times to one that makes more sense in regards to how effective the charge will be in the morning.
The intended usecase is quite niche as one needs to have a solar panel array and have a FoxESS system site. It's only really useful if the user gains cheaper charge times during offpeak hours (such as Octupus energy flex plan)

# Requirements

`pip install` requirements.txt

Users need an .env file which needs the following variables

`API_KEY`  
`LATITUDE`  
`LONGITUDE`
