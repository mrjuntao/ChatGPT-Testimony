from openai import OpenAI
import json

# --------------------------------------------------------------
# Initiate OpenAI API
# --------------------------------------------------------------

client = OpenAI()

# --------------------------------------------------------------
# Describe the function
# --------------------------------------------------------------

prompt = "Whats the population of Germany"

function_descriptions = [
    {
        "name": "get_population_data",
        "description": "Get the population data for a specific country",
        "parameters": {
            "type": "object",
            "properties": {
                "population": {
                    "type": "integer",
                    "description": "The number of inhabitants for this country",
                },
                "country_name": {
                    "type":"string",
                    "description":"The name of the country"
                }
            },
            "required": ["population","country_name"],
        },
    }
]

# --------------------------------------------------------------
# Make the API Call
# --------------------------------------------------------------

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user", "content": prompt}
  ],
  functions=function_descriptions,
  function_call="auto"
)

# --------------------------------------------------------------
# Extract the results
# --------------------------------------------------------------

output = completion.choices[0].message

population = json.loads(output.function_call.arguments).get("population")
country_name = json.loads(output.function_call.arguments).get("country_name")

print(population)
print(country_name)
