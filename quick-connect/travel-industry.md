---
description: >-
  In this guide, we'll go over the full flight booking process, important points
  to consider when getting started and how to build a flight booking website or
  app using just three Amadeus APIs.
---

# Getting started

## How online booking works

Whether you want to create a flight booking website or app from scratch or add new features and possibilities in your app, flight booking is a powerful functionality that can boost your bottom line and give your users a complete end-to-end experience. Before you start building a flight booking website or app, it’s important to first understand how online booking works. Below, we’ll outline the overall booking flow and the role of each step in the process.

### Step 1: Perform a flight search

The first step in the online booking flow is a flight search. This returns a list of all available flights and fares for the desired search criteria.

### Step 2: Confirm availability and fare

The availability and price of airfare fluctuate so it’s important to confirm before proceeding to book. This is especially true if time passes between the initial search and the decision to book, as fares are limited and there are thousands of bookings occurring every minute. During this step, you can also add ancillary products like extra bags or legroom.

### Step 3: Make a booking

Once the fare is confirmed, you’re ready to book. In the airline industry, a booking is made when a Passenger Name Record \(PNR\) is created on the airline’s reservation system. A PNR is a unique record containing reservation data like passenger information and itinerary details.

### Step 4: Complete payment

Once the booking is made, you need to complete payment. In most cases, you’ll receive payment from the customer and then pay the airline, typically via an industry-specific settlement procedure like the BSP or ARC \(more on those later\).

### Step 5: Issue a ticket

In the final step, a flight ticket is issued. In industry terms, a flight ticket is a confirmation that payment has been received, the reservation has been logged, and the customer has the right to enjoy the flight. For [IATA member airlines](https://www.iata.org/about/members/Pages/airline-list.aspx), only certain accredited parties can issue tickets. In the next section, we’ll go into detail about your options for managing this final step in the booking process.

{% hint style="info" %}
## Summary

Flight booking is a powerful capability that you can easily incorporate into your business with Amadeus APIs. Follow these steps and get started building your booking engine today:

* **Perform a flight search** with our [Flight Offers Search API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search)
* **Confirm the fare** with our [Flight Offers Price API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-price)
* **Make a booking** with our [Flight Create Orders API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-create-orders)
* **Complete payment** via an **airline consolidator** or industry **settlement plan**
* **Issue a ticket** through ****an **airline consolidator** or get accredited to issue tickets **yourself**
{% endhint %}

