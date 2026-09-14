
import pandas as pd

# import reference table from a study for human cancer medium
path = "raw_data/references/mmc3.xlsx"

medium_table = pd.read_excel(
        path, sheet_name = "Supplementary Table 3", header = 2)

print("Dimensions:", medium_table.shape)
print("Columns:", medium_table.columns.to_list())
print(medium_table.head())

# import reactions.tsv from github from human gem authors for mapping

reactions = pd.read_csv(
        "raw_data/references/reactions.tsv",
        sep = "\t"
        )

print(reactions[["rxns", "rxnHMR2ID"]].head())
print("Dimensions:", reactions.shape)

# join both tables
medium_joined = medium_table.merge(
        reactions[["rxns", "rxnHMR2ID"]],
        "left",
        left_on = "Exchange reaction ID",
        right_on = "rxnHMR2ID"
        )
print(medium_joined.head(10))
print("Missing mappings:", medium_joined["rxns"].isna().sum())
print("length_rxns:", len(medium_joined))
print(medium_joined)

# mark nutrient types
import numpy as np

inorganic_components = ["Fe2+", "H2O", "O2", "Pi", "sulfate"]

medium_joined["nutrient_type"] = np.where(
        medium_joined["Component"].isin(inorganic_components),
        "inorganic",
        "organic"
        )

print(medium_joined.head(15))
print(medium_joined["nutrient_type"].value_counts())

medium_joined["uptake_bound"] = np.where(
        medium_joined["nutrient_type"] == "inorganic",
        1000,
        10
        )
print(medium_joined.head(10))

medium_dict = dict(
        zip(
            medium_joined["rxns"],
            medium_joined["uptake_bound"]
            )
        )

print("n medium components:", len (medium_dict))
print(list(medium_dict.items())[:10])

# is the human gem able to survive with the Ham's medium?

