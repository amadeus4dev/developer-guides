# Flights

## How to search flights

### Inspirational Search

The [Flight Inspiration Search API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-inspiration-search) provides a list of destinations from a given airport that is ordered by price and can be filtered by departure date or maximum price. The following request retrieves a list of destinations from Boston:

```bash
GET https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=BOS
```

!!!information
    This API returns cached prices. Once a destination is chosen, use the Flight Offers Search API to get real-time pricing and availability.

The API provides a link to Flight Offers Search to search for flights once a
destination is chosen and a link to Flight Cheapest Date Search to check the
cheapest dates to fly:

```json
"data": [
        {
            "type": "flight-destination",
            "origin": "BOS",
            "destination": "CHI",
            "departureDate": "2022-07-22",
            "returnDate": "2022-07-28",
            "price": {
                "total": "52.18"
            },
            "links": {
                "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=BOS&destination=CHI&departureDate=2022-07-02,2022-12-28&oneWay=false&duration=1,15&nonStop=false&maxPrice=300&currency=USD&viewBy=DURATION",
                "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=BOS&destinationLocationCode=CHI&departureDate=2022-07-22&returnDate=2022-07-28&adults=1&nonStop=false&maxPrice=300&currency=USD"
            }
        }
    ]
```

#### Search for destinations for a specific duration of stay

For example, let's say a traveler wants to spend six days in a city but doesn't have a strong preference for the destination. With the Flight Inspiration API we can recommend the traveler the cheapest destinations based on the stay duration. 

This can be done using the parameter `viewBy` which returns flight destinations by `DATE`, `DESTINATION`, `DURATION`, `WEEK`, or `COUNTRY`. In our scenario we need to pass the value `DURATION` to the parameter `viewBy`, like in the example below. Also, as input we give a duration of six days and origin Miami. The departure date will be between the 1st and 3rd of September 2021.

`GET https://test.api.amadeus.com/v1/shopping/flight-destinations?departureDate=2021-09-01,2021-09-03&duration=6&origin=MIA&viewBy=DURATION`

```json
  {
            "type": "flight-destination",
            "origin": "MIA",
            "destination": "MSP",
            "departureDate": "2021-09-01",
            "returnDate": "2021-09-07",
            "price": {
                "total": "136.79"
            },
            "links": {
                "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MIA&destination=MSP&departureDate=2021-09-01,2021-09-03&oneWay=false&duration=6&nonStop=false&viewBy=DURATION",
                "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MIA&destinationLocationCode=MSP&departureDate=2021-09-01&returnDate=2021-09-07&adults=1&nonStop=false"
            }
        },
        {
            "type": "flight-destination",
            "origin": "MIA",
            "destination": "STT",
            "departureDate": "2021-09-02",
            "returnDate": "2021-09-08",
            "price": {
                "total": "137.36"
            },
            "links": {
                "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MIA&destination=STT&departureDate=2021-09-01,2021-09-03&oneWay=false&duration=6&nonStop=false&viewBy=DURATION",
                "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MIA&destinationLocationCode=STT&departureDate=2021-09-02&returnDate=2021-09-08&adults=1&nonStop=false"
            }
        }
```

As you can see, all the recommendations have a duration of six days and are sorted by the lowest price. The API also provides link to the Flight Offers Search for each result in order to check for available flights.

### Flexible Search on dates

The [Flight Cheapest Date Search API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-cheapest-date-search) finds the cheapest dates to travel from one
city to another. The API provides a list of flight options with dates and prices,
and allows you to order by price, departure date or duration.

!!!information
    This API returns cached prices. Once the dates are chosen, use the Flight Offers Search API to get real-time pricing and availability.

The following example retrieves a list of `flight-date` objects containing pricing information given the origin and destination, and a range of dates:

```bash
GET https://test.api.amadeus.com/v1/shopping/flight-dates?origin=BOS&destination=CHI&departureDate=2022-08-15,2022-08-28
```

The API provides a link to Flight Offers Search to search for flights once a
destination is chosen, in order to proceed with the booking flow.

### Offers Search

The [Flight Offers Search API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search) searches over 500 airlines to find the cheapest
flights for a given itinerary. The API lets you search flights between two
cities, perform multi-city searches for longer itineraries and access one-way
combinable fares to offer the cheapest options possible. For each itinerary,
the API provides a list of flight offers with prices, fare details, airline
names, baggage allowances and departure terminals.

!!!warning
    Flights from low-cost carriers and American Airlines are currently unavailable.

