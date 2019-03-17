import AddToPlaylist
import FindVideo
import BuildResource

youtube = BuildResource.run()

root_directory = r'D:\AAAAAAA Songs\%%\Twenty One Pilots'

VideoID, VideoName = FindVideo.run(youtube, root_directory)	

PlaylistID = 'PL1r3AlG9BUdZRE0zSYGf2P4bld8LBllT-'

AddToPlaylist.run(youtube, PlaylistID, VideoID, VideoName)