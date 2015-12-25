import cts.testunit.test
import cts.application.stringtable
import cts.display.display

class unittest:
    def __init__(self, name, test_tuples, pre_code=""):
        """test_tuples should be a list of the form (test_func, e_v)"""
            
        self.name = name
        self.tests = []
        for (t_f, e_v) in test_tuples:
            temp_test = cts.testunit.test.test(t_f, e_v)
            self.tests.append(temp_test)
            
        self.test_table = cts.application.stringtable.stringtable(self.name, self.tests)
        
    def RunTests(self):
        for t in self.tests:
            t.RunTest()
        self.Results()
            
    def Results(self):
        cts.display.display.DisplayStringTable(self.test_table, pause=1)