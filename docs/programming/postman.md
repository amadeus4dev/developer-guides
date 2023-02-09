# Self-Service API Postman collection

Follow this tutorial to test Amadeus Self-Service APIs using our dedicated Postman collection.

## Pre-requisites

Before you begin, you need to:

* Register your application with Amadeus for Developers as described in [Making your first API call](./quick-start.md).
* Create a new Postman account or use your existing Postman account.

## Fork the collection

1. Login to Postman.
2. Navigate to the Amadeus for Developers [public workspace](https://www.postman.com/amadeus4dev/workspace/amadeus-for-developers-s-public-workspace/documentation/2672636-27471449-d2ca-a8c4-1399-6b0cfbddd079).
    ![1](images/postman-1.png)
3. Click **Fork**.
    ![2](images/postman-2.png)
4. Select **Amadeus for Developers** from the **Environment** dropdown.
5. Give the fork a name.
6. Select the workspace where you need to fork the collection to.
7. Tick the **Watch original collection** box to get notified when the collection is updated.
8. Click **Fork collection**. You will be taken to the workspace that you selected previously.

## Generate the access token

1. In the navigation side bar, go to **Amadeus for Developers > Authorization > Access Granted Client Credentials>**.
2. Open the **Body** tab.
    ![3](images/postman-3.png)
3. Enter you [API key and secret values](../API-Keys/) into the `client_id` and `client_secret` parameters respectively.
4. Click **Send**.
5. Take a note of the **access_token** value in the response.

!!! danger
    The token is valid for 30 minutes and you must perform the previous step every 30 minutes to generate a new access_token.

## Make API calls

1. Select the required API from the collection by navigating to the required endpoint on the left side bar.
2. Select the **Authorization** tab.
3. Select **Bearer token** from the **Type** dropdown.
    ![4](images/postman-4.png)
4. Enter the **access_token** value into the **Token** field.
    ![5](images/postman-6.png)
5. Navigate to the **Params** tab.
6. Fill out the parameters as per the [documentation](https://developers.amadeus.com/self-service) of the API.
7. Click **Send** to make the call.