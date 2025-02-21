####################################################
# from image tell what is inside: Chat Completion API
####################################################
#            "url": "https://www.health.com/thmb/Fk6CXIwqw1tIakQE0kpwlpu4Ze0=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-92419172-2000-02cb2718ab5b4a28ad402ba9899ec022.jpg",


from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://lh3.googleusercontent.com/p/AF1QipM1x_H-kcdpOcqmcDv7c4JxaeO5gw2QV4b0RIpl=s1360-w1360-h1020",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
print(response.choices[0].message.content)

# required body for completions API: messages, model
