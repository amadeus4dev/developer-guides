---
title: PHP SDK Tutorial
---

# PHP

## PHP SDK

!!! warning
    The Amadeus PHP SDK is maintained independently by the developer community and is not supported or maintained by the Amadeus for Developers team.

#### Prerequisites

-  Amadeus for Developers API key and API secret: to get one, [create a free developer account](https://developers.amadeus.com/register){:target="\_blank"} and set up your first application in your [Workspace](https://developers.amadeus.com/my-apps){:target="\_blank"}.
- PHP version >= 7.4

### Installation

The PHP SDK has been uploaded to the official [PHP package repository](https://getcomposer.org/){:target="\_blank"}.

```
composer require amadeus4dev/amadeus-php
```
### Making your first API call 

#### Request

```php
<?php declare(strict_types=1);

use Amadeus\Amadeus;
use Amadeus\Exceptions\ResponseException;

require __DIR__ . '/vendor/autoload.php'; // include composer autoloader

try {
    $amadeus = Amadeus::builder("<YOUR-CLIENT-ID>", "<YOUR-CLIENT-SECRET>")
        ->build();

    // Flight Offers Search GET
    $flightOffers = $amadeus->getShopping()->getFlightOffers()->get(
                        array(
                            "originLocationCode" => "PAR",
                            "destinationLocationCode" => "MAD",
                            "departureDate" => "2023-08-29",
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
Replace `<YOUR-CLIENT-ID>` with your API Key and `<YOUR-CLIENT-SECRET>` with your API Secret in the command above and execute it.


#### Handling the response  

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

### Arbitrary API calls

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
