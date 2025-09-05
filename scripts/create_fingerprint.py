
import numpy as np
import zlib
from collections import Counter
import json

def shannon_entropy(sequence):
    """Calculates the Shannon entropy of a given sequence."""
    if not sequence:
        return 0.0
    counts = Counter(sequence)
    probabilities = [count / len(sequence) for count in counts.values()]
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def compressibility(sequence):
    """Calculates the compressibility of a sequence using zlib."""
    if not sequence:
        return 0.0
    compressed_sequence = zlib.compress(sequence.encode('utf-8'))
    return len(compressed_sequence) / len(sequence)

def kmer_spectrum(sequence, k_values=[3, 4, 5]):
    """Calculates the k-mer frequency spectrum for a list of k values."""
    spectrum = {}
    for k in k_values:
        if len(sequence) < k:
            spectrum[f'k{k}'] = {}
            continue
        
        kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
        kmer_counts = Counter(kmers)
        total_kmers = len(kmers)
        
        # Normalize to frequencies
        kmer_freq = {kmer: count / total_kmers for kmer, count in kmer_counts.items()}
        spectrum[f'k{k}'] = kmer_freq
    return spectrum

def create_fingerprint(sequence):
    """
    Generates a comprehensive informational fingerprint for a DNA sequence.
    """
    fingerprint = {
        'sequence_length': len(sequence),
        'shannon_entropy': shannon_entropy(sequence),
        'compressibility': compressibility(sequence),
        'kmer_spectrum': kmer_spectrum(sequence)
    }
    return fingerprint

if __name__ == "__main__":
    # This is a placeholder for the seed regulatory sequence (e.g., from SHANK3).
    # In a real run, this would be read from a file or database.
    seed_sequence = "CATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATG" \
                    "TGCATGTGCATGTGCATGTGCATGTGCATGTGCATGTGCATGTGCATG" \
                    "AGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCT" \
                    "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACA"

    print("Generating fingerprint for the seed sequence...")
    
    # Create the fingerprint
    informational_fingerprint = create_fingerprint(seed_sequence)
    
    # Print the fingerprint as a clean JSON string
    print(json.dumps(informational_fingerprint, indent=4))
    
    # Save the fingerprint to a file for later use in the pipeline
    with open('seed_fingerprint.json', 'w') as f:
        json.dump(informational_fingerprint, f, indent=4)
        
    print("\nFingerprint saved to seed_fingerprint.json")
```
