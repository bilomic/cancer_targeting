
# import packages
import cobra
import pandas as pd
import numpy as np

from config import (
    HUMANGEM_PATH,
    MEDIUM_PATH,
    REACTIONS_PATH,
    ORGANIC_UPTAKE,
    INORGANIC_UPTAKE,
)

# load Human-GEM
def load_human_gem():
    model = cobra.io.read_sbml_model(HUMANGEM_PATH)
    return model

# medium

def build_hams_medium(
    organic_uptake=ORGANIC_UPTAKE,
    inorganic_uptake=INORGANIC_UPTAKE
):

    medium_table = pd.read_excel(
        MEDIUM_PATH,
        sheet_name="Supplementary Table 3",
        header=2
    )

    reactions = pd.read_csv(
        REACTIONS_PATH,
        sep="\t"
    )

    medium_mapped = medium_table.merge(
        reactions[["rxns", "rxnHMR2ID"]],
        how="left",
        left_on="Exchange reaction ID",
        right_on="rxnHMR2ID"
    )

    inorganic_components = ["Fe2+", "H2O", "O2", "Pi", "sulfate"]

    medium_mapped["nutrient_type"] = np.where(
        medium_mapped["Component"].isin(inorganic_components),
        "inorganic",
        "organic"
    )

    medium_mapped["uptake_bound"] = np.where(
        medium_mapped["nutrient_type"] == "inorganic",
        inorganic_uptake,
        organic_uptake
    )

    medium_dict = dict(
        zip(
            medium_mapped["rxns"],
            medium_mapped["uptake_bound"]
        )
    )

    return medium_dict
