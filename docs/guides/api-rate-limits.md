# Rate limits

Most Amadeus for Developers Self-Service APIs have rate limits in place to protect against abuse by third-parties. The rate limits for each environment are detailed in the following table:

| `Test` | `Production` |
| :--- | :--- |
| 10 transactions per second, per user | 40 transactions per second, per user  |
| No more than 1 request every 100ms. | |

Note that the following APIs are currently limited to 20 transactions per second and no more than 1 request every 50ms:

### Destination content
- Safe Place
- Points of Interest
- Location Score
- Tours and Activities

### Covid-19 and travel safety
- Travel Restrictions

### Air
- Airport On-time Performance
- Flight Price Analysis 
- Flight Choice Prediction
- Flight Delay Prediction

### Trip
- Trip Purpose Prediction
- Travel Recommendations