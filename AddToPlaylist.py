import ytapi

def playlist_items_insert(youtube, VideoName, properties, **kwargs):
	
  resource = ytapi.build_resource(properties)

  kwargs = ytapi.remove_empty_kwargs(**kwargs)

  youtube.playlistItems().insert(body=resource, **kwargs).execute()

  print('Done : ', VideoName)


def run(youtube, PlaylistID, VideoID, VideoName):
  
  for index in range(len(VideoID)):
	  
	  playlist_items_insert(youtube, VideoName[index], 
	    {'snippet.playlistId': PlaylistID,
	     'snippet.resourceId.kind': 'youtube#video',
	     'snippet.resourceId.videoId': VideoID[index],
	     'snippet.position': ''},
	    part='snippet',
	    onBehalfOfContentOwner='')
  