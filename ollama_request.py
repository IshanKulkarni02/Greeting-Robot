import ollama

def getResponse(promptIn):
    response = ollama.chat(model='gemma2:27b', messages=[
        {
            'role': 'user',
            'content': promptIn,
        },
    ])
    return response['message']['content']


