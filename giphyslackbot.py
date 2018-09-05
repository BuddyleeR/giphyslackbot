
import os
import time
import requests
import re
from slackclient import SlackClient

# start slack client

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

#assign botid

slackbot_id = None

#constants

RTM_READ_DELAY = 1
EXAMPLE_COMMAND = "wut"
MENTION_REGEX = "<@(|[WU].+?)>(.*)"
user_id = "{SLACKBOTUSERNAMEHERE}"
giphyurl = "https://api.giphy.com/v1/gifs/random"

#Find bot command in Slack_events

def parse_bot_commands(slack_events):
	user_id = "{SLACKBOTUSERNAMEHERE}"

	for event in slack_events:
		if event["type"] == "message" and not "subtype" in event:
			user_id, message = parse_direct_mention(event["text"])
			if user_id == slackbot_id:
				return message, event["channel"]
	return None, None

#Parses for direct mentions to bot

def parse_direct_mention(message_text):

	matches = re.search(MENTION_REGEX, message_text)
	return (matches.group(1), matches.group(2).strip()) if matches else (None, None)
#Execute bot command

def handle_command(command, channel):

	payload = {'api_key': 'GIPHY API KEY HERE', 'tag': command, 'rating': 'R'}
        giphyrequest = requests.get(url = giphyurl, params = payload)
        giphydata = giphyrequest.json()
	default_response = "What the shit are you talking about?"
	giphydata = giphyrequest.json()
	response = giphydata['data']['url'] 

	slack_client.api_call(
		"chat.postMessage",
		channel=channel,
		text=response or default_response
	)



#MAIN

if __name__ == "__main__":
	if slack_client.rtm_connect(with_team_state=False):
		print("Bot connected and running!")
		slackbot_id = slack_client.api_call("auth.test")["user_id"]
		while True:
			command, channel = parse_bot_commands(slack_client.rtm_read())
			if command:
				handle_command(command, channel)
			time.sleep(RTM_READ_DELAY)
	else:
		print("Broken af, can't connect bro")
