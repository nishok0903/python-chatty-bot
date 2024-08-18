import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o-mini",
)