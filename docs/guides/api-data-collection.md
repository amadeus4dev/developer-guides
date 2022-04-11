# Test data collections

To build and test your applications, Amadeus for Developers provides a `Test Environment` with limited data collections. To access live data, you must move to `Production Environment`. The table below details the test data collection for each Self-Service API.


## COVID and travel safety
| API      | Test data |
| ----------- | ----------- |
| `Safe Place` | See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md)|
| `Travel Restrictions` | Cached data for all available countries/cities|

## Flight

| API      | Test data |
| :----------- | :----------- |
| `Flight Offers Search` |  Cached data including most origin and destination cities/airports|
| `Flight Offers Price` | Cached data including most origin and destination cities/airports|
| `SeatMap Display` | Works with the response of `Flight Offers Search`|
| `Flight Create Orders` | Works with the response of `Flight Offers Price` |
| `Flight Order Management` | Works with the response of `Flight Create Orders` |
| `Flight Choice Prediction` | No data restrictions in test |
| `Branded Fares Upsell` | Cached data including most airports |

## Flight Inspiration

| API      | Test data |
| :----------- | :----------- |
| `Flight Inspiration Search` | See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/flightsearch.md) |
| `Flight Cheapest Date Search` | See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/flightsearch.md) |
| `Flight Availabilities Search` | Cached data including most origin and destination cities/airports |
| `Travel Recommendations` | No data restrictions in test |

## Flight Schedule

| API      | Test data |
| :----------- | :----------- |
| `On Demand Flight Status` | Cached data including most flights returned by `Flight Offers Search` |
| `Flight Delay Prediction` | No data restrictions in test |
| `Airport On-time Performance` | No data restrictions in test |

## Airport

| API      | Test data |
| :----------- | :----------- |
| `Airline Code Lookup` | No data restrictions in test |
| `Flight Check-in Links` | See list of [valid airlines](https://github.com/amadeus4dev/data-collection/blob/master/data/checkinlinks.md) |

## Airlines

| API      | Test data |
| :----------- | :----------- |
| `Airport & City Search` | Cities/airports in the United States, Spain, the United Kingdom, Germany and India |
| `Airport Nearest Relevant` | Cities/airports in the United States, Spain, the United Kingdom, Germany and India |
| `Airport Routes` | Cached data including most airlines |

## Hotel
| API          | Test data |
| :----------- | :----------- |
| `Hotel Search`| See list of [valid hotel chains](https://github.com/amadeus4dev/data-collection/blob/master/data/hotelchains.md). Content is provided directly by hotels and can change dynamically. Test with big cities like `LON` (London) or `NYC` (New-York).|
| `Hotel Booking` | Works with the response of `Hotel Search` |
| `Hotel Ratings` | See list of [valid hotels](https://github.com/amadeus4dev/data-collection/blob/master/data/hotelratings.md)|
| `Hotel Name Autocomplete` | Cached data including most hotels available through Amadeus|


## Destination experiences
| API      | Test data |
| ----------- | ----------- |
| `Points Of Interest` | See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md)|
| `Tours and Activities` | See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md)|


## Itinerary management 
| API      | Test data |
| ----------- | ----------- |
| `Trip Parser` | No data restrictions in test |
| `Trip Purpose Prediction` | No data restrictions in test |

## Market insights
| API      | Test data |
| ----------- | ----------- |
| `Points Of Interest` | See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md)|
| `Location Score` | See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md)|
| `Tours and Activities` | See list of [valid cities](https://github.com/amadeus4dev/data-collection/blob/master/data/pois.md)|
| `Flight Most Traveled Destinations` | See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/ti.md) |
| `Flight Busiest Traveling Period` | See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/ti.md)  |
| `Flight Most Booked Destinations` | See list of [origin and destination cities/airports](https://github.com/amadeus4dev/data-collection/blob/master/data/ti.md)  |