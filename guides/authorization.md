![Amadeus for Developers](../../master/images/logo.png)

# Authorization

In the following guide you will learn how to perform the authorization to access all our APIs.

The basic steps are as follows:

1. [Register](https://uat.developers.amadeus.com/create-account) on the portal
2. Create an app to get your `API Key` and `API Secret`
3. Make an authorization call to get your access token
4. Call the API you want using the access token

> Please insure that you do not commit your `API Key` and your `API Secret`. 


## Introduction to OAuth

OAuth is a protocol that enables a token-based workflow which is more secure than basic authentication. It provides a way to ensure that a specific user has permissions to access services and resources.

Rather than using API keys for API access, `OAuth` uses `access
tokens`.  A token represents a permission granted to a client to access some
protected resources. The method to acquire a token is called __grant__.

There are different types of OAuth grants. __Amadeus for Developers__ uses the `Client Credentials Grant`.  

## Authorization Request/Response Flow

### Request
To request an access token you need to send a POST request with the following
body parameters to the authorization server:

* `grant_type` with the value `client_credentials`
* `client_id` with your `API Key`.
* `client_secret` with your `API Secret`.

Both `API Key` and `API Secret` were provided to you when you created your application in the portal.

### Response
The authorization server will respond with a JSON object containing the following properties:

* `type` set to `amadeusOAuth2Token` string.
* `username` your username (email address).
* `application_name` your application name created in the portal.
* `client_id` your `API Key` (same as the one used in the request).
* `token_type` with the value `Bearer`.
* `access_token` your authorization token.
* `expires_in` an integer representing the expiration time (in seconds) of the given token.
* `state` with the value `approved`

## Examples of how to get the token

### cURL

In the following example, you are going to learn how to request a new token using the `cURL` command. 

To do so you need to make a `POST` request to the
following endpoint `/v1/security/oauth2/token`.

```bash
curl \
-X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
https://test.api.amadeus.com/v1/security/oauth2/token \
-d "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
```

As we are sending the parameters in the body of the HTTP message as
name/value pairs separated by the ampersand (&), we need to set the header
`content-type` to `application/x-www-form-urlencoded`.

The response will contain the newly generated `access_token` which you can use
to access all resources.

```json
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

Once the token has been requested, you are ready to perform your API calls.

In order to get access to the protected resources, you need to add an the
`authorization` header to your request with the value `Bearer {access_token}`,
where `acess_token` is the previously obtained token.

You can then for example call the `Check-in Links` API to retrieve the
check-in URL for Iberia (`IB`):

```bash
curl -X GET \
  "https://test.api.amadeus.com/v2/reference-data/urls/checkin-links?airline=1X" \
      -H "Authorization: Bearer CpjU0sEenniHCgPDrndzOSWFk5mN"
```

```json
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
```
> Output
LAX
```


### With our SDKs

Although it helps to understand how authorization works using
`OAuth`, we highly recommend to use our [Amadeus for Developers
SDKs](https://github.com/amadeus4dev).  The `SDKs` wrap
all the complexity and abstraction the implementation for you.

This is how you can initialize the client and authenticate
with the Node SDK:

```js
var Amadeus = require('amadeus');

var amadeus = new Amadeus({
  clientId: '[API Key]',
  clientSecret: '[API Secret]'
});

```

The `SDK` fetches and stores the `access_token` and then sets all the headers automatically in all API calls.





