# Colorectal Cancer Metabolic Vulnerabilities

## Research Questions

1. **Model validity**

Can a transcriptomics and/or proteomics integrated model reproduce relevant metabolic features of colorectal cancer?
The model will be evaluated by comparing predicted metabolite uptake and secretion with public metabolomics data.
Single-gene knockouts will be used to identify dependencies that affect colorectal cancer more than normal colon cells.

2. **Nutrient-environment dependence**

How are different Nutrient-environments affecting the effects of Single-gene deletions?
The KO's will be simulated under baseline, low-glucose, lipid-rich, and combined conditions to distinguish robust from environment-specific vulnerabilities.

3. **Microbiome effects**

How do gut microbiome-derived metabolites and microbial cross-feeding affect colorectal cancer metabolism and gene dependencies?
The microbiome will be developed as a separate modeling layer and added only after the cancer model and nutrient-environment analyses are established.

## Project status

**Work ind progress**
The current work focuses on Human-GEM, medium definition, baseline simulations, and sensitivity analysis. The next step is the reconstruction of transcriptomics-informed colorectal cancer and normal colon models.

## Project Overview

```text
        Human-GEM
            ↓
transcriptomic integration
    ↙                    ↘
CRC transcriptomics    normal colon transcriptomics
    ↓                    ↓
CRC-specific GEM       normal-colon GEM
    ↓                    ↓
    Level 1: baseline model
            ↓
metabolite validation and single-gene knockouts
            ↓
Level 2: nutrient environments
baseline / low glucose / lipid-rich / combined
            ↓
    same knockouts across media
            ↓
Level 3: microbiome metabolites
diet → microbial community → cross-feeding → metabolite exchanges
            ↓
comparative growth and flux analysis
            ↓
tumor-selective vulnerabilities
```

## Primary Outcome

relative_growth_CRC(g) =
growth_CRC_KO / growth_CRC_WT

relative_growth_normal(g) =
growth_normal_KO / growth_normal_WT

A preliminary tumor-selective candidate is defined as:
CRC:    relative growth < 0.2
normal: relative growth > 0.8
