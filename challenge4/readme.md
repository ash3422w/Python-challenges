# Cyber Activity Risk Analyzer

## Project Description

This program reads activity scores from the user and classifies them
into four risk categories:

-   Low Risk
-   Medium Risk
-   High Risk
-   Critical Risk

Negative scores are ignored. After classification, a personalization
rule is applied based on the last digit of my register number (D).


## Register Digit (D)
D = 0

Since 0 is an even number, the program removes all Low Risk scores after
classification.


## Personalization Rule

If D is even → Remove all Low Risk scores\
If D is odd → Remove all Critical Risk scores

Because D = 0 (even), the Low Risk category is removed.



## Logic / Approach

1.  The program asks the user to enter the number of activity scores.
2.  Each score is stored in a list using a for loop.
3.  Another loop checks each score:
    -   Negative values are ignored.
    -   0--30 → Low Risk
    -   31--60 → Medium Risk
    -   61--100 → High Risk
    -   Above 100 → Critical Risk
4.  Since D = 0, all Low Risk values are removed.
5.  Finally, the program prints the updated lists and summary report.

------------------------------------------------------------------------
