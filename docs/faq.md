# Frequently Asked Questions

This page provides help with the most common questions about Amadeus Self-service APIs.

| Domain                                                                                                                                                          | Questions                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Account registration](#account-registration) |  <ul><li>[How do I change my password?](#how-do-i-change-my-password)</li><li>[I registered but never received a confirmation email? What should I do?](#i-registered-but-never-received-a-confirmation-email-what-should-i-do)</li></ul>              |
| [Business enquiries](#business-enquiries) |  <ul><li>[How can I monetise my application?](#how-can-i-monetise-my-application)</li><li>[I would like to partner up with Amadeus](#i-would-like-to-partner-up-with-amadeus)</li></ul>              |
| [Self-Service vs Enterprise](#self-service-vs-enterprise) |  <ul><li>[What is the difference between Self-Service and Enterprise APIs?](#what-is-the-difference-between-self-service-and-enterprise-apis)</li><li>[Can I use APIs from both Self-Service and Enterprise?](#can-i-use-apis-from-both-self-service-and-enterprise?)</li><li>[How can I contact Enterprise?](#how-can-i-contact-enterprise)</li></ul>               |
| [Self-Service APIs general](#self-service-apis-general) |    <ul><li>[Is there a test environment to try the Self-Service APIs?](#is-there-a-test-environment-to-try-the-self-service-apis?)</li><li>[How do I access the Self-Service APIs documentation?](#how-do-i-access-the-self-service-apis-documentation?)</li><li>[Do you provide SDKs?](#do-you-provide-sdks)</li><li>[Where can I see code examples for Amadeus Self-Service APIs?](#where-can-i-see-code-examples-for-amadeus-self-service-apis)</li><li>[How do I make my first Self-Service API call?](#how-do-i-make-my-first-self-service-api-call)</li><li>[How do I move Self-Service APIs from test to production?](#how-do-i-move-self-service-apis-from-test-to-production)</li><li>[How do I delete my application built using Self-Service APIs?](#how-do-i-delete-my-application-built-using-self-service-apis)</li><li>[Will you include more APIs in the Self-Service catalog?](#will-you-include-more-apis-in-the-self-service-catalog?)</li><li>[What are the terms of service for Amadeus Self-Service APIs?](#what-are-the-terms-of-service-for-amadeus-self-service-apis)</li><li>[I am not a travel agent and have no experience in the travel industry, can I still use the Self-Service APIs?](#i-am-not-a-travel-agent-and-have-no-experience-in-the-travel-industry,-can-i-still-use-the-self-service-apis)</li><li>[Are there any limitations to the Self-Service API dataset?](#are-there-any-limitations-to-the-self-service-api-dataset)</li></ul>              |
| [API keys](#api-keys) |       <ul><li>[How do I get my Self-Service API key?](#how-do-i-get-my-self-service-api-key)</li><li>[Why is my Self-Service API key not working?](#why-is-my-self-service-api-key-not-working)</li><li>[How long is my Self-Service access token valid for?](#how-long-is-my-self-service-access-token-valid-for)</li><li>[Can I use my API key in a public repository?](#can-i-use-my-api-key-in-a-public-repository)</li><li>[Why has my API key been revoked?](#why-has-my-api-key-been-revoked)</li></ul>              |
| [Billing](#billing) |         <ul><li>[How is billing calculated for Self-Service APIs?](#how-is-billing-calculated-for-self-service-apis)</li><li>[How do I request a refund of my Self-Service usage bill?](#how-do-i-request-a-refund-of-my-self-service-usage-bill)</li><li>[Where can I find my invoices?](#where-can-i-find-my-invoices)</li></ul>            |
| [Test collection](#test-collection) |           <ul><li>[Is there a limit to the calls I can make to Self-Service APIs in the test environment?](#is-there-a-limit-to-the-calls-i-can-make-to-self-service-apis-in-the-test-environment)</li><li>[What should I do if I'm about to reach my Self-Service free request quota limit?](#what-should-i-do-if-im-about-to-reach-my-self-service-free-request-quota-limit)</li><li>[Is there a limit to the calls I can make to Self-Service APIs in the production environment?](#is-there-a-limit-to-the-calls-i-can-make-to-self-service-apis-in-the-production-environment)</li><li>[Why do I get a 429 error in JSON if I have some free calls left?](#why-do-i-get-a-429-error-in-json-if-i-have-some-free-calls-left)</li><li>[Why do I get an error code 429 when I call a Self-Service API?](#why-do-i-get-an-error-code-429-when-i-call-a-self-service-api)</li><li>[Is the data returned in the Self-Service test environment accurate?](#is-the-data-returned-in-the-self-service-test-environment-accurate)</li></ul>           |
| [Flight Inspiration Search](#flight-inspiration-search) |       <ul><li>[Why didn't I get any results for Flight Inspiration Search?](#why-didnt-i-get-any-results-for-flight-inspiration-search)</li><li>[Why are some origin and destination pairings not returning results?](#why-are-some-origin-and-destination-pairings-not-returning-results)</li></ul>           |
| [Airport routes](#airport-routes) |       <ul><li>[The API returns an airport that has been permanently closed](#the-api-returns-an-airport-that-has-been-permanently-closed)</li></ul>           |
| [Airport Nearest Relevant API](#airport-nearest-relevant-api) |       <ul><li>[Why isn't the Airport Nearest Relevant API returning a specific airport near me?](#why-isnt-the-airport-nearest-relevant-api-returning-a-specific-airport-near-me)</li></ul>           |
| [Flight Offers Search](#flight-offers-search) |       <ul><li>[Why are the prices returned more expensive than on other websites?](#why-are-the-prices-returned-more-expensive-than-on-other-websites)</li><li>[What does nonHomogeneous mean in the API response?](#what-does-nonhomogeneous-mean-in-the-api-response)</li><li>[Why the dataWindow parameter returns less results with I3D or I2D?](#why-the-datawindow-parameter-returns-less-results-with-i3d-or-i2d)</li><li>[How do I search using loyalty programs?](#how-do-i-search-using-loyalty-programs)</li><li>[POST and GET do not return the same results](#post-and-get-do-not-return-the-same-results)</li></ul>           |
| [Flight Offers Price](#flight-offers-price) |       <ul><li>[How can we get information on refundable flights?](#how-can-we-get-information-on-refundable-flights)</li></ul>           |
| [Flight Price Analysis](#flight-price-analysis) |       <ul><li>[Why do some origin and destination pairings not return any results?](#why-do-some-origin-and-destination-pairings-not-return-any-results)</li></ul>           |
| [Flight Delay Prediction](#flight-delay-prediction) |       <ul><li>[Why do I get the INFERENCE error?](#why-do-i-get-the-inference-error)</li></ul>           |
| [Flight Cheapest Date Search](#flight-cheapest-date-search) |       <ul><li>[Why are some origin and destination pairings not returning results?](#why-are-some-origin-and-destination-pairings-not-returning-results)</li><li>[Why do I get the 500 error message?](#why-do-i-get-the-500-error-message)</li></ul>           |
| [Flight Availabilities Search](#flight-availabilities-search) |       <ul><li>[Why are some travel classes not returned in the search results?](#why-are-some-travel-classes-not-returned-in-the-search-results)</li></ul>           |
| [Branded Fares Upsell](#branded-fares-upsell) |       <ul><li>[Why do additional services change between segments in an Itinerary?](#why-do-additional-services-change-between-segments-in-an-itinerary)</li></ul>           |
| [SeatMap Display](#seatmap-display) |       <ul><li>[Is there any way to request a seat map by cabin instead of having to specify a booking class code?](#is-there-any-way-to-request-a-seat-map-by-cabin-instead-of-having-to-specify-a-booking-class-code)</li><li>[Why do I get the error code 4926?](#why-do-i-get-the-error-code-4926)</li><li>[Why am I unable to retrieve seatmap data?](#why-am-i-unable-to-retrieve-seatmap-data)</li><li>[Seatmap not available as flight operated by another carrier](#seatmap-not-available-as-flight-operated-by-another-carrier)</li></ul>           |
| [Flight Create Orders API](#flight-create-orders-api) |        <ul><li>[How are tickets issued for flights booked with Flight Create Orders in Self-Service?](#how-are-tickets-issued-for-flights-booked-with-flight-create-orders-in-self-service)</li><li>[How can I retrieve booking made with Flight Create Orders in Self-Service?](#how-can-i-retrieve-booking-made-with-flight-create-orders-in-self-service)</li><li>[Does Amadeus pay a commission for flights booked with Flight Create Orders in Self-Service?](#does-amadeus-pay-a-commission-for-flights-booked-with-flight-create-orders-in-self-service)</li><li>[Why do I get the INVALID DATA RECEIVED error?](#why-do-i-get-the-invalid-data-received-error)</li><li>[Why do I get the SEGMENT SELL FAILURE error?](#why-do-i-get-the-segment-sell-failure-error)</li><li>[How does payment work when I book a flight?](#how-does-payment-work-when-i-book-a-flight)</li><li>[How can I cancel a flight?](#how-can-i-cancel-a-flight)</li><li>[How to make the airline consolidator wait before issuing a ticket?](#how-to-make-the-airline-consolidator-wait-before-issuing-a-ticket)</li></ul>                 |
| [Hotel Search](#hotel-search) |       <ul><li>[What are guarantee, deposit and prepay?](#what-are-guarantee-deposit-and-prepay)</li><li>[What is the total price?](#what-is-the-total-price)</li><li>[What is the latest possible date for check-in?](#what-is-the-latest-possible-date-for-check-in)</li><li>[How to search a hotel by location](#how-to-search-a-hotel-by-location)</li><li>[How to search hotel images](#how-to-search-hotel-images)</li></ul>           |
| [Hotel Booking](#hotel-search) |       <ul><li>[What type of payments are supported?](#what-type-of-payments-are-supported)</li><li>[Can I markup the room prices?](#can-i-markup-the-room-prices)</li><li>[Payment providers and gateways](#payment-providers-and-gateways)</li><li>[How can I cancel a room booking?](#how-can-i-cancel-a-room-booking)</li><li>[Why do I get 500 status code?](#why-do-i-get-500-status-code)</li><li>[How can I see Amadeus API coverage for a hotel chain?](#how-can-i-see-amadeus-api-coverage-for-a-hotel-chain)</li><li>[What is considered a query?](#what-is-considered-a-query)</li><li>[Do I need any legal documents to make a booking?](#do-i-need-any-legal-documents-to-make-a-booking)</li><li>[What are the room type codes?](#what-are-the-room-type-codes)</li></ul>           |
| [Airline consolidators](#airline-consolidators) |    <ul><li>[What is an airline consolidator?](#what-is-an-airline-consolidator)</li><li>[How are payments handled with my consolidator?](#how-are-payments-handled-with-my-consolidator)</li><li>[How do I handle cancellations, changes and post-booking services for bookings made with Flight Create Orders in Self-Service?](#how-do-i-handle-cancellations-changes-and-post-booking-services-for-bookings-made-with-flight-create-orders-in-self-service)</li><li>[How do I handle refunds for flights booked with Flight Create Orders in Self-Service?](#how-do-i-handle-refunds-for-flights-booked-with-flight-create-orders-in-self-service)</li><li>[How can I get a consolidator?](#how-can-i-get-a-consolidator)</li></ul>            |
| [Technical support](#technical-support) |          <ul><li>[What kind of support does Amadeus for Developers offer?](#what-kind-of-support-does-amadeus-for-developers-offer)</li><li>[Where do I go for Self-Service technical support? What does it cost?](#where-do-i-go-for-self-service-technical-support-what-does-it-cost)</li><li>[Do you offer phone support for Self-Service APIs?](#do-you-offer-phone-support-for-self-service-apis)</li><li>[How can I report bugs or suggest improvements to the Self-Service section?](#how-can-i-report-bugs-or-suggest-improvements-to-the-self-service-section)</li></ul>          |



## Account registration

### How do I change my password?

To change your password, sign in to the [Developers portal](https://developers.amadeus.com/){:target="\_blank"} and click on **My Account** in the top right corner of the screen. You'll find the option to change your password at the bottom of the page. Please remember that we never send your password in any correspondence.

## I registered but never received a confirmation email? What should I do?

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


### Can I use APIs from both Self-Service and Enterprise?

Yes, you can use APIs from both catalogs, but please keep in mind that the requirements and conditions of each offer are very different. Please check our [Get Started guide](https://developers.amadeus.com/get-started/get-started-with-amadeus-apis-334){:target="\_blank"} for more information.

### How can I contact Enterprise?

To contact the Enterprise team, please fill in the following [contact us form](https://developers.amadeus.com/support/contact-us-enterprise) and someone from the Enterprise team will get back to you shortly. Please keep in mind that the access to Enterprise requires an implementation fee as well as monthly fees.


## Self-Service APIs general


### Is there a test environment to try the Self-Service APIs?

Yes! You can try Self-Service APIs in our test environment and enjoy a free monthly request quota to build and test your app. If you exceed this free request quota in the test environment, you'll receive a 429 error code in JSON and not be able to call the APIs.

If you need to increase the number of monthly API calls, please consider moving your application to production. It's a quick and easy process and you will keep the free request quota you enjoyed in test. Once you reach your threshold in production, you will simply pay for the additional API calls you make.

### How do I access the Self-Service APIs documentation?

Check our [Amadeus for Developers docs portal](/docs/index.md) for links to interactive reference documentation for each API and helpful guides covering topics such as authorization, pagination and common errors. On the [Amadeus for Developers GitHub page](https://github.com/amadeus4dev/){:target="\_blank"}, you can also find code samples and SDKs.

### Do you provide SDKs?

Yes! On the [Amadeus for Developers GitHub page](https://github.com/amadeus4dev/){:target="\_blank"} you can find open-source SDKs in various languages. Alternatively, you can use [OpenAPI Generator](/docs/developer-tools/openapi-generator.md){:target="\_blank"} to create an SDK from our [OpenAPI files](https://github.com/amadeus4dev/amadeus-open-api-specification){:target="\_blank"}.

### Where can I see code examples for Amadeus Self-Service APIs?

Code examples for all Amadeus Self-Service APIs are available in our [GitHub](https://github.com/amadeus4dev/amadeus-code-examples){:target="\_blank"}.

### How do I make my first Self-Service API call?

On the [Get Started with Self-Service APIs](https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335){:target="\_blank"} page you can find information on creating an account, getting your API key and making your first call.
 

### How do I move Self-Service APIs from test to production?

To launch your application to production, please follow the steps described in our [Moving to production](/docs/API-Keys/moving-to-production.md){:target="\_blank"} guide.

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

We do not return data on American Airlines, Low cost carriers, and, in some markets, British Airways. For other arlines we only return published rates. We do not return negotiated rates or any other special rates. The Flight Offers Search only returns the bag allowance information for one passenger type code. Airlines blacklisted in the EU are not returned using the Flight Offers Search GET, e.g., Iraqi Airways. There is a possibility to override this with the POST method.


## API keys

### What is an API key?

An API key is a unique reference number which identifies your application to Amadeus. The API key is part of the authorization process and must be sent with each API request. If you have multiple applications using Amadeus APIs, each application must have its own API key. For more details, check our [Authorization guide](/docs/API-Keys/authorization.md).

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

You will receive your invoices on a monthly basis from [data.distribution@amadeus.com](data.distribution@amadeus.com). Please note that once opened, you will not be able to open the same invoice again.

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

The information returned in test environment is from [limited data collections](/docs/test-data.md){:target="\_blank"}. This is done as a security measure to protect our data and our customers. When you move to production, you will get access to complete and live data.

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

### How do I search using loyalty programs?

Flight Offers Price and SeatMap Display both accept frequent flyer information, so end-users can benefit from their loyalty program. When adding frequent flyer information, please remember that each airline policy is different, and some require additional information like passenger name, email, or phone number to validate the account. If validation fails, your user won’t receive their loyalty program advantages.

### POST and GET do not return the same results

By default the GET method does not return airlines blacklisted in Europe. However, users can override this using the POST method.


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


## Hotel Search

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

* Since the commissioning of Hotel Search v3, we can no longer search hotels by IATA codes. In order to search by location you will need to use the [third endpoint of Hotel List](/reference-data/locations/hotels/by-geocode), which allows you to search using a latitude & longitude. The Hotel List API returns `hotelIds` based on the specific search coordinates. You will then need to use this `hotelId` in the third endpoint of the Hotel Search API.

* Alternatively, you can use the Google API to retrieve the geo location of a specific location and use the Hotel Search by geo location.


## Hotel Booking

### What type of payments are supported?

The current version of the Hotel Booking API only supports credit card payments. The Hotel Search API returns the payment policy of each hotel under `acceptedPayments` in the policies section.

### Can I markup the room prices?

It is not possible to markup the prices of the hotel rooms with the current version of the Hotel Booking API. The reason is that the content we offer today in our Hotel Search/Book API is post-paid, meaning the traveler will pay directly at the hotel. The Hotel Booking API is here to enable making a reservation but not to pay directly. We are working on adding more hotel offers, especially offers that will be pre-paid, meaning you will be able to charge the travelers directly and add a markup. However, you still need to add a credit card while booking in case of cancellations or no-shows.

### Payment providers and gateways

The Hotel Booking API works by using the guest's payment information and sending it to a chosen hotel for the reservation. You can use a payment gateway in your app, but this will not change the way the API works. The hotels will never collect any money from you. Instead, the payments are always done at the time of checkout between the guest and the hotel. During the booking process, Amadeus passes the payment and guest information to the hotel but does not validate information, so it doesn’t play the role of payment gateway. Be sure to validate the payment and guest information as invalid information may result in the reservation being canceled. As soon as your application stores, transmits, or processes cardholder information, you will need to comply with the PCI Data Security Standard (PCI DSS). For more information, visit the [PCI Security Council website](https://www.pcisecuritystandards.org/merchants/).

### How can I cancel a room booking?

As of now, the hotel booking API does not allow canceling rooms. If this option is possible with your hotel offer, the cancellation will have to be done manually with the hotels. We are working on an API for the cancellation; however, it is still too soon to commit to anything.

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

## Technical support

### What kind of support does Amadeus for Developers offer?

There are two different support paths available based on our two different offer: Self-Service and Enterprise.

1. Self-Service users have at their disposal detailed documentation, guides and SDKs, to help them solve any doubts they may have. Check the Self-Service Docs page for more information. For any other Self-Service support queries, such as billing issues or a refund request, please go to the support section and click on contact us about Self-Service support.
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
