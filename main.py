import cvxpy

allocations = cvxpy.Variable(4)
a, b, c, d = allocations
vars = cvxpy.Variable(4)
u, v, w, x = vars
#u,v,w,x are how much the participants (with two items they want) will put in the first item they want
#in the example in the code -
# u - how much AB puts in A
# v - how much AC puts in A
# w - how much AD puts in A
# x - how much BC puts in C

a = u +v +w + 100
b = x + 100 - u
c = 200 -v -x
d = 100-w

#a,b,c,d - how much budget each item gets

num_of_participants = 5
donations=[]
for i in range(num_of_participants):
    donations.append(100)

utilities = [cvxpy.minimum(a,b), cvxpy.minimum(a,c), cvxpy.minimum(a,d), cvxpy.minimum(b,c), a]


# here is another example -
# a = v +w + 100
# b = x + u
# c = 200 -v -x
# d = 100-w + 100 - u
#
# num_of_participants = 5
# donations=[]
# for i in range(num_of_participants):
#     donations.append(100)

# utilities = [cvxpy.minimum(b,d), cvxpy.minimum(a,c), cvxpy.minimum(a,d), cvxpy.minimum(b,c), a]



sum_of_min_of_each = cvxpy.sum([e for e in utilities])

#constraints
positivity_constraints = [f >= 0 for f in allocations]
sum_constraint = [cvxpy.sum(allocations) == sum(donations)]
value_constraints = [100>=x for x in vars]
value_constraints2 = [0<=x for x in vars]


problem = cvxpy.Problem(
    cvxpy.Maximize(sum_of_min_of_each),
    constraints=positivity_constraints + sum_constraint + value_constraints + value_constraints2)
problem.solve()


print("BUDGET: a={}, b={}, c={}, d={}".format(a.value, b.value, c.value, d.value))
mysum = cvxpy.sum([e for e in utilities])
print ("sum of minimum of each is: " + str(mysum.value))
i = 0
for letter in ("u", "v", "w", "x"):
    print(letter + ": " + str(vars[i].value))
    i+=1
