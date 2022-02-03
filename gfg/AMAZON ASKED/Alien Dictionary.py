'''
HINT : TOPOLOGICAL SORT
LEARN TOPOLOGICAL SORT BEFORE SOLVING THIS PROBLEM. 

Logic : Take two strings at a time and keep comparing them
till the point you find a different character.
For e.g how do we compare two strings which is smaller in normal english…
suppose there are two strings “abc” and “acc” so we compare the first character “a” and “a”
they are same so we move ahead..,,then we compare “b” with “c” now we see these two character
are different so we know “abc” is smaller than “bcc"

Now coming back to our original problem,

for e.g “baa” and “abcd” here the very first character is different so “b” will be smaller
than “a" we insert it into our graph and keep doing this for all the strings.
Once you get the graph then simply just apply toposort. 

'''
############
#QUESTION
############
'''
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.
 

Example 1:

Input: 
N = 5, K = 4
dict = {"baa","abcd","abca","cab","cad"}
Output:
1
Explanation:
Here order of characters is 
'b', 'd', 'a', 'c' Note that words are sorted 
and in the given language "baa" comes before 
"abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.
Example 2:

Input: 
N = 3, K = 3
dict = {"caa","aaa","aab"}
Output:
1
Explanation:
Here order of characters is
'c', 'a', 'b' Note that words are sorted
and in the given language "caa" comes before
"aaa", therefore 'c' is before 'a' in output.
Similarly we can find other orders.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function findOrder() which takes  the string array dict[], its size N and the integer K as input parameter and returns a string denoting the order of characters in the alien language.


Expected Time Complexity: O(N * |S| + K) , where |S| denotes maximum length.
Expected Space Compelxity: O(K)


Constraints:
1 ≤ N, M ≤ 300
1 ≤ K ≤ 26
1 ≤ Length of words ≤ 50
'''
TO BE SOLVED 
STILL FACING ERRORS
