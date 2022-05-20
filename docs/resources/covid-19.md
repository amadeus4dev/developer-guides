# COVID-19 and Travel Safety 



"Can I travel to South Korea? Thailand? or Costa Rica? Do I need to have a PCR test? before the flight? after I arrive? How many days of quarantine are required? Where can I find this information?" 

Don't worry, with Amadeus Self-Service APIs, you will be able to have the details information of **number of COVID-19 cases, entry requirements, and safety scores, etc** with more details in a searched destinations with one single API.

And even more, **safety information** can be retrieved for the destination you would like to visit so that you will be aware of where you are heading to. 



## Search by an area

There are 2 APIs to achieve the information 

1. [Amadeus Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions) for COVID-19 related information 
2. [Amadeus Safe Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place) for Safety information



[Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions) can be searched **by a country, city, or region**. 

```bash
curl https://test.api.amadeus.com/v1/duty-of-care/diseases/covid19-area-report?countryCode=FR&cityCode=PAR
```
!!! information
    The country code(2 letters code) is defined in [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) and the city code(3 letters code) is defined in [IATA](https://www.iata.org/en/publications/directories/code-search/). You can also use [Airport & City Search API](https://developers.amadeus.com/self-service/category/air) to get this information. 



[Safe Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place) can be searched by a given location with **latitude, longitude and radius**, or **Square information** (North, West, South, and east) or **by id**.

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-locations?latitude=48.856614&longitude=2.3522219&radius=2
```

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-locations/Q930400878
```

!!! information 
    **The id** is given by your first query which has been searched by others. the search by id was designed to target a specific area that you want to focus on.



## Get information from responses
Let's highlight some information you get from both Travel Restrictions API and Safe Place API. 

!!! Warning
    Don't forget that Amadeus for Developers provides a `Test Environment` with [limited data collections](https://amadeus4dev.github.io/developer-guides/guides/api-data-collection/). 

!!! information
   - the data source of Travel Restrictions API is from [Riskline](https://riskline.com/) and it has been sourced from local governments and media. The quantity of information provided may vary from country to country. 
   - the data source of Safe Place API is from [GeoSure](https://geosureglobal.com/), GeoSafeScores algorithm which analyzes crime, health and economic data, official travel alerts, local reporting, and a variety of other sources. 
 

### Get summary of the destination + Safety score

From the response of Travel Restrictions API : 

```json
"area": {
            "name": "South Korea",
            "iataCode": "KR",
            "areaType": "Country"
        },
        "summary": "<p>Authorities have relied on gathering limits and social distancing measures to contain outbreaks since the start of the pandemic. A three-stage lifting of COVID-19 measures was underway but was paused in late November 2021 as a new spike in COVID-19 cases led to rises in deaths and those with severe symptoms, and threatened hospital beds and ICU availabilities. </p>",
        "diseaseRiskLevel": "High",
        "diseaseInfection": {
            "date": "2022-03-06",
            "level": "Extreme",
            "rate": 5088.42
```

From the response of Safe Place API, you will get an overall safety score and scores for six-component categories. 

- Women’s Safety 
- Health & Medical Safety 
- Physical Harm 
- Theft 
- Political Freedoms 
- LGBTQ+ Safety 

```json
            "subType": "CITY",
            "name": "Seoul",
            "geoCode": {
                "latitude": 37.566534999999995,
                "longitude": 126.97796899999999
            },
            "safetyScores": {
                "lgbtq": 45,
                "medical": 45,
                "overall": 35,
                "physicalHarm": 33,
                "politicalFreedom": 28,
                "theft": 44,
                "women": 34
            }
        }
```

**Safety scores range on a scale of 1-100, with 1 being the safest and 100 being the least safe.** In this example of Seoul, South Korea, a “politicalFreedom” score of 28 indicates that the potential for infringement of political rights or political unrest is less likely to happen at this location.  


### Get COVID-19 related statistics 

From the response of Travel Restrictions API: the result provides COVID-19 statistics such as total cases, active cases, and the current rate of infection per 100,000 

```json
        "diseaseCases": {
            "date": "2022-03-10",
            "deaths": 9875,
            "confirmed": 5822626
        },
        "hotspots": "<p>Seoul, Incheon, Gyeonggi province</p>",
        "dataSources": {
            "healthDepartementSiteLink": "http://www.kdca.go.kr/index.es?sid=a3",
            "governmentSiteLink": "http://ncov.mohw.go.kr/en/"
        },
```
And what is the vaccination ratio in this country?

```json
        "areaVaccinated": [
            {
                "date": "2022-02-27",
                "vaccinationDoseStatus": "oneDose",
                "percentage": 87.336
            },
            {
                "date": "2022-03-09",
                "vaccinationDoseStatus": "fully",
                "percentage": 86.56
            }
```


### Get Travel Restrictions information 

From the response of Travel Restrictions API : 
Entry information, which origin countries will be required for quarantine, entry Requirements, mask information, tracing application, and much more...

```json
            "entry": {
                "date": "2022-03-04",
                "text": "<p>All inbound non-resident foreign nationals must secure a visa before their travel. All travelers, including residents and Non- South Korean nationals, must hold a valid negative PCR test result to be allowed to board an inbound flight to South Korea. However, South Korean nationals who were found after entry with a non-conforming certificate must undergo a five days quarantine in a government-designated facility and an additional two days home quarantine.</p>",
                "ban": "No",
                "throughDate": "indef",
                "rules": "http://ncov.mohw.go.kr/duBoardList.do?brdId=2&brdGubun=23",
                "borderBan": [
                    {
                        "borderType": "maritimeBorderBan",
                        "status": "Closed"
                    },
                    {
                        "borderType": "landBorderBan",
                        "status": "Closed"
                    }
                ]
            },
```
```json
"diseaseTesting": {
                "date": "2022-03-04",
                "text": "<p><strong>Before travel</strong></p><p><strong>Pre-Travel Testing</strong></p>\n<p>All inbound travellers aged six or older, including South Korean nationals, must submit English or Korean certificates of negative results of COVID-19 tests (or English or Korean translations notarised by South Korean Embassies or Consulates) issued in paper. ........(tests have been cut)>\n",
                "isRequired": "Yes",
                "when": "Before travel, After arrival",
                "requirement": "Mandatory",
                "rules": "http://ncov.mohw.go.kr/upload/viewer/skin/doc.html?fn=1644371353583_20220209104913.hwp&rs=/upload/viewer/result/202203/",
                "testType": "PCR, NAAT, LAMP, TMA, SDA, NEAR",
                "minimumAge": 6,
                "validityPeriod": {
                    "delay": "P48H",
                    "referenceDateType": "Departure"
```


```json
                "quarantineOnArrivalAreas": [
                    {
                        "iataCode": "AD",
                        "areaType": "country"
                    },
                    {
                        "iataCode": "AE",
                        "areaType": "country"
                    },
                    {
                        "iataCode": "AF",
                        "areaType": "country"
                    },
                    
```



## Available blog articles 
[Keep Travelers informed with Amadeus Travel Restrictions API](https://developers.amadeus.com/blog/-introducing-amadeus-covid-19-travel-restrictions-api)

[How to build a neighborhood safety map in Python with Amadeus Safe Place](https://developers.amadeus.com/blog/neighborhood-safety-map-python)
