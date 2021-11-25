#include<stdio.h>

int main(){
    // int num=-4294967296-1; // implicit conversion from 'long' to 'int' changes value from -4294967297 to -1 [-Wconstant-conversion]
    // int num=-4294967296; // implicit conversion from 'long' to 'int' changes value from -4294967296 to 0 [-Wconstant-conversion]

    // int num=-2147483648; // yep, -2^32
    // int num=-2147483647-1; // yep, -(2^32-1)-1
    // int num=2147483647; // yep, 2^32-1
    int num=2147483647+1; // overflow in expression; result is -2147483648 with type 'int' [-Winteger-overflow]

    // int num=-2147483648-1; // implicit conversion from 'long' to 'int' changes value from -2147483649 to 2147483647 [-Wconstant-conversion]

    printf("%d", num);
    printf("\n\n\n\n%d", num);
}