# Key concepts

This page provides help with the most common terminology used across Amadeus Self-service APIs.

### [COVID-19 and travel safety](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety){:target="\_blank"} 

| Term | Definition |
|----|----|
| Riskline  | Amadeus' travel restrictions data provider.    |

### [Air](https://developers.amadeus.com/self-service/category/air){:target="\_blank"}  and [Trip](https://developers.amadeus.com/self-service/category/trip){:target="\_blank"} 

| Term | Definition |
|----|----|
| Additional Baggage | Luggage beyond the standard allowance provided by an airline, subject to additional fees. |
| Aircraft Code         | [IATA aircraft code](http://www.flugzeuginfo.net/table_accodes_iata_en.php){:target="\_blank"} .              |
| Airline Code          | Airline code following IATA or ICAO standard - e.g. 1X; AF or ESY.  |  
| Airline consolidators | Wholesalers of air tickets that usually partner with airlines to get negotiated rates for air tickets, and then resell the air tickets to travel agents or consumers. |
| Amadeus Office ID | An identification number assigned to travel agencies to access Amadeus system and book reservations. |
| Amenities | Additional services or features offered to enhance the experience of the passengers, such as food, entertainment, Wi-Fi, extra legroom, baggage allowance, frequent flyer programs, and lounge access. They can vary depending on the class of service and the airline/train company. |
| Baggage allowance | The amount of luggage that a passenger is allowed to carry on a flight without additional charges. |
| Booking | The process of reserving a seat on a flight or a room in a hotel. |
| Cabin | The section of an aircraft or train where passengers sit during their trip. It is divided into different classes, such as first class, business class, and economy class, each one with different amenities and prices. |
| Commission | Fee paid to intermediaries for booking travel-related services, usually a percentage of the total cost. |
| Carrier Code          | 2 to 3-character IATA carrier code (IATA table codes).  |
| Country Code          | Country code following ISO 3166 Alpha-2 standard.         |
| Direct flight | A flight that goes from one destination to another without any stops in between. |
| Fare | The price of a ticket for a particular flight or travel itinerary. |
| Fare Rules | The terms and conditions that apply to a specific airline ticket or fare, including restrictions and information on refunds, cancellations, changes, baggage, seat assignments, upgrades, and frequent flyer programs. |
| Flight Order Id       | Unique identifier returned by the [Flight Create Orders API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-create-orders){:target="\_blank"} . |
| GDS (Global Distribution System) | A computerized system used by travel agents and airlines to search for and book flights, hotels, rental cars, and other travel-related services |
| IATA | [International Air Transport Association](https://www.iata.org){:target="\_blank"}  |
| IATA Code             | [Code](https://www.iata.org/en/publications/directories/code-search/){:target="\_blank"}  used by IATA to identify locations, airlines and aircraft. For example, the [Airport & City Search API](https://developers.amadeus.com/self-service/category/air/api-doc/airport-and-city-search){:target="\_blank"}  returns IATA codes for cities as the `iataCode` parameter.     |
| ICAO |  [International Civil Aviation Organization](https://www.icao.int/) |
| ISO8601 date format               | PnYnMnDTnHnMnS format, e.g. PT2H10M.      |
| Layover | A stopover in a destination en route to the final destination. |
| Location Id           | Amadeus-defined identifier that you can see in the search results when querying Self-Service APIs that retrieve information on geographical locations.                                                                            |
| Multi-stop flight | A flight itinerary that includes stops at multiple destinations before reaching the final destination. |
| Non-stop flight | A flight that goes from one destination to another without any stops in between. |
| Pricing | The process of determining the cost of a product or service, in the context of travel it refers to the cost of airline tickets, hotel rooms, rental cars. |
| PNR (Passenger Name Record) | A record in a computer reservation system that contains the details of a passenger's itinerary and contact information. |
| Round-trip | A trip that includes travel to a destination and then back to the original departure point. |
| Seatmap | A map or diagram of the seating layout in the cabin of an aircraft or train. It shows the location of different types of seats, such as exit row, bulkhead seat, aisle seat, window seat. It can be used to choose a seat or to see the availability of seats for a certain flight. |
| Ticketing | The process of issuing a travel document, typically a paper or electronic ticket, that confirms that a passenger has purchased a seat on a flight, train, bus, or other form of transportation. It can be refundable or non-refundable, one-way or round-trip, and open-jaw. |
| Travel Classes | Differentiation of service level and amenities offered to passengers on an aircraft or train, like first class, business class, economy class. |

### [Hotel](https://developers.amadeus.com/self-service/category/hotel){:target="\_blank"} 

| Term | Definition |
|----|----|
| Hotel Ids             | Amadeus Property Codes (8 chars). Comma-separated list of Amadeus Hotel Ids (max. 3). Amadeus Hotel Ids are found in the Hotel Search response (parameter name is `hotelId`).                                                     |

### [Destination content](https://developers.amadeus.com/self-service/category/destination-content){:target="\_blank"} 

| Term | Definition |
|----|----|
| Avuxi | Amadeus' data provider on locations popularity. |
| Activity Id           | [Tours and Activities  API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities/api-reference){:target="\_blank"}  returns a unique activity Id along with the activity name, short description, geolocation, customer rating, image, price and deep link to the provider page to complete the booking. |
| GeoSure | Amadeus's provider od data on locations crime rate, health and economic data, official travel alerts, local reporting and a variety of other sources.    |
| GeoSure GeoSafeScores | Algorithm that analyzes crime, health and economic data, official travel alerts, local reporting and a variety of other sources.    |
