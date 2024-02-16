import math


def binomial_expansion(n):
    if n == 1:
        return "x+y"
    else:
        expansion = ""
        for i in range(n + 1):
            coefficient = int(
                math.factorial(n) / (math.factorial(i) * math.factorial(n - i))
            )
            if coefficient > 0:
                if i > 0:
                    expansion += f"{coefficient}x^{{{n-i}}}y^{{{i}}}"
                else:
                    expansion += f"{coefficient}y^{{{n}}}"
            if i < n:
                if expansion:
                    expansion += " + "
        return expansion


print(binomial_expansion(int(input())))
