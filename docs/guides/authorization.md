# Authorization

In the following guide you will learn how to perform the authorization needed to access all our APIs.

The basic steps are:

1. Open an account on the [Amadeus for Developers portal](https://developers.amadeus.com/create-account)
2. Create an app
3. Get your `API Key` and `API Secret`
4. Make a call to our authorization server to get an access token
5. Call the APIs you want using the access token

{% hint style="info" %}
Please make sure that you do not share your `API Key` and your `API Secret` as these are strictly private.
{% endhint %}

## Introduction to OAuth

OAuth is a protocol that enables a token-based workflow, which is more secure than basic authentication. It provides a way to ensure that a specific user has permissions to access services and resources.

`OAuth` uses `access tokens` for accessing APIs. A token represents a permission granted to a client to access some protected resources. The method to acquire a token is called **grant**.

There are different types of OAuth grants. **Amadeus for Developers** uses the `Client Credentials Grant`.

## Authorization Request/Response Flow

### Request

To request an access token you need to send a POST request with the following body parameters to the authorization server:

* `grant_type` with the value `client_credentials`
* `client_id` with your `API Key`.
* `client_secret` with your `API Secret`.

Both `API Key` and `API Secret` were provided to you when you created your application in the portal.

### Response

The authorization server will respond with a JSON object containing the following properties:

* `type` set to `amadeusOAuth2Token` string.
* `username` your username \(email address\).
* `application_name` the name of your application.
* `client_id` your `API Key` \(same as the one used in the request\).
* `token_type` with the value `Bearer`.
* `access_token` your authorization token.
* `expires_in` an integer representing the expiration time \(in seconds\) of the given token.
* `state` with the value `approved`

## Getting the token through examples

### cURL

To request a new token using the `cURL` command you need to make a `POST` request to the following endpoint `/v1/security/oauth2/token`.

```bash
curl "https://test.api.amadeus.com/v1/security/oauth2/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
```

As we are sending the parameters in the body of the HTTP message as name/value pairs separated by the ampersand \(&\), we need to set the header `content-type` to `application/x-www-form-urlencoded`.

The response will contain the newly generated `access_token` which you can use to access all resources.

```javascript
{
    "type": "amadeusOAuth2Token",
    "username": "foo@bar.com",
    "application_name": "BetaTest_foobar",
    "client_id": "3sY9VNvXIjyJYd5mmOtOzJLuL1BzJBBp",
    "token_type": "Bearer",
    "access_token": "CpjU0sEenniHCgPDrndzOSWFk5mN",
    "expires_in": 1799,
    "state": "approved",
    "scope": ""
}
```

Once the token has been retrieved you are ready to perform your API calls.

To get access to the API you want, you need to add the `authorization` header to your request with the value `Bearer {access_token}`, where `acess_token` is the token you have just retrieved.

You can then call, for example, the `Check-in Links` API to retrieve the check-in URL for Iberia \(`IB`\):

```bash
curl "https://test.api.amadeus.com/v2/reference-data/urls/checkin-links?airline=1X" \
     -H "Authorization: Bearer CpjU0sEenniHCgPDrndzOSWFk5mN"
```

```javascript
> Output
{
    "data": [
        {
            "type": "checkin-link",
            "id": "1XEN-GBWeb",
            "href": "https://www.onex.com/manage/check-in",
            "channel": "Web"
        }
    ]
}
```

### Ruby

For this example we will use `oauth2` gem.

To install it:

```ruby
gem install oauth2
```

Following the same approach as with cURL, you can retrieve your `access token` as follows:

```ruby
require 'oauth2'

client = OAuth2::Client.new([CLIENT_ID], [CLIENT_SECRET], site: 'https://test.api.amadeus.com', token_url: 'https://test.api.amadeus.com/v1/security/oauth2/token')
token = client.client_credentials.get_token
```

You can now use your `token` to make an API call:

```ruby
response = token.get('/v1/reference-data/locations',
  params: {
    subType: 'AIRPORT',
    keyword: 'Los'
  })

response_body = JSON.parse(response.body)

puts response_body['data'].first['iataCode']
```

```text
> Output
LAX
```

### With our SDKs

Although it helps to understand how authorization works using `OAuth`, we highly recommend you use our [Amadeus for Developers SDKs](https://github.com/amadeus4dev). The `SDKs` abstract all the complexity of the implementation for you.

This is how you can initialize the client and authenticate with the Node SDK:

```javascript
var Amadeus = require('amadeus');

var amadeus = new Amadeus({
  clientId: '[API Key]',
  clientSecret: '[API Secret]'
});
```

The `SDK` fetches and stores the `access_token` and then sets all the headers automatically in all API calls.

You can then call for example the Flight Check-in Links API:

```javascript
amadeus.referenceData.urls.checkinLinks.get({ airline: 'IB' });
```

