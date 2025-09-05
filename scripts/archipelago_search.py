
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import json
import pyfaidx
from tqdm import tqdm

# --- Helper functions from create_fingerprint.py ---
# We include them here to make the script self-contained.

def shannon_entropy(sequence):
    """Calculates the Shannon entropy of a given sequence."""
    if not sequence:
        return 0.0
    counts = Counter(sequence)
    probabilities = [count / len(sequence) for count in counts.values()]
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def kmer_spectrum_vector(sequence, k_values=[3, 4, 5], all_possible_kmers=None):
    """
    Calculates the k-mer frequency spectrum and returns it as a fixed-length vector.
    """
    vector = []
    for k in k_values:
        # Get all possible k-mers for this k value
        possible_kmers = all_possible_kmers[k]
        
        # Calculate k-mer counts for the current sequence
        if len(sequence) < k:
            counts = {kmer: 0 for kmer in possible_kmers}
        else:
            kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
            counts = Counter(kmers)
        
        # Create a frequency vector in a fixed order
        total_kmers = sum(counts.values())
        if total_kmers == 0:
            freq_vector = [0.0] * len(possible_kmers)
        else:
            freq_vector = [counts.get(kmer, 0) / total_kmers for kmer in sorted(possible_kmers)]
        
        vector.extend(freq_vector)
    return np.array(vector)

# --- Main Search Functions ---

def generate_all_possible_kmers(k_values=[3, 4, 5]):
    """Generates all possible DNA k-mers for given k values."""
    bases = ['A', 'C', 'G', 'T']
    all_kmers = {}
    for k in k_values:
        from itertools import product
        all_kmers[k] = [''.join(p) for p in product(bases, repeat=k)]
    return all_kmers

def create_feature_vector(sequence, all_possible_kmers):
    """Creates a numerical feature vector from a sequence's fingerprint."""
    entropy = shannon_entropy(sequence)
    kmer_vec = kmer_spectrum_vector(sequence, all_possible_kmers=all_possible_kmers)
    
    # Combine features into a single vector
    feature_vector = np.concatenate(([entropy], kmer_vec))
    return feature_vector

def load_reference_fingerprint(fingerprint_file, all_possible_kmers):
    """Loads and vectorizes the reference fingerprint."""
    with open(fingerprint_file, 'r') as f:
        ref_fingerprint_data = json.load(f)

    # Recreate the reference sequence's feature vector
    # NOTE: This assumes the reference fingerprint was generated with the same k-mer values.
    # A more robust implementation would store the sequence itself. For now, we use a placeholder.
    # In a real pipeline, you'd load the original sequence used to create the fingerprint.
    placeholder_sequence = "CATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATG" \
                           "TGCATGTGCATGTGCATGTGCATGTGCATGTGCATGTGCATGTGCATG" \
                           "AGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCT" \
                           "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACA"

    ref_vector = create_feature_vector(placeholder_sequence, all_possible_kmers)
    return ref_vector.reshape(1, -1) # Reshape for cosine_similarity

def scan_genome(genome_file, ref_vector, all_possible_kmers, window_size=200, step_size=50, similarity_threshold=0.85):
    """
    Scans a genome for regions with high similarity to the reference fingerprint.
    """
    print(f"Loading genome from {genome_file}...")
    genome = pyfaidx.Fasta(genome_file)
    candidate_regions = []

    print("Scanning chromosomes...")
    # We scan only the main chromosomes to save time
    chromosomes_to_scan = [f'chr{i}' for i in range(1, 23)] + ['chrX', 'chrY']

    for chrom_name in chromosomes_to_scan:
        if chrom_name not in genome:
            continue
        
        chromosome = genome[chrom_name]
        chrom_len = len(chromosome)
        
        print(f"  - Scanning {chrom_name} (length: {chrom_len})...")
        
        # Using tqdm for a progress bar
        for i in tqdm(range(0, chrom_len - window_size, step_size), desc=f"  {chrom_name}", unit=" windows"):
            start = i
            end = i + window_size
            sequence = str(chromosome[start:end]).upper()

            # Skip windows with too many 'N's
            if sequence.count('N') / window_size > 0.1:
                continue

            # Create feature vector for the window
            window_vector = create_feature_vector(sequence, all_possible_kmers).reshape(1, -1)
            
            # Calculate cosine similarity
            sim = cosine_similarity(ref_vector, window_vector)[0][0]
            
            if sim >= similarity_threshold:
                candidate_regions.append({
                    'chromosome': chrom_name,
                    'start': start,
                    'end': end,
                    'similarity': sim
                })
                # Optional: Print found candidates in real-time
                # print(f"Found candidate on {chrom_name}:{start}-{end} with similarity {sim:.4f}")

    return candidate_regions

if __name__ == '__main__':
    # --- Configuration ---
    GENOME_FASTA_FILE = 'data/external/hg38.fa'  # Path to your genome file
    REFERENCE_FINGERPRINT_FILE = 'seed_fingerprint.json' # The fingerprint from the previous step
    OUTPUT_FILE = 'results/candidate_islands.bed'
    SIMILARITY_THRESHOLD = 0.85 # Tweak this based on results
    WINDOW_SIZE = 200 # Must match the size of the seed sequence
    STEP_SIZE = 50 # Smaller step = more thorough but slower scan
    
    # 1. Generate the universe of all possible k-mers
    print("Generating all possible k-mers...")
    all_kmers = generate_all_possible_kmers()

    # 2. Load the reference fingerprint and create its feature vector
    print(f"Loading reference fingerprint from {REFERENCE_FINGERPRINT_FILE}...")
    try:
        reference_vector = load_reference_fingerprint(REFERENCE_FINGERPRINT_FILE, all_kmers)
    except FileNotFoundError:
        print(f"Error: Reference fingerprint file '{REFERENCE_FINGERPRINT_FILE}' not found.")
        print("Please run 'create_fingerprint.py' first to generate it.")
        exit()

    # 3. Scan the entire genome
    try:
        candidate_islands = scan_genome(
            genome_file=GENOME_FASTA_FILE,
            ref_vector=reference_vector,
            all_possible_kmers=all_kmers,
            window_size=WINDOW_SIZE,
            step_size=STEP_SIZE,
            similarity_threshold=SIMILARITY_THRESHOLD
        )
    except pyfaidx.FastaIndexingError:
        print(f"Error: Genome file '{GENOME_FASTA_FILE}' not found or not properly indexed.")
        print("Please ensure the .fa and .fai files exist at the specified path.")
        exit()

    # 4. Save results to a BED file
    print(f"\nScan complete. Found {len(candidate_islands)} candidate regions.")
    
    # Sort candidates by similarity score in descending order
    sorted_candidates = sorted(candidate_islands, key=lambda x: x['similarity'], reverse=True)
    
    with open(OUTPUT_FILE, 'w') as f:
        f.write("#chrom\tstart\tend\tname\tscore\tstrand\n")
        for i, region in enumerate(sorted_candidates):
            name = f"island_{i+1:04d}"
            score = f"{region['similarity']:.4f}"
            f.write(f"{region['chromosome']}\t{region['start']}\t{region['end']}\t{name}\t{score}\t.\n")
            
    print(f"Results saved to {OUTPUT_FILE}")
```
