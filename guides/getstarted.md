# Self-Service Get Started Guide

## Set up your account

The first step to start using Amadeus Self-Service APIs is to register and create an account:

1. In the top right of the page, click on [register](https://developers.amadeus.com/create-account)
2. Complete the form, using a valid email address and click on `Create account` button. An automatic confirmation email is sent to the email address you registered.
3. In the confirmation email you receive, click on `Confirm my account`.

You can now log in to the portal with your new credentials! Welcome to __Amadeus for Developers__!


## Get your API key

To start using the APIs you need to tell the system that you are allowed to do so. This process is called authentication. All you need to do is to attach an alphanumeric string called __token__ to your calls. This token will identify us as valid users and is generated from two parameters: `API Key` and `API Secret`.

Getting the `API Key` and `API Secret` is easy. Once your account has been verified, you can [sign in](https://developers.amadeus.com/login) and follow these steps:

1. Click on your username (top right corner)
2. Go to [My Self-Service Workspace](https://developers.amadeus.com/my-apps)
3. Click on __Create New App__ button
4. Enter your application details and click on __Create__.

Your `API Key` and `API Secret` will be provided to you on the next screen:

![png](../images/sandbox.png)

It's important to understand that at this stage you are using  __Testing environment__ (Sandbox). This environment allows you to access the APIs for free, up to a certain number of calls. There are however limitations regarding the data which is either cached data, limited coverage or fake data. Check out our [pricing](https://developers.amadeus.com/pricing) page for more information about the quotas for each API.

> Remember that the API Key and API Secret are for personal use only. Do not share them with anyone (even in Testing environment). If you are developing a web based application, please make sure your API Key and Secret are stored on backend side.

Applications using __Testing environment__ can be easily identified because they all have the `Test` tag:

![appTesting](../images/apptesting.png)

The easiest way to start playing with APIs is probably through cURL. Let’s see how to request a token and perform our first call.

To request a new token using the cURL command you need to send a POST request to the following endpoint `/v1/security/oauth2/token` sending your `API Key` and `API Secret` in the body of the request:


```python
curl \
-X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
https://test.api.amadeus.com/v1/security/oauth2/token \
-d "grant_type=client_credentials&client_id=PgtsC87KMeMAUTAmT985jrdOMNALe&client_secret=Qw12345erTy"
```

> Note that as you are sending the parameters in the body of the HTTP message as name/value pairs separated by the ampersand (&), you need to set the header
`content-type` to `application/x-www-form-urlencoded`.

The response will contain a newly generated `access token` which you can use to access all resources:


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
> Please note that the token is valid for 30 minutes. Once expired, you'll need to generate a new one following the same procedure.

You are ready to perform our first call! 

## Make your first call

We recommend you use one of our [existing SDKs](https://github.com/amadeus4dev) available for Node, Java, Python and Ruby, but for this example we will use cURL.

For our first call, let's get a list of possible destinations from Paris for a maximum amount of 200 EUR using the [Flight Inspiration Search API](https://developers.amadeus.com/self-service/category/203/api-doc/3/api-docs-and-example/10001) which returns a list of destinations from a given origin along with the cheapest price for each one.

The documentation says you need to use `v1/shopping/flight-offers` as endpoint followed by the mandatory parameter `origin`. As you want to filter the offers to those cheaper than 200 EUR, you need to add the `maxPrice` parameter as well.

Our call is therefore:

```python
curl -X GET \
'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=PAR&maxPrice=200'\
-H "Authorization: Bearer ApjU0sEenniHCgPDrndzOSWFk5mN"
```

> Note how the `authorization` header has been added to the request with the value `Bearer {access_token}`, where `acess_token` is the token you have just retrieved.

The response returns a JSON object containing a list of destinations matching our criteria:

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

## What's next?

### Explore our APIs

You can find all our APIs in our [API catalogue](https://developers.amadeus.com/self-service). Don’t forget to stop by our [GitHub workspace](https://github.com/amadeus4dev/) which contains tons of samples and prototypes where you can inspire from.

We also provide a useful [Cheat Sheet](https://developers.amadeus.com/self-service/cheat_sheet.pdf) with instructions on how to get started and where you can see all APIs at glance.

And finally, if you are a happy postman user, as we are, feel free to use the [Amadeus for Developers postman collection](https://documenter.getpostman.com/view/2672636/RWEcPfuJ).

### Go live

Ready to move to production? We have prepared a [move to production guide](production.md) which explains how to request a production key.

