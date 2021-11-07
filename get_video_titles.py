# Credits to Indian Pythonista on Youtube for the tutorial on how to make this

from googleapiclient.discovery import build

# Create file api-key.txt and add api key there
with open("api_key.txt") as key:
    api_key = key.read()

youtube = build("youtube", "v3", developerKey=api_key)


def get_channel_videos():
    request = youtube.channels().list(
        part='contentDetails',
        # Replace below quotes with Channel ID
        id="UCmSp4bDxS9R0jpeZEvkut2g"
    ).execute()

    upload_playlist = request["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    videos = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(playlistId=upload_playlist,
                                               part="snippet",
                                               maxResults=50,
                                               pageToken=next_page_token).execute()

        videos += request["items"]
        next_page_token = request.get("nextPageToken")

        if next_page_token == None:
            break

    return videos


videos = get_channel_videos()
print(len(videos))
for i in videos:
    print(i["snippet"]["title"])
