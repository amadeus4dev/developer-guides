# Locations

| APIs                                                                                                                                                 | Description                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [Airport & City Search API](https://developers.amadeus.com/self-service/category/air/api-doc/airport-and-city-search) |  Finds airports and cities that match a specific word or string of letters.                                                 |
| [Airport Nearest Relevant API](https://developers.amadeus.com/self-service/category/air/api-doc/airport-nearest-relevant) | Finds the closest major airports to a starting point. |
| [Safe Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place) | Provides updated safety and security ratings for over 65,000 cities and neighborhoods worldwide, helping travelers consult and compare destination safety. |

## Airport and City Search

The [Airport & City Search API](https://developers.amadeus.com/self-service/category/air/api-doc/airport-and-city-search) finds airports and cities that match a specific
word or a string of letters. Using this API, you can automatically suggest
airports based on what the traveler enters in the search field. The API
provides a list of airports/cities ordered by yearly passenger volume with the
name, 3-letter IATA code, time zone and coordinates of each airport.

## Airport Nearest Relevant

The [Airport Nearest Relevant API](https://developers.amadeus.com/self-service/category/air/api-doc/airport-nearest-relevant) finds the closest major airports to a starting
point. The API provides a list of commercial airports within a 500km (311mi)
radius of a given point that are ordered by relevance, which considers their
distance from the starting point and their yearly flight traffic. For each
airport, the API provides the name, 3-letter IATA code, time zone and
coordinates.

## Safe Rates

The [Safe Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place) is the newest addition to our Self-Service API catalog.
Created in partnership with GeoSure, the global leader in scaled location
safety ratings, the API is powered by GeoSafeScores™ algorithm, which provides
safety and security ratings for over 65,000 cities and neighborhoods worldwide.  

### Safe Places by radius 

This endpoint returns the overall safety rating of the targeted location defined by latitude, longitude and a radius. It’s very useful when you want to retrieve safety information for a downtown area, or around a specific point like a hotel, market or crowed touristic attraction.  

For example, the following request retrieves the safety scores around the famous Sagrada Family in Barcelona: 

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-locations?latitude= 41.403749&longitude= 2.174387 
```

Note that you don’t have to specify the radius – it is an optional query parameter set to 1 km by default.

### Safe Places by square  

The last endpoint allows users to retrieve the safety rated information using the unique identifier for a specific location, returned by the previous two endpoints: 

```json
{ 
 "subType": "CITY", 
 "name": "Barcelona", 
 "id": "Q930402725", 
 "geoCode": { 
   "latitude": 41.4172284, 
   “longitude": 2.163444, 
 }, 
```
 
This endpoint is useful when you want to perform a new check on a previously retrieved area. The following example returns safety scores for the city of Barcelona using its unique ID: 

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-location?id=Q930402725", 
```

### Response

The API returns the Overall Safety score and scores for six component categories:

- Women’s Safety 
- Health & Medical Safety 
- Physical Harm 
- Theft 
- Political Freedoms 
- LGBTQ+ Safety 

Let’s look at the response of a call to Safe Place by Radius using central Barcelona as the coordinates:

```json
 "safetyScores": { 
                "lgbtq": 42, 
                "medical": 25, 
                "overall": 47, 
                "physicalHarm": 39, 
                "politicalFreedom": 50, 
                "theft": 56, 
                "women": 34 
            } 
```

Safety scores range on a scale of 1-100, with 1 being the safest and 100 being
the least safe. In this example, the “medical” score of 25 indicates that the
health and medical conditions at the location are very good and quality medical
facilities are available.   

On the other hand, the “theft” score of 56 indicates an average-level risk of
theft in the area.

