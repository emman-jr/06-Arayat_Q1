# q1_sg2_a2.md
| Section | C# - Name | Date |
| ------- | ------- | ------- |
| 9 - Arayat | #06 - Emmanuel V. Gusad Jr. | 08/13 |

USED WORKSHEET: *****Smart School Canteen Queue*****

# Step 1
# Main Problem:
*The PSHS canteen’s process is slow.*

# Step 2
1. Some students take too long to decide what to order.
2. The cashier has to manually calculate totals and give change.
3. There is no system to track which food items are running out.

# Step 3
| Sub-Problem | CT Skill | Solution |
| ------- | ------- | ------- |
| Some students take too long to decide what to order. | Breaking Down Complexity | By breaking down choices into simpler forms—number of orders, lists of food, available budget—may speed up the decision. |
| The cashier has to manually calculate totals and give change. | Efficiency | We can make a built-in calculator to speed thing up. |
| There is no system to track which food items are running out. | Foundation for Algorithms | We first need to need to make a structure deigned to track food items to make a fully functioning system. |

# Step 4
1. Initiate App
2. Initiate Variables: supply (set: name (set: strings), amount (set: int), price (set:float), bought (set:int)), supplyAddNum, supplyMinusNum, income
3. Choose Mode: Supply Check, Supply Add, Buying (Supply Subtract), Exit
4. If: Supply Check
   1. Print Supply Type and Supply Amount through iterator loop
5. If: Supply Add
      1. Input Supply Type
            1. If Supply Type exists in set "name":
                  1. Input positive supplyAddNum (int)
                  2. Confirm
                  3. Add supplyAddNum to "amount" in index of "name"
            2. Else:
                  1. Loop back to input supply type
6. If: Buy
      1. Initiate loop:
            1. Input Supply Type
                  1. If Supply Type exists in set "name":
                        1. If amount in index of "name" < 1:
                              1. Loop back to supply type input, print "No Supply"
                        2. If amount in index of "name" !< 1:
                              1. Add price to supplyMinusNum
                              2. Add bought in index of "name" by 1
                              3. Loop Back to Input
            1. Else:
                  1. Confirm
                  2. Add supplyMinusNum to income
                  3. Subtract amount in index of "name" to bought in index of "name"
7. If: Exit
      1. Print income
      2. Reprint Supply Check
      3. Terminate Program, no longer looping
8. Loop back to choose mode
