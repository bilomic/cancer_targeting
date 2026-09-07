# PDAC Metabolic Vulnerabilities

## Research Question

Which metabolic gene deletions selectively impair predicted growth of pancreatic ductal adenocarcinoma (PDAC) cells while having substantially smaller effects on normal pancreatic cells?

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
             single-gene deletions
                       ↓
                growth comparison
                       ↓
          tumor-selective vulnerabilities
                       ↓
               DepMap validation
```

The aim is to identify metabolic gene dependencies that strongly impair predicted tumor growth while preserving metabolic functionality in the corresponding normal-cell model.

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

## Planned Validation

Prioritized metabolic vulnerabilities will be compared with independent cancer dependency data, including DepMap gene-essentiality datasets.




