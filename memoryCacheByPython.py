import collections
import functools

class memoized(object):
    """Decorator,Caches a function's return value each time it is called
    if called later with same args,the cached value is returned
    (Not  reevaluated).
    """
    def __init__(self,func):
        self.func = func
        self.cache = {}
    def __call__(self,*args):
        if not isinstance(args,collections.Hashable):
            #uncacheable ,a list ,for instance
            #better to not cache than blow up
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        """return docstring of function"""
        return self.func.__doc__
    def __get__(self,obj,objtype):
        """support instance"""
        return functools.partial(self.__call__,obj)
@memoized
def fibnonacci(n):
    "return the nth fib number"
    if n in (0,1):
        return n
    return fibnonacci(n-1) +fibnonacci(n-2)

print fibonacci(12)







