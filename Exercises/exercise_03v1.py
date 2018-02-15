import os

def fasta_folder_to_dict(folder_path):
    fasta_dictionary = {}
    for file_name in os.listdir(folder_path):
        if not file_name.endswith(('.fasta')):
            continue
        else:
            with open(folder_path + '//' + file_name, 'r') as infile:
                infile = infile.read()
                seqs = infile.split('>')
            for seq in seqs:
                try:
                    x = seq.split('\n', 1)
                    header = x[0]
                    sequence = x[1].replace('\n','')


                except Exception as e:
                    print('Error: {} in reading {}'.format(e, x))
                    continue

                # At this point we are sure we have something for "header" and something for "sequence"
                # Here is a good place to perform checks before adding them to our dictionary

                # Check if seq is an empty string - if it is, continue

                # Checking "sequence" for not CTAG chars using a dictionary
                ALLOWED_CHARACTERS = {"A": '', "C": '', "G": '', "T": ''}
                leftover_chars = ''
                for character in sequence:
                    leftover_chars += ALLOWED_CHARACTERS.get(character, character)
                if len(leftover_chars) > 0: # All CTAG characters are now replaced with nothing/empty stings
                    print("Invalid characters: {}, in header: {}".format(leftover_chars, header))
                    continue
    

                #Check if duplicate header in dict
                    #Check if only header matches, or header and sequence match

                # Header and sequence have passed all checks, now add them to the dictionary
                fasta_dictionary[header] = sequence

    return fasta_dictionary

#print(fasta_folder_to_dict('test_files'))
x = fasta_folder_to_dict("C://Users//James//Documents//GitHub//repo.git//Exercises//test_files")
print(x)

