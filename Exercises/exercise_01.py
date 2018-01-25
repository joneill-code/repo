"""
Exercise 1
Place this script inside a new folder in your github repository called "Exercises".
This will be the directory for all of your in-class exercises this semester.

By the end of class on Thursday 1/25, students should have:
    - Created a private github repo for this class
    - Added their information to this sheet:
        https://docs.google.com/spreadsheets/d/1EKNYOqTnxelmBT4jqotRbUer5eVvWYM9RloN5doScyo/edit?usp=sharing
    - Added my github account (kylelevi) as a collaborator for their private repository
    - Completed these definitions and pushed this script to a folder called "Exercises" in their repo

"""

def hello():
    print("Hello World")
    return

def percent_decimal(x):
    if x == float(x):
        y = x*100
        y = int(y)
        print(str(y) + "%")
    if x >= 1:
        x = float(x)
        z = x/100
        print(z)
    return

    """
    Converts a percentage to a decimal or a decimal to a percentage depending on the input i
    :param i: a float between 0 and 100
    :return: a float between 0 and 100
    """

def exponent(integer, power):
    x=int(integer)
    y=int(power)
    z = x
    count = 0
    while count < y:
        z= z*x
        count = count + 1
    print(z)

    """
    Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    :param integer: a positive, non zero, integer
    :param power: a positive, non zero, integer
    :return: an integer
    """
    return

def complement(dna):
    dna = str(dna)
    dna = dna.replace("C","g")
    dna = dna.replace("G", "C")
    dna = dna.replace("A", "t")
    dna = dna.replace("T", "A")
    dna = dna.upper()
    """
    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G
    """
    print(dna)
    return
