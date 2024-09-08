import sys

if __name__ == "__main__":
    print("Core libaries of Simulatron CPU Emulator")
    sys.exit()

def plot_display(lst):
    replaced_list = ['□' if elem == 0 else '■' if elem == 1 else elem for elem in lst]
    return replaced_list


def plot(x, y, plot_lst):
    if plot_lst[y * 16 + x] == 0:
        plot_lst[y * 16 + x] = 1
    else:
        plot_lst[y * 16 + x] = 0


def display(lst, size):
    d = 0
    for i in plot_display(lst):
        if d == size:
            print()
            d = 0
        print(i, end=" ")
        d += 1
    print()
