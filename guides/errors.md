![Amadeus for Developers](../../master/images/logo.png)

# Error Handling

In this tutorial you will learn how to understand and handle errors with our APIs. 
 
## Types of Error

There two main type of errors depending on which side of the flow happen:

* Client: typically when the request has not been correctly built. We can debug and fix.
* Server: when something happened on the server side and has to be reported.


### Client Errors

If your API request is invalid you will receive a `Client Error` in response from
the system, with a HTTP `4xx` status code. The body of the response will match
the format defined in our `swagger` schema and generally provides more
information on why the request was invalid.

#### 1. Authorization Errors

##### 401 Invalid Token

Usually happens when the access token provided in the Authorization header is
no longer valid because it has already expired. In this particupar case you
need to request a new access token.

```
{
    "errors": [
        {
            "code": 38190,
            "title": "Invalid access token",
            "detail": "The access token provided in the Authorization header is invalid",
            "status": 401
        }
    ]
}
```

##### 400 Unsupported Grant Type

When trying to use a grant type different to `client credentials`. Make sure
you are following our [authorization](authorization.md) guide.


```json
{
    "error": "unsupported_grant_type",
    "error_description": "Only client_credentials value is allowed for the body parameter grant_type",
    "code": 38187,
    "title": "Invalid parameters"
}
```

##### 401 Invalid consumer key

The client credentials have invalid format and are not recognised.

```json
{
    "error": "invalid_client",
    "error_description": "Client credentials are invalid",
    "code": 38187,
    "title": "Invalid parameters"
}
```

#### 2. Data Format Errors

##### 400 Location format

The location parameter is expected to use IATA standard.

```
{
    "errors": [
        {
            "status": 400,
            "code": 477,
            "title": "INVALID FORMAT",
            "detail": "City/Airport - 3 characters [IATA code](https://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code) from which the traveler will depart.",
            "source": {
                "parameter": "origin"
            }
        }
    ]
}
```

##### 400 Collapse source format

```json
{
    "errors": [
        {
            "status": 400,
            "code": 4926,
            "title": "INVALID DATA RECEIVED",
            "detail": "Past date/time not allowed",
            "source": {
                "parameter": "departureDate/returnDate"
            }
        }
    ]
}
```

#### 3. Resource Errors

##### 401 Resource not found

The endpoint or URL does not exists. Probably you are trying to call a non
existing endpoint. Make sure this endpoint is correctly spelled.

```json
{
    "errors": [
        {
            "code": 38196,
            "title": "Resource not found",
            "detail": "The targeted resource doesn't exist",
            "status": 404
        }
    ]
}
```

### Server Errors

If something went wrong during the execution of your request, you will receive
a Server error in response from the system, with a HTTP `5xx` status code. The
body will again match the defined error format, allowing your application to
easily read it and display an appropriate message to the client. It may also
carry some debugging information which you can submit to us if you would like
us to investigate the error further

The following example shows an internal server error:

```json
{
    "errors": [
        {
            "code": 38189,
            "title": "Internal error",
            "detail": "An internal error occured, please contact your administrator",
            "status": 500
        }
    ]
}
```
