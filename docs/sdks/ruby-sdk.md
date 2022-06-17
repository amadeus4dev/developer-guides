# Ruby SDK

The [Amadeus Ruby SDK](https://github.com/amadeus4dev/amadeus-ruby) makes it easy to develop .NET applications with flight, hotel, and other travel data from Amadeus. In this guide, you'll install the library in your environment and make your first API call in minutes.

## Prerequisites

- Amadeus for Developers API key and secret: to get one, [create a free developer account](https://developers.amadeus.com/register) and set up your first application in your [Workspace](https://developers.amadeus.com/my-apps).
- Ruby 2.5 or higher

## Installing the Amadeus Ruby SDK

You can install it directly via the command line or via the bundler.
#### Command line
```bash
gem install amadeus
```
#### Bundler
```rb
gem 'amadeus'
```

## Making your first API call

For this tutorial, you'll call the [Flight Check-in Links](https://developers.amadeus.com/self-service/category/air/api-doc/flight-check-in-links) API to fetch the online check-in URL for British Airways. Open the Program.cs file and add the following code:

```rb
require 'amadeus'

amadeus = Amadeus::Client.new({
  client_id: 'REPLACE_BY_YOUR_API_KEY',
  client_secret: 'REPLACE_BY_YOUR_API_SECRET'
})

begin
  puts amadeus.reference_data.urls.checkin_links.get(airlineCode: 'BA').body
rescue Amadeus::ResponseError => error
  puts error
end
```

Let's pause to look at what happening in the code:

-   Once you import the amadeus library, you initialize the client by adding your credentials in the `builder` method. We suggest adding your credentials aas ennvironment variables to avoid exposing them directly in the code. The library can be initialized without any parameters when the environment variables `AMADEUS_CLIENT_ID` and `AMADEUS_CLIENT_SECRET` are present.
-   The authentication process is handled by the SDK.
-   The SDK uses namespaced methods to create a match between the APIs and the SDK. In this case, the API `GET /v2/reference-data/urls/checkin-links?airlineCode=BA` is implemented as `amadeus.reference_data.urls.checkin_links.get(airlineCode: 'BA')`

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

Every API call returns an `Amadeus::Response` object. If the API call contained a JSON response, it will parse the JSON into `.result` attribute. If this data also contains a data key, that will be made available in `.data`attribute. The raw body of the response is always available in `.body` attribute.

```rb
response = amadeus.reference_data.locations.get(
  keyword: 'LON',
  subType: Amadeus::Location::ANY
)

p response.body #=> The raw response, as a string
p response.result #=> The body parsed as JSON, if the result was parsable
p response.data #=> The list of locations, extracted from the JSON
```

When the API returns an error, the SDK throws appropriate exceptions based on the HTTP status code returned by the API. The available error classes in the SDK are the following:

```rb
  # This error occurs when there is some kind of error in the network
  class NetworkError < Amadeus::ResponseError; end
  # This error occurs when the response type was JSOn but could not be parsed
  class ParserError < Amadeus::ResponseError; end
  # This error occurs when there is an error on the server
  class ServerError < Amadeus::ResponseError; end
  # This error occurs when the client did not provide the right parameters
  class ClientError < Amadeus::ResponseError; end
  # This error occurs when the client did not provide the right credentials
  class AuthenticationError < Amadeus::ResponseError; end
  # This error occurs when the path could not be found
  class NotFoundError < Amadeus::ResponseError; end
```
## Arbitrary API calls

You can call any API not yet supported by the SDK by making arbitrary calls, for example you can call the Flight Check-in Links: 

```rb
amadeus.get('/v2/reference-data/urls/checkin-links', airlineCode: 'BA')

```