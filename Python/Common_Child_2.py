# Enter your code here. Read input from STDIN. Print output to STDOUT

# Complete the commonChild function below.
def commonChild(x, y):
    z=[[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            if a == b:
                z[i+1][j+1] = z[i][j] + 1
            else:
                z[i+1][j+1] = max(z[i+1][j], z[i][j+1])
    return z[-1][-1]

x = input()
y = input()
result = commonChild(x, y)
print (result)
