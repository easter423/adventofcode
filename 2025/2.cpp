#include <cassert>
#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string>

int mod(int a, int m) noexcept
{
    return (a % m + m) % m;
}

int main()
{
    int dial = 50;
    int cnt = 0;

    std::string s;
    while (std::cin >> s)
    {
        assert(dial >= 0 && dial < 100);

        int d = std::atoi(&s[1]);

        const int rotations = d / 100;
        cnt += rotations;

        d %= 100;

        if (d == 0)
        {
            continue;
        }
        assert(d > 0 && d < 100);

        const int prev = dial;

        if (s[0] == 'R')
        {
            dial = mod(dial + d, 100);
            if (dial < prev)
            {
                cnt++;
            }
        }
        else
        {
            dial = mod(dial - d, 100);
            if ((prev != 0) && (dial == 0 || dial > prev))
            {
                cnt++;
            }
        }
    }

    std::printf("%d\n", cnt);
}