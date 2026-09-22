3.1 Explanation of Each Approach
3.1.1 Plain Chatbot

What data does it use?
The plain chatbot uses the LLM alone. It does not have access to the private Mechatronics Lab equipment database.

For example, when asked:

“What is the price of ROB01?”

the chatbot cannot retrieve the actual private price because the equipment data is not provided to it.

Tools, rules, or none?

Uses an LLM.
No external tools.
No predefined decision-making rules.
No private database access.

How does it handle a request?

User Question
      ↓
     LLM
      ↓
  Response

The user sends a question, the LLM processes it, and the generated response is returned directly.

Limitations:
The chatbot cannot reliably answer questions requiring private equipment data. It may also provide incorrect information if asked to guess data that it cannot access.

However, it works well for general questions and text-generation tasks, such as:

“Write a welcome message for new students.”

3.1.2 Rule-Based Workflow

What data does it use?
The workflow directly accesses the private equipment dataset stored in the Python program.

For example:

ROB01 → ₹2,00,000
PLC01 → ₹75,000

Therefore, it can provide exact prices and perform calculations.

Tools, rules, or none?
The workflow uses predefined Python rules and conditions.

Examples:

Detect equipment codes.
Find equipment prices.
Calculate totals.
Apply discounts.
Compare prices.
Detect welcome-message requests.

No LLM is involved.

How does it handle a request?

User Question
      ↓
Predefined Rules
      ↓
Private Equipment Data
      ↓
Calculation / Processing
      ↓
Result

For example, for:

“What is the total price of ROB01 and PLC01 after a 10% discount?”

the workflow:

Detects ROB01 and PLC01.
Retrieves their prices.
Adds the prices.
Detects the 10% discount.
Calculates the final price.
Returns the result.

Limitations:
The workflow works well for predefined question patterns, but it is less flexible. If the user asks a question in an unexpected format, the existing rules may not recognize it.

Adding new types of questions requires manually writing additional rules.

3.1.3 AI Agent

What data does it use?
The AI agent uses the LLM together with controlled tools to access private equipment data.

The LLM itself does not directly receive the complete private database. Instead, it can request information through tools such as:

get_equipment_price()
get_equipment_status()
calculator()

Tools, rules, or none?
The agent uses:

LLM
Private-data tools
Calculator tool
Iterative tool-calling loop

The key concept is:

Agent = LLM + Tools + Loop

How does it handle a request?

User Question
      ↓
     LLM
      ↓
Select Appropriate Tool
      ↓
Execute Tool
      ↓
Observe Tool Result
      ↓
Decide Next Step
      ↓
Another Tool if Required
      ↓
   Final Answer

For example, for:

“What is the total price of ROB01 and PLC01 after a 10% discount?”

the agent can:

Understand that private prices are required.
Call get_equipment_price("ROB01").
Observe ₹2,00,000.
Call get_equipment_price("PLC01").
Observe ₹75,000.
Call the calculator tool.
Receive ₹2,47,500.
Generate the final answer.

This demonstrates dynamic multi-step tool usage.

Limitations:
The agent depends on the LLM to correctly understand the request and select the appropriate tools. Tool-calling errors or incorrect reasoning can cause failures. It is also more complex to implement and maintain than a simple chatbot or fixed workflow.

