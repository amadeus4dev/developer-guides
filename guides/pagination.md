# Understanding Pagination

Sometimes, when you’re making calls to the [Amadeus for
Developers](http://developers.amadeus.com) REST APIs, there will be a lot of
results to return. Let’s say your initial call is asking for all the flight
offers using the `Flight Low-fare Search` API; the result could be a massive
response with hundreds of pages. Don't panic. Pagination comes to the rescue,
splitting the results into different pages to make sure responses are easier to
handle.

 
### Accessing the paginated results

#### Using the SDKs

If you are using any of our [SDKs](https://github.com/amadeus4dev), accessing
the paginated results is very simple.  If an API endpoint supports pagination,
the other pages are available under the `.next`, `.previous`, `.last` and
`.first` methods.

Let's see the following example written on `node`:

```js
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

#### Manually parsing the response

The responses are received with the following `JSON` content:
 
```json

"data": [
    {

      "type": "flight-offer",
       "id": "12345",
       "items": []
    }
   ]
},
"meta": {
    "links": {
        "page2": {
          "https://test.api.amadeus.com/v1/endpoint?param=value"
         }
     }
}
```

Accessing the page of the results means to access the `meta/links/page2` node
within the `JSON` response.


