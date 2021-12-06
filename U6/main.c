#include <stdlib.h>
#include <stdio.h>
long long seed;
long long a = 96054250762914, b = 195253620256666;
unsigned int z1 = 3512796597, z2 = 1516901688;

unsigned int nextRandom(){
    seed = (seed * a + b) & ((1L << 48) - 1);
    return (unsigned int) (seed >> 16);
}



// function to convert decimal to binary
void decToBinary(long n)
{
    // Size of an integer is assumed to be 32 bits
    for (int i = 47; i >= 0; i--) {
        int k = n >> i;
        if (k & 1)
            printf("1");
        else
            printf("0");
    }
}

int main(int argc, char const *argv[])
{
        //3512796597 << 16

        //230214637780992 = 110100010110000100000101101101010000000000000000

        //230214637846527 = 110100010110000100000101101101011111111111111111
        
        for (long long i = 230214637780992; i < 230214637846528; i++)
        {
            seed = (i * a + b) & ((1L << 48) - 1);
            unsigned int z =(unsigned int) (seed >> 16);
            if (z == z2) {
                printf("%lld\n", seed);
                break;
            }
        }
    return 0;
}

