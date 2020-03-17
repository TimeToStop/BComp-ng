#
#   Parsing program file('user/program.txt')
#       Return:
#           Address of start program
#           Array of arrays of memory values
#


def parse_program_file(directory):
    with open(directory + '/user/program.txt', 'r') as file:
        start_program = file.readline()
        mem_init = []
        mem_part = []

        for line in file:
            if line[-1] == '\n':
                if line[0] == '!':
                    mem_init.append(mem_part)
                    mem_part = [line[1:-1:]]
                else:
                    mem_part.append(line[:-1:])
            else:
                if line[0] == '!':
                    mem_init.append(mem_part)
                    mem_part = [line[1::]]
                else:
                    mem_part.append(line)
        mem_init.append(mem_part)
        file.close()
        return start_program, mem_init[1::]
