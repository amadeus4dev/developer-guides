# Generating SDKs from Amadeus OpenAPI specification using the OpenAPI Generator

The [OpenAPI Generator](https://openapi-generator.tech/){:target="\_blank"} is an open-source project for generating REST API clients, server stubs, documentation and schemas based on the OpenAPI specification.

At Amadeus, we are following the contract-first approach to API development, which is at the core of the OpenAPI Generator's design philosophy. In this way, we only need to create or update an OpenAPI specification for a particluar API, and the OpenAPI Generator will automatically generate the SDKs in various programming languages and create the required API documentation.

## Amadeus OpenAPI specification

We have a [dedicated GitHub repository](https://github.com/amadeus4dev/amadeus-open-api-specification){:target="\_blank"} where you can find OpenAPI specification files for all our Self-Serving APIs. The OpenAPI Generator can easily consume these files to output a dedicated SDK for any of the [languages](https://openapi-generator.tech/docs/generators){:target="\_blank"} that it supports.

### How to create an SDK from Amadeus OpenAPI specification

If you are not familiar with the OpenAPI Generator, the following tutorial may help you get started. We will take Ruby as an example and show you the steps to create a turnkey SDK based on the specification for your required Amadeus API. We will use the [City Search API](https://github.com/amadeus4dev/amadeus-open-api-specification/blob/main/spec/json/CitySearch_v1_swagger_specification.json){:target="\_blank"} in our example.


#### Step 1. Setting up the OpenAPI Generator

!!! information
    The current stable release version of the OpenAPI Generator at the time of writing this document is 6.0.1.

There are many ways to [set up](https://openapi-generator.tech/docs/installation){:target="\_blank"} the OpenAPI Generator. To eliminate the need for any system dependencies, we will run the OpenAPI Generator as a Docker container. As a prerequisite to this, we need to install the [Docker Desktop](https://docs.docker.com/desktop/){:target="\_blank"} on our host and start running it.

#### Step 2. Downloading the OpenAPI specification for the City Search API

Navigate to the [Amadeus OpenAPI Specification](https://github.com/amadeus4dev/amadeus-open-api-specification){:target="\_blank"} and download the JSON file for the [City Search API specification](https://github.com/amadeus4dev/amadeus-open-api-specification/blob/main/spec/json/CitySearch_v1_swagger_specification.json){:target="\_blank"}. 

!!! information
    You can use both JSON and YAML files with the OpenAPI Generator. 

#### Step 3. Creating the Ruby SDK for the City Search API

!!! information
    The `docker run` command uses the `openapi-generator-cli` image: https://hub.docker.com/r/openapitools/openapi-generator-cli/.

Navigate to the directory where you downloaded the City Search API specification and run the following command:

```shell
docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/CitySearch_v1_swagger_specification.json \
  -g ruby \
  -o /local/city_search_ruby
```

This command uses the `CitySearch_v1_swagger_specification.json` as input (`-i`) located in the current directory (`/local/`). It generates (`-g`) a Ruby SDK (indicated by `ruby`) and outputs (`-o`) the files to folder `city_search_ruby`, which is located in the current directory (`/local/`).

#### Step 4. Enabling usage of the Ruby SDK for the City Search API

!!! information
    Before using the API you will need to get an access token. Please read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to get your token.

Navigate to the newly created `city_search_ruby` folder and open the `README.md`. This file shows the initial instructions on configuring our Ruby SDK for the City Search API.

Follow the instructions in the `README.md` to build the code into a gem and install it locally by running the following command from the `city_search_ruby` directory:

```shell
gem build ./openapi_client.gemspec
gem install ./openapi_client-1.0.0.gem
```

!!! information
    You may need to run this command with administrator privileges (`sudo`).

Now we have a full-featured Ruby SDK that is ready for production usage.

#### Step 5. Customising the Ruby SDK for the City Search API

There are several ways to customise an SDK created by the OpenAPI Generator:

* Using a configuration file
* Using command line arguments
* Using mustache templates

##### Configuration file

There is a number of configuration options that the OpenAPI Generator supports for [Ruby](https://openapi-generator.tech/docs/generators/ruby#config-options){:target="\_blank"}.

To apply them, we need to create a JSON file with the required parameters and define it when running the OpenAPI Generator. Let's create a file called `config.json` with the following contents:

```json
{
"gemName": "Amadeus_City_Search",
"gemSummary": "A ruby wrapper for the Amadeus City Search API",	
"moduleName": "CitySearch",
"gemLicense": "MIT",
"gemVersion": "0.3.1",
"gemRequiredRubyVersion": "2.1"
}
```

To generate an SDK with these custom parameters, put the `config.json` file into the same directory as the source OpenAPI specification file and run:

```shell
docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/CitySearch_v1_swagger_specification.json \
  -g ruby \
  -o /local/city_search_ruby \
  -c config.json \
```

##### Command line arguments

Instead of using a configuration file, we can specify the custom parameters as additional properties, separated by a comma:

```shell
docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/CitySearch_v1_swagger_specification.json \
  -g ruby \
  -o /local/city_search_ruby \
- -additional-properties gemVersion=0.3.1,gemName=Amadeus_City_Search
```

You can otherwise specify the parameters directly, for example:

```shell
--git-user-id openapi-generator-user --git-repo-id AmadeusCitySearch
```

This command will upload the SDK to a repository `AmadeusCitySearch` by the user called `openapi-generator-user`.

##### Mustache template

To customise the SDK beyond the custom parameters, we can use mustache templates. The [GitHub repository](https://github.com/OpenAPITools/openapi-generator){:target="\_blank"} of the OpenAPI Generator contains default mustache templates at `tree/master/modules/openapi-generator/src/main/resources/`. For our Ruby Client SDK, we will need the [api_client_spec template](https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator/src/main/resources/ruby-client/api_client_spec.mustache){:target="\_blank"}.

Download the template and customise it as required. After that, attach the template to the OpenAPI `run` command as follows:

```shell
docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/CitySearch_v1_swagger_specification.json \
  -g ruby \
  -o /local/city_search_ruby
  -t <path-to-template-directory>
```

Replace `<path-to-template-directory>` with the path to the template directory.

#### Step 6. Integrating the Ruby SDK for the City Search API with other libraries

Suppose we want to integrate our City Search Ruby SDK into an existing application that already contains many models defined in third-party libraries. One of these models may contain a model whose name is the same as in our City Search Ruby SDK. A solution to this is to add a prefix to all models generated by OpenAPI Generator using the
`--model-name-prefix` setting. For example:

```shell
docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/CitySearch_v1_swagger_specification.json \
  -g ruby --model-name-prefix Amadeus \
  -o /local/city_search_ruby
```

In this way, all models in our SDK will be prefixed with `Amadeus`, e.g. `AmadeusComponent`.

### Conclusion

In this tutorial we have seen how easy it is to generate a basic SDK from our API specification files using the OpenAPI Generator. We took Ruby as an example, but the OpenAPI Generator supports [many other languages](https://openapi-generator.tech/docs/generators){:target="\_blank"}, so you can easily find a solution that meets your requirements.
