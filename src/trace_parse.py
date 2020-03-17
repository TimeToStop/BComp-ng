#   Find the difference in memory
#   and return array of arrays of arrays :
#   [[[mem_address1, new_value1], [mem_address2, new_value2]],  First line of mem
#    [[mem_address1, new_value1], [mem_address2, new_value2]],  Second line of mem
#       ...
#   ]


def parse_mem(mem):
    print('Start parsing mem difference.')
    mem_diff = []

    for i in range(1, len(mem)):
        line_diff = []
        for j in range(len(mem[i])):
            if mem[i][j] != mem[i - 1][j]:
                line_diff.append([hex(j)[2::].zfill(3).upper(), mem[i][j]])
        mem_diff.append(line_diff)
    return mem_diff

#
#   Swap registers in report sequences
#


def swap_reg(regs):
    regs_swapped = []

    for line in regs:
        swapped_line = []

        swapped_line.append(line[2][1::])
        swapped_line.append(line[1])
        swapped_line.append(line[7][1::])
        swapped_line.append(line[0])
        swapped_line.append(line[3][1::])
        swapped_line.append(line[5])
        swapped_line.append(line[4])

        val = int(line[6], 16)
        if val < 0xF:
            swapped_line.append(str(bin(val))[2::].zfill(4))
        else:
            swapped_line.append(line[6])
        regs_swapped.append(swapped_line)

    return regs_swapped

#
#   Read and generate array of regs and memory and parse it
#


def parse(directory):
    with open(directory + '/data/trace.txt', 'r') as file:
        reg_size = 8
        mem_size = 2048
        regs = []
        mem = []

        for line in file:
            data = line[:-1:].split(' ')
            regs_step = []
            mem_step = []

            for i in range(reg_size):
                regs_step.append(hex(int(data[i]))[2:].zfill(4).upper())

            for i in range(mem_size):
                val = int(data[reg_size + i])
                if val < 0 or val > 0xFFFF:
                    val = 0
                mem_step.append(hex(val)[2::].zfill(4).upper())

            regs.append(regs_step)
            mem.append(mem_step)

        file.close()
        return swap_reg(regs)[1::], parse_mem(mem)
