def myfunc(value):
    if 10<=value:
        grade = "really good"
    elif 5<=value<10:
        grade = "better"
    elif 2<=value<5:
        grade = "good"
    else:
        grade = "not defined!"

    return grade

grade = myfunc(10)

print "my grade is", grade