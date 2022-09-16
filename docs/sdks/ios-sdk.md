# iOS SDK 

The [Amadeus iOS SDK](https://github.com/amadeus4dev/amadeus-ios) makes it easy to develop iOS applications with flight, hotel, and other travel data from Amadeus. In this guide, you'll install the library in your environment and make your first API call.

## Prerequisites

-   Amadeus for Developers API key and API secret: to get one, [create a free developer account](https://developers.amadeus.com/register) and set up your first application in your [Workspace](https://developers.amadeus.com/my-apps).
-  The [Xcode 11.0+](https://developer.apple.com/xcode/) IDE to build apps for iOS environments. 
- Swift 5.0 or higher.

## Installation 

We recommend installing the SDK using [Swift Package Manager](https://swift.org/package-manager). To start the installation, edit the `Package.swift`  file inside the directory containing your project, and simply add `amadeus-ios` as a dependency: 

```swift
import PackageDescription 
let package = Package( 
    name: "YOUR_PROJECT_NAME", 
    dependencies: [ 
        .package(url: "https://github.com/amadeus4dev/amadeus-ios.git", from: "2.0.0"), 
    ] 
) 
```

## Getting Started 

At this point you have to create a new project on XCode by selecting `File > New > Project` in the menu and following the wizard to automatically create your project template. 

You can also use the Swift CLI toolchain to build projects from the terminal. In that case, create an executable template using the "–type" argument, as follows: 

```
$ swift package init --type=executable 
Creating executable package: amadeus-example 
Creating Package.swift 
Creating README.md 
Creating .gitignore 
Creating Sources/ 
Creating Sources/deleteme/main.swift 
Creating Tests/ 
Creating Tests/LinuxMain.swift 
Creating Tests/deletemeTests/ 
Creating Tests/deletemeTests/deletemeTests.swift 
Creating Tests/deletemeTests/XCTestManifests.swift 
```

Then edit the `Package.swift` and add `amadeus-ios` as dependency.

## Making your first API call

Now edit the `main.swift` file with the following content: 

```swift
import amadeus 
var amadeus:Amadeus = Amadeus( 
    client_id: "REPLACE_BY_YOUR_API_KEY", 
    client_secret: "REPLACE_BY_YOUR_API_SECRET" 
) 
amadeus.referenceData.airLines.get( 
        params: ["airlineCodes": "BA"], 
        onCompletion: { 
          response, error in 
            if error == nil { 
               print(response!.data) 
            } 
         }) 
```

Let's pause for a moment to take a deeper look at the code. 

After importing the Amadeus package, initialize the client by instantiating the Amadeus class. The method receives two parameters: the API key and API secret. You can also initialize the library without arguments, in which case the API key and API secret will be read from the environment variables (AMADEUS_CLIENT_ID and AMADEUS_CLIENT_SECRET).  The library will manage the authentication process and the renewal of the token, so you won't have to worry about that anymore. 

Once you’ve created the client, you’re ready to perform an API call. The SDK uses namespaced methods to create a match between the API and the SDK. As this example uses the Airline Code Lookup API, the call will be implemented as `referenceData.Airlines`, followed by the method to retrieve the data (in this case, a GET).

The `get()` method receives two arguments: 

- A Swift dictionary (`params`) with both key (airlineCodes) and value (BA) as Strings. This represents the API query parameters. 

- A Swift Closure (`onCompletion`) which is automatically called once the API response is received and parsed. If you’re not sure what a Closure is, keep reading! 

Finally, the body of the Closure implements the logic once the response is received and parsed. A closure is basically a function which is automatically called (callback) and returns some values. This one returns two values: response, which contains the body (JSON) of the API response; and error, which contains the error code of the petition or points to nil if the API call returns a 200 code. 

Build and run the project using Xcode or use the following commands if you are using the Swift toolchain in console: 

```
$ swift build 
$ swift run 
``` 

The example finishes with the print of the JSON response: 

```json
{ 
    "type": "airline", 
    "iataCode": "BA", 
    "icaoCode": "BAW", 
    "businessName": "BRITISH AIRWAYS", 
    "commonName": "BRITISH A/W" 
} 
```

The iOS SDK uses methods to map every API path to a similar path. For example, `GET /v2/reference-data/urls/checkin-links?airline=BA` would be: 

```swift
amadeus.referenceData.urls.checkinLinks.get(params: ["airlineCode": "BA"], onCompletion: { 
   (data,error) in 
   ... 
 }) 
``` 

Similarly, to select a resource by ID, you can pass in the Id to the singular path. For example, `GET /v2/shopping/hotel-offers/XZY` would be: 

```swift
amadeus.shopping.hotelOffer(hotelId: "XZY").get(params:[:], 
          onCompletion: { 
             (data,error) in 
             ... 
  }) 
``` 

You can also make any arbitrary API call using the .get or .post methods. This is useful for calling a new API which is not yet supported by the SDK:

```swift
amadeus.get(path:'/v2/reference-data/urls/checkin-links', 
              params: ["airlineCode":"BA"], onCompletion: { 
                (data,error) in 
                 .... 
    }) 
```

## Handling the responses

Responses are based on [Swift closures](https://docs.swift.org/swift-book/LanguageGuide/Closures.html), which are self-contained blocks of functionality that can be passed around and used in your code. They are automatically called once an event occurs and they’re how the SDK implements asynchronous API calls. 

Every API call contains an `OnCompletion` closure as the last argument. The closure contains two values: response and error. 

The response object contains the JSON response from the API call as well as the http status code: 

```swift
amadeus.shopping.flightDestinations.get(params: ["origin": "MAD", "maxPrice": "10000"], onCompletion: { 
    response,error in 
      print(response!.body)       // => The raw response, as a string 
      print(response!.data)       // => JSON data field extracted from the JSON 
      print(response!.result)     // => The body parsed as JSON 
      print(response!.statusCode) // => HTTP Status code 
}) 
``` 

The error contains an enum value representing the error (if any) or nil in case the request was successfully executed. The following are the possible error values: 

```swift
public enum ResponseError: Error { 
    case badRequestError(String) // 400 - the client did not provide the right parameters 
    case authenticationError // 401 - the client did not provide the right credentials 
    case forbiddenError // 403 - access an invalid endpoint 
    case notFoundError // 404 - the path could not be found 
    case tooManyRequestsError // 429 - too many requests 
    case internalServerError // 500 - there is an error on the server 
    case unknownStatusCode(Int) // unknown http code 
    case returnedError(Error) // non http error 
    case invalidInputJSON // invalid JSON in the request 
    case malformedURL // invalid http request format 
} 
``` 

Of course, if the API call returns error, the response will contain the body of the error response ready to be parsed. 