from fastapi import FastAPI
from objects.openai import is_friendzoned
from objects.spotify import play_song
from objects.instagram import read_dm

app = FastAPI()

# make a get request that will take the message once it is 
@app.get("/")
def dm_recieved(req):
    # this is just in case the body doesn't contain the message. We will
    # use this method to extract the message
    message = read_dm(req.body)
    
    # send the message to the open ai chatbot
    # if the message is considered to be a friendzone message then play the song
    if is_friendzoned(message):
        play_song

    # otherwise just mock the user and tell him that he won them over
    else:
        return "AWWWW YOU GOT HERRRR/HIM SOO CUTEEEEEE. LOOK AT YOU LOVEBIRDS!! <3"
    