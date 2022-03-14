# Covid-19 and Travel Safety 


"Can I travel to South Korea? Thailand? or Costa Rica? Do I need to have a PCR test ? before the flight? after I arrive? How many days of quarantines is required? Where can I find these information?" 

Don't worry, with Amadeus Self Service APIs, you will be able to have the details information of **current restrictions, Number of covid-19 cases, Entry requirements and Safety scores etc** with more details in a searched destinations with one single API.

and even more, **safety information** can be retrieved for the destination you would like to visit, so that you will be clearly aware of where you are heading to. 

## Search by an area

There are 2 APIs to acheive the information 
1. [Amadeus Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions) for covid-19 related information 
2. [Amadeus Safety Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place) for Safety information

[Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions) can be searched **by a country, city or region**. 

```bash
curl https://test.api.amadeus.com/v1/duty-of-care/diseases/covid19-area-report?countryCode=FR&cityCode=PAR
```

!!! information
    Country code(2 letters code) is defined in [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) and city code(3 letters code) is defined in [IATA](https://www.iata.org/en/publications/directories/code-search/), which you can also use [Amadeus Airport & City Search API](https://developers.amadeus.com/self-service/category/air) to get.


[Safety Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place) can be searched by a given location with **latitude, longitude and radius**, or **Sqaure information** (North, West, South and east) or **by id**.

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-locations?latitude=48.856614&longitude=2.3522219&radius=2
```

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-locations/Q930400878
```

!!! information 
    the id is given by your first query which has been searched by others. the search by id was designed to target a specific area that you want to focus on.


## Get Information from the responses
Let's go through some highlights information you get from both Travel Restriction API and Safety Place API. 

!!!information
   Don't forget that Amadeus for Developers provides a `Test Environment` with [limited data collections](https://amadeus4dev.github.io/developer-guides/guides/api-data-collection/). 
   - the data source of travel restrictions API is from [Riskline](https://riskline.com/), they have sourced from local governments and media. The quantity of information provided may vary from country to country. 
   - the data source of Safety Place API is from [GeoSure](https://geosureglobal.com/), GeoSafeScores algorithm which analyzes crime, health and economic data, official travel alerts, local reporting and a variety of other sources. 

### Get summary of the destination + Safety score

from the response of Travel Restriction API : 

```json
"area": {
            "name": "South Korea",
            "iataCode": "KR",
            "areaType": "Country"
        },
        "summary": "<p>Authorities have relied on gathering limits and social distancing measures to contain outbreaks since the start of the pandemic. A three-stage lifting of COVID-19 measures was underway, but was pasued in late November 2021 as a new spike in COVID-19 cases led to rises in deaths and those with severe symptoms, and threatened hospital bed and ICU availabilities. </p>",
        "diseaseRiskLevel": "High",
        "diseaseInfection": {
            "date": "2022-03-06",
            "level": "Extreme",
            "rate": 5088.42
```

from the response of Safety Place API, you will get safety scores by category. 

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

### Get Covid-19 related statistics 

from the response of Travel Restriction API : the result provides Covid-19 statstics such as total cases, active cases, and current rate of infection per 100,000 

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
and what is the vaccination ratio in this country ?

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

from the response of Travel Restriction API : 
Entry information, which origin countries will be required for quarantine, Entry Requirements, Mask information, Tracing application and much more...

```json
            "entry": {
                "date": "2022-03-04",
                "text": "<p>All inbound non-resident foreign nationals must secure a visa prior to their travel. All travellers, including residents and Non- South Korean nationals, must hold a valid negative PCR test result to be allowed to borad on an inbound flight to South Korea. However, South Korean nationals who were found after entry with a non-conforming certificate must undergo a five days quarantine in a government designated facility and an additional two days home quarantine.</p>",
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
                    ....
```



### Available blog articles 
[Keep Travelers informed with Amadeus Travel Restriction API ](https://developers.amadeus.com/blog/-introducing-amadeus-covid-19-travel-restrictions-api)

