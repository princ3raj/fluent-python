'''Average_object_oriented'''


'''
To summarize: a closure is a function that retains the bindings of the 
free variables that exist when the function is defined, so that they
can be used later when the function is invoked and the defining scope is no longer available.
Note that the only situation in which a function may need to deal
with external variables that are nonglobal is when it is nested in
another function and those variables are part of the local scope of the outer function.

'''

class Averager:

    def __init__(self):
        self.series  = []
    
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return (total / len(self.series))

'''Functional Implementation'''

def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager

avg = Averager()

if __name__ == "__main__":
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg(13))

    average = make_averager()
    print(average(10))
    print(average(11))
    print(average(12))
    print(average(13))
    print(average.__code__.co_varnames)
    print(average.__code__.co_freevars)
    print(average.__closure__)
    print(average.__closure__[0].cell_contents)


'''

It’s obvious where the avg of the Averager class keeps the history:
the self.series instance attribute.
But where does the avg function in the second example find the series?

'''

'''

Note that series is a local variable of make_averager because the assignment series = [] happens in the body of that function.
But when avg(10) is called, make_averager has already returned, and its local scope is long gone.
Within averager, series is a free variable.
This is a technical term meaning a variable that is not bound in the local scope

'''

'''

Inspecting the returned averager object shows how Python
keeps the names of local and free variables in the __code__
attribute that represents the compiled body of the function.

'''

'''

The value for series is kept in the __closure__ attribute of the returned function avg.
Each item in avg.__closure__ corresponds to a name in avg.__code__.co_freevars. 
These items are cells,and they have an attribute called cell_contents
 where the actual value can be found. 
'''

'''
NOTE:

IPython assumed that the secrets.py that I was importing was Python's native secrets.py and not the one I had made.
Rather than mess with path variables or whatever else would be needed to work around this, simply
renaming my secrets.py to something else fixed the problem.
I'm still not sure why this behavior is different in a normal python environment, so if anyone can explain that, I'm all ears.

EDIT: With some guidance, I figured out why they were behaving differently.
Even though IPython's sys.path has the current working directory in it,
it was after the folder where python's secrets.py existed.
So IPython checked that folder, saw that there was a secrets.py,
and assumed that that was the one it was meant to import the API key from.
Whereas with the normal python, the CWD was the first entry in the list,
so it found the correct API key no problem.

'''


