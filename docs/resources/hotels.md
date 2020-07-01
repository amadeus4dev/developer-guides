# Hotels

The Amadeus Hotel Search and Hotel Booking APIs let you build a complete hotel
booking engine in four easy steps. Learn how to get started and help your users
book the perfect room at over 150,000 hotels worldwide.

The three endpoints of the Hotel Search API let your users search hotels by
destination, compare rates and rooms and get the final price of the stay. Once
a room and rate are selected, you can help them complete the reservation with
the Hotel Booking API. Here’s how it works.

## Searching Hotels

The API allows you to search for hotels for a given location and time. The
endpoints are designed from the perspective of a funnel; i.e. to search broadly
for all hotels, narrow down to a particular hotel and eventually its unique
offers. A host of parameters allow the user to filter the response as per
his/her need. This API thus renders enormous capabilities to build solutions
for travelers not only for the hotels space, but also complement other travel
scenarios or enrich apps with hotel-related information. 

### Search hotels by location

The first endpoint `/shopping/hotel-offers` provides a list of available hotels
in a chosen location, which is defined by a city code or a set of GPS
coordinates. You can customize the request with parameters like chain name,
amenities, star ratings, board type and more. 

```bash
curl https://test.api.amadeus.com/v2/shopping/hotel-offers?cityCode=LON
```

The API returns a list of `hotel-offers` objects containing the price of the
cheapest available room as well as information including the `hotelId`, location,
address, rating, description, amenities, contact information. 

!!! information
    The API returns cached prices. To get real-time prices and
    availability for a specific hotel, you’ll need to move to the second endpoint. 

###  See rates for a chosen hotel 

After selecting a hotel, the next step in the booking flow is to get a list the
available offers. Hotel offers are various combinations of rooms, services and
prices. A standard room or a studio suite? One bed or two? With breakfast and
free cancellation? These are the factors that make up a hotel offer.

To get a list of `hotel-offers` for your desired hotel, just pass the `hotelId`
from the response of the 1st endpoint into the request to the 2nd endpoint:

```bash
curl https://test.api.amadeus.com/v2/shopping/hotel-offers/by-hotel?hotelId=BGLONBGB
```

Where `BGLONBGB` belongs to the `hotelId` returned by the first endpoint. The
endpoint will return a new list of `hotel-offers` objects, together with a 
list of `offers`:

```json
"offers": [
    {
        "id": "Y0UE4D1MUT",
        "checkInDate": "2020-07-01",
        "checkOutDate": "2020-07-02",
        "rateCode": "PRO",
        "rateFamilyEstimated": {
            "code": "PRO",
            "type": "P"
        },
        "commission": {
            "percentage": "4.00"
        },
        "boardType": "ROOM_ONLY",
        "room": {
            "type": "ROH",
            "typeEstimated": {
                "category": "STANDARD_ROOM"
            }
        }
    }
```


### Get the final price and conditions

The third step is to confirm the final price and availability of the chosen
offer and get the full conditions. As there are thousands of people reserving
hotels at any given second, the availability of a given room may change between
the moment you search and the moment you decide to book. If you don’t confirm
the price and availability, you may receive an error when it comes time to make
the reservation. 

The 3rd endpoint also returns the full conditions of the offer including
cancellation policy, accepted methods of payment and a complete description of
what’s included in the offer.

```bash
curl https://test.api.amadeus.com/v2/shopping/hotel-offers/Y0UE4D1MUT
```

This endpoint takes the offer Id obtained in the previous step as a URL
parameter. 

Now that you have found the offer (and its Id) you want and confirmed the price and
availability, you're ready to book! 


## Booking the Hotel

The Hotel Booking API is the final step in the booking flow. By making a `POST`
request with the offer Id returned by the Hotel Search API, the guest
information and the payment information, you can create a booking directly on
the hotel reservation system. 

```bash
curl https://test.api.amadeus.com/v1/booking/hotel-bookings \
--data-raw '{
  "data": {
    "offerId": "Y0UE4D1MUT",
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
          "expiryDate": "2021-08"
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

Congratulations, you’ve just performed your first hotel booking! Once the
reservation is made, the API will return a unique booking confirmation ID which
you can send to your users. 

### Notes about Payment

The Hotel Search API returns information about the payment policy of each
hotel. The main policy types are: 

- Guarantee: the hotel will save credit card information during booking but not make any charge to the account. In the case of a no-show or out-of-policy cancellation, the hotel may charge penalties to the card. 
- Deposit: at the time or booking or on a given deadline, the hotel will charge the guest a percentage of the total amount of the reservation. The remaining amount is paid by the traveler directly at the hotel. 
- Prepay: the total amount of the reservation must be paid by the traveler during booking. 

The current version of the Hotel Booking API only permits booking at hotels
that accept credit cards. During the booking process, Amadeus passes the
payment and guest information to the hotel but does not validate information.
Be sure to validate the payment and guest information, as invalid information
may result in the reservation being cancelled. 

As soon as your application stores, transmits, or processes cardholder
information, you will need to comply with PCI Data Security Standard (PCI DSS).
For more information, visit the [PCI Security Council website](https://www.pcisecuritystandards.org/merchants). 


## Getting Hotel Ratings

Amadeus Hotel Ratings API returns a rating for many of the crucial elements of
a hotel’s offer; whether that be sleep quality, services, facilities, room
comforts, value for money, location and many other variables. Hotel Ratings API
guarantees high-quality service for your customers.

The sentiment analysis, just like the one below, is displayed in a simple flow
to allow you to easily identify the best hotels based on traveler reviews:

```bash
curl https://test.api.amadeus.com/v2/e-reputation/hotel-sentiments?hotelIds=TELONMFS,ADNYCCTB,XXXYYY01
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
With these additional filters, your booking process is made more efficient and
you can offer your customers an enriched shopping experience, confident that
you are offering a hotel choice that is rated highly in the areas that
customers most appreciate.

## Common Errors

### AcceptedPayments must be creditCards 

The current version of the Hotel Booking API only supports credit card
payments, which are accepted by most hotels. The Hotel Search API returns the
payment policy of each hotel under acceptedPayments in the policies section.

###  Empty response from the View Room endpoint  

If you get an empty response from the Hotel Search API’s second endpoint,
then the hotel is fully booked and has no vacancy for the requested dates. If
you don't use the checkInDate and checkOutDate parameters in the request the
API will return results for a one-night stay starting on the current date. If
the hotel is full, the response will be empty. 

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

The offer of the selected Hotel is not longer available. Please select a new one.

