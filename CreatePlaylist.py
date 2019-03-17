    
def add_playlist(youtube, title, privacyStatus = 'private'):
  
  body = dict(snippet = dict(title = title, description = None), status = dict(privacyStatus = privacyStatus)) 
    
  try:
      playlists_insert_response = youtube.playlists().insert(
    part = 'snippet,status',
    body = body
  ).execute()
  except:
      print('CreatePlaylist Error')
      return None
  
  print('New playlist Name: %s' % title)
  print('New playlist ID: %s' % playlists_insert_response['id'])
  
  return list(playlists_insert_response['id'])
  
  
  
def run(youtube, title, description = None, privacy = 'public'):

  playlistId = []
  
  for index in range(len(title)):
    playlistId.append(add_playlist(youtube, title[index], privacy))
    
  return playlistId
    
    
    
    
    