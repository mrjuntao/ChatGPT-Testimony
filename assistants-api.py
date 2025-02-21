####################################################
#   Assistants API example, the problem is the result is not showing

#   The assistant does not rely on pre-written or hardcoded solutions. 
#   Instead, it generates the necessary Python code in response 
#   to each unique query and executes it in real-time.
####################################################
from openai import OpenAI
client = OpenAI()

# create assistants
assistant = client.beta.assistants.create(
name="Math Tutor",
instructions="You are a personal math tutor. Write and run code to answer math questions.",
tools=[{"type": "code_interpreter"}],
model="gpt-4",
)

# create thread
thread = client.beta.threads.create()
# print(thread)

#create message
message = client.beta.threads.messages.create(
thread_id=thread.id,
role="user",
content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
# print(message)

# run
run=client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

run=client.beta.threads.runs.retrieve(
  thread_id = thread.id,
  run_id = run.id
)

messages = client.beta.threads.messages.list(
    thread_id=thread.id
)

for message in reversed(messages.data):
    print(message.role + ": " + message.content[0].text.value)
