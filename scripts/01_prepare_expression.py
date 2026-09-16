from numpy import exp
import pandas as pd
import cobra

from config import (
    FPKM_PATH,
    HUMANGEM_PATH,
    EXPRESSION_MATRIX_PATH,
    CRC_TPM_PATH,
    NORMAL_COLON_TPM_PATH,
    TRANSCRIPTOMICS_RESULTS_DIR,
)

# load the fpkm data
def load_fpkm_data() -> pd.DataFrame:
    expression = pd.read_csv(
        FPKM_PATH,
        sep = "\t",
        compression = "gzip",
    )

    if "ID" not in expression.columns:
        raise ValueError("The expected column 'ID' was not found.")

    expression = expression.set_index("ID")

    # Eventuelle Versionssuffixe entfernen, z. B. ENSG00000123456.7
    expression.index = (
        expression.index.astype(str)
        .str.replace(r"\.\d+$", "", regex=True)
    )

    if expression.index.duplicated().any():
        duplicated = expression.index[
            expression.index.duplicated()
        ].unique().tolist()
        raise ValueError(
            f"Duplicated Gene-IDs after filtering: {duplicated[:10]}"
        )

    expression = expression.apply(pd.to_numeric, errors="raise")

    if expression.isna().any().any():
        raise ValueError("Expression matrix contains missing values.")

    if (expression < 0).any().any():
        raise ValueError("Expression matrix contains negative values.")

    return expression

# fpkm to tpm
def fpkm_to_tpm(fpkm: pd.DataFrame) -> pd.DataFrame:
    sample_sums = fpkm.sum(axis=0)

    if (sample_sums == 0).any():
        raise ValueError("at least one samples has a total sum of 0.")

    return fpkm.div(sample_sums, axis= "columns") * 1_000_000


def main() -> None:
    TRANSCRIPTOMICS_RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    fpkm = load_fpkm_data()
    tpm = fpkm_to_tpm(fpkm)

    normal_samples = []
    for column in tpm.columns:
        if column.endswith("_N"):
            normal_samples.append(column)

    crc_samples = []
    for column in tpm.columns:
        if column.endswith("_T"):
            crc_samples.append(column)

    if not normal_samples or not crc_samples:
        raise ValueError(
            "No fit for normal or tumor samples found."
        )

    normal_ids = {
        column.removesuffix("_N")
        for column in normal_samples
    }

    crc_ids = {
        column.removesuffix("_T")
        for column in crc_samples
    }

    if normal_ids != crc_ids:
        raise ValueError(
            "normal and tumor samples are not matched."
        )

    model = cobra.io.read_sbml_model(str(HUMANGEM_PATH))

    model_gene_ids = {
        gene.id.split(".")[0]
        for gene in model.genes
    }

    expression_gene_ids = set(tpm.index)
    overlapping_gene_ids = sorted(
        expression_gene_ids.intersection(model_gene_ids)
    )

    if not overlapping_gene_ids:
        raise ValueError(
            "No overlapping gene ids were found between expression data and human-GEM."
        )

    model_tpm = tpm.loc[overlapping_gene_ids]

    crc_expression = model_tpm[crc_samples].median(axis=1)
    normal_expression = model_tpm[normal_samples].median(axis=1)

    crc_expression.name = "CRC"
    normal_expression.name = "NORMAL_COLON"

    tpm.to_csv(
        EXPRESSION_MATRIX_PATH,
        sep="\t",
    )

    crc_expression.to_frame().to_csv(
        CRC_TPM_PATH,
        sep="\t",
    )

    normal_expression.to_frame().to_csv(
        NORMAL_COLON_TPM_PATH,
        sep="\t",
    )

    overlap_report = pd.DataFrame(
        {
            "expression_genes": [len(expression_gene_ids)],
            "model_genes": [len(model_gene_ids)],
            "overlapping_genes": [len(overlapping_gene_ids)],
            "model_coverage": [
                len(overlapping_gene_ids) / len(model_gene_ids)
            ],
            "normal_samples": [len(normal_samples)],
            "crc_samples": [len(crc_samples)],
        }
    )

    overlap_report.to_csv(
        TRANSCRIPTOMICS_RESULTS_DIR / "overlap_report.tsv",
        sep="\t",
        index=False,
    )

    print(f"FPKM-Gene: {len(fpkm)}")
    print(f"TPM-Gene: {len(tpm)}")
    print(f"Human-GEM-Gene: {len(model_gene_ids)}")
    print(f"Überlappende Gene: {len(overlapping_gene_ids)}")
    print(f"Normalproben: {len(normal_samples)}")
    print(f"CRC-Proben: {len(crc_samples)}")
    print("Expressiondaten erfolgreich vorbereitet.")


if __name__ == "__main__":
    main()
