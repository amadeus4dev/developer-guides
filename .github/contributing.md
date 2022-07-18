# How to contribute

First of all, we are so glad that you are reading this right now, we need YOU to make [Amadeus for Developers documentation](https://amadeus4dev.github.io/developer-guides/) more consistent, and readable, adding missing information, correcting factual errors, or/and fixing typos. :heart_eyes::tada: 


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

Now you can go to http://127.0.0.1:8000 and check out the documentation. For amy changes you make, you will just have to refresh your browser to see them.

```
### Do you have any questions?
Please feel free to join [our Discord channel](https://github.com/amadeus4dev/developer-guides/blob/dcd481558da870a539a49f5564e8cb4e5e159835/mkdocs.yml) to meet our community and ask questions! 

Thank you! :heart::airplane: Happy Travel, Happy Coding

_The Amadeus for Developers Team_