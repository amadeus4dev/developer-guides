# Itinerary Management

In the **Itinerary Management** category, you can give travelers a simple and personalized way to view their itinerary. 

!!! information
    Our catalogue of [Self-Service APIs](https://developers.amadeus.com/self-service){:target="\_blank"} is currently organised by categories that are different to what you see on this page.

| APIs                                                                                                                                                 | Description                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [Trip Purpose Prediction](https://developers.amadeus.com/self-service/category/trip/api-doc/trip-purpose-prediction/api-reference){:target="\_blank"} | Analyze a flight itinerary and predict whether the trip is for business or leisure. |
| [City Search](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search){:target="\_blank"} | Finds cities that match a specific word or string of letters. |


## Predict the trip purpose from a flight

Another API in the itinerary management category, the [Trip Purpose Prediction API](https://developers.amadeus.com/self-service/category/trip/api-doc/trip-purpose-prediction/api-reference){:target="\_blank"}, predicts whether a flight is searched for **business** or **leisure**. Our machine-learning models have detected which patterns of departure and arrival cities, flight dates, and search dates are associated with business and leisure trips. Understand why your users travel and show them the flights, fares, and ancillaries that suit them best.

Below is an example to see if the flight from New York to Madrid from 2022-12-01 to 2022-12-12 is leisure or business. 

```bash
GET https://test.api.amadeus.com/v1/travel/predictions/trip-purpose?originLocationCode=NYC&destinationLocationCode=MAD&departureDate=2022-12-01&returnDate=2022-12-12
```

The result? You can probably guess it. :) 

```json
{
  "data": {
    "id": "NYCMAD20221201",
    "probability": "0.9970142",
    "result": "LEISURE",
    "subType": "trip-purpose",
    "type": "prediction"
  },
  "meta": {
    "defaults": {
      "searchDate": "2022-06-30"
    },
    "links": {
      "self": "https://test.api.amadeus.com/v1/travel/predictions/trip-purpose?originLocationCode=NYC&destinationLocationCode=MAD&departureDate=2022-12-01&returnDate=2022-12-12&searchDate=2022-06-30"
    }
  }
}
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
