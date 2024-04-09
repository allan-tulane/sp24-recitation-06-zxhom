# CMPS 2200 Recitation 06
## Answers

**Name:** Zach Hom
**Name:** Disha Amin


Place all written answers from `recitation-07.md` here for easier grading.


- **2)**
- W(n) = W(n-1) + W(n-2) + O(1)
- 
- Work is W(n) = O(2^n) 
- 

- **3)**
- S(n) = S(n-1) + S(n-2) + O(1)
- 
- S(n) = O(n) because you cannot parallelize due to dependency
- ex. W(n-1) = W(n-2) + W(n-3); W(n-1) requires W(n-2) to calculate so dependency between branches exists
- 

- **4)**
- The counts list records up until the (n-1)th fibonacci number while the sum of the counts list is the value of (n+1)th fibonacci number subtracted by 1.

- **6)**
- In fib_top_down(i), each previously calculated fibonacci number is stored in a memory array so no intermediate i value will be calculated more than once. Considering this, the maximum number of times fib_top_down(i) will be called for any value i is i times???
- W = O(n)
- S = O(n)

- **8)**
- Fi will only be read only once for each value of i since successive calls for i+1 uses previously defined subproblems so redundancy is elimintaed. 
- W = O(n)
- S = O(n)
