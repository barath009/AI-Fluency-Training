(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241MZ107_Day2 assignment> py config.py                                       
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241MZ107_Day2 assignment> py tools.py
============================================================
MECHATRONICS LAB TOOL TEST
============================================================

ROB01 price: 200000
PLC01 status: Maintenance
Discount calculation: 247500.0
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241MZ107_Day2 assignment> py direct_prompt.py
======================================================================
DIRECT PROMPTING
======================================================================

QUESTION 1:
A Mechatronics Lab has 18 students. They are divided equally into 3 teams. Each team needs 2 PLC trainers. How many PLC trainers are required?

ANSWER:
6 PLC trainers are required.

QUESTION 2:
A lab has 4 equipment categories. If each category is inspected twice per week, how many inspections are performed in one week?

ANSWER:
8 inspections are performed in one week.

QUESTION 3:
The Robotic Arm is available. The CNC Machine is in use. The PLC Trainer is under maintenance. Which equipment can a student use immediately?

ANSWER:
The student can use the **Robotic Arm** immediately.

QUESTION 4:
What is the price of ROB01?

ANSWER:
I’m sorry, but I don’t have the price information for ROB01.
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241MZ107_Day2 assignment> py cot_compare.py
======================================================================
CHAIN-OF-THOUGHT COMPARISON
Provider: groq | Model: openai/gpt-oss-20b
======================================================================

======================================================================
QUESTION 1:
A Mechatronics Lab has 18 students. They are divided equally into 3 teams. Each team needs 2 PLC trainers. How many PLC trainers are required?

--- WITHOUT CoT ---
6 PLC trainers are required.

--- WITH CoT ---
**Step 1: Determine the number of teams**

- The lab has **18 students**.
- They are divided **equally into 3 teams**.

So the number of teams is simply **3**.

**Step 2: Find the number of trainers per team**

- Each team requires **2 PLC trainers**.

**Step 3: Calculate the total number of trainers needed**

\[
\text{Total trainers} = (\text{number of teams}) \times (\text{trainers per team})
\]
\[
\text{Total trainers} = 3 \times 2 = 6
\]

---

**Answer:** **6 PLC trainers** are required.

======================================================================
QUESTION 2:
A lab has 4 equipment categories. If each category is inspected twice per week, how many inspections are performed in one week?

--- WITHOUT CoT ---
8 inspections are performed in one week.

--- WITH CoT ---
**Step‑by‑step calculation**

1. **Identify the number of categories**  
   The lab has **4** equipment categories.

2. **Determine inspections per category**  
   Each category is inspected **twice** per week.

3. **Compute total inspections**  
   Multiply the number of categories by the inspections per category:

   \[
   \text{Total inspections} = 4 \text{ categories} \times 2 \text{ inspections/category} = 8 \text{ inspections}
   \]

**Answer**

In one week, the lab performs **8 inspections**.

======================================================================
QUESTION 3:
A lab has 24 students. One-third work on robotics, one-quarter work on PLCs, and the remaining students work on automation. Howmany students work on automation?

--- WITHOUT CoT ---
10 students work on automation.

--- WITH CoT ---
**Step 1: Find how many students work on robotics**

\[
\text{Robotics students} = \frac{1}{3}\times 24 = 8
\]

**Step 2: Find how many students work on PLCs**

\[
\text{PLCs students} = \frac{1}{4}\times 24 = 6
\]

**Step 3: Determine the remaining students who work on automation**

\[
\text{Automation students} = 24 - (8 + 6) = 24 - 14 = 10
\]

---

**Answer:** **10 students** work on automation.
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241MZ107_Day2 assignment> py agent.py
======================================================================
REACT AGENT
======================================================================

QUESTION:
What is the price of ROB01, and what is the total price of ROB01 and PLC01 after a 10% discount?
step 1: get_equipment_price({'equipment_code': 'ROB01'})
        observation -> 200000
step 2: get_equipment_price({'equipment_code': 'PLC01'})
        observation -> 75000
step 3: calculator({'expression': '(200000 + 75000) * 0.9'})
        observation -> 247500.0

FINAL ANSWER:
- **Price of ROB01:** ₹200,000  
- **Total price of ROB01 and PLC01 after a 10 % discount:** ₹247,500
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241MZ107_Day2 assignment> py react_trace.py
======================================================================
REACT TRACE - MECHATRONICS LAB
======================================================================

QUESTION:
What is the price of ROB01, and what is the total price of ROB01 and PLC01 after a 10% discount?

--- AGENT ACTIONS AND OBSERVATIONS ---
step 1: get_equipment_price({'equipment_code': 'ROB01'})
        observation -> 200000
step 2: get_equipment_price({'equipment_code': 'PLC01'})
        observation -> 75000
step 3: calculator({'expression': '(200000 + 75000) * 0.9'})
        observation -> 247500.0

FINAL ANSWER:
- **Price of ROB01:** ₹200,000  
- **Total price of ROB01 and PLC01 after a 10 % discount:** ₹247,500
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241MZ107_Day2 assignment> py self_consistency.py
======================================================================
SELF-CONSISTENCY
======================================================================

QUESTION:
A Mechatronics Lab has 24 students. One-third work on robotics, one-quarter work on PLCs, and the remaining students work on automation. How many students work on automation?

Temperature: 0.8
run 1: 10**
run 2: 10**
run 3: ** 10 students work on automation.
run 4: \]
run 5: ** 10 students work on automation.

Majority answer (2 of 5 runs): 10**
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241MZ107_Day2 assignment> 