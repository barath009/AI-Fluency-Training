import json

from config import client, MODEL
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a Mechatronics Lab ReAct agent.

You have access to private laboratory equipment information
through tools.

Available equipment:
ROB01 = Robotic Arm
CNC01 = CNC Machine
PLC01 = PLC Trainer
3DPR01 = 3D Printer

Rules:
1. Use get_equipment_price for private equipment prices.
2. Use get_equipment_status for private equipment status.
3. Use calculator for arithmetic.
4. Never guess private data.
5. Use multiple tools when necessary.
6. Continue until enough information is available.
7. Give the final answer clearly.
8. Prices are in Indian Rupees.
"""


def run_agent(question, max_steps=8):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0,
            max_tokens=500
        )

        message = response.choices[0].message

        # If no tool is requested, return final answer
        if not message.tool_calls:

            return message.content

        # Add assistant tool-call message
        messages.append(message)

        # Execute requested tools
        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            try:
                arguments = json.loads(
                    tool_call.function.arguments
                )
            except Exception:
                arguments = {}

            print(
                f"step {step}: "
                f"{tool_name}({arguments})"
            )

            if tool_name not in TOOL_FUNCTIONS:

                result = f"Unknown tool: {tool_name}"

            else:

                try:
                    result = TOOL_FUNCTIONS[tool_name](
                        **arguments
                    )

                except Exception as e:
                    result = f"Tool error: {e}"

            print(
                f"        observation -> {result}"
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

    return "Maximum agent steps reached."


if __name__ == "__main__":

    question = (
        "What is the price of ROB01, and what is the total "
        "price of ROB01 and PLC01 after a 10% discount?"
    )

    print("=" * 70)
    print("REACT AGENT")
    print("=" * 70)

    print("\nQUESTION:")
    print(question)

    answer = run_agent(question)

    print("\nFINAL ANSWER:")
    print(answer)