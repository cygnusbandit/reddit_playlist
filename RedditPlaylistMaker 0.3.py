import gdata.youtube.service
import re
import datetime
import webbrowser
import urllib2
import getpass

def authentification():
    user = raw_input("Input your youtube account email: ")
    password = getpass.getpass("Input your password: ")

    try:
        #Authentification with google
        yt_service.email = user
        yt_service.password = password
        yt_service.developer_key = "add your key"
        yt_service.client_id = "add your client id"
        yt_service.ProgrammaticLogin()
    except:
        print "User or pass is wrong. Try again."
        authentification()

#<--------Do no touch this part ^--------->

def selection():
    print "\nPlaylist Maker"
    reddit = raw_input("Input subreddit>>reddit.com/r/: (ex: metal): ")
    subreddit = "http://www.reddit.com/r/%s.rss" % reddit
    calling(subreddit)



def calling(subreddit):

    #open link
    link = urllib2.urlopen(subreddit).read()

    #capture ids
    ids = re.findall("https?://www.youtube.com/watch\?v=(\w{11})",link)
    ids2 = re.findall("https?://youtu.be/(\w{11})",link)
    f_ids = ids+ids2

    if len(f_ids)>0:

        #name for playlist
        name = str(datetime.datetime.now())

        #creating new playlist
        new_playlist = yt_service.AddPlaylist(name,"Playlist of the day")


        #finding the fucking uri
        uri = re.findall("https://gdata.youtube.com/feeds/api/playlists/.*?\s*\?",str(new_playlist))

        #playlist entry
        for e in f_ids:
            playlist_entry = yt_service.AddPlaylistVideoEntryToPlaylist(uri[0],e)

        #opening in browser
        print "Setting everything in place.Wait."
        playlist_link = re.findall("https://gdata.youtube.com/feeds/api/playlists/(.*?)\s*\?",str(new_playlist))
        webbrowser.open("http://www.youtube.com/playlist?list="+playlist_link[0])
        print "Done"
    else:
        print "There are no links here today ^^"

#<-----Main------>
print "This is an alpha."
yt_service = gdata.youtube.service.YouTubeService()
authentification()
selection()


