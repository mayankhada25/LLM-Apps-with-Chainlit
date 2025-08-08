import chainlit as cl
from src.llm import ask_order, messages

@cl.on_message
async def main(message: cl.Message):
    #Your custom logic
    messages.append({"role": "user", "content": message.content})
    response = ask_order(messages)
    messages.append({"role": "assistant", "content": response})

    # send back the response to user
    await cl.Message(
        content=response,
    ).send()