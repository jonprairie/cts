import cts.application.row

class test(cts.application.row.row):
    def __init__(self, test_func, e_v, pre_code=""):
        """test_func is a function that defines the test being run.
            e_v is the expected value returned by test_func.
            pre_code is code wrapped in quotes that should be 'eval'ed before running test_func"""
            
        self.test_func = test_func
        self.e_v = e_v
        self.value = "None"
        self.output = "None"
        cts.application.row.row.__init__(self, dict(value=self.value, output = self.output, expected = self.e_v))
                
    def RunTest(self):
        self.output = self.test_func()
        self.value = (self.e_v == self.output)
        self.UpdateRow("value", self.value)
        self.UpdateRow("output", self.output)