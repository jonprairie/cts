import cts.application.menudriver
import cts.testunit.unittest
import cts.application.node
import cts.display.display

tests = []
def p1():
    return 1
def p2():
    return 2
def p3():
    return 3
def p4():
    return 4
def p5():
    return 5
    
en1 = cts.application.node.exteriornode("testing 1", p1)
en2 = cts.application.node.exteriornode("testing 2", p2)
en3 = cts.application.node.exteriornode("testing 3", p3)
en4 = cts.application.node.exteriornode("testing 4", p4)
en5 = cts.application.node.exteriornode("testing 5", p5)
in3 = cts.application.node.interiornode("level 3", [en4, en5])
in2 = cts.application.node.interiornode("level 2", [in3, en3])
in1 = cts.application.node.interiornode("level 1", [in2, en2])

m = cts.application.menudriver.menudriver("menudriver test", [in1, en1])

def test1():
    return m.Select(2)
ev1 = 1

def test2():
    m.JumpToTop()
    m.Select(1)
    r = m.Select(2)
    return r
ev2 = 2

def test3():
    m.JumpToTop()
    m.Select(1)
    m.Select(1)
    m.Select(1)
    m.Select(0)
    return m.Select(2)
ev3 = 3

ut = cts.testunit.unittest.unittest("menudriver unit test", [(test1, ev1), (test2, ev2), (test3, ev3)])
ut.RunTests()