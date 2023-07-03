import openai
openai.api_key = "" # replace with your own OpenAI API key

system_prompt = "You are a pirate." # replace with your own system prompt

messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

while True:
    
    user_content = input()
    messages.append({
        "role": "user",
        "content": user_content
    })

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    print(result.choices[0].message.content)

    messages.append(result.choices[0].message)