from googleapiclient.discovery import build
import json

# Create file api-key.txt and add api key there
with open("api_key.txt") as key:
    api_key = key.read()

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.channels().list(
    part='contentDetails',
    # Replace below line with Channel ID, or remove it and add line: forUsername="Channel username"
    id="UCtkqAaVriyVMlXxyrTs6WCg"
)

response = request.execute()
upload_playlist = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

request = youtube.playlistItems().list(playlistId=upload_playlist,
                                       part="snippet", maxResults=3000)

response = request.execute()
for i in response["items"]:
    print(i["snippet"]["title"])
