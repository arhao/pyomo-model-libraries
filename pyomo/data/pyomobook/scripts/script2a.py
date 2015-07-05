import pyomo.environ
from pyomo.opt import SolverFactory
from concrete1 import model

model.pprint()

instance = model
instance.pprint()

# @cmd:
opt = SolverFactory('ipopt')
# @:cmd
results = opt.solve(instance)

results.write()
