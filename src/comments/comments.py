from .contol_unit import *


def comment(ip, command):
    mnem, comm = parse_no_address_command(command)

    if command[:2:] == 'CE':
        mnem = 'JUMP IP + {} + 1'.format(command[2::])
        comm = 'IP = {}'.format(hex(int(command[2::], 16) + ip)[2::].upper())
        return mnem, comm
    else:
        if mnem != '':
            return mnem, comm
        else:
            mnem, comm = parse_address_command(command, ip)

            if mnem != '':
                return mnem, comm
            else:
                mnem, comm = parse_branch_command(command, ip)

                if mnem != '':
                    return mnem, comm
                else:
                    return '', ''
