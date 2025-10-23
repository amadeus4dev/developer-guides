---
title: Hotel Booking API Migration Guide
---

Are you still using the old version of the [Hotel Booking API](https://developers.amadeus.com/self-service/category/hotels/api-doc/hotel-booking/v/1.0){:target="\_blank"}? This guide will help you migrate to the new version of the [Hotel Booking API](https://developers.amadeus.com/self-service/category/hotels/api-doc/hotel-booking/v/2.0){:target="\_blank"} and leverage its advantages right from the start.

# Endpoint Changes

The primary changes in the API endpoint involve updates to the base path and naming conventions.

| Aspect             | v1                         | v2                         | Impact                                       |
|--------------------|----------------------------|----------------------------|---------------------------------------------|
| **Base path**      | `/v1`                      | `/v2`                      | All endpoints need to be updated to `/v2`.  |
| **Primary endpoint** | `/booking/hotel-bookings` | `/booking/hotel-orders`    | New naming convention. Update all create booking calls. |

---

# Request Body Changes

The request body structure has been significantly updated in v2 to improve clarity and organization. Key changes include the reorganization of fields, the addition of new elements, and enhanced details for existing fields.

| Field      | v1                                       | v2                                                                  |
|------------|-----------------------------------------|----------------------------------------------------------------------|
| **offerId** | Present at the root level.             | Moved into `data.roomAssociations.hotelOfferId`.                   |
| **guests**  | Includes name and contact fields in a single array. | Expanded to include fields like `tid`, `title`, `firstName`, `lastName`, `phone`, and `email`. |
| **payments** | Includes `method` and `card` directly under `payments`. | Renamed `payment` and includes nested `paymentCard` object with detailed card info. |
| **rooms**    | Optional for v1 when matching the offer room quantity. | Renamed to `roomAssociations` in v2 to explicitly correlate guests and offers. |
| **travelAgent** | Not present.                       | New field in v2, containing contact information such as `email`.   |

### v1 Request Body Example

```json
{
  "data": {
    "offerId": "NRPQNQBOJM",
    "guests": [
      {
        "name": {
          "title": "MR",
          "firstName": "BOB",
          "lastName": "SMITH"
        },
        "contact": {
          "phone": "+33679278416",
          "email": "bob.smith@email.com"
        }
      }
    ],
    "payments": [
      {
        "method": "creditCard",
        "card": {
          "vendorCode": "VI",
          "cardNumber": "0000000000000000",
          "expiryDate": "2026-01"
        }
      }
    ]
  }
}
```

### v2 Request Body Example

```json
{
  "data": {
    "type": "hotel-order",
    "guests": [
      {
        "tid": 1,
        "title": "MR",
        "firstName": "BOB",
        "lastName": "SMITH",
        "phone": "+33679278416",
        "email": "bob.smith@email.com"
      }
    ],
    "travelAgent": {
      "contact": {
        "email": "bob.smith@email.com"
      }
    },
    "roomAssociations": [
      {
        "guestReferences": [
          {
            "guestReference": "1"
          }
        ],
        "hotelOfferId": "4L8PRJPEN7"
      }
    ],
    "payment": {
      "method": "CREDIT_CARD",
      "paymentCard": {
        "paymentCardInfo": {
          "vendorCode": "VI",
          "cardNumber": "4151289722471370",
          "expiryDate": "2026-08",
          "holderName": "BOB SMITH"
        }
      }
    }
  }
}
```

# Response Changes

The response structure in v2 provides enhanced details, aligning with the expanded data model. While v1 focused only on booking ID and provider confirmation, v2 offers a holistic view of the booking, including guests, room associations, policies, pricing, and more.

## Key Changes

| Aspect                | v1                                                                 | v2                                                                                                   |
|-----------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| **Root type**         | `"hotel-booking"`.                                                | `"hotel-order"`.                                                                                    |
| **Root id**           | Unique ID of the booking (e.g., `"XD_8138319951754"`).            | Unique ID of the hotel order (e.g., `"V0g2VFJaLzIwMjQtMDYtMDc="`). Essential for cancellations or retrieval. |
| **Nested Bookings**    | Not supported directly. Each hotel-booking is a top-level item.   | Nested under `hotelBookings` array in `hotel-order`. Includes room associations, policies, and price details. |
| **Booking Status**     | Not included.                                                    | Available under `bookingStatus` in each `hotelBookings` item. Values like `"CONFIRMED"` or `"PENDING"`. |
| **Provider Confirmation** | Provided as `providerConfirmationId`.                        | Included in `hotelProviderInformation` array with `hotelProviderCode` and `confirmationNumber`.      |
| **Guests**             | Not included.                                                    | Listed in `guests` array. Includes detailed info such as `title`, `firstName`, `lastName`, `phone`, and `email`. |
| **Room Associations**  | Not included.                                                    | Nested under `roomAssociations`. Maps guests to rooms and links them to `hotelOfferId`.              |
| **Hotel Details**       | Not included.                                                   | Available under `hotel`. Includes `hotelId`, `chainCode`, `name`, and a `self` link for additional details. |
| **Price Details**       | Not included.                                                   | Nested under `price` in `hotelOffer`. Provides breakdowns like base, total, taxes, and daily variations. |
| **Policies**           | Not included.                                                   | Included in `policies` under `hotelOffer`. Covers cancellations, payment type, and guarantees/deposits. |
| **Associated Records** | Flat array under `associatedRecords`.                           | Still included but now part of `hotel-order`. Adds metadata like `reference` and `originSystemCode`. |
| **Payment Information** | Not included.                                                  | Included under `payment` in `hotelBookings`. Covers method and nested `paymentCard` details.         |
| **Self-Link**          | Not included.                                                   | Provided under `self` in `hotel-order`. A direct URL to retrieve the full order details.             |

---

## Response Examples

### v1 Example
```json
{
  "data": [
    {
      "type": "hotel-booking",
      "id": "XD_8138319951754",
      "providerConfirmationId": "8138319951754",
      "associatedRecords": [
        {
          "reference": "QVH2BX",
          "originSystemCode": "GDS"
        }
      ]
    }
  ]
}
```

### v2 Example
```json
{
  "data": {
    "type": "hotel-order",
    "id": "V0g2VFJaLzIwMjQtMDYtMDc=",
    "hotelBookings": [
      {
        "type": "hotel-booking",
        "id": "MS84OTkyMjcxMC85MDIyNDU0OQ==",
        "bookingStatus": "CONFIRMED",
        "hotelProviderInformation": [
          {
            "hotelProviderCode": "AR",
            "confirmationNumber": "89922710"
          }
        ],
        "roomAssociations": [
          {
            "guestReferences": [
              {
                "guestReference": "1"
              }
            ]
          }
        ],
        "hotelOffer": {
          "type": "hotel-offer",
          "category": "TYPE_CONDITIONAL",
          "checkInDate": "2024-06-07",
          "checkOutDate": "2024-06-08",
          "guests": {
            "adults": 1
          },
          "policies": {
            "cancellations": [
              {
                "amount": "215.05",
                "deadline": "2024-06-06T23:59:00+02:00"
              }
            ],
            "paymentType": "GUARANTEE"
          },
          "price": {
            "base": "195.50",
            "currency": "EUR",
            "sellingTotal": "215.05",
            "taxes": [
              {
                "amount": "19.55",
                "code": "VALUE_ADDED_TAX",
                "currency": "EUR",
                "included": false,
                "pricingFrequency": "PER_STAY",
                "pricingMode": "PER_PRODUCT"
              }
            ],
            "total": "215.05",
            "variations": {
              "changes": [
                {
                  "endDate": "2024-06-08",
                  "startDate": "2024-06-07",
                  "base": "195.50",
                  "currency": "EUR"
                }
              ]
            }
          },
          "rateCode": "S9R",
          "room": {
            "description": {
              "lang": "EN",
              "text": "Marriott Senior Discount, includes"
            },
            "type": "XMI"
          },
          "roomQuantity": 1
        },
        "hotel": {
          "hotelId": "ARMADAIT",
          "chainCode": "AR",
          "name": "AC BY MARRIOTT HOTEL AITANA",
          "self": "https://test.travel.api.amadeus.com/v1/reference-data/locations/by-hotel/ARMADAIT"
        },
        "payment": {
          "method": "CREDIT_CARD",
          "paymentCard": {
            "paymentCardInfo": {
              "vendorCode": "VI",
              "cardNumber": "415128XXXXXX1370",
              "expiryDate": "0826",
              "holderName": "BOB SMITH"
            }
          }
        },
        "travelAgentId": "00000000"
      }
    ],
    "guests": [
      {
        "tid": 1,
        "id": 1,
        "title": "MR",
        "firstName": "BOB",
        "lastName": "SMITH",
        "phone": "+33679278416",
        "email": "bob.smith@email.com"
      }
    ],
    "associatedRecords": [
      {
        "reference": "WH6TRZ",
        "originSystemCode": "GDS"
      }
    ],
    "self": "http://test.api.amadeus.com/v2/booking/hotel-orders/V0g2VFJaLzIwMjQtMDYtMDc="
  }
}
```

# Recommendations for Migration

To migrate to the updated version of the API, you will need to reorganize request payload fields to align with the v2 model. This involves restructuring data to include elements like `roomAssociations` and `paymentCard` while also incorporating the `travelAgent` details if they are applicable to your use case.  

Error handling will need to be adapted to reflect the changes in v2. The error pointers in v2 have been updated, so you will need to map your existing error handling logic to these revised pointers.  

Thoroughly test the new integration in the Amadeus-provided test environment to ensure that your application operates as expected with the new Hotel Booking API version.  


# Use Case Inspirations

With the new capabilities of the Hotel Booking API v2, you can design more powerful travel solutions. The expanded data model, detailed pricing and policy information, and improved guest and room management open the door to innovative use cases.  

For personalized booking recommendations, pair Hotel Booking v2 with the Hotel Search API. The Hotel Search API will identify hotels that match a user’s preferences. The v2 Hotel Booking API enhances this selection by allowing you to create bookings with detailed guest profiles (`guests` object), advanced room-to-guest mapping (`roomAssociations`), and rich payment options (`paymentCard`).  

You can also combine the Hotel Booking API v2 with the Hotel Ratings API or the Hotel Name Autocomplete API. With the v2 API, the detailed `hotel` object provides precise property identifiers (`hotelId`, `chainCode`) that can be used to fetch ratings, recommendations, or additional property details for meaningful engagement even after the booking is completed.  


# FAQs

**How can I retrieve the room details or hotel information?**  
You can use the `hotel` object within the `hotelBookings` array to access basic details such as `hotelId`, `chainCode`, `name`, and a `self`-link for additional information about the hotel.  

**Can I correlate guests with rooms and offers in v2?**  
Yes! The `roomAssociations` object explicitly maps guests to rooms and links them to specific `hotelOfferIds`.  

**How do I handle new payment data?**  
The v2 API introduces a nested `paymentCard` object, which includes detailed information about the card.  

**Do I need to update error handling logic?**  
Yes, v2 has updated error pointers. Review the error response structure and adapt your error-handling mechanisms to align with the v2 model.  

**Can I access pricing breakdowns and policies for bookings?**  
Absolutely! The expanded `hotelOffer` object provides a comprehensive pricing breakdown, including base price, taxes, and variations, as well as detailed cancellation and payment policies.  



