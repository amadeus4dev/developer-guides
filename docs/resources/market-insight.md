# Market insights APIs

Amadeus Self Service APIs provides some APIs to get insights from millions of bookings. 
Spot trends and understand both travelers and destinations better.

## Flight Most Traveled Destinations API

Get insight into local travel habits by finding which destinations are most visited by travelers from a specific city. 
The Flight Most Traveled Destinations API returns a list of the most popular flight destinations among travelers from 
a given city, each with a flight score (flights to the destination as a percentage of total departures) and 
a traveler score (number of passengers traveling to the destination as a percentage of total passenger departures).

**Request:**

```
curl https://test.api.amadeus.com/v1/travel/analytics/air-traffic/traveled?originCityCode=MAD&period=2017-01
```

**Response:**

```json
{
  "meta": {
    "count": 10,
    "links": {
      "self": "https://test.api.amadeus.com/v1/travel/analytics/air-traffic/traveled?originCityCode=MAD&page%5Blimit%5D=10&page%5Boffset%5D=0&period=2017-01"
    }
  },
  "data": [
    {
      "type": "air-traffic",
      "destination": "PAR",
      "subType": "TRAVELED",
      "analytics": {
        "flights": {
          "score": 74
        },
        "travelers": {
          "score": 100
        }
      }
    },
    {
      "type": "air-traffic",
      "destination": "BCN",
      "subType": "TRAVELED",
      "analytics": {
        "flights": {
          "score": 100
        },
        "travelers": {
          "score": 78
        }
      }
    }
  ]
}
```

Further information: https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-traveled-destinations

## Flight Most Booked Destinations API

Get insight into local booking trends by finding which destinations are most frequently booked by travelers 
in a specific city. The Flight Most Booked Destinations API provides a list of the most booked destinations 
by travelers from a given city, each with a flight score (flights to the destination as a percentage of 
total departures) and a traveler score (number of passengers traveling to the destination 
as a percentage of total passenger departures).

**Request:**

```
curl https://test.api.amadeus.com/v1/travel/analytics/air-traffic/booked?originCityCode=MAD&period=2017-01
```

**Response:**

```json
{
  "meta": {
    "count": 10,
    "links": {
      "self": "https://test.api.amadeus.com/v1/travel/analytics/air-traffic/booked?originCityCode=MAD&page%5Blimit%5D=10&page%5Boffset%5D=0&period=2017-01"
    }
  },
  "data": [
    {
      "type": "air-traffic",
      "destination": "PAR",
      "subType": "BOOKED",
      "analytics": {
        "flights": {
          "score": 100
        },
        "travelers": {
          "score": 100
        }
      }
    },
    {
      "type": "air-traffic",
      "destination": "TCI",
      "subType": "BOOKED",
      "analytics": {
        "flights": {
          "score": 52
        },
        "travelers": {
          "score": 85
        }
      }
    }
  ]
}
```

Further information: https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-booked-destinations

## Flight Busiest Traveling Period API

The Flight Busiest Traveling Period API finds the peak periods for travel to/from a specific city. 
The API provides 12 reports (one for each month) that contain the monthly passenger volumes as a percentage 
of the yearly total for a given city. The percentages are based on Amadeus historical flight data.

**Request:**

```
curl https://test.api.amadeus.com/v1/travel/analytics/air-traffic/busiest-period?cityCode=MAD&period=2017
```

**Response:**

```json
{
  "meta": {
    "count": 12,
    "links": {
      "self": "https://test.api.amadeus.com/v1/travel/analytics/air-traffic/busiest-period?cityCode=MAD&period=2017"
    }
  },
  "data": [
    {
      "type": "air-traffic",
      "period": "2017-05",
      "analytics": {
        "travelers": {
          "score": 9
        }
      }
    },
    {
      "type": "air-traffic",
      "period": "2017-12",
      "analytics": {
        "travelers": {
          "score": 9
        }
      }
    }
  ]
}
```

Further information: https://developers.amadeus.com/self-service/category/air/api-doc/flight-busiest-traveling-period

## Location Score API

Help users gain insights into a neighborhood, hotel or vacation rental with the Amadeus Location Scores API. 
For a given latitude and longitude, the Location Scores API provides a popularity scores for 
the following leisure and tourism categories:

- Sightseeing
- Restaurants
- Shopping
- Nightlife

For each category, the API provides an overall popularity score and scores for select subcategories 
like luxury shopping, vegetarian restaurants or historical sights, among others. Location scores are on 
a simple 0-100 scale and are powered by the AVUXI TopPlace algorithm which analyzes millions of online reviews, 
comments and points of interest.

Notes:
- For each location, the API will return scores for a 200m., 500m., and 1500m. radius.
- Scores indicate positive traveler sentiments and may not reflect the most visited locations.

**Request:**

```
curl https://test.api.amadeus.com/v1/location/analytics/category-rated-areas?latitude=41.397158&longitude=2.160873
```

**Response:**

```json
{
  "data": [
    {
      "type": "category-rated-area",
      "geoCode": {
        "latitude": 41.397158,
        "longitude": 2.160873
      },
      "radius": 200,
      "categoryScores": {
        "sight": {
          "overall": 87,
          "historical": 83,
          "beachAndPark": 0
        },
        "restaurant": {
          "overall": 92,
          "vegetarian": 61
        },
        "shopping": {
          "overall": 96,
          "luxury": 96
        },
        "nightLife": {
          "overall": 86
        }
      }
    },
    {
      "type": "category-rated-area",
      "geoCode": {
        "latitude": 41.397158,
        "longitude": 2.160873
      },
      "radius": 500,
      "categoryScores": {
        "sight": {
          "overall": 99,
          "historical": 69,
          "beachAndPark": 0
        },
        "restaurant": {
          "overall": 94,
          "vegetarian": 71
        },
        "shopping": {
          "overall": 99,
          "luxury": 99
        },
        "nightLife": {
          "overall": 88
        }
      }
    }
  ],
  "meta": {
    "count": 3,
    "links": {
      "self": "https://test.api.amadeus.com/v1/location/analytics/category-rated-areas?latitude=41.397158&longitude=2.160873"
    }
  }
}
```

Further information: https://developers.amadeus.com/self-service/category/destination-content/api-doc/location-score
