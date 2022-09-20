# Making your first API call

## Step 1: Create an account

The first step to start using Amadeus Self-Service APIs is to register and create an account:

* Open the [Amadeus Developers Portal](https://developers.amadeus.com/).
* Click on [Register](https://developers.amadeus.com/register).
* Complete the form using a valid email address and click on the `Create account` button. An automatic confirmation email will be sent to the email address you provided.
* In the confirmation email you receive, click on `Activate your account`. 

You can now log in to the portal with your new credentials! Welcome to **Amadeus for Developers**!

## Step 2: Get your API key

To start using the APIs, you need to tell the system that you are allowed to do so. This process is called authorization.

!!! danger
    Remember that the API Key and API Secret are for personal use only. Do not share them with anyone.

All you need to do, is to attach an alphanumeric string called **token** to your calls. This token will identify you as a valid user.  Each token is generated from two parameters: `API Key` and `API Secret`. Once your account has been verified, you can get your API key and API Secret by following these steps:

* Sign in to the [Developers Portal](https://developers.amadeus.com/signin).
* Click on your username \(located in the top right corner of the [Developers portal](https://developers.amadeus.com/) page\) 
* Go to [My Self-Service Workspace](https://developers.amadeus.com/my-apps). 
    ![api_key1](../images/api_key1.png)

* Click on **Create New App** button.
    ![api_key2](../images/api_key2.png)

* Enter your application details and click on **Create**.
    ![api_key3](../images/api_key3.png)

!!! important
    **Test environment** <br>
    At this stage, you are using the testing environment, where you will enjoy a fixed number of free API call quotas per month for all your applications. When you reach the limit, you will receive an error message. This environment will help you build and test your app for free and get ready for deploying it to the market.

## Step 3: Calling the API

For our first call, let's get a list of possible destinations from Paris for a maximum amount of 200 EUR using the [Flight Inspiration Search API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-inspiration-search/api-reference), which returns a list of destinations from a given origin along with the cheapest price for each destination.

### Creating the Request

Before making your first API call, you need to get your **access token**. For security purposes, we implemented the `oauth2` process that will give you an access token based on your `API Key` and `API Secret.` To retrieve the **token**, you need to send a `POST` request to the endpoint `/v1/security/oauth2/token`with the correct `Content-Type` header and body. Replace `{client_id}` with your API Key and `{client_secret}` with your API Secret in the command below and execute it:

```bash
curl "https://test.api.amadeus.com/v1/security/oauth2/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
```

!!! warning
    Please take a look at our [Authorization guide](API-Keys/authorization.md) to understand how the process works in depth.

According to the documentation, you need to use `v1/shopping/flight-destinations` as the endpoint, followed by the mandatory query parameter `origin`. As you want to filter the offers to those cheaper than 200 EUR, you need to add the `maxPrice` parameter to your query as well.

Our call is therefore:

```bash
curl 'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=PAR&maxPrice=200' \
      -H 'Authorization: Bearer ABCDEFGH12345'
```

Note how we add the `Authorization` header to the request with the value `Bearer` string concatenated with the token previously requested.

### Evaluating the Response

The response returns a `JSON` object containing a list of destinations matching our criteria:

```json
{
    "data": [
        {
            "type": "flight-destination",
            "origin": "PAR",
            "destination": "CAS",
            "departureDate": "2022-09-06",
            "returnDate": "2022-09-11",
            "price": {
                "total": "161.90"
            }
        },
        {
            "type": "flight-destination",
            "origin": "PAR",
            "destination": "AYT",
            "departureDate": "2022-10-16",
            "returnDate": "2022-10-31",
            "price": {
                "total": "181.50"
            }
        }
    ]
}
```

Congratulations! You have just made your first Amadeus for Developers API call!

