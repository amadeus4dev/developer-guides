# Wrap a REST API endpoint with GraphQL in Python

Follow this tutorial to wrap a REST API endpoint with a GraphQL wrapper to make it accessible via a dedicated GraphQL API.

In this tutorial we will use a standalone [Ariadne server](https://ariadnegraphql.org/), which is a Python library for implementing GraphQL servers. It aims to make it easy and enjoyable for developers to create GraphQL APIs by using a schema-first approach, where you define your GraphQL schema using the Schema Definition Language (SDL) and then map your resolvers to the schema.

For the REST API endpoint we will use the [City Search API](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search).

The goal of this tutorial is to create a GraphQL API, which will only use the `keyword` parameter for the query and return only the `name` parameter in the response.

## Pre-requisites

Before you begin, you need to:

* Register your application with Amadeus for Developers as described in [Making your first API call](../quick-start.md).
* Have Python installed on your machine.

## Create a new Pytho  project

1. Open your terminal and create a new directory for this project:
   ```shell
   mkdir graphql-wrapper
   ```
2. Navigate to the directory:
   ```shell
   cd graphql-wrapper
   ```

## Install required dependencies

Install `uvicorn` and `requests` packages by running:

```shell
pip3 install uvicorn
pip3 install requests
```

## Define GraphQL schema

Create a `schema.graphql` file with the necessary types and queries. In this tutorial, we are only using the `keyword` parameter to query the [City Search API](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search) and we are only interested in the `name` parameters that this query returns in the response data. For this reason, our `schema.graphql` will look as follows:

```ts
type Query {
  getCities(keyword: String!): [City]
}

type City {
  name: String
}
```

## Create a data fetching function

Create a `fetch_data.py` file and define a function that fetches data from the REST endpoint:

```py
import requests

def fetch_cities(keyword, token):
    endpoint = f"https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword={keyword}"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    print("API Response:", data)

    return data["data"]
```

In the above example we are outputting logs to the console for easier troubleshooting.

## Implement GraphQL resolvers

Create a `resolvers.py` file and implement the resolver functions for the queries:

```py
from fetch_data import fetch_cities

def resolve_get_cities(_, info, keyword):
    token = info.context["request"].headers["authorization"]
    cities = fetch_cities(keyword, token)
    return [{"name": city["name"]} for city in cities]
```

## Set up the Ariadne server

Create the main file `main.py` that sets up the Ariadne server with the schema and resolvers:

```py
from ariadne import QueryType, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from resolvers import resolve_get_cities

type_defs = load_schema_from_path("schema.graphql")
query = QueryType()
query.set_field("getCities", resolve_get_cities)

schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)
```

## Run the server

Open the terminal and run:

```shell
uvicorn main:app
```

## Query the GraphQL API

!!! information
    Before running the query, make sure to obtain the token as described in our [Authorization guide](../API-Keys/authorization.md).

Now that we have the server running, we can send requests to it. The most straightforward method to do this is by using `curl`. To query this API by the `keyword` "Paris":

```shell
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: <your_bearer_token>" \
  -d '{ "query": "{ getCities(keyword: \"PARIS\") { name } }" }' \
  http://localhost:8000/
```

If your token is valid, the above command will return a list of city names that contain the word `Paris`.
