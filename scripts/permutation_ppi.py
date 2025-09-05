
import pandas as pd
import networkx as nx
import numpy as np
import random
from tqdm import tqdm
import json
import os

def load_ppi_network(ppi_file, confidence_threshold=700):
    """
    Loads the STRING PPI network from a file into a NetworkX graph.
    Filters interactions based on a confidence score.
    """
    print(f"Loading PPI network from {ppi_file}...")
    try:
        # Assuming the file is a tab-separated file from STRING
        df = pd.read_csv(ppi_file, sep=' ', comment='#')
        df.columns = ['protein1', 'protein2', 'combined_score']
    except FileNotFoundError:
        print(f"Error: PPI file not found at '{ppi_file}'.")
        print("Please download the STRING PPI data for your organism and place it in 'data/external/'.")
        return None
        
    # Filter by confidence score
    df_filtered = df[df['combined_score'] >= confidence_threshold]
    
    # Create graph
    G = nx.from_pandas_edgelist(df_filtered, 'protein1', 'protein2', ['combined_score'])
    print(f"PPI network loaded with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    return G

def load_candidate_genes(gene_file):
    """Loads the list of candidate genes from a text file."""
    print(f"Loading candidate genes from {gene_file}...")
    try:
        with open(gene_file, 'r') as f:
            # Assumes one gene symbol per line
            genes = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Candidate gene file not found at '{gene_file}'.")
        print("This file should be generated after running the genome scan and mapping islands to genes.")
        return None
        
    print(f"Loaded {len(genes)} candidate genes.")
    return genes

def run_permutation_test(G, candidate_genes, num_permutations=10000):
    """
    Performs a permutation test to check if the candidate gene set
    is more interconnected than random sets of genes.
    """
    if not G or not candidate_genes:
        print("Cannot run test due to missing graph or gene list.")
        return None

    # Filter candidate genes that are actually present in the PPI network
    candidate_nodes_in_graph = [gene for gene in candidate_genes if gene in G]
    print(f"{len(candidate_nodes_in_graph)} of {len(candidate_genes)} candidate genes are in the PPI network.")
    
    if len(candidate_nodes_in_graph) < 2:
        print("Too few candidate genes in the network to perform a meaningful test.")
        return None
        
    # --- Calculate Observed Interactions ---
    subgraph_observed = G.subgraph(candidate_nodes_in_graph)
    observed_interactions = subgraph_observed.number_of_edges()
    print(f"\nObserved interactions within the candidate set: {observed_interactions}")

    # --- Run Permutations ---
    print(f"Running {num_permutations} permutations...")
    all_nodes_in_graph = list(G.nodes())
    random_interaction_counts = []

    for _ in tqdm(range(num_permutations), desc="Permutations"):
        # Select a random set of genes of the same size as the candidate set
        random_nodes = random.sample(all_nodes_in_graph, len(candidate_nodes_in_graph))
        
        # Create subgraph and count interactions
        subgraph_random = G.subgraph(random_nodes)
        random_interactions = subgraph_random.number_of_edges()
        random_interaction_counts.append(random_interactions)
        
    # --- Calculate Statistics ---
    random_interaction_counts = np.array(random_interaction_counts)
    mean_random_interactions = np.mean(random_interaction_counts)
    std_random_interactions = np.std(random_interaction_counts)

    # Calculate p-value: the proportion of random sets with at least as many interactions as the observed set
    count_more_extreme = np.sum(random_interaction_counts >= observed_interactions)
    p_value = (count_more_extreme + 1) / (num_permutations + 1) # Add 1 to avoid p=0

    results = {
        "num_candidate_genes": len(candidate_genes),
        "num_candidate_genes_in_network": len(candidate_nodes_in_graph),
        "observed_interactions": int(observed_interactions),
        "num_permutations": num_permutations,
        "mean_random_interactions": float(mean_random_interactions),
        "std_dev_random_interactions": float(std_random_interactions),
        "p_value": float(p_value),
        "random_interaction_distribution": random_interaction_counts.tolist()
    }
    
    return results

if __name__ == '__main__':
    # --- Configuration ---
    # NOTE: You must download the protein links file (e.g., 9606.protein.links.v11.5.txt.gz) from the STRING database
    # for your organism (9606 is Homo sapiens) and place it in the specified path.
    PPI_NETWORK_FILE = 'data/external/9606.protein.links.v11.5.txt'
    CANDIDATE_GENE_FILE = 'data/processed/candidate_genes.txt' # This file needs to be created
    OUTPUT_RESULTS_FILE = 'results/network_analysis/permutation_results.json'
    NUM_PERMUTATIONS = 10000

    # 1. Load PPI Network
    ppi_graph = load_ppi_network(PPI_NETWORK_FILE, confidence_threshold=700)
    
    # 2. Load Candidate Genes
    genes_of_interest = load_candidate_genes(CANDIDATE_GENE_FILE)
    
    # 3. Run the Test
    test_results = run_permutation_test(ppi_graph, genes_of_interest, NUM_PERMUTATIONS)

    # 4. Save and Print Results
    if test_results:
        print("\n--- Permutation Test Results ---")
        print(f"Observed Interactions: {test_results['observed_interactions']}")
        print(f"Mean Random Interactions: {test_results['mean_random_interactions']:.2f}")
        print(f"P-value: {test_results['p_value']:.6f}")
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(OUTPUT_RESULTS_FILE), exist_ok=True)
        
        with open(OUTPUT_RESULTS_FILE, 'w') as f:
            json.dump(test_results, f, indent=4)
            
        print(f"\nFull results saved to {OUTPUT_RESULTS_FILE}")

