# Flights

## How to search flights

### Inspirational Search

The [Flight Inspiration Search API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-inspiration-search) provides a list of destinations from a given airport that is ordered by price and can be filtered by departure date or maximum price. The following request, retrieves a list of destinations from Boston:

```bash
curl https://api.amadeus.com/v1/shopping/flight-destinations?origin=BOS
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

### Flexible Search on dates

The [Flight Cheapest Date Search API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-cheapest-date-search) finds the cheapest dates to travel from one
city to another. The API provides list of flight options with dates and prices,
and allows you to order by price, departure date or duration.

!!!information
    This API returns cached prices. Once the dates are chosen, use the Flight Offers Search API to get real-time pricing and availability.

The following example retrieves a list of `flight-date` objects containing pricing information given the origin and destination, and a range of dates:

```bash
curl https://api.amadeus.com/v1/shopping/flight-dates?origin=BOS&destination=CHI&departureDate=2022-08-15,2022-08-28
```

The API provides a link to Flight Offers Search to search for flights once a
destination is chosen, in order to proceed with the booking flow.


### Offers Search

The [Flight Offers Search API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search) searches over 500 airlines to find the cheapest
flights for a given itinerary. The API lets you can search flights between two
cities, perform multi-city searches for longer itineraries and access one-way
combinable fares to offer the cheapest options possible. For each itinerary,
the API provides a list of flight offers with prices, fare details, airline
names, baggage allowances and departure terminals.

!!!warning
    - Flights from low-cost carriers and American Airlines are currently unavailable.

The Flight Offers Search API starts the booking cycle with a search for the
best fares. The API returns a list of the cheapest flights given a city/airport
of departure, a city/airport of arrival, the number and type of passengers and
travel dates. The results are complete with airline name and fares as well as
additional information like bag allowance and pricing for additional baggage. 

The API comes in two flavors:

- Simple version: GET operation with few parameters but which is quicker to integrate.
- On steroids: POST operation offering the full functionalities of the API.

The minimum `GET` request has following parameters:

```bash
curl https://api.amadus.com/v2/shopping/flight-offers?adults=1&originLocationCode=BOS&destinationLocationCode=CHI&departureDate=2022-07-22
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

#### Flight Offers Prediction

The Flight Choice Prediction API predicts the flight your users will choose.
Our machine-learning models have analyzed historical interactions with the
Flight Low-Fare Search API and can determine each flight’s probability of being
chosen. Boost conversions and create a personalized experience by filtering out
the noise and showing your users the flights which are best for them.

Here is a quick cURL example piping Low fare search API results directly to the prediction API, stay tuned for SDK updates with more helpers!

Let’s look at flight offers for a Madrid-New York round trip (limiting to 4 options for this test illustration)

```bash
curl --request GET \
     --header 'Authorization: Bearer <token>' \
     --url https://test.api.amadeus.com/v1/shopping/flight-offers\?origin\=MAD\&destination\=NYC\&departureDate\=2019-08-24\&returnDate\=2019-09-19\&max\=4 \
| curl --request POST \
       --header 'content-type: application/json' \
       --header 'Authorization: Bearer <token>' \
       --url https://test.api.amadeus.com/v1/shopping/flight-offers/prediction --data @-
```

The prediction API returns the same content as Low Fare search with the
addition of the `choiceProbability` field for each flight offer element

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

In the following example, we’ll fly from Madrid to Paris, where we’ll spend a couple
days, then fly to Munich for three days. Next, we’ll visit Amsterdam for two
days before finishing our journey with a return to Madrid. We'll use the
following IATA city codes: `MAD > PAR > MUC > AMS > MAD`

The request will look like this:


```bash
curl https://api.amadeus.com/v2/shopping/flight-offers \
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
## Confirming Fares

The availability and price of airfare fluctuate so it’s important to confirm
before proceeding to book. This is especially true if time passes between the
initial search and the decision to book, as fares are limited and there are
thousands of bookings occurring every minute. During this step, you can also
add ancillary products like extra bags or legroom.

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

## Booking a Flight

Once the fare is confirmed, you’re ready to use the _Flight Create Orders API_
to perform the actual booking. This API lets you log a reservation in the
airlines’ systems and create a PNR, and returns a unique ID number and the
reservation details. If you’re using an airline consolidator, the PNR will be
automatically sent to the consolidator for ticket issuance. [Visit the Flight
Create Orders documentation
page](https://developers.amadeus.com/self-service/category/air/api-doc/flight-create-orders)
for more details on this API.

Remember, you need to be able to issue a ticket to make bookings with our
Flight Create Order API. To access the API in production, you need to either
sign a contract with an airline consolidator or be accredited to issue tickets
yourself. 

## Issuing a ticket

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

## Common Errors

###  Issuance not allowed in Self Service 

Self-Service users must work with an airline consolidator that can issue
tickets on your behalf. In that case, the payment is not processed by the API
but directly between you and the consolidator. Adding a form of payment into
the Flight Create Orders API will be rejected by error INVALID FORMAT.

###  Price discrepancy 

The price of airfare fluctuates constantly. Creating an order for a flight
whose price is no longer valid at the time of booking will trigger the
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