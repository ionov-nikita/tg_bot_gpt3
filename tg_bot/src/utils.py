import os

from openai import OpenAI


class OpenAIBot:
    def __init__(self, gpt_token: str):
        self.token = gpt_token
        self.client = OpenAI(api_key=self.token)

    async def get_answer(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}. Answer me in text format.",
                },
            ],
        )
        return str(completion.choices[0].message.content)


gpt = OpenAIBot(gpt_token=os.getenv("GPT_TOKEN"))
