; C to F Calc

.main:
    in 0

    ldi 1 9
    ldi 2 5

    div 3 1 2

    mul 4 0 3

    ldi 5 32
    add 4 4 5

    out 4

    jmp .hlt

.hlt:
    hlt

