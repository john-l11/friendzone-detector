from openai import OpenAI

def is_friendzoned(message):
  '''
  This function will be used to send the dm to openai to detect whether the
  reciever got friendzoned or if it's just a regular message.
  rtype: boolean
  '''
  # instantiate the openai client
  # note: the api key will be in the OPEN_API_KEY env var
  client = OpenAI()

  # prompt for openai
  prompt = "You are my wingman and I'm just talking to the person of my dreams" \
  "if this message seems like I got friendzoned then give me a \"YES\" otherwise" \
  "just give me a \"NO\"."

  # send the message over to openAI
  response = client.chat.completions.create(
    model="gpt-4o",
    instructions=prompt,
    input=message
  )

  # return the response of the model back to the server
  return response.choices[0].message.content == "YES"
