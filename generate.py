'''
This file creates two files, each with 1000 different first and last names.
by nocheatoriginal
'''

from faker import Faker
import random

def generate(file):
    fake = Faker('de_DE')
    names = set()

    while len(names) < 1000:
        names.add(fake.first_name())

    names = list(names)
    random.shuffle(names)

    with open(file, 'w') as f:
        f.write('\n'.join(names))

    print(f"1000 Namen wurden generiert und in der Datei: {file} gespeichert.")

def main():
    generate("vornamen.txt")
    generate("nachnamen.txt")

if __name__ == '__main__':
    main()