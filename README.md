# CustomGPT

A <i>very</i> simple custom chatbot in ten lines of Python, using OpenAI's API. Intended for the students of COS 109.

## Instructions

<ol>
    <li>
        Sign in to OpenAI at <a href='https://platform.openai.com'>platform.openai.com</a>. Go to your profile in the top right hand corner and click 'View API Keys', then create a new key.
        <ul>
            <li>
                API is short for <b>A</b>pplication <b>P</b>rogramming <b>I</b>nterface. It's a way that OpenAI has created for your program to communicate with their computers.
            </li>
            <li>An API key is a secret password which lets your program identify itself when it calls an API.</li>
            <li>Remember to save your API key somewhere safe — if you forget it, you'll have to create a new one.</li>
        </ul>
    </li>
    <li>
        Download 'CustomGPT.py' or copy and paste <a href='https://github.com/archie-mckenzie/CustomGPT/blob/main/CustomGPT.py'>the code</a> into your own '.py' file.
    </li>
    <li>
        On the second line of 'CustomGPT.py', set 'openai.api_key' equal to the API key that you created in Step 1.
    </li>
    <li>
        Write instructions for your chatbot's personality or purpose in the 'system_prompt' variable.
        <ul>
            <li>
                ChatGPT's system prompt is something like: "Assistant is a large language model trained by OpenAI. Current date: 03/07/23. Knowledge cutoff: 09/21.".
            </li>
        </ul>
    </li>
    <li>
        Run 'pip3 install openai' in your terminal. This installs the 'openai' library.
        <ul>
            <li>
                'openai' is a library created by OpenAI. It contains all the specifications for their API so your program can easily access it.
            </li>
            <li>
                You only need to install a library once.
            </li>
        </ul> 
    </li>
    <li>
        Run 'CustomGPT.py'. You can do this by typing 'python3 CustomGPT.py' in your terminal, or finding and pressing the run button in your chosen development environment.
        <ul>
            <li>Type a request in the terminal, just like you would to ChatGPT, and see what happens!</li>
        </ul>
    </li>
</ol>

## Line-by-line Explanation

So what exactly is `CustomGPT.py` doing? Here is an explainer for each line:

`import openai`

This lets your program use the `openai` library. 

`openai.api_key = "" # replace with your own OpenAI API key`

This sets the API key so that your program can identify itself when it calls the OpenAI API. It should be replaced with your own secret API key.

`system_prompt = "You are a pirate." # replace with your own system prompt`

This creates a variable called `system_prompt`. The system prompt is the initial set of instructions for the chatbot. 

`messages = [{"role": "system", "content": system_prompt}]`

This creates an array (denoted by `[]` in Python) called 'messages', which is filled with objects (denoted by `{}` in Python).

Each object in the 'messages' array represents a message to the AI model. Each message object has two properties: a "role" and some "content". 

There are only three possible values for the role attribute: "system", "user", and "assistant".
<ul>
    <li>"system" provides goals, values, or key information that the assistant can use throughout the conversation.</li>
    <li>"user" indicates that a (human) user has written the content.</li>
    <li>"assistant" indicates that the AI model has written the content.</li>
</ul>

The content attribute is a string value representing the content of the message.

So, a typical conversation might look like this:

```
[
    {
        "role": "system",
        "content": "You are an AI assistant."
    },
    {
        "role": "user",
        "content": "What's the capital of China?"
    },
    {
        "role": "assistant"
        "content": "The capital of China is Beijing."
    }
]
```

At the start, the 'messages' array only has one object in it — the system message. As the conversation develops, the program will keep adding more messages.

`while True:`

This creates an infinite loop, within which code will run repeatedly. This is so that the conversation can continue back-and-forth forever[^1].

`user_content = input()`

This creates a string variable called `user_content` and sets it to whatever the user types in. This is the user's message content - their "prompt" to the AI model.

`messages.append({"role": "user", "content": user_content})`

To "append" something to an array means adding it to the end. (The opposite of "append" is "prepend" — that adds it to the beginning!) So this line appends the `user_content` created in the last line to the array of messages you created earlier, as a new message object.

`result = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)`

This is the line where the program call the OpenAI API. Your program makes a request over the internet, OpenAI runs your request through their AI models, and the result is returned to you. 

`openai.ChatCompletion.create()` is the function in the `openai` library which lets you make this request. You provide it with two parameters — "model" and "messages". "messages" is the array of messages which represents the conversation so far. "model" is the exact AI model you want to respond to your request. In this case, the requested model is "gpt-3.5-turbo", the same one that ChatGPT uses. 

Another model that it's possible to use is "gpt-4". GPT-4 is a OpenAI's latest and greatest language model. Because it is more powerful than their standard 3.5 offering, it is more expensive and not yet generally available. If you are a student of COS 109 and would like to experiment with GPT-4, get in touch.

`print(result.choices[0].message.content)`

`result.choices[0].message` is the message object (which looks like `{"role": "assistant", "content": ""}`) that has been returned by the `openai.ChatCompletion.create()` function. This line prints that message's content, so that the user can see how the AI model has responded.

`messages.append(result.choices[0].message)`

The program appends the newly created message object to the end of the messages array, so that it becomes part of the conversation history and can be used in future responses, just like in ChatGPT. (After this, the loop restarts and the user can enter a new prompt.)

And that's it! ChatGPT is just a slightly fancier version of this, behind a well-designed user interface.

As you can see, the difficult part of AI is not using the models, but creating them in the first place. It takes hundreds of millions of dollars, weeks of running time, and mind-bending amounts of energy and data to synthesize a model like gpt-3.5-turbo. That's why companies like OpenAI need so much money — like the $10B which Microsoft<a href='https://www.bloomberg.com/news/articles/2023-01-23/microsoft-makes-multibillion-dollar-investment-in-openai'>gave them</a> in January.

[^1]: Here, the program will eventually halt because the content of the messages array has outgrown what "gpt-3.5-turbo" can handle. A more sophisticated program might get around this by removing messages at the start to make room for new messages at the end.

## Contact

This demo was created by <a href='https://archiemckenzie.com'>Archie McKenzie</a> for the students of COS 109 in Fall 2023. Feel free to get in touch at <a href='mailto:archiem@princeton.edu'>archiem@princeton.edu</a> with any questions or issues.

## Code

```
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
```