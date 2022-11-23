Are you still using the old version of the [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search)? This guide will help you migrate to the new version of the [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search) and leverage its advantages right from the start.

## How is the Hotel Search API v3 different to v2.1?

The main difference between the two API versions is that the v2.1 endpoint `/shopping/hotel-offers/by-hotel` has been integrated into the v3 `/shopping/hotel-offers/ endpoint`. All hotel offers in the Hotel Search v3 are now queried by hotel’s unique Amadeus Id, which renders the v2.1 endpoint `/shopping/hotel-offers/by-hotel` obsolete.

We also have a new API to help you ensure a seamless migration – the [Hotel List API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-list). This API returns a list of hotels by a unique Amadeus hotel Id, IATA city code or geographic coordinates.

The diagram below shows a high-level overview of the differences between the [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search) v2.1 and v3.
 
![overview](../images/hotel-search.png) 

Now let’s have a closer look at the differences on the parameters level.

### GET /shopping/hotel-offers

#### New required query parameters

| **Parameter** | **Description** |
| :--- | :--- |
| `hotelIds` | Amadeus property codes on 8 chars. This parameter was an optional query parameter in v2.1. |
| `adults` | Number of adult guests (1-9) per room. This parameter was an optional query parameter in v2.1. |	
	
	

#### Removed query parameters

| **Parameter** | **Description** |
| :--- | :--- |
| `cityCode` | Destination IATA city code. This parameter is still returned in the successful response for each hotel. To search a hotel by the IATA city code, use the Hotel List API. |
| `latitude` | Latitude of a geographical point used for the search. This parameter is returned in the successful response for each hotel as the latitude of the given hotel. To search a hotel by geographic coordinates, use the Hotel List API. |
| `longitude` | Longitude of a geographical point used for the search. This parameter is returned in the successful response for each hotel as the longitude of the given hotel. To search a hotel by geographic coordinates, use the Hotel List API. |
| `radius` | Maximum distance (in radiusUnit) from Destination (city centre or geocodes). This parameter is not present in the response. |
| `radiusUnit` | Distance unit (of the radius value). This parameter is not present in the response. |
| `hotelName` | Hotel name used for the search. This parameter is returned in the successful response for each hotel. |
| `chains` | Chain (EM...) or Brand (SB...) or Merchant (AD...) (comma separated list of Amadeus 2 chars codes). This parameter is now shown as chainCode and returned in the successful response for each hotel. |
| `amenities` | Amenities list per hotel. To use this parameter for hotel search, refer to the Hotel List API. |
| `ratings` | Hotel stars. To use this parameter for hotel search, refer to the Hotel List API. |
| `cacheControl` | Parameter to force bypass the Amadeus cache (slower response) or get only hotels that are in the cache. |



#### Added optional query parameters 

| **Parameter** | **Description** |
| :--- | :--- |
| `countryOfResidence` | Code of the traveller’s country of residence in the ISO 3166-1 format. |


#### Data model changes

##### Hotel Offers

###### Removed parameters 

•	The hotel object does not contain the hotelDistance object as the search by radius has been omitted.
•	The address, contact, amenities and media objects are excluded from the response.
•	Metadata for the pagination is not in the response as the Hotel Search v3 does not use pagination.

###### Added parameters

•	The offers object now contains the checkInDate and checkOutDate.
•	New object commission has been added to the response.
•	New object taxes has been added to the response.

| **Parameter** | **Description** |
| :--- | :--- |
| `checkInDate` | Check-in date. |
| `checkOutDate` | Check-out date. |
| `commission` | This object defines the commission to be paid by the traveller to the hotel. It has three properties:<ul><li>`percentage` – a string showing the percentage of the commission paid to the travel seller, the value is between 0 and 100.</li><li>`amount` – a string showing the amount of the commission paid to the travel seller, the amount is always linked to the currency code of the offer.</li><li>`description` – a string for the free text field for any notes on the commission.</li></ul> |
| `taxes` | This object shows the tax data as per the IATA tax definition: “An impost for raising revenue for the general treasury and which will be used for general public purposes”. It contains the following properties:<ul><li>`amount` - a string, which defines the tax amount with a decimal separator.</li><li>`currency`- a string, which defines a monetary unit of the tax. It is a three-alpha code (IATA code). Example: EUR for Euros, USD for US dollar, etc.</li><li>`code` - a string for the International Standards Organization (ISO) Tax code. It is a two-letter country code.</li><li>`percentage` - a string, which will indicate, in the case of a tax on TST value, the percentage of the tax.</li><li>`included` - a boolean, which indicates if tax is included or not.</li><li>`description` - a string for the tax description.</li><li>`pricingFrequency` - a string, which specifies if the tax applies per stay or per night.</li><li>`pricingMode` - a string, which specifies if the tax applies per occupant or per room.</li></ul> |


