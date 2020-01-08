---
description: >-
  This tutorial will guide you through the process of creating a simple Python
  application which calls the Flight Inspiration Search API using the Amadeus
  for Developers Python SDK
---

# Step-by-Step example

## Requests

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

## Pretty printing the response



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

