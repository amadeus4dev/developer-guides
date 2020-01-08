---
description: >-
  All examples are based on AdoptOpenJDK version 8, so let's see how to install
  it.
---

# Set up the environment

## Java JDK Installation

### Linux / Windows

Go to [AdoptOpenJDK website](https://adoptopenjdk.net/) and download the tarball \(Version 8 at the time of writting this\).

Make sure the new Java installation is the default Java in your system:

* Extract the `.tar.gz`.
* Add `bin` directory to your PATH environment.
* Export a new `JAVA_HOME` environment variable pointing to the directory where Java has been installed.
* Check that Java has installed correctly

```text
java -version
```

{% hint style="info" %}
On Linux, use `update-alternatives --config java` whenever is possible.
{% endhint %}

### macOS

We recommend to use **brew** if possible. If you haven't installed brew already [install it!](http://brew.sh/)  Then install **Java** as follows:

```bash
brew cask uninstall java
brew tap adoptopenjdk/openjdk
brew cask install adoptopenjdk8
```

## Gradle

Managing a Java project and its dependencies manually could be an exhausting task if you don't use the proper tools or IDEs \(Eclipse, NetBeans, IntelliJ...\). This tutorial is meant to be followed using command line. This will give us a better understanding about what's going on beneath any IDE.

There are several tools which makes us life eaiser. The most interesting ones are [Gradle](https://gradle.org/) and [maven](https://maven.apache.org/).

Although our [Java SDK](https://github.com/amadeus4dev/amadeus-java) supports both `Gradle` and `maven`, for our example we are going to use `Gradle`. Let's see how it works.

### Installation

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

