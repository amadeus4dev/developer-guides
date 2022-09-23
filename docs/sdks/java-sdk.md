# Java SDK

Amadeus Java SDK for Self-service APIs is available as a `Maven` dependency
which the Amadeus for Developers team is continuously updating as the new APIs and features get released.

You can refer to the [Amadeus Java SDK](https://github.com/amadeus4dev/amadeus-java) or [Amadeus Maven dependency](https://mvnrepository.com/artifact/com.amadeus/amadeus-java) for the detailed changelog.

## Installation

The SDK can be easily installed using your preferred build automation tool, such as `Maven` or `Gradle`:


### Maven

```xml
<dependency>
  <groupId>com.amadeus</groupId>
  <artifactId>amadeus-java</artifactId>
  <version>6.3.0</version>
</dependency>
```

### Maven

```
compile "com.amadeus:amadeus-java:6.3.0"
```

**Further information:**

- https://mvnrepository.com/artifact/com.amadeus/amadeus-java/latest

## Step-by-step example

This tutorial will guide you through the process of creating a simple Java
application which calls the Flight Inspiration Search API using the Amadeus
for Developers Java SDK.

### Using the Amadeus Java SDK

For this tutorial we will use Unix-based commands. Windows has similar commands for each task.

The requirements to follow this tutorial include:

* Your favorite editor
* Java installed
* A build automation tool, such as `Maven`
* Amadeus for Developers API key

Let's do something cool by calling one of our [Flight Search APIs](https://developers.amadeus.com) from your Java code.

To help you get started, we have created a small [Maven skeleton](https://github.com/amadeus4dev/amadeus-java-getting-started) that is ready to use. 

Let's create a class `FlightSearch.java` in the package `edu.amadeus.sdk` with the following content:

```java
package edu.amadeus.sdk;

import com.amadeus.Amadeus;
import com.amadeus.Params;

import com.amadeus.exceptions.ResponseException;

import com.amadeus.shopping.FlightDestinations;
import com.amadeus.resources.FlightDestination;

public class FlightSearch {
    public static void main(String[] args) throws ResponseException {
        Amadeus amadeus = Amadeus.builder(System.getenv()).build();

        Params params = Params.with("origin", "MAD");

        FlightDestination[] flightDestinations = amadeus.shopping.flightDestinations.get(params);

        if (flightDestinations[0].getResponse().getStatusCode() != 200) {
            System.out.println("Wrong status code for Flight Inspiration Search: " + flightDestinations[0].getResponse().getStatusCode());
            System.exit(-1);
        }

        System.out.println(flightDestinations[0]);
    }
}
```

but before testing the example, export your credentials in your terminal:

```bash
export AMADEUS_CLIENT_ID=YOUR_CLIENT_ID
export AMADEUS_CLIENT_SECRET=YOUR_CLIENT_SECRET
```

Let's build and run the code to see that everything is working properly:

```bash
./mvnw compile exec:java -Dexec.mainClass="edu.amadeus.sdk.FlightSearch"

[INFO] Scanning for projects...
[INFO] 
[INFO] ------------< edu.amadeus.sdk:amadeus-java-getting-started >------------
[INFO] Building amadeus-java-getting-started 0.1.0-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- maven-resources-plugin:2.6:resources (default-resources) @ amadeus-java-getting-started ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] Copying 1 resource
[INFO] 
[INFO] --- maven-compiler-plugin:3.8.1:compile (default-compile) @ amadeus-java-getting-started ---
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 2 source files to /amadeus-java-getting-started/target/classes
[INFO] 
[INFO] --- exec-maven-plugin:3.0.0:java (default-cli) @ amadeus-java-getting-started ---
FlightDestination(type=flight-destination, origin=MAD, destination=OPO, departureDate=Mon Oct 03 00:00:00 CEST 2022, returnDate=Tue Oct 18 00:00:00 CEST 2022, price=FlightDestination.Price(total=41.81))
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  4.407 s
[INFO] Finished at: 2022-09-19T12:36:39+02:00
[INFO] ------------------------------------------------------------------------
```

If you observe in the example, the main method, 
instantiate an Amadeus object, taking the credentials from the 
environment:

```java
Amadeus amadeus = Amadeus.builder(System.getenv()).build();
```

In order to use the method `amadeus.shopping.flightDestinations.get()`
you need to pass a `Params` object like the example:


```java
Params params = Params.with("origin", "MAD");
FlightDestination[] flightDestinations = amadeus.shopping.flightDestinations.get(params);
```

The method `amadeus.shopping.flightDestinations.get()` will return an Array with the results:

```java
System.out.println(flightDestinations[0]);
```

If you experimented with this example, and you understood
how to use the objects, you could review the [Javadocs](https://amadeus4dev.github.io/amadeus-java/) from this
SDK and learn new ways to use it.
