import cobra
from raven_toolbox.tasks import parse_task_list
from config import HUMANGEM_PATH, METABOLIC_TASK_PATH

tasks = parse_task_list(METABOLIC_TASK_PATH)

print("total number of metabolic tasks:", len(tasks))
print("object type:", type(tasks[0]))
print("first task:", tasks[0])

model = cobra.io.read_sbml_model(str(HUMANGEM_PATH))

print("solver:", model.solver.interface.__name__)
solution = model.optimize()

print("status:", solution.status)
print("objective:", solution.objective_value)
print("reactions:", len(model.reactions))
print("genes:", len(model.genes))
print("metabolites:", len(model.metabolites))



