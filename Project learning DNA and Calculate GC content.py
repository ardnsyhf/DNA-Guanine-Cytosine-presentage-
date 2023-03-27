"""Correction DNA sequences from lower case and another non DNA string,
Nucleotide long, and GC presentage"""

judul_dna = """Influenza A virus (A/swine/Italy/81220/2017(H1N1)) 
segment 7 matrix protein 2 (M2) and matrix protein 1 (M1) genes
complete cds""" # masukkan judul nucleotide disini
print("Genes Title :", judul_dna)

#Enter a DNA sequence below
dna_base = """ATGAGTCTTCTAACCGAGGTCGAAACGTATGTTCTTTCTATCATCCCATCGGGCCCCCTCAAAGCCGAGA
TCGCACAGAGACTGGAAGGTGTCTTTGCAGGGAAGAACACAGATCTTGAGGCTCTAATGGAATGGCTAAA
GACAAGACCAATCCTGTCACCTCTGACTAAGGGAATTCTGGGGTTTGTGTTCACGCTCACCGTGCCCAGT
GAGCGAGGACTGCAGCGTAGACGCTTTGTTCAAAATGCCCTAAATGGAAATGGGGATCCTAATAACATGG
ATAGAGCAGTCAAATTATACAAGAAGCTAAAAAGGGAAATAACGTTCCATGGGGCAAAGGAAGTCTCATT
AAGCTACTCAACTGGTGCTCTTGCCAGTTGCATGGGCCTCATATACAATAGAATGGGAACAGTAACCACA
GAAGCTGCGTTCGGCCTGGTGTGTGCCACTTGTGAACAGATCGCTGATTCACAACATCGGTCACACAGAC
AAATGGCCACTACCACTAACCCACTAATCAGGCATGAAAACAGAATGGTACTGGCTAGCACTACAGCTAA
GGCTATGGAGCAGATGGCTGGATCGAGTGAACAGGCTGCAGAGGCCATGGAGGTTGCCAATCAGACCAGG
CAGATGGTGCATGCAATGAGAACAATTGGGACACATCCCAGCTCCAGTGCCGGTCTGAAAGATGATCTTC
TTGAAAATTTGCAGGCCTATCAGaaaCGGATGGGAGTGCAAATACAGCGGTTCAAGTGA"""

#Koreksi Nucleotide
dna_uppercase = dna_base.upper()

import re
dna = re.sub("[^ATCG]", "", dna_uppercase)
print("Urutan Nucleotide :", dna)

#Jumlah nucleotide
total_nuc = len(dna)
bp_symbol = "bp"
print("Jumlah Nucleotide Sebanyak =", total_nuc, bp_symbol)

#menghitung banyaknya Guanine dan cytosine
total_g = dna.count("G")
print("Jumlah Guanine :", total_g)
total_c = dna.count("C")
print("Jumlah Cytosine", total_c)

#menghitung presentase gc pada nucleotide
total_gc = total_g + total_c
presentage_gc = (total_gc / total_nuc) * 100 
hasil_presentage_gc = "{:.2f}%".format(presentage_gc)
print("hasil persentasi GC adalah", hasil_presentage_gc)