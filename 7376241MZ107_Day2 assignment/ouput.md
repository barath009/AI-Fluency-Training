py react_trace.py
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241mz107_day2_lab> py react_trace.py       
QUESTION: Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? By how much? 

--- the agent's actions and observations ---
   step 1: get_course_fee({'course_code': 'CS101'}) -> 12000
   step 2: get_course_fee({'course_code': 'AI202'}) -> 18000
   step 3: get_course_fee({'course_code': 'DS303'}) -> 15000
   step 4: calculator({'expression': '12000+18000'}) -> 30000
   step 5: calculator({'expression': '30000*0.1'}) -> 3000.0
   step 6: calculator({'expression': '30000-3000'}) -> 27000
   step 7: calculator({'expression': '12000+18000+15000'}) -> 45000

FINAL ANSWER: **Cheaper option:** CS101 + AI202 with a 10 % scholarship.  
**Difference:** ₹6,750 (the two‑course plan costs ₹6,750 less than the three‑course plan with a 25 % scholarship).


py cot_compare.py
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241mz107_day2_lab> py cot_compare.py       

=== CHAIN-OF-THOUGHT COMPARISON | provider: groq | model: openai/gpt-oss-20b ===

========================================================================
QUESTION 1: A student takes three courses costing Rs. 12,000, Rs. 18,000 and Rs. 15,000. She gets a 15% scholarship on the total and pays the rest in 4 equal instalments. How much is each instalment?

--- WITHOUT CoT ---
Rs. 9,562.50 per instalment. 

--- WITH CoT ---
**Step 1 – Compute the total cost of the courses**  
\(12,000 + 18,000 + 15,000 = 45,000\) rupees.

**Step 2 – Calculate the scholarship amount**  
\(15\% \text{ of } 45,000 = 0.15 \times 45,000 = 6,750\) rupees.

**Step 3 – Find the amount that must be paid after the scholarship**  
\(45,000 - 6,750 = 38,250\) rupees.

**Step 4 – Divide the payable amount into 4 equal instalments**  
\(\dfrac{38,250}{4} = 9,562.5\) rupees per instalment.

---

**Final Answer:** 9,562.50 rupees per instalment. 

========================================================================
QUESTION 2: A lab has 18 computers. In the morning each computer is shared by 2 students, and in the afternoon by 3 students. How many student sittings happen in one day?

--- WITHOUT CoT ---
90 

--- WITH CoT ---
**Step 1:**  
Count the student sittings in the morning.  
- 18 computers × 2 students per computer = **36** student sittings.

**Step 2:**  
Count the student sittings in the afternoon.  
- 18 computers × 3 students per computer = **54** student sittings.

**Step 3:**  
Add the morning and afternoon sittings to get the total for one day.  
- 36 (morning) + 54 (afternoon) = **90** student sittings.

Final Answer: 90 

========================================================================
QUESTION 3: Ravi is taller than Kumar. Kumar is taller than Arun. Priya is shorter than Arun. Who is the tallest and who is the shortest?

--- WITHOUT CoT ---
Tallest: Ravi  
Shortest: Priya 

--- WITH CoT ---
**Step 1:** List the given comparisons  
- Ravi is taller than Kumar → Ravi > Kumar  
- Kumar is taller than Arun → Kumar > Arun  
- Priya is shorter than Arun → Priya < Arun  

**Step 2:** Chain the comparisons  
From Ravi > Kumar and Kumar > Arun, we can chain them:  
Ravi > Kumar > Arun  

**Step 3:** Place Priya in the chain  
We know Priya < Arun. Since Arun is already below Kumar and Ravi, Priya must be below Arun:  
Priya < Arun < Kumar < Ravi  

**Step 4:** Identify the extremes  
- The tallest person is the one at the top of the chain: Ravi.  
- The shortest person is the one at the bottom of the chain: Priya.  

**Final Answer:** Ravi is the tallest and Priya is the shortest. 

(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241mz107_day2_lab> 

py self_consistency.py
(.venv) PS D:\7376241MZ107_AI FLUENCY TRAINING\7376241mz107_day2_lab> py self_consistency.py                                                         
                                                                                                                                                     
=== SELF-CONSISTENCY | provider: groq | model: openai/gpt-oss-20b ===

QUESTION: A student takes three courses costing Rs. 12,000, Rs. 18,000 and Rs. 15,000. She gets a 15% scholarship on the total and pays the rest in 4 equal instalments. How much is each instalment? 

   run 1: ** Rs. 9,562.50 per instalment.
   run 2: **Rs. 9,562.5 per instalment**
   run 3: 9562.50
   run 4: **Rs. 9,562.50** per instalment.
   run 5: ** Rs. 9,562.50 per instalment.

Majority answer (2 of 5 runs): ** Rs. 9,562.50 per instalment.
