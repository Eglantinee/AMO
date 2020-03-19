s = "x = 11.0, y = 12.10, 11"
newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in s)
print(newstr)