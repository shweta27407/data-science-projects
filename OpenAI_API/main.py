import openai

API_KEY = open("API_KEY.txt", "r").read()
openai.api_key = API_KEY

