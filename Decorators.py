
import functools

def the_decorator(func):
        @functools.wraps(func)
        def running_func():
            print("your welcome to")
            func()
            print("we have day and boarding students")

        return running_func() 


@the_decorator
def func_toRun():
    print("Irma Preiffer High School") 

func_toRun()