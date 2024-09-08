.main:
    jmp .label

.label:
    ldi 0 Hello
    out 0
    jmp .display

.display:
    ldi 1 0
    ldi 2 0
    plt 1 2

hlt