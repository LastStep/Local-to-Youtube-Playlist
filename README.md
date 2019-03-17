# Local-to-Youtube-Playlist

# What this does : 
 - Reads all the songs in the specified directory and searches by 'Artist Name + Song Name' on YouTube
 - Takes the first result and adds the video in the specified playlist

# How to use :

**Step 1: Setup Google developer account**

https://developers.google.com/api-client-library/python/start/get_started

- From the API list search for two YouTube APIs and enable them
- Setup developer **credentials** with **OAuth2 key**
- Download credentials **.json** file and save it as **client-secret.json** in the directory you are working in

**Step 2: Download modules**

  Open a terminal window and pip install the following modules

    pip install mutagen

**Step 3: Store Credentials**

  -  Run the **StoreCredentials.py** file
  -  This will create a new **.json** file with all the Credential details
  -  Go to the **quickstart.py** file and copy paste the directory address in ***root_directory*** variable 
  -  If you want to add to an already create playlist then copy paste the **PlayListID** in ***PlayListID*** variable

**Note  :**

 - Currently it only supports ***.flac***, ***.mp3***, ***.m4a*** formats
 - Check the quota limit for youtube api. You can add around 50 videos a day I think
 
 
**To-Do :**

- looping playlistIDs



p.s: fuck google api
