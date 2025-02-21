####################################################
# 1. create image code: Dall.E API
####################################################

from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="career development platform, a small guy is coaching a lady",
  size="1024x1024",
  quality="standard",
  n=1,
)
image_url = response.data[0].url
print(image_url)
