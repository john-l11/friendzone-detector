from fastapi import FastAPI
from objects.openai import is_friendzoned
from objects.spotify import play_song
from objects.instagram import read_dm
from fastapi import Response
import os

app = FastAPI()
VERIFY_TOKEN = os.getenv("IG_VERIFY_TOKEN")

@app.get("/")
def verify_webhook(
    hub_mode: str = None,
    hub_verify_token: str = None,
    hub_challenge: str = None,
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return Response(content=hub_challenge, media_type="text/plain")
    return Response(status_code=403)

# make a get request that will take the message once it is 
@app.post("/")
async def dm_recieved(req):
    
    body = await req.json()

    # this is just in case the body doesn't contain the message. We will
    # use this method to extract the message
    message = read_dm(body)
    
    # send the message to the open ai chatbot
    # if the message is considered to be a friendzone message then play the song
    if is_friendzoned(message):
        play_song()

    # otherwise just mock the user and tell him that he won them over
    else:
        print("AWWWW YOU GOT HERRRR/HIM SOO CUTEEEEEE. LOOK AT YOU LOVEBIRDS!! <3")

    return {"status": "ok"}
    