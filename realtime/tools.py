import chainlit as cl

give_feedback_on_answer_def = {
    "name": "give_feedback_on_answer",
    "description": "As a Y Combinator partner, provide a short feedback on the answer the user gave to your question. This function shoudl be called after the user has answered a question.",
    "parameters": {
        "type": "object",
        "properties": {
            "feedback": {
                "type": "string",
                "description": "The feedback to provide to the user",
            },
        },
        "required": ["feedback"],
    },
}


async def give_feedback_on_answer_handler(feedback):
    print("feedback handler")
    print(feedback)
    await cl.Message(content=feedback).send()


give_feedback_on_answer = (give_feedback_on_answer_def, give_feedback_on_answer_handler)

tools = [give_feedback_on_answer]