The Flight Offers Search API starts the booking cycle with a search for the
best fares. The API returns a list of the cheapest flights given a city/airport
of departure, a city/airport of arrival, the number and type of passengers and
travel dates. The results are complete with airline name and fares as well as
additional information, such as bag allowance and pricing for additional baggage. 

The API comes in two flavors:

- Simple version: GET operation with few parameters but which is quicker to integrate.
- On steroids: POST operation offering the full functionalities of the API.

The minimum `GET` request has following parameters:

```bash
GET https://test.api.amadus.com/v2/shopping/flight-offers?adults=1&originLocationCode=BOS&destinationLocationCode=CHI&departureDate=2022-07-22
```

The API returns a list of `flight-offer` objects (up to 250), including
information such as itineraries, price, pricing options, etc.

```json
"data": [
    {
      "type": "flight-offer",
      "id": "1",
      "source": "GDS",
      "instantTicketingRequired": false,
      "nonHomogeneous": false,
      "oneWay": false,
      "lastTicketingDate": "2022-07-02",
      "numberOfBookableSeats": 9,
      "itineraries": [ ],
      "price": {
        "currency": "EUR",
        "total": "22.00",
        "base": "13.00",
        "fees": [
          {
            "amount": "0.00",
            "type": "SUPPLIER"
          },
          {
            "amount": "0.00",
            "type": "TICKETING"
          }
        ],
        "grandTotal": "22.00"
      }
    }
  ]
```

#### Include or exclude specific airlines 

If you want your search to return flights with only specified airlines, you can use the parameter `includedAirlineCodes` to consider specific airlines. For example, there is a traveler who wants to travel from Berlin to Athens only with Aegean Airlines (A3): 

`GET https://test.api.amadeus.com/v2/shopping/flight-offers?max=3&adults=1&includedAirlineCodes=A3&originLocationCode=BER&destinationLocationCode=ATH&departureDate=2022-12-06`

With the parameter `excludedAirlineCodes` you can ignore specific airlines. For example, there is a traveler who wants to travel from Berlin to Athens ignoring both Aegean Airlines (A3) and Iberia (IB):

`GET https://test.api.amadeus.com/v2/shopping/flight-offers?max=3&adults=1&excludedAirlineCodes=A3,IB&originLocationCode=BER&destinationLocationCode=ATH&departureDate=2021-09-06`

#### Find the best flight option

The [Flight Choice Prediction API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-choice-prediction) predicts the flight your users will choose.
Our machine-learning models have analyzed historical interactions with the
`Flight Offers Search` API and can determine each flight’s probability of being
chosen. Boost conversions and create a personalized experience by filtering out
the noise and showing your users the flights which are best for them.

Here is a quick cURL example piping Flight Offers Search API results directly to the prediction API.

Let’s look at flight offers for a Madrid-New York round trip (limiting to four options for this test illustration)

```bash
curl --request GET \
     --header 'Authorization: Bearer <token>' \
     --url https://test.api.amadeus.com/v2/shopping/flight-offers\?origin\=MAD\&destination\=NYC\&departureDate\=2019-08-24\&returnDate\=2019-09-19\&adults\=1 \
| curl --request POST \
       --header 'content-type: application/json' \
       --header 'Authorization: Bearer <token>' \
       --url https://test.api.amadeus.com/v2/shopping/flight-offers/prediction --data @-
```

The prediction API returns the same content as the Low Fare search with the
addition of the `choiceProbability` field for each flight offer element.

```json
 {
  "data": [
    {
      "choiceProbability": "0.9437563627430908",
      "id": "1558602440311-352021104",
      "offerItems": [...],
      "type": "flight-offer"
    },
    {
      "choiceProbability": "0.0562028823257711",
      "id": "1558602440311--1831925786",
      "offerItems": [...],
      "type": "flight-offer"
    },
    {
      "choiceProbability": "0.0000252425060482",
      "id": "1558602440311-480701674",
      "offerItems": [...],
      "type": "flight-offer"
    },
    {
      "choiceProbability": "0.0000155124250899",
      "id": "1558602440311--966634676",
      "offerItems": [...],
      "type": "flight-offer"
    }
  ],
  "dictionaries": {...}
  },
  "meta": {...}
  }
}
```

#### Multi-city Searches

Many travelers take advantage of their international trips to visit several
destinations. Multi-city search is a functionality that lets you search for
consecutive one-way flights between multiple destinations in a single request.
The returned flights are packaged as a complete, bookable itinerary. 

