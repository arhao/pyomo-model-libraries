from pyomo.environ import *

model = AbstractModel()

# @decl:
model.A = Set(dimen=2)
model.B = Param(model.A)
# @:decl

instance = model.create('param5a.dat')

keys = instance.B.keys()
for key in sorted(keys):
    print(str(key)+" "+str(value(instance.B[key])))
