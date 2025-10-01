# Node

## Node SDK

Amadeus Node SDK for Self-service APIs is available with `npm`(node package manager) and Amadeus for Developers team is continuously updating with new APIs and features. 

You can refer to the [amadeus-node](https://github.com/amadeus4dev/amadeus-node){:target="\_blank"} or [Amadeus npm package](https://www.npmjs.com/package/amadeus){:target="\_blank"} for more details on the changelog.

### Installation
This module has been tested using [Node LTS versions](https://nodejs.org/en/about/releases/){:target="\_blank"}. You can install it using Yarn or NPM.

```sh
npm install amadeus --save
```

### Getting Started

To make your first API call, you will need to [register](https://developers.amadeus.com/register){:target="\_blank"} for an Amadeus Developers Account and [set up your first application](https://developers.amadeus.com/my-apps){:target="\_blank"}.

```js
var Amadeus = require('amadeus');
var amadeus = new Amadeus({
  clientId: '<YOUR-CLIENT-ID>',
  clientSecret: '<YOUR-CLIENT-SECRET>'
});

amadeus.shopping.flightOffersSearch.get({
    originLocationCode: 'SYD',
    destinationLocationCode: 'BKK',
    departureDate: '2022-10-21',
    adults: '2'
}).then(function(response){
  console.log(response.data);
}).catch(function(responseError){
  console.log(responseError.code);
});
```
Replace `<YOUR-CLIENT-ID>` with your API Key and `<YOUR-CLIENT-SECRET>` with your API Secret in the command above.

### Initialization

The client can be initialized directly as below. Your credentials `client Id` and `Client Secret` can be found on the [Amadeus dashboard](https://developers.amadeus.com/my-apps){:target="\_blank"}.


```js
// Initialize using parameters
var amadeus = new Amadeus({
  clientId: '<YOUR-CLIENT-ID>',
  clientSecret: '<YOUR-CLIENT-SECRET>'
});
```
Replace `<YOUR-CLIENT-ID>` with your API Key and `<YOUR-CLIENT-SECRET>` with your API Secret in the command above.

!!! warning
    Remember that hardcoding your credentials is not the best practice due to the potential exposure to others. Read more about best practices for [secure API key storage](https://developers.amadeus.com/blog/best-practices-api-key-storage){:target="\_blank"}.


Alternatively, you can initialize by setting up environment variables. In Node, we like to use [dotenv package](https://www.npmjs.com/package/dotenv){:target="\_blank"}. 

```sh
npm install dotenv
```

Put your API credentials in `.env` file:

```sh
AMADEUS_CLIENT_ID=<YOUR-CLIENT-ID>,
AMADEUS_CLIENT_SECRET=<YOUR-CLIENT-SECRET>
```
Replace `<YOUR-CLIENT-ID>` with your API Key and `<YOUR-CLIENT-SECRET>` with your API Secret in the command above.

Initialize using dotenv package:

```js
const dotenv = require('dotenv').config();
var amadeus = new Amadeus();
```

!!! important
    You will also want to add `.env` to your `.gitingore` so that your API credentials aren't included in your git repository.
    
If you don't want to use another package, you can also simply export your key in terminal directly to initalize.

Export your credentials in terminal:

```sh
export AMADEUS_CLIENT_ID="<YOUR-CLIENT-ID>"
export AMADEUS_CLIENT_SECRET="<YOUR-CLIENT-SECRET>"
```
Replace `<YOUR-CLIENT-ID>` with your API Key and `<YOUR-CLIENT-SECRET>` with your API Secret in the command above.

Initialize:

```js
var amadeus = new Amadeus();
```

### Moving to Production

By default, the SDK environment is set to `test` environment. To switch to `production` (pay-as-you-go) environment, please change the hostname as follows:

```js
var amadeus = new Amadeus({
  hostname: 'production'
});
```

### Promises

Every API call returns a `Promise` that either resolves or rejects. 

Every resolved API call returns a `Response` object containing a `body` attribute with the raw response. If the API call contained a JSON response, it will parse the JSON into the `result` attribute. If this data contains a `data` key, that will be made available in `data` attribute.

For a failed API call, it returns a `ResponseError`object containing the (parsed or unparsed) response, the request, and an error code.

```js
amadeus.referenceData.urls.checkinLinks.get({
  airlineCode: 'BA'
}).then(function(response){
  console.log(response.body);   //=> The raw body
  console.log(response.result); //=> The fully parsed result
  console.log(response.data);   //=> The data attribute taken from the result
}).catch(function(error){
  console.log(error.response); //=> The response object with (un)parsed data
  console.log(error.response.request); //=> The details of the request made
  console.log(error.code); //=> A unique error code to identify the type of error
});
```

### Pagination

If an API endpoint supports pagination, the other pages are available under the `.next`, `.previous`, `.last` and `.first` methods.

```js
amadeus.referenceData.locations.get({
  keyword: 'LON',
  subType: 'AIRPORT,CITY'
}).then(function(response){
  console.log(response.data); // first page
  return amadeus.next(response);
}).then(function(nextResponse){
  console.log(nextResponse.data); // second page
});
```

If a page is not available, the response will resolve to `null`.

### Video Tutorial

You can also check the video tutorial on how to get started with the Node SDK.

![type:video](https://www.youtube.com/embed/rfkgJLKlI4s)

### Managing API rate limits

[Amadeus Self-Service APIs](https://developers.amadeus.com/self-service){:target="\_blank"} have [rate limits](../api-rate-limits.md){:target="\_blank"} in place to protect against abuse by third parties. You can find Rate limit example in Node using the Amadeus Node SDK [here](https://github.com/amadeus4dev-examples/APIRateLimits){:target="\_blank"}. 
