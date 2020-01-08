---
description: Learn the basics for getting a list of flight offers in less than 3 minutes.
---

# Making your first API call

## Step 1: Create an account

The first step to start using Amadeus Self-Service APIs is to register and create an account:

* In the top right corner of the page, click on [register](https://developers.amadeus.com/register)
* Complete the form, using a valid email address and click on the `Create account` button. An automatic confirmation email will be sent to the email address you registered
* In the confirmation email you receive, click on `Confirm my account`

You can now log in to the portal with your new credentials! Welcome to **Amadeus for Developers**!

## Step 2: Get your API key

To start using the APIs you need to tell the system that you are allowed to do so. This process is called authentication.

{% hint style="danger" %}
Remember that the API Key and API Secret are for personal use only. Do not share them with anyone.
{% endhint %}

All you need to do is to attach an alphanumeric string called **token** to your calls. This token will identify you as valid user and is generated from two parameters: `API Key` and `API Secret`. In order to get them, and once your account has been verified, you can [sign in](https://developers.amadeus.com/signin) and follow these steps:

* Click on your username \(top right corner\)
* Go to [My Self-Service Workspace](https://developers.amadeus.com/my-apps)
* Click on **Create New App** button
* Enter your application details and click on **Create**

{% hint style="success" %}
**Test environment** 

At this stage you are using the testing environment, where you will enjoy a fixed free number of free API call quota per month for all your applications. When you reach the limit, you will receive an error message. Use this limited data collection to prototype your app and get ready for launching it to the market.
{% endhint %}

## Step **3**: calling the API

For our first call, let's get a list of possible destinations from Paris for a maximum amount of 200 EUR using the [Flight Inspiration Search API](https://developers.amadeus.com/self-service/category/203/api-doc/3/api-docs-and-example/10001), which returns a list of destinations from a given origin along with the cheapest price for each one.

### Creating the Request

Before making your first API call, you need to get your **access token**. For security purposes we implemented the `oauth2` process that will give you your access token based on your `API Key` and `API Secret.` In order to retrieve the **token,** the we need to send a `POST` request to the following endpoint `/v1/security/oauth2/token,`with the correct `Content-Type` header and body:

```bash
curl "https://test.api.amadeus.com/v1/security/oauth2/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
```

{% hint style="warning" %}
Please take a look at our [Authorization guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization) to understand how the process works in deep.
{% endhint %}

The documentation says you need to use `v1/shopping/flight-destinations` as endpoint followed by the mandatory parameter `origin`. As you want to filter the offers to those cheaper than 200 EUR, you need to add the `maxPrice` parameter as well.

Our call is therefore:

```bash
curl 'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=PAR&maxPrice=200' \
      -H 'Authorization: Bearer ABCDEFGH12345'
```

Note how we add the `Authorization` header to the request with value `Bearer` string concatenated with the token previously requested.

### Evaluating the Response

The response returns a `JSON` object containing a list of destinations matching our criteria:

```javascript
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


