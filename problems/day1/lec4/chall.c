#include <stdio.h>
#include <string.h>

void win(){
    system("/bin/sh");
}

int main(){
    char my_name[]="null_null";
    char buff[0x10];

    printf("I want to be nullptr... : ");
    scanf("%s",buff);

    if(strcmp(my_name,"nullptr")==0){
        win();
    }

    return 0;
}