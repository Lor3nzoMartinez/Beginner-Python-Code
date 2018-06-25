import sys

def day_name(Num):
    if Num == 1:
        return 'Monday'
    if Num == 2:
        return 'Tuesday'
    if Num == 3:
        return 'Wednesday'
    if Num == 4:
        return 'Thursday'
    if Num == 5:
        return 'Friday'
    if Num == 6:
        return 'Saturday'
    if Num == 0:
        return 'Sunday'

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_suite():
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
   
     
test_suite()

