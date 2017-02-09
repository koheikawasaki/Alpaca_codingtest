"""Given a text txt[0..n-1] and a pattern pat[0..m-1], 
write a function search(char pat[], char txt[]) 
that prints all occurrences of pat[] in txt[]. You may assume that n > m.
"""

def find(txt, pat):
	for i in range(len(txt) - len(pat)+1):
		if pat[0] == txt[i]:
			for j in range(len(pat)-1):
				if pat[1+j] != txt[i+j+1]:
					break
				if j == len(pat)-2:
					print "Pattern found at index", i
					
txt = "THIS IS A TEST TEXT"
pat = "TEST"
find(txt, pat)
"""
Output: Pattern found at index 10
"""
txt = "AABAACAADAABAABA"
pat = "AABA"
"""Output: Pattern found at index 0
Pattern found at index 9
Pattern found at index 12"""
find(txt, pat)