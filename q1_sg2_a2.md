Annex C
Code Quality Assessment Worksheet

Section: 9-Arayat                              Score:____________

C# / Name:   04-Bobila, 05-Caleon, 06-Gusad     Date: 8/16/2026


Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.


PseudoCode 1

Algorithm FindMax1(numbers)

    max ← numbers[0]

    For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

    EndFor

    Return max

    EndAlgorithm

PseudoCode 2

Algorithm FindMax2(numbers)

    For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

    EndFor

    EndAlgorithm

Questions with Checklists

1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?

*Algorithm 1 is faster because it uses one for loop and one if statement, while algorithm 2 uses twice as many.*


|PseudoCode 1| PseudoCode 2|
|------|------|
|*One* Does the algorithm use one loop or two nested loops? |*Two* Does the algorithm use one loop or two nested loops?|
|__ Does the algorithm repeat work unnecessarily? |✓ Does the algorithm repeat work unnecessarily?|
|✓ Which algorithm finishes in fewer steps? |__ Which algorithm finishes in fewer steps?|

Checklist to guide your answer:

2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

*Algorithm 1, because there are multiple calculations in the same lines and nested loops inside Algorithm 2*

Checklist to guide your answer:

|PseudoCode 1|PseudoCode 2|
|------|------|
|✓ Are variable names meaningful (e.g., max vs. bigger)?|✓ Are variable names meaningful (e.g., max vs. bigger)?|
|*Simple* Is the logic simple or complicated?|*Complicated* Is the logic simple or complicated?|
|✓ Are there fewer lines of code?|__ Are there fewer lines of code?|


3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

*Algorithm 1, because the code is shorter, more straightforward, and easier to  understand.*

Checklist to guide your answer:

|PseudoCode 1|PseudoCode 2|
|------|------|
|✓ Is the structure straightforward?|__ Is the structure straightforward?|
|✓ Would adding new steps break the code easily?|__ Would adding new steps break the code easily?|
|✓ Is there less chance of errors when updating?|__ Is there less chance of errors when updating?|

4. Testability
Which algorithm is easier to test with different inputs? Why?

*Algorithm 1, because it doesn't use nested loops, which makes it simpler and easier to fix if an error occurs.*

Checklist to guide your answer:


|PseudoCode 1|PseudoCode 2|
|------|------|
|✓ Can you test with small lists easily?|✓ Can you test with small lists easily?|
|✓ Does the algorithm have fewer conditions to check?|__ Does the algorithm have fewer conditions to check?|
|✓ Is the output predictable and clear?|✓ Is the output predictable and clear?|



5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

*The algorithm should check if the item is either a numerical value or not*

Checklist to guide your answer:

|PseudoCode 1|PseudoCode 2|
|------|------|
|__ Does the algorithm check if the list is empty?|__ Does the algorithm check if the list is empty?|
|__ Does it handle invalid inputs (like letters instead of numbers)?|__ Does it handle invalid inputs (like letters instead of numbers)?|
|__ Does it avoid crashing when inputs are unusual?|✓ Does it avoid crashing when inputs are unusual?|

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

*Algorithm 1, because compared to Algorithm 2, It is shorter, simpler, faster, Straightforward, does not do unnecessary steps, and has less conditions to check*
