# Airlines

We have three APIs that provide information on airlines, from a list of available destinations to the check-in process. We have grouped them into the **Airlines** category.

!!! information
    Our catalogue of [Self-Service APIs](https://developers.amadeus.com/self-service) is currently organised by categories that are different to what you see on this page.

| APIs                                                                                                                                                          | Description                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Flight Check-in Links](https://developers.amadeus.com/self-service/category/air/api-doc/flight-check-in-links) |  Simplifies the check-in process by providing direct links to the airline check-in page.                |
| [Airline Code Lookup](https://developers.amadeus.com/self-service/category/air/api-doc/airline-code-lookup)           | Finds the name of an airline by its IATA or ICAO airline codes.                  |
| [Airline Routes](https://developers.amadeus.com/self-service/category/air/api-doc/airline-routes) | Finds all destinations served by a given airline.


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

#### Get routes for a specific airline

The [Airline Routes API](https://developers.amadeus.com/self-service/category/air/api-doc/airline-routes) shows all destinations for a given airline. To follow up on our previous example, let's check what destinations the British Airways fly to. There's definitely plenty of options, so we can limit the maximum number of results to two for the sake of simplicity. Keep in mind that this limit will apply from the beginning of the results list in the alphabetical order of the city names.

The request will look like this:

```bash
curl --request GET \
     --header 'Authorization: Bearer <token>' \
     --url https://test.api.amadeus.com/v1/airline/destinations?airlineCode=BA&max=2 \
```

So we can see the the following results:

```json
{
  "data": [
    {
      "type": "location",
      "subtype": "city",
      "name": "Bangalore",
      "iataCode": "BLR"
    },
    {
      "type": "location",
      "subtype": "city",
      "name": "Paris",
      "iataCode": "PAR"
    }
  ],
  "meta": {
    "count": "2",
    "sort": "iataCode",
    "links": {
      "self": "https://test.api.amadeus.com/v1/airline/destinations?airlineCode=BA&max=2"
    }
  }
}
```
