from collections import Counter

from config import client, MODEL


QUESTION = (
    "A Mechatronics Lab has 24 students. "
    "One-third work on robotics, one-quarter work on PLCs, "
    "and the remaining students work on automation. "
    "How many students work on automation?"
)


COT_PROMPT = """
You are a helpful assistant.

Solve the problem step by step.

At the end, write:
Final Answer: <answer>
"""


RUNS = 5
TEMPERATURE = 0.8


def get_answer(text):

    for line in reversed(text.splitlines()):

        if "final answer" in line.lower():

            return line.split(":", 1)[-1].strip()

    return text.splitlines()[-1].strip()


def run_many():

    answers = []

    for attempt in range(1, RUNS + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": COT_PROMPT
                },
                {
                    "role": "user",
                    "content": QUESTION
                }
            ],
            temperature=TEMPERATURE,
            max_tokens=400
        )

        answer = get_answer(
            response.choices[0].message.content
        )

        print(
            f"run {attempt}: {answer}"
        )

        answers.append(answer)

    return answers


def main():

    print("=" * 70)
    print("SELF-CONSISTENCY")
    print("=" * 70)

    print("\nQUESTION:")
    print(QUESTION)

    print(
        f"\nTemperature: {TEMPERATURE}"
    )

    answers = run_many()

    counts = Counter(answers)

    winner, count = counts.most_common(1)[0]

    print(
        f"\nMajority answer "
        f"({count} of {len(answers)} runs): {winner}"
    )


if __name__ == "__main__":
    main()