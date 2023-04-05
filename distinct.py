'''
This file checks whether in the files vornamen.txt and nachnamen.txt actually just contain different names.
by nocheatoriginal
'''

def distinct(file):
    with open(file, "r") as f:
        names = f.read().splitlines()

    duplicates = []
    for name in set(names):
        if names.count(name) > 1:
            duplicates.append(name)

    if duplicates:
        print("Folgende Namen kommen mehrfach vor:")
        for name in duplicates:
            lines = [i for i, n in enumerate(names) if n == name]
            print (f"{name} in den Zeilen {lines}")
    else:
        print(f"Es sind keine doppelten Namen in der Datei: {file} vorhanden.")

def main():
    distinct("vornamen.txt")
    distinct("nachnamen.txt")

if __name__ == '__main__':
    main()