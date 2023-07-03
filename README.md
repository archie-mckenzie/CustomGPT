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
            <li>Remember to save your API key somewhere safe - if you forget it, you'll have to create a new one.</li>
        <ul>
    </li>
    <li>
        Download `CustomGPT.py` or copy and paste <a href='https://github.com/archie-mckenzie/CustomGPT/blob/main/CustomGPT.py'>the code</a> into your own `.py` file.
    </li>
    <li>
        On the second line of `CustomGPT.py`, set `openai.api_key` equal to the API key that you created in Step 1.
    </li>
    <li>
        Write instructions for your chatbot's personality or purpose in the `system_prompt` variable.
        <ul>
            <li>
                ChatGPT's system prompt is something like: "Assistant is a large language model trained by OpenAI. Current date: 03/07/23. Knowledge cutoff: 09/21.".
            </li>
        </ul>
    </li>
    <li>
        Run `pip3 install openai` in your terminal. This installs the `openai` library.
        <ul>
            <li>
                `openai` is a library created by OpenAI. It contains all the specifications for their API so your program can easily access it.
            </li>
            <li>
                You only need to install a library once.
            </li>
        </ul> 
    </li>
    <li>
        Run `CustomGPT.py`!
    </li>
</ol>