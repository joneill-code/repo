"""
exercise_03
2/8/2018

For this Exercise you will write one definition that will take in the name of a
directory as a string, and return a dictionary containing every sequence in every FASTA file where
the sequence header is the key and the DNA sequences are values.

Your definition will be tested with improperly formatted FASTA files and should handle the following cases:
    1) If there are extra new line characters, or empty lines, your program should still process sequences normally
    2) If a duplicate header exists between two entries your definition should check to see if the sequences are the same
        * If the headers and sequences are identical, your program should print a message that "a duplicate entry exists
          for <header>" and continue normally.
        * If the only the headers match, you should print a message that "duplicate headers with non-identical
          sequences were found for <header>" and neither entry should be added in the dictionary.
          (your print statements don't need to be identical to what I have written here)
    3) If a file in the directory is not a fasta file, your program should not open it. DONE
    4) If a sequence contains characters that are not A, C, G, or T, then it should not be added to the dictionary.

If your program is working correctly, the dictionary should only contain the 4 "good sequence"s in the test folder.


The following syntax may be helpful:

# deleting from a dictionary
del my_dictionary[key]

# printing and formatting a string
x = 'my_variable'
print('Error related to variable: {}'.format(x))

# checking your final dictionary by printing out key, value pairs
for key, value in my_dictionary.items():
    print('Key is: {}\tValue is: {}'.format(key, value))

"""
#if duplicate headers, delete both
#if two of the same, use only one
#if program has a protein sequence, print out protein sequence, but don't add to dictionary
#if key is missing value, don't add to dictionary
import os

def fasta_folder_to_dict(folder_path):
    fasta_dictionary = {}
    fasta_list = []
    for file_name in os.listdir(folder_path):
        if not file_name.endswith(('.fasta')):
            continue
        else:
            with open(folder_path + '//' + file_name, 'r') as infile:
                #print(infile)
                infile = infile.read()
                seqs = infile.split('>')
                for seq in seqs:
                    try:
                        x = seq.split('\n', 1)
                        header = x[0]
                        sequence =x[1].replace('\n','')
                        if len(seq) == 0:
                            continue
                if header in fasta_dictionary and seq == fasta_dictionary[header]:
                    print("Duplicate header and sequence for {}".format(header))
                          continue
                elif header in fasta_dictionary:
                          print("duplicate header {}, but non matching sequence".format(header))
                          del fasta_dictionary[header]
                          continue
                fasta_dictionary[header]=sequence
                        #print(fasta_list)
                        for key,value in fasta_dictionary.items():
                                if key == fasta_dictionary.keys():
                                    print(key)
                                    #x= fasta_dictionary.keys().count(key)
                                    #print(x)
                                    #if value not in fasta_dictionary[key]:
                                        #print(key)
                                        #fasta_dictionary.pop(key,None)
                                        
                            #else:
                                #fasta_dictionary[header]= sequence
                        #fasta_dictionary[header]=sequence
                    #fasta_dictionary.pop(key,None)
                            

                    except:
                        print('error')
            #print('Key is: {}\tValue is: {}'.format(key, value))
        for key, value in fasta_dictionary.items():
            letters = ["A","G","C","T"]
            for letter in list(value):
                if letter not in letters:
                    print("Is protein not DNA")
                    fasta_dictionary.pop(key,value)
                    break
            if value == '':
                fasta_dictionary.pop(key,value)
            #for key in fasta_dictionary.keys():
                #if key in fasta_dictionary.keys():
                    #fasta_dictionary.pop(key,None)
    print(fasta_dictionary)
'''
                seqs = infile.split('>')
                for seq in seqs:
                    try:
                        x = seq.split('\n', 1)
                        header = x[0]
                        sequence =x[1].replace('\n','')

                        fasta_dictionary[header] = sequence
                    except:
                        print('error')


def dictionary_cleaner(fasta_dictionary):
    for key, value in fasta_dictionary.items():
                letters = ["A","G","C","T"]
                if value not in letters:
                    del fasta_dictionary[key, value]
                    print("Not DNA")
                print(fasta_dictionary)
                
            #del my_dictionary[key]

'''   

x = fasta_folder_to_dict("C://Users//James//Documents//GitHub//repo.git//Exercises//test_files")
print(x)

"""
    Constructs a dictionary of all of the FASTA formatted entries from a folder containing FASTA files.
    :param folder_path: string
    :return: dictionary
            '''
                        for letter in sequence:
                            letters = ["A","G","C","T"]
                            if letter == '':
                                print('Empty String')
                                pass
                            elif letter not in letters:
                                print('Not DNA')
                                pass
                            #fasta_dictionary[line]=
        '''
             
"""
