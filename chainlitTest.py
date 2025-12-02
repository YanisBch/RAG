import chainlit as cl
from geminiApiManager import completionRequest
from rag import promptGeneration

@cl.on_message
async def main(message: cl.Message):
    
    # Your custom logic goes here...
    response = completionRequest(promptGeneration(message.content))
    
    # Send a response back to the user
    await cl.Message(
        content=f"{response}",
    ).send()
    
    