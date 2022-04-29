def read_input(file_name) :
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda line: (line.strip().split(':')[0], int(line.strip().split(":")[1])), lines))
        return lines

def out(inputs) :
    for i in range(len(inputs)) :
        instruct = get_commands(inputs, i)
        if (instruct[0] == 'INC') :
            print('inc')
        elif (instruct[0] == 'REM') :
            print('rem')
        elif (instruct[0] == 'BUS=') :
            print('bus')

inputs = read_input('in.txt')
print(inputs)
# out(inputs1)
        




