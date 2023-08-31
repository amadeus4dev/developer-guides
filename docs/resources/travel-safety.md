# Travel Safety 

Amadeus for Developers provides travel safety data making it easy for developers to build applications that keep travelers safe at every step of the journey.

| APIs                                                                                                                                                          | Description                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Safe Place](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place){:target="\_blank"}          |  Provides updated safety and security ratings for over 65,000 cities and neighborhoods worldwide, helping travelers consult and compare destination safety.                  |


## Search by an area

With the Safe Place API you can find categorized risk levels with neighborhood-level granularity. You will get an overall safety score and scores for six-component categories: 

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


## Available blog articles

[How to build a neighborhood safety map in Python with Amadeus Safe Place](https://developers.amadeus.com/blog/neighborhood-safety-map-python){:target="\_blank"}
