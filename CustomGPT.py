import openai
openai.api_key = "" # Your OpenAI API key here

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

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    print(completion.choices[0].message.content)
    
    messages.append(completion.choices[0].message)