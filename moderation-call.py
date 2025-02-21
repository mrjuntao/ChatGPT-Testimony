from openai import OpenAI

client = OpenAI()

# Text to moderate
text = "I hate you and want to hurt you."

# Call the Moderation API
response = client.moderations.create(
  input=text
)

print(response.results[0].flagged)
print(response.results[0].categories)
print(response.results[0].category_scores)
