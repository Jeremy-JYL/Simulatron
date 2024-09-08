;########################################
; Simple XYPLOTER (8x8) type Q to exit! #
;########################################

.main:
    ldi 0 XYPLOTER (16x16) Press "Q" To Quit!
    out 0
    in 0
    ldi 2 Q
    .need:
        ldi 0 X
        out 0
        in 0
        ldi 1 Y
        out 1
        in 1
        jcn 0 2 .hlt
        jcn 1 2 .hlt
        plt 0 1
        jmp .need

.hlt:
    hlt