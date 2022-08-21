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
* Sanic API Framework
* Pydantic
* MongoDB
* Pytest
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
