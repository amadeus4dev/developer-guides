# Python SDK

## Installation

The Python SDK has been uploaded to the official [Python package
repository](https://pypi.org/project/amadeus/), which makes life easier since
you can install the SDK as a regular Python package.

!!! information
    Although the SDK works fine with Python 2.7 or 3.4+, we recommend using 3.5 or higher if possible.

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


## Set up the environment

Managing several Python versions locally could be a real pain. This guide
explains how to manage our environment to easily switch between different
Python versions using pyenv.

### Why Use `pyenv`?

`pyenv` is a wonderful tool for managing multiple Python versions. Even if you already have Python installed on your system, it is worth having `pyenv` installed so that you can easily try out new language features or help contribute to a project that is on a different version of Python.

You can find more information on the [GitHub](https://github.com/pyenv/pyenv) project repository.

### Installation

Installation couldn't be easier:

```text
curl https://pyenv.run | bash
```

This will install `pyenv` along with a few plugins that are useful:

* **`yenv`**: The actual `pyenv` application
* **`pyenv-virtualenv`**: Plugin for `pyenv` and virtual environments
* **`pyenv-update`**: Plugin for updating `pyenv`
* **`pyenv-doctor`**: Plugin to verify that `pyenv` and build dependencies are installed
* **`pyenv-which-ext`**: Plugin to automatically lookup system commands

Add the following lines to your `.bashrc` or `.zshrc` files:

```text
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### Basic Usage

`pyenv` allows to install both specific version per project and a global one. Let's install a global Python 3.6 version:

```text
pyenv install 3.6.8
```

You can check the available versions using the following command:

```text
pyenv install --list
```

Finally, check that the new version has been installed correctly:

```text
python --version

Python 3.6.8
```


## Step-by-Step example

This tutorial will guide you through the process of creating a simple Python
application which calls the Flight Inspiration Search API using the Amadeus
for Developers Python SDK

### Requests

Becoming a super hero is a fairly straight forward process:

{% hint style="info" %}
 Super-powers are granted randomly so please submit an issue if you're not happy with yours.
{% endhint %}

Once you're strong enough, save the world:

{% tabs %}
{% tab title="Python" %}
```python
from amadeus import Client, ResponseError

client = Client(
    client_id='REPLACE_BY_YOUR_API_KEY',
    client_secret='REPLACE_BY_YOUR_API_SECRET'
)

try:
    response = client.shopping.flight_destinations.get(origin='MAD')
    print(response.data)
except ResponseError as error:
    print(error)
```
{% endtab %}
{% endtabs %}

### Pretty printing the response


{% tabs %}
{% tab title="Python" %}
```python
from amadeus import Client, ResponseError
import json

client = Client(
    client_id='REPLACE_BY_YOUR_API_KEY',
    client_secret='REPLACE_BY_YOUR_API_SECRET'
)

try:
    response = client.shopping.flight_destinations.get(origin='MAD')
    print(json.dumps(response.data), ident=4)
except ResponseError as error:
    print(error)
```
{% endtab %}
{% endtabs %}
