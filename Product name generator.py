import os
import openai


for i in range(100):
    openai.api_key = "your api key"
    model_engine = "text-davinci-003"
    user_input = input("Product description:")
    prompt = "Create product names from examples words. Influenced by a community prompt:" + user_input

    response = openai.Completion.create(
        model=model_engine,
        prompt=prompt,
        max_tokens=1000,
        top_p=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    r = response.choices[0].text
    print("Product names:"+r)