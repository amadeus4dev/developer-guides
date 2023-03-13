# COVID-19 and Travel Safety 


"Can I travel to South Korea? Thailand? or Costa Rica? Do I need to have a PCR test? before the flight? after I arrive? How many days of quarantine are required? Where can I find this information?" 

Don't worry, with Amadeus Self-Service APIs, you will be able to get detailed information on **number of COVID-19 cases, entry requirements, safety scores and a lot more** with some extra data about the searched destination using just one single API.

And even more, **safety information** can be retrieved for the destination you would like to visit so that you will be aware of where you are heading to. 

There are two APIs to get this information, which we have grouped into the **COVID-19 and Travel Safety** category.

!!! information
    Our catalogue of [Self-Service APIs](https://developers.amadeus.com/self-service){:target="\_blank"} is currently organised by categories that are different to what you see on this page.

| APIs                                                                                                                                                          | Description                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Travel Restrictions](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"} | Provides up-to-date data on COVID-19 caseloads and travel restrictions for over 200 countries and territories, as well as hundreds of cities and regions worldwide.                |
| [Safe Place](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place){:target="\_blank"}          |  Provides updated safety and security ratings for over 65,000 cities and neighborhoods worldwide, helping travelers consult and compare destination safety.                  |


## Search by an area

### Travel Restrictions

[Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"} can be searched **by a country** and narrowed down to a city, if required.

The ISO country code is the only mandatory query parameter:

```bash
curl https://test.api.amadeus.com/v1/duty-of-care/diseases/covid19-area-report?countryCode=FR
```

The IATA city code is an optional query parameter to use with the mandatory query parameter:

```bash
curl https://test.api.amadeus.com/v1/duty-of-care/diseases/covid19-area-report?countryCode=FR&cityCode=PAR
```

!!! information
    The country code (2 letters) is defined by [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2){:target="\_blank"} and the city code (3 letters) is defined by [IATA](https://www.iata.org/en/publications/directories/code-search/){:target="\_blank"}. You can also use [Airport & City Search API](https://developers.amadeus.com/self-service/category/air){:target="\_blank"} to get this information. 

The results can be requested in different languages by passing the ISO language code as an optional query parameter `language`.

```bash
curl https://test.api.amadeus.com/v1/duty-of-care/diseases/covid19-area-report?countryCode=FR&cityCode=PAR&language=FR
```

The following languages are currently supported: 

* EN - English
* ES - Spanish
* DE - German
* JA - Japanese
* KO - Korean
* TH - Thai
* ID - Bahasa
* ZH - Chinese
* FR - French

### Safe Place

[Safe Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place){:target="\_blank"} can be searched by a given location using:

* Latitude, longitude and optionally a radius
* Square information (North, West, South, and East
* Amadeus location Id

Each of these options has a dedicated endpoint.

#### Latitude/longitude/radius

Latitude and longitude are mandatory query parameters:

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-locations?latitude=48.856614&longitude=2.3522219&radius=2
```

Radius (in km) is an optional parameter that can be used to narrow down the search by latitude and longitude:

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-locations?latitude=48.856614&longitude=2.3522219&radius=2
```

!!! information
    This endpoint supports [pagination](../pagination.md). 

#### Square information

The square information is define by four mandatory query parameters:

* Latitude north of bounding box
* Longitude west of bounding box 
* Latitude south of bounding box
* Longitude east of bounding box

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-locations/by-square?north=41.397158&west=2.160873&south=41.394582&east=2.177181
```

!!! information
    This endpoint supports [pagination](../pagination.md). 

#### Location Id

The location Id is an Amdeus-defined identifier that you can see in the search results when queritung the [Safe Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place){:target="\_blank"} by latitude/longitude/radius or square information. You can then use this Id as a shortcut to query the [Safe Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place){:target="\_blank"} for a specific location:


```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-locations/Q930400878
```

!!! information 
    The search by Id was designed to target a specific area that you want to focus on.


## Get information from responses
Let's highlight some information that you'll get from both Travel Restrictions API and Safe Place API. 

!!! Warning
    Don't forget that Amadeus for Developers provides a `Test Environment` with [limited data collections](../test-data.md){:target="\_blank"}. 

!!! information
   - the data for Travel Restrictions API comes from [Riskline](https://riskline.com/){:target="\_blank"} and it has been sourced from local governments and media. The quantity of information provided may vary from country to country. 
   - the data for Safe Place API comes from [GeoSure](https://geosureglobal.com/){:target="\_blank"} GeoSafeScores algorithm, which analyzes crime, health and economic data, official travel alerts, local reporting, and a variety of other sources. 
 

### Get summary of the destination + Safety score

From the response of [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"}: 

```json
"area": {
      "name": "South Korea",
      "code": "KR",
      "areaType": "Country"
    },
    "summary": {
      "lastUpdate": "2022-05-25",
      "text": "<p>Authorities have relied on gathering limits and social distancing measures to contain outbreaks since the start of the pandemic. A new spike in COVID-19 cases led to rises in deaths and those with severe symptoms, and threatened hospital bed and ICU availabilities in late November 2021. While daily new case numbers have reached a record high of over 500,000 in mid-March, reductions in deaths and severe cases have prompted authorities to gradually lift most restrictions. Measures are unlikely to re-tighten in the near-term as the new incoming President Yoon won the recent election while criticising the harshness of previous restrictions.</p>"
    },
    "diseaseRiskLevel": {
      "text": "Medium"
    },
    "diseaseInfection": {
      "lastUpdate": "2022-05-22",
      "level": "Extreme",
      "rate": 785.41,
      "trend": "Decrease"
    }
```

If you include a city in the search query, the response will include the `subAreas` array. This array includes the `area` object describing the city with its name, IATA code, geocoordinates, area type and a summary. The disease risk level is shown specifically for the city. The disease infection rate, however, is shown on the country level. For NYC in US, this would be:

```json
"subAreas": [
      {
        "area": {
          "name": "New York",
          "code": "NYC",
          "geoCode": {
            "latitude": 40.7306,
            "longitude": -73.9865
          },
          "areaType": "City"
        },
        "summary": {
          "text": "<p>The counties comprising the New York City metro area (Bronx, Dutchess, Kings, Nassau, New York, Orange, Putnam, Queens, Richmond, Rockland, Suffolk and Westchester) report plateauing numbers of COVID-19 cases through the beginning of May​.</p> <p>Staff shortages have led to periodic shutdowns of multiple New York City Subway lines.</p>"
        },
        "diseaseRiskLevel": {
          "text": "Medium"
        },
        "relatedArea": [
          {
            "methods": [
              "GET"
            ],
            "rel": "Child"
          }
        ]
      }
    ]
    ```


From the response of Safe Place API, you will get an overall safety score and scores for six-component categories: 

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

Each location found by the [Safe Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place){:target="\_blank"} is shown with its Amadeus location Id, which can be used in subsequent search queries:

```json
"type": "safety-rated-location",
      "id": "Q930402720"
```

### Get COVID-19 related statistics 

From the response of Travel Restrictions API: the result provides COVID-19 statistics such as total cases, active cases, and the current rate of infection per 100,000, including the data sources: 

```json
    "diseaseInfection": {
      "lastUpdate": "2022-05-22",
      "level": "Extreme",
      "rate": 785.41,
      "trend": "Decrease"
    },
    "diseaseCases": {
      "lastUpdate": "2022-05-31",
      "deaths": 24197,
      "confirmed": 18119415
    },
    "hotspots": {
      "text": "<p>Seoul, Incheon, Gyeonggi province</p>"
    },
    "dataSources": {
      "healthDepartmentSiteLink": "http://www.kdca.go.kr/index.es?sid=a3",
      "governmentSiteLink": "http://ncov.mohw.go.kr/en/"
    },
```

If available, the disease infection information is suplemented by a link to the infection statistics map, for example:

```json
"infectionMapLink": "https://www.nytimes.com/interactive/2021/us/covid-cases.html"
```

And what is the vaccination ratio in this country?

```json
    "areaVaccinated": [
      {
        "lastUpdate": "2022-05-16",
        "vaccinationDoseStatus": "oneDose",
        "percentage": 87.698
      },
      {
        "lastUpdate": "2022-05-30",
        "vaccinationDoseStatus": "fully",
        "percentage": 86.9
      }
    ]
```


### Get Travel Restrictions information 

From the response of Travel Restrictions API, you can get information on:

#### Area restrictions

These are the general restrictions in the area according to the confirmed information on a given date:

```json
    "areaRestrictions": [
      {
        "lastUpdate": "2022-05-26",
        "text": "<p>Capacity limits on public gatherings and time restrictions for bars, restaurants and other venues have been lifted. Houses of worship may also operate at full capacity.</p>",
        "restrictionType": "OTHER"
      }
    ]
```

#### Area access restrictions

These are the restrictions applying to entering or leaving an area.

##### Area access restrictions to transportation

```json
    "transportation": {
        "lastUpdate": "2022-05-29",
        "text": "<p>Quarantine-free 'travel bubble flights for group travellers fully vaccinated at least 14 days prior to travel have commenced between <strong>Incheon International Airport (ICN/RKSI)</strong> serving Seoul and <strong>Saipan International Airport (SPN/PGSN)</strong> in the <strong>Northern Mariana Islands</strong> (an unincorporated territory and commonwealth of the United States). Quarantine-free 'travel bubble' flights are also available for fully vaccinated travellers from Singapore; travellers must have tested negative for COVID-19 prior to departure to be eligible. Similar arrangements are being negotiated with <strong>Thailand</strong> and <strong>Guam</strong>, but talks have stalled due to spikes in COVID-19 cases.</p> <p>Jeju Air resumed flights between <strong>Incheon Airport</strong> and Bangkok’s <strong>Suvarnabhumi Airport (BKK/VTBS)</strong> from 22 December.</p> <p>A gradual resumption of international flights got underway at <strong>Daegu International Airport (TAE/RKTN)</strong>, starting with regular flights to and from <strong>Da Nang International Airport (DAD/VVDN)</strong> in <strong>Vietnam</strong>, after their COVID-19 related suspension. Further flight resumptions are planned with <strong>Yanji Chaoyangchuan (YNJ/ZYYJ)</strong>, <strong>Bangkok (BKK/VTBS)</strong> and <strong>Mactan–Cebu (CEB/RPVM)</strong> airports in <strong>China</strong>, <strong>Thailand</strong> and the <strong>Philippines</strong> respectively in June.</p> <p>AirAsia, Air India and some other international carriers have suspended commercial flights to and from South Korea until further notice. All Korean Air flights to and from Russia are suspended until further notice.</p> <p><strong>Planned policy</strong></p> <p>Authorities plan to resume flights between <strong>Gimpo International Airport (GMP/RKSS)</strong> serving <strong>Seoul</strong> and <strong>Tokyo</strong>'s <strong>Haneda Airport (HND/RJTT)</strong> in <strong>Japan</strong> from 15 June.</p>",
        "transportationType": "FLIGHT",
        "isBanned": "Partial",
        "throughDate": "indef"
      }
```

##### Area access restrictions to declaration documents

```json
    "declarationDocuments": {
        "lastUpdate": "2022-05-26",
        "text": "<p><strong>Health document</strong><br>All permitted inbound travellers must fill out and submit a Health Questionnaire and a Special Quarantine Declaration form while in-flight. Entry can be restricted if the contact information (phone number, address, etc.) on the Special Quarantine Declaration cannot be verified.</p>\n<p>This requirement is waived for those who have completed the <a href=\"https://cov19ent.kdca.go.kr/cpassportal/biz/beffatstmnt/main.do?lang=en\">Quarantine Information Advance Input System</a> prior to travel.</p>\n",
        "isRequired": "Yes"
      }
```

##### Area access restrictions to entry

```json
    "entry": {
        "lastUpdate": "2022-05-29",
        "text": "<p>All travellers, including South Korean nationals and residents, must hold a valid negative PCR or Antigen test result to be allowed to board an inbound flight to South Korea. South Korean nationals who are found after entry with a non-conforming certificate must undergo a five days quarantine in a government-designated facility and an additional two days of home quarantine.</p> <p>Visa-free entry has resumed. Eligible travellers from select countries/regions must apply and obtain a Korea Electronic Travel Authorisation (K-ETA) for receiving a South Korea bound boarding pass. Travellers from around 102 countries/regions are eligible to apply for a K-ETA, while some countries/regions, including Japan, Taiwan, Hong Kong and Macau, among other areas, are currently suspended from the list of eligible countries. Further information on K-ETA can be found <a href=\"https://www.moj.go.kr/immigration_eng/index.do\" target=\"_blank\" rel=\"noopener\">here</a>. Inbound foreign nationals intending to enter South Korea for any purpose that is not covered under K-ETA or those coming from countries not listed <a href=\"https://viewer.moj.go.kr/skin/doc.html?rs=/result/bbs/229&amp;fn=temp_1652688501265100\" target=\"_blank\" rel=\"noopener\">here</a> must secure a visa prior to their travel.</p> <p><strong>Planned policy</strong></p> <p>Authorities announced that the issuance of short-term visas, including tourist visas, as well as electronic visa application services will fully resume for inbound travellers departing Level 1 countries from 1 June; currently, all countries are designated as Level 1. Also, previously suspended short-term multiple-entry visas that have yet to expire will once again be considered valid.</p>",
        "ban": "No",
        "throughDate": "indef",
        "referenceLink": "http://ncov.mohw.go.kr/duBoardList.do?brdId=2&brdGubun=23",
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
      }
```

##### Area access restrictions to tests

```json
    "travelTest": {
        "lastUpdate": "2022-05-24",
        "isRequired": "Yes",
        "requirement": "Mandatory",
        "referenceLink": "http://ncov.mohw.go.kr/shBoardView.do?brdId=2&brdGubun=23&ncvContSeq=6640, https://overseas.mofa.go.kr/fi-en/brd/m_9574/view.do?seq=754925&page=1, http://ncov.mohw.go.kr/shBoardView.do?brdId=2&brdGubun=23&ncvContSeq=6413",
        "travelTestConditionsAndRules": [
          {
            "travelPhases": "BEFORE_TRAVEL",
            "scenarios": [
              {
                "name": "Default",
                "condition": {
                  "traveller": {
                    "whoNeeds": "All travellers from...",
                    "minimumAge": "6"
                  },
                  "trip": {
                    "countries": [
                      {
                        "code": "AD",
                        "areaType": "country"
                      },
                      
                      ...

                      {
                        "code": "ZW",
                        "areaType": "country"
                      }
                    ]
                  },
                  "textualScenario": "<p>All inbound travellers aged six or older, including South Korean nationals, must submit English or Korean certificates of negative results of COVID-19 tests (or English or Korean translations notarised by South Korean Embassies or Consulates) issued in paper. The test must have been taken within two days (48 hours) before their departure dates to be valid. A supervised Rapid Antigen Test (RAT) no older than one day (24 hours) before the departure date is also accepted. All non-South Korean nationals, as well as South Korean nationals departing from <strong>Indonesia</strong> and <strong>Myanmar</strong> without valid negative pre-travel COVID-19 test certificates, have been denied boarding on South Korea bound flights.</p>\n<p>South Korean nationals who recovered from COVID-19 between 10-40 days before departure can be exempted from the pre-travel testing requirement. Documents required for exemption can be found <a href=\"https://www.kdca.go.kr/board/board.es?mid=a20504000000&amp;bid=0014\">here</a>.</p>\n<p>Also, travellers with a humanitarian or urgent reason to enter the country including attending funerals or official business reasons are exempted from the pre-departure testing requirement. Additionally, aircrews, Korean sailors departing from Singapore (must hold a Seafarer&#39;s Book of the Republic of Korea) and those who are refused entrance at their destination are also exempted.</p>\n<p>Travellers departing from the <strong>Philippines</strong> or <strong>Uzbekistan</strong> must conduct their tests at their respective government-designated testing centres that are recognised by the South Korean Embassies or Consulates in those countries. Similar test centre restriction is possible in other departure countries; check the departure country&#39;s South Korean Embassy/Consulate websites for updates.</p>\n<p>South Korean nationals who arrive without a valid negative pre-travel COVID-19 test certificate and test positive for COVID-19 after arrival have been fined up to KRW 2,000,000.</p>\n"
                },
                "rule": {
                  "exemptions": [
                    "Aircrew",
                    "Deported",
                    "Seamen",
                    "Urgent"
                  ],
                  "test": [
                    {
                      "types": [
                        "PCR",
                        "NAAT",
                        "LAMP",
                        "TMA",
                        "SDA",
                        "NEAR"
                      ],
                      "validity": {
                        "delay": "48",
                        "referenceDateTime": "Departure"
                      }
                    },
                    {
                      "types": [
                        "Antigen"
                      ],
                      "validity": {
                        "delay": "24",
                        "referenceDateTime": "Departure"
                      }
                    }
                  ]
                }
              }
            ]
          },
          {
            "travelPhases": "AFTER_ARRIVAL",
            "scenarios": [
              {
                "condition": {
                  "traveller": {
                    "whoNeeds": "All travellers from..."
                  },
                  "trip": {
                    "countries": [
                      {
                        "code": "AD",
                        "areaType": "country"
                      },

                      ...

                      {
                        "code": "ZW",
                        "areaType": "country"
                      }
                    ]
                  },
                  "textualScenario": "<p>All fully vaccinated arrivals must take a PCR test for COVID-19 within three days of arrival. Long-stay residents must test at their local Public Health Centres, while all other fully vaccinated non-nationals must test at the Incheon Airport COVID-19 Test Centre or medical institution at their own expense. </p>\n<p>Quarantine exempted diplomatic passport holders and military personnel must undergo a PCR test at a government-designated facility. Those who test positive must quarantine based on rules that apply to non-fully vaccinated travellers.</p>\n<p>Unvaccinated short-stay non-nationals and non-compliant travellers who are subject to quarantine at a government-approved facility or at a temporary residential facility must undergo PCR tests within three days of arrival and again on either day six or seven of quarantine.</p>\n<p>Nationals or long-stay non-nationals who are not fully vaccinated and are subject to quarantine for seven days at home are only required the first PCR test taken within three days of arrival at a Public Health Center.</p>\n<p>All arrivals by sea ports must take a PCR test for COVID-19 on their vessel of arrival or at testing site as designated by authorities within one day of arrival. Those who test positive must quarantine based on rules that apply to non-fully vaccinated travellers.</p>\n"
                },
                "rule": {
                  "arrivalTestDays": "1"
                }
              }
            ]
          }
        ]
      }
```

##### Area access restrictions to tracing application

```json
    "tracingApplication": {
        "lastUpdate": "2022-05-26",
        "text": "<p>Travellers are no longer required to install the \"Self-quarantine Safe Protection\" contact tracing app.</p>",
        "isRequired": "No",
        "iosUrl": [
          "https://apps.apple.com/us/app/%EC%9E%90%EA%B0%80%EA%B2%A9%EB%A6%AC%EC%9E%90-%EC%95%88%EC%A0%84%EB%B3%B4%ED%98%B8/id1502372537"
        ],
        "androidUrl": [
          "https://play.google.com/store/apps/details?id=kr.go.safekorea.sqsm&hl=ko"
        ]
      }
```

##### Area access restrictions to masks

```json
    "masks": {
        "lastUpdate": "2022-05-26",
        "text": "<p>The wearing of face masks is a mandatory requirement in all indoor areas including on public transportation and outdoor areas where a one-metre distance cannot be maintained between people as well as outdoor gatherings, including sports matches, rallies and events, with 50 or more people.</p> <p>A fine of up to KRW 100,000 have been issued for non-compliance with the face mask mandate. Those under the age of 14 and those unable to wear masks due to medical conditions are exempt.</p>",
        "isRequired": "Partial"
      }
```

##### Area access restrictions to exiting the country

```json
    "exit": {
        "lastUpdate": "2022-05-26",
        "specialRequirements": "No",
        "isBanned": "No"
      }
```

##### Any additional area access restrictions

```json
    "otherRestrictions": {
        "lastUpdate": "2022-05-26",
        "text": "<p>Travellers waived of quarantine, including those with diplomatic visas A-1, A-2 and A-3 must submit daily health status checks via the ‘Self Diagnosis App’ found <a href=\"http://ncov.mohw.go.kr/selfcheck/\" target=\"_blank\" rel=\"noopener\">here</a>.</p>"
      }
```

##### Area access restrictions to travel vaccination

```json
    "travelVaccination": {
        "lastUpdate": "2022-05-26",
        "isRequired": "No",
        "referenceLink": "https://overseas.mofa.go.kr/sg-en/brd/m_2435/view.do?seq=761390&page=1",
        "acceptedCertificates": [
          "Not Specified",
          " Vietnam certificate"
        ],
        "qualifiedVaccines": [
          {
            "supportedVaccineProducts": "Pfizer",
            "numberOfDoses": 2,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "AstraZeneca (Vaxzevria)",
            "numberOfDoses": 2,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "Vaxevria (South Korea)",
            "numberOfDoses": 2,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "Covishield (India)",
            "numberOfDoses": 2,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "Johnson & Johnson",
            "numberOfDoses": 1,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "Sinopharm (Beijing)",
            "numberOfDoses": 2,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "CoronaVac",
            "numberOfDoses": 2,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "Moderna",
            "numberOfDoses": 2,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "CanSinoBIO",
            "numberOfDoses": 1,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "No"
          },
          {
            "supportedVaccineProducts": "Sinopharm (Wuhan)",
            "numberOfDoses": 2,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "Nuvaxovid (Novavax)",
            "numberOfDoses": 2,
            "expiration": {
              "expiresAfter": "14"
            },
            "boosterRequired": "Yes",
            "boosterExpiration": {
              "expiresAfter": "6"
            },
            "validity": {
              "delay": "6"
            }
          },
          {
            "supportedVaccineProducts": "Immunity through previous infection",
            "expiration": {
              "expiresAfter": "10"
            },
            "validity": {
              "delay": "1"
            }
          }
        ],
        "details": "<p>Travellers who have completed the recommended dose of the vaccine and have received a booster dose at least 14 days before departure are designated as fully vaccinated. Travellers who acquire their vaccinations outside of South Korea must integrate the proof of vaccination within the <a href=\"https://ncv.kdca.go.kr/menu.es?mid=a12507000000\" target=\"_blank\" rel=\"noopener\">COOV app</a>.</p> <p>South Korean nationals who have recently recovered from the virus and hold a medical certificate proving recovery and a positive PCR test result issued within 10-40 days prior to departure are exempt from a pre-departure testing requirement.</p> <p>All travellers fully vaccinated against COVID-19 are exempt from the seven-day quarantine on arrival, provided these travellers submitted their vaccination records on the <a href=\"https://cov19ent.kdca.go.kr/cpassportal/\" target=\"_blank\" rel=\"noopener\">Q-CODE portal</a>.</p>",
        "minimumAge": 12,
        "vaccinatedTravellers": {
          "policy": "No"
        }
      }
```

##### Area access restrictions to travel quarantine

```json
    "travelQuarantineModality": {
        "lastUpdate": "2022-05-26",
        "text": "<p>All non-South Korean nationals must quarantine for seven days. Long-term residents must do so at their residence, while short-term residents and all other non-nationals must do so at a government-designated facility; long-term residents without a residence suitable for quarantine must quarantine at a government-designated facility. Quarantine at a government-designated facility must be done at the traveller&#39;s own expense (max. KRW 150,000 per day).</p>\n<p>Fully vaccinated travellers with an invalid certificate or those who fail to submit their vaccine certificate in the Q-Code portal before departure will be designated as unvaccinated travellers and will be required to quarantine on arrival.</p>\n<p>Those who violate COVID-19 related measures during quarantine must wear an electronic tracking bracelet to ensure compliance with official orders during quarantine, and those who violate quarantine orders can face up to a year in prison or fines of up to KRW 10,000,000.</p>\n<p>Travellers entring the country to attend the funeral of an immediate family member may apply for a quarantine exemption via the <a href=\"https://consul.mofa.go.kr/en/main.do\">consular service web</a>. </p>\n<p>Unvaccinated South Korean nationals must quarantine at their residence for seven days. Those without a residence suitable for quarantine must quarantine at a government-designated facility. Quarantine at a government-designated facility must be done at the traveller&#39;s own expense (max. KRW 150,000 per day).</p>\n<p>Fully vaccinated travellers with an invalid certificate or those who fail to submit their vaccine certificate in the Q-Code portal before departure will be designated as unvaccinated travellers and will be required to quarantine on arrival.</p>\n<p>Those who violate COVID-19 related measures during quarantine must wear an electronic tracking bracelet to ensure compliance with official orders during quarantine, and those who violate quarantine orders can face up to a year in prison or fines of up to KRW 10,000,000.</p>\n<p>Travellers entring the country to attend the funeral of an immediate family member may apply for a quarantine exemption via the <a href=\"https://consul.mofa.go.kr/en/main.do\">consular service web</a>.</p>\n",
        "eligiblePerson": "Some travellers",
        "quarantineType": "Self",
        "duration": 7,
        "referenceLink": "http://ncov.mohw.go.kr/shBoardView.do?brdId=2&brdGubun=23&ncvContSeq=6413",
        "mandateList": "http://ncov.mohw.go.kr/shBoardView.do?brdId=2&brdGubun=23&ncvContSeq=6268",
        "quarantineOnArrivalAreas": [
          {
            "code": "AD",
            "areaType": "country"
          },

          ...

          {
            "code": "ZW",
            "areaType": "country"
          }
        ]
      }
```

##### Area access restrictions to area health pass

```json
    "areaHealthPass": {
        "lastUpdate": "2022-05-26",
        "isRequired": "No",
        "applicationGuidance": "<p>Effective 1 March, authorities suspended a vaccine pass mandate nationwide, with people no longer required to present proof of being fully vaccinated or possess negative test results to enter public places, due to a high vaccination rate and legal challenges. The suspension may later be reinstated if necessary.</p>"
      }
```

#### Area policy

```json
    "areaPolicy": {
      "lastUpdate": "2022-05-25",
      "text": "<p>Authorities lifted all remaining restrictions except face mask mandates for indoor venues.</p>",
      "status": "Opening",
      "startDate": "2021-12-18",
      "endDate": "indef",
      "referenceLink": "http://ncov.mohw.go.kr/en/tcmBoardList.do?brdId=12&brdGubun=125&dataGubun=&ncvContSeq=&contSeq=&board_id="
    }
```


## Available blog articles 
[Keep Travelers informed with Amadeus Travel Restrictions API](https://developers.amadeus.com/blog/-introducing-amadeus-covid-19-travel-restrictions-api){:target="\_blank"}

[How to build a neighborhood safety map in Python with Amadeus Safe Place](https://developers.amadeus.com/blog/neighborhood-safety-map-python){:target="\_blank"}