To perform multi-city searches, you must use the `POST` method of `Flight
Offers Search API`. The API lets you search for up to six origin and
destination city pairs.

In the following example, we’ll fly from Madrid to Paris, where we’ll spend a couple of
days, then fly to Munich for three days. Next, we’ll visit Amsterdam for two
days before finishing our journey with a return to Madrid. We'll use the
following IATA city codes: `MAD > PAR > MUC > AMS > MAD`

The request will look like this:


```bash
curl https://test.api.amadeus.com/v2/shopping/flight-offers \
-d '{ 
  "originDestinations": [ 
    { 
      "id": "1", 
      "originLocationCode": "MAD", 
      "destinationLocationCode": "PAR", 
      "departureDateTimeRange": { 
        "date": "2022-10-03" 
      } 
    }, 
    { 
      "id": "2", 
      "originLocationCode": "PAR", 
      "destinationLocationCode": "MUC", 
      "departureDateTimeRange": { 
        "date": "2022-10-05" 
      } 
    }, 
    { 
      "id": "3", 
      "originLocationCode": "MUC", 
      "destinationLocationCode": "AMS", 
      "departureDateTimeRange": { 
        "date": "2022-10-08" 
      } 
    }, 
    { 
      "id": "4", 
      "originLocationCode": "AMS", 
      "destinationLocationCode": "MAD", 
      "departureDateTimeRange": { 
        "date": "2022-10-11" 
      } 
    } 
  ], 
  "travelers": [ 
    { 
      "id": "1", 
      "travelerType": "ADULT", 
      "fareOptions": [ 
        "STANDARD" 
      ] 
    } 
  ], 
  "sources": [ 
    "GDS" 
  ], 
  "searchCriteria": { 
    "maxFlightOffers": 1 
  } 
}' 
```
#### Search using loyalty programs

`Flight Offers Price` and `SeatMap Display` APIs both accept Frequent Flyer information so end-users can benefit from their loyalty program. When adding Frequent Flyer information, please remember that each airline policy is different, and some require additional information, such as passenger name, email or phone number to validate the account. If the validation fails, your user won’t receive their loyalty program advantages.

### Check flight and fare availability

With the `Flight Availabilities Search` you can check the flight and fare availability for any itinerary. This refers to the full inventory of fares available for an itinerary at any given time. The concept of flight availability originated in the early days of flight booking as a way for agents to check what options existed for their travelers’ itineraries.

Here’s an example request for a one-way flight from Mad (MIA) to Atlanta (ATL) for one traveler departing on December 12, 2021: 

`POST https://test.api.amadeus.com/v1/shopping/availability/flight-availabilities`

```json
{
    "originDestinations": [
        {
            "id": "1",
            "originLocationCode": "MIA",
            "destinationLocationCode": "ATL",
            "departureDateTime": {
                "date": "2021-11-01"
            }
        }
    ],
    "travelers": [
        {
            "id": "1",
            "travelerType": "ADULT"
        }
    ],
    "sources": [
        "GDS"
    ]
}
```

The response contains a list of available flights matching our request criteria (for the sake of this example, we only show the first result). Each flight availability includes descriptive data about the flight and an `availabilityClasses` list containing the available fare classes and the number of bookable seats remaining in each fare class.

```json
"data": [
        {
            "type": "flight-availability",
            "id": "1",
            "originDestinationId": "1",
            "source": "GDS",
            "instantTicketingRequired": false,
            "paymentCardRequired": false,
            "duration": "PT1H54M",
            "segments": [
                {
                    "id": "1",
                    "numberOfStops": 0,
                    "blacklistedInEU": false,
                    "departure": {
                        "iataCode": "MIA",
                        "at": "2021-11-01T05:30:00"
                    },
                    "arrival": {
                        "iataCode": "ATL",
                        "terminal": "S",
                        "at": "2022-11-01T07:24:00"
                    },
                    "carrierCode": "DL",
                    "number": "2307",
                    "aircraft": {
                        "code": "321"
                    },
                    "operating": {},
                    "availabilityClasses": [
                        {
                            "numberOfBookableSeats": 9,
                            "class": "J"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "C"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "D"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "I"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "Z"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "W"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "Y"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "B"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "M"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "H"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "Q"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "K"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "L"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "U"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "T"
                        },
                        {
                            "numberOfBookableSeats": 9,
                            "class": "E"
                        }
                    ]
                }
            ]
        },
```

Note that airlines’ bookable seat counters goe up to a maximum of 9, even if more seats are available in that fare class. If there are less than 9 bookable seats available, the exact number is displayed.  

