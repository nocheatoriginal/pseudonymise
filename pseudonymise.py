'''
This file creates a random student number from 000000 to 999999.
The first three digits create the first name and the last three digits create the last name.
The matriculation number is thereby pseudonymised.
by nocheatoriginal
'''

import random

def pseudonym(matrikel):
    with open('vornamen.txt', 'r') as f:
        vornamen = f.read().splitlines()
    with open('nachnamen.txt', 'r') as f:
        nachnamen = f.read().splitlines()

    matrikel_str = str(matrikel).zfill(6)
    first_name_index = int(matrikel_str[:3]) % len(vornamen)
    last_name_index = int(matrikel_str[3:]) % len(nachnamen)

    first_name = vornamen[first_name_index]
    last_name = nachnamen[last_name_index]

    return f'{first_name} {last_name}'

def main():
    matrikel = random.randint(0, 999999)
    print(str(matrikel).zfill(6) + ": " + pseudonym(matrikel))

if __name__ == '__main__':
    main()
