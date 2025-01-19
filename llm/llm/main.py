import openai
import os

from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
open_ai_key=os.getenv("OPENAI_API_KEY")
print(open_ai_key)


