# The following helps accept multiple user input
z, x, c = map(int, input().split())
if (c>x or c>z):
    print("PASS")
else:
    print("FAIL")