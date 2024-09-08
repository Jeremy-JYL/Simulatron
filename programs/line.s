.main:
    ldi 0 0
    ldi 1 1
    ldi 2 16
    .plot:
        plt 0 0
        add 0 0 1
        jcn 0 2 .hlt
        jmp .plot
        
.hlt:
    hlt
