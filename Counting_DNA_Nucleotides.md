## Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset
```
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```
Sample Output
```
20 12 17 21
```
Link to the problem
http://rosalind.info/problems/dna/

## Solution

'''
from collections import Counter

def counting_DNA_nucleotides(stringDNA):
  counter = Counter(stringDNA)
  return (counter['A'], counter['C'], counter['G'], counter['T'])


sample_DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC' 
print(counting_DNA_nucleotides(sample_DNA))
'''

