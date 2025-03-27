---
title: Glossary
description: Explore our glossary of tourism and travel industry terms, featuring key concepts for working with Amadeus Self-Service APIs.
---

# Key concepts

This glossary offers guidance on the most common terms used in the tourism and travel industry, ranging from basic concepts to API technical vocabulary. It covers airlines and air travel definitions, as well as topics in hospitality, destination content, and some essential business aspects within the framework of Amadeus for Developers Self-Service offering.

### [Air](https://developers.amadeus.com/self-service/category/air){:target="\_blank"}  and [Trip](https://developers.amadeus.com/self-service/category/trip){:target="\_blank"} 

| Term | Definition |
|----|----|
| Additional Baggage | Luggage beyond the standard allowance provided by an airline, subject to additional fees. |
| Aircraft Code         | [IATA aircraft code](http://www.flugzeuginfo.net/table_accodes_iata_en.php){:target="\_blank"} .              |
| Airline Code          | Airline code following IATA or ICAO standard - e.g. 1X; AF or ESY.  |  
| Airline consolidators | Wholesalers of air tickets that usually partner with airlines to get negotiated rates for air tickets, and then resell the air tickets to travel agents or consumers. |
| Amadeus Office ID | An identification number assigned to travel agencies to access Amadeus system and book reservations. |
| Amenities | Additional services or features offered to enhance the experience of the passengers, such as food, entertainment, Wi-Fi, extra legroom, baggage allowance, frequent flyer programs, and lounge access. They can vary depending on the class of service and the airline/train company. |
| ARC Number | An ARC number is a unique identifier issued by the Airlines Reporting Corporation (ARC) to travel agencies in the USA. Similar to an IATA number, it is required to issue tickets and earn commissions. |
| Automatic Ticketing | Automatic ticketing in flight booking refers to the process of automating ticket issuance, eliminating the need for manual intervention. Some consolidators may require a specific remark in the booking request to enable this process. |
| Baggage allowance | The amount of luggage that a passenger is allowed to carry on a flight without additional charges. |
| Booking | The process of reserving a seat on a flight or a room in a hotel. |
| Cabin | The section of an aircraft or train where passengers sit during their trip. It is divided into different classes, such as first class, business class, and economy class, each one with different amenities and prices. |
| Commission | Fee paid to intermediaries for booking travel-related services, usually a percentage of the total cost. |
| Consolidator | Airline consolidators are wholesalers that partner with airlines to secure negotiated fares and resell tickets to travel agents or consumers. Many airline consolidators also act as host agencies for retail travel agencies or online travel startups that lack an International Air Transport Association (IATA) license to issue tickets. To issue tickets through a consolidator, travel startups must establish commercial agreements with them in their target markets. |
| Carrier Code          | 2 to 3-character IATA carrier code (IATA table codes).  |
| Country Code          | Country code following ISO 3166 Alpha-2 standard.         |
| Delayed Ticketing | Delayed ticketing allows travel agents to postpone ticket issuance until a specified time instead of issuing tickets immediately after booking. This provides agents with more flexibility to collect payments from travelers and the option to cancel without fees within the allowed timeframe. |
| Direct flight | A flight that goes from one destination to another without any stops in between. |
| E-ticketing | E-ticketing is the digital process of issuing flight tickets, allowing direct issuance and avoiding airline consolidator fees. However, a consolidator can still be contracted for post-ticketing services. In the Self-Service framework, E-ticketing is not available, and all ticket issuance must be done through a consolidator. |
| EOS Agreement | An Extended Ownership Security (EOS) agreement controls how data is shared between different office IDs. Before enabling flight booking in Self-Service, we establish an EOS agreement between you and your consolidator, granting them access to a queue of all bookings you generate in production. |
| Fare | The price of a ticket for a particular flight or travel itinerary. |
| Fare Rules | The terms and conditions that apply to a specific airline ticket or fare, including restrictions and information on refunds, cancellations, changes, baggage, seat assignments, upgrades, and frequent flyer programs. |
| Flight Order Id       | Unique identifier returned by the [Flight Create Orders API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-create-orders){:target="\_blank"} . |
| Full Post Ticketing Capabilities |  Full post-ticketing capabilities include all available post-ticketing actions, such as cancellations, changes, and voiding. These actions are only accessible through Amadeus Web Services (SOAP APIs). |
| Full Service Carrier | A full-service carrier (FSC) is an airline that provides a comprehensive range of services and amenities included in the ticket price. |
| GDS (Global Distribution System) | A computerized system used by travel agents and airlines to search for and book flights, hotels, rental cars, and other travel-related services |
| IATA | [International Air Transport Association](https://www.iata.org){:target="\_blank"}  |
| IATA Code             | [Code](https://www.iata.org/en/publications/directories/code-search/){:target="\_blank"}  used by IATA to identify locations, airlines and aircraft. For example, the [Airport & City Search API](https://developers.amadeus.com/self-service/category/air/api-doc/airport-and-city-search){:target="\_blank"}  returns IATA codes for cities as the `iataCode` parameter.     |
| ICAO |  [International Civil Aviation Organization](https://www.icao.int/){:target="\_blank"} |
| Incentives | Incentives are commission-based bonuses awarded to travel agents for reaching a specific booking volume. They are not available through our Self-Service APIs. |
| Instant Ticketing | Instant ticketing is the process of issuing flight tickets immediately after booking. |
| ISO8601 date format               | PnYnMnDTnHnMnS format, e.g. PT2H10M.      |
| Layover | A stopover in a destination en route to the final destination. |
| LCC | A low-cost carrier (LCC), also known as a budget airline, operates with a focus on minimizing costs to offer lower fares compared to traditional full-service carriers. LCC content is not available through the Self-Service APIs. |
| Limited Post Ticketing Capabilities | Limited post-ticketing capabilities mean that only partial modifications can be performed after ticket issuance. For full post-ticketing functionality, you must use Amadeus Web Services (SOAP APIs). |
| Light Ticketing | Light ticketing is a booking method used by low-cost airlines to simplify and streamline ticketing for travel agents. This option is available only through the Enterprise APIs. |
| Location Id           | Amadeus-defined identifier that you can see in the search results when querying Self-Service APIs that retrieve information on geographical locations.                                                                            |
| Markups | A markup is an additional amount added by travel agents to the base fare of a flight ticket to cover operational costs and generate profit. Our APIs allow you to freely set markups on top of airline prices. |
| Manual Ticketing | Manual ticketing requires human intervention to verify, process, and issue tickets. If a booking is not sent to the correct office ID or queue number, manual processing may be necessary. This method is less efficient, more time-consuming, and may incur additional fees from some consolidators. |
| Multi-stop flight | A flight itinerary that includes stops at multiple destinations before reaching the final destination. |
| Negotiated Fare | Negotiated fares, also known as consolidator fares, are special discounted rates that airlines or fare consolidators offer exclusively to authorized travel agents. Access to these fares is restricted to the Enterprise APIs. |
| NDC | NDC (New Distribution Capability) is a travel industry program developed by the International Air Transport Association (IATA) to modernize airline content distribution. It enables travel agents to access richer content and exclusive fares. NDC content is available only through the Enterprise framework. |
| Non-stop flight | A flight that goes from one destination to another without any stops in between. |
| Owner Office ID | The Owner Office ID is a unique identifier assigned to a travel agent to associate bookings with their account. It is created during the implementation process. If working with a consolidator, the Owner Office ID will be linked to them, allowing them access to the bookings you generate. |
| Pricing | The process of determining the cost of a product or service, in the context of travel it refers to the cost of airline tickets, hotel rooms, rental cars. |
| PNR (Passenger Name Record) | A record in a computer reservation system that contains the details of a passenger's itinerary and contact information. |
| Post Ticketing Capabilities | Post-ticketing capabilities include actions performed after a flight ticket has been issued, such as changes or cancellations. In the Self-Service framework, full post-ticketing modifications are not available. You can only cancel a flight using Flight Orders Management if the ticket has not yet been issued. |
| Public Fare | Public fares, also known as published fares, are standard airline rates available to all travel agents. By default, all our APIs return public fares. |
| Receiver Office ID | The Receiver Office ID is a unique identifier for the office responsible for processing and ticketing a booking. If working with a consolidator, they will provide the necessary Receiver Office ID along with any required queue or category numbers. |
| Reissue | Reissuance refers to the process of issuing a new ticket to replace an existing one due to itinerary changes. This service is not available through Self-Service APIs, but some consolidators may offer it for an additional fee. |
| Remarks | In flight booking, remarks are notes added to a Passenger Name Record (PNR) to provide additional booking details. They help ensure all relevant information is captured and communicated effectively. Some consolidators may require specific remarks in the booking request to trigger certain processes. |
| Reservation vs. Ticket Issued | Booking a flight involves two key steps: generating a flight order and issuing the ticket. The first step includes searching for a flight offer, confirming pricing, and generating a Passenger Name Record (PNR). At this stage, a seat is reserved in the airline's inventory, but the booking remains incomplete. Ticket issuance finalizes the booking when the airline receives payment. Until this happens, the reservation is not valid for travel. (For more details, refer to our guide (https://developers.amadeus.com/get-started/create-a-flight-booking-engine-651) on building a flight booking engine.) In the Self-Service framework, ticket issuance requires a consolidator, even if you are a certified travel agent. |
| Round-trip | A trip that includes travel to a destination and then back to the original departure point. |
| Seatmap | A map or diagram of the seating layout in the cabin of an aircraft or train. It shows the location of different types of seats, such as exit row, bulkhead seat, aisle seat, window seat. It can be used to choose a seat or to see the availability of seats for a certain flight. |
| Self-Service vs. Enterprise API | Amadeus for Developers offers two solutions tailored to different customer needs: Self-Service and Enterprise. The Self-Service offer is designed for independent developers and startups looking for quick and easy integration with Amadeus APIs. These REST/JSON APIs can be accessed and tested within minutes, with a flexible pay-as-you-go pricing model. The catalog includes categories such as Flights, Destination Experience, Car & Transfers, Market Insights, Hotels, and Itinerary Management. The Enterprise offer provides access to the full Amadeus API catalog (REST/JSON and SOAP/XML) and is tailored for companies with scaling needs and leading brands in the travel industry. Enterprise API customers receive dedicated support from account managers and benefit from a customized pricing scheme. Access to Enterprise APIs is granted under specific conditions. |
| TDIS | The Travel Industry Designator Service (TIDS) is a program by the International Air Transport Association (IATA) that assigns a unique identification code to travel agents and sales intermediaries. This code facilitates recognition and identification of travel sellers. However, a TIDS code alone does not grant the ability to issue bookings independently. |
| Ticketing | The process of issuing a travel document, typically a paper or electronic ticket, that confirms that a passenger has purchased a seat on a flight, train, bus, or other form of transportation. It can be refundable or non-refundable, one-way or round-trip, and open-jaw. |
| Travel Classes | Differentiation of service level and amenities offered to passengers on an aircraft or train, like first class, business class, economy class. |
| Queuing | Queuing involves assigning a booking to a specific queue within a consolidator’s ticketing system. The consolidator may provide a queue number that must be included in the booking request for proper processing. |

### [Hotel](https://developers.amadeus.com/self-service/category/hotel){:target="\_blank"} 

| Term | Definition |
|----|----|
| Hotel Ids             | Amadeus Property Codes (8 chars). Comma-separated list of Amadeus Hotel Ids (max. 3). Amadeus Hotel Ids are found in the Hotel Search response (parameter name is `hotelId`).                                                     |

### [Destination content](https://developers.amadeus.com/self-service/category/destination-content){:target="\_blank"} 

| Term | Definition |
|----|----|
| Activity Id           | [Tours and Activities  API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities/api-reference){:target="\_blank"}  returns a unique activity Id along with the activity name, short description, geolocation, customer rating, image, price and deep link to the provider page to complete the booking. |
| Metasearch Engine | Metasearch engines compile fare and availability data from multiple travel agencies and airlines. They operate on an affiliate model, earning commissions based on the referral volume they generate for specific providers. |

### API technology

| Term | Definition |
|----|----|
| REST APIs | REST (Representational State Transfer) APIs facilitate communication with web services using standard HTTP methods such as GET and POST. These APIs enable efficient data exchange, typically in lightweight formats like JSON. Our Self-Service catalog exclusively supports REST APIs. |
| SOAP APIs | SOAP (Simple Object Access Protocol) APIs use XML for structured message exchange, adhering to strict protocols that ensure security, reliability, and interoperability. These APIs provide built-in authentication and error-handling mechanisms. SOAP APIs are available exclusively through our Enterprise Web Services. |
