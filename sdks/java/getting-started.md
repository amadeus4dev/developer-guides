---
description: >-
  This tutorial will guide you through the process of creating a simple Java
  application which calls the Flight Inspiration Search API using the Amadeus
  for Developers Java SDK
---

# Step-by-step example

## Using the Amadeus Java SDK

{% hint style="info" %}
For this tutorial we will use Unix-based commands. Windows has similar commands for each.

The requirements to follow this tutorial are the following:

* Your favorite editor
* Java correctly installed \(see previous section\)
* gradle
* Amadeus for Developers API key
{% endhint %}

Let's do something cool by calling one of our [Flight Search APIs](https://developers.amadeus.com) from your Java code.

Let's start by creating a new folder `AmadeusTest` on your `$HOME` directory. Switch to this new folder and create a subdirectory structure that will host our project:

```bash
mkdir -p src/main/java/flightsearch
```

Create a new file called `FlightSearch.java` inside `src/main/java/flightsearch` with the following content:

```java
package flightsearch;

public class FlightSearch {
  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}
```

Go back to the root folder `AmadeusTest` and initialize your project using `gradle`:

```bash
gradle init
```

You'll notice a few new files in your root folder. You can freely add them to your version control system so everyone can build it just the same way.

Edit the `build.gradle` file with your favorite editor and add:

```java
apply plugin: 'java'
apply plugin: 'application'

mainClassName = 'flightsearch.FlightSearch'
```

> Note that `mainClassName` must be fully qualified class name.

Let's build and run the source using the `gradlew` wrapper script that `Gradle` has just created:

```bash
./gradlew run

> Task :run
Hello World

BUILD SUCCESSFUL in 2s
2 actionable tasks: 2 executed
```

The `run` argument is a task. Each project includes a collection of tasks, each of which performs a basic operation. `Gradle` comes with a set of predefined tasks that could be extended using an API. Managing tasks is out of the scope of this tutorial, but you can find more information about how to extend and configure tasks on [Gradle documentation](https://guides.gradle.org/).

{% hint style="info" %}
Note that a new folder `build/libs` has been created containing the `jar` file of your project.
{% endhint %}

Now that we have our skeleton ready, let's extend it to implement a call to the [Flight Inspiration Search API](https://developers.amadeus.com/self-service/category/air/api-doc/flight-inspiration-search).

According to the [Java SDK](https://github.com/amadeus4dev/amadeus-java) documentation, we need to update our `build.gradle` file to include the following dependencies:

```java
compile 'com.google.code.gson:gson:2.8.5'
compile "com.amadeus:amadeus-java:3.3.0"
```

Our `build.gradle` will look like:

```java
apply plugin: 'java'
apply plugin: 'application'

sourceCompatibility = 1.8
targetCompatibility = 1.8

dependencies {
    compile 'com.google.code.gson:gson:2.8.5'
    compile 'com.amadeus:amadeus-java:3.3.0'
}

repositories { maven { url "https://jcenter.bintray.com" } }

jar {
    baseName = 'flightSearch'
    version =  '0.1.0'
}

mainClassName = 'flightsearch.FlightSearch'
```

Note that we have added `repositories` section in order to retrieve the jar files automatically during the `build` task.

It's time to call the APIs from our Java sample! Edit the `FlightSearch.java` file and add the necessary imports:

```java
import com.amadeus.Amadeus;
import com.amadeus.Params;
import com.amadeus.exceptions.ResponseException;
import com.amadeus.shopping.FlightDestinations;
import com.amadeus.resources.FlightDestination;
```

Add the SDK initialization right after the `main` class replacing "_CLIENT\_ID_" and "_CLIENT\_SECRET_" with the real values of your `client id` and `client secret`:

```java
    Amadeus amadeus = Amadeus
            .builder("CLIENT_ID","CLIENT_SECRET")
            .build();
```

Finally call the API and print out the first result of the . This call will retrieve the best offers departuring from Madrid as of today. See how the `get` method of `flightDestinations` object returns a list of `FlightDestination` objects:

```java
FlightDestination[] flightDestinations = amadeus.shopping.flightDestinations.get(
                                                      Params.with("origin", "MAD")
                                                     );
```

The complete sample file looks like this:

```java
import com.amadeus.Amadeus;
import com.amadeus.Params;

import com.amadeus.exceptions.ResponseException;

import com.amadeus.shopping.FlightDestinations;
import com.amadeus.resources.FlightDestination;

public class FlightSearch {
  public static void main(String[] args) throws ResponseException {
    Amadeus amadeus = Amadeus
            .builder("CLIENT_ID","CLIENT_SECRET")
            .build();

    FlightDestination[] flightDestinations = amadeus.shopping.flightDestinations.get(Params.with("origin", "MAD"));

    if (flightDestinations[0].getResponse().getStatusCode() != 200) {
        System.out.println("Wrong status code for Flight Inspiration Search: " + flightDestinations[0].getResponse().getStatusCode());
        System.exit(-1);
    }

    System.out.println(flightDestinations[0]);
  }
}
```

Let's build and run the code to see that everything is working properly \(the output has been splitted into different lines for clarity\):

```bash
./gradlew run

> Task :run
FlightDestination(type=flight-destination, 
origin=MAD,
destination=BIO,
departureDate=Sat Nov 17 00:00:00 CET 2018,
returnDate=Wed Nov 21 00:00:00 CET 2018,
price=FlightDestination.Price(total=92.26))
```

