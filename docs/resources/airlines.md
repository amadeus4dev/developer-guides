# Airlines


| APIs                                                                                                                                                          | Description                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Flight Check-in Links  API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-check-in-links) |  Simplifies the check-in process easy by providing a direct links to the airline check-in page.                |
| [Airline Code Lookup API](https://developers.amadeus.com/self-service/category/air/api-doc/airline-code-lookup)           | Finda the name of an airline by its IATA or ICAO airline code.                  |


## Get a direct link to the airline check-in page

If we build an app with an integrated check-in functionality for a aprticular airline, we can leverage the [Flight Check-in Links  API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-check-in-links) to generate a link to the official check-in page in a required language for both web and mobile platforms. The only parameter that we need to provide in our search query is the airline IATA code. If required, we can request the results in a specific language, such as UK English (en-GB). This is what our request would look like:


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

Here we've got a link for web applications, a link for mobile applications and a link that works on all platforms.

## Get the airline ICAO code by the IATA code

If we need to get the IATA code for an airline, but we only know the airline's ICAO code, the [Airline Code Lookup API](https://developers.amadeus.com/self-service/category/air/api-doc/airline-code-lookup) can do this for us. Just put the IATA code into the query and send the request away:

```bash
curl --request GET \
     --header 'Authorization: Bearer <token>' \
     --url https://test.api.amadeus.com/v1/reference-data/airlines?airlineCodes=BA \
```

The response is very straightforward:

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
