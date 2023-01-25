# Python

## Python SDK

### Installation

You can call the Amadeus APIs using the Python SDK. The Python SDK has been uploaded to the official [Python package
repository](https://pypi.org/project/amadeus/), which makes life easier since
you can install the SDK as a regular Python package.

#### Prerequisites

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



### Your first API call 

This tutorial will guide you through the process of creating a simple Python application which calls the Airport and Search API using the Amadeus for Developers Python SDK.

#### Request

```python
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='AMADEUS_CLIENT_ID',
    client_secret='AMADEUS_CLIENT_SECRET'
)

try:
    response = amadeus.reference_data.locations.get(
    keyword='LON',
    subType=Location.AIRPORT)    
    print(response.data)
except ResponseError as error:
    print(error)
```

- Once you import the amadeus library, you initialize the client by adding your credentials in the `builder` method. The library can also be initialized without any parameters when the environment variables `AMADEUS_CLIENT_ID` and `AMADEUS_CLIENT_SECRET` are present.
- The authentication process is handled by the SDK and the access token is renewed every 30 minutes.
- The SDK uses namespaced methods to create a match between the APIs and the SDK. In this case, the API `GET /v1/reference-data/locations?keyword=LON&subType=AIRPORT` is implemented as `amadeus.reference_data.locations.get(keyword='LON',subType=Location.AIRPORT)`.

#### Handling the response  

Every API call returns a `Response` object. If the API call contains a JSON response, it will parse the JSON into the `.result` attribute. If this data also contains a data key, it will make that available as the `.data` attribute. The raw body of the response is always available as the `.body` attribute.

```python
print(response.body) #=> The raw response, as a string
print(response.result) #=> The body parsed as JSON, if the result was parsable
print(response.data) #=> The list of locations, extracted from the JSON
```

### Arbitrary API calls

You can call any API not yet supported by the SDK by making arbitrary calls.

For the `get` endpoints:

```python
amadeus.get('/v2/reference-data/urls/checkin-links', airlineCode='BA')


```

For the `post` endpoints:

```python
amadeus.post('/v1/shopping/flight-offers/pricing', body)

```

### Video Tutorial

You can also check the video tutorial on how to get started with the Python SDK.

![type:video](https://www.youtube.com/embed/R8LolxJTzQk)

### Managing Amadeus API rate limits using the Python SDK

[Amadeus Self-Service APIs](https://developers.amadeus.com/self-service) have [rate limits](https://amadeus4dev.github.io/developer-guides/api-rate-limits/) in place to protect against abuse by third parties. You can find Rate limit example in Python using the Amadeus Python SDK [here](https://github.com/amadeus4dev-examples/APIRateLimits/tree/master/Python){:target="\_blank"}. 

## Python Async API calls

In a synchronous program, each step is completed before moving on to the next one. However, an asynchronous program may not wait for each step to be completed. Asynchronous functions can pause and allow other functions to run while waiting for a result. This enables concurrent execution and gives the feeling of working on multiple tasks at the same time.

In this guide we are going to show you how to make async API calls in Python to improve the performance of your Python applications.

For all these examples we are going to call the [Flight-Checkin Links API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-check-in-links). 

### Prerequisites

To follow along with the tutorial you will need the followings: 

- Python version >= 3.8
    
- Amadeus for Developers API key and API secret: to get one, [create a free developer account](https://developers.amadeus.com/register) and set up your first application in your [Workspace](https://developers.amadeus.com/my-apps).
    
- `aiohttp`: you will use the [aiohttp](https://docs.aiohttp.org/en/stable/) library to make asynchronous API calls. You can install it using the command `pip install aiohttp`.
    
- `requests`: you will use the [requests](https://requests.readthedocs.io/en/latest/) library for synchronous requests. You can install it using the command `pip install requests`.

- `amadeus`: the Amadeus Pthon SDK. You can install it using the command `pip install amadeus`.


### Async API calls with aiohttp

`aiohttp` is a Python library for making asynchronous HTTP requests build top of `asyncio`. The library provides a simple way of making HTTP requests and handling the responses in a non-blocking way.

In the example below you can call the the Amadeus Flight-Checkin link API using the `aiohttp` library and the code runs in an async way.

```python
import aiohttp
import asyncio
import requests

AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"grant_type": "client_credentials",
        "client_id": 'YOUR_AMADEUS_API_KEY',
        "client_secret": 'YOUR_AMADEUS_API_SECRET'}
response = requests.post(AUTH_ENDPOINT,
                        headers=headers,
                        data=data)
access_token = response.json()['access_token']

async def main():
    headers = {'Authorization': 'Bearer' + ' ' + access_token}
    flight_search_endpoint = 'https://test.api.amadeus.com/v2/reference-data/urls/checkin-links'
    parameters = {"airlineCode": 'BA'}

    async with aiohttp.ClientSession() as session:

        for number in range(20):
            async with session.get(flight_search_endpoint,
                            params=parameters,
                            headers=headers) as resp:
                flights = await resp.json()
                print(flights)
                
asyncio.run(main())
```

The above code makes `POST` request to the Authentication API using the `requests` library. The returned access token is then used in the headers of following requests to make 20 asyncronous API calls.

### Async API calls with thread executor 

Since we offer the Python SDK we want to show you how you are able to make async API calls using the SDK. The SDK is built using the requests `library` which only supports synchronous API calls. This means that when you call an API, your application will block and wait for the response. The solution is to use a thread executor to allow run blocking calls in separate threads, as the example below:

```python
import asyncio
import requests
from amadeus import Client

amadeus = Client(
    client_id='YOUR_AMADEUS_API_KEY',
    client_secret='YOUR_AMADEUS_API_SECRET'
)

async def main():
 
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                None, 
                requests.get,
                amadeus.reference_data.urls.checkin_links.get(
                airlineCode='BA')
            )
            for number in range(20)
            ]
        for response in await asyncio.gather(*futures):
            print(response.status_code)

asyncio.run(main())
```