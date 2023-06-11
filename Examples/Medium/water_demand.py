from dwave.system import DWaveSampler, EmbeddingComposite
# from dwave.system import LeapHybridSampler
from dimod import BinaryQuadraticModel

# Set up the problem
pumps = [0, 1, 2, 3]
costs = [[36, 27],
        [56, 65],
        [48, 36],
        [52, 16]
]
flow = [2, 7, 3, 8]
demand = 20
time = [0, 1]


# Build a variable for each pump
x = [[f'P{p}_AM', f'P{p}_PM'] for p in pumps]

# Initialize BQM()
bqm = BinaryQuadraticModel('BINARY')

# Objective
for p in pumps:
  for t in time:
    bqm.add_variable(x[p][t], costs[p][t])

# Constraint 1: Every pump runs at least once per day
for p in pumps:
  c1 = [(x[p][t], 1) for t in time]
  bqm.add_linear_inequality_constraint(
      c1, lb=1, ub=len(time), lagrange_multiplier=13, 
      label='c1_pump_'+str(p)
  )

# Constraint 2: At any time, at most 3 pumps can run
for t in time:
  c2 = [(x[p][t], 1) for p in pumps]
  bqm.add_linear_inequality_constraint(
      c2, constant=-3, lagrange_multiplier=1,
      label='c2_time_'+str(t)
  )

# Constraint 3: We need to satify demand for the day
c3 = [(x[p][t], flow[p]) for t in time for p in pumps]
bqm.add_linear_equality_constraint(
    c3, constant=-demand, lagrange_multiplier=28
)


sampler = EmbeddingComposite(DWaveSampler())  # Let DWave decide the embedding
sampleset = sampler.sample(bqm, num_reads=1000)

sample = sampleset.first.sample
total_flow = 0
total_cost = 0

print('\n\tAM\tPM')
for p in pumps:
  printout = 'P' + str(p)
  for t in time:
    printout += '\t' + str(sample[x[p][t]])
    total_flow += sample[x[p][t]]*flow[p]
    total_cost += sample[x[p][t]]*costs[p][t]
  print(printout)


print('\nTotal flow:\t', total_flow)
print('\nTotal cost:\t', total_cost)