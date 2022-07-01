// A 'C' program to varify the value of x obtained is correct or not.

#include <stdio.h>
#include <math.h>
int main()
{
    int x = 30;
    float y = (sqrt(5 * 30) + sqrt(2 * 30 - 6)) / (sqrt(5 * 30) - sqrt(2 * 30 - 6));
    printf("The value of LHS is %0.0f on putting x=30\n", y);
    if (y == 4)
    {
        printf("Which is equal to RHS of given equation\nHence the solution is correct\n");
    }
    else
    {
        printf("The solution is incorrect");
    }

    return 0;
}