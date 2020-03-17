import os
from src.trace_parse import parse
from src.word.word import word
from src.program_parse import parse_program_file

#
#       This program make program and trace table in Word(report/trace.docx)
#           Before running it. You have to make sure that report/trace.docx is closed.
#           In src file it you can find source code.
#           This program need data/trace.txt file that you can make by running 'executor.exe'
#


def main():
    directory = os.path.split(os.path.abspath(__file__))[0]
    regs, mem_diff = parse(directory)
    start_program, program = parse_program_file(directory)
    word(directory, start_program, program, regs, mem_diff)


if __name__ == "__main__":
    main()
