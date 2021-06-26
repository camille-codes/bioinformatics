from collections import Counter

# this function counts the number of nucleotides in a DNA. 
# It returns a tuple in the format of A, C, G, T
def counting_DNA_nucleotides(string_DNA):
  counter = Counter(string_DNA)
  count_DNA =  {'A': counter['A'], 'C': counter['C'], 'G': counter['G'], 'T': counter['T']}
  return count_DNA

# this function replaces all occurrences of the nucleotide T with U
def transcribe_DNA_to_RNA(string_DNA):
    string_DNA = list(string_DNA)
    
    for index, nucleotide in enumerate(string_DNA):
        if nucleotide == 'T':
            string_DNA[index] = 'U'

    return ''.join(string_DNA)

# This function returns the reverse complement of a DNA strand i.e. "GTCA" is "TGAC"
# 'A' becomes 'T', 'T' becomes 'A', 'C' becomes 'G', and 'G' becomes 'C'
# The original order of the DNA nucleotides is also reversed
def complement_DNA_strand(string_DNA):
    string_DNA = list(string_DNA[::-1])
    
    for index, nucleotide in enumerate(string_DNA):
        if nucleotide == 'A':
            string_DNA[index] = 'T'
        elif nucleotide == 'T':
            string_DNA[index] = 'A'
        elif nucleotide == 'C':
            string_DNA[index] = 'G'
        elif nucleotide == 'G':
            string_DNA[index] = 'C'        
    return ''.join(string_DNA)                          

# this function runs the main interface of the program where the user can enter the filename and select mode
def main():
    print('Welcome! This bioinformatics program analyzes DNA strand entered to the program.')
    print('-' * 30)
    filename = input('Enter filename (e.g. file.txt) containing string of DNA strand to be analyzed.'
                     '\nMake sure that the file is in the same folder as the program file: ')
    infile = open(filename, 'r')
    string_DNA = infile.read()
    
    print()
    preview = input('Show preview of DNA strand entered? (yes or no): ')
    
    while preview.lower() != 'yes' or preview.lower() != 'no':
        if preview.lower() == 'yes':
            print(string_DNA)
            break
        elif preview.lower() == 'no':
            break    
        preview = input('Show preview of DNA strand entered? (yes or no): ')
    
    print('OPTIONS: Enter the following keywords to select mode')
    print('\'count\'      ---- count DNA nucleotides')
    print('\'transcribe\' ---- transcribe DNA strand to RNA')
    print('\'complement\' ---- find complement DNA strand')
    print('\'exit\'       ---- exit program')
    print()
    menu = input('Enter mode: ' )    
    
    while menu != 'exit':
        if menu.lower() == 'count':
            print(counting_DNA_nucleotides(string_DNA))
        elif menu.lower() == 'transcribe':
            print(transcribe_DNA_to_RNA(string_DNA))
        elif menu.lower() == 'complement':
            print(complement_DNA_strand(string_DNA))
        elif menu.lower() == 'exit':
            print('The program has ended. Thank you!')
            break
        menu = input('Enter mode: ' )   
        
main()
