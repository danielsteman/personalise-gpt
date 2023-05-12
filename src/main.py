from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ["OPEN_AI_API_KEY"])
