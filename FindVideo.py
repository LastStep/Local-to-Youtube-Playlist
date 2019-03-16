import requests
import re
import os
import eyed3
import AddToPlaylist

def get_song_name(root, search):
	
	location = root + '\\' + search
	song = eyed3.load(location)
	
	return song.tag.artist + ' ' + song.tag.title

def run(youtube):
	root_directory = 'D:\AAAAAAA Songs\%%\Joji'
	
	files = {}
	
	filters = ('.mp3', '.m4a')
	for root, dirs, file in os.walk(root_directory):
		temp = []
		for f in file:
			if f.endswith(filters): 
				temp.append(f)
		files[root] = temp
	
	VideoID, VideoName = [], []
	
	for root in files.keys():
		
		for search in files[root]:
			
			search = get_song_name(root, search)
			
#			site = 'http://www.youtube.com/results?search_query=' + search
#			data = requests.get(site)
#			
#			search_results = re.findall(r'href=\"\/watch\?v=(.{11})', data.text)
			
			search_results = search_youtube(youtube, search)
			VideoId = search_results['items'][0]['id']['videoId']
			VideoID.append(VideoId)
			VideoName.append(search)
			print('Done :', search)
			print('Video:https://www.youtube.com/watch?v='+VideoId)
			
	return VideoID, VideoName


def search_list_by_keyword(youtube, **kwargs):

  kwargs = AddToPlaylist.remove_empty_kwargs(**kwargs)

  return youtube.search().list(
    **kwargs
  ).execute()
  

def search_youtube(youtube, search):
  
  return search_list_by_keyword(youtube,
    part='snippet',
    maxResults=5,
    q=search,
    type='')
  
  