### Search branded fares

Branded fares are airfares that bundle tickets with extras, such as checked bags, seat selection, refundability or loyalty points accrual. Each airline defines and packages its own branded fares and they vary from one airline to another. Branded fares not only help build brand recognition and loyalty, but also offer travelers an attractive deal as the incremental cost of the fare is usually less than that of buying the included services à la carte.  

The `Branded Fares Upsell API` API receives flight offers from the Flight Offers Search and returns branded fares as flight offers which can be easily passed to the next step in the booking funnel. The booking flow is the following: 

- Search for flights using the Flight Offers Search. 
- Find branded fare options for a selected flight using the Branded Fares Upsell. 
- Confirm the fare and get the final price using the Flight Offers Price. 
- Book the flight using the Flight Create Orders. 

Let's see an example of how to search for branded fares. 

You can build the request by passing the flight-offer object from the Flight Offers Search into the body of the `POST` request:

```bash
POST https://test.api.amadeus.com/v1/shopping/flight-offers/upselling
```

```json
{ 
  "data": { 
    "type": "flight-offers-upselling", 
    "flightOffers": [ 
      {
            "type": "flight-offer",
            "id": "1",
            "source": "GDS",
            "instantTicketingRequired": false,
            "nonHomogeneous": false,
            "oneWay": false,
            "lastTicketingDate": "2022-06-12",
            "numberOfBookableSeats": 3,
            "itineraries": [
                {
                    "duration": "PT6H10M",
                    "segments": [
                        {
                            "departure": {
                                "iataCode": "MAD",
                                "terminal": "1",
                                "at": "2022-06-22T17:40:00"
                            },
                            "arrival": {
                                "iataCode": "FCO",
                                "terminal": "1",
                                "at": "2022-06-22T20:05:00"
                            },
                            "carrierCode": "AZ",
                            "number": "63",
                            "aircraft": {
                                "code": "32S"
                            },
                            "operating": {
                                "carrierCode": "AZ"
                            },
                            "duration": "PT2H25M",
                            "id": "13",
                            "numberOfStops": 0,
                            "blacklistedInEU": false
                        },
                        {
                            "departure": {
                                "iataCode": "FCO",
                                "terminal": "1",
                                "at": "2022-06-22T21:50:00"
                            },
                            "arrival": {
                                "iataCode": "ATH",
                                "at": "2022-06-23T00:50:00"
                            },
                            "carrierCode": "AZ",
                            "number": "722",
                            "aircraft": {
                                "code": "32S"
                            },
                            "operating": {
                                "carrierCode": "AZ"
                            },
                            "duration": "PT2H",
                            "id": "14",
                            "numberOfStops": 0,
                            "blacklistedInEU": false
                        }
                    ]
                }
            ],
            "price": {
                "currency": "EUR",
                "total": "81.95",
                "base": "18.00",
                "fees": [
                    {
                        "amount": "0.00",
                        "type": "SUPPLIER"
                    },
                    {
                        "amount": "0.00",
                        "type": "TICKETING"
                    }
                ],
                "grandTotal": "81.95",
                "additionalServices": [
                    {
                        "amount": "45.00",
                        "type": "CHECKED_BAGS"
                    }
                ]
            },
            "pricingOptions": {
                "fareType": [
                    "PUBLISHED"
                ],
                "includedCheckedBagsOnly": false
            },
            "validatingAirlineCodes": [
                "AZ"
            ],
            "travelerPricings": [
                {
                    "travelerId": "1",
                    "fareOption": "STANDARD",
                    "travelerType": "ADULT",
                    "price": {
                        "currency": "EUR",
                        "total": "81.95",
                        "base": "18.00"
                    },
                    "fareDetailsBySegment": [
                        {
                            "segmentId": "13",
                            "cabin": "ECONOMY",
                            "fareBasis": "OOLGEU1",
                            "class": "O",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "14",
                            "cabin": "ECONOMY",
                            "fareBasis": "OOLGEU1",
                            "brandedFare": "ECOLIGHT",
                            "class": "O",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        }
                    ]
                }
            ]
        } 
    ]
  } 
}  
```

### Recommend personalized destinations

The `Travel Recommendations` API  provides personalized destinations based on the traveler's location and an input destination, such as a previously searched flight destination or city of interest.

For example, for a traveler based in San Francisco who has searched for multiple flights to Barcelona, what other similar destinations the API could recommend? The API takes as input the country of the traveler and the IATA code of the city that was searched, in our case this will be US and BCN respectively. 

