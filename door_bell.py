from gpiozero import Button
from slackclient import SlackClient

import subprocess
import time


slack_token = "<Enter Slack bot auth token here>"
sc = SlackClient(slack_token)

button = Button(13)

def slack_upload():
    image = ("images/image" + time.strftime("%m_%d_%Y_%H_%M_%S") + ".jpg")
    subprocess.call(["fswebcam", image])
    time.sleep(5)
    
    with open(image, 'rb') as image_content:
        sc.api_call(
            "files.upload",
            channels="<Enter Slack channel id here>",
            file=image_content,
            title=":bell: DING DONG :bell:"
        )

while True:
    try:

        if button.is_pressed:
            slack_upload()
                        
    except FileNotFoundError:
        pass   