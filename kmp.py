#!/usr/bin/env python
# -*- coding: utf-8 -*-


def prefix_table(p):
    m = len(p)
    pi = [0] * m
    length = 0
    i = 1
    while i < m:
        if p[i] == p[length]:
            length += 1
            pi[i] = length
            i += 1
        else:
            if length != 0:
                length = pi[length - 1]
            else:
                pi[i] = 0
                i += 1
    return pi


def kmp(string, pattern):
    matches = []
    n, m = len(string), len(pattern)
    pi = prefix_table(pattern)
    i = j = 0
    while i < n:
        if pattern[j] == string[i]:
            j += 1
            i += 1
        if j == m:
            matches.append(i - j)
            j = pi[j - 1]
        elif i < n and pattern[j] != string[i]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1
    return matches


if __name__ == '__main__':
    print(kmp('acbacaacaacacaacab', 'a'))
