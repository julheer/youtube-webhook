# youtube-webhook
Discord is a bot that allows you to receive notifications about new videos from a specific YouTube channel.

### Installation
In order to install this bot on your hosting, you will need to install the following dependencies:
 * **pymongo** (`pip install -U pymongo`, and `pip install -U dnspython`)
 * **discord.py** (`pip install -U discord`)
 * **requests** (`pip install -U requests`)
Then, you need to correctly and correctly fill in the bot configuration fields that are contained in the file `config.py`.
Below you can see what each configuration line is responsible for:
```python
# This line is responsible for the bot token, which you can get on https://discord.com/developers/, creating a new bot.
bot_token = ''

# This variable is responsible for what message will be sent when a
# new video is released on a certain channel
# (deprecated in 1.1, will be deleted in 1.3).
new_video_message = '**{user_channel}** submitted **{user_channel_title}**, **{user_channel_url}**.'

# This variable is responsible for the string through
# The main collection that will contain all the channels and IDs .
mongo_connection_token = ''

# The main collection that will contain all the channels and IDs.
mongo_base_collection = 'connected_channels'

# This variable is responsible for the YouTube API token,
# which you can get on https://console.cloud.google.com/apis/credentials.
youtube_api_key = ''

# ID of the YouTube API version. Don't touch it if you don't know what it's responsible for.
youtube_api_ver = 3
```

### Todos & plans
- [ ] Finish the bot's web panel.
- [ ] Make your own message for each server.
- [ ] Translate to the YouTube library for Python.

© [Julheer](https://github.com/julheer), 2021. Developed with ❤.
