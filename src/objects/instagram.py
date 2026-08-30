def read_dm(body):
    '''
    This function will be used to read a dm once the instagram hook says that
    a message has been recieved
    '''
    try:
        entry = body["entry"][0]
        messaging_event = entry["messaging"][0]
    except (KeyError, IndexError):
        return None

    # Skip events that aren't a plain text message (e.g. postbacks,
    # your own outgoing message echoed back, read receipts, etc.)
    message = messaging_event.get("message")
    if message is None or "text" not in message:
        return None

    return message["text"]