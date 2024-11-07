# Destination Experiences

With Amadeus Self-Service APIs, you can find data on over two million places and 150,000 activities and show travelers the best things to see and do. In the **Destination Experiences** category, we have two APIs available for that.

| APIs                                                                                                                                                 | Description                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [Points of Interest](https://developers.amadeus.com/self-service/category/destination-content/api-doc/points-of-interest/api-reference){:target="\_blank"}     | Find the best sights, shops, and restaurants in any city or neighborhood.                                                 |
| [Tours and Activities](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities/api-reference){:target="\_blank"} | Find the best tours, activities, and tickets in any city or neighborhood. Includes a deep link to book with the provider. |
| [City Search](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search){:target="\_blank"} | Finds cities that match a specific word or string of letters. |

The first two APIs have the same behavior. You can search by radius or by a square, and retrieve results by ID. Let's go through them one by one.

## Show Travelers the best sights, shops, and restaurants

The [Points of Interest  API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/points-of-interest/api-reference){:target="\_blank"} relies on AVUXI’s GeoPopularity algorithm, which analyses and ranks geolocated data from more than 60 sources, including comments, photos, and reviews from millions of users.

### Search by radius

The first endpoint supports only `GET` method and returns a list of points of interest for a given location - latitude and longitude - and a radius (1 km by default).

The following sample returns a list of Points of Interest for someone geolocated in Barcelona downtown: 

```bash
curl https://test.api.amadeus.com/v1/reference-data/locations/pois?latitude=41.397158&longitude=2.160873
```

In case we want to expand the area of search, we could use the radius parameter. In the following example, we increase the radius to 3 kilometers:

```bash
curl https://test.api.amadeus.com/v1/reference-data/locations/pois?latitude=41.397158&longitude=2.160873&radius=3
```

### Search by a square

The second endpoint works in a similar way to the radius-based endpoint. It also supports `GET` operations but it defines the area of search by a square: North, West, South, and East.

The following example returns a list of points of interest for an area around Barcelona:

```bash
curl https://test.api.amadeus.com/v1/reference-data/locations/pois/by-square?north=41.397158&west=2.160873&south=41.394582&east=2.177181   
```

### Response

For both endpoints you can expect the same response format - a list of locations with the following JSON structure:

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
- `id` is a unique value for this point of interest, which you can use in the next endpoint. 
- `geoCode` is a structure that contains geolocation information: latitude and longitude of the location.
- `name` contains the string identifying the location.
- `category` corresponds to the category of the location and could be one of the following values: SIGHTS, BEACH_PARK, HISTORICAL, NIGHTLIFE, RESTAURANT, or SHOPPING.
- `rank` is the position compared to other locations based on how famous a place is, with 1 being the highest.
- `tags` field is a list of words related to that location, which comes directly from the different sources of data analyzed.


### Retrieve by Id 

You can also keep the unique Id of each point of interest and retrieve it with the last endpoint as below.


```bash
curl https://test.api.amadeus.com/v1/reference-data/locations/pois/AF57D529B2  
```

## Offer tours, activities, and attraction tickets

The [Tours and Activities  API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities/api-reference){:target="\_blank"}  is built in partnership with MyLittleAdventure. [Tours and Activities  API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities/api-reference){:target="\_blank"} enables you to offer users the best activities in any destination, complete with a photo, description, price, and link to book the activity directly with the provider. 

For the API, we partnered with MyLittleAdventure which aggregates offers from over 45 of the world’s top activity platforms, such as Viator, GetYourGuide, Klook and Musement and applies an algorithm to identify duplicate activities across providers, compare them and return the best one. 

You can now help your users find the best things to do in over 8,000 destinations worldwide and book more than 300,000 unique activities including sightseeing tours, day trips, skip-the-line museum tickets, food tours, hop-on-hop-off bus tickets and much more. 

This API has the same design as other endpoints, such as the Points of Interest API.

### Search by radius

You can search activities for a specific location by providing a latitude and longitude. The API returns activities within a 1km radius, but you can also define a custom radius. 

```bash
curl https://test.api.amadeus.com/v1/shopping/activities/longitude=-3.69170868&latitude=40.41436995&radius=1   
```

### Search by a square

You can search activities within a given area by providing the coordinates: North, West, South, and East. 

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

As you can see, the API returns a unique activity Id along with the activity name, short description, geolocation, customer rating, image, price and deep link to the provider page to complete the booking.  

- `Type` is a literal with a fixed value.
- `id` is a unique value for this activity, that you can use in the next endpoint. 
- `name` and `shortDescription` contains the information about the activity. 
- `geoCode` is a structure that contains geolocation information: latitude and longitude of the location.
- `rating` is a rating of the activity. 
- `pictures` and `booking link` are external links to check the relevant pictures and to go to the booking URL from the activity provider.
- `price` is the price of the fare, which can be alpha-numeric. Ex- 500.20 or 514.13A, `A` signifies additional collection.

### Retrieve by Id

Same as [Points of Interest  API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/points-of-interest/api-reference){:target="\_blank"}, you can keep the unique Id of each activity and retrieve it with the last endpoint as below.

```bash
curl https://test.api.amadeus.com/v1/shopping/activities/23642
```

## Find a city by keywords

If you are unsure of the exact spelling of a city, you can reach out to the [City Search API](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search){:target="\_blank"}. This API uses a keyword, which is a string containing a minimum of 3 and a maximum of 10 characters, to search for a city whose name contains this keyword. It is not critical whether you enter the entire city name or only a part of it. For example, `Paris`, `Par` or `ari` will all return `Paris` in the search results.

There are two optional parameters to help you make the query more precise - `countryCode` and `max`. The `countryCode` is a string for the ISO 3166 Alpha-2 code of the country where you need to locate a city, for example, `FR` for France. The `max` is an integer that defines the maximum number of search results.

You can also include a list of airports for each city returned in the search results. To do this, you need to add `AIRPORTS` to the include field, which is an array of strings defining additional resources for your search.

Let's check out the results for keyword `PAR`. We will limit the search scope to `FR` and the number of results to two.

```bash
GET https://test.api.amadeus.com/v1/reference-data/locations/cities?countryCode=FR&keyword=PAR&max=2
```

The results are probably rather predictable:

```json
{
  "meta": {
    "count": 2,
    "links": {
      "self": "https://test.api.amadeus.com/v1/reference-data/locations/cities?countryCode=FR&keyword=PAR&max=2"
    }
  },
  "data": [
    {
      "type": "location",
      "subType": "city",
      "name": "Paris",
      "iataCode": "PAR",
      "address": {
        "countryCode": "FR",
        "stateCode": "FR-75"
      },
      "geoCode": {
        "latitude": 48.85341,
        "longitude": 2.3488
      }
    },
    {
      "type": "location",
      "subType": "city",
      "name": "Le Touquet-Paris-Plage",
      "iataCode": "LTQ",
      "address": {
        "countryCode": "FR",
        "stateCode": "FR-62"
      },
      "geoCode": {
        "latitude": 50.52432,
        "longitude": 1.58571
      }
    }
  ]
}
```

First of all we see the French capital at the top of the list. The second result refers to the town Le Touquet-Paris-Plage, whose official name contains three letters that match our keyword. If we want to see more results, we can always adjust the `max` number of results.

The main difference between the [Airport & City Search API](https://developers.amadeus.com/self-service/category/air/api-doc/airport-and-city-search){:target="\_blank"} and [City Search API](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search){:target="\_blank"} is that the [Airport & City Search API](https://developers.amadeus.com/self-service/category/air/api-doc/airport-and-city-search){:target="\_blank"} only shows cities that have an airport, while the [City Search API](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search){:target="\_blank"} retrieves any city that matches a keyword.