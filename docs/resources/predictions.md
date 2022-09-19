# Predictions

## Flight Delay Prediction API

We used historical flight delay data to train a machine learning model to predict whether a flight will be on time or delayed.

Calling the API is simple. You need to input basic information about the
flight, including the carrier, airports and flight number to begin calling. Check
out our API reference page to see the swagger with all the parameters.

Here’s an example for a flight from Frankfurt to Brussels:

```bash
curl https://test.api.amadeus.com/v1/travel/predictions/flight-delay?originLocationCode=BRU&destinationLocationCode=FRA&departureDate=2022-11-14&departureTime=11:05:00&arrivalDate=2022-11-14&arrivalTime=12:10:00&aircraftCode=32A&carrierCode=LH&flightNumber=1009&duration=PT1H05M
```

The API will return four possible delay categories:

```text
    LESS_THAN_30_MINUTES
    BETWEEN_30_AND_60_MINUTES
    BETWEEN_60_AND_120_MINUTES
    OVER_120_MINUTES_OR_CANCELLED
```

The API returns the corresponding probability of each delay length, so you’ll know the statistical likelihood of each delay occurring.

Ready to see the results of the flight to Brussels? Here’s the output: 

```json
"data": [
        {
            "id": "TK1816NCEIST20200801",
            "probability": "0.13336977",
            "result": "LESS_THAN_30_MINUTES",
            "subType": "flight-delay",
            "type": "prediction"
        },
        {
            "id": "TK1816NCEIST20200801",
            "probability": "0.42023364",
            "result": "BETWEEN_30_AND_60_MINUTES",
            "subType": "flight-delay",
            "type": "prediction"
        },
        {
            "id": "TK1816NCEIST20200801",
            "probability": "0.34671372",
            "result": "BETWEEN_60_AND_120_MINUTES",
            "subType": "flight-delay",
            "type": "prediction"
        },
        {
            "id": "TK1816NCEIST20200801",
            "probability": "0.09968289",
            "result": "OVER_120_MINUTES_OR_CANCELLED",
            "subType": "flight-delay",
            "type": "prediction"
        }
    ]
```
As you can see, the algorithm returns a 42.7% chance of a two-hour delay or
eventual cancellation. Knowing this now, would you still make the decision to
book the flight? We created this API because we want to empower travelers to
make that choice.

## Airport On-Time Performance

The Airport On-Time Performance API estimates the percentage of an airport’s
flights that will leave on time. We’ve harnessed Amadeus historical data to
predict the best airports for an speedy, stress-free flight. Give users
meaningful context and empower them to make better choices about connecting
flights and departure airports.

## Trip Purpose Prediction

The Trip Purpose Prediction API predicts whether a flight search is for
business or leisure. Our machine-learning models have detected which patterns
of departure and arrival cities, flight dates and search dates are associated
with business and leisure trips. Understand why your users are traveling
and show them the flights, fares and ancillaries that suit them best.

