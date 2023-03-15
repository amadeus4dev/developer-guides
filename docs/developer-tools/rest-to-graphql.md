# Wrap a REST API endpoint with GraphQL

Follow this tutorial to wrap a REST API endpoint with a GraphQL wrapper to make it accessible via a dedicated GraphQL API.

In this tutorial we will use a standalone [Apollo server](https://www.apollographql.com/), which is an easy-to-use option for setting up a GraphQL server without any additional configuration. For the REST API endpoint we will use the [City Search API](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search).

The goal of this tutorial is to create a GraphQL API, which will only use the `keyword` parameter for the query and return only the `name` parameter in the response.

## Pre-requisites

Before you begin, you need to:

* Register your application with Amadeus for Developers as described in [Making your first API call](../quick-start.md).
* Have Node.js installed on your machine.

## Initialize a new Node.js project

1. Open your terminal and create a new directory for this project:
   ```shell
   mkdir graphql-wrapper
   ```
2. Navigate to the directory and run the following command to initialize a new Node.js project:
   ```shell
   cd graphql-wrapper
   npm init -y
   ```

## Install required dependencies

Install `apollo-server`, `graphql`, and `node-fetch` packages by running:

```shell
npm install apollo-server graphql node-fetch
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

!!! information
    The `node-fetch` package is an ECMAScript module (ESM), so we will use .mjs extensions and ECMAScript module syntax in these examples.

Create a `fetchData.mjs` file and define a function that fetches data from the REST endpoint using `node-fetch`:

```js
import fetch from 'node-fetch';


const fetchCities = async (keyword, token) => {
  const endpoint = `https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword=${keyword}`;

  const response = await fetch(endpoint, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });

  const data = await response.json();

  console.log('API Response:', data);

  return data.data;
};

export { fetchCities };
```

In the above example we are outputting logs to the console for easier troubleshooting.

## Implement GraphQL resolvers

Create a `resolvers.mjs` file and implement the resolver functions for the queries:

```ts
import { fetchCities } from './fetchData.mjs';

const resolvers = {
  Query: {
    getCities: async (_, { keyword }, { token }) => {
      const cities = await fetchCities(keyword, token);
      return cities.map(city => ({ name: city.name }));
    },
  },
};

export default resolvers;
```

## Set up the Apollo server

Create the main file `index.mjs` that sets up the Apollo server with the schema and resolvers:

```js
import { ApolloServer, gql } from 'apollo-server';
import { readFileSync } from 'fs';
import resolvers from './resolvers.mjs';

const typeDefs = gql(readFileSync('./schema.graphql', 'utf8'));

const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: ({ req }) => {
    const token = req.headers.authorization || '';

    return { token };
  },
});

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
```

## Run the server

Open the terminal and run:

```js
node index.mjs
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
  http://localhost:4000/
```

If your token is valid, the above command will return a list of city names that contain the word `Paris`.
