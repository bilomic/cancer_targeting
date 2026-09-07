

# Medium definition

Human-GEM is a generic human metabolic model and requires defined
media constraints for meaningful gene-deletion simulations.

The Human-GEM developers previously used Ham's medium as a relatively
minimal mammalian-cell medium for gene-deletion analyses.

TODO:
Identify the exact Ham's medium composition and corresponding
Human-GEM exchange reactions.

## Reproducibility limitation

Lee et al. specify uptake bounds of 10 mmol/gDCW/h for "main carbon
sources" and ±1000 mmol/gDCW/h for inorganic nutrients, but neither
the manuscript nor Supplementary Table 3 explicitly identifies which
Ham's medium components belong to these categories.

Therefore, the exact published medium constraints cannot be
reconstructed unambiguously from the available supplementary material.

## Medium sensitivity

Predicted biomass was sensitive to the maximum organic nutrient uptake
constraint. Increasing the bound from 5 to 1000 increased predicted biomass
from approximately 10.18 to 65.41.

Therefore, an organic uptake bound of 10 mmol/gDCW/h is used as the baseline
condition, following the general modeling convention described by Lee et al.
However, this value is treated as a modeling assumption rather than a
physiological uptake rate, and the exact nutrient classification used in the
original study could not be reconstructed unambiguously.

Sensitivity analyses across alternative uptake bounds will be used to assess
the robustness of downstream gene-essentiality predictions.
