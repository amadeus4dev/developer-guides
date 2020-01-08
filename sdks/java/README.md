---
description: >-
  Java usually refers to the programming language but also to the platform: a
  set of tools -virtual machine, compiler and libraries- which allow developers
  to create cross-platform applications.
---

# Java SDK

## OpenJDK? Oracle JDK? help!

Despite the complexity of the Java ecosystem, it's important to understand that there is only one set of source code for the JDK released under GPL license and hosted at [OpenJDK](http://openjdk.java.net/projects/jdk/). You can always follow [these instructions](http://hg.openjdk.java.net/jdk9/jdk9/raw-file/tip/common/doc/building.html) to compile and generate your own JDK flavor.

Different vendors build the OpenJDK adding additional tools, utilities or branding elements, but never modifying the language. As result the vendor provides a new build with some unique vendor capabilities or certification processes.

There are many JDK implementations out there, but the most used ones are:

* [OpenJDK](http://jdk.java.net/). Oracle GPL license unbranded builds of the OpenJDK.
* [Oracle JDK](http://www.oracle.com/technetwork/java/javase/downloads/). Branded builds from Oracle that could be used without cost.

There are more implementations like [Zulu](https://www.azul.com/downloads/zulu/), [IBM JDK](https://developer.ibm.com/javasdk/support/lifecycle/), [Red Hat](https://developers.redhat.com/products/openjdk/overview/) or [AdoptOpenJDK](https://adoptopenjdk.net/).

If you want to switch seamessly between flavors and versions, we recommend you to take a look to the  [sdkman](https://sdkman.io/) tool.

