# Explanation of Scramble String

**Three Dimensional DP problem**

> Scramble String is a new string with swap operation of sub-tree of original string

Therefore we can find that in a specific length, 
s1 can be divide into two sub strings, which respectively are s11 and s12
s2 will be divide into two sub strings as well, which are s21 and s22

Then it is easy to find that in the specific position, the result will be corresponding 
to the length of substring and the start position of sub strings

> dp[i][j][l] represents whether it is scramble string, while the start position in s1 is i, 
the start position in s2 is j, and the length of the string is l

Then it is easy to find that
> dp[i][j][l] will be true, 
	if both (s11 and s21) and (s12 and s22) are scramble string,
	or both (s11 and s22) and (s12 and s21) are scramble string