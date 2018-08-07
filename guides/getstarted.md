# Self-Service Get Started Guide

## Set up your account

Creating an account is the first step to start using Amadeus Self-Service APIs.

Go to the upper right corner and click on [register](https://developers.amadeus.com/create-account). Fill in the form and confirm your account by clicking on the `Confirm my account` link you will find in the confirmation email.

Log in to the portal with your new credentials and that’s all! Welcome to __Amadeus for Developers__!


## Get your API key

Let’s make our first call to the APIs. In order to start using the APIs we need to tell the system we are allowed to do so. This process is called authentication and all we need is to attach an alphanumeric string called __token__ to our calls. This token will identify ourselves as valid users and is generated out of two parameters: `API Key` and `API Secret`.

Getting a new `API Key` and `API Secret` is quite easy. Once your account has been verified, all you have to do is:

1. [Sign in](https://developers.amadeus.com/login)
2. Click on your username (top right corner)
3. Go to [My Self-Service Workspace](https://developers.amadeus.com/my-apps)
4. And click on __Create New App__ button.
5. Enter your application details and select __Create__.

Your `API Key` and `API Secret` can be found on the next screen:

![png](../images/sandbox.png)

It's important to understand that at this stage, you are using __Testing environment__ (Sandbox). This environment is free up to a certain number of calls but comes with some limitations: some APIs use cached data, they come with limited number of routes, etc. Check out our [pricing](https://developers.amadeus.com/pricing) page to understand the quotas defined for each API.

Applications using Testing environment can be easily identified because they all have the `Test` tag:

![appTesting](../images/apptesting.png)

There's no easier way to start playing with APIs than through cURL. Let’s see how to request a token and perform our first call.

To request a new token using the cURL command you need to send a POST request to the following endpoint `/v1/security/oauth2/token` sending your `API Key` and `API Secret` on the body of the request:


```python
curl \
-X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
https://test.api.amadeus.com/v1/security/oauth2/token \
-d "grant_type=client_credentials&client_id=PgtsC87KMeMAUTAmT985jrdOMNALe&client_secret=Qw12345erTy"
```

> Note that as we are sending the parameters in the body of the HTTP message as name/value pairs separated by the ampersand (&), we need to set the header
`content-type` to `application/x-www-form-urlencoded`.

Finally, the response will contain the newly generated `access token` which you can use to access all resources:


```elixir
{
    "type": "amadeusOAuth2Token",
    "username": "foo@bar.com",
    "application_name": "foobar_app",
    "client_id": "PgtsC87KMeMAUTAmT985jrdOMNALe",
    "token_type": "Bearer",
    "access_token": "ApjU0sEenniHCgPDrndzOSWFk5mN",
    "expires_in": 1799,
    "state": "approved",
    "scope": ""
}
```
> Be aware that the token is valid for 30 minutes. Once expired, you'll need to retrieve a new one following the same procedure.

We are ready to perform our first call! 

## Your first call

Most applications will use one of our [existing SDKs](https://github.com/amadeus4dev) in the language of your choice, but for this example we are going to use cURL.

For our first call, we would like to get a list of possible destinations based on my current city (Paris) and the maximum amount of money that I'm willing to pay (200 EUR). For this, we are going to make use of the [Flight Inspiration Search API](https://developers.amadeus.com/self-service/category/203/api-doc/3/api-docs-and-example/10001) which returns a list of potential destinations from a given origin along with the cheapest price for each one.

We are going to use `cURL` to call the API. The documentation says we need to use `v1/shopping/flight-offers` as endpoint followed by the mandatory parameter `origin`. Since we are interested to filter the returns to the ones matching my criteria (cheaper than 200 EUR), we need to add the `maxPrice` parameter as well.

Our call looks similar to this:

```python
curl -X GET \
'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=PAR&maxPrice=200'\
-H "Authorization: Bearer ApjU0sEenniHCgPDrndzOSWFk5mN"
```

> Note that we have added the `authorization` header to the request with the value `Bearer {access_token}`, where `acess_token` is the token you have just retrieved.

The response returns a JSON structure containing the destinations matching our criteria:

```elixir
{
    "data": [
        {
            "type": "flight-destination",
            "origin": "PAR",
            "destination": "CAS",
            "departureDate": "2019-01-06",
            "returnDate": "2019-01-11",
            "price": {
                "total": "161.90"
            }
        },
        {
            "type": "flight-destination",
            "origin": "PAR",
            "destination": "AYT",
            "departureDate": "2018-10-16",
            "returnDate": "2018-10-31",
            "price": {
                "total": "181.50"
            }
        }
    ]
}
```

Congratulations! You have just made your first Amadeus for Developers API call!

## Discover our APIs

We invite you to discover our [API catalogue](https://developers.amadeus.com/self-service). Don’t forget to stop by our [Github workspace](https://github.com/amadeus4dev/), which contains tons of samples and prototypes where you can inspire from.

We also provide a useful [Cheat Sheet](https://developers.amadeus.com/self-service/cheat_sheet.pdf) where you can see all APIs at glance.

And finally, if you are happy postman user as we are, feel free to use the [Amadeus for Developers postman collection](https://documenter.getpostman.com/view/2672636/RWEcPfuJ).

## Going live

Once you believe your application is ready to be used in the Real World™, you might consider moving it to __Production Environment__.

Moving your application to Production Environment involves the request of a __Production Key__. But don't be scared! The process is quite easy:

1. [Sign in](https://developers.amadeus.com/login)
2. Click on your username (top right corner)
3. Go to [My Self-Service Workspace](https://developers.amadeus.com/my-apps)
4. Select the application you want to move to Production and click on `Get Production environment` button:

![request_prod](../images/request_production_key.png)

Requesting a Production Key, involves three basic steps:

1. Fill in your personal and billing information: Personal data, billing address and application description.
2. Add your payment information.
3. Sign the agreement. Your contract will be electronically signed using [DocuSign](https://www.docusign.com/). You will receive a copy of the contract via email.

> Heads up! The process to get the production key can take up to 72 hours for the first application. Additional applications will __not__ require any waiting time.

At this point, you can check that your application's tag has changed to __pending__:

![pending](../images/app_pending.png)

Once the validation is completed, you will be notified and the app's tag will change to __live__:

![live](../images/app_live.png)

Your application is ready to disrupt the market!
