# How to contribute

First of all, we are so glad that you are reading this right now, we need YOU to make [Amadeus for Developers documentation](https://amadeus4dev.github.io/developer-guides/) more consistent, and readable, adding missing information, correcting factual errors, or/and fixing typos. :heart_eyes::tada: 

### Style guide

Our guides are written in the second-person point of view, which is more engaging for the reader.

#### Menu item names and headers

Keep the menu item names as short as possible but describe them in the page headers. For example, **Pricing > Pricing options for Amadeus Travel APIs**.

#### Start each step with a verb

When writing step-by-step instructions, start each step with a verb. For example:

1. Create an account.
2. Register your app.
3. Make an API call.

#### Information and warning boxes

!!! warning
    This text box is used to describe an action that can potentially inflict damage to your system or business.

!!! information
    This text box is used to provide any supplementary information about your topic.

#### Page names and navigation paths

When referring to specific pages or products, we prefer putting their names in bold. For example, "navigate to the **Settings** page".

We prefer putting the navigation paths in bold as well. For example, "navigate to **Settings > API keys**".

#### Placeholders in the code

If you need to use a placeholder in a code sample, set it between angle brackets and describe it after the code. For example:

```javascript
{
    "client_id": "<YOUR-CLIENT-ID>",
    "token_type": "Bearer"
}
```

Replace `<YOUR-CLIENT-ID>` with your client Id.

#### Parameter name in the text

When using a `parameter_name` in the text, put it between backticks ``.

#### Amadeus API names

When mentioning an Amadeus API, use a link to the [API catalogue](https://developers.amadeus.com/self-service) in the `[link](url)` format.


### Did you find a typo or misleading information? 
- Open a [GitHub issue](https://github.com/amadeus4dev/developer-guides/issues) with descriptions of which sections and the reasons if necessary. 


### Do you have an idea or/and contents to contribute? 
There are 2 ways for you to contribute by spreading your ideas!  
1. Make changes directly to [the source code in GitHub](https://github.com/amadeus4dev/developer-guides), and then open a pull request to apply your changes to the main branch. In this case, you will be able to contribute with your own words and contents directly. Check below about the documentation navigation so that you know which folders/files to update. 
2. Open a [GitHub issue](https://github.com/amadeus4dev/developer-guides/issues) with descriptions of your ideas and contents. 


### Documentation Navigation
The Amadeus for Developers documentation is generated with [Mkdocs](https://www.mkdocs.org/) and each page in the documentation is based on Markdown.
[mkdocs.yml file](https://github.com/amadeus4dev/developer-guides/blob/dcd481558da870a539a49f5564e8cb4e5e159835/mkdocs.yml) has the navigation indicating which section is with which file. 

For example, API Tutorials > Flights section is with [resources/flights.md](https://github.com/amadeus4dev/developer-guides/blob/dcd481558da870a539a49f5564e8cb4e5e159835/docs/resources/flights.md)

### How to run the project locally

Clone the repository

```
git clone https://github.com/amadeus4dev/developer-guides.git
cd developer-guides
```

Create your virtual environment and install the dependences 

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the server

```
mkdocs serve
```

Now you can go to http://127.0.0.1:8000 and check out the documentation. For any changes you make, you will just have to refresh your browser to see them.

**NOTE:** If you encounter a problem starting MkDocs, upgrade it by running `pip install -U mkdocs`.

### Do you have any questions?
Please feel free to join [our Discord channel](https://github.com/amadeus4dev/developer-guides/blob/dcd481558da870a539a49f5564e8cb4e5e159835/mkdocs.yml) to meet our community and ask questions! 

Thank you! :heart::airplane: Happy Travel, Happy Coding

_The Amadeus for Developers Team_
