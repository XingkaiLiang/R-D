def add(a,b):
    print "add %d+%d " % (a,b)
    return a+b

def substract(a,b):
    print "subs %d - %d" % (a,b)
    return a-b
age = add(230,34)
height = substract(23,5)
minus = substract(3,4999)

print "age: %d,height:%d,minus:%d" % (age,height,minus)
