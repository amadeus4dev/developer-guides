# Python SDK

!!! danger
    This SDK is maintained by the developer community only. The Amadeus for Developers team doesn't support or maintain it. 

### Prerequisites

-  Amadeus for Developers API key and API secret: to get one, [create a free developer account](https://developers.amadeus.com/register) and set up your first application in your [Workspace](https://developers.amadeus.com/my-apps).
- PHP version >= 7.4

## Installation

The PHP SDK has been uploaded to the official [PHP package repository](https://getcomposer.org/).

```
composer require amadeus4dev/amadeus-php
```
## Making your first API call 

### Request

```php
<?php declare(strict_types=1);

use Amadeus\Amadeus;
use Amadeus\Exceptions\ResponseException;

require __DIR__ . '/vendor/autoload.php'; // include composer autoloader

try {
    $amadeus = Amadeus::builder("REPLACE_BY_YOUR_API_KEY", "REPLACE_BY_YOUR_API_SECRET")
        ->build();

    // Flight Offers Search GET
    $flightOffers = $amadeus->getShopping()->getFlightOffers()->get(
                        array(
                            "originLocationCode" => "PAR",
                            "destinationLocationCode" => "MAD",
                            "departureDate" => "2022-12-29",
                            "adults" => 1
                        )
                    );
    print $flightOffers[0];

    // Flight Offers Search POST
    $body ='{
              "originDestinations": [
                {
                  "id": "1",
                  "originLocationCode": "PAR",
                  "destinationLocationCode": "MAD",
                  "departureDateTimeRange": {
                    "date": "2023-08-29"
                  }
                }
              ],
              "travelers": [
                {
                  "id": "1",
                  "travelerType": "ADULT"
                }
              ],
              "sources": [
                "GDS"
              ]
            }';
    $flightOffers = $amadeus->getShopping()->getFlightOffers()->post($body);
    print $flightOffers[0];
} catch (ResponseException $e) {
    print $e;
}
```

### Handling the response  

Every API call returns a `Response` object which contains raw response body in string format:

```php
$locations = $amadeus->getReferenceData()->getLocations()->get(
                array(
                    "subType" => "CITY",
                    "keyword" => "PAR"
                )
            );

// The raw response, as a string
$locations[0]->getResponse()->getResult(); // Include response headers
$locations[0]->getResponse()->getBody(); //Without response headers

// Directly get response headers as an array
$locations[0]->getResponse()->getHeadersAsArray();

// Directly get response body as a Json Object
$locations[0]->getResponse()->getBodyAsJsonObject();

// Directly get the data part of response body
$locations[0]->getResponse()->getData();
```

## Arbitrary API calls

You can call any API not yet supported by the SDK by making arbitrary calls.

For the `get` endpoints:

```php
// Make a GET request only using path
$amadeus->getClient()->getWithOnlyPath("/v1/airport/direct-destinations?departureAirportCode=MAD");

// Make a GET request using path and passed parameters
$amadeus->getClient()->getWithArrayParams("/v1/airport/direct-destinations", ["departureAirportCode" => "MAD"]);
```

For the `post` endpoints:

```php
$amadeus->getClient()->postWithStringBody("/v1/shopping/availability/flight-availabilities", $body);
```