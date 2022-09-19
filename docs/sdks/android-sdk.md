# Android SDK 

The [Amadeus Android SDK](https://github.com/amadeus4dev/amadeus-android) makes it easy to develop Android applications with flight, hotel, and other travel data from Amadeus. In this guide, you'll install the library in your environment and make your first API call.

## Prerequisites

- Amadeus for Developers API key and API secret: to get one, [create a free developer account](https://developers.amadeus.com/register) and set up your first application in your [Workspace](https://developers.amadeus.com/my-apps).
- The [Android Studio](https://developer.android.com/studio) IDE to build apps for Android applications.
- Java version 1.8 and Kotlin version 1.3.70 minimum

## Installation 

Install the`amadeus-android` SDK via Maven or Gradle 

**Maven**

```
<dependency> 
  <groupId>com.amadeus</groupId> 
  <artifactId>amadeus-android</artifactId> 
  <version>1.2.1</version> 
</dependency>
```

**Gradle**

```
implementation 'com.amadeus:amadeus-android:1.2.1' 

```

## Getting Started 

Follow the steps below to create your first app: 

- Create a new Android project with Android Studio: `File > New > New Project`. 
- In the menu, use the wizard to select `Basic Activity` to automatically create your project template.
- Name your app and your package (by default, com.example.amadeusdemo).
- Select `Kotlin`-  as your programming language and select the Minimum SDK version you want.
- Edit the `build.gradle` (Module:app) file to add `amadeus-android` as dependency.

```
dependencies { 
    implementation fileTree(dir: 'libs', include: ['*.jar']) 
    implementation 'com.amadeus:amadeus-android:1.3.1' 
... 
} 
```
## Making your first API call

Next, let's create a sample application. Create an Application class in the root package (here is`com.example.amadeusdemo` > `SampleApplication.kt`). This file will be used to instantiate the SDK: 

```kotlin
// Being in an Activity/Fragment/ViewModel or any file you want

import com.amadeus.android.Amadeus
import com.amadeus.android.ApiResult
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.launch
import android.util.Log;

val job = SupervisorJob()
val scope = CoroutineScope(Dispatchers.Main + job)

val amadeus = Amadeus.Builder(context)
    .setClientId("REPLACE_BY_YOUR_API_KEY")
    .setClientSecret("REPLACE_BY_YOUR_API_SECRET")
    .build()

scope.launch {
  when (val checkinLinks = amadeus.referenceData.airlines.get(airlineCodes = "BA")) {
    is ApiResult.Success -> {
      Log.d("Result", "${result.data}")
    }
    is ApiResult.Error -> {
      // Handle your error
    }
  }
}
```

Let's pause for a moment to take a deeper look at the code. 

After importing the Amadeus package, initialize the client by instantiating the Amadeus class. The method receives two parameters: the API key and API secret. You can also initialize the library without arguments, in which case the API key and API secret will be read from the environment variables (REPLACE_BY_YOUR_API_KEY and REPLACE_BY_YOUR_API_SECRET). The library will manage the authentication process and the renewal of the token, so you won't have to worry about that anymore. 

Once you’ve created the client, you’re ready to perform an API call. The SDK uses namespaced methods to create a match between the API and the SDK. As this example uses the Airline Code Lookup API, the call will be implemented as `referenceData.airlines`, followed by the method to retrieve the data (in this case, a GET).

As you can see, we don't throw Exceptions (except for some specific cases) in the API, but we provide a `ApiResult.Error` object with all the information you need to know. Coroutines and exceptions are not good friends, so with this abstraction, you can handle every use case you want in a safe way.

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

The SDK uses methods to map every API path to a similar path. For example, `GET /v2/reference-data/urls/checkin-links?airline=BA` would be: 

```kotlin
amadeus.referenceData.urls.checkinLinks.get(airlineCode = "BA")
``` 

Similarly, to select a resource by ID, you can pass in the Id to the singular path. For example, `GET /v2/shopping/hotel-offers/XZY` would be: 

```kotlin
amadeus.shopping.hotelOffer("XXX").get()
``` 

You can also make any arbitrary API call using the .get or .post methods. This is useful for calling a new API which is not yet supported by the SDK:

```swift
val stringResult = amadeus.get("https://test.api.amadeus.com/v1/travel/analytics/air-traffic/busiest-period?cityCode=MAD&period=2017&direction=ARRIVING")
```

## Handling the responses

The API response returns an `ApiResult` object that can be either a `Success` or an `Error` object: 

- `APIResult.Success` - contains a ready-to-use typed data value, some metadata and dictionaries. 

- `APIResult.Error` - contains the status code, error code and message of the API response. 

The `Success` object contains the JSON response from the API call as well as the HTTP status code: 

```kotlin
val checkinLinks = amadeus.referenceData.urls.checkinLinks.get(airlineCode = "LH") 
if (checkinLinks is ApiResult.Success) { 
Log.d("${checkinLinks.data}")           // => JSON data field extracted  
Log.d("${checkinLinks.meta}")           // => JSON meta data field 
Log.d("${checkinLinks.dictionaries}")   // => JSON dictionaries data field 
Log.d("${checkinLinks.code}")           // => HTTP status code 
} 
```

If the call fails, the `Error` object will contain:

```kotlin
val checkinLinks = amadeus.referenceData.urls.checkinLinks.get(thisParamDoesNotExist = "XXX") 
if (checkinLinks is ApiResult.Error) { 
Log.d("${checkinLinks.errors}")           // => JSON data of the list of errors           
} 
```