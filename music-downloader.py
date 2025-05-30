from spotdl import Spotdl
url = input("URLを入力: ")
spotdl = Spotdl(client_id="0a11935211a14259a6523798a32e45e7", client_secret="afd8a7dbf45449d188d8bf3a95490925")
songs = spotdl.search([url])
results = spotdl.download_songs(songs)