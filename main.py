import sympy
from fractions import Fraction

A = []
B = []
k = 0
g = 0
LU, values, L, U = [], [], [], []

n = int(input("number of equations : "))


def printer_2dimensions(any_list, lenght):  # NOQA
    for LINES in range(n):
        print("∣  ", end="")
        for COLUMNS in range(n):
            try:
                print(
                    f"{str(Fraction(float(any_list[LINES][COLUMNS])).limit_denominator(max_denominator=100000)):{int(lenght)}}",
                    end=' ')
            except (ValueError, TypeError):
                print(f"{str(any_list[LINES][COLUMNS]):{int(lenght)}}", end=' ')
        print("∣")
    print()


def is_number(num):
    try:
        float(num)
        return True
    except (ValueError, TypeError):
        return False


def printer_1dimension(any1_list):
    for K in any1_list:
        try:
            print(f"∣  {str(Fraction(K).limit_denominator(max_denominator=100000)):3} ∣")
        except (ValueError, TypeError):
            print(f"∣ {K} ∣")
    print()


def formatter(equation):
    variable = 0
    eq = []
    while equation[variable] != "=":
        eq.append(equation[variable])
        variable += 1
    if equation[equation.index("=") + 1] == "-":
        eq.append("+")
        for chars in range(equation.index("=") + 2, len(equation)):
            eq.append(equation[chars])
        return str(''.join(eq))
    else:
        eq.append("-")
        for chars in range(equation.index("=") + 1, len(equation)):
            eq.append(equation[chars])
        return str(''.join(eq))


# making the matrix
for lines in range(n):
    lines_list = []
    equations = input(f"Equation {lines + 1} = ")
    for columns in range(n):
        if columns == 0:
            v = float(equations[0: equations.index("x")])
        else:
            v = float(equations[
                      equations.index("xyzabcdefghijklmnopqrstuvw"[columns - 1]) + 1: equations.index(  # NOQA
                          "xyzabcdefghijklmnopqrstuvw"[columns])])  # NOQA

        lines_list.append(v)
    w = equations[equations.index("=") + 1::]
    B.append(float(w))
    A.append(lines_list)
print("A : ")
printer_2dimensions(A, 6)
# making L
for i in range(n):  # List with 0's
    L_lines = []
    for j in range(n):
        L_lines.append(0)
    L.append(L_lines)

for j in range(n):  # Lower Part
    for i in range(0, j + 1):
        L[j][i] = "abcdefghijklmnopqrstuvwxyz"[g]  # NOQA
        g += 1
print("L : ")
printer_2dimensions(L, 6)
# making list with 0's
for _ in range(n):
    U_list = []
    for _ in range(n):
        U_list.append(0)
    U.append(U_list)
# making U
for i in range(n):  # upper part
    for j in range(n):
        U[i][j] = L[j][i]  # NOQA
print("U : ")
printer_2dimensions(U, 6)


def update():
    global LU
    LU1 = sympy.Matrix(L).multiply(sympy.Matrix(U))  # NOQA
    LU = []
    k = 0  # NOQA
    for i in range(n):  # NOQA  # making LU1 into LU =  List inside Lists
        l_lines = []
        for j in range(n):  # NOQA
            l_lines.append(LU1[k])
            k += 1
        LU.append(l_lines)


update()
print("L*U : ")
printer_2dimensions(LU, 24)
print("L*U = A :\n")

for i in range(n):  # printing the equations
    for j in range(n):
        print(f"{LU[i][j]} = {A[i][j]}")

for y in range(n):
    for t in range(n):
        if not is_number(U[y][t]):
            var = sympy.symbols(U[y][t])
            values.append(str(U[y][t]) + " = " + str(
                Fraction(str(sympy.solve(formatter(f"{LU[y][t]}={A[y][t]}"), var)[-1])).limit_denominator(
                    max_denominator=10000)))
            for er in range(n):
                for er2 in range(n):
                    if L[er][er2] == str(var):
                        L[er][er2] = str(  # NOQA : 139
                            Fraction(str(sympy.solve(formatter(f"{LU[y][t]}={A[y][t]}"), var)[-1])).limit_denominator(
                                max_denominator=10000))
            U[y][t] = str(Fraction(str(sympy.solve(formatter(f"{LU[y][t]}={A[y][t]}"), var)[-1])).limit_denominator(
                max_denominator=10000))
            update()

    update()
print()

for f in range(3 * n - 3):
    print(values[f])

print("L : ")
printer_2dimensions(L, 6)
print("U : ")
printer_2dimensions(U, 6)
Y = []
for h in range(n):  # making Y
    Y.append("abcdefghujklmnopqrstuvw"[h])  # NOQA
LY = []


def update2():
    global LY
    LY = []
    LY1 = sympy.Matrix(L).multiply(sympy.Matrix(Y))  # NOQA
    for y in range(n):  # NOQA
        LY.append(LY1[y])


update2()
for l in range(n):  # NOQA  # finding Y
    var3 = sympy.symbols("abcdefghijklmnopqrstuvwxyz"[l])  # NOQA
    Y[l] = str(
        Fraction(str(sympy.solve(formatter(f"{LY[l]}={B[l]}"), var3)[-1])).limit_denominator(max_denominator=10000))
    update2()

print("Y : ")
printer_1dimension(Y)
X = []
for x in range(n):  # making X
    X.append("xyzabcdefghujklmnopqrstuvw"[x])  # NOQA
UX = []


def update3():
    global UX
    UX = []
    UX1 = sympy.Matrix(U).multiply(sympy.Matrix(X))  # NOQA
    for v in range(n):  # NOQA
        UX.append(UX1[v])


update3()
print('UX = Y :')
for j in range(n):  # UX = Y
    print(f"{UX[j]} = {Y[j]}")
charac = n - 1  # NOQA
for x in range(n - 1, -1, -1):  # finding X
    var4 = sympy.symbols("xyzabcdefghijklmnopqrstuvw"[charac])  # NOQA : 204
    X[x] = str(
        Fraction(str(sympy.solve(formatter(f"{UX[x]} = {Y[x]}"), var4)[-1])).limit_denominator(max_denominator=10000))
    update3()
    charac -= 1
print("X : ")
printer_1dimension(X)
counter = 0
for answers in X:
    print(
        f'{"xyzabcdefghijklmnopqrstuvwxyz"[counter]} = {str(Fraction(answers).limit_denominator(max_denominator=100000))}')  # NOQA
    counter += 1
