import ytapi
import sys

def playlist_items_insert(youtube, VideoName, properties):
	
  resource = ytapi.build_resource(properties)
  
  try: youtube.playlistItems().insert(body=resource).execute()
  except: 
	  print('AddToPlaylist Error')
	  sys.exit()
	  
  print('Done : ', VideoName)


def run(youtube, PlaylistID, VideoID, VideoName):
  
  for index in range(len(VideoID)):
	  
	  playlist_items_insert(youtube, VideoName[index], 
	    {'snippet.playlistId': PlaylistID,
	     'snippet.resourceId.kind': 'youtube#video',
	     'snippet.resourceId.videoId': VideoID[index],
	     'snippet.position': ''})
  