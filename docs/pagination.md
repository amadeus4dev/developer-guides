# Pagination on Self-Service APIs

Amadeus for Developers Self-Service APIs can often return a lot of results. For example, when calling the [Safe Place API](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place){:target="\_blank"}, you may get a response hundreds of pages long.
That's where **pagination** comes in. Using pagination, you can split the results into different pages to make the responses easier to handle.

Not all Amadeus Self-Service APIs support pagination. The following APIs currently support pagination:


* [Safe Place](https://developers.amadeus.com/self-service/category/covid-19-and-travel-safety/api-doc/safe-place){:target="\_blank"} 
* [Points of Interest](https://developers.amadeus.com/self-service/category/destination-content/api-doc/points-of-interest){:target="\_blank"}
* [Airport Nearest Relevant](https://developers.amadeus.com/self-service/category/air/api-doc/airport-nearest-relevant){:target="\_blank"}
* [Airport & City Search](https://developers.amadeus.com/self-service/category/air/api-doc/airport-and-city-search){:target="\_blank"}
* [Hotel Search v2](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search){:target="\_blank"} 
* [Flight Most Travelled Destinations](https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-traveled-destinations){:target="\_blank"}
* [Flight Most Booked Destinations](https://developers.amadeus.com/self-service/category/air/api-doc/flight-most-booked-destinations){:target="\_blank"}

## Accessing paginated results

### Using SDKs

[Amadeus for Developers SDKs](https://github.com/amadeus4dev){:target="\_blank"} make it simple to access paginated results. If the API endpoint supports pagination, you can get page results using the the `.next`, `.previous`, `.last` and
`.first` methods.

Example in `Node`:

```javascript
amadeus.referenceData.locations.get({
  keyword: 'LON',
  subType: 'AIRPORT,CITY'
}).then(function(response){
  console.log(response.data); // first page
  return amadeus.next(response);
}).then(function(nextReponse){
  console.log(nextReponse.data); // second page
});
```

If a page is not available, the response will resolve to `null`.

The same approach is valid for other languages, such as `Ruby`:

```ruby
response = amadeus.reference_data.locations.get(
  keyword: 'LON',
  subType: Amadeus::Location::ANY
)
amadeus.next(response) #=> returns a new response for the next page
```

In this case, the method will return `nil` if the page is not available.

### Manually parsing the response

The response will contain the following `JSON` content:

```javascript
{
  "meta": {
     "count": 28,
     "links": {
        "self": "https://api.amadeus.com/v1/reference-data/locations/airports?latitude=49.0000&longitude=2.55",
        "next": "https://test.api.amadeus.com/v1/reference-data/locations/airports?latitude=49.0000&longitude=2.55&page%5Boffset%5D=10",
        "last": "https://test.api.amadeus.com/v1/reference-data/locations/airports?latitude=49.0000&longitude=2.55&page%5Boffset%5D=18"
     }
  },
  "data": [
     {
       /* large amount of items */
     }
  ]
}
```

You can access the next page of the results using the value of `meta/links/next` or
`meta/links/last` node within the JSON response.

Note that indexing elements between pages is done via the `page[offset]` query
parameter. For example, `page[offset]=18`. The `next` and `last` returned in the example above encode the special characters `[]` as `%5B` and `%5D`. This is called [percent
encoding](https://en.wikipedia.org/wiki/Percent-encoding){:target="\_blank"} and is used to
encode special characters in the url parameter values.