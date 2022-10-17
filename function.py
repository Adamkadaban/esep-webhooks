#!/bin/python3

import requests

def lambda_handler(event, context):
	message = "Issue Created " + event['issue']['html_url']
	with open('slack_hook.secret') as fin:
		url = fin.read().strip()
	response = requests.post(url, json = {"text":message})
	return response.text
