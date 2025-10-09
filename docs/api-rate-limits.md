---
title: API Rate Limits
---

# Rate limits

## Rate limits per API
[Amadeus Self-Service APIs](https://developers.amadeus.com/self-service){:target="\_blank"} have two types of **rate limits** in place to protect against abuse by third parties.

### Artificial Intelligence and Partners' APIs

Artificial intelligence APIs and APIs from Amadeus partners' are currently following the rate limits below. 

| Test and Production                   |
|---------------------------------------|
| 20 transactions per second, per user |
| No more than 1 request every 50ms   |

#### List of APIs with the above rate limits:

- [Tours and Activities](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities){:target="\_blank"}
- [Airport On-time Performance](https://developers.amadeus.com/self-service/category/air/api-doc/airport-on-time-performance)
- [Flight Price Analysis](https://developers.amadeus.com/self-service/category/air/api-doc/flight-price-analysis){:target="\_blank"}
- [Flight Delay Prediction](https://developers.amadeus.com/self-service/category/air/api-doc/flight-delay-prediction){:target="\_blank"}
- [Flight Choice Prediction](https://developers.amadeus.com/self-service/category/air/api-doc/flight-choice-prediction){:target="\_blank"}



### The other APIs

**The rest of Self-Service APIs** apart from Artificial intelligence and Partners' APIs are below rate limits **per environment**.

| **Test** | **Production** |
| :--- | :--- |
| 10 transactions per second, per user | 40 transactions per second, per user  |
| No more than 1 request every 100ms | |

## Rate limits Examples 
To manage the rate limits in APIs, there are mainly two options: 
- Use an external library
- Build a request queue from scratch

The right choice depends on your resources and requisites. 

Check out the [rate limits examples](https://github.com/amadeus4dev-examples/APIRateLimits){:target="\_blank"} in Node, Python and Java using the respective [Amadeus SDKs](./developer-tools/index.md).
