import cobra

model = cobra.io.read_sbml_model("../raw_data/Human-GEM.xml")

print(model)
print(len(model.reactions))
print(len(model.metabolites))
print(len(model.genes))

## objective funtion
print(model.objective)

rxn = model.reactions.get_by_id("MAR13082")
print(rxn.id)
print(rxn.name)
print(rxn.reaction)

## baseline growth
solution = model.optimize()
print("status:", solution.status)
print("objective_value:", solution.objective_value)

## uptake reactions
medium = model.medium
print("n uptake reactions:", len(medium))

for rxn_id, uptake in list(medium.items())[:10]:
    rxn = model.reactions.get_by_id(rxn_id)
    print(rxn_id,:verbose map <C-CR> rxn.name, uptake)

# atp exchange reaction
atp_ex = model.reactions.get_by_id("MAR00569")

print("ID:", atp_ex.id)
print("Name:", atp_ex.name)
print("Reaction:", atp_ex.reaction)
print("Lower bound:", atp_ex.lower_bound)
print("Upper bound:", atp_ex.upper_bound)
