#Lets import some Libraries

from itertools import permutations


def stringperm(str):

    permlist = permutations(str)

    #Lets Iterate through the LIST

    for perm in list(permlist):
        print(''.join(perm))

if __name__ == "__main__":
    str = "AWS"
    stringperm(str)

    

