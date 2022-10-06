'''A broken implementation of make_averager


def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        total += new_value
        count+=1
        return total / count
    return averager



'''

'''
Moral of The Story:


The problem is that the statement count += 1 actually means the same as count = count + 1,
when count is a number or any immutable type. So we are actually assigning to count
in the body of averager, and that makes it a local variable.
The same problem affects the total variable.
We did not have this problem in Example 9-8 because we never assigned
to the series name; we only called series.append and invoked sum and len on it.
So we took advantage of the fact that lists are mutable.
But with immutable types like numbers, strings, tuples, etc., 
all you can do is read, never update. If you try to rebind them, as 
in count = count + 1, then you are implicitly creating a local variable count. 
It is no longer a free variable, and therefore it is not saved in the closure.
To work around this, the nonlocal keyword was introduced in Python 3. 
It lets you declare a variable as a free variable even when it is assigned
'''

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager



if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))