`GET https://test.api.amadeus.com/v1/reference-data/recommended-locations?cityCodes=BCN&travelerCountryCode=US`

The response will look like this:

```json
{
     "type": "flight-date",
     "origin": "SFO",
     "destination": "ROM",
     "departureDate": "2021-09-19",
     "returnDate": "2021-09-23",
     "price": {
         "total": "348.75"
     },
     "links": {
         "flightDestinations": "https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=SFO&departureDate=2021-04-15,2021-10-11&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
         "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=SFO&destinationLocationCode=ROM&departureDate=2021-09-19&returnDate=2021-09-23&adults=1&nonStop=false"
     }
 }
```

 If you want to take it to the next level, you can call the `Flight Cheapest Date Search` API to let the users know not only the recommended destinations but also what are the cheapest dates to visit any of these cities. For real-time flights, you can also call the `Flight Offers Search` API. The Travel Recommendations API has returned links to both APIs. 

### Recommend nearby destinations 

With the `Airport Nearest Relevant` API you can find the closest major airports to a starting point. By default, results are sorted by relevance but they can also be sorted by `distance`, `flights`, `travelers` using the parameter `sort`.

!!!information
    To get the latitude and longitude of a city you can use the `Airport & City Search` API using the city's IATA code.

Let's call the Airport Nearest Relevant API to find airports within the 500km radius of Madrid.

`GET https://test.api.amadeus.com/v1/reference-data/locations/airports?latitude=40.416775&longitude=-3.703790&radius=500`

A part of the response looks like:
 
```json
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "AIRPORT",
            "detailedName": "BARCELONA/ES:AIRPORT",
            "timeZoneOffset": "+02:00",
            "iataCode": "BCN",
            "geoCode": {
                "latitude": 41.29694,
                "longitude": 2.07833
            },
            "address": {
                "cityName": "BARCELONA",
                "cityCode": "BCN",
                "countryName": "SPAIN",
                "countryCode": "ES",
                "regionCode": "EUROP"
            },
            "distance": {
                "value": 496,
                "unit": "KM"
            },
            "analytics": {
                "flights": {
                    "score": 25
                },
                "travelers": {
                    "score": 25
                }
            },
            "relevance": 5.11921
        }
```
What we want to do at this point, is to find the cheapest dates for all these destinations. 

We can do this by calling the `Flight Cheapest Date` API which finds the cheapest dates to travel from one city to another. Let's see, for example, the cheapest dates to fly to Barcelona in November 2021. 

`GET https://test.api.amadeus.com/v1/shopping/flight-dates?origin=MAD&destination=BCN&departureDate=2021-05-01,2021-05-30`

```json
{
    "type": "flight-date",
    "origin": "MAD",
    "destination": "BCN",
    "departureDate": "2021-05-29",
    "returnDate": "2021-06-11",
    "price": {
        "total": "73.61"
    },
    "links": {
        "flightDestinations": "https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD&departureDate=2021-05-01,2021-05-30&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=BCN&departureDate=2022-09-29&returnDate=2021-06-11&adults=1&nonStop=false"
    },
{
    "type": "flight-date",
    "origin": "MAD",
    "destination": "BCN",
    "departureDate": "2021-05-05",
    "returnDate": "2021-05-06",
    "price": {
        "total": "79.67"
    },
    "links": {
        "flightDestinations": "https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD&departureDate=2021-05-01,2021-05-30&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=BCN&departureDate=2021-05-05&returnDate=2021-05-06&adults=1&nonStop=false"
    }
},
{
    "type": "flight-date",
    "origin": "MAD",
    "destination": "BCN",
    "departureDate": "2021-05-02",
    "returnDate": "2021-05-06",
    "price": {
        "total": "80.61"
    },
    "links": {
        "flightDestinations": "https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD&departureDate=2021-05-01,2021-05-30&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
        "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=BCN&departureDate=2021-05-02&returnDate=2021-05-06&adults=1&nonStop=false"
    }
}
```
As you can see above, in the results we have a list of dates for a roundtrip from Madrid to Barcelona ordered by the lowest price.

In the last step, we want to let the traveler perform a flight search for any of the above dates that are convenient for them. That is very easy with our APIs, as the `Flight Cheapest Date` API for each result contains a link to the `Flight Offers Search` API. For example, if we want to perform a flight search for the first result, we only have to take the link provided and make an API call:

