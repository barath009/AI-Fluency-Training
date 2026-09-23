from agent import run_agent


QUESTION = (
    "What is the price of ROB01, and what is the total "
    "price of ROB01 and PLC01 after a 10% discount?"
)


print("=" * 70)
print("REACT TRACE - MECHATRONICS LAB")
print("=" * 70)

print("\nQUESTION:")
print(QUESTION)

print("\n--- AGENT ACTIONS AND OBSERVATIONS ---")

answer = run_agent(
    QUESTION,
    max_steps=8
)

print("\nFINAL ANSWER:")
print(answer)