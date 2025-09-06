Wet-Lab Protocol
Functional Validation of Shadow Archipelago Islands using CRISPRi
Version: 1.1
Date: 2025-09-06

1. Objective

To functionally validate the top 8 candidate "Shadow Archipelago" islands by assessing the effect of their transcriptional repression (CRISPRi) on the expression of their nearest neighboring genes in human neuronal models.

2. Materials & Reagents
2.1 Cell Lines

Primary Model: iPSC-derived human excitatory neurons (healthy donor).

Alternative Model: SH-SY5Y neuroblastoma (ATCC® CRL-2266™).

Lentivirus Production: HEK293T cells (ATCC® CRL-3216™).

2.2 Plasmids & Vectors

CRISPRi Effector: lenti-dCas9-KRAB-Blast (Addgene #89567).

gRNA Expression Vector: lentiGuide-Puro (Addgene #52963).

Lentiviral Packaging: psPAX2 (#12260), pMD2.G (#12259).

2.3 Key Reagents

Cell Culture: DMEM/F12 + N2/B27, Neurobasal Plus, GlutaMAX, Pen/Strep.

Transfection: Lipofectamine 3000 (Thermo Fisher L3000015).

Transduction Enhancer: Polybrene (Sigma TR-1003-G).

Selection: Blasticidin (Thermo Fisher R21001), Puromycin (Thermo Fisher A1113803).

RNA Extraction: RNeasy Mini Kit (QIAGEN 74104).

cDNA Synthesis: iScript™ cDNA Synthesis Kit (Bio-Rad 1708891).

qPCR: SsoAdvanced™ Universal SYBR® Green Supermix (Bio-Rad 1725271).

2.4 Oligos & Primers

gRNA Oligos: See Oligo_Order_Sheet.xlsx (32 experimental + controls).

qPCR Primers: See Appendix A for validated primers for SHANK3, RBFOX1, CSMD1, CTNNA2, and housekeeping genes (ACTB, GAPDH).

3. Experimental Workflow (Timeline: ~3-4 Weeks)
Week 1: Plasmid Preparation & Lentivirus Production

gRNA Cloning (Day 1–3):

Anneal and ligate gRNA oligos into BsmBI-digested lentiGuide-Puro.

Verify insert by Sanger sequencing.

Lentivirus Production (Day 4–7):

Co-transfect HEK293T cells with packaging plasmids + gRNA/dCas9 plasmids.

Collect viral supernatant and concentrate.

Week 2: Generation of Stable dCas9-KRAB Cell Line

Transduction (Day 8): Transduce neurons with lenti-dCas9-KRAB-Blast virus.

Selection (Day 10–14): Apply Blasticidin to generate stable dCas9-KRAB-expressing cells.

Week 3–4: Functional Assay

gRNA Transduction (Day 15): Seed dCas9-KRAB neurons and transduce with individual gRNA lentiviruses.

Selection (Day 17): Apply Puromycin to select successfully transduced cells.

Sample Collection (Day 19–20): Harvest cells for RNA extraction.

Gene Expression Analysis (Day 21–22):

RNA extraction → cDNA synthesis → qPCR.

Include 4 biological replicates per gRNA.

Include non-targeting control (NTC) gRNAs in parallel.

4. Data Analysis & Success Criteria

qPCR Analysis:

Use ΔΔCt method, normalize to housekeeping genes (ACTB, GAPDH).

Express fold change relative to NTC.

Statistical Analysis:

Two-tailed Student’s t-test (p < 0.05) for significance.

Optionally, apply FDR correction for multiple comparisons.

Success Criteria:

Candidate is validated if ≥2 out of 4 gRNAs reduce target gene expression by ≥20% with statistical significance.

5. Notes & Recommendations

Maintain low passage numbers for iPSC-derived neurons to reduce variability.

Use parallel negative controls for both dCas9-KRAB only and NTC gRNAs.

Consider additional validation by ATAC-seq or RNA-seq for top hits to assess broader network effects.

Document MOI, cell density, and viability at each step.

Appendix A: Validated qPCR Primers
Target Gene	Forward Primer (5'-3')	Reverse Primer (5'-3')
SHANK3	AGATGATGGGAACGAGAGGTC	TCCTCGGTCAGGCTTGTAGT
RBFOX1	TGGCTTTCAACGGCAAGTTT	CTTCCATGCCACACTTGACA
GAPDH	GAAGGTGAAGGTCGGAGTCA	GAAGATGGTGATGGGATTTC
ACTB	CACCATTGGCAATGAGCGGTTC	AGGTCTTTGCGGATGTCCACGT
