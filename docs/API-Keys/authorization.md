# Authorizing your application

Amadeus for Developers uses `OAuth` to authenticate access requests. `OAuth` generates an `access token` which grants the client permission to access a protected resource. 

The method to acquire a token is called **grant**. There are different types of `OAuth grants`. Amadeus for Developers uses the `Client Credentials Grant`.

## Requesting an access token

Once you have created an app and received your `API Key` and  `API Secret`, you can generate an access token by sending a `POST` request to the authorization server:

[https://test.api.amadeus.com/v1/security/oauth2/token](https://test.api.amadeus.com/v1/security/oauth2/token){:target="\_blank"}

!!!information
    Remember that your `API Key` and  `API Secret` should be kept private. Read more about best practices for [secure API key storage](https://developers.amadeus.com/blog/best-practices-api-key-storage).

The body of the request is encoded as `x-www-form-urlencoded`, where the keys and values are encoded in key-value tuples separated by '&', with a '=' between
the key and the value:

| **Key** | **Value** |
| ----------- | ----------- |
| `grant_type`      | The value `client_credentials`        |
| `client_id`       | The `API Key` for the application     |
| `client_secret`   | The `API Secret` for the application  |

Specify the type of the request using the `content-type` HTTP header with the value `application/x-www-form-urlencoded`.

The following example uses `cURL` to request a new token:

```bash
curl "https://test.api.amadeus.com/v1/security/oauth2/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=<YOUR-CLIENT-ID>&client_secret=<YOUR-CLIENT-SECRET>"
```
Replace `<YOUR-CLIENT-ID>` with your API Key and `<YOUR-CLIENT-SECRET>` with your API Secret in the command above.

Note that the `-X POST` parameter is not needed in the `cURL` command. As we are sending a body, `cURL` sends the request as `POST` automatically.

## Response

The authorization server will respond with a JSON object:

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
The response will contain the following parameters:

| **Parameter**      | **Description** |
| ----------- | ----------- |
| `type`      | The type of resource. The value will be `amadeusOAuth2Token`. |
| `username`       | Your username \(email address\).        |
| `application_name`   | The name of your application.  |
| `client_id`      |  The `API Key` for your application  |
| `token_type`       | The type of token issued by the authentication server. The value will be `Bearer`.        |
| `access_token`   | The token to authenticate your requests.  |
| `expires_in`   | The number of seconds until the token expires.  |
| `state`   | The status of your request. Values can be `approved` or `expired`.  |

## Using the token

Once the token has been retrieved, you can authenticate your requests to Amadeus Self-Service APIs.

Each API call must contain the `authorization` HTTP header with the value `Bearer <access_token>`, where `<acess_token>` is the token you have just retrieved.

The following example is a call to the `Flight Check-in Links` API to retrieve the check-in URL for Iberia \(`IB`\):

```bash
curl "https://test.api.amadeus.com/v2/reference-data/urls/checkin-links?airline=IB" \
     -H "Authorization: Bearer <YOUR-BEARER-TOKEN>"
```
Replace `<YOUR-BEARER-TOKEN>` with the token you received from the authorization call.

## Managing tokens from your source code

To retrieve a token using your favourite programming language, send a `POST` request and parse the `JSON` response as in the `cURL` examples above.  

There are different strategies to maintain your token updated, like checking the time remaining until expiration before each API call or capturing the `unauthorized` error when the token expires. In both cases, you must request a new token.

To simplify managing the authentication process, you can use the [Amadeus for Developers SDKs](https://github.com/amadeus4dev){:target="\_blank"} available on GitHub. The `SDKs`
automatically fetch and store the `access_token` and set the headers in all API
calls.

Example of initializing the client and authenticating with the `Node` SDK:

```javascript
var Amadeus = require('amadeus');

var amadeus = new Amadeus({
  clientId: '<YOUR-CLIENT-ID>',
  clientSecret: '<YOUR-CLIENT-SECRET>'
});
```
Replace `<YOUR-CLIENT-ID>` with your API Key and `<YOUR-CLIENT-SECRET>` with your API Secret.

You can then call the API. The following example is a call to the `Flight Check-in Links` API to retrieve the check-in URL for Iberia \(`IB`\):


```javascript
var Amadeus = require('amadeus');

var amadeus = new Amadeus({
  clientId: '<YOUR-CLIENT-ID>',
  clientSecret: '<YOUR-CLIENT-SECRET>'
});

amadeus.referenceData.urls.checkinLinks.get({
  airlineCode : 'IB'
}).then(function(response){
  console.log(response.data);
}).catch(function(responseError){
  console.log(responseError.code);
});
```
Replace `<YOUR-CLIENT-ID>` with your API Key and `<YOUR-CLIENT-SECRET>` with your API Secret.

