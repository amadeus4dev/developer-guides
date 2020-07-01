# Java SDK

Java usually refers to the programming language but also to the platform: a set
of tools -virtual machine, compiler and libraries- which allow developers to
create cross-platform applications.

## OpenJDK? Oracle JDK? help!

Despite the complexity of the Java ecosystem, it's important to understand that there is only one set of source code for the JDK released under GPL license and hosted at [OpenJDK](http://openjdk.java.net/projects/jdk/). You can always follow [these instructions](http://hg.openjdk.java.net/jdk9/jdk9/raw-file/tip/common/doc/building.html) to compile and generate your own JDK flavor.

Different vendors build the OpenJDK adding additional tools, utilities or branding elements, but never modifying the language. As result the vendor provides a new build with some unique vendor capabilities or certification processes.

There are many JDK implementations out there, but the most used ones are:

* [OpenJDK](http://jdk.java.net/). Oracle GPL license unbranded builds of the OpenJDK.
* [Oracle JDK](http://www.oracle.com/technetwork/java/javase/downloads/). Branded builds from Oracle that could be used without cost.

There are more implementations like [Zulu](https://www.azul.com/downloads/zulu/), [IBM JDK](https://developer.ibm.com/javasdk/support/lifecycle/), [Red Hat](https://developers.redhat.com/products/openjdk/overview/) or [AdoptOpenJDK](https://adoptopenjdk.net/).

If you want to switch seamessly between flavors and versions, we recommend you to take a look to the  [sdkman](https://sdkman.io/) tool.

## Installation

The SDK can be installed by adding a `Gradle` dependency or `Maven` dependency, or by cloning the source into a project. Additionally it can be installed by downloading one of the precompiled JARs from the releases page on [GitHub](https://github.com/amadeus4dev/amadeus-java).

### Maven

```xml
<dependency>
  <groupId>com.amadeus</groupId>
  <artifactId>amadeus-java</artifactId>
  <version>3.3.0</version>
</dependency>
```

### Gradle

```java
compile "com.amadeus:amadeus-java:3.3.0"
```

## Setting up the environment

### Java JDK Installation

#### Linux / Windows

Go to [AdoptOpenJDK website](https://adoptopenjdk.net/) and download the tarball \(Version 8 at the time of writting this\).

Make sure the new Java installation is the default Java in your system:

* Extract the `.tar.gz`.
* Add `bin` directory to your PATH environment.
* Export a new `JAVA_HOME` environment variable pointing to the directory where Java has been installed.
* Check that Java has installed correctly

```bash
java -version
```

!!!information
    On Linux, use `update-alternatives --config java` whenever is possible.

#### macOS

We recommend to use **brew** if possible. If you haven't installed brew already [install it!](http://brew.sh/)  Then install **Java** as follows:

```bash
brew cask uninstall java
brew tap adoptopenjdk/openjdk
brew cask install adoptopenjdk8
```

### Gradle

Managing a Java project and its dependencies manually could be an exhausting task if you don't use the proper tools or IDEs \(Eclipse, NetBeans, IntelliJ...\). This tutorial is meant to be followed using command line. This will give us a better understanding about what's going on beneath any IDE.

There are several tools which makes us life eaiser. The most interesting ones are [Gradle](https://gradle.org/) and [maven](https://maven.apache.org/).

Although our [Java SDK](https://github.com/amadeus4dev/amadeus-java) supports both `Gradle` and `maven`, for our example we are going to use `Gradle`. Let's see how it works.

#### Installation

Go ahead and install Gradle following the [instructions](https://gradle.org/install/) from the website. Make sure the `gradle` tool belongs to your `PATH` variable.

To test the Gradle installation, run `gradle` from the command line:

```text
gradle

Welcome to Gradle 4.10.2!

Here are the highlights of this release:
 - Incremental Java compilation by default
 - Periodic Gradle caches cleanup
 - Gradle Kotlin DSL 1.0-RC6
 - Nested included builds
 - SNAPSHOT plugin versions in the `plugins {}` block

For more details see https://docs.gradle.org/4.10.2/release-notes.html
```


## Step-by-step example

This tutorial will guide you through the process of creating a simple Java
application which calls the Flight Inspiration Search API using the Amadeus
for Developers Java SDK

### Using the Amadeus Java SDK

For this tutorial we will use Unix-based commands. Windows has similar commands for each.

The requirements to follow this tutorial are the following:

* Your favorite editor
* Java correctly installed \(see previous section\)
* gradle
* Amadeus for Developers API key

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

!!! information
    Note that a new folder `build/libs` has been created containing the `jar` file of your project.

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

```java hl_lines="3 4"
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
