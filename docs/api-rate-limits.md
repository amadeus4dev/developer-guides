# Rate limits

## Rate limits per API
[Amadeus Self-Service APIs](https://developers.amadeus.com/self-service) have two types of **rate limits** in place to protect against abuse by third parties.

### Artificial Intelligence and Partners' APIs 

Artificial intelligence APIs and APIs from Amadeus partners' are currently following the rate limits below. 

<center>

| Test and Production                   |
|---------------------------------------|
| 20 transactions per second, per user |
| No more than 1 request every 50ms   |

</center>

| API Category             | API Sub Category        | API name                                                                                                                          |
|--------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Covid-19 & Travel Safety | Covid-19                | [Travel Restrictions](https://developers.amadeus.com/self-service/category/destination-content/api-doc/travel-restrictions)       |
| Covid-19 & Travel Safety | Location Risk           | [ Safe Place ]( https://developers.amadeus.com/self-service/category/destination-content/api-doc/safe-place )                     |
| Air                      | Artificial Intelligence | [ Airport On-time Performance ]( https://developers.amadeus.com/self-service/category/air/api-doc/airport-on-time-performance )   |
| Air                      | Artificial Intelligence | [ Flight Price Analysis  ]( https://developers.amadeus.com/self-service/category/air/api-doc/flight-price-analysis )              |
| Air                      | Artificial Intelligence | [ Flight Choice Prediction ]( https://developers.amadeus.com/self-service/category/air/api-doc/flight-choice-prediction )         |
| Air                      | Artificial Intelligence | [ Flight Delay Prediction ]( https://developers.amadeus.com/self-service/category/air/api-doc/flight-delay-prediction )           |
| Destination Content      | Location                | [ Points of Interest ]( https://developers.amadeus.com/self-service/category/destination-content/api-doc/points-of-interest )     |
| Destination Content      | Location                | [ Tours and Activities ]( https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities ) |
| Destination Content      | Travel Insight          | [ Location Score ]( https://developers.amadeus.com/self-service/category/destination-content/api-doc/location-score )             |



### The other APIs

**The rest of Self-Service APIs** apart from Artificial intelligence and Partners' APIs are below rate limits **per environment**.

<center>

| **Test** | **Production** |
| :--- | :--- |
| 10 transactions per second, per user | 40 transactions per second, per user  |
| No more than 1 request every 100ms | |

</center>

## Rate limits Examples 
To manage the rate limits in APIs, we have mainly two options, use an external library or build a request queue from scratch. The choice depends on your resources and requisites. There are some great open-source ones available for the main programming languages. You can find [Rate limit examples](https://github.com/amadeus4dev-examples/APIRateLimits){:target="\_blank"} in Node, Python and Java using the respective [Amadeus SDK](https://amadeus4dev.github.io/developer-guides/programming/).