from config import client, MODEL


SYSTEM_PROMPT = """
You are a helpful Mechatronics Lab assistant.

Answer the user's question directly.

Do not use tools.
Do not provide step-by-step reasoning.
Give only the final answer.

The following information is provided in the question when needed.
"""


QUESTIONS = [

    "A Mechatronics Lab has 18 students. "
    "They are divided equally into 3 teams. "
    "Each team needs 2 PLC trainers. "
    "How many PLC trainers are required?",

    "A lab has 4 equipment categories. "
    "If each category is inspected twice per week, "
    "how many inspections are performed in one week?",

    "The Robotic Arm is available. "
    "The CNC Machine is in use. "
    "The PLC Trainer is under maintenance. "
    "Which equipment can a student use immediately?",

    "What is the price of ROB01?"
]


def ask_direct(question):

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
        temperature=0,
        max_tokens=300
    )

    return response.choices[0].message.content


def main():

    print("=" * 70)
    print("DIRECT PROMPTING")
    print("=" * 70)

    for i, question in enumerate(QUESTIONS, 1):

        print(f"\nQUESTION {i}:")
        print(question)

        print("\nANSWER:")
        print(ask_direct(question))


if __name__ == "__main__":
    main()