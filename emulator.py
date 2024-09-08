from Simulatron import emulate
import sys

if len(sys.argv) < 3:
    print("Simulatron CPU Emulator")
    print("emulator [BIN FILE] [CLOCK] [DEBUG OUT]")
    print("Clock Flags: M - Manual, N - No Limit")
    sys.exit()
if len(sys.argv) < 4:
    with open(sys.argv[1], "r") as f:
        code = f.readlines()
    emulate.emulate(code, sys.argv[2])

else:
    with open(sys.argv[1], "r") as f:
        code = f.readlines()
    debug = emulate.emulate(code, sys.argv[2], True)
    lst = ""
    for i in debug:
        lst = lst + i
    
    with open(sys.argv[3], "w") as f:
        f.write(lst)
