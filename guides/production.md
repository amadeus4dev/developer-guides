# Moving to Production Guide

## What is this?

Once you feel that your application is ready to be used in the Real World™, you
might consider moving it to the __Production Environment__.

## Requesting the production keys

Moving your application to Production Environment means requesting a
__production keys__. But don't be scared! The process is quite easy:

1. [Sign in](https://developers.amadeus.com/login)
2. Click on your username (top right corner)
3. Go to [My Self-Service Workspace](https://developers.amadeus.com/my-apps)
4. Select the application you want to move to Production and click on `Get Production environment` button:

![request_prod](../images/request_production_key.png)

The __get production environment__ move involves the completion of three steps:

1. Personal and application information.
2. Payment method: credit card or bank transfer.
3. Sign the agreement and confirm.

Once you have completed the steps above, you will receive a copy of your contract by mail.

At this point your application's tag changes to __pending__:

![pending](../images/app_pending.png)

Once the validation is successful you will be notified and the app's tag will change to __live__:

![live](../images/app_live.png)

> The process to get the production key can take up to 72 hours for the first application. Additional applications do __not__ require any waiting time.

Remember that once you reach the threshold of free transactions, you will be
automatically billed on a monthly basis. But don’t worry we made this easy for
you, you can manage your apps and track your usage in [My
Self-Service](https://developers.amadeus.com/my-apps) Workspace.

## Using the new production keys

Once It's time to adapt your source code to target the new production environment, which basically means:

- Point your calls to target the production URL.
- Use the production keys when authenticating.

If you are using our [SDKs]('https://github.com/amadeus4dev'), just initialise the client as follows:

```python

amadeus = Client(client_id='YOUR_PRODUCTION_CLIENT_ID',
                 client_secret='YOUR_PRODUCTION_CLIENT_SECRET',
                 hostname='production')
```

For any other implementation, replace the base URL in your API calls to point
to `https://api.amadeus.com` and send your recently received `API key` and `API
Secret` when you perform the authentication. 

Congrats! Your application is ready to disrupt the travel industry!
