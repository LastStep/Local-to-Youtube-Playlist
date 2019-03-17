import os
import ytapi
import mutagen


def get_song_name(root, search):

  location = root + '\\' + search
  song = mutagen.File(location)

  try:
    if search.endswith('.flac'):
      return song['artist'][0] + ' ' + song['title'][0]
    elif search.endswith('.mp3'):
      return song.tags['TPE1'][0] + ' ' + song.tags['TIT2'][0]
    elif search.endswith('.m4a'):
      return song['©nam'][0] + ' ' + song['©ART'][0]
  except:
    return search

def run(youtube, root_directory):

  files = {}
  filters = ('.mp3', '.flac', '.m4a')

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

      search_results = search_youtube(youtube, search)

      if search_results == 'Error': return VideoID, VideoName

      VideoId = search_results['items'][0]['id']['videoId']
      VideoID.append(VideoId)
      VideoName.append(search)

      print('Done :', search)
      print('Video:https://www.youtube.com/watch?v='+VideoId)

  return VideoID, VideoName


def search_list_by_keyword(youtube, **kwargs):

  kwargs = ytapi.remove_empty_kwargs(**kwargs)

  try:
    return youtube.search().list(**kwargs).execute()
  except:
    print('FindVideo Error')
    return youtube.search().list(**kwargs).execute()

def search_youtube(youtube, search):

  return search_list_by_keyword(youtube,
                                part='snippet',
                                maxResults=1,
                                q=search,
                                type='Video')

