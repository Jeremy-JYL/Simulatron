; A pixel can move with wasd and q for quit
; This is a very bad example it missing error handling and more
; Note: please run it with N clock flag for best performance, Arrow key: 500

; Arrow Keys
; ldi 1 65
; ldi 2 68
; ldi 3 66
; ldi 4 67

; WASD
ldi 1 119
ldi 2 97
ldi 3 115
ldi 4 100

ldi 5 113
ldi 6 0
ldi 7 0


plt 6 7
main:
    out 6 7
    gch 0
    jcn 0 1 .w
    jcn 0 2 .a
    jcn 0 3 .s
    jcn 0 4 .d
    jcn 0 5 .q
    jmp main
    .w:
        cpt
        ldi 0 1
        sub 7 7 0
        plt 6 7
    jmp main
    .a:
        cpt
        ldi 0 1
        sub 6 6 0
        plt 6 7
    jmp main
    .s:
        cpt
        ldi 0 1
        add 7 7 0
        plt 6 7
    jmp main
    .d:
        cpt
        ldi 0 1
        add 6 6 0
        plt 6 7
    jmp main
    .q:
        hlt
