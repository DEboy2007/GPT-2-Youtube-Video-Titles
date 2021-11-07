# GPT-2-Youtube-Video-Titles
Submission for Midnight Hacks 2021

# Instructions

## Step 1: Get api key
First, create a file called api_key.txt and enter your api_key there. Follow <a href = "https://www.youtube.com/watch?v=th5_9woFJmk&ab_channel=CoreySchafer">this</a> tutorial to get an api key and install the requirements for Youtube's API

## Step 2: Edit get_video_titles.py to add your desired channel
Get your desired channel's ID and replace it with the placeholder ID on line 16 (in the function get_channel_videos).

### How to find channel ID:
To obtain the channel id you can view the source code of the channel page and find either ```data-channel-external-id="Channel ID"``` or ```"externalId":"Channel ID"```

## Step 3: Install requirements for GPT-2
Follow <a href = "https://medium.com/analytics-vidhya/installing-the-requirements-for-gpt-2-tensorflow-pytorch-and-transformers-9105348f10f4">this</a> tutorial to create a virtual environment and install the requirements for GPT-2. **Remember to use python 3.7 or below**

## Step 4: Run programs
First, run get_video_titles.py and copy all the video titles you get. Create a file called video_titles.txt and paste your video titles there. Duplicate the contents you copied multiple times until there is over 1000 lines of text.

Next, upload the .ipynb notebook and text file with video titles to google colab. Then, set the hardware accelerator to GPU by going to Runtime > Change runtime type and then choosing GPU<br>
![image](https://user-images.githubusercontent.com/66331423/140658129-a1858378-0c0d-40c3-bf3d-e777b75e5cbe.png)<br>
![image](https://user-images.githubusercontent.com/66331423/140658088-d60c02cf-ac9c-41c1-be77-69519e96f454.png)<br>

Finally, run all the cells on the notebook and you will have your video titles that sound just like what the channel would upload!



