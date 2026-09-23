## 7.1 Worksheet

### ReAct Trace

**Question:**
Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? And by how much?

| Step | Type         | Content                                                                                | Why this step                                                         |
| ---: | ------------ | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
|    1 | Thought      | I need to find the fees of CS101 and AI202 for the first option.                       | The course fees are not known yet.                                    |
|    2 | Action       | `get_course_fee("CS101")`                                                              | To get the fee of CS101.                                              |
|    3 | Observation  | CS101 fee = ₹12,000                                                                    | Now I know the fee of CS101.                                          |
|    4 | Thought      | I need to find the fee of AI202 to calculate the first option.                         | I need both course fees for the first option.                         |
|    5 | Action       | `get_course_fee("AI202")`                                                              | To get the fee of AI202.                                              |
|    6 | Observation  | AI202 fee = ₹18,000                                                                    | Now I know the fees of CS101 and AI202.                               |
|    7 | Thought      | I need to find the fee of DS303 to calculate the second option.                        | The second option includes all three courses.                         |
|    8 | Action       | `get_course_fee("DS303")`                                                              | To get the fee of DS303.                                              |
|    9 | Observation  | DS303 fee = ₹15,000                                                                    | Now I know the fees of all three courses.                             |
|   10 | Thought      | I need to calculate the discounted cost of the first option.                           | The first option has a 10% scholarship.                               |
|   11 | Action       | `calculator("(12000 + 18000) * 0.9")`                                                  | To calculate the cost after the 10% scholarship.                      |
|   12 | Observation  | First option cost = ₹27,000                                                            | The cost of CS101 + AI202 after the scholarship is ₹27,000.           |
|   13 | Thought      | I need to calculate the discounted cost of the second option and compare both options. | The second option has a 25% scholarship.                              |
|   14 | Action       | `calculator("(12000 + 18000 + 15000) * 0.75")`                                         | To calculate the cost of all three courses after the 25% scholarship. |
|   15 | Observation  | Second option cost = ₹33,750                                                           | The cost of all three courses after the scholarship is ₹33,750.       |
|   16 | Thought      | I need to find the difference between the two options.                                 | This will show how much cheaper the first option is.                  |
|   17 | Action       | `calculator("33750 - 27000")`                                                          | To calculate the difference in cost.                                  |
|   18 | Observation  | Difference = ₹6,750                                                                    | The first option costs ₹6,750 less than the second option.            |
|   19 | Final Answer | **CS101 + AI202 with a 10% scholarship is cheaper by ₹6,750.**                         | This answers the question.                                            |

### Questions

**How many tool calls did you need?**
6 tool calls — 3 fee lookups and 3 calculator calls.

**How many LLM calls would that be in real life?**
It would depend on the agent implementation. In a typical ReAct agent, the LLM generates the next thought/action after observing each tool result, so multiple LLM calls may be required.

**Could any two actions have been done at the same time (in parallel)?**
Yes. The fee lookups for CS101, AI202, and DS303 are independent, so they could potentially be performed in parallel. The calculator operations that depend on those results must wait until the required fee information is available.
