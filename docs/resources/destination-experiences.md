# Destination Experiences

with Amadeus Self-Service APIs, you can find data on over 2 million places and 150,000 activities and show travelers the best things to see and do. In `Destination Experiences` category, we have 2 APIs available for that.

| [Points of Interest  API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/points-of-interest/api-reference)  | Find the best sights, shops, and restaurants in any city or neighborhood.                                                 |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [Tours and Activities  API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities/api-reference) | Find the best tours, activities, and tickets in any city or neighborhood. Includes a deep link to book with the provider. |

These 2 APIs has same behaviors in endpoints. you can search by radius, by a sqaure and retrieve by id. Let's go through one by one. 

## Show Travelers the best sights, shops and restaurants

The `Points of Interest API` relies on AVUXI’s GeoPopularity algorithm, which analyses and ranks geolocated data from more than 60 sources, including comments, photos, and reviews from millions of users.

### Search by radius

The first endpoint supports only `GET` method and returns a list of points of interest for a given location - latitude and longitude - and a radius (1 km by default).

The following sample returns a list of Points of Interests for someone geolocated in Barcelona downtown: 

```bash
curl https://test.api.amadeus.com/v1/reference-data/locations/pois?latitude=41.397158&longitude=2.160873
```

In case we want to expand the area of search, we could use the radius parameter. In the following example, we increase the radius up to 3 kilometers:

```bash
curl https://test.api.amadeus.com/v1/reference-data/locations/pois?latitude=41.397158&longitude=2.160873&radius=3
```

### Search by a square

The second endpoint works in a similar way to the radius-based endpoint: It supports also `GET` operations but it defines the area of search with a box: north, west, south, and east.

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
            "id": "AF57D529B2",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/pois/AF57D529B2",
                "methods": [
                    "GET"
                ]
            },
            "geoCode": {
                "latitude": 41.40359,
                "longitude": 2.17436
            },
            "name": "La Sagrada Familia",
            "category": "SIGHTS",
            "rank": 5,
            "tags": [
                "church",
                "sightseeing",
                "temple",
                "sights",
                "attraction",
                "historicplace",
                "tourguide",
                "landmark",
                "professionalservices",
                "latte",
                "activities",
                "commercialplace"
            ]
        }
```

- `Type` and `subType` are literals with fixed values.
- `id` is a unique value for this point of interests, that you can use to retrieve again with next endpoint. 
- `geoCode` is a structure which contains geolocation information: latitude and longitude of the location.
- `name` contains the string identifying the location.
- `category` corresponds to the category of the location and could be one of the following values: SIGHTS, BEACH_PARK, HISTORICAL, NIGHTLIFE, RESTAURANT or SHOPPING.
- `rank` is the position compared to other locations based on how famous is a place. 1 being the highest.
- `tags` field is a list of words related to that location which comes directly from the different sources of data analyzed.

### Retrieve by id 

You can also keep the unique id of each point of interests and retrieve with the last endpoint as below.

```bash
curl https://test.api.amadeus.com/v1/reference-data/locations/pois/AF57D529B2  
```

## Offer tours, activities and attraction tickets

The [Tours and Activities API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities/api-reference) is Built in partnership with MyLittleAdventure, Tours and Activities enables you offer users the best activities in any destination, complete with a photo, description, price and link to book the activity directly with the provider. 

For the API, we partnered with MyLittleAdventure which aggregates offers from over 45 of the world’s top activity platforms like Viator, GetYourGuide, Klook and Musement and applies an algorithm to identify duplicate activities across providers, compare them and return the best one. 

You can now help your users find the best things to do in over 8,000 destinations worldwide and book more than 300,000 unique activities including sightseeing tours, day trips, skip-the-line museum tickets, food tours, hop-on-hop-off bus tickets and much more. 

This API shares the same endpoint design as others like Points of Interest API.

### Search by radius

you can search activities for a specific location by providing a latitude and longitude. The API returns activities within a 1km radius, but you can also define a custom radius. 

```bash
curl https://test.api.amadeus.com/v1/shopping/activities/longitude=-3.69170868&latitude=40.41436995&radius=1   
```

### Search by a square

you can search activities within a given area by providing the cardinals : north, west, south, and east. 

```bash
curl https://test.api.amadeus.com/v1/shopping/activities/by-square?north=41.397158&west=2.160873&south=41.394582&east=2.177181 
```

### Response

Let’s look at a sample response from the Tours and Activities API:

```json
{ 
  "data": [ 
    { 
      "id": "23642", 
      "type": "activity", 
      "self": { 
        "href": "https://test.api.amadeus.com/v1/shopping/activities/23642", 
        "methods": [ 
          "GET" 
        ] 
      }, 
      "name": "Skip-the-line tickets to the Prado Museum", 
      "shortDescription": "Book your tickets for the Prado Museum in Madrid, discover masterpieces by Velázquez, Goya, Mantegna, Raphael, Tintoretto and access all temporary exhibitions.", 
      "geoCode": { 
        "latitude": "40.414000", 
        "longitude": "-3.691000" 
      }, 
      "rating": "4.500000", 
      "pictures": [ 
        "https://images.musement.com/cover/0001/07/prado-museum-tickets_header-6456.jpeg?w=500" 
      ], 
      "bookingLink": "https://b2c.mla.cloud/c/QCejqyor?c=2WxbgL36", 
      "price": { 
        "currencyCode": "EUR", 
        "amount": "16.00" 
      } 
    } 
  ] 
} 
```

As you can see the API returns a unique activity id along with the activity name, short description, geolocation, customer rating, image, price and deep link to the provider page to complete the booking.  

- `Type` is a literal with fixed value.
- `id` is a unique value for this activity, that you can use to retrieve again with next endpoint. 
- `name` and `shortDescription` contains the information about the activity. 
- `geoCode` is a structure which contains geolocation information: latitude and longitude of the location.
- `rating` is a rating of the activity. 
- `pictures` and `bookingLink` are external links to check the relevant pictures and to go to the booking URL from the activity provider.
- `price` is amount of the fare, and it could be alpha numeric. Ex- 500.20 or 514.13A, `A` signifies additional collection.

### Retrieve by id

Same as `Points of Interest API`, You can keep the unique id of each activity and retrieve with the last endpoint as below.

```bash
curl https://test.api.amadeus.com/v1/shopping/activities/23642
```