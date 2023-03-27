import os
import openai
openai.api_key = os.getenv("GPT_TOKEN")

def gpt(text):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
     {"role": "user", "content": text}
    ]
  )
  return completion.choices[0].message.content

