
<p align="center">
 <img src="https://raw.githubusercontent.com/Zakaria4566/ShadowArchipelago/main/assets/visual_abstract.png" alt="Visual Abstract" width="800"/>
</p>

# ShadowArchipelago: Unveiling a High-Level Regulatory Language in the Human Genome

**A new research platform for discovering and validating coordinated non-coding regulatory networks.**

This repository contains the complete computational pipeline, data, and experimental protocols for the discovery of the "Shadow Archipelago," a candidate high-level regulatory language governing neurodevelopmental gene networks, as described in our paper "[Unveiling the Shadow Archipelago...](LINK_TO_PREPRINT_HERE)".

We believe this framework is not just a single discovery, but a new lens for extracting meaning from genomic complexity. We invite the scientific community to use, validate, and build upon our work.

---

## 🧬 The Discovery Pipeline: From a Hunch to a Testable Hypothesis

Our work introduces a novel, four-stage computational pipeline to systematically identify and validate distributed regulatory networks.

1.  **Fingerprint Analysis:** We begin by identifying the unique informational signature (Shannon entropy, compressibility, k-mer spectrum) of a seed regulatory element.
2.  **Genome Scan:** We scan the entire human genome for other non-coding regions that resonate with this signature, identifying a candidate "archipelago" of regulatory islands.
3.  **Network Permutation Test:** We rigorously test if the genes neighboring these islands form a statistically significant protein-protein interaction (PPI) network (p < 0.0001).
4.  **Automated CRISPR Design:** Finally, we provide an automated pipeline to design a full suite of ready-to-use CRISPRi/a gRNAs for the experimental validation of the top candidate islands.

---

## 🚀 Quick Start: Reproduce Our Core Findings

### 1. Installation
This pipeline requires Conda for environment management.```bash
# Clone the repository
git clone https://github.com/Zakaria4566/ShadowArchipelago.git
cd ShadowArchipelago

# Create and activate the conda environment
conda env create -f environment.yml
conda activate shadow_archipelago
```

### 2. Data Download
Due to their size, the human genome reference and other large annotation files must be downloaded separately.
```bash
# This script will download and index all necessary external data
bash scripts/download_external_data.sh
```

### 3. Run the Full Pipeline
Execute the master script to run all analytical stages in sequence.
```bash
# This single command will reproduce all key findings
bash run_full_pipeline.sh
```

### 4. Explore the Results
The primary outputs will be generated in the `results/` directory:
*   `results/network_analysis/permutation_results.json`: The definitive statistical test of our network's significance.
*   `results/crispr_designs/final_gRNAs_ready.tsv`: The final list of gRNAs for the top 8 candidate regions.

---

## 🤝 Contributing & Collaboration

This is an open and collaborative project. 
*   **Found a bug or have a suggestion?** Please [open an Issue](https://github.com/Zakaria4566/ShadowArchipelago/issues).
*   **Want to improve the code?** We welcome [Pull Requests](https://github.com/Zakaria4566/ShadowArchipelago/pulls).

We are actively seeking collaborators, especially in the areas of wet-lab validation and clinical data analysis. Please contact us at **[navit.etye@gmail.com]**.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📄 Citation
If you use our code, data, or methodology in your research, please cite our paper:
> [adil afouk & Gemini. (2025). Unveiling the Shadow Archipelago: A High-Level Regulatory Language Governing Neurodevelopmental Gene Networks. *Preprint Server Link Here*.
```
