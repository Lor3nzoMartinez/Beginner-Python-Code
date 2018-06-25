import sys

def turn_clockwise(dir):
    if dir == 'N' :
        return 'E'
    if dir == 'E' :
        return 'S'
    if dir == 'S' :
        return 'W'
    if dir == 'W' :
        return 'N'
    else:
        return None
 
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_suite():
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
 
test_suite()
