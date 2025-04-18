x = 10

def test() :
    x = 20

test()
print(x)
# print(x) >>> 10 출력


def test() :
    global x
    x = 20

test()
print(x)
# print(x) >>> 20 출력


# def fact(x) :
#     value = 1
#     for i in range(x, 0, -1) :
#         value *= i
#     print(value)

# result = fact(5)
# >>> result = 5*4*3*2*1

def fact(x) :
    if x == 0 :
        return 1
    else :
        # x * (x-1) * (x-2) ...
        return x * fact(x-1)
        # x = 5 >> 5 * fact(4) >> 5 * 4 * fact(3) ...
print(fact(5))

