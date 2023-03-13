# Introducing the Travel Restrictions API v2 : Get more travel safety data

Many things have changed in the travel industry since we [introduced](https://developers.amadeus.com/blog/-introducing-amadeus-covid-19-travel-restrictions-api){:target="\_blank"} our [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"} in the summer of last year.

With the successful rollout of the COVID-19 vaccination programme and the continuous improvement of testing technology, public health safety measures have been continuously refined. 

To keep up with these developments, we have expanded the scope of the [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"} to ensure that our customers get the most relevant information on the latest COVID-19 safety and travel regulations.

In this blog post, we would like to highlight the most notable additions to the original API.

## How to use Travel Restrictions API

The new edition of the [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"} is located in the same Self-Service and Enterprise catalogues.

If you are already using the [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"}, just change the prefix of the base URL from v1 to v2.

If you are new to the [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"}:

1. [Sign-up for a free account](https://developers.amadeus.com/register){:target="\_blank"} 

2. Create a new project in your [Self-Service Workspace](https://developers.amadeus.com/my-apps){:target="\_blank"} to get your API key 

3. Follow the steps in our [Authentication Guide](../API-Keys/authorization.md) to generate your access token 

4. Make your first call using the [API reference](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions/api-reference){:target="\_blank"} or the tool of your choice. 

In our test environment, you’ll have access to sample data and 200 free requests per month to build your app, with live data available once you move to production. To help you along the way, you can also check out our client libraries and code samples on GitHub and get support straight from the Amadeus developer relations team on Discord.

### Get responses in multiple languages
The new [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"} can show the search results in several languages. This is enabled by the new query parameter language, which currently supports English (EN), Spanish (ES), French (FR), German (DE), Japanese (JA), Korean (KO), Thai (TH), Bahasa (ID), and Chinese (ZH).

### New object for travel test conditions and rules

We have redesigned the entire object related to the test conditions and rules to expand it with more detailed information on COVID-19 testing. All testing-related information is now aggregated into a single object `travelTestConditionsAndRules`.

The `travelTestConditionsAndRules` object is divided into the string `travelPhases` and the object scenarios. The `travelPhases` indicates the phase of the travel to which the test conditions and rules apply, such as "before travel", "upon travel" etc. The scenarios drills further down into the travel specifics.

Each scenario is identified by the string name and contains two objects:

`condition` - this is the travel test condition in terms of what type of traveller needs a test and for what kind of trip. 

`rule` - this is the travel test rule in terms of exemptions, test type and validity period. 

### What is included in the travel test conditions?

The `condition` object contains three items:

`traveller` - the Travel Test Traveller condition, defined by the string `whoNeeds` (indicating the type of traveller who needs to take a test) and the string `minimumAge` (indicating the minimum age to take a test). 

`trip` - the Travel Test Trip condition, defined by the object countries and the strings `destinationCountry` (IATA code), `destinationCity` (city name), `transitCountry` (IATA code), `transitCity` (IATA code). 

`textualScenario` - the free text string to describe the travel scenario. 

The object countries is essentially defined by another object – `Area`, which gives a more precise description of the place that the traveller goes to. The `Area` contains the strings name (which indicates the name of the area), code (IATA code of the area), `areaType` (such as country, city, region etc.; as you see, the `Area` is not limited to only countries) and the object `geoCode`, which contains the integers `latitude` (in the range from -90 to 90) and `longitude` (in the range from -180 to 180).

### What is included in the travel test rules?

The `rule` object contains three items:

`exemptions` – this string describes any applicable exemptions to the tests. 

`test` - the Travel Test Requirements Rules object, which contains the string `types` (indicating the test types) and the object `validity`, containing the strings `delay` (validity period for the test) and `referenceDateTime` (reference date and time for the test validity period). 

`arrivalTestDays` - this string indicates the time period to take a test upon arrival. 

### New object for declaration documents

We have also added an object that provides information on the traveller’s health insurance requirements. This is now defined by a dedicated object `healthInsurance`, which contains the strings `isRequired` (showing whether a health insurance is required for this trip), `minAmount` (minimum coverage of the insurance, if required), `currencyCode` (insurance coverage currency) and text for any additional comments.

### Additional information on banned travellers

The Entry schema now contains a list of travellers banned from entering a particular area. This is reflected in the bannedTravellers string.

### Additional data on disease infection

A new string trend has been added to the Disease Infection dataset. This trend compares the infection rate from the latest week to that of the previous week. This can be “Significant Decrease”, “Significant Increase”, “Decrease”, “Increase” or “Steady”. We can now also see any additional comments in the text string.

### New object for travel vaccination

The Travel Vaccination object has been expanded with a new object `qualifiedVaccines` and the integer `minimumAge` (indicating the minimum age, in years, to get a vaccine; no vaccine is required for persons under this age).

The `qualifiedVaccines` object contains the following items:

`supportedVaccineProducts` - a string for the vaccine’s short name. 

`numberOfDoses` - an integer defining the number of doses required for full vaccination. 

`expiration` - an object containing the strings `expiresAfter` and `referenceDateTime` defining the vaccine’s expiration date. 

`boosterRequired` - a string showing whether a booster shot is required. 

`boosterExpiration` - an object containing the strings expiresAfter and `referenceDateTime`, which define the booster’s expiration date. 

`validity` - an object containing the strings delay and `referenceDateTime`, which define the validity period and reference date and time for the vaccine. 

### New object for area health passes

A new object `AreaHealthPass` contains information about the health pass required for a specific area. This object contains the following items:

`isRequired` - a string that indicates whether a health pass is required for this area. 

`applicationGuidance` - a string that explains what activities and establishments require a health pass. 

`obtentionMethods` - a string that explains how to obtain a health pass. 

`referenceLink` - a string for a URL to the health pass rules, web portal or app landing page. 

`lastUpdate` - the last date of the health pass update. 

`text` - a string for any additional comments.  

We have also renamed several existing parameters to provide more clarity about their purpose. 

## Get the most out of your travel safety data

To get the most out of the new [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"}, we recommend combining it with other Amadeus APIs. For example, if you are planning a journey, you can use the [Flight Offers Search API](https://developers.amadeus.com/blog/migrate-to-the-new-flight-offers-search-api){:target="\_blank"} and the [Hotel List API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-list){:target="\_blank"} to explore the tickets and accommodation options. Once you know where to go and where to stay, reach out to the [Travel Restrictions API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/travel-restrictions){:target="\_blank"} for any advice on the latest COVID-19 safety and travel requirements that are relevant to your plan and maximise the safety of your journey by running your destination choice by the Safe Place API.

Collaboration and technology are key to drive our industry towards a brighter future. Together, let’s rebuild travel.
