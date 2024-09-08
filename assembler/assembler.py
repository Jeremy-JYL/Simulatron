import sys

opcode = {
    "HLT": "00000000",
    "NOP": "00000001",
    "JMP": "00000010",
    "JCN": "00000011",
    "LD":  "00000100",
    "LDI": "00000101",
    "ST":  "00000110",
    "STI": "00000111",
    "ADD": "00001000",
    "SUB": "00001001",
    "OR":  "00001010",
    "XOR": "00001011",
    "AND": "00001100",
    "NOT": "00001101",
    "OUT": "00001110",
    "IN":  "00001111",
    "PLT": "00010000",
    "CPT": "00010001",
    "JMR": "00010010",
    "MUL": "00010011",
    "DIV": "00010100",
    "MOV": "00010101",
    "CP":  "00010110",
    "INC": "00010111",
    "DEC": "00011000",
    "RIT": "00011001",
    "GCH": "00011010",
    "CMP": "00011011",
    "RET": "00011100",
    "CAL": "00011101"
}

def remove_labels(code):
    labels = {}
    instructions = []
    current_address = 0

    for line in code.split('\n'):
        line = line.strip()
        if not line:
            continue
        elif line.startswith(";"):
            continue
        elif ':' in line:
            label, _ = line.split(':')
            labels[label.strip()] = current_address
        else:
            instructions.append(line)
            current_address += 1

    for i, instruction in enumerate(instructions):
        parts = instruction.split()
        for j, part in enumerate(parts):
            parts[j] = str(labels.get(part, part))
        instructions[i] = ' '.join(parts)

    return '\n'.join(instructions)


def assembler(asm):
    asm = asm.upper()
    return opcode[asm]

def list_to_string(lst):
    return " ".join(map(str, lst))



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Simulatron ASM assembler")
        print("assembler [ASM FILE] [OUTPUT FILE]")
        sys.exit()

    try:
        with open(sys.argv[1], "r") as f:
            code = f.read()
        binary = []
        for i in remove_labels(code).split("\n"):
            if len(i.split()) == 0:
                continue
            binary.append(assembler(i.split()[0]) + " " + list_to_string(i.split()[1:]))
        with open(sys.argv[2], "w") as f:
            for i in binary:
                f.write(i + "\n")
    except FileNotFoundError:
        print(f"Can't find the file: {sys.argv[1]}!")
        sys.exit(1)
    except KeyError:
        print(f"Unknown Instructions: {i}!")
        sys.exit(1)
