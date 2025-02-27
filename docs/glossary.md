# Key concepts

This page provides help with the most common terminology used across Amadeus Self-service APIs.

### [Air](https://developers.amadeus.com/self-service/category/air){:target="\_blank"}  and [Trip](https://developers.amadeus.com/self-service/category/trip){:target="\_blank"} 

| Term | Definition |
|----|----|
| Additional Baggage | Luggage beyond the standard allowance provided by an airline, subject to additional fees. |
| Aircraft Code         | [IATA aircraft code](http://www.flugzeuginfo.net/table_accodes_iata_en.php){:target="\_blank"} .              |
| Airline Code          | Airline code following IATA or ICAO standard - e.g. 1X; AF or ESY.  |  
| Airline consolidators | Wholesalers of air tickets that usually partner with airlines to get negotiated rates for air tickets, and then resell the air tickets to travel agents or consumers. |
| Amadeus Office ID | An identification number assigned to travel agencies to access Amadeus system and book reservations. |
| Amenities | Additional services or features offered to enhance the experience of the passengers, such as food, entertainment, Wi-Fi, extra legroom, baggage allowance, frequent flyer programs, and lounge access. They can vary depending on the class of service and the airline/train company. |
| ARC Number | The ARC (Airlines Reporting Corporation) number is a U.S.-specific accreditation for travel agencies, functioning similarly to the IATA number. It is required for issuing airline tickets and earning commissions in the U.S. |
| Automatic Ticketing | Automatic ticketing streamlines flight booking by automating the issuance of tickets once a reservation meets predefined conditions. This eliminates manual intervention and ensures faster processing. Some consolidators require specific remarks in the booking request to enable automatic ticketing. |
| Baggage allowance | The amount of luggage that a passenger is allowed to carry on a flight without additional charges. |
| Booking | The process of reserving a seat on a flight or a room in a hotel. |
| Cabin | The section of an aircraft or train where passengers sit during their trip. It is divided into different classes, such as first class, business class, and economy class, each one with different amenities and prices. |
| Commission | Fee paid to intermediaries for booking travel-related services, usually a percentage of the total cost. |
| Carrier Code          | 2 to 3-character IATA carrier code (IATA table codes).  |
| Country Code          | Country code following ISO 3166 Alpha-2 standard.         |
| Delayed Ticketing | Delayed ticketing postpones ticket issuance until a specified time, giving travel agents more flexibility to collect payment from customers and adjust bookings before finalization. |
| Direct flight | A flight that goes from one destination to another without any stops in between. |
| E-Ticketing | E-ticketing refers to the electronic issuance of flight tickets, eliminating the need for physical paper tickets. While e-ticketing reduces costs and enhances efficiency, it still requires compliance with airline and consolidator policies. In the Self-Service framework, e-ticketing is not possible, and all ticket issuance must be done through a consolidator. |
| EOS Agreement (Extended Ownership Security) | An Extended Ownership Security (EOS) agreement governs data-sharing permissions between different office IDs. Before enabling flight booking in Self-Service, we establish an EOS agreement between you and your consolidator, allowing them to access a queue of all bookings you generate in production. |
| Fare | The price of a ticket for a particular flight or travel itinerary. |
| Fare Rules | The terms and conditions that apply to a specific airline ticket or fare, including restrictions and information on refunds, cancellations, changes, baggage, seat assignments, upgrades, and frequent flyer programs. |
| Flight Order Id       | Unique identifier returned by the [Flight Create Orders API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-create-orders){:target="\_blank"} . |
| Full Post-Ticketing Capabilities | Full post-ticketing capabilities include all modification functions, such as cancellations, changes, refunds, and voiding of tickets. These features are exclusively available through Amadeus Web Services (SOAP APIs). |
| Full-Service Carrier (FSC) | A full-service carrier (FSC) offers a comprehensive range of passenger services, including checked baggage, in-flight meals, and flexible booking policies, all included in the ticket price. |
| GDS (Global Distribution System) | A computerized system used by travel agents and airlines to search for and book flights, hotels, rental cars, and other travel-related services |
| IATA | [International Air Transport Association](https://www.iata.org){:target="\_blank"}  |
| IATA Code             | [Code](https://www.iata.org/en/publications/directories/code-search/){:target="\_blank"}  used by IATA to identify locations, airlines and aircraft. For example, the [Airport & City Search API](https://developers.amadeus.com/self-service/category/air/api-doc/airport-and-city-search){:target="\_blank"}  returns IATA codes for cities as the `iataCode` parameter.     |
| IATA Number | The IATA number is a globally recognized accreditation issued by IATA to certified travel agencies. This identifier is mandatory for agencies that wish to issue tickets or receive airline commissions. In the U.S., an ARC number is required instead. |
| ICAO |  [International Civil Aviation Organization](https://www.icao.int/){:target="\_blank"} |
| Instant Ticketing | Instant ticketing immediately issues flight tickets upon booking confirmation, ensuring rapid transaction completion. |
| Incentives | Incentives are commission-based bonuses awarded to travel agents based on booking volume. These rewards are not available through Self-Service APIs. |
| ISO8601 date format               | PnYnMnDTnHnMnS format, e.g. PT2H10M.      |
| Layover | A stopover in a destination en route to the final destination. |
| LCC (Low-Cost Carrier) | A low-cost carrier (LCC), also known as a budget airline, minimizes operating expenses to offer lower fares compared to full-service airlines. LCC content is not available through Self-Service APIs. |
| Light Ticketing | Light ticketing is a streamlined ticketing process used by low-cost airlines to simplify and accelerate booking for travel agents. This feature is exclusive to Enterprise APIs. |
| Limited Post-Ticketing Capabilities | Limited post-ticketing capabilities mean only partial modifications (such as cancellations before ticket issuance) are available. To perform full post-ticketing actions, you must use Amadeus Web Services (SOAP APIs). |
| Location Id           | Amadeus-defined identifier that you can see in the search results when querying Self-Service APIs that retrieve information on geographical locations.                                                                            |
| Manual Ticketing | Manual ticketing requires human intervention to verify, process, and issue tickets. This method is typically used when bookings lack automated processing parameters, such as incorrect office IDs or queue assignments. Manual ticketing is slower, less scalable, and may incur additional fees from consolidators. |
| Markups | A markup is an additional fee added by travel agents to the base fare of a flight ticket to cover operational costs and generate profit. Our APIs allow you to freely configure markup values on top of airline prices. |
| Multi-stop flight | A flight itinerary that includes stops at multiple destinations before reaching the final destination. |
| Negotiated Fare | Negotiated fares, also known as consolidator fares, are special discounted rates that airlines or fare consolidators make available to authorized travel agents. These fares are not publicly available and often include specific terms and conditions. Access to negotiated fares is restricted to the Enterprise APIs. |
| Non-stop flight | A flight that goes from one destination to another without any stops in between. |
| Pricing | The process of determining the cost of a product or service, in the context of travel it refers to the cost of airline tickets, hotel rooms, rental cars. |
| PNR (Passenger Name Record) | A record in a computer reservation system that contains the details of a passenger's itinerary and contact information. |
| Post-Ticketing Capabilities | Post-ticketing capabilities encompass all modifications, reissues, refunds, and cancellations after a ticket has been issued. In the Self-Service framework, post-ticketing actions are limited, and full modifications require access to a consolidator or the Enterprise APIs. |
| Public Fares | Public fares, also called published fares, are standard airline rates made available to all travel agents and consumers. These fares are universally accessible and subject to airline-defined pricing policies. By default, all our APIs return public fares. |
| Reissue | A reissue occurs when an existing ticket is replaced due to itinerary changes, fare adjustments, or passenger modifications. This functionality is not available through Self-Service APIs, but certain consolidators may offer reissue services for an additional fee. |
| Reservation vs. Ticket Issued | Booking a flight involves two distinct steps: **Reservation (Flight Order Creation):** Includes fare search, price confirmation, and PNR generation. At this stage, a seat is reserved but not ticketed. **Ticket Issuance:** The airline receives payment, and the reservation is converted into a confirmed ticket. In the Self-Service framework, ticket issuance requires a consolidator, even if you are a certified travel agent. |
| Remarks | Remarks in flight bookings refer to metadata or special instructions added to a Passenger Name Record (PNR). These remarks can trigger specific processing actions, such as fare validation or automatic ticket issuance. Some consolidators require custom remarks for workflow automation. |
| Round-trip | A trip that includes travel to a destination and then back to the original departure point. |
| Seatmap | A map or diagram of the seating layout in the cabin of an aircraft or train. It shows the location of different types of seats, such as exit row, bulkhead seat, aisle seat, window seat. It can be used to choose a seat or to see the availability of seats for a certain flight. |
| TDIS (Travel Industry Designator Service) | TDIS, managed by IATA, assigns a unique identifier to non-IATA travel sellers, facilitating industry recognition. However, a TDIS number alone does not grant the ability to issue tickets independently. |
| Ticketing | The process of issuing a travel document, typically a paper or electronic ticket, that confirms that a passenger has purchased a seat on a flight, train, bus, or other form of transportation. It can be refundable or non-refundable, one-way or round-trip, and open-jaw. |
| Travel Classes | Differentiation of service level and amenities offered to passengers on an aircraft or train, like first class, business class, economy class. |
| Queuing | Queuing involves placing a booking into a designated processing queue within a consolidator’s ticketing system. The consolidator assigns a queue number, which must be included in the booking request to route transactions appropriately. |

### [Hotel](https://developers.amadeus.com/self-service/category/hotel){:target="\_blank"} 

| Term | Definition |
|----|----|
| Hotel Ids             | Amadeus Property Codes (8 chars). Comma-separated list of Amadeus Hotel Ids (max. 3). Amadeus Hotel Ids are found in the Hotel Search response (parameter name is `hotelId`).                                                     |

### [Destination content](https://developers.amadeus.com/self-service/category/destination-content){:target="\_blank"} 

| Term | Definition |
|----|----|
| Avuxi | Amadeus' data provider on locations popularity. |
| Activity Id           | [Tours and Activities  API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/tours-and-activities/api-reference){:target="\_blank"}  returns a unique activity Id along with the activity name, short description, geolocation, customer rating, image, price and deep link to the provider page to complete the booking. |

### Technology

| Term | Definition |
|----|----|
| Metasearch Engine | A metasearch engine aggregates fare and availability data from multiple travel agencies, airlines, and booking platforms. Instead of handling direct transactions, metasearch engines operate on an affiliate model, redirecting users to providers and earning commissions based on referral volume. |
| NDC (New Distribution Capability) | New Distribution Capability (NDC) is an XML-based messaging standard developed by IATA to modernize airline content distribution. NDC enables airlines to offer richer, more dynamic fare structures, ancillary services, and personalized offers to travel agents. Access to NDC content is available only through the Enterprise framework. |
| Owner Office ID | The Owner Office ID is a unique identifier assigned to a travel agency, linking all bookings to its account. During implementation, we generate this ID for you. If working with a consolidator, your Owner Office ID is linked to their system, granting them access to bookings you generate. |
| Receiver Office ID | The Receiver Office ID designates the entity responsible for processing and ticketing a booking. When working with a consolidator, they provide the necessary Receiver Office ID, along with relevant queue or category numbers for ticket issuance. |
| REST APIs | REST (Representational State Transfer) APIs facilitate communication with web services using standard HTTP methods such as GET, POST, PUT, and DELETE. These APIs enable efficient data exchange, typically in lightweight formats like JSON, ensuring seamless integration with modern web applications. Our Self-Service catalog exclusively supports REST APIs. |
| Self-Service vs. Enterprise API | **Self-Service APIs:** Designed for independent developers and startups, offering quick integration via REST/JSON APIs with pay-as-you-go pricing. **Enterprise APIs:** Designed for large-scale travel businesses, offering the full Amadeus API catalog (REST/JSON and SOAP/XML), with dedicated account management, custom pricing, and expanded capabilities. |
| SOAP APIs | SOAP (Simple Object Access Protocol) APIs rely on XML for structured message exchange, adhering to strict standards for security, error handling, and stateful transactions. SOAP APIs provide robust reliability and built-in authentication mechanisms, making them ideal for enterprise-grade integrations. These APIs are available only through our Enterprise Web Services. |