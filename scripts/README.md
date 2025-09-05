Scripts

This directory contains all the Python scripts for the Shadow Archipelago discovery pipeline.

The scripts are designed to be run in the following order:

1.  `create_fingerprint.py`: Generates the initial informational fingerprint from a seed sequence.
2.  `archipelago_search.py`: Scans the genome to find other regions with a similar fingerprint.
3.  `permutation_ppi.py`: Performs the statistical permutation test to validate the significance of the resulting gene network.
