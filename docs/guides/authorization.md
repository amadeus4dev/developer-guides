# Authorization

In the following guide you will learn how to perform the authorization needed to access all our APIs.

The basic steps are:

1. Open an account on the [Amadeus for Developers portal](https://developers.amadeus.com/create-account)
2. Create an app
3. Get your `API Key` and `API Secret`
4. Make a call to our authorization server to get an access token
5. Call the APIs you want using the access token

!!! warning
    Please make sure that you do not share your `API Key` and your `API Secret` as these are strictly private.

## Introduction to OAuth

OAuth is a protocol that enables a token-based workflow, which is more secure
than basic authentication. It provides a way to ensure that a specific user has
permissions to access services and resources.

`OAuth` uses `access tokens` for accessing APIs. A token represents a
permission granted to a client to access some protected resources. The method
to acquire a token is called **grant**.

There are different types of OAuth grants. **Amadeus for Developers** uses the
`Client Credentials Grant`.

## Authorization Flow

### Requesting a Token

To request an access token you need to send a POST request with the following body parameters to the authorization server:

* `grant_type` with the value `client_credentials`
* `client_id` with your `API Key`.
* `client_secret` with your `API Secret`.

There are different content types to send information via POST to the server.
Our authorization request will be encoded as `x-www-form-urlencoded`, where the keys
and values are encoded in key-value tuples separated by '&', with a '=' between
the key and the value.

!!!information
    Remember that both `API Key` and `API Secret` were provided to you when you created your application in the portal.

Let's use `cURL` to request a new token. We need to send a `POST` request to
the following endpoint `/v1/security/oauth2/token`. Note that there is no need
to specify the `-X POST` parameter as we are sending a body, `cURL` automatically
prepares the `POST`.

As mentioned, we need to specify the type of the request using the
`content-type` HTTP header set to `application/x-www-form-urlencoded`.

```bash
curl "https://test.api.amadeus.com/v1/security/oauth2/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
```

### Understanding the Response

The authorization server will respond with a JSON object containing the following properties:

* `type` set to `amadeusOAuth2Token` string.
* `username` your username \(email address\).
* `application_name` the name of your application.
* `client_id` your `API Key` \(same as the one used in the request\).
* `token_type` with the value `Bearer`.
* `access_token` your authorization token.
* `expires_in` an integer representing the expiration time \(in seconds\) of the given token.
* `state` with the value `approved`

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

### Using the Token

Once the token has been retrieved you are ready to perform your API calls.

To get access to the API you want, you need to add the `authorization` header
to your request with the value `Bearer {access_token}`, where `acess_token` is
the token you have just retrieved.

You can then call, for example, the `Check-in Links` API to retrieve the
check-in URL for Iberia \(`IB`\):

```bash
curl "https://test.api.amadeus.com/v2/reference-data/urls/checkin-links?airline=1X" \
     -H "Authorization: Bearer CpjU0sEenniHCgPDrndzOSWFk5mN"
```

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

Although `cURL` helps to understand how authorization works, we highly
recommend you use our [Amadeus for Developers
SDKs](https://github.com/amadeus4dev). The `SDKs` abstract all the complexity
of the implementation for you.

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

