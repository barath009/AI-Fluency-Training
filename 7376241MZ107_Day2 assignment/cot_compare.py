from config import client, MODEL


QUESTIONS = [

    (
        "A Mechatronics Lab has 18 students. "
        "They are divided equally into 3 teams. "
        "Each team needs 2 PLC trainers. "
        "How many PLC trainers are required?"
    ),

    (
        "A lab has 4 equipment categories. "
        "If each category is inspected twice per week, "
        "how many inspections are performed in one week?"
    ),

    (
        "A lab has 24 students. "
        "One-third work on robotics, one-quarter work on PLCs, "
        "and the remaining students work on automation. "
        "How many students work on automation?"
    )
]


DIRECT_PROMPT = """
You are a helpful assistant.

Give only the final answer.
Do not explain the reasoning.
"""


COT_PROMPT = """
You are a helpful assistant.

Solve the problem step by step.
Show the important calculations.
Then provide the final answer clearly.
"""


def ask(system_prompt, question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()


def main():

    print("=" * 70)
    print("CHAIN-OF-THOUGHT COMPARISON")
    print(
        f"Provider: groq | Model: {MODEL}"
    )
    print("=" * 70)

    for number, question in enumerate(QUESTIONS, 1):

        print("\n" + "=" * 70)

        print(f"QUESTION {number}:")
        print(question)

        print("\n--- WITHOUT CoT ---")
        print(
            ask(
                DIRECT_PROMPT,
                question
            )
        )

        print("\n--- WITH CoT ---")
        print(
            ask(
                COT_PROMPT,
                question
            )
        )


if __name__ == "__main__":
    main()