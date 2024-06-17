# Run2.py Usage Guide

`run2.py` is a Python script that interacts with the Twilio API to fetch all active conversations and tasks associated with a given workspace.

## Setting Up

Before running `run2.py`, you need to set up some environment variables. These variables hold the credentials for the Twilio API.

1. `ACCOUNT_SID`: Your Account SID from twilio.com/console
2. `AUTH_TOKEN`: Your Auth Token from twilio.com/console
3. `WORKSPACE_SID`: The SID of the workspace you want to interact with

You can set these environment variables in a `.env` file in the same directory as `run2.py`. The file should look something like this:

```env
ACCOUNT_SID=your_account_sid_here
AUTH_TOKEN=your_auth_token_here
WORKSPACE_SID=your_workspace_sid_here

