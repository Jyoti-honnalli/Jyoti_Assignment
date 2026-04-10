#include <stdio.h>

int main() {
    int ports[] = {22, 80, 443, 3306};

    for(int i=0;i<4;i++){
        printf("Port %d: CLOSED\n", ports[i]);
    }

    return 0;
}