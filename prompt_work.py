from google import genai
import api_var

def response_chatbot(prompt):
    client = genai.Client(api_key = api_var.API_chatbot)

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents = prompt
    )
    return response.text



def response_memory(prompt):
    client = genai.Client(api_key = api_var.API_memory)

    new_memory = client.models.generate_content(
        model="gemini-2.5-flash", contents = prompt
    )
    return new_memory.text