import AddToPlaylist
import SaveCredentials
import FindVideo

youtube = SaveCredentials.run()

VideoID, VideoName = FindVideo.run(youtube)

	
#
#PlaylistID = 'PL1r3AlG9BUdZUpQYqJG7P-jLYPLLTVFPi'
#
#AddToPlaylist.run(youtube, PlaylistID, VideoID, VideoName)