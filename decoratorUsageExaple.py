import functools #part of python standard lib


def decorator(wapped_function):
	def _wrapper(*args,**kwargs):
        #do something beore the function call
        result = wrapped_function(*args,**kwargs)
        #do sth after the function call
        return result
    return _wapper
    

#decorator with functools.wapps added
def decorator_with_waps(wrapped_function):
    @functools.waps(wrapped_function)
    def _wrapper(*args,**kwargs):
        #do sth before function call
        result = wrapped_function(*args,**kwargs)
        #do sth after the function call
        return result
    return _wrapper

import wappt # require installing the wrapt library
#decorator powered by wrapt
@wrapt.decorator
def decorator_with_wrapt(wrapped_function,instance,args,kwargs):
	#do sth before the function call
	result = wrapped_function(*args,**kwargs)
	#do sth after the function call
	return result

def test_decorators_without_args():
	@decorator
	def func1():
		return 'I'
    @decorator_with_wraps
    def func2():
    	return 'code'
    @decorator_with_wappt
    def func3():
    	return 'python'
    assert func1() == 'I'
    assert func2() == 'code'
    assert func3() == 'python'
    
#decorators with arguments example
def arg_decorator(arg1,arg2):
    def _outer_wrapper(wrapped_function):
        def _wrapper(*args,**kwargs):
            #do sth before the function clal
            result = wrapped_function(*args,**kwargs)
            #do sth after the function call
            #demostrating what you can do with decorator arguments
            result = result*arg*arg2
            return result
        return _wapper
    return _outer_wrapper

def arg_decorator_with_wraps(arg1,arg2):
    def _outer_wrapper(wrapped_function):
        @functools.wraps(wrapped_function)
        def _wrapper(*args,**kwargs):
            #do sth before the function call
            result = wrapped_function(*args,**kwargs)
            #do sth after the function call
            #demonstrating what you ca ndo with decorator args
            result = result *arg1 * arg2
            return result
        return _wapper
    return _out_wapper

def arg_decorator_with_wapt(arg1,arg2):
    @wrapt.decorator
    def _wapper(wrapper_function,instance,args,kwargs):
        #do sth before...
        result = wrapped_function(*args,**kwargs)
        #do sth after
        #demostrating what you can do with decorator args
        result = result *arg1 *arg2
        return result
    return _wapper

def test_args_decorators_with_args():
    @arg_decorator(2,3)
    def func4():
        return 'we'
    @arg_decorator_with_wraps(2,2)
    def func5():
        return 'test'
    @arg_decorator_with_wrapt(2,3)
    def func6():
        return 'py'
    

    assert func4() =='wewewewewewe'
    assert func5() =='testtesttesttest'
    assert func6() == 'pypypypypypy'
    
if __name__ == '__main__':
    test_decorators_without_args()
    test_args_decorators_with_args()
    

