import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write about why Don Quijote is the worst book",
  temperature=0.7,
  max_tokens=393,
  top_p=1,
  frequency_penalty=0.3,
  presence_penalty=0
)