# Pagination

Sometimes, when you’re making calls to the [Amadeus for
Developers](http://developers.amadeus.com) REST APIs, there will be a lot of
results to return. Let’s say your initial call is asking for all the flight
offers using the [Flight Offers Search
API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search);
the result could be a massive response with hundreds of pages. Don’t panic.
Pagination comes to the rescue, splitting the results into different pages to
make sure responses are easier to handle.

{% hint style="danger" %}
Please be aware that no all APIs support pagination. Don't forget to check the API reference!
{% endhint %}

## Accessing the paginated results

### Using the SDKs

If you are using any of our [SDKs](https://github.com/amadeus4dev), accessing
the paginated results is very simple. If an API endpoint supports pagination,
the other pages are available under the `.next`, `.previous`, `.last` and
`.first` methods.

Let's see the following example written on `node`:

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

In this case, the method will return `nil` in case we try to reach a non existing page.

### Manually parsing the response

The response received from the server, will contain the following `JSON` content:

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

Accessing the page of the results means to access the `meta/links/next` or
`meta/links/last` node within the JSON response.

Note that indexing elements between pages is done via `page[offset]` query
parameter, such as `page[offset]=18`. The `next` and `last` returned on the
example, encodes the special characters `[]` as `%5B` and `%5D`. This is called [percent
encoding](https://en.wikipedia.org/wiki/Percent-encoding) and is used in
encoding special characters in the url parameter values.

