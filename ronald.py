import os

os.environ["OPENAI_API_KEY"] = input("API Key: ")

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

import webbrowser

mission = input("What can I help you with? - ")

if mission == "Chat":
    prompt = input("You: ")
    user_input_chat = prompt
    while user_input_chat != "End":
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
                ]
                )
        print("Ronald: " + completion.choices[0].message.content)
        user_input_chat = input("You: ")
        prompt = user_input_chat

if mission == "Completion":
    prompt = input("Prompt: ")
    user_input_comp = prompt
    while user_input_comp != "End":
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=1000
            )
        print("Ronald: " + response.choices[0].text)
        user_input_comp = input("Prompt: ")
        prompt = user_input_comp

if mission == "Image Generation":
    prompt = input("Image Prompt: ")
    user_input_image = prompt
    while user_input_image != "End":
        image = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
            )
        webbrowser.open(image['data'][0]['url'])
        user_input_image = input("Image Prompt: ")
        prompt = user_input_image