from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
 model="gpt-4o",
 messages=[
   {"role": "system", "content": "You are a poetic assistant, skilled in explaining love story."},
   {"role": "user", "content": "Compose a poem that expresses the deep love from a father to his daughter in Chinese. only 20 lines"}
 ]
)

print(completion.choices[0].message.content)
