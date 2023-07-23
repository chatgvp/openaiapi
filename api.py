import os
import openai

api_key = "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"
openai.api_key = api_key


def get_chatgpt_response(chatgpt_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": chatgpt_prompt},
        ],
        temperature=0,
        max_tokens=1000,
    )
    return response["choices"][0]["message"]["content"].strip()


# Example usage:
chatgpt_prompt = "Tell me a joke!"
response_text = get_chatgpt_response(chatgpt_prompt)
print(response_text)
