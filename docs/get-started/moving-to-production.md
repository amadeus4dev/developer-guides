# Moving to production

Once you feel that your application is ready to be deployed to the Real World™, you will want to move it to Production Environment.

## Requesting the production keys

Moving your application to Production Environment means requesting a **production key**, but don't be scared! The process is very straight forward:

1. [Sign in](https://developers.amadeus.com/login) to your account
2. Click on your username \(top right corner\)
3. Go to [My Self-Service Workspace](https://developers.amadeus.com/my-apps)
4. Select the application that you want to move to Production and click on `Get Production environment` button:

![request_prod](../images/request_production_key.png)

Moving to **production environment** involves 3 steps:

1. Information about you and your app
2. Payment information \(credit card or bank transfer\)
3. Signing the terms and conditions \(via _DocuSign_\)

Once you have completed the steps above, you will receive a copy of your contract by email.

At this point your application's status will show **pending**:

![pending](../images/app_pending.png)

Once your application is validated you will be notified and the application's status will change to **live**:

![live](../images/app_live.png)

!!! information
    Please note that the process can take up to 72 hours for your first application. Additional applications will **not** require any waiting time.

Remember that once you reach the threshold of free transactions, you will
automatically be billed on a monthly basis, for each transaction. You can
easily manage and track your app usage in [My Self-Service
Workspace](https://developers.amadeus.com/my-apps).

## Using the new production keys

Once you get your production key, you will need to change your source code:

- Replace the base URL for your API calls to point to `https://api.amadeus.com`
instead of `https://test.api.amadeus.com`
- Change your `API key` and `API secret` with your new production keys.

If you are using our [SDKs](https://github.com/amadeus4dev), just initialise the client as follows:

    ``` python
    amadeus = Client(client_id='YOUR_PRODUCTION_CLIENT_ID',
                 client_secret='YOUR_PRODUCTION_CLIENT_SECRET',
                 hostname='production')
    ```

**Congrats**! 🎉 Your application is ready to disrupt the travel industry!
