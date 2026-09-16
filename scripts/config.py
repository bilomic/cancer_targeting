

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

HUMANGEM_PATH = PROJECT_ROOT / "raw_data" / "Human-GEM.xml"
MEDIUM_PATH = PROJECT_ROOT / "raw_data" / "mmc3_references.xlsx"
REACTIONS_PATH = PROJECT_ROOT / "raw_data" / "reactions.tsv"

ORGANIC_UPTAKE = 10.0
INORGANIC_UPTAKE = 1000.0

TRANSCRIPTOMICS_DATASET = "GSE142279"
TRANSCRIPTOMICS_GENE_ID_TYPE = "ensembl"

TRANSCRIPTOMICS_RAW_DIR = PROJECT_ROOT / "raw_data" / "transcriptomics"
TRANSCRIPTOMICS_RESULTS_DIR = PROJECT_ROOT / "results" / "transcriptomics"

EXPRESSION_MATRIX_PATH = (
    TRANSCRIPTOMICS_RESULTS_DIR / "expression_tpm.tsv"
)

SAMPLE_METADATA_PATH = (
    TRANSCRIPTOMICS_RAW_DIR / "sample_metadata.tsv"
)

FPKM_PATH = (
    TRANSCRIPTOMICS_RAW_DIR / "GSE142279_FPKM.xls.gz"
)

CRC_TPM_PATH = (
    TRANSCRIPTOMICS_RESULTS_DIR / "crc_expression_tpm.tsv"
)

NORMAL_COLON_TPM_PATH = (
    TRANSCRIPTOMICS_RESULTS_DIR / "normal_colon_expression_tpm.tsv"
    )
