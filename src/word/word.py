from docx import Document
from .trace_reg_mem import trace
from .program_table import program_table

#
#   Generate Word report
#


def word(directory, start_program, program, regs, diff_mem):
    d = Document()
    trace(regs, diff_mem, start_program, d)
    program_table(program, d)
    is_open = True
    while is_open:
        try:
            d.save(directory + '//report//trace.docx')
            is_open = False
        except PermissionError:
            is_open = True
            print('Close report/trace.docx to save trace.')
            input()
