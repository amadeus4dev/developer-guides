# Node SDK

Amadeus Node SDK for Self-service APIs is available with `npm`(node package manager) and Amadeus for Developers team is continuosly updating with new APIs and features. 
you can refer [Amadeus-node GitHub page](https://github.com/amadeus4dev/amadeus-node) or [Amadeus npm page](https://www.npmjs.com/package/amadeus) for more details of change logs and issues to be fixed for up-to-date usage. 

## Installation
This module has been tested using Node 6 and higher, though it should work with Node 4 and 5 as well. You can install it using Yarn or NPM.

```sh
npm install amadeus --save
```

## Getting Started
To make your first API call, you will need to [register](https://developers.amadeus.com/register) for an Amadeus Developer Account and [set up your first application](https://developers.amadeus.com/my-apps).

```js
var Amadeus = require('amadeus');
var amadeus = new Amadeus({
  clientId: 'REPLACE_BY_YOUR_API_KEY',
  clientSecret: 'REPLACE_BY_YOUR_API_SECRET'
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

## Initialization
The client can be initialized directly as below. Your credentials `client Id` and `Client Secret` can be found on the [Amadeus dashboard](https://developers.amadeus.com/my-apps).


```js
// Initialize using parameters
var amadeus = new Amadeus({
  clientId: 'REPLACE_BY_YOUR_API_KEY',
  clientSecret: 'REPLACE_BY_YOUR_API_SECRET'
});
```

!!! warning
    Remember that direct hard coding your credentials in your code is not the best practice due to the potential exposure them to others. Read more about best practices for [secure API key storage](https://developers.amadeus.com/blog/best-practices-api-key-storage).


Alternatively, you can initialize by setting up environment variables. In Node, we like to use [dotenv package](https://www.npmjs.com/package/dotenv). 

```sh
npm install dotenv
```

Put your API credentials in `.env` file 
```sh
AMADEUS_CLIENT_ID=REPLACE_BY_YOUR_API_KEY,
AMADEUS_CLIENT_SECRET=REPLACE_BY_YOUR_API_SECRET
```

Initialize using dotenv package
```js
const dotenv = require('dotenv').config();
var amadeus = new Amadeus();
```

!!! important
    You will also want to add `.env` to your `.gitingore` so that your API credentials aren't included in your git repository
    
If you don't want to use another package, you can also simply export your key in terminal directly to initalize.

export your credentials in terminal 
```sh
export AMADEUS_CLIENT_ID="REPLACE_BY_YOUR_API_KEY"
export AMADEUS_CLIENT_SECRET="REPLACE_BY_YOUR_API_SECRET"

```
Initialize without 
```js
var amadeus = new Amadeus();
```

## Moving to Production

By default, the SDK environment is set to `test` environment. To switch to a `production` (pay-as-you-go) environment, please switch the hostname as follows:

```js
var amadeus = new Amadeus({
  hostname: 'production'
});
```

## Promises

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

## Pagination

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


## Useful resources
[Get Started amadeus Node SDK with Docker](https://developers.amadeus.com/blog/get-started-amadeus-node-sdk)
