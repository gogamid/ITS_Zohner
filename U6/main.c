#include <stdlib.h>
#include <stdio.h>
long long seed;
long long a = 96054250762914, b = 195253620256666;
unsigned int z1 = 3512796597, z2 = 1516901688 ;

unsigned int nextRandom(){
    seed = (seed * a + b) & ((1L << 48) - 1);
    return (unsigned int) (seed >> 16);
}

// function to convert decimal to binary
void decToBinary(long n)
{
    // Size of an integer is assumed to be 32 bits
    for (int i = 63; i >= 0; i--) {
        int k = n >> i;
        if (k & 1)
            printf("1");
        else
            printf("0");
    }
}

int main(int argc, char const *argv[])
{
    // for (size_t i = 0; i < 100000000000; i++)
    // {
    //     unsigned int r = nextRandom();
    //     if (r == 3512796597) {
    //         printf("we have the seed for first %lld\n", seed);
    //         printf("%u\n", nextRandom());
    //     }
    //  }
        //from 355991552 
        //from 0000000000000000000000000000000000010101001110000000000000000000
        //till 356057087
        //till 0000000000000000000000000000000000010101001110001111111111111111
        z2 = z2;
        printf("%u\n", z2);
        decToBinary(z2);
        system("echo hellowrold");
   
    
    
    return 0;
}

