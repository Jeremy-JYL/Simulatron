import sys

if __name__ == "__main__":
    print("Core libaries of Simulatron CPU Emulator")
    sys.exit()

from Simulatron import ram
import random, getch

reg = [0] * 16


class halt(Exception):
    pass


def read(address):
    try:
        return reg[int(address)]
    except ValueError:
        raise Exception("Unknown Reg Address!")


def write(address, data):
    try:
        reg[int(address)] = data
    except IndexError:
        raise Exception("Reg Over Flow!")
    except ValueError:
        raise Exception("Unknown Reg Address!")

def list_to_string(lst):
    return " ".join(map(str, lst))

def cpu(opcode, operand, pc, opc, out):
    x = None
    y = None
    pc += 1

    match opcode:
        case "00000000":
            raise halt
        case "00000001":
            pass
        case "00000010":
            pc = int(operand[0])
        case "00000011":
            if read(operand[0]) == read(operand[1]):
                pc = int(operand[2])
            else:
                pass
        case "00000100":
            write(operand[0], ram.read(operand[1]))
        case "00000101":
            write(operand[0], list_to_string(operand[1:]))
        case "00000110":
            ram.write(operand[0], read(operand[1]))
        case "00000111":
            ram.write(operand[0], list_to_string(operand[1:]))
        case "00001000":
            write(operand[0], '{0:g}'.format(float(read(operand[1])) + float(read(operand[2]))))
        case "00001001":
            write(operand[0], '{0:g}'.format(float(read(operand[1])) - float(read(operand[2]))))
        case "00001010":
            if read(operand[1]) or read(operand[2]):
                write(operand[0], "1")
        case "00001011":
            if read(operand[1]) != read(operand[2]):
                write(operand[0], "1")
        case "00001100":
            if read(operand[1]) and read(operand[2]):
                write(operand[0], "1")
        case "00001101":
            if not read(operand[1]):
                write(operand[0], "1")
            else:
                write(operand[0], "0")
        case "00001110":
            out = ""
            for i in operand[0:]:
                out = out + read(i) + " "
        case "00001111":
            write(operand[0], input("? "))
        case "00010000":
            x = read(operand[0])
            y = read(operand[1])
        case "00010001":
            x = -1
            y = -1
        case "00010010":
            pc = int(read(operand[0]))
        case "00010011":
            write(operand[0], '{0:g}'.format(float(read(operand[1])) * float(read(operand[2]))))
        case "00010100":
            write(operand[0], '{0:g}'.format(float(read(operand[1])) / float(read(operand[2]))))
        case "00010101":
            write(operand[0], read(operand[1]))
            write(operand[1], 0)
        case "00010110":
            write(operand[0], read(operand[1]))
        case "00010111":
            write(operand[0], '{0:g}'.format(float(read(operand[1])) + 1))
        case "00011000":
            write(operand[0], '{0:g}'.format(float(read(operand[1])) - 1))
        case "00011001":
            write(operand[0], random.randint(int(read(operand[1])), int(read(operand[2]))))
        case "00011010":
            write(operand[0], str(ord(getch.getch())))
        case "00011011":
            if read(operand[3]) == read(operand[4]):
                write(operand[0], "1")
            else:
                write(operand[0], "0")
            if read(operand[3]) < read(operand[4]):
                write(operand[1], "1")
            else:
                write(operand[1], "0")
            if read(operand[3]) > read(operand[4]):
                write(operand[2], "1")
            else:
                write(operand[2], "0")
        case "00011100":
            pc = opc
            opc = 0
        case "00011101":
            opc = pc
            pc = int(operand[0])
        case _:
            raise Exception(f"Unknown machine code! Please reassemble your code!")
    return pc, out, x, y, opc
