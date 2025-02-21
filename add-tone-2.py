from openai import OpenAI
client = OpenAI()

prompt = "What are the opening hours for the library?"

def get_gpt_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {"role": "system", "content": "You are a witty and humorous assistant who enjoys making users laugh while providing helpful information."},
            {"role": "user",
             "content": prompt}
        ],
        max_tokens = 300,
        n = 1,
        stop = None,
        temperature = 0.7,
    )
    return print(completion.choices[0].message.content)
response = get_gpt_response(prompt)
