import json

from config import client, MODEL
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a Mechatronics Lab equipment assistant.

Private equipment information is available ONLY through tools.

Never guess equipment prices or equipment status.

Available equipment codes:
ROB01
CNC01
PLC01
3DPR01

Rules:
1. Use get_equipment_price whenever you need a private equipment price.
2. Use get_equipment_status whenever you need private equipment status.
3. Use calculator whenever arithmetic is required.
4. You may use multiple tools for one question.
5. After receiving tool results, continue until you can give the final answer.
6. All prices are in Indian Rupees (₹), not dollars.
7. Give the final answer clearly and concisely.
"""


QUESTIONS = [
    "What is the price of ROB01?",

    "What is the total price of ROB01 and PLC01 after a 10% discount?",

    "Is CNC01 more expensive than ROB01, and by how much?",

    "What is the status of PLC01?",

    "Write a short welcome message for new students joining the Mechatronics Lab."
]


def run_agent(question, max_steps=6):

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

        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=TOOLS,
                tool_choice="auto",
                max_tokens=500
            )

        except Exception as e:

            print(f"\nLLM error: {e}")

            return "The agent encountered an error while communicating with the model."


        message = response.choices[0].message


        # ------------------------------------------------
        # If no tool is requested, return final answer
        # ------------------------------------------------

        if not message.tool_calls:

            if message.content:
                return message.content

            return "The model did not provide a final answer."


        # ------------------------------------------------
        # Add assistant message containing tool calls
        # ------------------------------------------------

        messages.append(message)


        # ------------------------------------------------
        # Execute every requested tool
        # ------------------------------------------------

        for tool_call in message.tool_calls:

            original_tool_name = tool_call.function.name

            # Groq can occasionally append internal text
            # such as <|channel|>commentary to tool names.
            tool_name = original_tool_name.split("<|")[0].strip()


            # Parse arguments
            try:

                arguments = json.loads(
                    tool_call.function.arguments
                )

            except json.JSONDecodeError:

                arguments = {}


            # ------------------------------------------------
            # Find and execute the Python tool
            # ------------------------------------------------

            if tool_name not in TOOL_FUNCTIONS:

                result = f"Unknown tool: {tool_name}"

            else:

                try:

                    result = TOOL_FUNCTIONS[tool_name](
                        **arguments
                    )

                except Exception as e:

                    result = f"Tool error: {e}"


            # ------------------------------------------------
            # Show agent trace
            # ------------------------------------------------

            print(
                f"step {step}: "
                f"{tool_name}({arguments}) -> {result}"
            )


            # ------------------------------------------------
            # Send tool result back to the LLM
            # ------------------------------------------------

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )


    return "Agent stopped because the maximum number of steps was reached."


def main():

    print("=" * 60)
    print("AI AGENT")
    print("=" * 60)

    for i, question in enumerate(QUESTIONS, 1):

        print("\n" + "=" * 60)

        print(f"Q{i}: {question}")

        print("-" * 60)

        answer = run_agent(question)

        print("Final answer:", answer)


if __name__ == "__main__":
    main()