`GET https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MAD&destinationLocationCode=BCN&departureDate=2021-05-29&returnDate=2021-06-11&adults=1&nonStop=false`

## Confirm Fares

The availability and price of airfare fluctuate, so it’s important to confirm
before proceeding to book. This is especially true if time passes between the
initial search and the decision to book, as fares are limited and there are
thousands of bookings occurring every minute. During this step, you can also
add ancillary products like extra bags or legroom. For that you can use the [Flight Offers Price API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-price).

Once a flight has been selected, you’ll need to confirm the availability and
price of the fare. This is where the Flight Offers Price API comes in. This API
returns the final fare price \(including taxes and fees\) of flights from the
Flight Offers Search API as well as pricing for ancillary products and the
payment information that will be needed to make the final booking. 

The body to be sent via `POST` is built by a new object of type
`flight-offers-pricing` composed by a list of `flight-offers` (up to 6) +
payment information.

```json
{
   "data": {
        "type": "flight-offers-princing",
        "flightOffers": [
            { "type": "flight-offer" }
        ],
        "payment" : [
            { Payment_Object }
        ]
    }
```
## Return fare rules

The `Flight Offers Price` API confirms the final price and availability of a fare. It also returns detailed fare rules, including the cancellation policy and other information. To get the fare rules, add the parameter `include=detailed-fare-rules` to your API call, as shown below: 

```bash
POST https://test.api.amadeus.com/v1/shopping/flight-offers/pricing?include=detailed-fare-rules
```

## Book a Flight

