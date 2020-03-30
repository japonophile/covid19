from Bio import Entrez
import json
import os
import requests
import yaml

ncov_seq_url = "https://www.ncbi.nlm.nih.gov/core/assets/genbank/files/ncov-sequences.yaml"
seqs = yaml.load(requests.get(ncov_seq_url).text, Loader=yaml.FullLoader)
seqs = seqs['genbank-sequences']
print('Found %d sequences' % len(seqs))

allseq = {}
for x in seqs:
    if 'gene-region' in x and x['gene-region'] == 'complete':
        nm = x['accession']
        print('Downloading', nm)
        dna = Entrez.efetch(db='nucleotide', id=nm,
                            email='antoine@japonophile.com',
                            rettype='fasta', retmode='text').read().split('\n')[1:]
        allseq[nm] = ''.join(dna)

outfile = 'data/allseq.json'
print('Saving sequences to', outfile)
os.makedirs('data', exist_ok=True)
with open(outfile, 'w') as f:
    json.dump(allseq, f)

