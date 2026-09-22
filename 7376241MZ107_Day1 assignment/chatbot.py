from config import client, MODEL


SYSTEM_PROMPT = """
You are a helpful Mechatronics Lab assistant.

The laboratory has private equipment information such as
prices and equipment status.

However, you do NOT have access to the private equipment database.

Do not guess private prices or statuses.

If the user asks for private equipment information,
clearly say that the information is not available to you.

You can answer general questions and generate normal text.
"""


QUESTIONS = [
    "What is the price of ROB01?",
    "What is the total price of ROB01 and PLC01 after a 10% discount?",
    "Is CNC01 more expensive than ROB01, and by how much?",
    "Write a short welcome message for new students joining the Mechatronics Lab."
]


def ask_chatbot(question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        max_tokens=200
    )

    return response.choices[0].message.content


def main():

    print("=" * 60)
    print("PLAIN CHATBOT")
    print("=" * 60)

    for i, question in enumerate(QUESTIONS, 1):

        print(f"\nQ{i}: {question}")

        answer = ask_chatbot(question)

        print("Answer:", answer)


if __name__ == "__main__":
    main()