Once the fare is confirmed, you’re ready to use the `Flight Create Orders` API
to perform the actual booking. This API lets you log a reservation in the
airlines’ systems and create a [PNR](https://developers.amadeus.com/blog/what-is-pnr-booking-reference), and returns a unique Id number and the
reservation details. If you’re using an airline consolidator, the PNR will be
automatically sent to the consolidator for ticket issuance. [Visit the Flight
Create Orders documentation
page](https://developers.amadeus.com/self-service/category/air/api-doc/flight-create-orders)
for more details on this API.

Remember, you need to be able to issue a ticket to make bookings with our
Flight Create Order API. To access the API in production, you need to either
sign a contract with an airline consolidator or be accredited to issue tickets
yourself. 

You can see the process step to step in this [video tutorial](https://www.youtube.com/watch?v=OEX7k6d52Ic&feature=youtu.be).

If you are interested in knowing more about issuing tickets in travel industry, please check out this [article](https://developers.amadeus.com/blog/what-is-air-ticketing). 

## Issue a ticket

Once the booking is made, you need to complete payment. In most cases, you’ll
receive payment from the customer and then pay the airline, typically via an
industry-specific settlement procedure like the BSP or ARC \(more on those
later\).

In the final step, a flight ticket is issued. In industry terms, a flight
ticket is a confirmation that payment has been received, the reservation has
been logged, and the customer has the right to enjoy the flight. For [IATA
member airlines](https://www.iata.org/about/members/Pages/airline-list.aspx),
only certain accredited parties can issue tickets. In the next section, we’ll
go into detail about your options for managing this final step in the booking
process.

## The aircraft cabin layout

With the SeatMap Display API you can view the aircraft cabin layout: 

- `deckConfiguration` - the dimensions of the passenger deck in (x,y) coordinates, including the location of the wings, exit rows, and cabins. These dimensions form a grid on which you will later place facilities and seats.
- `facilities` - the (x,y) coordinates of aircraft facilities, such as bathrooms or galleys.
- `seats` - the (x,y) coordinates of all seats on the aircraft, with their respective availability status, characteristics, and prices.

To help you build a more consistent display, the API returns a uniform width for all cabins and classes. Rows with special seating like business class or extra-legroom seats have fewer seats per row (e.g., 4 seats for width of 7 coordinates) than economy rows (e.g. 7 seats for a width of 7 coordinates).

Check out this [video tutorial](https://youtu.be/uTOQjGsZLfI) for more details. 

### Display in-flight amenities

Both endpoints of the SeatMap Display API return information about the following in-flight amenities:

- Seat
- Wi-fi
- Entertainment
- Power
- Food
- Beverage

### Select a seat 

Requests to either endpoint of SeatMap Display will return a list of seating options with their characteristics, pricing, and coordinates. Let's look at an example response:

```json
{
                "cabin": "M",
                "number": "20D",
                "characteristicsCodes": [
                  "A",
                  "CH",
                  "RS"
                ],
                "travelerPricing": [
                  {
                    "travelerId": "1",
                    "seatAvailabilityStatus": "AVAILABLE",
                    "price": {
                      "currency": "EUR",
                      "total": "17.00",
                      "base": "17.00",
                      "taxes": [
                        {
                          "amount": "0.00",
                          "code": "SUPPLIER"
                        }
                      ]
                    }
                  }
                ],
                "coordinates": {
                  "x": 10,
                  "y": 4
                }
              },
```

For each seat, the SeatMap Display API provides a seatAvailabilityStatus so you can indicate which seats are currently available for booking. Seats may have one of three availability statuses:

- `AVAILABLE` – the seat is not occupied and is available to book.
- `BLOCKED` – the seat is not occupied but isn’t available to book for the user. This is usually due to the passenger type (e.g., children may not sit in exit rows) or their fare class (e.g., some seats may be reserved for flyers in higher classes).
- `OCCUPIED` – the seat is  occupied and unavailable to book.

If a flight is fully booked, the API returns an OCCUPIED status for all seats. In most cases, fully booked flights are filtered out during search with Flight Offers Search or when confirming the price with Flight Offers Price. Flight Create Orders returns an error message if you try to book an unavailable seat. For more information on the booking flow, check out how to build a flight booking engine.

Once your user has selected their seat, the next step is to add the desired seat to the flight offer and prepare them for booking.

In the above example response, seat `20D` is indicated as `AVAILABLE`. For your user to be able to book the seat, you must add the seat to the flightOffer object and call `Flight Offers Price` to get a final order summary with the included seat.

To include the seat in the `flightOffer` object, add it to `fareDetailsBySegment` → `additionalServices` → `chargeableSeatNumber`, as shown below:

```json
"fareDetailsBySegment": [
            {
            "additionalServices": {
             "chargeableSeatNumber": "20D"
              },
              "segmentId": "60",
              "cabin": "ECONOMY",
              "fareBasis": "NLYO5L",
              "brandedFare": "LITE",
              "class": "N",
              "includedCheckedBags": {
                "quantity": 0
              }
            }
          ]
```

Flight Offers Price then returns the `flightOffer` object with the price of the chosen seat included within `additionalServices`:

```json
"additionalServices":
            {
              "type": "SEATS",
              "amount": "17.00"
            }
```

You can use the same process to select seats for multiple passengers. For each passenger, you must add the selected seats in `fareDetailsBySegment` for each `travelerId` within the flight offer.

At this point, you now have a priced `flightOffer` which includes your user's selected seat. The final step is to book the flight using `Flight Create Orders API`. To do this, simply pass the `flightOffer` object into a request to the Flight Create Orders API, which will book the flight and return an order summary and a booking Id.

## Add additional baggage

### Search additional baggage options

The first step is to find the desired flight offer using the `Flight Offers Search` API. Each flight offer contains an `additionalServices` field with the types of additional services available, in this case bags, and the maximum price of the first additional bag. Note that at this point, the price is for informational purposes only.  

To get the final price of the added baggage with the airline policy and the traveler's tier level taken into account, you must call `Flight Offers Price`. To do this, add the `include=bags` parameter in the path of the Flight Offers Price API: 

```bash
POST https://test.api.amadeus.com/v1/shopping/flight-offers/pricing?include=bags 
```

As you see below, the API returns the catalog of baggage options with the price and quantity (or weight): 

```json
"bags": { 
    "1": { 
        "quantity": 1, 
        "name": "CHECKED_BAG", 
        "price": { 
            "amount": "25.00", 
            "currencyCode": "EUR" 
        }, 
        "bookableByItinerary": true, 
        "segmentIds": [ 
            "1", 
            "14" 
        ], 
        "travelerIds": [ 
            "1" 
        ] 
    } 
    "2": {  
        "quantity": 2, 
        "name": "CHECKED_BAG", 
        "price": { 
            "amount": "50.00", 
            "currencyCode": "EUR" 
        }, 
        "bookableByItinerary": true, 
        "segmentIds": [ 
            "1", 
            "14" 
        ], 
        "travelerIds": [ 
            "1" 
        ] 
    } 
} 
```

The `Flight Offers Price` API returns two bag offers for the given flight. The catalog shows that either one or two bags are available to be booked per passenger. Higher bag quantity will be rejected due to the airline's policy.

In the example above, the price of two bags is double that of one bag, though some airlines do offer discounts for purchasing more than one checked bag. Each bag offer is coupled to the specific segment and traveler Id returned in each bag offer. 

If there is no extra baggage service available, the API won’t return a baggage catalog. 

### Add additional baggage to the flight offer

Next, you need to add the additional baggage to the desired flight segments. This gives you the flexibility to include extra bags on only certain segments of the flight.  

Fill in `chargeableCheckedBags` with the desired quantity (or weight, depending on what the airline returns) in `travelerPricings/fareDetailsBySegment/additionalServices`, as shown below:

```json
"fareDetailsBySegment": [{ 
    "segmentId": "1", 
    "cabin": "ECONOMY", 
    "fareBasis": "TNOBAGD", 
    "brandedFare": "GOLIGHT", 
    "class": "T", 
    "includedCheckedBags": { 
        "quantity": 0 
    }, 
    "additionalServices": { 
        "chargeableCheckedBags": { 
            "quantity": 1 
        } 
    } 
}] 
```

### Confirm the final price and book

Once you’ve added the desired bags to the flight order, you need to call Flight Offers Price API to get the final price of the flight with all additional services included. Once this is done, you can then call the `Flight Create Orders` API to book the flight. If you want to add different numbers of bags for different itineraries, you can do it following the same flow. 

If the desired flight you want to book, does not permit the additional service, `Flight Create Orders` will reject the booking and return the following error:

```json
{ 
    "errors": [{ 
        "status": 400, 
        "code": 38034, 
        "title": "ONE OR MORE SERVICES ARE NOT AVAILABLE", 
        "detail": "Error booking additional services" 
    }] 
} 
```

## Cancel a reservation

Just as you can help users book a flight with the Flight Create Orders, you can now also help them cancel their reservations with the [Flight Order Management](https://developers.amadeus.com/self-service/category/air/api-doc/flight-order-management) API. However, you have a limited window of time to cancel via API. If you’re working with an airline consolidator for ticketing, cancellations via API are generally only allowed while the order is queued for ticketing. Once the ticket has been issued, you’ll have to contact your consolidator directly to handle the cancellation.

To call the Flight Order Management, you have pass as a parameter the flight-orderId from the Flight Create Orders API, such as:

```bash
DELETE https://test.api.amadeus.com/v1/booking/flight-orders/eJzTd9f3NjIJdzUGAAp%2fAiY
```

## View reservation details

With the Flight Order Management API you can consult and check your flight reservation. 

To call Flight Order Management, you have pass as a parameter the flight-orderId from the Flight Create Orders API, such as:

```bash
GET https://test.api.amadeus.com/v1/booking/flight-orders/eJzTd9f3NjIJdzUGAAp%2fAiY
```

## Common Errors

### Issuance not allowed in Self Service

Self-Service users must work with an airline consolidator that can issue
tickets on your behalf. In that case, the payment is not processed by the API
but directly between you and the consolidator. Adding a form of payment to
the Flight Create Orders API will be rejected by error INVALID FORMAT.

### Price discrepancy 

The price of airfare fluctuates constantly. Creating an order for a flight whose price is no longer valid at the time of booking will trigger the
following error:

```json
{
  "errors": [
    {
      "status": 400,
      "code": 37200,
      "title": "PRICE DISCREPANCY",
      "detail": "Current grandTotal price (2780.28) is different from request one (2779.58)"
    }
  ]
}
```

If you receive this error, reconfirm the fare price with the Flight Offers Price API before booking.


The following is a common error in the test environment, as you can perform many bookings without restrictions (no real payment), but the inventory is a copy of the real one, so if you book many seats, the inventory will be empty and you won't be able to book anymore.

```json
{
            "status": 400,
            "code": 34651,
            "title": "SEGMENT SELL FAILURE",
            "detail": "Could not sell segment 1"
        }
```

## Notes

### Carriers and rates

- Low cost carriers (LCCs), American Airlines are not available. Depending on the market, British Airways is also not available.
- Published rates only returned in Self-Service. Cannot access to negotiated rates, or any other special rates. 

### Post-booking modifications 

With the current version of our Self-Service APIs, you can’t add additional baggage after the flight has been booked. This and other post-booking modifications must be handled directly with the airline consolidator that is issuing tickets on your behalf.   

### How payment works

There are two things to consider regarding payments for flight booking:

- The payment between you (the app owner) and your customers (for the services provided + the price of the flight ticket). You decide how to collect this payment, it is not included in the API. A third party payment gateway, such as Stripe will be an easier solution for this.
- The payment between you and the consolidator (to be able to pay the airline and issue the flight ticket). This will be done between you and your consolidator of choice, and is to be agreed with the consolidator.
