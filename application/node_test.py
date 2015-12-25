import cts.testunit.unittest
import cts.application.node
import cts.display.display

tests = []
def p1():
    return 7
def p2():
    return 25
def p3():
    return 8
    
en1 = cts.application.node.exteriornode("testing 1", p1)
en2 = cts.application.node.exteriornode("testing 2", p2)
e_nodes = [en1, en2]
pn1 = cts.application.node.rootnode("nodeTest 1", e_nodes, dynamic=1)
en3 = cts.application.node.exteriornode("testing 3", p3)
e_nodes.append(en3)
pn1.Refresh()

def test1():
    return len(pn1.children_dict)
ev1 = 3    

def test2():
    return pn1.Select(2).Select()()    
ev2 = 25

tests.append((test1, ev1))
tests.append((test2, ev2))

ut = cts.testunit.unittest.unittest("nodeTest", tests)
ut.RunTests()