import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("GPT_TOKEN")

def chat(text):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
     {"role": "user", "content": text}
    ]
  )
  return completion.choices[0].message.content

def img(text):
  completion = openai.Image.create(
    prompt=text,
    n=1,
    size="1024x1024"
  )
  return completion.data[0].url

def var(text):
  openai.Image.create_variation(
    image=open(text, "rb"),
    n=1,
    size="1024x1024"
  )