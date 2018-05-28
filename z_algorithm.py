#!/usr/bin/env python
# -*- coding: utf-8 -*-


def z_find(string, pattern):
    matches = []
    z = pattern + "#" + string
    n = len(z)
    Z = z_array(z)
    for i in range(n):
        if Z[i] == len(pattern):
            matches.append(i - len(pattern) - 1)
    return matches


def z_array(string):
    n = len(string)
    Z = [0] * n

    left = right = 0
    for i in range(1, n):
        if i > right:
            left = right = i
            while right < n and string[right - left] == string[right]:
                right += 1
            Z[i] = right - left
            right -= 1
        else:
            k = i - left
            if Z[k] < right - i + 1:
                Z[i] = Z[k]
            else:
                left = i
                while right < n and string[right - left] == string[right]:
                    right += 1
                Z[i] = right - left
                right -= 1
    return Z


if __name__ == '__main__':
    p = 'aab'
    s = 'baabaa'
    print(z_array(p + '#' + s))
    print(z_find(s, p))
