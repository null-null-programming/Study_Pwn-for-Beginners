#include <stdio.h>
#include <string.h>

void win(){
    system("/bin/sh");
}

int main(){
    char buff[0x10];

    printf("What's your name?");

    gets(buff);
//next_addr -> stack
//next_addr -> win()
//ret2win
//next_addr  -> 0x4141414141...
    printf("Bye,%s!\n",buff);
    return 0;
}