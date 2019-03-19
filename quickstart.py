import AddToPlaylist
import FindVideo
import BuildResource
import CreatePlaylist

youtube = BuildResource.run()

root_directory = r'D:\AAAAAAA Songs\%%\Twenty One Pilots'

#PlaylistID = CreatePlaylist.run(youtube, 'TOP')

VideoID, VideoName = FindVideo.run(youtube, root_directory)

PlaylistID = 'PL1r3AlG9BUdZRE0zSYGf2P4bld8LBllT-'

AddToPlaylist.run(youtube, PlaylistID, VideoID, VideoName)