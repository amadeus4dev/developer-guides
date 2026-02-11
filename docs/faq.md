---
title: API FAQ - Q&A
---

# Frequently Asked Questions

This page provides help with the most common questions about Amadeus Self-service APIs.

## Account registration

### How do I change my password?

To change your password, sign in to the [Developers portal](https://developers.amadeus.com/){:target="\_blank"} and click on **My Account** in the top right corner of the screen. You'll find the option to change your password at the bottom of the page. Please remember that we never send your password in any correspondence.

### I registered but never received a confirmation email? What should I do?

If you haven't received a confirmation mail, it is often because the email address was entered incorrectly. Please sign in to the [Developers portal](https://developers.amadeus.com/){:target="\_blank"} and visit the **My Account** section to confirm that the email address used to create the account is correct. If so, please check your spam folder for an email from noreply@amadeus.com.

## Business enquiries

### How can I monetise my application?

You are free to create your own business models around our APIs, such as charging users to use our APIs in their apps or adopting a subscription-based model. However, we do not give any commission or other types of incentives for the Self-Service API. The latter is only possible in the Enterprise framework. If you're offering flight booking services, you can generate revenue for your apps by applying a markup on flight offers.

### I would like to partner up with Amadeus

You can partner with Amadeus through the [Amadeus Partner Network](https://amadeus.com/en/partners). This includes different types of partnerships, with the possibility to get access to technology or to connect to Amadeus' global network of customers and partners.


## Self-Service vs Enterprise


### What is the difference between Self-Service and Enterprise APIs?

Amadeus for Developers provides two different offers, each of which meets distinct customer needs: Self-Service and Enterprise. 

The **Self-Service** offer targets independent developers and start-ups that wish to connect to Amadeus APIs in a quick and easy manner. You can access and start testing these new REST/JSON APIs in less than 3 minutes, and get quick access to production data with a flexible pay-as-you-go pricing model. Please note that the catalog includes some selected APIs only, although we will be constantly releasing new APIs.
 
The **Enterprise** offer provides access to the full Amadeus APIs catalog, tailored to companies with scaling needs as well as the leading brands in the travel industry. Customers of Enterprise APIs receive dedicated support from their account managers and enjoy a customized pricing scheme to meet their needs. Please note that access to Enterprise APIs is only granted on a request basis, and some special requirements may apply. Our Enterprise commercial teams will be happy to guide you through the process.

### Can you help us with moving our application to Enterprise? 
Unfortunately, the self-service team will not be able to help you move to Enterprise. Enterprise APIs are managed by different teams based on your business area. You will need to find the contact form of your specific business area in the [Amadeus contact us form](https://amadeus.com/en/contact). After you submit the form, someone from the right business area will reach out to you with the next steps. 

### Can I use APIs from both Self-Service and Enterprise?

Yes, you can use APIs from both catalogs, but please keep in mind that the requirements and conditions of each offer are very different. Please check our [Get Started guide](https://developers.amadeus.com/get-started/get-started-with-amadeus-apis-334){:target="\_blank"} for more information.

### How can I contact Enterprise?

To contact the Enterprise team, please visit the [Amadeus contact us form](https://amadeus.com/en/contact), select your specific business area (example: Airlines, Airports, Travel Sellers, etc.), and fill the form. Choosing the right business area helps the correct team to reach out to you and ensures a fast implementation process. Please keep in mind that the access to Enterprise requires an implementation fee as well as monthly fees.

### How much do I need to pay to access Enterprise APIs?

The access to Enterprise APIs is subject to certain requirements depending on your market and the functionalities you want to access. It is usually reserved for experienced companies with the need to scale. Before we can disclose the pricing details you will need to sign an NDA. 

## Self-Service APIs general

### What is an alternative to Amadeus for Developers self-service APIs? 

Unfortunately, we currently do not have internal alternatives to Amadeus for Developers self-service APIs.

### Is there a test environment to try the Self-Service APIs?

Yes! You can try Self-Service APIs in our test environment and enjoy a free monthly request quota to build and test your app. If you exceed this free request quota in the test environment, you'll receive a 429 error code in JSON and not be able to call the APIs.

If you need to increase the number of monthly API calls, please consider moving your application to production. It's a quick and easy process and you will keep the free request quota you enjoyed in test. Once you reach your threshold in production, you will simply pay for the additional API calls you make.

### How do I access the Self-Service APIs documentation?

Check our [Amadeus for Developers docs portal](./index.md) for links to interactive reference documentation for each API and helpful guides covering topics such as authorization, pagination and common errors. On the [Amadeus for Developers GitHub page](https://github.com/amadeus4dev/){:target="\_blank"}, you can also find code samples and SDKs.

### Do you provide SDKs?

Yes! On the [Amadeus for Developers GitHub page](https://github.com/amadeus4dev/){:target="\_blank"} you can find open-source SDKs in various languages. Alternatively, you can use [OpenAPI Generator](./developer-tools/openapi-generator.md) to create an SDK from our [OpenAPI files](https://github.com/amadeus4dev/amadeus-open-api-specification){:target="\_blank"}.

### Where can I see code examples for Amadeus Self-Service APIs?

Code examples for all Amadeus Self-Service APIs are available in our [GitHub](https://github.com/amadeus4dev/amadeus-code-examples){:target="\_blank"}.

### How do I make my first Self-Service API call?

On the [Get Started with Self-Service APIs](https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335){:target="\_blank"} page you can find information on creating an account, getting your API key and making your first call.

### How do I move Self-Service APIs from test to production?

To launch your application to production, please follow the steps described in our [Moving to production](./API-Keys/moving-to-production.md){:target="\_blank"} guide.

You will be asked to sign a contract and provide billing information before receiving your new API key. When you move to production, you will maintain the same free monthly request quota you enjoyed in test. When you reach your monthly threshold, you will be billed for the additional API calls you make at the rates shown on our [Pricing page](https://developers.amadeus.com/pricing){:target="\_blank"}.

### How do I delete my application built using Self-Service APIs?

To delete an application, visit the **My apps** section of your **My Self-Service Workspace**. Remember that deleted apps cannot be recovered.

### Will you include more APIs in the Self-Service catalog?

We are constantly expanding our Self-Service API catalog with new APIs from all travel segments such as flights, hotels, cars or destination content. If you have any specific requests or feedback regarding APIs that you would like to add to your catalog, please contact us. We'd love to hear from you!

### What are the terms of service for Amadeus Self-Service APIs?

To find out more about our terms and conditions for the test environment, please visit our [Terms and Conditions page](https://developers.amadeus.com/legal/terms-of-use){:target="\_blank"}.

If you are already in production, you should have received an email with the legal terms regulating API usage in the production environment. If you have not received this information, please [contact us](https://developers.amadeus.com/support/contact-us-self-service){:target="\_blank"}.

### I am not a travel agent and have no experience in the travel industry, can I still use the Self-Service APIs?

Our Self-Service offer is designed for newcomers to Amadeus, there are no prerequisites. Any developer who wishes to connect to Amadeus travel data can do so in a quick and easy way via our Self-Service offer.  For more details, please check our [Get Started guide](https://developers.amadeus.com/get-started/get-started-with-amadeus-apis-334){:target="\_blank"}.

### Are there any limitations to the Self-Service API dataset?

We do not return data on American Airlines, Delta, British Airways and Low cost carriers. For other arlines we only return published rates. We do not return negotiated rates or any other special rates. The Flight Offers Search only returns the bag allowance information for one passenger type code. Airlines blacklisted in the EU are not returned using the Flight Offers Search GET, e.g., Iraqi Airways. There is a possibility to override this with the POST method.

### How can I do group booking?

Our Self-Service APIs allow you to book up to 9 passengers on the same PNR number. For more passengers you will need to create a new booking.

### What is it returning different prices with the Self-Service APIs and other Amadeus solutions?

The Self-Service catalog only returns published GDS rates. If you have access to special rates through another solution, they will not be available through our Self-Service APIs.

### Do I need an IATA license?

IATA or ARC licenses (depending on your market) are mandatory if you want to issue flight tickets, but this option is only available in our Enterprise framework. In Self-Service you will need to work with an airline consolidator to issue flight tickets, therefore no IATA or ARC license is needed.

## API keys

### What is an API key?

An API key is a unique reference number which identifies your application to Amadeus. The API key is part of the authorization process and must be sent with each API request. If you have multiple applications using Amadeus APIs, each application must have its own API key. For more details, check our [Authorization guide](./API-Keys/authorization.md).

Your API keys are also used to track usage. To avoid unwanted charges, please do no share or post them in public repositories. For more information, see this [article on best practices for secure API key storage](https://developers.amadeus.com/blog/best-practices-api-key-storage){:target="\_blank"}.

### How do I get my Self-Service API key?

To get a Self-Service API key, simply create an account in the [Amadeus for Developers portal](https://developers.amadeus.com/){:target="\_blank"}. Next, visit the **My Self-Service Workspace** area and create your first application. An API key will be generated automatically. Remember, your API key is private and should not be shared publicly.

### Why is my Self-Service API key not working?

If your API key is not working, please verify that it is the same exact key that was provided in the **My Self-Service Workspace**.

Please keep in mind that we automatically revoke API keys that are publicly searchable. This is done to protect users against unwanted usage bills. As a general rule, you should not put your API keys in the source code you commit to GitHub or other public repositories. Instead, you should store your keys as environment variables rather than hard-coding them in your script. For more information, see this [article on best practices for secure API key storage](https://developers.amadeus.com/blog/best-practices-api-key-storage){:target="\_blank"}.

### How long is my Self-Service access token valid for?

The access token is valid for 1800 seconds (30mins). If you get an authentication fail, please request a new token.

### Can I use my API key in a public repository?

Storing your API keys or any other sensitive information in a public repository must be avoided at all costs to prevent malicious access to your APIs, which could result in unwanted usage bills.

In order to protect our users, we automatically revoke API keys that are publicly searchable. We recommend that you store your keys as environment variables rather than hard-coding them in your script. For more information, see this [article on best practices for secure API key storage](https://developers.amadeus.com/blog/best-practices-api-key-storage){:target="\_blank"}.

### Why has my API key been revoked?

We automatically revoke publicly searchable API keys to prevent unwanted charges to your account. To prevent this from happening, you should read your API key from a system environment variable rather than putting it in the source code you commit to GitHub. If you need to get a new API key, please go to **My Self-Service Workspace**.

## Billing

### How is billing calculated for Self-Service APIs?

It is free to test and prototype with Self-Service APIs and you will enjoy a free monthly request quota in both the test and production environments.

When you exceed your free request quota in production, you will be billed for the additional calls you make at the rates indicated on our [Pricing page](https://developers.amadeus.com/pricing){:target="\_blank"}, with no additional fees. Please note that prices vary from one API to another.

You can check your monthly usage and select your preferred payment method (credit card or bank transfer) in your Self-Service Workspace.

### How do I request a refund of my Self-Service usage bill?

If you're a Self-Service API user, please send your refund requests via the [contact us](https://developers.amadeus.com/support/contact-us-self-service){:target="\_blank"} and our team will carefully analyse them. You will be notified if your refund is approved and be reimbursed within the following days (please note that refund processing times may vary depending on your bank).

### Where can I find my invoices?

You will receive your invoices on a monthly basis from [data.distribution@amadeus.com](mailto:data.distribution@amadeus.com). Please note that once opened, you will not be able to open the same invoice again.

## Test collection

### Is there a limit to the calls I can make to Self-Service APIs in the test environment?

Yes, each Self-Service API in test includes a limited number of free monthly calls. This free request quota varies from one API to another and it applies to the sum of all your applications. If you exceed the quota in test, you'll receive a 429 error code in JSON.

To see how many free requests remain, log into your account and check your API usage & quota in your Workspace area. Please keep in mind that it can take up to 12 minutes for data to appear.

Your free request quota should be sufficient for testing purposes. If you need to increase your number of monthly API calls, please consider moving your application to production. The process is quick and simple and you will keep the free request quotas you enjoyed in test.

### What should I do if I'm about to reach my Self-Service free request quota limit?

The test environment is designed for testing purposes. Every month, you'll receive a free request quota to build and test your app. If you need to increase your number of monthly API calls, please move your application to production. The process is quick and easy, and you will keep the free monthly request quota you enjoyed in test. Once you exceed your quota in production, you will be billed for the additional API calls you make.

### Is there a limit to the calls I can make to Self-Service APIs in the production environment?

There is no consumption limit in production, as long as there are no outstanding usage bills and your account's payment method is up to date.

### Why do I get a 429 error in JSON if I have some free calls left?

After making API call, it can take up to 12 minutes for the data to appear on your usage & quota page. If you are nearing your limit free request quota limit and receive a 429 error, it's likely that you have run out of free calls.

To keep using the APIs, you can either move your app to production or wait until the free request quota is reset at the beginning of each month.  


### Why do I get an error code 429 when I call a Self-Service API?

This error indicates you carried out too many requests and went over your limit of free calls for this API. 

If you wish to keep using the APIs, you can either move your app to production and enter your preferred payment method or alternatively wait until the following month to get more free calls.

### Is the data returned in the Self-Service test environment accurate?

The information returned in test environment is from [limited data collections](./test-data.md){:target="\_blank"}. This is done as a security measure to protect our data and our customers. When you move to production, you will get access to complete and live data.

## Flight Inspiration Search

### Why didn't I get any results for Flight Inspiration Search?

This API works with cached data in the test environment and not all airports are cached. You can find a list of airports included in the cached data in our guides section. When combining these searches with the Airport Nearest Relevant API, it is better to search using the city code rather than the airport code.

### Why are some origin and destination pairings not returning results?

The Flight Inspiration Search and Flight Cheapest Date Search APIs are built on top of a pre-computed cache of selected origin-destination pairs. This is why, even in production, you cannot find all possible origin-destination pairs. If you need to access more results, you need to use the live Flight Offers Search API.

## Airport routes

### The API returns an airport that has been permanently closed

This is the expected behavior. The IATA code in the response corresponds to the Destination City IATA code but not the Airport Code.

## Airport Nearest Relevant API

### Why isn't the Airport Nearest Relevant API returning a specific airport near me?

This may be because an airport is near a national boarder. If so, please check the API parameters for location. Also, please keep in mind that our Airport Nearest Relevant API excludes private and military airports.

## Flight Offers Search

### Why are the prices returned more expensive than on other websites?

The API only returns published rates, which are the standard rates given by airlines. Amadeus then redistributes them to the travel agencies around the world. However, big players in the industry can negotiate their rates directly with the airlines, which can help them be more competitive or maximise returns made form selling tickets.


### What does nonHomogeneous mean in the API response?

PNRs are designed to be homogeneous, meaning that one PNR contains the same type of content (e.g., flights only) and number of passengers. However, nowadays, there can be a mix of different content, such as air and hotel. When nonHomogeneous is true, it means that a single PNR can contain records that would initially be split across different PNRs.

### Why the dataWindow parameter returns less results with I3D or I2D?

This is normal behaviour. Flight Offers Search returns the cheapest option for all flights. When you request an extra delay in the search (+/- xDays), Flight Offers Search takes a matching flight (i.e., AF111), checks all possible days, and returns only the cheapest offers. Using more filters does not increase the number of results. It increases the range of data the API uses to find the cheapest offers to return. Having fewer options between 'I3D' and 'I2D' is normal. With 'I2D,' you most likely compare a working week with very regular flights, and with 'ID3,' you always include weekend flights on top, so there are more options.

### How can I add a loyalty program to a booking?

Flight Offers Price and SeatMap Display both accept frequent flyer information, so end-users can benefit from their loyalty program. When adding frequent flyer information, please remember that each airline policy is different, and some require additional information like passenger name, email, or phone number to validate the account. If validation fails, your user won’t receive their loyalty program advantages.

### POST and GET do not return the same results

By default the GET method does not return airlines blacklisted in Europe. However, users can override this using the POST method.

### How do I add bags to a check in bag for flight reservation? 

You can add a checked-in bag to a flight booking using the ‘’additionalServices’’ element in the flight offer when calling Flight Offers Price. For more details, please check our guide on [adding baggage with Amadeus flight booking APIs](https://developers.amadeus.com/blog/add-baggage-amadeus-flight-booking-api). 

### How do I add bags to a cabin bag for flight reservation? 

Our APIs do not return cabin bag information in the responses, and it is not possible to add an additional cabin bag to a booking. 

### Can I display the price of flights using air miles/loyalty points and book a flight?
Our Self-Service APIs do not let you display the prices in loyalty points or book a flight using loyalty points.

### Why are some taxes refundable?
A refundable tax is a type of tax or fee that is collected when you purchase an airline ticket but can be refunded to the passenger under certain circumstances, these conditions will vary depending on the specific country and airline. 

### How can I integrate flight booking?
You can integrate flight booking using our Self-Service APIs. Production access is subject to certain requirements, including being registered in one of our approved markets, meeting your local legal requirements, and working with an airline consolidator to issue tickets.

The booking flow involves the following APIs:
- [Flight Offers Search](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search?utm_source=support&utm_medium=email): to search for the best bookable flight offers.
- [Flight Offers Price](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-price?utm_source=support&utm_medium=email): confirms the latest price and availability of a specific chosen flight.
- [Flight Create Orders](https://developers.amadeus.com/self-service/category/air/api-doc/flight-create-orders): to book flights and ancillary services proposed by the airline.
- [Flight Orders Management](https://developers.amadeus.com/self-service/category/flights/api-doc/flight-order-management): to manage and consult your bookings. This API also includes an endpoint to cancel the reservation.

Once you generate a booking in production, your consolidator will receive it in their back office and issue the tickets from there. After the ticket has been issued, you will need to contact your consolidator for any modifications to the booking or refund requests. 
For more information on flight booking please check our guide on [how to build a flight booking engine](https://developers.amadeus.com/get-started/create-a-flight-booking-engine-651).

### Do you provide Co2 emission?

**New update from January 2024:** 
You can return Co2 emission in the [Flight Offers Price API](https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-price) response when you are validating the price and available, or after the booking step in the [Flight Create Orders API](https://developers.amadeus.com/self-service/category/flights/api-doc/flight-create-orders) response.

### What are fare rules?

Fare rules are a set of conditions that determine the price of an air ticket for each seat class. They also define whether a ticket is refundable/nonrefundable or whether additional charges are applicable. You can return those with our Self-Service APIs using Flight Offers Price and adding ''include=detailed-fare-rules'' in your base URL:

`https://test.api.amadeus.com/v1/shopping/flight-offers/pricing?include=detailed-fare-rules`

Please keep in mind that this will return the fare rules in a raw format. If you want a structured version of these, you will need to use our Enterprise APIs.

### Do you return airline logos?

We do not return airline logos in our Self-Service catalog.


## Flight Offers Price

### How can we get information on refundable flights?

To get the refund policy for a specific flight, you will need to use the [Flight Offers Price API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-price), with the parameter `include` set to `detailed-fare-rules` at the endpoint of the URL as follows: https://api.amadeus.com/v1/shopping/flight-offers/pricing?include=detailed-fare-rules 

## Flight Price Analysis

### Why do some origin and destination pairings not return any results?

Not all possible routes are supported by the API even in production. The reason is that the machine learning model filters out all the routes with an error rate below 15% MAPE (Mean absolute percentage error). For more insights on how the model works, please refer to [this blog post](https://developers.amadeus.com/blog/flight-price-analysis-model-machine-learning).


## Flight Delay Prediction

### Why do I get the INFERENCE error?

This means the requested origin/city pairing was not included in our training data. So, we have no previous information on whether that flight is normally delayed or not.


## Flight Cheapest Date Search

### Why are some origin and destination pairings not returning results?

The Flight Inspiration Search & Flight Cheapest Date Search APIs are built on top of a pre-computed cache of selected origin-destination pairs. This is why, even in production, you cannot find all possible origin-destination pairs. To access more results, you need to use the live Flight Offers Search API.

### Why do I get the 500 error message?

The 500 error message `'SYSTEM ERROR HAS OCCURRED', 'detail': 'Primitive Timeout'`  is caused by the search being too generic, and the API taking too much time to fetch the data. Unfortunately, there is nothing we can do about this for now. The solution will be to filter the search down using more parameters.

## Flight Availabilities Search

### Why are some travel classes not returned in the search results?

Travel class is not standardized, and some airlines may use different letters for the same travel class. For example, All Nippon Airways does not use 'Class: I'. By default, this API excludes closed booking classes, departed flights, and cancelled flights. To return closed content, you can use the parameter `includeClosedContent` and set it to `true`.


## Branded Fares Upsell

### Why do additional services change between segments in an Itinerary?

Additional services can change between segments in an itinerary. For example, a passenger could end up with a checked bag which is allowed in one of the segments of an itinerary but not on the others (because of its weight or because it's not included at all). This is normal behavior for this API. The packages are created at the flight level. This means that even an itinerary made up of two flights from the same airline could have different upsell options. Additionally, not every airline will have the option to upsell.

## SeatMap Display

### Is there any way to request a seat map by cabin instead of having to specify a booking class code?

There is no way to specify a cabin, but you will get this information in the response of Flight Offers Search. This will allow you to filter based on that.

### Why do I get the error code 4926?

Returning the error: `'warnings': [{'code': 4926, 'title': 'INVALID DATA RECEIVED', 'detail': 'Invalid departure/Arrival city pair'}]` is caused by airlines choosing not to display the seat map of some flights, so the API returns a warning with the information we have.

### Seatmap not available as flight operated by another carrier

This error is generated when the specified flight in the query is a codeshare, and no agreement exists with the operating flight. Unfortunately, the only way to mitigate this in the future is to avoid calling the SeatMap Display API with this specific operating carrier.


### Why am I unable to retrieve seatmap data?

This error message means that the airline never filled in a seat map for the specific flight. It's usually not generic to all flights of the airline. Unfortunately, there is no solution for this one.

### What does AVAILABLE, BLOCKED, and OCCUPIED mean in the response? 
- `AVAILABLE`: the seat is not occupied and is available to book. 
- `BLOCKED`: the seat is not occupied but isn’t available to book for the user. This is usually due to the passenger type (e.g., children may not sit in exit rows), or their fare class (e.g., some seats may be reserved for travelers in higher classes).
- `OCCUPIED`: the seat is occupied and unavailable to book.


## Flight Create Orders API

### How are tickets issued for flights booked with Flight Create Orders in Self-Service?

For Self-Service users, ticketing must be done via airline consolidator. Airline consolidators are essentially air ticket wholesalers that have special arrangements with airlines and, among other functions, can serve as host agencies for travel agents without the necessary IATA/ARC certifications necessary to issue tickets.

To access Flight Create Orders in production, you must have a contract signed with a consolidator for ticket issuance. If you need help finding a consolidator, please contact our support team to put in touch with the best consolidator in your region.

### How can I retrieve booking made with Flight Create Orders in Self-Service?

You can consult booking made through Flight Create Orders using the Flight Order Management API. This API works using a unique identifier(the flight offer id) that is returned by the Flight Create Orders API.

### Does Amadeus pay a commission for flights booked with Flight Create Orders in Self-Service?

Generally, Amadeus does not offer booking commissions for Self-Service users.


### Why do I get the INVALID DATA RECEIVED error?

Getting the error message: `INVALID DATA RECEIVED`. Some of the data in the query is false. It could be that the fare does not match the traveling class, or that the flight number is incorrect. This is common to all our APIs. It comes from the API backend validating your query. All the fields of the price reply should be exactly the same as the one from the book query to be sure there is a problem.

### Why do I get the SEGMENT SELL FAILURE error?

Getting the error message: `SEGMENT SELL FAILURE` means that you were not able to book the seat in the airline inventory. Most of the time, it comes from the flight being full. This often happens in the test environment, as you can perform many bookings without restrictions (no real payment). But the inventory is a copy of the real one, so if you book many seats, the inventory can get empty and you won't be able to book anymore. The good practice here is to use Flight Offers Price right before booking and avoid last-minute flights that tend to quickly get full.

### How does payment work when I book a flight?

There are two things to consider regarding payments for flight booking:

1. The payment between you (the app owner) and your customers (for the services provided + the price of the flight ticket). You decide how to collect this payment. It is not included in the API. A third-party payment gateway, like Stripe for example, will be the easiest solution for this.

2. The payment between you and the consolidator (to be able to pay the airline and issue the flight ticket). This will be done between you and your consolidator of choice and is to be agreed upon with the consolidator.

### How can I cancel a flight?

Cancellation is possible with the Flight Orders Management API as long as the booking has not been issued by the consolidator yet. If the booking has been issued, it will need to be canceled by the consolidator directly.

### How to make the airline consolidator wait before issuing a ticket?

You can delay ticketing using the `ticketingAgreement` parameter in Flight Create Orders. For this, you can use the following options:

* `DELAY_TO_QUEUE`: this allows you to queue the reservation for the desired date if the traveller does not make the payment.
* `DELAY_TO_CANCEL`: if the traveler does not make the payment, the reservation for the desired date will be cancelled.

The queuing and cancellation take place based on the local date and time. If no specific time is mentioned, the reservation is queued or cancelled at 00:00.

### Can I markup prices of flight tickets sold?

Yes you are free to add a markup on any flight ticket. This must be done through your own payment gateway.

### How can I modify my booking once the ticket is issued?
This is not possible through our Self-Service APIs. Once a ticket has been issued you will need to contact the consolidator for any changes, and this will be subject to a fee. 
In case the ticket has not been issued. You will need to delete the booking and rebook with the modifications.


## Hotel Search & Book

### What are guarantee, deposit and prepay?

* **Guarantee:** The hotel will save credit card information during booking but will not make any charges to the account. In the case of a no-show or out-of-policy cancellation, the hotel may charge penalties to the card.
* **Deposit:** At the time of booking or on a given deadline, the hotel will charge the guest a percentage of the total amount of the reservation. The remaining amount is paid by the traveler directly at the hotel.
* **Prepay:** The traveler must pay the total amount of the reservation during booking.

### What is the total price?

The price total refers to the total price to be paid for the full stay. The variations, on the other hand, represent the average price per night. In the example you highlighted, a guest will need to pay €548.56 for the three nights, and the average price for the room is €182.85 per night (€548.55 overall). For more details, you can refer to our data model found in the OpenAPI specification of the Hotel Search API.

### What is the latest possible date for check-in?

The maximum date for the 'checkInDate' parameter is 359 days from today. Anything beyond this will return the error message 'MAXIMUM ADVANCE DAYS BOOKING EXCEEDED'.


### How to search a hotel by location

Regarding the input for a specific location in a hotel search, you have the following options:

* Since the commissioning of Hotel Search v3, we can no longer search hotels by IATA codes. In order to search by location you will need to use the third endpoint of Hotel List `/reference-data/locations/hotels/by-geocode`, which allows you to search using a latitude & longitude. The Hotel List API returns `hotelIds` based on the specific search coordinates. You will then need to use this `hotelId` in the third endpoint of the Hotel Search API.

* Alternatively, you can use the Google API to retrieve the geo location of a specific location and use the Hotel Search by geo location.

### What type of payments are supported?

The current version of the Hotel Booking API only supports credit card payments. The Hotel Search API returns the payment policy of each hotel under `acceptedPayments` in the policies section.

### Can I markup the room prices?

It is not possible to markup the prices of the hotel rooms with the current version of the Hotel Booking API. The reason is that the content we offer today in our Hotel Search/Book API is post-paid, meaning the traveler will pay directly at the hotel. The Hotel Booking API is here to enable making a reservation but not to pay directly. We are working on adding more hotel offers, especially offers that will be pre-paid, meaning you will be able to charge the travelers directly and add a markup. However, you still need to add a credit card while booking in case of cancellations or no-shows.

### Payment providers and gateways

The Hotel Booking API works by using the guest's payment information and sending it to a chosen hotel for the reservation. You can use a payment gateway in your app, but this will not change the way the API works. The hotels will never collect any money from you. Instead, the payments are always done at the time of checkout between the guest and the hotel. During the booking process, Amadeus passes the payment and guest information to the hotel but does not validate information, so it doesn’t play the role of payment gateway. Be sure to validate the payment and guest information as invalid information may result in the reservation being canceled. As soon as your application stores, transmits, or processes cardholder information, you will need to comply with the PCI Data Security Standard (PCI DSS). For more information, visit the [PCI Security Council website](https://www.pcisecuritystandards.org/merchants/).

### Why do I get 500 status code?

The process of booking a hotel in the test environment involves sending your request to each hotel provider, and each provider has its own environment and rules. Due to these differences, there may be connectivity issues with the providers that can result in a timeout. Additionally, if many requests are sent to a particular hotel, they may choose to block them. If you provide us with a timestamp and details of another API request that has failed, including the hotel in question, we can search our logs to find more information. However, it is likely that the issue is one of the aforementioned cases.

### How can I see Amadeus API coverage for a hotel chain?

You can find the list of supported hotel chains in [our data collection](https://github.com/amadeus4dev/data-collection/blob/master/data/hotelchains.md).

### What is considered a query?

When you make an initial call to the Hotel Search API with a cityCode parameter, it is considered one query that returns 10 hotels. If you then click on each hotel to view room details and other information, you are making additional API calls using the second endpoint of the Hotel Search. Each hotel that you click on generates another API call. For example, if you click on 5 hotels to see room details, you will be making a total of 5 additional queries.

### Do I need any legal documents to make a booking?

No, there are no legal documents required. However, you will need to comply with any local legal requirements for your market.

### What are the room type codes?

The room type code is a 3-character identifier that indicates the room type category, the number of beds, and the bed type. However, some hotels may not follow this pattern and instead use custom types. In such cases, the room description is the best way to understand the room type.

### How do I cancel a hotel booking?

There is no way to cancel hotel bookings through the APIs. This needs to be done offline by ringing the hotels. 

### Why is Hotel Search returning empty responses ‘{"data": []}’?
You are returning this because this specific hotel is closed or unavailable for this specific date. You can either try to change the check-in date or use the ''includeClosed'' parameter set to ''true''. The latter will return further information on the hotel, but you will not be able to book it.

### Do you return hotel images?
Hotel images are not available through our Self-Service catalog.

## Airline consolidators

### What is an airline consolidator?

Airlines consolidators are wholesalers of air tickets. They usually partner with airlines to get negotiated rates for air tickets, and then resell the air tickets to travel agents or consumers.

Many airlines consolidators act as host agencies for retail travel agencies or online travel agency startups that do not have the license from the International Air Transport Association (IATA) to issue air tickets. To issue air tickets via airline consolidators, the travel startups have to settle commercial agreements with the airline consolidators in the markets in which they want to operate. 

It is to be noted that not all the airline consolidators provide post-ticketing services such as monitoring and notifying travel agencies about schedule changes and flight cancellations. This is something that startups have to check with their potential airline consolidators. 


### How are payments handled with my consolidator?

Different airline consolidators handle payments in different ways. In some cases, you will be asked to make an initial deposit to cover future ticketing charges. In other cases, you will be billed monthly for the services consumed. Please contact our support team or refer to your airline consolidator contract for more details.
 
### How do I handle cancellations, changes and post-booking services for bookings made with Flight Create Orders in Self-Service?

For Self-Service users, all post-booking services must be handled offline with the consolidator you work with for ticket issuance. In general, these actions can be made while the Passenger Name Record (PNR) is queued for ticketing (before the ticket is issued), though their availability once a ticket has issued depends largely on the consolidator and the clauses of your agreement. 


### How can I get a consolidator?

Before requesting a consolidator, please first make sure that you are **in one of the** approved markets for Flight Create Orders. You need it to implement flight booking in Self-Service. Once this is verified, please go to the Support section and get in touch with us using the Contact form.

### How do I handle refunds for flights booked with Flight Create Orders in Self-Service?

Refunds must be handled offline directly with your consolidator. 

### Can I use multiple consolidators?

Yes you can use different consolidator, but you will need to tell us so we can connect both your accounts. Once we open the access, you can decide where you want your booking to go using the ‘’queuingOfficeId’’ parameter in the Flight Create Orders request.

## Destination Experiences

### Do you provide tours and activities at destination?

You can search and book activities with our [Tours and Activities API](https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/tours-and-activities). It includes 300,000 activities around the world, such as sightseeing tours, days trips, and museum tickets. The API provides a list of top activities for a given location, including the prices, ratings, descriptions, photos, as well as a deep link to complete the booking with the provider.

## Cars & Transfers 

### Who are the providers available in the Car & Transfers APIs?
The Transfers APIs will allow you to offer private transfers, hourly services, taxis, shared transfers, airport express, airport buses, private jets, and helicopter transfer. The API uses the following providers:

| Name             | Code |
|------------------|------|
| Drivania         | DRV  |
| Eco Rent A Car   | ECO  |
| EZ Shuttle ZA    | ESZ  |
| FlygTaxi         | FGT  |
| Get-E            | GET  |
| GroundScope      | GSE  |
| GroundSpan       | GSN  |
| HolidayTaxis     | HTX  |
| iVcardo          | IVC  |
| JPD Transport    | JPD  |
| Servantrip       | SVP  |
| Sixt Ride        | SMD  |
| SuperShuttle     | SPS  |
| Svea Taxi Allians| TXB  |
| Talixo           | TXO  |
| Taxibokning      | TXB  |
| TaxiTender       | TXT  |
| World Transfer   | WTR  |


## Technical support

### What kind of support does Amadeus for Developers offer?

There are two different support paths available based on our two different offer: Self-Service and Enterprise.

1. Self-Service users have at their disposal detailed documentation, guides and SDKs, to help them solve any doubts they may have. Check the Self-Service Docs page for more information. For any other Self-Service support queries, such as billing issues or a refund request, please go to the support section and click on contact us about Self-Service support.

!!! important
    **Contact Support** <br>
    You need to be [registered](https://developers.amadeus.com/register){:target="\_blank"} and [signed in](https://developers.amadeus.com/signin){:target="\_blank"} to reach out to the [Self-Service support](https://developers.amadeus.com/support/contact-us-self-service){:target="\_blank"}.

2. Enterprise users have access to dedicated support. If you are an Enterprise user, get in touch with your Account Manager or open a ticket via the Amadeus Service Hub.
 
### Where do I go for Self-Service technical support? What does it cost?

If you are a Self-Service customer experiencing a technical issue, you should do the following:
 
1. First, look for an answer in our Self-Service APIs Docs and this FAQs page. We update this page regularly with explanations on fixing common issues.
2.  Search for a solution in Stack Overflow, or ask the community for help. Our developer advocacy team actively monitors and answers the questions on Stack Overflow that relate to our APIs.
3. Finally, if you are still experiencing a problem with Self-Service APIs, you can get in touch with our developer advocates via the contact form in the Support page. We will try to get back to you as quickly as possible, however please understand that in times of high demand we may not be able to guarantee a prompt answer.

### Do you offer phone support for Self-Service APIs?

We do not currently offer phone support for Self-Service APIs. If you need assistance you can get in touch with our Developer Advocates via the contact form in the Support page. Please keep in mind that in times of high demand we may not be able to guarantee a prompt answer.

### How can I report bugs or suggest improvements to the Self-Service section?

We love feedback from our community and it helps us create the best possible product for all users! If you want to report a bug or suggest improvements, please go to the Support section and get in touch using the Contact form.
