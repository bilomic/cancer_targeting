# PDAC Metabolic Vulnerabilities

## Research Question

Which metabolic gene deletions selectively impair predicted growth of pancreatic ductal adenocarcinoma (PDAC) cells while having substantially smaller effects on normal pancreatic cells, and how robust are these vulnerabilities across different nutrient environments?

## Project Status

**Work in progress.**

The current stage focuses on model setup, medium definition, baseline simulations, and sensitivity analysis before generating tumor- and normal-specific metabolic models.

## Project Overview

```text
                    Human-GEM
                        ↓
          transcriptomic integration
             ↙                  ↘
     PDAC transcriptomics   normal pancreatic
                            transcriptomics
             ↓                  ↓
      PDAC-specific GEM    normal-specific GEM
             ↘                  ↙
              nutrient environments
        ┌──────────┬───────────┬──────────────┐
        ↓          ↓           ↓              ↓
     baseline   low glucose   lipid-rich   combined stress
        └──────────┴───────────┴──────────────┘
                       ↓
             flux and growth analysis
                       ↓
             single-gene deletions
                       ↓
                growth comparison
                       ↓
          tumor-selective vulnerabilities
                       ↓
          environmental robustness analysis
                       ↓
               DepMap validation
```

The aim is to identify metabolic gene dependencies that strongly impair predicted tumor growth while preserving metabolic functionality in the corresponding normal-cell model.

An additional objective is to determine whether these predicted vulnerabilities remain stable across biologically plausible nutrient environments. This allows identification of metabolic dependencies that are either robust across conditions or specifically induced by nutrient limitation.

## Nutrient Environment Analysis

Different extracellular nutrient conditions will be simulated by modifying selected exchange-reaction constraints.

Initial scenarios may include:

```text
baseline
low glucose
lipid-rich
low glucose + lipid-rich
```

These conditions are intended to represent simplified extracellular nutrient environments rather than complete dietary states.

For each condition, flux distributions and predicted growth rates will be compared between PDAC-specific and normal pancreatic models before gene-deletion analysis.

## Primary Outcome

For each gene \(g\), relative growth after single-gene deletion is calculated as:

```text
relative_growth_tumor(g)  = growth_tumor_KO / growth_tumor_WT
relative_growth_normal(g) = growth_normal_KO / growth_normal_WT
```

A preliminary tumor-selective candidate is defined as:

```text
tumor:  relative growth < 0.2
normal: relative growth > 0.8
```

These thresholds are used as initial prioritization criteria and will be evaluated through sensitivity analyses.

For each candidate gene, selectivity will additionally be assessed across nutrient environments to distinguish:

```text
robust vulnerabilities
environment-specific vulnerabilities
non-robust predictions
```

## Planned Validation

Prioritized metabolic vulnerabilities will be compared with independent cancer dependency data, including DepMap gene-essentiality datasets.

Predictions that are both experimentally supported and robust across multiple nutrient environments will receive higher priority.
