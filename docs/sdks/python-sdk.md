# Python SDK

## Installation

The Python SDK has been uploaded to the official [Python package
repository](https://pypi.org/project/amadeus/), which makes life easier since
you can install the SDK as a regular Python package.

### Prerequisites

-  Amadeus for Developers API key and API secret: to get one, [create a free developer account](https://developers.amadeus.com/register) and set up your first application in your [Workspace](https://developers.amadeus.com/my-apps).
- Python version >= 3.4
- [virtualenv](https://virtualenv.pypa.io/en/latest/) when installing packages for your local projects. There are several beneficts of creating isolated environment, but the most interesting one is to avoid conflicts between different versions of the same package. 

The tool can be easily installed using `pip`:

```text
pip install virtualenv
```

Next step is to create the environment. Switch to your project repository and type:

```text
virtualenv venv
```

A new folder `venv` will be created with everything necessary inside. Let's activate the isolated environment with the following command:

```text
source venv/bin/activate
```

From now on, all packages installed using `pip` will be located under `venv/lib` and not on your global `/usr/lib` folder.

Finally, install the Amadeus SDK as follows:

```text
pip install amadeus
```

You can also add it to your `requirements.txt` file and install using:

```text
pip install -r requirements.txt
```

The virtual environment can be disabled by typing:

```text
deactivate
```



## Making your first API call 

This tutorial will guide you through the process of creating a simple Python application which calls the Airport and Search API using the Amadeus for Developers Python SDK.

### Request

```python
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='REPLACE_BY_YOUR_API_KEY',
    client_secret='REPLACE_BY_YOUR_API_SECRET'
)

try:
    response = amadeus.reference_data.locations.get(
    keyword='LON',
    subType=Location.AIRPORT)    
    print(response.data)
except ResponseError as error:
    print(error)
```

- Once you import the amadeus library, you initialize the client by adding your credentials in the `builder` method. The library can also be initialized without any parameters when the environment variables `AMADEUS_CLIEN_ID` and `AMADEUS_CLIENT_SECRET` are present.
- The authentication process is handled by the SDK and the access token is renewed every 30 minutes.
- The SDK uses namespaced methods to create a match between the APIs and the SDK. In this case, the API `GET /v1/reference-data/locations?keyword=LON&subType=AIRPORT` is implemented as `amadeus.reference_data.locations.get(keyword='LON',subType=Location.AIRPORT)`.

### Handling the response  

Every API call returns a `Response` object. If the API call contains a JSON response, it will parse the JSON into the `.result` attribute. If this data also contains a data key, it will make that available as the `.data` attribute. The raw body of the response is always available as the `.body` attribute.

```python
print(response.body) #=> The raw response, as a string
print(response.result) #=> The body parsed as JSON, if the result was parsable
print(response.data) #=> The list of locations, extracted from the JSON
```

## Arbitrary API calls

You can call any API not yet supported by the SDK by making arbitrary calls.

For the `get` endpoints:

```python
amadeus.get('/v2/reference-data/urls/checkin-links', airlineCode='BA')


```

For the `post` endpoints:

```python
amadeus.post('/v1/shopping/flight-offers/pricing', body)

```

## Video Tutorial

You can also check the video tutorial on how to get started with the Python SDK.

![type:video](https://www.youtube.com/embed/R8LolxJTzQk)