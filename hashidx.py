class Directory:
    gd = 0
    elem = []

def create_directory(global_depth) :
    i = 0
    dir = Directory()
    dir.gd = global_depth
    for i in range(2**global_depth) :
        dir.elem.append(0)
    return dir

dir_test = create_directory(2)

def create_buckets(directory) :
    i = 0
    for i in range(len(directory.elem)) :
        b_number = str(i)
        b = open('b' + b_number, 'w')
        directory.elem[i] = b
create_buckets(dir_test)

def hash_databank(databank, directory) :
    db = open(databank, 'r')
    i = 0
    for line in db.readlines() :
        lines = line.splitlines()
        elements = lines[0].split()

        hash_code = hash(int(elements[2]))
        directory.elem[hash_code%(2**directory.gd)].write(elements[2] + ' ' + elements[0] + '\n')
    db.close()

#não funciona :(())
def find_element(key, directory) :
    hash_code = hash(key)
    x = open('b' + str(hash_code%(2**directory.gd)), 'r')
    print('hell')
    for line in x.readlines() :
        print('entrei')
        lines = line.splitlines()
        elements = lines[0].split()
        print('eai')
        if (elements[0] == key) :
            print('oi')
            print(elements[0] + '' + elements[1])


hash_databank('databank.txt', dir_test)
find_element(2001, dir_test)







    