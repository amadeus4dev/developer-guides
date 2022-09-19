# .NET SDK

The [Amadeus .NET SDK](https://github.com/amadeus4dev/amadeus-dotnet) makes it easy to develop .NET applications with flight, hotel, and other travel data from Amadeus. In this guide, you'll install the library in your environment and make your first API call in minutes.

## Prerequisites

-   Amadeus for Developers API key and API secret: to get one, [create a free developer account](https://developers.amadeus.com/register) and set up your first application in your [Workspace](https://developers.amadeus.com/my-apps).
-   .NET 3.1 or higher: download the version of your choice from the [official website](https://dotnet.microsoft.com/en-us/download).
-   Visual Studio: [download](https://visualstudio.microsoft.com/) the free community version of the IDE.

## Installing the Amadeus .NET SDK

In this section, you will create a new project and install the Amadeus SDK. Open Visual Studio and click File > New Solution > App > Console Application to create a new console application.

Next, install the `amadeus-dotnet` package. Open your project's NuGet packages manager, search for the library, and install the latest version.

## Making your first API call

For this tutorial, you'll call the [Flight Check-in Links](https://developers.amadeus.com/self-service/category/air/api-doc/flight-check-in-links) API to fetch the online check-in URL for British Airways. Open the Program.cs file and add the following code:

```
using System;

using amadeus;
using amadeus.resources;

namespace amadeusTest

{
    class Program
    {
        static void Main(string[] args) {
            GetCheckinLinks();
        }

        public static void GetCheckinLinks() {
            try
            {
                Amadeus amadeus = Amadeus
                    .builder("REPLACE_BY_YOUR_API_KEY", "REPLACE_BY_YOUR_API_SECRET")
                    .build();

                Console.WriteLine("Get Check-in links:");
                CheckinLink[] checkinLinks = amadeus.referenceData.urls.checkinLinks.get(Params
                        .with("airlineCode", "BA"));

                Console.WriteLine(checkinLinks[0].response.data);

            }
            catch (Exception e)
            {
                Console.WriteLine("ERROR: " + e.ToString());
            }
        }
    }
}
```

Let's pause for a moment to take a deeper look at the code. 

-   Once you import the Amadeus library, you initialize the client by adding your credentials in the `builder` method. We suggest adding your credentials as ennvironment variables to avoid exposing them directly in the code. The library can be initialized without any parameters when the environment variables `AMADEUS_CLIENT_ID` and `AMADEUS_CLIENT_SECRET` are present.
-   The authentication process is handled by the SDK.
-   The SDK uses namespaced methods to create a match between the APIs and the SDK. In this case, the API `GET /v2/reference-data/urls/checkin-links?airlineCode=BA` is implemented as `amadeus.referenceData.urls.checkinLinks.get(Params.with("airlineCode", "BA"));`

This will call the API to retrieve the online check-in links for British Airways (BA).

Build and run the project and you will see the API response:

```
[
    {
        "type": "checkin-link",
        "id": "BAEN-GBAll",
        "href": "<https://www.britishairways.com/travel/olcilandingpageauthreq/public/en_gb>",
        "channel": "All"
    },
    {
        "type": "checkin-link",
        "id": "BAEN-GBMobile",
        "href": "<https://www.britishairways.com/travel/olcilandingpageauthreq/public/en_gb/device-mobile>",
        "channel": "Mobile"
    },
    {
        "type": "checkin-link",
        "id": "BAEN-GBWeb",
        "href": "<https://www.britishairways.com/travel/olcilandingpageauthreq/public/en_gb>",
        "channel": "Web"
    }
]
```
## Handling the responses

All successful API calls return a `Resource` object. In the above example, `CheckinLink` is the resource object returned by the Flight Checkin-Links API.

Let's see another example with the Airport and City Search API, which returns a resource object `Location`:

```
Location[] locations = amadeus.referenceData.locations.get(Params
  .with("keyword", "LON")
  .and("subType", "CITY"));

Console.Write(locations[0].response.body); //the raw response, as a string
Console.Write(locations[0].response.result); //the body parsed as JSON, if the result was parsable
Console.Write(locations[0].response.data); //the list of locations, extracted from the JSON
Console.Write(locations[0].response.statusCode); //the HTTP status code
```

When the API returns an error, the SDK throws appropriate exceptions based on the HTTP status code returned by the API. The available error classes in the SDK are the following:

```
internal void detectError() {
            ResponseException exception = null;
            if (statusCode >= 500) {
              exception = new ServerException(this);
            } else if (statusCode == 404) {
              exception = new NotFoundException(this);
            } else if (statusCode == 401) {
              exception = new AuthenticationException(this);
            } else if (statusCode >= 400) {
              exception = new ClientException(this);
            } else if (!parsed) {
              exception = new ParserException(this);
            }

            if (exception != null)
            {
                throw exception;
            }
        }
```
## Arbitrary API calls

You can call any API not yet supported by the SDK by making arbitrary calls. In this case, the API returns a raw `Resource`.

For the `get` endpoints:

```
amadeus.get("/v2/reference-data/urls/checkin-links",
  Params.with("airlineCode", "BA"))

```

For the `post` endpoints:

```
amadeus.post("/v1/shopping/availability/flight-availabilities", body);

```