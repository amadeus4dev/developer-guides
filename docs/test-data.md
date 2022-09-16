# Free test data collection of Self-Service APIs

To build and test your applications, Amadeus for Developers provides a `Test Environment` with limited data collections. To access live data, you must move to `Production Environment`. The table below details the test data collection for each Self-Service API.

## Air


| **API**      | **Test data** |
| ----------- | ----------- |
| [Flight Inspiration Search](https://developers.amadeus.com/self-service/category/air/api-doc/flight-inspiration-search) | See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/flightsearch.md). |
| [Flight Cheapest Date Search](https://developers.amadeus.com/self-service/category/air/api-doc/flight-cheapest-date-search) |  See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/flightsearch.md). |
| [Flight Availabilities Search](https://developers.amadeus.com/self-service/category/air/api-doc/flight-availabilities-search)  | Cached data including most origin and destination cities/airports. |
| [Airport Routes](https://developers.amadeus.com/self-service/category/air/api-doc/airport-routes) |  Static dataset containing all airport routes in November 2021. |
| [Flight Offers Search](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search) |  Cached data including most origin and destination cities/airports. |
| [Flight Offers Price](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-price) |  Cached data including most origin and destination cities/airports. |
| [Branded Fares Upsell](https://developers.amadeus.com/self-service/category/air/api-doc/branded-fares-upsell) |  Cached data including most airlines. |
| [SeatMap Display](https://developers.amadeus.com/self-service/category/air/api-doc/seatmap-display) |  Works with the response of Flight Offers Search. |
| [Flight Create Orders](https://developers.amadeus.com/self-service/category/air/api-doc/flight-create-orders) |  Works with the response of Flight Offers Price. |
| [Flight Order Management](https://developers.amadeus.com/self-service/category/air/api-doc/flight-order-management)  | Works with the response of Flight Create Orders. |
| [Flight Price Analysis](https://developers.amadeus.com/self-service/category/air/api-doc/flight-price-analysis) |  No data restrictions in test. |
| [Flight Delay Prediction](https://developers.amadeus.com/self-service/category/air/api-doc/flight-delay-prediction) | No data restrictions in test. |
| [Airport On-time Performance](https://developers.amadeus.com/self-service/category/air/api-doc/airport-on-time-performance) |  No data restrictions in test. |
| [Flight Choice Prediction](https://developers.amadeus.com/self-service/category/air/api-doc/flight-choice-prediction) | No data restrictions in test. |
| [On Demand Flight Status](https://developers.amadeus.com/self-service/category/air/api-doc/on-demand-flight-status)  | Cached data including most flights returned by Flight Offers Search. |
| [Flight Most Traveled Destinations](https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-traveled-destinations) |  See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/ti.md). |
| [Flight Busiest Traveling Period](https://developers.amadeus.com/self-service/category/air/api-doc/flight-busiest-traveling-period) |  See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/ti.md). |
| [Flight Most Booked Destinations](https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-booked-destinations) |  See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/ti.md). |
| [Airline Code Lookup](https://developers.amadeus.com/self-service/category/air/api-doc/airline-code-lookup) |  No data restrictions in test. |
| [Airport & City Search](https://developers.amadeus.com/self-service/category/air/api-doc/airport-and-city-search) |  Cities/airports in the United States, Spain, the United Kingdom, Germany and India. |
| [Airport Nearest Relevant](https://developers.amadeus.com/self-service/category/air/api-doc/airport-nearest-relevant)  | Cities/airports in the United States, Spain, the United Kingdom, Germany and India. |
| [Flight Check-in Links](https://developers.amadeus.com/self-service/category/air/api-doc/flight-check-in-links) |  See list of [valid airlines](https://github.com/amadeus4dev/data-collection/blob/master/data/checkinlinks.md). |


## Hotel


| **API**      | **Test data** |
| ----------- | ----------- |
| [Hotel Search](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search) |  See list of [valid hotel chains](https://github.com/amadeus4dev/data-collection/blob/master/data/hotelchains.md). Test with major cities like `LON` or `NYC`. |
| [Hotel Booking](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-booking) |  Works with the response of `Hotel Search`. |
| [Hotel Ratings](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-ratings) |  See list of [valid hotels](https://github.com/amadeus4dev/data-collection/blob/master/data/hotelratings.md). |
| [Hotel Name Autocomplete](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-name-autocomplete) | Cached data including most hotels available through Amadeus |


## Destination Content

| **API**      | **Test data** |
| ----------- | ----------- |
| [Safe Place](https://developers.amadeus.com/self-service/category/destination-content/api-doc/safe-place) |  See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md). |
| [Travel Restrictions](https://developers.amadeus.com/self-service/category/destination-content/api-doc/travel-restrictions) | Cached data for all available countries/cities. |
| [Points of Interest](https://developers.amadeus.com/self-service/category/destination-content/api-doc/points-of-interest) | See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md). |
| [Location Score](https://developers.amadeus.com/self-service/category/destination-content/api-doc/location-score) |  See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md). |
| [Tours and Activities](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities) |  See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md). |


## Trip

| **API**      | **Test data** |
| ----------- | ----------- |
| [Trip Parser](https://developers.amadeus.com/self-service/category/trip/api-doc/trip-parser) |  No data restrictions in test. |
| [Trip Purpose Prediction](https://developers.amadeus.com/self-service/category/trip/api-doc/trip-purpose-prediction)  | No data restrictions in test. |
| [AI-generated Photos](https://developers.amadeus.com/self-service/category/trip/api-doc/ai-generated-photos) | No data restrictions in test. |
| [Travel Recommendations](https://developers.amadeus.com/self-service/category/trip/api-doc/travel-recommendations)  | No data restrictions in test. |

