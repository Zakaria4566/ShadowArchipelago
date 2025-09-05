
# Wet-Lab Protocol: Functional Validation of Shadow Archipelago Islands using CRISPRi
**Version 1.0**
**Date: 2025-09-04**

## 1. Objective
To functionally validate the regulatory potential of the top 8 candidate "Shadow Archipelago" islands by assessing the impact of their transcriptional repression (CRISPRi) on the expression of their nearest neighboring genes in a human neuronal cell model.

## 2. Materials & Reagents

### 2.1. Cell Lines
- **Primary Model:** iPSC-derived human excitatory neurons (e.g., from a healthy donor line).
- **Alternative/Backup Model:** SH-SY5Y neuroblastoma cell line (ATCC® CRL-2266™).
- **Lentivirus Production:** HEK2S93T cells (ATCC® CRL-3216™).

### 2.2. Plasmids & Vectors
- **CRISPRi Effector:** lenti-dCas9-KRAB-Blast (Addgene #89567 or similar).
- **gRNA Expression Vector:** lentiGuide-Puro (Addgene #52963 or similar).
- **Lentiviral Packaging:** psPAX2 (Addgene #12260), pMD2.G (Addgene #12259).

### 2.3. Key Reagents
- **Cell Culture:** DMEM/F12 + N2/B27 supplements, Neurobasal Plus, GlutaMAX, Pen-Strep.
- **Transfection (HEK293T):** Lipofectamine 3000 (Thermo Fisher, L3000015).
- **Lentivirus Transduction:** Polybrene (Sigma, TR-1003-G).
- **Selection:** Blasticidin (Thermo Fisher, R21001), Puromycin (Thermo Fisher, A1113803).
- **RNA Extraction:** RNeasy Mini Kit (QIAGEN, 74104).
- **cDNA Synthesis:** iScript™ cDNA Synthesis Kit (Bio-Rad, 1708891).
- **qPCR:** SsoAdvanced™ Universal SYBR® Green Supermix (Bio-Rad, 1725271).

### 2.4. Oligos & Primers
- **gRNA Oligos:** See `Oligo_Order_Sheet.xlsx` for all 32 experimental gRNAs + controls. Order as desalted oligo pairs.
- **qPCR Primers:** See Appendix A for validated primer sequences for target genes (`SHANK3`, `RBFOX1`, etc.) and housekeeping genes (`ACTB`, `GAPDH`).

---

## 3. Experimental Workflow (Timeline: ~3-4 Weeks)

### Week 1: Plasmid Preparation & Lentivirus Production
1.  **gRNA Cloning (Day 1-3):** Anneal and ligate gRNA oligo pairs into BsmBI-digested `lentiGuide-Puro`. Verify by Sanger sequencing.
2.  **Lentivirus Production (Day 4-7):** Co-transfect HEK293T cells with packaging plasmids and gRNA/dCas9 plasmids. Collect and concentrate virus.

### Week 2: Generation of Stable dCas9-KRAB Cell Line
1.  **Transduction (Day 8):** Transduce target neurons with lenti-dCas9-KRAB-Blast virus.
2.  **Selection (Day 10-14):** Apply Blasticidin selection to generate a stable cell population.

### Week 3-4: Functional Assay
1.  **gRNA Transduction (Day 15):** Seed dCas9-KRAB neurons and transduce with individual gRNA lentiviruses.
2.  **Selection (Day 17):** Apply Puromycin selection.
3.  **Sample Collection (Day 19-20):** Harvest cells for RNA extraction.
4.  **Gene Expression Analysis (Day 21-22):** Perform RNA extraction, cDNA synthesis, and qPCR.

---

## 4. Data Analysis & Success Criteria
1.  **qPCR Analysis:** Calculate fold change using the ΔΔCt method relative to Non-Targeting Control (NTC) samples.
2.  **Statistical Analysis:** Compare results to NTC using a two-tailed Student's t-test (p < 0.05).
3.  **Success Criteria:** A candidate is validated if at least **2 out of 4 gRNAs** cause a **statistically significant downregulation of ≥20%** in the target gene's expression.

---

## Appendix A: Validated qPCR Primers
| Target Gene | Forward Primer (5'-3')      | Reverse Primer (5'-3')       |
|-------------|-----------------------------|------------------------------|
| SHANK3      | AGATGATGGGAACGAGAGGTC       | TCCTCGGTCAGGCTTGTAGT         |
| RBFOX1      | TGGCTTTCAACGGCAAGTTT        | CTTCCATGCCACACTTGACA         |
| GAPDH       | GAAGGTGAAGGTCGGAGTCA        | GAAGATGGTGATGGGATTTC         |
| ACTB        | CACCATTGGCAATGAGCGGTTC      | AGGTCTTTGCGGATGTCCACGT       |
```
