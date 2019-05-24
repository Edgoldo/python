"""
Alice recently started learning about cryptography and wants to create her own 
encryption method. Alice decides to generate a random seed for her encryption by 
transforming two strings into anagrams by removing characters from each string as 
necessary.

Two words are anagrams of each other if the first word's letters can be rearranged to 
form the second word. So, the two strings must have the same characters (in any order) 
and the same length. For instance, given the strings and , Alice can remove the from to 
have which is an anagram of . The minimum number of operations performed to create the 
anagram is , so that will be her seed value.

Your challenge is to complete a line of code to calculate this seed value. You will be 
given two strings and must cumulate the minimum number of characters that must be 
removed from each string to create an anagram.

Notes

    Your code should replace the text FILL THE MISSING LINE HERE
    The provided code should not be modified.

Input Format

Two lines each containing a string.

Constraints

	1 <= length of A,B <= 10000
    A and B will only consist of lowercase latin letters, ascii (a-z).

Output Format

A single integer which is the number of character deletions.

Sample Input 0

cde
abc

Sample Output 0

4

Explanation 0

We need to delete 4 characters to make both strings anagram i.e. and from first 
string and and from second string. 
"""
w1 = raw_input() # palabra
w2 = raw_input() # abrakadabra

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    total += w1.count(letter) - w2.count(letter) if w1.count(letter) >= w2.count(letter) else w2.count(letter) - w1.count(letter)

print total