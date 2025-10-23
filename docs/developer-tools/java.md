---
title: Java SDK Tutorial
---

# Java

## Java SDK

Amadeus Java SDK for the Self-Service APIs is available as a `Maven` dependency, which the Amadeus for Developers team is continuously updating as the new APIs and features get released.

You can refer to the [Amadeus Java SDK](https://github.com/amadeus4dev/amadeus-java){:target="\_blank"} or [Amadeus Maven dependency](https://mvnrepository.com/artifact/com.amadeus/amadeus-java){:target="\_blank"} for the detailed changelog.

### Installation

The SDK can be easily installed using your preferred build automation tool, such as `Maven` or `Gradle`:

#### Maven

```xml
<dependency>
  <groupId>com.amadeus</groupId>
  <artifactId>amadeus-java</artifactId>
  <version>7.0.0</version>
</dependency>
```

#### Gradle

```
compile "com.amadeus:amadeus-java:7.0.0"
```

**Further information:**

You can check the library in the [Maven repository](https://mvnrepository.com/artifact/com.amadeus/amadeus-java/latest){:target="\_blank"} for futher information.

### Step-by-step example

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

Let's do something cool by calling one of our [Flight Search APIs](https://developers.amadeus.com){:target="\_blank"} from your Java code.

To help you get started, we have created a small [Maven skeleton](https://github.com/amadeus4dev/amadeus-java-getting-started){:target="\_blank"} that is ready to use. 

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

Before testing the example, export your credentials in your terminal:

```bash
export AMADEUS_CLIENT_ID=YOUR_CLIENT_ID
export AMADEUS_CLIENT_SECRET=YOUR_CLIENT_SECRET
```

Let's build and run the code to make sure that everything is working properly:

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

As you see in the example, the main method 
instantiates an Amadeus object, taking the credentials from the following
environment:

```java
Amadeus amadeus = Amadeus.builder(System.getenv()).build();
```

In order to use the method `amadeus.shopping.flightDestinations.get()`,
you need to pass a `Params` object as in the below example:


```java
Params params = Params.with("origin", "MAD");
FlightDestination[] flightDestinations = amadeus.shopping.flightDestinations.get(params);
```

The method `amadeus.shopping.flightDestinations.get()` will return an Array with the results:

```java
System.out.println(flightDestinations[0]);
```

Now that you've tried out this example and know how to use the objects, you can review the [Javadocs](https://amadeus4dev.github.io/amadeus-java/){:target="\_blank"} in this
SDK and discover new ways to use it.

### Video Tutorial

You can also check the video tutorial on how to get started with the Java SDK.

![type:video](https://www.youtube.com/embed/qCBj_mDkDjc)

### Managing API rate limits

[Amadeus Self-Service APIs](https://developers.amadeus.com/self-service){:target="\_blank"} have [rate limits](../api-rate-limits.md){:target="\_blank"} in place to protect against abuse by third parties. You can find Rate limit example in Java using the Amadeus Java SDK [here](https://github.com/amadeus4dev-examples/APIRateLimits/tree/master/Java){:target="\_blank"}. 
