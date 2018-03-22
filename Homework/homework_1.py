"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
complement_dictionary = {"C": "G","T":"A","G":"C","A":"T"}
def fast_complement(dna):
    dna_list = list(dna)
    complement=""
    for dnas in dna_list:
        letter=complement_dictionary[dnas]
        complement+=letter
    return complement
                   
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """


def remove_interval(s, start, stop):
    news = s[int(start)]:[int(stop)]
    return news
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    codons=[]
    i=0
    for i in range(0,len(s),int(k)):
        codon=s[i:i+int(k)]
        codons.append(codon)
    return codons
    
def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    codons=()
    i=0
    for i in range(0,len(s),int(k)):
        codon=s[i:i+int(k)]
        codons.update(codon)
    return codons
def kmer_dict(s, k):
    
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    codons={}
    i=0
    for i in range(0,len(s),int(k)):
        count = 0
        codon=s[i:i+int(k)]
        for mer in codon:
            count+=1
        codons[codon] = count
    return codons

# Reading Files
def head(file_name):
    f = open("file_name", "rw+")
    line= f.readlines()[:10]
    print(line)
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    f.close()
    return

def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    f = open("file_name", "rw+")
    line= f.readlines()[10:]
    print(line)
    f.close()
    return

def print_even(file_name):
    f = open("file_name", "rw+")
    n=1
    for line in f.readlines():
        if n % 2 ==0:
            print(line)
        n +=1
    f.close
    print(line)
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    return

def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    with open(file_name, 'r') as csv:
        for line in csv:
            columns = line.rstrip('\n').split(',')
        

    return csv

def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    with open(file_name, 'r') as csv:
        lister = []
        for line in csv:
            if csv.lines().split(',')[0] == column:
                lister.append(line)
    return lister

def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    with open ("file_name", 'r') as fasta:
        x = fasta.readlines()
        y = ""
        for line in x:
            if line[0] == line.startswith(">"):
               continue
            else:
                y +=line
            
    return y

def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    with open ("file_name", 'r') as fasta:
        x = fasta.readlines()
        y = ""
        for line in x:
            if line[0] == line.startswith(">"):
                y +=line
            else:
                continue
            
    return y

def fasta_dict(file_name): 
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    dna_dictionary={}
    with open ("file_name", 'r') as fasta:
        x = fasta.readlines()
        y = fasta.read()
        for line in x:
            if line[0] == line.startswith(">"):
                for letter in y:
                    if letter[0] == letter.startswith(">"):
                        continue
                    else:
                        dna_dictionary[line]=letter

            
    return dna_dictionary

def fastq_to_fasta(file_name):
    with open (file_name, 'r') as f:
        f = f.readlines()
        for line in f:
            line = str(line).replace("@",">")
            if line[0] == (">"):
                #print(line)
                fasta = f[1]
                print(line + fasta)
                get_label = str(file_name).replace("/",".").split(".")
                new_label = str(get_label[-2])
                with open (str(new_label) + ".fasta", 'a') as fout:
                    fout.write(line + fasta)
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    return #str(fout)
x = fastq_to_fasta("C://Users//James//Documents//GitHub//repo.git//Exercises//test_files//proper_fastq.fastq")
print(x)
# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    dna = str(dna)
    dna = dna.replace("C","g")
    dna = dna.replace("G", "C")
    dna = dna.replace("A", "t")
    dna = dna.replace("T", "A")
    dna = dna.upper()
    dna = dna[::-1]
    print(dna)
    return

def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    dna = str(dna)
    dna = dna.replace("T", "U")
    dna = dna.upper()

    print(dna)
    return

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    codons=[]
    i=0
    for i in range(0,len(rna),3):
        codon=rna[i:i+3]
        codons.append(codon)
    protein=""
    for codon in codons:
        aa=standard_code[codon]
        protein+=aa
    return protein

def reading_frames(dna):
    rdna = dna[::-1]
    last_codon_start = len(dna) - 2
    rlast_codon_start = len(rdna) -2
    master_list = []
    protein0 = []
    protein1 = []
    protein2 = []
    protein3 = []
    protein4 = []
    protein5 = []
    for start in range(0,last_codon_start,3): 
        codon = dna[start:start+3]
        #print(codon)
        protein0.append(codon)
        #print(protein0)
    for start in range(1,last_codon_start,3): 
        codon = dna[start:start+3] 
        protein1.append(codon)
    for start in range(2,last_codon_start,3): 
        codon = dna[start:start+3] 
        protein2.append(codon)
    for start in range(0,rlast_codon_start,3): 
        codon = rdna[start:start+3] 
        protein3.append(codon)
    for start in range(1,rlast_codon_start,3): 
        codon = rdna[start:start+3] 
        protein4.append(codon)
    for start in range(2,rlast_codon_start,3): 
        codon = rdna[start:start+3] 
        protein5.append(codon)
    master_list.append(protein0)
    master_list.append(protein1)
    master_list.append(protein2)
    master_list.append(protein3)
    master_list.append(protein4)
    master_list.append(protein5)
    return master_list
dna = "ATAGATAGATAGATAGATAGATAGCCCCAGATGACGATAGATAG"
print(reading_frames(dna))

