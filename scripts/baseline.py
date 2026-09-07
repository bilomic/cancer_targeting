
# load model and build hams medium

from functions import load_human_gem, build_hams_medium

model = load_human_gem()
medium = build_hams_medium()

model.medium = medium

solution = model.optimize()

print("Medium components:", len(model.medium))
print("Status:", solution.status)
print("Biomass:", solution.objective_value)

# which nutrients is the model using?
import cobra as cob

pfba_solution = cob.flux_analysis.pfba(model)

for rxn_id in medium:
    flux = pfba_solution.fluxes[rxn_id]

    if flux < -1e-6:
        print(rxn_id, model.reactions.get_by_id(rxn_id).name, flux)

# there are some satured uptake bounds. let's isolate them.

print("\nuptake reactions at their maximum bound:")

for rxn_id, bound in medium.items():
    flux = pfba_solution.fluxes[rxn_id]

    if flux < -1e-6:
        saturation = -flux / bound

        if saturation > 0.99:
            rxn = model.reactions.get_by_id(rxn_id)
            print(rxn.name, flux, "saturation", saturation)
    
# 21 of the uptake reactions are running at their maximum flux of 10. So, the biomass reaction of 20.36 is not a robust prediction.
# Next step is to restructure the medium function in a way that the organic uptake reactions can vary a little bit.

organic_bounds = [5, 10, 50, 100, 1000]

sensitivity_results = []

for bound in organic_bounds:
    with model:
        medium = build_hams_medium(organic_uptake=bound)
        model.medium = medium

        solution = model.optimize()

        sensitivity_results.append(
            {
                "organic_uptake": bound,
                "biomass": solution.objective_value
            }
        )

print(sensitivity_results)

import pandas as pd

sensitivity_df = pd.DataFrame(sensitivity_results)

print(sensitivity_df)

sensitivity_df.to_csv(
    "results/medium_sensitivity.csv",
    index=False
)

# sensitivity curve
import matplotlib.pyplot as plt

plt.plot(
    sensitivity_df["organic_uptake"],
    sensitivity_df["biomass"],
    marker="o"
)

plt.xlabel("Maximum organic uptake")
plt.ylabel("Predicted biomass flux")
plt.title("Sensitivity of biomass to organic uptake bound")
plt.xscale("log")

plt.savefig(
    "results/medium_sensitivity.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

