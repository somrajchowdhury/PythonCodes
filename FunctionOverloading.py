class function_overload:

    '''
    function to add
    takes as many parameters as user wants
    '''
    def add(self, *args):
        result = 0
        for i in args:
            result = result + i
        return result

obj1 = function_overload()
print('Result = ',obj1.add(1,2))
print('Result = ',obj1.add(1,2,3))


