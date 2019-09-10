import cobra

model = cobra.io.read_sbml_model("test_model.xml")
print("Model:")
print(len(model.reactions),"reactions")
print(len(model.metabolites),"metabolites")
print(len(model.genes),"genes")

biomass_rxn = model.reactions.get_by_id("BIO0100")
model.objective = biomass_rxn
medium = model.medium
medium["O2_Exchange_reactions_e"] = 1000
medium["EXC0050"] = 1000
print(medium)
model.medium = medium
with model:
    solution = model.optimize()
print("---------------------------------------------")
print("Solution:")
print(solution.objective_value)
print(solution.status)
