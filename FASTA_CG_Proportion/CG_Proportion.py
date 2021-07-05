# this function reads the FASTA file and returns the CG proportion for each DNA sample
# as well as the DNA sample with the most CG proportion
def FASTA(filename):
    infile = open(filename, 'r')
    FASTA = infile.read().replace('\n', '')
    
    DNA_dict = {}
    for record in FASTA[1::].split('>'):
        DNA_dict.update({record[:13]:record[13:]})
    
    CG = {}
    for ID, DNA in DNA_dict.items():
        CG.update({(DNA.count('C') + DNA.count('G')) / len(DNA) * 100 : ID})

    
    for CG_proportion, ID in CG.items():
        print(ID, CG_proportion)
        if CG_proportion == max(CG):
            print()
            print('DNA sample with most CG proportion:')
            return ID, f'{CG_proportion:<10.6f}'.format()

# this function runs the main interface of the program where the user can enter the filename 
# and see the output of the CG proportion analysis
def main():
    filename = input('Enter filename (e.g. file.txt) containing string of DNA strand to be analyzed.'
                     '\nMake sure that the file is FASTA format and in the same folder as the program file: ')
    print()
    print('Sample ID    ', 'CG Proportion (%)')
    print('--------------------------------')
    print(FASTA(filename))

main()
