---
description: >-
  On this section you'll learn how to install the SDK using pip under a
  semi-isolated environment.
---

# Installation

The Python SDK has been uploaded to the official [Python package repository](https://pypi.org/project/amadeus/), which makes life easier since you can install the SDK as a regular Python package.

{% hint style="info" %}
Although the SDK works fine with Python 2.7 or 3.4+, we recommend using 3.5 or higher if possible.
{% endhint %}

It is highly recommended to use [virtualenv](https://virtualenv.pypa.io/en/latest/) when installing packages for your local projects. There are several beneficts of creating isolated environment, but the most interesting one is to avoid conflicts between different versions of the same package. 

The tool can be easily installed using `pip`:

```text
pip install virtualenv
```

Next step is to create the environment. Switch to your project repository and type:

```text
virtualenv venv
```

A new folder `venv` will be created with everything necessary inside. Let's activate the isolated environment with the following command:

```text
source venv/bin/activate
```

From now on, all packages installed using `pip` will be located under `venv/lib` and not on your global `/usr/lib` folder.

Finally, install the Amadeus SDK as follows:

```text
pip install amadeus
```

You can also add it to your `requirements.txt` file and install using:

```text
pip install -r requirements.txt
```

The virtual environment can be disabled by typing:

```text
deactivate
```

