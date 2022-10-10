# Itinerary Management

In the `Itinerary Management` category, you can give travelers a simple and personalized way to view their itinerary. 

| APIs                                                                                                                                                 | Description                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [Trip Parser](https://developers.amadeus.com/self-service/category/trip/api-doc/trip-parser/api-reference) | Build a single itinerary with information from different booking confirmation emails.                                                 |
| [Trip Purpose Prediction](https://developers.amadeus.com/self-service/category/trip/api-doc/trip-purpose-prediction/api-reference) | Analyze a flight itinerary and predict whether the trip is for business or leisure. |
 
## Parse the email confirmation into JSON

The [Trip Parser  API](https://developers.amadeus.com/self-service/category/trip/api-doc/trip-parser/api-reference) helps to extract information from different booking confirmation emails and compile it into a single structured `JSON` itinerary. This API can parse information from `flight`, `hotel`, `rail`, and `rental car` confirmation emails. It provides the result of your parsing immediately, thanks to our algorithm. 

!!! information
    `Trip Parser API` V3.0 has been released since August 2021 and the document is up to date. 

### Encode your booking confirmation in Base64

The first step to parsing is to encode your booking confirmation file in `Base64` format. This will give you the base of your API request. You should not add formatting or any other elements to your booking confirmation as it will affect the parsing.  

There are many tools and software that you can use for Base64 encoding. Some programming languages implement encoding and decoding functionalities in their standard library. In `python`, for example, it will look similar to this:  

```py
import base64 
with open("booking.pdf", "rb") as booking_file: 
    encoded_string = base64.b64encode(booking_file.read()) 
print(encoded_string)
```

### Get the parsing results 

Next, add the encoded booking confirmation to the body of a `POST` request to the endpoint 

```bash
POST https://test.api.amadeus.com/v3/travel/trip-parser
```

```json
{
  "payload": "your Base64 code here",
  "metadata": {
    "documentType": "PDF",
    "name": "BOOKING_DOCUMENT",
    "encoding": "BASE_64"
  }
}
```

- `documentType` : pdf, xml, json or jpg
- `encoding` : BASE_64 or BASE_64_URL

This will extract all the relevant data from the booking information into a structured JSON format, just like the example below.

```json
{
  "data": {
    "trip": {
      "reference": "JUPDRM",
      "stakeholders": [
        {
          "name": {
            "firstName": "MIGUEL",
            "lastName": "TORRES"
          }
        }
      ],
      "products": [
        {
          "air": {
            "departure": {
              "localDateTime": "2021-06-16T08:36:00"
            },
            "arrival": {
              "localDateTime": "2021-06-17T00:00:00"
            },
            "marketing": {
              "flightDesignator": {
                "carrierCode": "CM",
                "flightNumber": "644"
              }
            }
          }
        },
        {
          "air": {
            "departure": {
              "localDateTime": "2021-06-16T11:21:00"
            },
            "arrival": {
              "localDateTime": "2021-06-17T00:00:00"
            },
            "marketing": {
              "flightDesignator": {
                "carrierCode": "CM",
                "flightNumber": "426"
              }
            }
          }
        },
        {
          "air": {
            "departure": {
              "localDateTime": "2021-06-20T18:56:00"
            },
            "arrival": {
              "localDateTime": "2021-06-21T00:00:00"
            },
            "marketing": {
              "flightDesignator": {
                "carrierCode": "CM",
                "flightNumber": "645"
              }
            }
          }
        }
      ]
    }
  }
}

```


## Predict the trip purpose from a flight

Another API in the itinerary management category, the [Trip Purpose Prediction API](https://developers.amadeus.com/self-service/category/trip/api-doc/trip-purpose-prediction/api-reference), predicts whether a flight is searched for **business** or **leisure**. Our machine-learning models have detected which patterns of departure and arrival cities, flight dates, and search dates are associated with business and leisure trips. Understand why your users travel and show them the flights, fares, and ancillaries that suit them best.

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

