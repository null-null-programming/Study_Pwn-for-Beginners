#include <stdio.h>
#include <string.h>

void win(){
    system("/bin/sh");
}

int main(){
    char buff[0x10];

    printf("What's your name?");

    gets(buff);

    printf("Bye,%s!\n",buff);
    return 0;
}