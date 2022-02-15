'''
Given a string of lowercase characters from ‘a’ – ‘z’. We need to write a program to print the characters of this string in sorted order.

Input:
The first line contains an integer T, denoting number of test cases. Then T test case follows. First line of each test case contains a string S each.

Output:
For each test case, print the string S in sorted order.

Constraints:
1<=T<=100
1<=|S|<=4*10^4
String S will contains lowercase character from 'a'-'z

Example:
Input:
2
bbccdefbbaa
geeksforgeeks
Output :
aabbbbccdef
eeeefggkkorss
'''

T=int(input())
for i in range(T):
    S=input()
    print("".join(sorted(S)))
