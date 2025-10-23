---
title: Common Errors - REST API Response Codes
---

# Common client and server errors

Amadeus for Developers Self-Service APIs use HTTP status codes to communicate whether a request has been successfully processed.

## Types of errors

There two main types of errors are:

* **Client**:  typically occur when the request has not been properly built. 
* **Server**: occur when there is an issue on the server side.

## Client errors

If your API request is invalid, you will receive a `Client Error` response with an HTTP `4xx` status code. The body of the response will match the format defined in our `swagger` schema and provide details about the error.

### Authorization errors

**400 Bad request - Unsupported grant type**

Occurs when using a grant type other than `client credentials`. For more information, read our [Authorization Guide](API-Keys/authorization.md).

```json
{
    "error": "unsupported_grant_type",
    "error_description": "Only client_credentials value is allowed for the body parameter grant_type",
    "code": 38187,
    "title": "Invalid parameters"
}
```

**401 Unauthorized - Invalid access token**

Occurs when the access token provided in the Authorization header is expired or not longer valid. You must generate a new token.

```json
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


**401 Unauthorized -  Invalid client**

Occurs when the client credentials have an invalid format and are not recognized.

```json
{
    "error": "invalid_client",
    "error_description": "Client credentials are invalid",
    "code": 38187,
    "title": "Invalid parameters"
}
```

**401 Unauthorized - Invalid HTTP header**

The Authorization header is missing or its format invalid, e.g. the required word "Bearer" is wrongly spelled or not present at all in the Authorization header in an API request.
```json
{
    "errors": [
        {
            "code": "38191",
            "title": "Invalid HTTP header",
            "detail": "Missing or invalid format for mandatory Authorization header",
            "status": "401"
        }
    ]
}
```

**401 Unauthorized – Access token expired**

The access token sent by the client is expired. Access tokens are only valid for 30 minutes. To ease the generation of access tokens you can use our SDKs.
```json
{
    "errors": [
        {
            "code": 38192,
            "title": "Access token expired",
            "detail": "The access token is expired",
            "status": 401
        }
    ]
}
```

**401 Unauthorized – Access token revoked**

The access token has been revoked. Please generate a new one.
```json
{
    "errors": [
        {
            "code": 38193,
            "title": "Access token revoked",
            "detail": "The access token is revoked",
            "status": 401
        }
    ]
}
```

**401 Unauthorized –API revoked**

The API credentials have been revoked. This could be because we found it searchable in a public repository, in this case you can generate new keys in your Self-Service workspace. Or it could be that you have unpaid bills and we revoked your access, if that is the case please contact support.

```json
{
    "errors": [
        {
            "code": 39683,
            "title": "API key revoked",
            "detail": "The API key is revoked",
            "status": 401
        }
    ]
}
```

**401 Unauthorized – Invalid API key**

The API key used is invalid. Please check for spaces in the end and make sure you are using the correct key and case URL.
```json
{
    "errors": [
        {
            "code": 39686,
            "title": "Invalid API key",
            "detail": "The API key is invalid",
            "status": 401
        }
    ]
}
```

### Data Format Errors

**400 Bad request - Invalid format**

Occurs when an input query parameter is incorrect. In the example below, the Airport & City Search API returns an error because the location parameter is not in the expected IATA standard.

```json
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

**403 Forbidden**

The HTTP protocol is used instead of HTTPS when making the API call. Or you are attempting to reach an endpoint which requires additional permission. 
```json
{
    "errors": [
        {
            "code": 38197,
            "title": "Forbidden",
            "detail": "Access forbidden",
            "status": 403
        }
    ]
}
```

### Too Many Requests Errors

**429 Too many requests**

Too many requests are sent in the given timeframe. Please check our rate limits and adjust accordingly for the targeted environment and API.
```json
{
    "errors": [
        {
            "code": 38194,
            "title": "Too many requests",
            "detail": "The network rate limit is exceeded, please try again later",
            "status": 429
        }
    ]
}
```


**429 Quota limit exceeded**

The number of free transactions allowed in test has been reached for this month. Please consider moving your app to production or wait next month to keep using the APIs.
```json
{
    "errors": [
        {
            "code": 38195,
            "title": "Quota limit exceeded",
            "detail": "The quota limit is exceeded.",
            "status": 429
        }
    ]
}
```

### Resource Errors

**404 Not found - Resource not found**

Occurs when the endpoint or URL does not exist. Make sure you are calling a valid endpoint and that there are no spelling errors.

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

## Server errors

If an error occurs during the execution of your request, you will receive
a `Server error` resonse with an HTTP `5xx` status code. The body will match the defined error format, allowing your application to read it and display an appropriate message to the client. It may also contain debugging information which you can submit to us to further investigate the error.

**500 Internal error**

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

