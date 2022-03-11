# Covid-19 and Travel Safety 

Access travel Restriction data for over 200 countries

[Keep Travelers informed with Amadeus Travel Restriction API ](https://developers.amadeus.com/blog/-introducing-amadeus-covid-19-travel-restrictions-api)

Powered by [Riskline](https://riskline.com/), the travel restrictions data is updated every hour to so you can keep your travelers informed of the latest developments on their trip. 

## Search by an area
the [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions) can be searched by a country, city or region. 
 
```bash
curl https://test.api.amadeus.com/v1/duty-of-care/diseases/covid19-area-report?countryCode=KR&cityCode=SEL
```

!!! information
    Country code(2 letters code) is defined in [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) and city code(3 letters code) is defined in [IATA](https://www.iata.org/en/publications/directories/code-search/), which you can also use [Amadeus Airport & City Search API](https://developers.amadeus.com/self-service/category/air) to get.


## Get Covid-19 statistics 
the result provides Covid-19 Statstics such as total cases, active cases, and current rate of infection per 100,000 

```json
"diseaseCases": {
                            "confirmed": 32940846,
                            "deaths": 585970,
                            "recovered": 0,
                            "active": 32354876,
                            "date": "2021-05-06"
                          },
                          "hotspots": "<p>Minnesota, Michigan, Pennsylvania, New Jersey, Delaware, New York, Connecticut, Rhode Island, New Hampshire, Vermont, Massachusetts</p>",
                          "dataSources": {
                            "governmentSiteLink": "https://www.cdc.gov/coronavirus/2019-ncov/index.html",
                            "healthDepartmentSiteLink": "https://www.helsenorge.no/en/coronavirus/"
                          },
```

## Get Travel Restrictions information

## Get Entry Requirements

## Get Local Guidance

## Get Safety information
