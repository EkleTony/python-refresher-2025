"""
    
    The farmer owns an N by M meter field and is facing financial challenges. He's considering selling most of the field but wants to keep a 3x3 section while conserving water usage. 

Each 1x1 plot needs a specific amount of water. Your task is to identify the optimal 3x3 slot for him, considering water efficiency.

(Given a NxM matrix, find the minimum sum of 3x3 submatrix.)

Example: Given matrix:

[
1,2,3,4,5,4,
3,1,2,1,0,4,
2,6,7,0,1,1,
4,6,7,0,0,1,
1,2,4,6,2,3,
2,7,9,8,1,5,
]
for the sub-matrix [ (row=1, coloumn=3) to (row=3, column=5)], the sum is 8 and this is the minimum 3x3 cells.


def min_sumMatrx(matrix):
  min_sum = 0
  
  rows, cols = N, M
  if rows<3 or
  
  def get_sum(r, c):
    # cal my sum for 3x3 sub matrix
    return sum[matrix[ 
  
  def dfs(r, c):
    if r > rows-3 or c > cols -3:
      return
    # use my helper func
    sum_result = min(get_sum(r,c), dfs(r, c+1) )
      
      
      
      
Given a math puzzle of a + b = c, where are a, b, and c are strings and the characters in the strings are English 
      characters that represent a digit from 0 to 9. For example:

   S E N D
 + M O R E
---------------
 M O N E Y
      
Limitations:

No two characters can encode the same digit.
Resolved numbers should not start with a leading 0. In the example above, it's not valid for S or M to be 0.
      
Question: For a solution (assignment of values to characters), verify whether it is correct.
      
Inputs:
given_solution = {[D: 1], [N, 2], [E, 7]} ....
str1: 'SEND'
Str2: 'MORE'
Str3: 'MONEY'
 
      # step--uniqueness, 2, leading zero 3) check the maths
      def verifyChar(word1, word2, res,solution):
          # 1, check uniqueness
          if len(set(solution.values() )) != len(solution):
             return False 
          # 2. check for leading zeros
          # any()
            if solution[word[0]] == 0  for word in word1:
                return False
            elif solution[word[0]] ==0 for word in word2:
                return False
         
    
 """
