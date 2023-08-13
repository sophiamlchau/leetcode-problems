"""
ORIGINAL, BRUTE FORCE SOLUTION
Runtime: 41ms (better than 74%)
Memory: 16.52mb (better than 38%)
"""

import math

word1 = "abc"
word2 = "def"
word1Length = len(word1)
word2Length = len(word2)

result = ""
count = 0

if word1Length == word2Length:
    while count < (word1Length*2):
        if count % 2 == 0:
            result += word1[math.ceil(count / 2)]
        elif count % 2 == 1:
            result += word2[math.ceil(count / 2 - 1)]
        
        count += 1
elif word1Length < word2Length:
    while count < (word1Length*2):
        if count % 2 == 0:
            result += word1[math.ceil(count / 2)]
        elif count % 2 == 1:
            result += word2[math.ceil(count / 2 - 1)]
    
        count += 1
    
    count = count // 2
    result += word2[count:]
elif word1Length > word2Length:
    while count < (word2Length*2):
        if count % 2 == 0:
            result += word1[math.ceil(count / 2)]
        elif count % 2 == 1:
            result += word2[math.ceil(count / 2 - 1)]
        
        count += 1
    
    count = count // 2
    result += word1[count:]

"""
BETTER SOLUTION, MORE SIMPLE
Runtime: 44ms (better than 60.39%)
Memory: 16.12mb (better than 95%)
Time Complexity: O(n)
Published By: Vikas-Pathak-123
"""

# Works by having us go through a loop that only ends when the end of both strings has been reached
# Then, it appends to a list in order the words. It only stops appending once the end of each word has been reached
# At the end, we get our result by creating a string from the result list using a join operator
result = []
i = 0

while i < len(word1) or i < len(word2):
    if i < len(word1):
        result.append(word1[i])
    if i < len(word2):
        result.append(word2[i])
    
    i += 1

# NEW LEARNING THING
#.join operator can be used to create a string out of a list of strings. The '' preceding will tell what is between
# each element of the list (in this case, nothing)
finalResult =  ''.join(result)