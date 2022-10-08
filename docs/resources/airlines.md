# Airlines


| APIs                                                                                                                                                          | Description                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Flight Check-in Links  API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-check-in-links) |  Simplifies the check-in process by providing direct links to the airline check-in page.                |
| [Airline Code Lookup API](https://developers.amadeus.com/self-service/category/air/api-doc/airline-code-lookup)           | Finds the name of an airline by its IATA or ICAO airline codes.                  |


## Get a direct link to the airline check-in page

Suppose we are building an app with an integrated check-in flow for a particular airline. In this case, we can leverage the [Flight Check-in Links  API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-check-in-links) to generate a link to the airline's official check-in page in a required language for both web and mobile platforms. The only parameter that we need to provide in our search query is the airline's IATA code. If required, we can request the links in a specific language, such as UK English (en-GB). This is what our request would look like:


```bash
curl --request GET \
     --header 'Authorization: Bearer <token>' \
     --url https://test.api.amadeus.com/v2/reference-data/urls/checkin-links?airlineCode=BA&language=en-GB \
```

This is what we get in the response:

```json
{
  "meta": {
    "count": 3,
    "links": {
      "self": "https://test.api.amadeus.com/v2/reference-data/urls/checkin-links?airlineCode=BA&language=EN-GB"
    }
  },
  "data": [
    {
      "type": "checkin-link",
      "id": "BAEN-GBAll",
      "href": "https://www.britishairways.com/travel/olcilandingpageauthreq/public/en_gb",
      "channel": "All"
    },
    {
      "type": "checkin-link",
      "id": "BAEN-GBMobile",
      "href": "https://www.britishairways.com/travel/olcilandingpageauthreq/public/en_gb/device-mobile",
      "channel": "Mobile"
    },
    {
      "type": "checkin-link",
      "id": "BAEN-GBWeb",
      "href": "https://www.britishairways.com/travel/olcilandingpageauthreq/public/en_gb",
      "channel": "Web"
    }
  ]
}
```

Here we've got a dedicated link for web applications, a dedicated link for mobile applications and a link that works on all platforms.

## Get the airline ICAO code by the IATA code

If we need to know the IATA code for a particular airline but only have the airline's ICAO code, the [Airline Code Lookup API](https://developers.amadeus.com/self-service/category/air/api-doc/airline-code-lookup) can help us out. Just specify the IATA code in the query and send out the request:

```bash
curl --request GET \
     --header 'Authorization: Bearer <token>' \
     --url https://test.api.amadeus.com/v1/reference-data/airlines?airlineCodes=BA \
```

The response is pretty straightforward:

```json
{
  "meta": {
    "count": 1,
    "links": {
      "self": "https://test.api.amadeus.com/v1/reference-data/airlines?airlineCodes=BA"
    }
  },
  "data": [
    {
      "type": "airline",
      "iataCode": "BA",
      "icaoCode": "BAW",
      "businessName": "BRITISH AIRWAYS",
      "commonName": "BRITISH A/W"
    }
  ]
}
```
