#include <stdio.h>
#include <string.h>

void win(){
    system("/bin/sh");
}

int main(){
    char my_name[]="null_null";
    char buff[0x10];

    printf("My name is ... : ");
    scanf("%s",buff);
    printf("%s!",my_name);

    if(strcmp(my_name,"null_null")!=0){
        win();
    }

    return 0;
}