# Locations

## Airport and City Search

The Airport & City Search API finds airports and cities that match a specific
word or string of letters. Using this API, you can automatically suggest
airports based on what the traveler enters in the search field. The API
provides a list of airports/cities ordered by yearly passenger volume with the
name, 3-letter IATA code, time zone and coordinates of each airport.

## Airport Nearest Relevant

The Airport Nearest Relevant API finds the closest major airports to a starting
point. The API provides a list of commercial airports within a 500km (311mi)
radius of a given point that are ordered by relevance, which considers their
distance from the starting point and their yearly flight traffic. For each
airport, the API provides the name, 3-letter IATA code, time zone and
coordinates.

## Points of Interest

The Points of Interest API relies on AVUXI’s GeoPopularity algorithm, which
analyses and ranks geolocated data from more than 60 sources, including
comments, photos, and reviews from millions of users.

### Points of Interest by radius

The first endpoint supports only GET method and returns a list of points of
interest for a given location - latitude and longitude - and a radius (1 km by
default).

The following sample returns a list of POIs for someone geolocated in Barcelona downtown: 

```bash
curl https://test.api.amadeus.com/v1/reference-data/ locations/pois?latitude=41.397158&longitude=2.160873
```

In case we want to expand the area of search, we could use the radius parameter. In the following example, we increase the radius up to 3 kilometers:

```bash
curl https://test.api.amadeus.com/v1/reference-data/locations/pois?latitude=41.397158&longitude=2.160873&radius=3
```

### Points of Interest by a square

The second endpoint works in a similar way to the radius-based endpoint: It
supports also GET operations but it defines the area of search with a box:
north, west, south, and east.

The following example returns a list of points of interest for an area around Barcelona:

```bash
curl https://test.api.amadeus.com/v1/reference-data/locations/pois/by-square?north=41.397158&west=2.160873&south=41.394582&east=2.177181   
```

### Response

For both endpoints you can expect the same response format: a list of locations with the following JSON structure:

```json
{
   "type": "location",
   "subType": "POINT_OF_INTEREST",
   "geoCode": {
       "latitude": 41.39165,
       "longitude": 2.164772
   },
   "name": "Casa Batlló",
   "category": "SIGHTS",
    "tags": [
       "sightseeing",
       "museum",
       "sights",
       "landmark"
     ]
 }
```

Where:

- `Type` and `subType` are literals with fixed values.
- `geoCode` is a structure which contains geolocation information: latitude and longitude of the location.
- `name` contains the string identifying the location.
- `category` corresponds to the category of the location and could be one of the following values: SIGHTS, BEACH_PARK, HISTORICAL, NIGHTLIFE, RESTAURANT or SHOPPING.
- `tags` field is a list of words related to that location which comes directly from the different sources of data analyzed.

## Safe Rates

The Safe Place API is the newest addition to our Self-Service API catalog.
Created in partnership with GeoSure, the global leader in scaled location
safety ratings, the API is powered by GeoSafeScores™ algorithm which provides
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
 
This endpoint is useful when you want to perform a new check on a previously retrieved area. The following example, return the safety scores for the city of Barcelona using its unique id: 

```bash
curl https://test.api.amadeus.com/v1/safety/safety-rated-location?id=Q930402725", 
```

### Response

The API returns an Overall Safety score and scores for six component categories:

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
the least safe. In this example, a “medical” score of 25 indicates that the
health and medical conditions at the location are very self and quality medical
facilities are available.   

On the other hand, the “theft” score of 56 indicates an average-level risk of
theft in the area.

