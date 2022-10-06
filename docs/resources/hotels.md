# Hotels

| APIs                                                                                                                                                          | Description                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Amadeus Hotel APIs](https://developers.amadeus.com/self-service/category/hotel) | Lets you search, compare and book rooms at over 350 of the world’s top hotel chains and enrich your product with detailed information, descriptions, and ratings.                |
| [Hotel List API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-list/api-reference) | Returns the name, address, geoCode, and time zone for each hotel bookable in Amadeus. |
| [Hotel Ratings API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-ratings/api-reference) | Uses sentiment analysis of hotel reviews to provide an overall hotel ratings and ratings for categories like location, comfort, service, staff, internet, food, facilities, pool or sleep quality. |
| [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search/api-reference) | Provides a list of the cheapest hotels in a given location with detailed information on each hotel and the option to filter by category, chain, facilities or budget range.  |
| [Hotel Booking API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-booking/api-reference) | Lets you complete bookings at over 150,000 hotels and accommodations around the world. |


The [Amadeus Hotel APIs](https://developers.amadeus.com/self-service/category/hotel) lets you search, compare and book rooms at over 350 of the world’s top hotel chains and enrich your product with detailed information, descriptions, and ratings. 

Let's learn how to get started and help your users book the perfect rooms at over 150,000 hotels worldwide.

!!! information
    This page has been updated based on `Hotel Search V3` updates since MAY 2022. 

## Search hotels

### Get a list of hotels by location 

First, users should be able to search hotels for a given location. The [Hotel List API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-list/api-reference) returns the list of hotels based on a city or a geographic code. To answer a question, such as **"what are the hotels closed to the city hall?"** the `Hotel List API` has three endpoints to utilize based on your search criteria. It returns `hotel name`, `location`, and `hotel id` for you to proceed to the next steps of the hotel search. 

Based on the search criteria, you will get the list of `hotelId` with hotel information as in the example below.

```json
        {
            "chainCode": "AC",
            "iataCode": "PAR",
            "dupeId": 700169556,
            "name": "ACROPOLIS HOTEL PARIS BOULOGNE",
            "hotelId": "ACPARH29",
            "geoCode": {
                "latitude": 48.83593,
                "longitude": 2.24922
            },
            "address": {
                "countryCode": "FR"
            },
            "lastUpdate": "2022-03-01T15:22:17"
        }
```

#### Search hotels by a city or Geocode 

You can specify an [IATA city code](https://www.iata.org/en/publications/directories/code-search/) or Geocode to search a more specific area to get the list of hotels. You can customize the request using parameters, such as radius, chain code, amenities, star ratings, and hotel source. 

For example: 

Using the `by-city` endpoint, get a list of hotels in Paris with a swimming pool and more than four stars:

```bash
GET https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=PAR&amenities=SWIMMING_POOL&ratings=4,5
```

Using the `by-geocode` endpoint, get a list of hotels in Paris (latitude=41.397158 and longitude=2.160873):

```bash
GET https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-geocode?latitude=41.397158&longitude=2.160873
```

#### Search hotels by hotel ids

If you already know the Id of a hotel that you would like to check, you can use it to call the [Hotel List API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-list/api-reference). 

```bash
GET https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-hotels?hotelIds=ACPARF58
```

### Autocomplete Hotel Names 

`Hotel Name Autocomplete API` - to be updated 

### Display Hotel Ratings

When users search for hotels in a desired area, they may wonder about the hotel rating. [Hotel Ratings API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-ratings/api-reference) returns ratings for many crucial elements of a hotel, such as sleep quality, services, facilities, room comfort, value for money, location and many others. [Hotel Ratings API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-ratings/api-reference) guarantees high-quality service for your customers.

The sentiment analysis, just like the one below, is displayed in a simple flow to allow you to easily identify the best hotels based on traveler reviews:

```bash
GET https://test.api.amadeus.com/v2/e-reputation/hotel-sentiments?hotelIds=TELONMFS,ADNYCCTB,XXXYYY01
```

```json
{ "data": [  {
    "type": "hotelSentiment",
    "numberOfReviews": 218,
    "numberOfRatings": 278,
   "hotelId": "ADNYCCTB",
    "overallRating": 93,
    "sentiments": {
      "sleepQuality": 87,
      "service": 98,
      "facilities": 90,
      "roomComforts": 92,
      "valueForMoney": 87,
      "catering": 89,
      "location": 98,
      "pointsOfInterest": 91,
      "staff": 100
    }
  },
  {
    "type": "hotelSentiment",
    "numberOfReviews": 2667,
    "numberOfRatings": 2666,
    "hotelId": "TELONMFS",
    "overallRating": 81,
    "sentiments": {
      "sleepQuality": 78,
      "service": 80,
      "facilities": 75,
      "roomComforts": 87,
      "valueForMoney": 75,
      "catering": 81,
     "location": 89,
      "internet": 72,
      "pointsOfInterest": 81,
      "staff": 89
    }
  }
]
```

With these additional filters, your booking process becomes more efficient and you can offer your customers an enriched shopping experience. In this way, you can be confident that you are offering a highly rated hotels selection in the areas that customers appreciate the most.


## Check Availabilities and Prices

Once users have explored the list of hotels in their desired area, they would want to check the price of a specific hotel or compare the prices of hotels on the list. With the `hotelIds` that you got from [Hotel List API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-list/api-reference), you now can check the available rooms with real-time prices and room descriptions by calling the [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search/api-reference). 

An example to request available rooms and prices for one room in Hilton Paris Opera for one adult with check-in date 2022-11-22:

```bash
GET https://test.api.amadeus.com/v3/shopping/hotel-offers?hotelIds=HLPAR266&adults=1&checkInDate=2022-11-22&roomQuantity=1
```

The API returns a list of `offers` objects containing the price of the cheapest available room as well as information including the room description and payment policy. 

!!! Note
    The response of `Hotel Search V3` contains real-time data, so you don't need an additional validation step anymore. However, as there are thousands of people reserving hotels at any given second, the availability of a given room may change between the moment you search and the moment you decide to book. It is therefore advised that you proceed with booking **as soon as possible** or **add a validation step** by searching by `offerid` described below.

```json
{
    "data": [
        {
            "type": "hotel-offers",
            "hotel": {
                "type": "hotel",
                "hotelId": "HLPAR266",
                "chainCode": "HL",
                "dupeId": "700006199",
                "name": "Hilton Paris Opera",
                "cityCode": "PAR",
                "latitude": 48.8757,
                "longitude": 2.32553
            },
            "available": true,
            "offers": [
                {
                    "id": "ZBC0IYFMFV",
                    "checkInDate": "2022-11-22",
                    "checkOutDate": "2022-11-23",
                    "rateCode": "RAC",
                    "rateFamilyEstimated": {
                        "code": "PRO",
                        "type": "P"
                    },
                    "commission": {
                        "percentage": "8"
                    },
                    "room": {
                        "type": "A07",
                        "typeEstimated": {
                            "category": "SUPERIOR_ROOM"
                        },
                        "description": {
                            "text": "ADVANCE PURCHASE\nSUPERIOR ROOM\nFREE WIFI/AIRCON\nHD/ SAT TV/SAFE",
                            "lang": "EN"
                        }
                    },
                    "guests": {
                        "adults": 1
                    },
                    "price": {
                        "currency": "EUR",
                        "base": "359.01",
                        "total": "361.89",
                        "taxes": [
                            {
                                "code": "TOTAL_TAX",
                                "pricingFrequency": "PER_STAY",
                                "pricingMode": "PER_PRODUCT",
                                "amount": "2.88",
                                "currency": "EUR",
                                "included": false
                            }
                        ],
                        "variations": {
                            "average": {
                                "base": "359.01"
                            },
                            "changes": [
                                {
                                    "startDate": "2022-11-22",
                                    "endDate": "2022-11-23",
                                    "base": "359.01"
                                }
                            ]
                        }
                    },
                    "policies": {
                        "deposit": {
                            "acceptedPayments": {
                                "creditCards": [
                                    "VI",
                                    "CA",
                                    "AX",
                                    "DC",
                                    "DS",
                                    "JC",
                                    "CU"
                                ],
                                "methods": [
                                    "CREDIT_CARD"
                                ]
                            }
                        },
                        "paymentType": "deposit",
                        "cancellation": {
                            "amount": "361.89",
                            "type": "FULL_STAY",
                            "description": {
                                "text": "Non refundable rate",
                                "lang": "EN"
                            }
                        }
                    },
                    "self": "https://api.amadeus.com/v3/shopping/hotel-offers/ZBC0IYFMFV",
                    "cancelPolicyHash": "F1DC3A564AF1C421C90F7DB318E70EBC688A5A70A93B944F6628D0338F9"
                }
            ],
            "self": "https://api.amadeus.com/v3/shopping/hotel-offers?hotelIds=HLPAR266&adults=1&checkInDate=2022-11-22&roomQuantity=1"
        }
    ]
}

```

If the time between displaying prices and booking the room is long enough to allow others to book the same room, you can consider requesting [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search/api-reference) again with the `offerid` that you got before. This is not mandatory as you always will see if the offer is available or not when you try to book the offer.

An example to request the offer information with `offer id`: 

```bash
GET https://test.api.amadeus.com/v3/shopping/hotel-offers/ZBC0IYFMFV
```

Now that you have found the available offer (and its `offerId`) with the price, you're ready to book! 


## Booking the Hotel

The [Hotel Booking API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-booking/api-reference) is the final step in the hotel booking flow. By making a `POST` request with the offer Id returned by the Hotel Search API, the guest information, and the payment information, you can create a booking directly in the hotel reservation system. 

```bash
POST https://test.api.amadeus.com/v1/booking/hotel-bookings \
{
  "data": {
    "offerId": "ZBC0IYFMFV",
    "guests": [
      {
        "id": 1,
        "name": {
          "title": "MR",
          "firstName": "BOB",
          "lastName": "SMITH"
        },
        "contact": {
          "phone": "+33679278416",
          "email": "bob.smith@email.com"
        }
      }
    ],
    "payments": [
      {
        "id": 1,
        "method": "creditCard",
        "card": {
          "vendorCode": "VI",
          "cardNumber": "4151289722471370",
          "expiryDate": "2023-08"
        }
      }
    ],
    "rooms": [
      {
        "guestIds": [
          1
        ],
        "paymentId": 1,
        "specialRequest": "I will arrive at midnight"
      }
    ]
  }
}'
```

Congratulations! You’ve just performed your first hotel booking! Once the reservation is made, the API will return **a unique booking confirmation ID** which you can send to your users. 

### Notes about Payment

The Hotel Search API returns information about the payment policy of each hotel. The main policy types are: 

- **Guarantee**: the hotel will save credit card information during booking but not make any charges to the account. In the case of a no-show or out-of-policy cancellation, the hotel may charge penalties to the card. 
- **Deposit**: at the time of booking or by a given deadline, the hotel will charge the guest a percentage of the total amount of the reservation. The remaining amount is paid by the traveler directly at the hotel. 
- **Prepay**: the total amount of the reservation fee must be paid by the traveler when making the booking. 

The current version of the [Hotel Booking API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-booking/api-reference) only permits booking at hotels that accept credit cards. During the booking process, Amadeus passes the payment and guest information to the hotel but does not validate this information. Be sure to validate the payment and guest information, as invalid information may result in the reservation being canceled. 

As soon as your application stores transmits, or processes cardholder information, you will need to comply with PCI Data Security Standard (PCI DSS). For more information, visit the [PCI Security Council website](https://www.pcisecuritystandards.org/merchants). 


## Guide for multiple hotel rooms

Now that we have gone through the hotel booking flow, you may wonder how to proceed to booking more than two rooms in a hotel. 

### Check availability and prices for multiple rooms 

The first step to booking multiple rooms is to search for hotels in your destination with the desired number of available rooms. You can do this by specifying the `roomQuantity` parameter when you call the [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search/api-reference) using the `hotelid` that you got from the [Hotel List API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-list/api-reference). 

Here is an example of a search in Hilton Paris for **two rooms** for **three adults**: 

```bash
GET https://test.api.amadeus.com/v3/shopping/hotel-offers?hotelIds=HLPAR266&adults=3&checkInDate=2022-11-22&roomQuantity=2
```

The API will then return the available offers where `roomQuantity`is equal to 2.

```json
 "offers": [ 
            { 
                "id": "48E6C8C7DAA0BA5C22663E2A2A2B7629F5468BCBE2722FE4AB8174", 
                "roomQuantity": "2", 
                "checkInDate": "2022-11-22", 
                "checkOutDate": "2022-11-23",
```
### Book multiple rooms with details for one guest

To call the [Hotel Booking API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-booking/api-reference), you must provide details for at least one guest per offer (the offer contains all rooms for the reservation). For example, the JSON query below provides details of one guest to book two rooms by `offerId`: 

```json
{ 
   "data":{ 
      "offerId":"F837D841218665647003CC9A8CA2A37CEC7276BBE14F9B9C525FBD1B7B69A8FF", 
      "guests":[ 
         { 
            "name":{ 
               "title":"MR", 
               "firstName":"BOB", 
               "lastName":"SMITH" 
            }, 
            "contact":{ 
               "phone":"+33679278416", 
               "email":"bob.smith@email.com" 
            } 
         } 
      ], 
      "payments":[ 
         { 
            "method":"creditCard", 
            "card":{ 
               "vendorCode":"VI", 
               "cardNumber":"4111111111111111", 
               "expiryDate":"2026-01" 
            } 
         } 
      ] 
   } 
} 
```
Once the booking is complete, the API will return the following confirmation:

```json
{ 
    "data": [ 
        { 
            "type": "hotel-booking", 
            "id": "HA_36000507", 
            "providerConfirmationId": "36000507", 
            "associatedRecords": [ 
                { 
                    "reference": "R622XL", 
                    "originSystemCode": "GDS" 
                } 
            ] 
        }, 
        { 
            "type": "hotel-booking", 
            "id": "HA_36000506", 
            "providerConfirmationId": "36000506", 
            "associatedRecords": [ 
                { 
                    "reference": "R622XL", 
                    "originSystemCode": "GDS" 
                } 
            ] 
        } 
    ] 
}
```

### Book multiple rooms with guest distribution

One common question is how to assign guest distribution among the booked rooms. 

When you call the [Hotel Booking API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-booking/api-reference), the `rooms` object represents the rooms. Each room contains guests distributed per room. Specifically, each `room` object needs IDs of the guests staying in that room.  

Below is a sample request to book two rooms with guest distribution. The first room is for guest ID’s `1` & `2` and the second room for guest Id `3`.

```json

{ 
  "data": { 
    "offerId": "4A449AE835DD68F2E7C3571740FD00B76209D7311E719E3B66DE4E1100", 
    "guests": [ 
      { 
        "id": 1, 
        "name": { 
          "title": "MR", 
          "firstName": "BOB", 
          "lastName": "SMITH" 
        }, 
        "contact": { 
          "phone": "+33679278416", 
          "email": "bob.smith@email.com" 
        } 
      }, 
      { 
        "id": 2, 
        "name": { 
          "title": "MRS", 
          "firstName": "EMILY", 
          "lastName": "SMITH" 
        }, 
        "contact": { 
          "phone": "+33679278416", 
          "email": "bob.smith@email.com" 
        } 
      }, 
      { 
        "id": 3, 
        "name": { 
          "firstName": "JOHNY", 
          "lastName": "SMITH" 
        }, 
        "contact": { 
          "phone": "+33679278416", 
          "email": "bob.smith@email.com" 
        } 
      } 
    ], 
    "payments": [ 
      { 
        "id": 1, 
        "method": "creditCard", 
        "card": { 
          "vendorCode": "VI", 
          "cardNumber": "4151289722471370", 
          "expiryDate": "2026-08" 
        } 
      } 
    ], 
    "rooms": [ 
      { 
        "guestIds": [ 
          1, 2 
        ], 
        "paymentId": 1, 
        "specialRequest": "I will arrive at midnight" 
      }, 
      { 
        "guestIds": [ 
          3 
        ], 
        "paymentId": 1, 
        "specialRequest": "I will arrive at midnight" 
      } 
    ] 
  } 
} 
```

The API response will be the same as when you booked multiple rooms using the details of just one guest:

```json
{ 
    "data": [ 
        { 
            "type": "hotel-booking", 
            "id": "XK_88803316", 
            "providerConfirmationId": "88803316", 
            "associatedRecords": [ 
                { 
                    "reference": "MJ6HLK", 
                    "originSystemCode": "GDS" 
                } 
            ] 
        }, 
        { 
            "type": "hotel-booking", 
            "id": "XK_88803315", 
            "providerConfirmationId": "88803315", 
            "associatedRecords": [ 
                { 
                    "reference": "MJ6HLK", 
                    "originSystemCode": "GDS" 
                } 
            ] 
        } 
    ]​ 
```

## Common Errors

### AcceptedPayments must be creditCards 

The current version of the [Hotel Booking API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-booking/api-reference) only supports credit card payments, which are accepted by most hotels. The [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search/api-reference) returns the payment policy of each hotel under `acceptedPayments` in the policies section.

###  Empty response from the View Room endpoint  

If you get an empty response from the Hotel Search API’s second endpoint, then the hotel is fully booked and has no vacancy for the requested dates. If you don't use the `checkInDate` and `checkOutDate` parameters in the request, the API will return results for a one-night stay starting on the current date. If the hotel is full, the response will be empty. 

### No rooms available at requested property

```json
{
    "errors": [
        {
            "status": 400,
            "code": 3664,
            "title": "NO ROOMS AVAILABLE AT REQUESTED PROPERTY"
        }
    ]
}
```

The offer for the selected Hotel is no longer available. Please select a new one.

