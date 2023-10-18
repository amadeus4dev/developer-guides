# Cars and Transfers

The Amadeus Cars and Transfers APIs provide an extensive suite of capabilities designed to simplify the process of booking and managing transfers during a traveler's trip, delivering a seamless and efficient experience.

![Cars and transfers API](../images/resources/cars-transfers/TransfersAPI.png)

Have a look at our dedicated [Postman collection](./developer-tools/postman.md) to easily test the Cars and Transfers API with pre-set requests.

| APIs                                                                                                                                                 | Description                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [Transfer Search](https://developers.amadeus.com/self-service/category/cars-and-transfers/api-doc/transfer-search/api-reference){:target="\_blank"}     | This API enables users to search for a transfer using a range of pre-arranged transportation options. These options include Private Transfers, Hourly Services, Taxis, Shared Transfers, Airport Express trains and buses, Private Jets, and Helicopter Transfers.                                                 |
| [Transfer Booking](https://developers.amadeus.com/self-service/category/cars-and-transfers/api-doc/transfer-booking){:target="\_blank"} | Once a transfer is chosen, the Transfer Booking API completes the reservation. It provides a unique booking ID and reservation details, which can be used to manage the reservation later. |
| [Transfer Management](https://developers.amadeus.com/self-service/category/cars-and-transfers/api-doc/transfer-management){:target="\_blank"} | This API provides tools for managing transfer reservations. Using the booking ID provided by the Transfer Booking API, users can cancel reservations. |


## Search for a transfer

The search is carried out through a POST API call to /shopping​/transfer-offers. The API request includes parameters like the start and end locations, type of transfer, number of passengers, provider codes, and other optional parameters.


In the following example request, we have multiple parameters each with its own specific meaning and structure:

* `startLocationCode`: "CDG" - This is an International Air Transport Association (IATA) airport code which represents Charles de Gaulle Airport in Paris, France. The starting location of the journey.

* `endAddressLine`: "Avenue Anatole France, 5" - This is the exact address where the journey will end, presumably a location in Paris.

* `endCityName`: "Paris" - The city where the journey ends.

* `endZipCode`: "75007" - This represents the postal code of the end location.

* `endCountryCode`: "FR" - It's a two-letter country code representing France.

* `endName`: "Souvenirs De La Tour" - The name of the destination, perhaps a business or venue at the end location.

* `endGooglePlaceId`: "ChIJL-DOWeBv5kcRfTbh97PimNc" - A unique identifier that Google assigns to a location. You can use it to get more details about this location using Google's Places API.

* `endGeoCode`: "48.859466,2.2976965" - The geographical coordinates of the end location. The first number is latitude and the second is longitude.

* `transferType`: "PRIVATE" - This indicates that the transfer type is private, meaning the transfer will not be shared with others. This value is the Amadeus transfer service type, which can take one of the following:

  - *PRIVATE*: Private transfer from point to point
  - *SHARED*: Shared transfer from point to point
  - *TAXI*: Taxi reservation from point to point, price is estimated
  - *HOURLY*: Chauffeured driven transfer per hour
  - *AIRPORT_EXPRESS*: Express Train from/to Airport
  - *AIRPORT_BUS*: Express Bus from/to Airport
  - *HELICOPTER*: Private helicopter flight from/to airport
  - *PRIVATE_JET*: Private flight from airport to airport

* `startDateTime`: "2021-11-10T10:30:00" - The ISO 8601 timestamp when the journey begins.

* `providerCodes`: "TXO" - The code representing the provider of the transfer service.

* `passengers`: 2 - The total number of passengers who will take the journey.

* `stopOvers`: This is an array of objects representing different stopovers on the journey. Each object includes details about the duration of the stopover, the sequence number (which stopover it is), and information about the stopover's address, country code, city name, zip code, Google place ID, name, and geographical coordinates. For example, a `stopOver` object might look like this:

```json
{
  "duration": "PT2H30M",
  "sequenceNumber": 1,
  "addressLine": "Avenue de la Bourdonnais, 19",
  "countryCode": "FR",
  "cityName": "Paris",
  "zipCode": "75007",
  "googlePlaceId": "DOWeBv5kcRfTbh97PimN",
  "name": "De La Tours",
  "geoCode": "48.859477,2.2976985",
  "stateCode": "FR"
}
```

* `startConnectedSegment`: This object contains information about a connected transportation segment, like a flight, that leads to the start of this transfer. It includes details about the transportation type, transportation number, and the departure and arrival of this segment.

* `passengerCharacteristics`: This array of objects includes details about the passengers' type codes and their ages. For example, "ADT" stands for an adult passenger and "CHD" stands for a child passenger.


```json
{
  "startLocationCode": "CDG",
  ...
  "endGeoCode": "48.859466,2.2976965",
  "transferType": "PRIVATE",
  ...
  "passengers": 2,
  "stopOvers": [
    {
      "duration": "PT2H30M",
      "sequenceNumber": 1,
      ...
      "stateCode": "FR"
    }
  ],
  ...
  "passengerCharacteristics": [
    {
      "passengerTypeCode": "ADT",
      "age": 20
    },
    ...
  ]
}
```

This request initiates a search for a private transfer for two passengers from location CDG with specific passenger characteristics and other details.

Let's have a look at the response:

```json
{
  "data": [
    {
      "type": "transfer-offer",
      "id": "0cb11574-4a02-11e8-842f-0ed5f89f718b",
      "transferType": "PRIVATE",
      "start": {
        "dateTime": "2021-11-10T10:30:00",
        "locationCode": "CDG"
      },
      "end": {
        "address": {
          "line": "Avenue Anatole France, 5",
          "zip": "75007",
          "countryCode": "FR",
          "cityName": "Paris",
          "latitude": 48.859466,
          "longitude": 2.2976965
        },
        "googlePlaceId": "ChIJL-DOWeBv5kcRfTbh97PimNc",
        "name": "Souvenirs De La Tour"
      },
      "stopOvers": [
        {
          "duration": "PT2H30M",
          "sequenceNumber": 1,
          "location": {
            "locationCode": "CDG",
            "address": {
              "line": "Avenue de la Bourdonnais, 19",
              "zip": "75007",
              "countryCode": "FR",
              "cityName": "Paris",
              "latitude": 48.859477,
              "longitude": 2.2976975
            },
            "googlePlaceId": "DOWeBv5kcRfTbh97PimN",
            "name": "De La Tours"
          }
        }
      ],
      "vehicle": {
        "code": "VAN",
        "category": "BU",
        "description": "Mercedes-Benz V-Class, Chevrolet Suburban, Cadillac Escalade or similar",
        "seats": [
          {
            "count": 3
          }
        ],
        "baggages": [
          {
            "count": 3,
            "size": "M"
          }
        ],
        "imageURL": "https://provider.com/images/BU_VAN.png"
      },
      "serviceProvider": {
        "code": "ABC",
        "name": "Provider name",
        "logoUrl": "https://provider.com/images/logo.png",
        "termsUrl": "https://provider.com/terms_and_conditions.html",
        "contacts": {
          "phoneNumber": "+33123456789",
          "email": "support@provider.com"
        },
        "settings": [
          "BILLING_ADDRESS_REQUIRED",
          "FLIGHT_NUMBER_REQUIRED",
          "CVV_NUMBER_REQUIRED"
        ]
      },
      "quotation": {
        "monetaryAmount": "63.70",
        "currencyCode": "USD",
        "isEstimated": false,
        "base": {
          "monetaryAmount": "103.70"
        },
        "discount": {
          "monetaryAmount": "50.00"
        },
        "fees": [
          {
            "indicator": "AIRPORT",
            "monetaryAmount": "10.00"
          }
        ],
        "totalTaxes": {
          "monetaryAmount": "12.74"
        },
        "totalFees": {
          "monetaryAmount": "10.00"
        }
      },
      "converted": {
        "monetaryAmount": "63.70",
        "currencyCode": "EUR",
        "isEstimated": false,
        "base": {
          "monetaryAmount": "103.70"
        },
        "discount": {
          "monetaryAmount": "50.00"
        },
        "fees": [
          {
            "indicator": "AIRPORT",
            "monetaryAmount": "10.00"
          }
        ],
        "totalTaxes": {
          "monetaryAmount": "12.74"
        },
        "totalFees": {
          "monetaryAmount": "10.00"
        }
      },
      "extraServices": [
        {
          "code": "EWT",
          "itemId": "EWT0291",
          "description": "Extra 15 min. wait",
          "quotation": {
            "monetaryAmount": "39.20",
            "currencyCode": "USD",
            "base": {
              "monetaryAmount": "36.00"
            },
            "totalTaxes": {
              "monetaryAmount": "3.20"
            }
          },
          "converted": {
            "monetaryAmount": "32.70",
            "currencyCode": "EUR",
            "base": {
              "monetaryAmount": "30.00"
            },
            "totalTaxes": {
              "monetaryAmount": "2.7"
            }
          },
          "isBookable": true,
          "taxIncluded": true,
          "includedInTotal": false
        }
      ],
      "equipment": [
        {
          "code": "BBS",
          "description": "Baby stroller or Push chair",
          "quotation": {
            "monetaryAmount": "39.20",
            "currencyCode": "USD",
            "base": {
              "monetaryAmount": "36.00"
            },
            "totalTaxes": {
              "monetaryAmount": "3.20"
            }
          },
          "converted": {
            "monetaryAmount": "32.70",
            "currencyCode": "EUR",
            "base": {
              "monetaryAmount": "30.00"
            },
            "totalTaxes": {
              "monetaryAmount": "2.7"
            }
          },
          "isBookable": true,
          "taxIncluded": true,
          "includedInTotal": false
        }
      ],
      "cancellationRules": [
        {
          "feeType": "PERCENTAGE",
          "feeValue": "100",
          "metricType": "DAYS",
          "metricMin": "0",
          "metricMax": "1"
        },
        {
          "feeType": "PERCENTAGE",
          "feeValue": "0",
          "metricType": "DAYS",
          "metricMin": "1",
          "metricMax": "100"
        }
      ],
      "methodsOfPaymentAccepted": [
        "CREDIT_CARD",
        "INVOICE"
      ],
      "discountCodes": [
        {
          "type": "CD",
          "value": "FJKS0289LDIW234"
        }
      ],
      "distance": {
        "value": 152,
        "unit": "KM"
      },
      "startConnectedSegment": {
        "transportationType": "FLIGHT",
        "transportationNumber": "AF380",
        "departure": {
          "localDateTime": "2021-11-10T09:00:00",
          "iataCode": "NCE"
        },
        "arrival": {
          "localDateTime": "2021-11-10T10:00:00",
          "iataCode": "CDG"
        }
      },
      "passengerCharacteristics": [
        {
          "passengerTypeCode": "ADT",
          "age": 20
        },
        {
          "passengerTypeCode": "CHD",
          "age": 10
        }
      ]
    }
  ],
  "warnings": [
    {
      "code": 101,
      "title": "PICK-UP DATE TIME CHANGED",
      "detail": "Transfer pick-up date and time have been changed by provider",
      "source": {
        "pointer": "/data/1/start/dateTime",
        "parameter": "dateTime"
      }
    }
  ]
}
```


The data represents a private transfer offer with the id `0cb11574-4a02-11e8-842f-0ed5f89f718b`. The transfer begins from the location `CDG` at the time `2021-11-10T10:30:00` and ends at the location `Souvenirs De La Tour` located at Avenue Anatole France, 5 in Paris, France.

During the journey, there's a stopover at `De La Tours` situated at Avenue de la Bourdonnais, 19 in Paris, France for 2 hours and 30 minutes. The vehicle to be used for this transfer is a VAN in the category BU. The model of the vehicle can be a Mercedes-Benz V-Class, Chevrolet Suburban, Cadillac Escalade or similar. The vehicle can accommodate 3 passengers and 3 medium-sized baggages.

The transfer service provider is `Provider name` with the code `ABC`. The quotation for the transfer is 63.70 USD after a discount of 50.00 USD from the base price of 103.70 USD. The total taxes and fees for the transfer are 12.74 USD and 10.00 USD respectively.

There are also options to avail extra services like "Extra 15 min. wait" for 39.20 USD and to rent equipment like `Baby stroller or Push chair` for 39.20 USD. The cancellation rules state a 100% fee for cancellations made between 0 to 1 day before the transfer and no fee for cancellations made between 1 to 100 days before the transfer.

The payment for the transfer can be made through Credit Card or Invoice. A discount code `FJKS0289LDIW234` is also available for use.

This transfer offer is linked to a flight with the transportation number `AF380` departing from `NCE` at `2021-11-10T09:00:00` and arriving at `CDG` at `2021-11-10T10:00:00`. The transfer caters to a passenger aged 20 and a child aged 10.

A warning code `101` titled `PICK-UP DATE TIME CHANGED` is issued stating that the transfer pick-up date and time have been changed by the provider.

## Booking a transfer

Let's now look into the [Transfer Booking API](https://developers.amadeus.com/self-service/category/cars-and-transfers/api-doc/transfer-booking){:target="\_blank"}.

The main endpoint URL is `https://test.api.amadeus.com/v1/ordering/transfer-orders?offerId=<OFFER_ID>`. The parameter `<OFFER_ID>` needs to be replaced with the actual ID of the offer you wish to order, such as `0cb11574-4a02-11e8-842f-0ed5f89f718b`, which we obtained in our previous example.


```json
{
  "data": {
    "note": "Note to driver",
    "passengers": [
      {
        "firstName": "John",
        "lastName": "Doe",
        "title": "MR",
        "contacts": {
          "phoneNumber": "+33123456789",
          "email": "user@email.com"
        },
        "billingAddress": {
          "line": "Avenue de la Bourdonnais, 19",
          "zip": "75007",
          "countryCode": "FR",
          "cityName": "Paris"
        }
      }
    ],
    "agency": {
      "contacts": [
        {
          "email": {
            "address": "abc@test.com"
          }
        }
      ]
    },
    "payment": {
      "methodOfPayment": "CREDIT_CARD",
      "creditCard": {
        "number": "4111111111111111",
        "holderName": "JOHN DOE",
        "vendorCode": "VI",
        "expiryDate": "1018",
        "cvv": "111"
      }
    },
    "extraServices": [
      {
        "code": "EWT",
        "itemId": "EWT0291"
      }
    ],
    "equipment": [
      {
        "code": "BBS"
      }
    ],
    "corporation": {
      "address": {
        "line": "5 Avenue Anatole France",
        "zip": "75007",
        "countryCode": "FR",
        "cityName": "Paris"
      },
      "info": {
        "AU": "FHOWMD024",
        "CE": "280421GH"
      }
    },
    "startConnectedSegment": {
      "transportationType": "FLIGHT",
      "transportationNumber": "AF380",
      "departure": {
        "uicCode": "7400001",
        "iataCode": "CDG",
        "localDateTime": "2021-03-27T20:03:00"
      },
      "arrival": {
        "uicCode": "7400001",
        "iataCode": "CDG",
        "localDateTime": "2021-03-27T20:03:00"
      }
    },
    "endConnectedSegment": {
      "transportationType": "FLIGHT",
      "transportationNumber": "AF380",
      "departure": {
        "uicCode": "7400001",
        "iataCode": "CDG",
        "localDateTime": "2021-03-27T20:03:00"
      },
      "arrival": {
        "uicCode": "7400001",
        "iataCode": "CDG",
        "localDateTime": "2021-03-27T20:03:00"
      }
    }
  }
}
```
- **`data`**: Root level object encapsulating all the necessary data for the transfer order.
    - **`note`**: A string containing a note intended for the driver. (Example: "Note to driver")
    - **`passengers`**: An array of objects, each representing a passenger with the following properties:
        - **`firstName`**: A string containing the passenger's first name. (Example: "John")
        - **`lastName`**: A string containing the passenger's last name. (Example: "Doe")
        - **`title`**: A string containing the passenger's title ("MR", "MS", etc.). (Example: "MR")
        - **`contacts`**: An object containing contact details:
            - **`phoneNumber`**: A string containing the passenger's phone number. (Example: "+33123456789")
            - **`email`**: A string containing the passenger's email address. (Example: "user@email.com")
        - **`billingAddress`**: An object containing the billing address details:
            - **`line`**: Street name and number. (Example: "Avenue de la Bourdonnais, 19")
            - **`zip`**: Zip or postal code. (Example: "75007")
            - **`countryCode`**: Country code. (Example: "FR")
            - **`cityName`**: City name. (Example: "Paris")
    - **`agency`**: An object representing the agency details with the following properties:
        - **`contacts`**: An array containing objects, each representing a contact's details:
            - **`email`**: An object containing the email details:
                - **`address`**: A string containing the contact's email address. (Example: "abc@test.com")
    - **`payment`**: An object containing payment details:
        - **`methodOfPayment`**: A string indicating the method of payment. (Example: "CREDIT_CARD")
        - **`creditCard`**: An object containing credit card details:
            - **`number`**: A string containing the credit card number. (Example: "4111111111111111")
            - **`holderName`**: A string containing the card holder's name. (Example: "JOHN DOE")
            - **`vendorCode`**: A string containing the vendor's code. (Example: "VI")
            - **`expiryDate`**: A string containing the expiry date of the card. (Example: "1018")
            - **`cvv`**: A string containing the card's CVV. (Example: "111")
    - **`extraServices`**: An array containing objects, each representing an extra service:
        - **`code`**: A string indicating the service's code. (Example: "EWT")
        - **`itemId`**: A string indicating the service's item ID. (Example: "EWT0291")
    - **`equipment`**: An array containing objects, each representing an equipment detail:
        - **`code`**: A string indicating the equipment's code. (Example: "BBS")
    - **`corporation`**: An object containing corporation details:
        - **`address`**: An object containing the corporation address:
            - **`line`**: Street name and number. (Example: "5 Avenue Anatole France")
            - **`zip`**: Zip or postal code. (Example: "75007")
            - **`countryCode`**: Country code. (Example: "FR")
            - **`cityName`**: City name. (Example: "Paris")
        - **`info`**: An object containing additional corporation info:
            - **`AU`**: Additional information (Example: "FHOWMD024")
            - **`CE`**: Additional information (Example: "280421GH")
    - **`startConnectedSegment`**: An object representing the start of a connected transport segment:
        - **`transportationType`**: A string indicating the type of transportation. (Example: "FLIGHT")
        - **`transportationNumber`**: A string indicating the transportation number. (Example: "AF380")
        - **`departure`**: An object containing departure details:
            - **`uicCode`**: A string indicating the UIC code. (Example: "7400001")
            - **`iataCode`**: A string indicating the IATA code. (Example: "CDG")
            - **`localDateTime`**: A string indicating the local date and time of departure. (Example: "2021-03-27T20:03:00")
        - **`arrival`**: An object containing arrival details:
            - **`uicCode`**: A string indicating the UIC code. (Example: "7400001")
            - **`iataCode`**: A string indicating the IATA code. (Example: "CDG")
            - **`localDateTime`**: A string indicating the local date and time of arrival. (Example: "2021-03-27T20:03:00")
    - **`endConnectedSegment`**: An object representing the end of a connected transport segment (same structure as `startConnectedSegment`).

## Cancelling a transfer

The [Transfer Management API](https://developers.amadeus.com/self-service/category/cars-and-transfers/api-doc/transfer-management){:target="\_blank"} effectively allows us to cancel a transfer linked with an existing order.

For example:

`POST https://test.api.amadeus.com/v1/ordering/transfer-orders/{orderId}/transfers/cancellation`


The `{orderId}` in the URL should be replaced with the unique identifier of the order that was previously generated when the order was created. For instance, the `orderId` could be something like `0cb11574-4a02-11e8-842f-0ed5f89f718b`.

The `confirmNbr` is a unique confirmation number associated with the transfer that is to be cancelled. 

The response for this request will confirm the cancellation of the transfer. Here's an example response:

```json
{
  "data": {
    "confirmNbr": "2904892",
    "reservationStatus": "CANCELLED"
  }
}
```

In this example response, we see the `confirmNbr` `2904892` and the reservationStatus `CANCELLED`, confirming that the cancellation has been successful.
