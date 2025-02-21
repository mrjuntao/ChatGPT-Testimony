####################################################
# fine tuning call (Test in playground)
# build a Jsonl file --> Create a Model --> use model
####################################################

# 11-1 Upload a training file,Json
from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("mydata.jsonl", "rb"),
  purpose="fine-tune"
)

# 11-2 Create a fine-tuned model
from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-abc123", 
  model="gpt-4o-mini"
)

# 11-3 use fine tuned model (I don't know where)
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::A2mPBvel",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "how far away is from Chengdu to Chongqing?"}
  ]
)
print(completion.choices[0].message)
