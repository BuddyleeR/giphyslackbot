# giphyslackbot

A slack bot integration that fetches a GIF based on the message passed to the slackbot.

# Setting up your "Starterbot" environment

Due to security concerns with the API keys, and managing python dependencies, we are going to run the entirety of the slackbot in a virtualenv. Start with the following commands:

virtualenv starterbot

source starterbot/bin/activate

Finally, you'll have to pass your slackbot's API token (please reference Slack documentation on obtaining bot key):

export SLACK_BOT_TOKEN='your bot user access token here'

This way, your key won't be hardcoded into the python script.

# Configuring the giphyslackbot

There are a few key components that must be altered in the script depending on what you want out of the bot, as well as some details needed such as your GIPHY API key.

We are currently by default hitting the "random" gif API endpoint:

https://api.giphy.com/v1/gifs/random

Refer to giphy documentation (https://developers.giphy.com/docs/) for all of the different endpoints that are available.

For our example, we are also packing the following parameters into our query to GIPHY that are required:

'api_key': 'GIPHY API KEY HERE'
'tag': command (this is actually passed from a previous function and is actually the user's captured message to your slackbot)
'rating': R (this can be set to be the rating for the gifs you want to come back at you)

That's it.

Simply run the python script once the payloads and tokens are in place, you'll be able to @ your slackbot (invite him to channel first) and he'll take your message and ping the giphy API with an appropriate response, you hope.

(you can pass your giphy token via an env variable as well, however we are simply using it to GET gifs and nothing else)