### GET / shopping/hotel-offers/{offerId}

#### Data Model changes

##### Offers

###### Added parameters 

•	The checkInDate, checkOutDate, category, commission, boardType properties have been added.
•	The price object has additional properties sellingTotal, base, taxes, markups, variations.
•	New object policies has been added.

| **Parameter** | **Description** |
| :--- | :--- |
| `checkInDate` | Check-in date. |
| `checkOutDate` | Check-out date. |
| `category` | Offer category. |
| `commission` | This object defines the commission to be paid by the traveller to the hotel. It has three properties:<ul><li>`percentage` – a string showing the percentage of the commission paid to the travel seller, the value is between 0 and 100.</li><li>`amount` – a string showing the amount of the commission paid to the travel seller, the amount is always linked to the currency code of the offer.</li><li>`description` – a string for the free text field for any notes on the commission.</li></ul> |
| `sellingTotal` | A string defining the price Total + margins + markup + totalFees – discounts. |
| `base` | A string for the base price of the offer. |
| `taxes` | This object shows the tax data as per the IATA Tax definition: “An impost for raising revenue for the general treasury and which will be used for general public purposes”. It contains the following properties:<ul><li>`amount` - a string, which defines the tax amount with a decimal separator.</li><li>`currency`- a string, which defines a monetary unit of the tax. It is a three-alpha code (IATA code). Example: EUR for Euros, USD for US dollar, etc.</li><li>`code` - a string for the International Standards Organization (ISO) Tax code. It is a two-letter country code.</li><li>`percentage` - a string, which will indicate, in the case of a tax on TST value, the percentage of the tax.</li><li>`included` - a boolean, which indicates if tax is included or not.</li><li>`description` - a string for the tax description.</li><li>pricingFrequency - a string, which specifies if the tax applies per stay or per night.</li></ul> |
| `pricingMode` | a string, which specifies if the tax applies per occupant or per room. |
| `markups` | An object defining the markup. Markups are applied to provide a service or a product to the client. The markup can be introduced by any stakeholder. Typical use case is to convey markup information set by the travel agent or in case of merchant mode. The object contains a string amount, which defines the monetary value with a decimal position. |
| `variations` | An object defining the hotel daily price variations. It has the following properties:<ul><li>`average` – an object that encompasses the price object.</li><li>`changes` – an object defining the collection of price periods if the daily price changes during the stay.</li></ul> |	
| `policies` | An object defining the hotel booking rules. |


##### Hotel

###### Removed parameters

The rating, latitude, longitude, amenities, media parameters have been removed.

###### Values returned by the response

The address, contact, amenities, media values have been removed.

## Use case inspirations

You can easily integrate the new [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search) in your hotel booking engine or combine it with other APIs in our Hotel category, such as the [Hotel Ratings API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-ratings) or [Hotel Name Autocomplete API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-name-autocomplete). Whatever your use case might be, the Amadeus Self-Service APIs will help your business achieve the competitive advantage in the travel industry.


## FAQ

-	How can I get the hotel image/address/contact details/rating/amenities?
    *	Due to legal constraints we, unfortunately, can no longer distribute hotel images and specific details through our Self-Service APIs. We apologise for any inconvenience caused. If you need a workaround in the meantime, we recommend using [Leonardo](https://www.leonardoworldwide.com/), our trusted data provider. 

-	How can I use the data without the cache data control?
    * The [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search) v3 is using live data directly while avoiding the need to build cache and add any extra validation mechanisms to the data.

-	How do I get the hotel rating?
    * We offer data on hotel rating via our Hotel Rating API. Please bear in mind that this rating information is based on the sentiment analysis and not the star rating system. You can, however, retrieve a list of hotels by their star rating using the [Hotel List API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-list) with the required star rating as an additional query parameter.
