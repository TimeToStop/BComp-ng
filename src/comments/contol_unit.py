address_cmd_mnem = {
    '2': 'AND {}',
    '3': 'OR {}',
    '4': 'ADD {}',
    '5': 'ADC {}',
    '6': 'SUB {}',
    '7': 'CMP {}',
    '8': 'LOOP {}',
    'A': 'LD {}',
    'B': 'SWAM {}',
    'C': 'JUMP {}',
    'D': 'CALL {}',
    'E': 'ST {}'
}

address_cmd_comm = {
    '2': 'AC = AC & {}',
    '3': 'AC = AC | {}',
    '4': 'AC = AC + {}',
    '5': 'AC = AC + C + {}',
    '6': 'AC = AC - {}',
    '7': 'Сравнить AC и {}',
    '8': 'Пока {} >= 0',
    'A': 'AC = {}',
    'B': 'AC <-> {}',
    'C': 'IP = {}',
    'D': '(--SP) = {}',
    'E': '{} = AC'
}

type_address_cmd = {
    'Auto inc': 1,
    'Auto dec': 2,
    'SP rel': 3,
    'IP rel': 4,
    'Operand load': 5,
    'Rel': 6
}


def parse_m(command, ip):
    type_of_address = int(command[1], 16)

    if type_of_address <= 7:
        return '{}'.format(hex(int(command, 16) % 2048)[2::].zfill(3).upper())
    elif type_of_address == 8:
        return '{}'.format(hex(ip + int(command[2::], 16))[2::].zfill(3).upper())
    elif type_of_address == 10:
        return '{}'.format(hex(ip + int(command[2::], 16))[2::].zfill(3).upper())
    elif type_of_address == 11:
        return '{}'.format(hex(ip + int(command[2::], 16))[2::].zfill(3).upper())
    elif type_of_address == 12:
        return 'SP + {}'.format(hex(int(command[2::], 16))[2::].upper())
    elif type_of_address == 14:
        return '{}'.format(hex(ip + int(command[2::], 16))[2::].zfill(3).upper())
    elif type_of_address == 15:
        return '{}'.format(hex(int(command[2::], 16))[2::].upper())
    else:
        return ''


def parse_address_command(command, ip):
    if command[0] in address_cmd_mnem:
        m = parse_m(command, ip)
        mnem = address_cmd_mnem[command[0]].format(m)

        if command[0] == 'D':
            comm = address_cmd_comm[command[0].format(m)].format(m)
        elif command[1]  == 'F':
            comm = address_cmd_comm[command[0]].format(m)
        else:
            comm = address_cmd_comm[command[0]].format('({})'.format(m))

        return mnem, comm
    else:
        return '', ''


no_address_cmd_mnem = {
    '0000': ' ',
    '0100': 'HLT',
    '0200': 'CLA',
    '0280': 'NOT',
    '0300': 'CLC',
    '0380': 'CMC',
    '0400': 'ROL',
    '0480': 'ROR',
    '0500': 'ASL',
    '0580': 'ASR',
    '0600': 'SXTB',
    '0680': 'SWAB',
    '0700': 'INC',
    '0740': 'DEC',
    '0780': 'NEG',
    '0800': 'POP',
    '0900': 'POPF',
    '0A00': 'RET',
    '0B00': 'IRET',
    '0C00': 'PUSH',
    '0D00': 'PUSHF',
    '0E00': 'SWAP'
}

no_address_cmd_comm = {
    '0000': '',
    '0100': 'Конец программы',
    '0200': 'AC = 0',
    '0280': 'AC = !AC',
    '0300': 'C = 0',
    '0380': 'C = !C',
    '0400': 'Циклический сдвиг влево \nC = AC15 и AC0 = C',
    '0480': 'Циклический сдвиг вправо \nC = AC0 и AC15 = C',
    '0500': 'Арифметический сдвиг влево \nAC = 2 * AC C = AC15',
    '0580': 'Арифметический сдвиг вправо \nAC = AC / 2 C = AC % 2',
    '0600': 'Расширение знака',
    '0680': 'Обмен старшего и младшего байтов',
    '0700': 'AC++',
    '0740': 'AC--',
    '0780': 'AC = -AC',
    '0800': 'AC = (SP++)',
    '0900': 'PS = (SP++)',
    '0A00': 'IP = (SP++)',
    '0B00': 'PS = (SP++) IP = (SP++)',
    '0C00': '(--SP) = AC',
    '0D00': '(--SP) = PS',
    '0E00': 'AC <-> (SP)'
}


def parse_no_address_command(command):
    if command in no_address_cmd_mnem:
        return no_address_cmd_mnem[command], no_address_cmd_comm[command]
    else:
        return '', ''


branch = ['Z', 'N', 'V', 'C', 'N(+)V']

branch_mnem = {
    'F0': 'BEQ {}',
    'F1': 'BNE {}',
    'F2': 'BMI {}',
    'F3': 'BPL {}',
    'F4': 'BCS {}',
    'F5': 'BCC {}',
    'F6': 'BVS {}',
    'F7': 'BVC {}',
    'F8': 'BLT {}',
    'F9': 'BGE {}',
}


def parse_branch_command(command, ip):
    if command[0] == 'F' and int(command[1], 16) <= 10:
        mnem = branch_mnem[command[:2:]].format(command[2::])
        comm = 'IF {} == {} THEN\nIP = {}'.format(branch[int(command[1], 16) // 2],
                                                        str((int(command[1], 16) + 1) % 2),
                                                        hex(ip + int(command[2::]))[2::].upper())
        return mnem, comm
    else:
        return '', ''
