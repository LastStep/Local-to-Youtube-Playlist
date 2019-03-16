import AddToPlaylist
import SaveCredentials
import FindVideo

youtube = SaveCredentials.run()

VideoID, VideoName = FindVideo.run(youtube)	

PlaylistID = 'PL1r3AlG9BUdZRE0zSYGf2P4bld8LBllT-'

AddToPlaylist.run(youtube, PlaylistID, VideoID, VideoName)