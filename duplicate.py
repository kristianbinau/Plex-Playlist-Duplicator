from plexapi.server import PlexServer
from plexapi.playlist import Playlist
import os
import sys

#PLEX INFO
url = "http://192.168.1.#:32400"
token = "##################"

plex = PlexServer(url, token)
for i, playlist in enumerate(plex.playlists()):
	print i+1, ")", playlist.title
choice = -1
while choice == -1:
	selection = raw_input("Select playlist: ")
	try:
		selection = int(selection)
		if selection > 0 and selection <= i+1:
			choice = selection - 1
		else:
			print "Invalid selection"
	except:
		print "Invalid selection"
new_playlist_name = raw_input("Enter new playlist name: ")
Playlist.create(plex, new_playlist_name, plex.playlists()[choice].items())

