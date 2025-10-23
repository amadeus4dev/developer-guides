---
title: OpenAPI to GraphQL Converter Tutorial
---

# Convert an OpenAPI specification to a GraphQL schema

Follow this tutorial to learn how to convert an OpenAPI specification to a GraphQL schema.

Our Self-Service APIs are stored as OpenAPI specs in [this repository](https://github.com/amadeus4dev/amadeus-open-api-specification). In this tutorial, we will use the [City Search API](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search/api-reference) spec as an example and convert it to a GraphQL schema using [openapi-to-graphql](https://github.com/IBM/openapi-to-graphql). While there are many similar tools available, the underlying principle remains the same.

The goal is to create a GraphQL schema and then utilise this schema for your GraphQL wrapper, regardless of the programming language your GraphQL server is written in.

## Pre-requisites

Before you begin, you need to:

* Have Node.js installed on your machine.

## Install the openapi-to-graphql tool

```shell
npm install -g openapi-to-graphql-cli
```

## Download the required OpenAPI schema

Navigate to the [amadeus-open-api-specification repository](https://github.com/amadeus4dev/amadeus-open-api-specification) and download the required specification for your API. Alternatively, you can visit the [Developers portal](https://developers.amadeus.com/self-service) and download the specification from the page of a specific API.

## Convert

For example, let's download the [City Search API](https://developers.amadeus.com/self-service/category/trip/api-doc/city-search/api-reference) OpenAPI specification to the same directory where we run our project. We will then specify the name for the output file - `schema.graphql` and execute the following command:

```shell
openapi-to-graphql CitySearch_v1_Version_1.0_swagger_specification.json --save schema.graphql   
```

## Access the generated schema

The schema is now created as `schema.graphql`. For the City Search API, the contents will appear like this:

```ts
type Query {
  """
  GET Cities by keyword
  
  Equivalent to GET /reference-data/locations/cities
  """
  referenceDataLocationsCities(
    """ISO 3166 Alpha-2 code. e.g. "US" United States of America."""
    countryCode: String

    """Resources to be included example : Airports"""
    include: [IncludeListItem]

    """keyword that should represent the start of a word in a city name."""
    keyword: String!

    """Number of results user want to see in response."""
    max: Int
  ): String
}

enum IncludeListItem {
  AIRPORTS
}
```

## Import the schema to your code

Depending on the server that we use, we will now need to reference this schema. For example, in Node.js, you can use the Apollo Server library to create a GraphQL server:

```js
const { ApolloServer, gql } = require('apollo-server');
const fs = require('fs');

const typeDefs = gql(fs.readFileSync('<path-to-generated-graphql-schema>', 'utf8'));
const resolvers = {}; // Implement your resolvers here

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
```
Replace `<path-to-generated-graphql-schema>` with the path to the schema generated in the **Convert** step.
