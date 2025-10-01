# Market insights

With Amadeus Self-Service APIs, you can get insights from millions of bookings and our technology partners.  In the **Market insights** category, we have four APIs available.

| APIs                                                                                                                                                          | Description                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Flight Most Traveled Destinations](https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-traveled-destinations/api-reference){:target="\_blank"} | See the top destinations by passenger volume for a given city and month.                |
| [Flight Most Booked Destinations](https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-booked-destinations/api-reference){:target="\_blank"}           | See the top destinations by booking volume for a given city and month.                  |
| [Flight Busiest Traveling Period](https://developers.amadeus.com/self-service/category/air/api-doc/flight-busiest-traveling-period/api-reference){:target="\_blank"}        | See monthly air traffic levels by city to understand season trends.                     |

## Find the top destinations or the busiest period for a given city

You may wonder which destination the travelers travel to the most and when is the busiest period for a given city. You can get the travel insight from a given city and month with the following three endpoints.

!!! information
    - The results of these three endpoints are based on estimated flight traffic summary data from the past 12 months. 
    - Flight traffic summary data is based on bookings made over Amadeus systems.

### The top destinations by passenger volume 

[Flight Most Traveled Destinations  API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-traveled-destinations/api-reference){:target="\_blank"} returns the most visited destinations from a given city. 

```bash
GET https://test.api.amadeus.com/v1/travel/analytics/air-traffic/traveled?originCityCode=NCE&period=2018-01
```

### The top destinations by booking volume 

[Flight Most Booked Destinations API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-booked-destinations/api-reference){:target="\_blank"} returns the most booked destinations from a given city. 

```bash
GET https://test.api.amadeus.com/v1/travel/analytics/air-traffic/booked?originCityCode=NCE&period=2018-01
```

### The busiest month/period by air traffic 

[Flight Busiest Traveling Period  API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-busiest-traveling-period/api-reference){:target="\_blank"} returns the peak periods for travel to/from a specific city. 

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

Sorting is enabled on the [Top Destinations](https://developers.amadeus.com/self-service/category/market-insights/api-doc/flight-most-traveled-destinations/api-reference) endpoints. 

- `analytics.flights.score` - sort destination by flights score (decreasing)
- `analytics.travelers.score` - sort destination by traveler's score (decreasing)

For example : 

```bash
GET https://test.api.amadeus.com/v1/travel/analytics/air-traffic/traveled?originCityCode=NCE&period=2018-01&sort=analytics.travelers.score
```

### Direction 

For the Flight Busiest Traveling Period insight, you can specify the direction as:

- `ARRIVING` for statistics on travelers arriving in the city
- `DEPARTING` for statistics on travelers leaving the city

By default, statistics are given on travelers ARRIVING in the city.

```bash
GET https://test.api.amadeus.com/v1/travel/analytics/air-traffic/busiest-period?cityCode=PAR&period=2018&direction=ARRIVING
```
