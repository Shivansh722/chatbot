import openai

openai.api_key = "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"

def query(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        break
    response = query(user_input)
    print("ChatGPT: " + response)
