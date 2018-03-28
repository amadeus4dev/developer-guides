![Amadeus for Developers](../../master/images/logo.png)

# Authorization

In the following guide we will learn how to perform the authentication and
authorization in our applications.

Beware that before making any requests to the APIs, you must sign up in the
portal in order to get your client and application keys.

## Introduction to OAuth

OAuth is, in a nutshell, a protocol that supports authorization workflows. In
other words, it provides a way to ensure that a specific user has permissions
to do something.

Rather than using API keys for API access, `OAuth` needs to use `access
tokens`.  A token represents a permission granted to a client to access some
protected resources. The method to acquire a token is called __grant__.

There are 4 separate types of OAuth grants, depending who owns the token and
whether or not the client is capable of keeping a secret. Each mode serves a
different purpose, and is used in a different way:

1. `Authorization Code Grant`. This grant is used when you are building a web
   application with server side component.
2. `Implicit Grant Type`. Used on web applications that don’t have a server
   side component (only front end).
3. `Password Credentials Grant`. The user provides their service credentials
   (username and password) directly to the application, which uses the
   credentials to obtain an access token from the service. Normally is used
   when the user fully trusts on the application (native applications). 
4. `Client Credentials Grant`. This grant is suitable when building an
   application that is requesting access to protected resources under its
   control and there is no third-party involved.

### Client Credential Grant

Client Credentials is the grant used in __Amadeus for Developers__. Let's see
how it works and kind of parameters are necesary to perform the authentication.

#### Authentication Flow

To request an access token you will need to send a POST request with following
body parameters to the authorization server:

* `grant_type` with the value `client_credentials`
* `client_id` with the client id.
* `client_secret` with the client secret.

Both `client_id` and `client_secret` have been provided to you when registering
new applications in the portal.

The authorization server will respond with a JSON object containing the following properties:

* `type` usually set to `amadeusOAuth2Token` string.
* `username` which contains the username (mail address).
* `application_name` with the application name created in the portal.
* `client_id` with the client id (same value as the request).
* `token_type` with the value `Bearer`.
* `access_token` which contains the authorization token.
* `expires_in` with an integer representing the expiration time (in seconds) for the given token.
* `state` with the value `approved`

#### Requesting an Access Token via cURL

On the following example, we are going to request a new token using the `cURL`
command. 

In order to perform the authentication, we need to make a `POST` request to the
following endpoint `v1/security/oauth2/token`.

```bash
curl \
-X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
https://test.api.amadeus.com/v1/security/oauth2/token \
-d "grant_type=client_credentials&client_id={consumer-key}&client_secret={consumer-secret}"
```

Since we are sending the parameters on the body of the HTTP message as
name/value pairs separated by the ampersand (&), we need to send the header
`content-type` as `application/x-www-form-urlencoded`.

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

You can copy your token and use it in the same way as you would use an API Key.

#### Requesting an Access Token using Ruby

Following the same approach, your can use your favourite language to retrieve an `access token`.

```ruby
TOKEN_REQUEST_URL = 'https://test.api.amadeus.com/v1/security/oauth2/token'
CONSUMER_KEY = 'zzz'
CONSUMER_SECRET = 'xxx'

client = OAuth2::Client.new(CONSUMER_KEY, CONSUMER_SECRET, token_url: TOKEN_REQUEST_URL)
token = client.client_credentials.get_token
```

Our `token` variable is ready to be used in further API calls.

#### Using the `access_token` to call other APIs

Once the token has been requests, you are ready to perform your API calls.

In order to get access to the protected resources, you need to add an the
`authorization` header to your request with the value `Bearer {access_token}`,
where `acess_token` is the previously obtained token.

The following example uses `cURL` to call `Check-in Links` API to retrieve the
check-in URL of the `1X` airline:

```bash
curl -X GET \
  "https://test.api.amadeus.com/v2/reference-data/urls/checkin-links?airline=1X" \
      -H "Authorization: Bearer CpjU0sEenniHCgPDrndzOSWFk5mN"
```

The response will be a 200 status code along with the data:

```json
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

### Authorization with SDKs

Even though is recommended to understand how the authorization works using
`OAuth`, we highly recommend to use the [Amadeus for Developers
SDKs](https://github.com/amadeus4dev) as much as possible.  The `SDKs` wraps
all the complexity and abstracts the implementation.

The following example initializes the client and perform the authentication
underneath:

```js
var Amadeus = require('amadeus');

var amadeus = new Amadeus({
  clientId: '[YOUR_CLIENT_ID]',
  clientSecret: '[YOUR_CLIENT_SECRET]'
});

```

The `SDK` stores the `access_token` and set all needed headers automatically.

