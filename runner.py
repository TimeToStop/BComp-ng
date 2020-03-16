import os

#
#       This program translate your 'user/program.txt' file into 'data/registers/!ip_init'
#       and 'data/memory/!mem_init.txt' that bcomp-ng.jar(hacked) using to initialize itself.
#

# Current directory
current_directory = os.path.split(os.path.abspath(__file__))[0]

#
#   Write in '!ip_init.txt' start value of IP
#


def init_ip(start_program):
    with open(current_directory + '/data/registers/!ip_init.txt', 'w') as file:
        file.writelines(['2\n', str(int(start_program, 16)) + '\n'])
        file.close()

#
#   Write in !mem_init.txt memory values
#       mem_init - array of arrays, that holds mem address and then memory values
#


def init_mem(mem_init):
    # Memory
    memory = [0 for i in range(2048)]

    # Init memory
    for mem in mem_init:
        # Memory address
        index = int(mem[0], 16)
        for i in range(1, len(mem)):
            # Init mem values after memory address
            memory[index] = int(mem[i], 16)
            index += 1
    # Write memory in
    with open(current_directory + '/data/memory/!mem_init.txt', 'w') as file:
        file.writelines([str(mem) + '\n' for mem in memory])
        file.close()

#
#   Parsing program file('user/program.txt')
#       Return:
#           Address of start program
#           Array of arrays of memory values
#       Throw:
#           AssertException - if bad value in file
#           FileNotFound - id file does not exist
#


def parse_program_file():
    with open(current_directory + '/user/program.txt', 'r') as file:
        start_program = file.readline()
        mem_init = []
        mem_part = []

        for line in file:
            if line[-1] == '\n':
                if line[0] == '!':
                    assert len(line) == 6, [line[:-1:], '5']
                    mem_init.append(mem_part)
                    mem_part = [line[1:-1:]]
                else:
                    assert len(line) == 5, [line[:-1:], '4']
                    mem_part.append(line[:-1:])
            else:
                if line[0] == '!':
                    assert len(line) == 5, [line, '5']
                    mem_init.append(mem_part)
                    mem_part = [line[1::]]
                else:
                    assert len(line) == 4, [line, '4']
                    mem_part.append(line)
        mem_init.append(mem_part)
        file.close()
        return start_program, mem_init[1::]


def main():
    start_program = ''
    mem_init = []

    try:
        start_program, mem_init = parse_program_file()
    except FileNotFoundError:
        print('File \'user/program.txt\' not found!')
    except AssertionError as e:
        line = e.args[0]
        length = e.args[1]
        print('Error in line \'{}\' it must have {} length.'.format(line, length))
        input()

    try:
        init_ip(start_program)
        init_mem(mem_init)
    except FileNotFoundError:
        print('Cannot find system directory(registers/reg or memory/mem)!')
        input()
    except IndexError:
        print('Wrong memory cell!')
        input()


if __name__ == '__main__':
    main()
