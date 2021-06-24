
# Python is call by sharing


def ref_demo(x):
    print("x=",x," id=",id(x))
    x=42
    print("x=",x," id=",id(x))

x = 9
print(id(x))

ref_demo(x)
print(id(x))


    