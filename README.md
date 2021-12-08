# README

A command line application to analyse reports from [TBC Warcraft Logs](https://tbc.warcraftlogs.com/).
The application was written and tested with Python 3.9.

## Features

Dumps analyses for certain fights to stdout.
Currently supported fights and analyses are listed below.

### SSC & TK
#### Lady Vashj
  * Time it takes for tainted cores to be picked up and dunked or lost.
  * Time it takes for Tainted Elementals to die or despawn and who contributed to their deaths.
  * Time it takes for Coilfang Striders to die and who contributed to their deaths.

####  Kael'thas Sunstrider
  * Time it takes for Tainted Elementals to die or hatch and who contributed to their deaths.


## How to get started

* Create [an API client](https://www.warcraftlogs.com/api/clients/) and save the `client_id` and the `client_secret` (see [here](https://www.warcraftlogs.com/api/docs)).
* Create and activate a virtualenv (optional; e.g. `python3 -m venv venv && source venv/bin/activate`)
* Install requirements via `pip install -r requirements.txt`
* Provide API credentials (see below)
* Invoke the application via `python main.py $REPORT_ID`


### Authorisation via Client ID and Client Secret

Create a file named `credentials.json` using the values from creating an API client (see above):

    {
       "client_id":"secret",
       "client_secret":"secret"
    }

This approach will create a new access token with each invocation of the application.

### Authorisation via API token

You can generate an API token manually and provide it to the application as environment variable:

    export AT=$(curl -u $CLIENT_ID:$CLIENT_SECRET -d grant_type=client_credentials https://www.warcraftlogs.com/oauth/token | jq .access_token)
