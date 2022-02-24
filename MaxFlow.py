from pyomo.environ import *

model = AbstractModel()

# Nodes in the network
model.N = Set()

# Network arcs, initializing with node information previously declared
model.A = Set(within=model.N*model.N)

# Source node
model.s = Param(within=model.N)
# Sink node
model.t = Param(within=model.N)
# Flow capacity limits
model.c = Param(model.A)


# The flow over each arc
model.x = Var(model.A, within=NonNegativeReals)


# Define rule to calculate the flow into the sink nodes
def total_rule(model):
    return sum(model.x[i,j] for (i, j) in model.A if j == value(model.t))

# Add it to the model as an objective function to maximize
model.total = Objective(rule=total_rule, sense=maximize)

# Enforce an upper limit on the flow across each arc
def limit_rule(model, i, j):
    return model.x[i,j] <= model.c[i, j]

# Add the rule to the model
model.limit = Constraint(model.A, rule=limit_rule)

# Enforce flow through each node
def flow_rule(model, k):
    if k == value(model.s) or k == value(model.t):
        return Constraint.Skip # Note here you can skip the rule for certain conditions
    
    inFlow  = sum(model.x[i,j] for (i,j) in model.A if j == k)
    outFlow = sum(model.x[i,j] for (i,j) in model.A if i == k)
    return inFlow == outFlow
model.flow = Constraint(model.N, rule=flow_rule)
