#include <stdio.h>
#include <string.h>

void win(){
    system("/bin/sh");
}

char password[]="n4mele55";

int main(){
    char buff[0x10];

    printf("pwssword: ");
    scanf("%s",buff);

    if(strcmp(buff,password)==0){
        win();
    }else{
        printf("invalid\n");
    }

    return 0;
}