# Market insights

With Amadeus Self-Service APIs, you can get insights from millions of bookings and our technology partners.  In the `Market insights` category, we have 4 APIs available.

| APIs                                                                                                                                                          | Description                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [ Flight Most Traveled Destinations  API]( https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-traveled-destinations/api-reference ) | See the top destinations by passenger volume for a given city and month.                |
| [ Flight Most Booked Destinations API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-booked-destinations/api-reference )           | See the top destinations by booking volume for a given city and month.                  |
| [Flight Busiest Traveling Period  API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-busiest-traveling-period/api-reference)        | See monthly air traffic levels by city to understand season trends.                     |
| [Location Score API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/location-score/api-reference)                               | Assess a neighborhood’s popularity for sightseeing, shopping, eating out, or nightlife. |


## Find the top destinations or the busiest period for a given city

You may wonder which destination the travelers travel to the most and when is the busiest period from a given city. You can get the travel insight from a given city and month with 3 endpoints.

!!! information
    - The results of these 3 endpoints are based on estimated flight traffic summary data from the past 12 months. 
    - Flight traffic summary data is based on bookings made over Amadeus systems.

### The top destinations by passenger volume 

`Flight Most Traveled Destinations API` returns the most visited destinations from a given city. 

```bash
GET https://test.api.amadeus.com/v1/travel/analytics/air-traffic/traveled?originCityCode=NCE&period=2018-01
```

### The top destinations by booking volume 

`Flight Most Booked Destinations API` returns the most booked destinations from a given city. 

```bash
GET https://test.api.amadeus.com/v1/travel/analytics/air-traffic/booked?originCityCode=NCE&period=2018-01
```

### The busiest month/period by air traffic 

`Flight Busiest Traveling Period API` returns the peak periods for travel to/from a specific city. 

```bash
GET https://test.api.amadeus.com/v1/travel/analytics/air-traffic/busiest-period?cityCode=NCE&period=2018
```

### Response 

The three endpoints have the same response structure.

Response to the top destinations from a given city : 

```json
{
    "meta": {
        "count": 8,
        "links": {
            "self": "https://test.api.amadeus.com/v1/travel/analytics/air-traffic/booked?originCityCode=NCE&page%5Blimit%5D=10&page%5Boffset%5D=0&period=2018-01&sort=analytics.travelers.score"
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
            "destination": "MAD",
            "subType": "BOOKED",
            "analytics": {
                "flights": {
                    "score": 10
                },
                "travelers": {
                    "score": 8
                }
            }
        }
    ]
}
```

Response to the busines period from a given city : 

```json
{
    "meta": {
        "count": 3,
        "links": {
            "self": "https://test.api.amadeus.com/v1/travel/analytics/air-traffic/busiest-period?cityCode=PAR&direction=ARRIVING&period=2018"
        }
    },
    "data": [
        {
            "type": "air-traffic",
            "period": "2018-03",
            "analytics": {
                "travelers": {
                    "score": 34
                }
            }
        },
        {
            "type": "air-traffic",
            "period": "2018-02",
            "analytics": {
                "travelers": {
                    "score": 33
                }
            }
        },
        {
            "type": "air-traffic",
            "period": "2018-01",
            "analytics": {
                "travelers": {
                    "score": 33
                }
            }
        }
    ]
}
```

- `subType` is `BOOKED` or `TRAVELED`, depending on the endpoint. 
- In `analytics`, the `score` in `flight` is flights to this destination as a percentage of total departures, and the `score` in `traveler` is the number of passengers traveling to the destination as a percentage of total passenger departures.


### Sorting

Sorting is possible for the top destinations' endpoints. 

- analytics.flights.score - sort destination by flights score (decreasing)
- analytics.travelers.score - sort destination by traveler's score (decreasing)

for example : 

```bash
GET https://test.api.amadeus.com/v1/travel/analytics/air-traffic/traveled?originCityCode=NCE&period=2018-01&sort=analytics.travelers.score
```

### Direction 

For the busiest period of travel insight from a given city, you can specify the direction either `ARRIVING` to have statistics on travelers or `DEPARTING` for statistics on travelers leaving the city. By default, statistics are given on travelers ARRIVING the city.

```bash
GET https://test.api.amadeus.com/v1/travel/analytics/air-traffic/busiest-period?cityCode=PAR&period=2018&direction=ARRIVING
```

## Find insight within a given city

Apart from the top destinations and busiest period insight in a city, you can also help users gain insights into a neighborhood, hotel, or vacation rental with the `Location Scores API`. 

For a given latitude and longitude, it provides popularity scores for the following leisure and tourism categories:

- Sightseeing
- Restaurants
- Shopping
- Nightlife

For each category, the API provides an overall popularity score and scores for select subcategories 
like luxury shopping, vegetarian restaurants, or historical sights, among others. Location scores are on 
a simple 0-100 scale and are powered by the [AVUXI TopPlace](https://www.avuxi.com/topplace/location-scores) algorithm which analyzes millions of online reviews, comments, and points of interest.

!!! Notes
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
