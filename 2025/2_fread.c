#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

int main()
{
    int dial = 50;
    int cnt = 0;

    static char in[100000000]; 
    
    size_t len = fread(in, 1, sizeof(in) - 1, stdin);
    in[len] = '\0';

    char *p = in;
    
    while (*p)
    {
        if (*p < 'L') { 
            p++; 
            continue; 
        }

        char cmd = *p++;
        
        int d = 0;
        while (*p >= '0' && *p <= '9') {
            d = d * 10 + (*p - '0');
            p++;
        }

        cnt += d / 100;
        
        d %= 100;

        if (d == 0) continue;

        int prev = dial;

        if (cmd == 'R')
        {
            dial += d;
            if (dial >= 100) 
            {
                dial -= 100;
                cnt++; 
            }
        }
        else // 'L'
        {
            dial -= d;
            if (dial < 0) 
            {
                dial += 100;
                if (prev != 0) cnt++;
            }
            else if (dial == 0)
            {
                if (prev != 0) cnt++;
            }
        }
    }

    printf("%d\n", cnt);
    return 0;
}