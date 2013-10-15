# Writing recursive functions and seeing if they work

# Simple summation recursion which sums all numbers up to and including x.
def sum_up_to(x):
    if x == 1:
        return x
    else:
        return x + sum_up_to(x-1)

print sum_up_to(5)