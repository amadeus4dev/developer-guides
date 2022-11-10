# Frequently Asked Questions

This page provides help with the most common questions about Amadeus Self-service APIs.

| Domain                                                                                                                                                          | Questions                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Account registration](#account-registration) |  <ul><li>[How do I change my password?](#how-do-i-change-my-password)</li><li>[I registered but never received a confirmation email? What should I do?](#i-registered-but-never-received-a-confirmation-email-what-should-i-do)</li></ul>              |
| [Self-Service vs Enterprise](#self-service-vs-enterprise) |  <ul><li>[What is the difference between Self-Service and Enterprise APIs?](#what-is-the-difference-between-self-service-and-enterprise-apis)</li><li>[Can I use APIs from both Self-Service and Enterprise?](#can-i-use-apis-from-both-self-service-and-enterprise?)</li></ul>               |
| [Self-Service APIs](#self-service-apis) |    <ul><li>[Is there a test environment to try the Self-Service APIs?](#is-there-a-test-environment-to-try-the-self-service-apis?)</li><li>[How do I access the Self-Service APIs documentation?](#how-do-i-access-the-self-service-apis-documentation?)</li><li>[Do you provide SDKs?](#do-you-provide-sdks)</li><li>[Where can I see code examples for Amadeus Self-Service APIs?](#where-can-i-see-code-examples-for-amadeus-self-service-apis)</li><li>[How do I make my first Self-Service API call?](#how-do-i-make-my-first-self-service-api-call)</li><li>[How do I move Self-Service APIs from test to production?](#how-do-i-move-self-service-apis-from-test-to-production)</li><li>[How do I delete my application built using Self-Service APIs?](#how-do-i-delete-my-application-built-using-self-service-apis)</li><li>[Will you include more APIs in the Self-Service catalog?](#will-you-include-more-apis-in-the-self-service-catalog?)</li><li>[What are the terms of service for Amadeus Self-Service APIs?](#what-are-the-terms-of-service-for-amadeus-self-service-apis)</li><li>[I am not a travel agent and have no experience in the travel industry, can I still use the Self-Service APIs?](#i-am-not-a-travel-agent-and-have-no-experience-in-the-travel-industry,-can-i-still-use-the-self-service-apis)</li></ul>              |
| [API keys](#api-keys) |       <ul><li>[How do I get my Self-Service API key?](#how-do-i-get-my-self-service-api-key)</li><li>[Why is my Self-Service API key not working?](#why-is-my-self-service-api-key-not-working)</li><li>[How long is my Self-Service access token valid for?](#how-long-is-my-self-service-access-token-valid-for)</li><li>[Can I use my API key in a public repository?](#can-i-use-my-api-key-in-a-public-repository)</li><li>[Why has my API key been revoked?](#why-has-my-api-key-been-revoked)</li></ul>              |
| [Billing](#billing) |         <ul><li>[How is billing calculated for Self-Service APIs?](#how-is-billing-calculated-for-self-service-apis)</li><li>[How do I request a refund of my Self-Service usage bill?](#how-do-i-request-a-refund-of-my-self-service-usage-bill)</li></ul>            |
| [Test collection](#test-collection) |           <ul><li>[Is there a limit to the calls I can make to Self-Service APIs in the test environment?](#is-there-a-limit-to-the-calls-i-can-make-to-self-service-apis-in-the-test-environment)</li><li>[What should I do if I'm about to reach my Self-Service free request quota limit?](#what-should-i-do-if-im-about-to-reach-my-self-service-free-request-quota-limit)</li><li>[Is there a limit to the calls I can make to Self-Service APIs in the production environment?](#is-there-a-limit-to-the-calls-i-can-make-to-self-service-apis-in-the-production-environment)</li><li>[Why do I get a 429 error in JSON if I have some free calls left?](#why-do-i-get-a-429-error-in-json-if-i-have-some-free-calls-left)</li><li>[Why do I get an error code 429 when I call a Self-Service API?](#why-do-i-get-an-error-code-429-when-i-call-a-self-service-api)</li><li>[Is the data returned in the Self-Service test environment accurate?](#is-the-data-returned-in-the-self-service-test-environment-accurate)</li></ul>           |
| [Flight Inspiration Search](#flight-inspiration-search) |       <ul><li>[Why didn't I get any results for Flight Inspiration Search?](#why-didnt-i-get-any-results-for-flight-inspiration-search)</li></ul>           |
| [Airport Nearest Relevant API](#airport-nearest-relevant-api) |       <ul><li>[Why isn't the Airport Nearest Relevant API returning a specific airport near me?](#why-isnt-the-airport-nearest-relevant-api-returning-a-specific-airport-near-me)</li></ul>           |
| [Flight Create Orders API](#flight-create-orders-api) |        <ul><li>[How are tickets issued for flights booked with Flight Create Orders in Self-Service?](#how-are-tickets-issued-for-flights-booked-with-flight-create-orders-in-self-service)</li><li>[How can I retrieve booking made with Flight Create Orders in Self-Service?](#how-can-i-retrieve-booking-made-with-flight-create-orders-in-self-service)</li><li>[Does Amadeus pay a commission for flights booked with Flight Create Orders in Self-Service?](#does-amadeus-pay-a-commission-for-flights-booked-with-flight-create-orders-in-self-service)</li></ul>                 |
| [Airline consolidators](#airline-consolidators) |    <ul><li>[What is an airline consolidator?](#what-is-an-airline-consolidator)</li><li>[How are payments handled with my consolidator?](#how-are-payments-handled-with-my-consolidator)</li><li>[How do I handle cancellations, changes and post-booking services for bookings made with Flight Create Orders in Self-Service?](#how-do-i-handle-cancellations-changes-and-post-booking-services-for-bookings-made-with-flight-create-orders-in-self-service)</li><li>[How do I handle refunds for flights booked with Flight Create Orders in Self-Service?](#how-do-i-handle-refunds-for-flights-booked-with-flight-create-orders-in-self-service)</li></ul>            |
| [Technical support](#technical-support) |          <ul><li>[What kind of support does Amadeus for Developers offer?](#what-kind-of-support-does-amadeus-for-developers-offer)</li><li>[Where do I go for Self-Service technical support? What does it cost?](#where-do-i-go-for-self-service-technical-support-what-does-it-cost)</li><li>[Do you offer phone support for Self-Service APIs?](#do-you-offer-phone-support-for-self-service-apis)</li><li>[How can I report bugs or suggest improvements to the Self-Service section?](#how-can-i-report-bugs-or-suggest-improvements-to-the-self-service-section)</li></ul>          |



## Account registration

### How do I change my password?

To change your password, sign in to the [Developers portal](https://developers.amadeus.com/) and click on **My Account** in the top right corner of the screen. You'll find the option to change your password at the bottom of the page. Please remember that we never send your password in any correspondence.

## I registered but never received a confirmation email? What should I do?

If you haven't received a confirmation mail, it is often because the email address was entered incorrectly. Please sign in to the [Developers portal](https://developers.amadeus.com/) and visit the **My Account** section to confirm that the email address used to create the account is correct. If so, please check your spam folder for an email from noreply@amadeus.com.

## Self-Service vs Enterprise


### What is the difference between Self-Service and Enterprise APIs?

Amadeus for Developers provides two different offers, each of which meets distinct customer needs: Self-Service and Enterprise. 

The **Self-Service** offer targets independent developers and start-ups that wish to connect to Amadeus APIs in a quick and easy manner. You can access and start testing these new REST/JSON APIs in less than 3 minutes, and get quick access to production data with a flexible pay-as-you-go pricing model. Please note that the catalog includes some selected APIs only, although we will be constantly releasing new APIs.
 
The **Enterprise** offer provides access to the full Amadeus APIs catalog, tailored to companies with scaling needs as well as the leading brands in the travel industry. Customers of Enterprise APIs receive dedicated support from their account managers and enjoy a customized pricing scheme to meet their needs. Please note that access to Enterprise APIs is only granted on a request basis, and some special requirements may apply. Our Enterprise commercial teams will be happy to guide you through the process.


### Can I use APIs from both Self-Service and Enterprise?

Yes, you can use APIs from both catalogs, but please keep in mind that the requirements and conditions of each offer are very different. Please check our [Get Started guide](https://developers.amadeus.com/get-started/get-started-with-amadeus-apis-334) for more information.

## Self-Service APIs


### Is there a test environment to try the Self-Service APIs?

Yes! You can try Self-Service APIs in our test environment and enjoy a free monthly request quota to build and test your app. If you exceed this free request quota in the test environment, you'll receive a 429 error code in JSON and not be able to call the APIs.

If you need to increase the number of monthly API calls, please consider moving your application to production. It's a quick and easy process and you will keep the free request quota you enjoyed in test. Once you reach your threshold in production, you will simply pay for the additional API calls you make.

### How do I access the Self-Service APIs documentation?

Check our [Amadeus for Developers docs portal](https://amadeus4dev.github.io/developer-guides/) for links to interactive reference documentation for each API and helpful guides covering topics such as authorization, pagination and common errors. On the [Amadeus for Developers GitHub page](https://github.com/amadeus4dev/), you can also find code samples and SDKs.

### Do you provide SDKs?

Yes! On the [Amadeus for Developers GitHub page](https://github.com/amadeus4dev/) you can find open-source SDKs in various languages. Alternatively, you can use [OpenAPI Generator](https://amadeus4dev.github.io/developer-guides/sdks/openapi-generator/) to create an SDK from our [OpenAPI files](https://github.com/amadeus4dev/amadeus-open-api-specification).

### Where can I see code examples for Amadeus Self-Service APIs?

Code examples for all Amadeus Self-Service APIs are available in our [GitHub](https://github.com/amadeus4dev/amadeus-code-examples).

### How do I make my first Self-Service API call?

On the [Get Started with Self-Service APIs](https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335) page you can find information on creating an account, getting your API key and making your first call.
 

### How do I move Self-Service APIs from test to production?

To launch your application to production, please follow the steps described in our [Moving to production](https://amadeus4dev.github.io/developer-guides/API-Keys/moving-to-production/) guide.

You will be asked to sign a contract and provide billing information before receiving your new API key. When you move to production, you will maintain the same free monthly request quota you enjoyed in test. When you reach your monthly threshold, you will be billed for the additional API calls you make at the rates shown on our [Pricing page](https://developers.amadeus.com/pricing).

### How do I delete my application built using Self-Service APIs?

To delete an application, visit the **My apps** section of your **My Self-Service Workspace**. Remember that deleted apps cannot be recovered.

### Will you include more APIs in the Self-Service catalog?

We are constantly expanding our Self-Service API catalog with new APIs from all travel segments such as flights, hotels, cars or destination content. If you have any specific requests or feedback regarding APIs that you would like to add to your catalog, please contact us. We'd love to hear from you!

### What are the terms of service for Amadeus Self-Service APIs?

To find out more about our terms and conditions for the test environment, please visit our [Terms and Conditions page](https://developers.amadeus.com/legal/terms-of-use).

If you are already in production, you should have received an email with the legal terms regulating API usage in the production environment. If you have not received this information, please [contact us](https://developers.amadeus.com/support/contact-us-self-service).

### I am not a travel agent and have no experience in the travel industry, can I still use the Self-Service APIs?

Our Self-Service offer is designed for newcomers to Amadeus, there are no prerequisites. Any developer who wishes to connect to Amadeus travel data can do so in a quick and easy way via our Self-Service offer.  For more details, please check our [Get Started guide](https://developers.amadeus.com/get-started/get-started-with-amadeus-apis-334).


## API keys

### What is an API key?

An API key is a unique reference number which identifies your application to Amadeus. The API key is part of the authorization process and must be sent with each API request. If you have multiple applications using Amadeus APIs, each application must have its own API key. For more details, check our [Authorization guide](https://amadeus4dev.github.io/developer-guides/API-Keys/authorization/).

Your API keys are also used to track usage. To avoid unwanted charges, please do no share or post them in public repositories. For more information, see this [article on best practices for secure API key storage](https://developers.amadeus.com/blog/best-practices-api-key-storage).

### How do I get my Self-Service API key?

To get a Self-Service API key, simply create an account in the [Amadeus for Developers portal](https://developers.amadeus.com/). Next, visit the **My Self-Service Workspace** area and create your first application. An API key will be generated automatically. Remember, your API key is private and should not be shared publicly.

### Why is my Self-Service API key not working?

If your API key is not working, please verify that it is the same exact key that was provided in the **My Self-Service Workspace**.

Please keep in mind that we automatically revoke API keys that are publicly searchable. This is done to protect users against unwanted usage bills. As a general rule, you should not put your API keys in the source code you commit to GitHub or other public repositories. Instead, you should store your keys as environment variables rather than hard-coding them in your script. For more information, see this [article on best practices for secure API key storage](https://developers.amadeus.com/blog/best-practices-api-key-storage).

### How long is my Self-Service access token valid for?

The access token is valid for 1800 seconds (30mins). If you get an authentication fail, please request a new token.

### Can I use my API key in a public repository?

Storing your API keys or any other sensitive information in a public repository must be avoided at all costs to prevent malicious access to your APIs, which could result in unwanted usage bills.

In order to protect our users, we automatically revoke API keys that are publicly searchable. We recommend that you store your keys as environment variables rather than hard-coding them in your script. For more information, see this [article on best practices for secure API key storage](https://developers.amadeus.com/blog/best-practices-api-key-storage).

### Why has my API key been revoked?

We automatically revoke publicly searchable API keys to prevent unwanted charges to your account. To prevent this from happening, you should read your API key from a system environment variable rather than putting it in the source code you commit to GitHub. If you need to get a new API key, please go to **My Self-Service Workspace**.

## Billing

### How is billing calculated for Self-Service APIs?

It is free to test and prototype with Self-Service APIs and you will enjoy a free monthly request quota in both the test and production environments.

When you exceed your free request quota in production, you will be billed for the additional calls you make at the rates indicated on our [Pricing page](https://developers.amadeus.com/pricing), with no additional fees. Please note that prices vary from one API to another.

You can check your monthly usage and select your preferred payment method (credit card or bank transfer) in your Self-Service Workspace.

### How do I request a refund of my Self-Service usage bill?

If you're a Self-Service API user, please send your refund requests via the [contact us](https://developers.amadeus.com/support/contact-us-self-service) and our team will carefully analyse them. You will be notified if your refund is approved and be reimbursed within the following days (please note that refund processing times may vary depending on your bank).

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

The information returned in test environment is from [limited data collections](https://amadeus4dev.github.io/developer-guides/test-data/). This is done as a security measure to protect our data and our customers. When you move to production, you will get access to complete and live data.

## Flight Inspiration Search

### Why didn't I get any results for Flight Inspiration Search?

This API works with cached data in the test environment and not all airports are cached. You can find a list of airports included in the cached data in our guides section. When combining these searches with the Airport Nearest Relevant API, it is better to search using the city code rather than the airport code.

## Airport Nearest Relevant API

### Why isn't the Airport Nearest Relevant API returning a specific airport near me?

This may be because an airport is near a national boarder. If so, please check the API parameters for location. Also, please keep in mind that our Airport Nearest Relevant API excludes private and military airports.

## Flight Create Orders API

### How are tickets issued for flights booked with Flight Create Orders in Self-Service?

For Self-Service users, ticketing must be done via airline consolidator. Airline consolidators are essentially air ticket wholesalers that have special arrangements with airlines and, among other functions, can serve as host agencies for travel agents without the necessary IATA/ARC certifications necessary to issue tickets.

To access Flight Create Orders in production, you must have a contract signed with a consolidator for ticket issuance. If you need help finding a consolidator, please contact our support team to put in touch with the best consolidator in your region.

### How can I retrieve booking made with Flight Create Orders in Self-Service?

You can consult booking made through Flight Create Orders using the Flight Order Management API. This API works using a unique identifier(the flight offer id) that is returned by the Flight Create Orders API.

### Does Amadeus pay a commission for flights booked with Flight Create Orders in Self-Service?

Generally, Amadeus does not offer booking commissions for new Self-Service users.

## Airline consolidators

### What is an airline consolidator?

Airlines consolidators are wholesalers of air tickets. They usually partner with airlines to get negotiated rates for air tickets, and then resell the air tickets to travel agents or consumers.

Many airlines consolidators act as host agencies for retail travel agencies or online travel agency startups that do not have the license from the International Air Transport Association (IATA) to issue air tickets. To issue air tickets via airline consolidators, the travel startups have to settle commercial agreements with the airline consolidators in the markets in which they want to operate. 

It is to be noted that not all the airline consolidators provide post-ticketing services such as monitoring and notifying travel agencies about schedule changes and flight cancellations. This is something that startups have to check with their potential airline consolidators. 


### How are payments handled with my consolidator?

Different airline consolidators handle payments in different ways. In some cases, you will be asked to make an initial deposit to cover future ticketing charges. In other cases, you will be billed monthly for the services consumed. Please contact our support team or refer to your airline consolidator contract for more details.
 
### How do I handle cancellations, changes and post-booking services for bookings made with Flight Create Orders in Self-Service?

For Self-Service users, all post-booking services must be handled offline with the consolidator you work with for ticket issuance. In general, these actions can be made while the Passenger Name Record (PNR) is queued for ticketing (before the ticket is issued), though their availability once a ticket has issued depends largely on the consolidator and the clauses of your agreement. 

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
