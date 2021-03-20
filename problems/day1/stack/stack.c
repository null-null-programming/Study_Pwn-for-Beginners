#include <stdio.h>

int main(){
    char A[0x8];
    char B[0x8];
    char C[0x8];
    scanf("%s",A);
    scanf("%s",B);
    scanf("%s",C);
    return 0;
}



//rbp     :
//rbp-0x8 :->A="AA.." rbp-0x8~0x10
//rbp-0x10:->B="BB.." rbp-0x10~0x18
//rbp-0x18:->C="CC.." rbp-0x18~0x20