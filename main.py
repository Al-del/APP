from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
response = chat_gpt("What is a quantum computer?")
print(response)