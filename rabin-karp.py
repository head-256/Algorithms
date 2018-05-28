#!/usr/bin/env python
# -*- coding: utf-8 -*-


def hashcode(string):
    h = 0
    n = len(string)
    for i in range(n):
        h = 256 * h + ord(string[i])
    return h


def rabin_karp(pattern, string):
    matches = []
    n, m = len(string), len(pattern)
    pattern_hash = string_hash = 0
    alphabet_size = 256
    table_size = 101

    h = 1
    for i in range(1, m):
        h = (h * alphabet_size) % table_size

    for i in range(m):
        pattern_hash = (alphabet_size * pattern_hash + ord(pattern[i])) % table_size
        string_hash = (alphabet_size * string_hash + ord(string[i])) % table_size

    for i in range(n - m + 1):
        if pattern_hash == string_hash:
            j = 0
            while j < m:
                if string[i + j] != pattern[j]:
                    break
                j += 1
            if j == m:
                matches.append(i)

        if i < n - m:
            string_hash = (alphabet_size * (string_hash - ord(string[i]) * h) + ord(string[i + m])) % table_size
            if string_hash < 0:
                string_hash += table_size

    return matches


if __name__ == '__main__':
    print(hashcode('cats'))
    print(rabin_karp('cats', 'my cats the best cats from all cats'))
