import csv

# this function converts RNA strand to protein
def RNA_to_codon(RNA): 
    n = 3
    list_codon = [RNA[i:i+n] for i in range(0, len(RNA), n)]
    
    codons = {'UUU':'F','CUU':'L', 'AUU':'I','GUU':'V','UUC':'F','CUC':'L', 'AUC':'I', 'GUC':'V', 'UUA':'L','CUA':'L', \
              'AUA':'I', 'GUA':'V', 'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V', 'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A', \
              'UCC':'S', 'CCC':'P', 'ACC': 'T', 'GCC':'A', 'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A', 'UCG':'S', 'CCG':'P', \
              'ACG':'T', 'GCG':'A', 'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D', 'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',\
              'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E', 'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E', 'UGU':'C', 'CGU':'R', \
              'AGU':'S', 'GGU':'G', 'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G', 'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',\
              'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}
    
    list_protein = []
    for codon1 in list_codon:
        for codon2, protein in codons.items():
            if codon1 == codon2:
                list_protein.append(protein)
    
    return (''.join(list_protein[:-1]))              

# this function replaces all occurrences of the nucleotide T with U
def transcribe_DNA_to_RNA(string_DNA):
    string_DNA = list(string_DNA)
    
    for index, nucleotide in enumerate(string_DNA):
        if nucleotide == 'T':
            string_DNA[index] = 'U'

    return ''.join(string_DNA)

# this function reads the FASTA file and returns the CG proportion for each DNA sample
# as well as the DNA sample with the most CG proportion
def CG_Proportion(DNA_dict):    
    CG = {}
    for ID, DNA in DNA_dict.items():
        CG.update({ID: (DNA.count('C') + DNA.count('G')) / len(DNA) * 100})
    return CG

# this function saves processed file to csv
def save_to_csv(data_dict, label):
    filename = input('Enter filename for csv (i.e. text.csv): ')
    with open(filename, 'w') as f:
        fieldnames = ['ID', label]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        data = [dict(zip(fieldnames, [k, v])) for k, v in data_dict.items()]
        writer.writerows(data)
    print('File successfully saved')    
    
# this function runs the main interface of the program
def main():
    print('This program transcribes DNA strand to RNA and encodes the codon from the RNA into amino acids'
          '\nOnly text files with data in FASTA format is accepted.')
    filename = input('Enter filename (e.g. file.txt) containing string of DNA strand to be analyzed.'
                     '\nMake sure that the file is FASTA format and in the same folder as the program file: ')
    
    print()
    
    # instructions to use the program
    print('OPTIONS: Enter the following keywords to select mode')
    print('\'codon\' ---- encodes the codon from the RNA into amino acids')
    print('\'cg\'    ---- calculates the CG proportion for each DNA sample')
    print('\'exit\'  ---- exits program')
    print()
    
    infile = open(filename, 'r')
    FASTA = infile.read().replace('\n', '')
    
    # extracts data from the file and converts to dictionary 
    # with keys as the ID and values as the DNA
    DNA_dict = {}
    for record in FASTA[1::].split('>'):
        DNA_dict.update({record[:13]:record[13:]})
        
    # transcribes DNA per record
    transcribed_dict = {}
    for record, DNA in DNA_dict.items():
        transcribed_dict.update({record: transcribe_DNA_to_RNA(DNA)})
    
    menu = input('Enter mode: ' )
    
    # menu options
    while menu:
        if menu.lower() == 'codon':
            codon_dict = {}
            for record, RNA in transcribed_dict.items():
                codon_dict.update({record: RNA_to_codon(RNA)})        
            print(codon_dict)
            save = input('Save file to csv? (yes or no): ')          
            if save.lower() == 'yes':
                save_to_csv(codon_dict, 'Codon')
            elif save.lower() != 'no':
                break
            print()
        elif menu.lower() == 'cg':
            print(CG_Proportion(DNA_dict))
            save = input('Save file to csv? (yes or no): ')        
            if save.lower() == 'yes':
                save_to_csv(CG_Proportion(DNA_dict), 'CG Proportion')
            elif save.lower() != 'no':
                break
            print()
        elif menu.lower() == 'exit':
            print('The program has ended.')
            break
        menu = input('Enter mode: ')

main()   
