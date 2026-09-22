from config import EQUIPMENT
import re


QUESTIONS = [
    "What is the price of ROB01?",
    "What is the total price of ROB01 and PLC01 after a 10% discount?",
    "Is CNC01 more expensive than ROB01, and by how much?",
    "Write a short welcome message for new students joining the Mechatronics Lab."
]


def extract_codes(text):
    codes = []

    for code in EQUIPMENT:
        if code in text.upper():
            codes.append(code)

    return codes


def process_question(question):

    q = question.lower()
    codes = extract_codes(question)

    # Rule 1: Single equipment price
    if ("price" in q or "cost" in q) and len(codes) == 1:

        code = codes[0]
        price = EQUIPMENT[code]["price"]

        return f"The price of {code} is ₹{price:,}."


    # Rule 2: Total with discount
    if "total" in q and "discount" in q and len(codes) >= 2:

        total = sum(
            EQUIPMENT[code]["price"]
            for code in codes
        )

        match = re.search(r"(\d+)\s*%", q)

        discount = 0

        if match:
            discount = int(match.group(1))

        final_price = total * (1 - discount / 100)

        return (
            f"Original total: ₹{total:,}\n"
            f"Discount: {discount}%\n"
            f"Final total: ₹{final_price:,.0f}"
        )


    # Rule 3: Compare prices
    if ("more expensive" in q or "more costly" in q) and len(codes) >= 2:

        first = codes[0]
        second = codes[1]

        price1 = EQUIPMENT[first]["price"]
        price2 = EQUIPMENT[second]["price"]

        difference = abs(price1 - price2)

        if price1 > price2:

            return (
                f"Yes. {first} is more expensive than "
                f"{second} by ₹{difference:,}."
            )

        elif price2 > price1:

            return (
                f"Yes. {second} is more expensive than "
                f"{first} by ₹{difference:,}."
            )

        else:
            return "Both equipment have the same price."


    # Rule 4: Welcome message
    if "welcome" in q:

        return (
            "Welcome to the Mechatronics Lab! "
            "Explore, experiment, build, and learn through "
            "hands-on engineering."
        )


    return "Sorry, I do not have a rule for this type of question."


def main():

    print("=" * 60)
    print("RULE-BASED WORKFLOW")
    print("=" * 60)

    for i, question in enumerate(QUESTIONS, 1):

        print(f"\nQ{i}: {question}")

        answer = process_question(question)

        print("Answer:", answer)


if __name__ == "__main__":
    main()