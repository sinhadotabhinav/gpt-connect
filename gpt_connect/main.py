import openai
import logging
from .config import get_api_key

class GPTConnect:
    def __init__(self):
        self.api_key = get_api_key()
        openai.api_key = self.api_key

    def generate_text(self, prompt, model="text-davinci-003", max_tokens=150, temperature=0.7):
        logging.info(f"Generating text for prompt: {prompt}")
        try:
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].text.strip()
        except openai.error.OpenAIError as e:
            logging.error(f"Error generating text: {e}")
            return f"An error occurred: {e}"

    def chat(self, messages, model="gpt-4"):
        logging.info(f"Chatting with messages: {messages}")
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages
            )
            return response.choices[0].message['content'].strip()
        except openai.error.OpenAIError as e:
            logging.error(f"Error in chat: {e}")
            return f"An error occurred: {e}"
