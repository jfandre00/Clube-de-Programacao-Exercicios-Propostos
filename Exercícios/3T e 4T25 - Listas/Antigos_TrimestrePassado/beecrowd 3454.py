s = input().strip()

if s.count('X') != 2 or s.count('O') != 1:
    print("?")
else:
    if (s[0] == 'X' and s[1] == 'X') or (s[1] == 'X' and s[2] == 'X'):
        print("Alice")
    else:
        print("*")