# Upwork Scanner

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Using](#using)

## General info

This is an API created with the purpose of fetching data from different upwork users

## Technologies

The project is running with:
* Python

* Sanic API Framework:
    The reason why Sanic was used is because it`s an out of the box async API that can handle a big amount of requests at the same time
* Pydantic
    Pydantic was used to instantiate the models
* http3
    Since UPwork connections are HTTP/3 based, the use of this library was a must to fetch the information
* MongoDB
    MongoDB was used to store the data collected, in a next version of the application, a feature will be implemented to first query the data on the DB before scanning
* Pytest
    Pytest is a great test suite, that's easy to use and has the possibility to create out of the box fixtures that assist a lot when working with diverse codebases
## Setup

Clone repository from github

```sh
git clone https://github.com/caioluciofc/upwork_scanner
```

Open the folder on your terminal and run:

```sh
pip install -r requirements.txt
```
Then run the API with

```sh
python application.py
```

## Using

After running your API, make a call to the endpoint "/fetch_data/"
with the Username and Password of the Upwork User you want to scan, this will
return a JSON with the desired information.
