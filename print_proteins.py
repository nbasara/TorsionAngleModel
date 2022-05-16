
def main():
    with open('proteins.txt') as fd:
        content = fd.read()
        protein =  content.split()
        print(protein[-1])
        print(len(protein))

if __name__ == '__main__':
    main()
