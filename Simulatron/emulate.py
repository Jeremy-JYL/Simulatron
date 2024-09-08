import sys
import traceback

if __name__ == "__main__":
    print("Core libaries of Simulatron CPU Emulator")
    sys.exit()

import time

from Simulatron import cpu
from Simulatron import xyplot

def clock(clk):
    if clk == "M":
        input()
    elif clk == "N":
        pass
    else:
        clk = 1 / int(clk)
        time.sleep(clk)

def emulate(code, clk, d=False):
    pc = 0
    out = ""
    x, y = None, None
    plot = [0] * 256
    cycle = 0
    debug = []
    opc = 0
    while True:
        try:
            # Display
            print("\033[2J\033[1;1H", end="")
            print(f"PC: {pc}")
            print(f"Cycle: {cycle}")
            print(f"Output: {out}")
            # Plot
            if x == -1 and y == -1:
                plot = [0] * 256
                xyplot.display(plot, 16)
            elif x and y:
                xyplot.plot(int(float(x)), int(float(y)), plot)
                xyplot.display(plot, 16)
            else:
                xyplot.display(plot, 16)
            # Debug
            print(code[pc], end="")
            if d:
                debug.append(f"CODE: {code[pc]}PC: {pc}\nCycle: {cycle}\nOut: {out}\nPLT: {x} {y}\nREG: {cpu.reg}\nRAM: {cpu.ram.ram}\n\n")
            # EXEC
            pc, out, x, y, opc = cpu.cpu(code[pc].split()[0], code[pc].split()[1:], pc, opc, out)
            cycle += 1
            # Clock
            clock(clk)
        except cpu.halt:
            if d:
                return debug
            else:
                return
        except KeyboardInterrupt:
            if d:
                return debug
            else:
                return
        except Exception as e:
            if d:
                try:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                    a = ""
                    for i in lines:
                        a = a + i
                    debug.append(f"EMU ERROR: {e}\n{a}")
                    print("EMU ERROR")
                    return debug
                except:
                    return list(f"EMU ERROR: {str(e)}")
            else:
                return

