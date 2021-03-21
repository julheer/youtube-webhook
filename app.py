from discord.ext import commands, tasks
from requests import get
from pymongo import MongoClient
from config import youtube_api_key, mongo_connection_token, mongo_base_collection, bot_token, youtube_api_ver, \
    new_video_message

collection = MongoClient(mongo_connection_token)['database'][mongo_base_collection]
client = commands.AutoShardedBot(command_prefix='!')


@client.event
async def on_ready():
    print(f'[LOG] Application successfully started. Logged in as {client.user}.')
    await checkLastVideo()
    await checkRuntime.start()


@tasks.loop(minutes=25.0)
async def checkRuntime():
	await checkLastVideo()


async def checkLastVideo():
    for channel_data in collection.find({}):
        channel_id = channel_data['channel_id']
        base_url = f'https://www.googleapis.com/youtube/v{youtube_api_ver}/search?part=snippet&channelId={channel_id}' \
                   f'&maxResults=1&order=date&type=video&key={youtube_api_key}'

        request_json = get(base_url).json()
        try:
            last_video_id = request_json['items'][0]['id']['videoId']

            if last_video_id != channel_data['last_video_id']:
                alert_channel = client.get_channel(channel_data['connected_channel'])
                await alert_channel.send(new_video_message.replace('{user_channel}',
                                                                   request_json['items'][0]['snippet'][
                                                                       'channelTitle']).replace('{user_channel_title}',
                                                                                                request_json['items'][
                                                                                                    0]['snippet'][
                                                                                                    'title']).replace(
                    '{user_channel_url}', f'https://youtube.com/watch?v={last_video_id}'))
                collection.update_one({'channel_id': channel_data['channel_id']},
                                      {'$set': {'last_video_id': last_video_id}})
        except IndexError:
            pass


client.run(bot_token)
