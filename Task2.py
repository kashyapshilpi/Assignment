from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from random import choice

# Function to reverse complement a sequence
def reverse_complement(sequence):
    return str(Seq(sequence).reverse_complement())

# Function to introduce a random 1 nucleotide change
def introduce_random_change(sequence):
    if len(sequence) > 0:
        position = choice(range(len(sequence)))
        new_base = choice('ACTG'.replace(sequence[position], ''))
        mutated_sequence = sequence[:position] + new_base + sequence[position + 1:]
        return mutated_sequence
    else:
        return sequence

# Your influenza genome file
genome_filename = "influenza.fna"

# Read the primary multi-fasta file using SeqIO.parse
genome_records = SeqIO.parse(genome_filename, "fasta")

# Create a BED file with coordinates for at least 3 locations
bed_content = """\
Scaffold1\t100\t200
Scaffold2\t300\t400
Scaffold3\t500\t600
"""

# Save the BED content to a file
bed_filename = "influenza.bed"
with open(bed_filename, "w") as bed_file:
    bed_file.write(bed_content)

# Read the BED file and process/insert sequences into the primary sequence
for record in genome_records:
    for line in bed_content.strip().split("\n"):
        scaffold, start, end = line.split("\t")
        start, end = int(start), int(end)

        subsequence = record.seq[start-1:end]
        reversed_complement = reverse_complement(subsequence)
        processed_subsequence = introduce_random_change(reversed_complement)

        record.seq = (
            record.seq[:start-1] +
            Seq(processed_subsequence) +
            record.seq[end:]
        )

    # Save the modified sequence to an output file
    output_filename = "output_processed_influenza.fasta"
    SeqIO.write([record], output_filename, "fasta")

    print(f"Processed influenza genome saved to {output_filename}")

