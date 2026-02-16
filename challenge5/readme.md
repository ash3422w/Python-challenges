# Emergency Resource Dispatch Analyzer

## Project Description

During a disaster drill, emergency teams report the number of resources
requested by different zones. Some reports may contain invalid values,
unrealistic demands, or critical shortages.
This program processes the list of requests, classifies them into demand
categories, applies a personalized filtering rule (PLI), and generates a
final dispatch report.

------------------------------------------------------------------------

## Name Length (L) and PLI

Full Name: Ashok Reddy

Length of full name (excluding spaces):\
AshokReddy → 10 characters

L = 10

PLI = L % 3\
PLI = 10 % 3\
PLI = 1

------------------------------------------------------------------------

## Applied Rule

PLI = 1 → Rule B

Remove all High Demand requests from the final report.

------------------------------------------------------------------------

## Classification Rules

For each request value:

\< 0 → Invalid Request\
0 → No Demand\
1--20 → Low Demand\
21--50 → Moderate Demand\
\> 50 → High Demand

Lists used in the program:

-   low_demand
-   moderate_demand
-   high_demand
-   invalid_requests

------------------------------------------------------------------------

## Algorithm

1.  Start the program.
2.  Accept a list of integers representing resource requests.
3.  Create empty lists for each demand category.
4.  Use a for loop to process each request.
5.  Classify each value using conditional statements.
6.  Count total valid requests (excluding invalid ones).
7.  Apply the personalization rule (PLI = 1 → remove High Demand).
8.  Count how many requests were removed due to PLI.
9.  Display L value, PLI value, applied rule, total valid requests,
    removed request count, and final categorized lists.
10. End the program.

