import sys

if __name__ == "__main__":
    print("Core libaries of Simulatron CPU Emulator")
    sys.exit()

ram = [0] * 64

def write(address, data):
    try:
        ram[int(address)] = data
    except IndexError:
        raise Exception("Ram Over Flow!")
    except ValueError:
        raise Exception("Unknown Ram Address!")


def read(address):
    try:
        return ram[int(address)]
    except ValueError:
        raise Exception("Unknown Ram Address!")

def reset():
    ram = [0] * 64
