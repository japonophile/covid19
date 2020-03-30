from lib import translate, cc

# Protein alignments: http://virological.org/t/alignment-of-58-sarbecovirus-genomes-for-conservation-analysis-of-sars-cov-2/430

# https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2
# https://www.ncbi.nlm.nih.gov/nuccore/MN908947
# https://zhanglab.ccmb.med.umich.edu/C-I-TASSER/2019-nCov/

# whole thing has a "lipid bilayer envelope", with S E M sticking out
# the ORF proteins are non structural and form a "replicase-transcriptase complex"

# copy machine == https://www.uniprot.org/uniprot/Q0ZJN1
# zhanglab breaks this down into many more proteins, orf1b seems like a myth

# begin: 266 base pair "untranslated"
# https://en.wikipedia.org/wiki/Five_prime_untranslated_region

corona = {}

# 1ab = replicase polyprotein, https://www.ncbi.nlm.nih.gov/protein/YP_009724389.1?report=graph
# (same one for SARS v1 https://www.ncbi.nlm.nih.gov/protein/NP_828849.2?report=graph)
# 1-15 are in orf1ab
#    1 = Host translation inhibitor nsp1, leader protein
#    2 = ???
#    3 = Papin-like proteinase
#        see diff https://www.ncbi.nlm.nih.gov/projects/msaviewer/?rid=7FXGTZFN016&coloring=cons
#    4 = nsp4B_TM; contains transmenbrane domain 2 (TM2); produced by both pp1a and pp1b
#    5 = Proteinase 3CL-PRO
#    6 = putative transmembrane domain
#    7 = ???
#    8 = ???
#    9 = ssRNA-binding protein; produced by both pp1a and pp1ab
#   10 = nsp10_CysHis; formerly known as growth-factor-like protein (GFL)
#   11 = https://en.wikipedia.org/wiki/RNA-dependent_RNA_polymerase
#   12 = Helicase (Hel).
#   13 = Guanine-N7 methyltransferase (ExoN) or maybe 3'-to-5' exonuclease
#   14 = Uridylate-specific endoribonuclease (NendoU), endoRNAse
#   15 = 2'-O-methyltransferase (2'-O-MT), https://en.wikipedia.org/wiki/MRNA_(nucleoside-2%27-O-)-methyltransferase
corona['orf1a'] = translate(cc[266-1:13483], True)
## orf1b = translate(cc[13468-1:21555], False)
## try to fix orf1b with this piece backwards by 18 base pairs
corona['orf1b'] = translate(cc[13442-1:13468], False) + translate(cc[13468-1:21555], False)
corona['orf1b'] = corona['orf1b'].strip('*')
corona['orf1ab'] = corona['orf1a'] + corona['orf1b']

# exploit vector, attaches to ACE2, also called "surface glycoprotein"
# closed state -- https://www.ncbi.nlm.nih.gov/Structure/pdb/6VXX
# open state (after delivering payload?) -- https://www.ncbi.nlm.nih.gov/Structure/pdb/6VYB
# sort of 3 proteins, S1, S2 and S2'
corona['spike_glycoprotein'] = translate(cc[21563-1:25384], True)

corona['orf3a'] = translate(cc[25393-1:26220], True)

# these 2 things stick out
corona['envelope_protein'] = translate(cc[26245-1:26472], True)
corona['membrane_protein'] = translate(cc[26523-1:27191], True)  # orf5

corona['orf6'] = translate(cc[27202-1:27387], True)

# Non-structural protein which is dispensable for virus replication in cell culture.
# Suppression of host tetherin activity.
corona['orf7a'] = translate(cc[27394-1:27759], True)
corona['orf7b'] = translate(cc[27756-1:27887], True)

corona['orf8'] = translate(cc[27894-1:28259], True)

# capsid is the protein shell of a virus; the capsid encloses the genetic material of the virus
# Packages the positive strand viral genome RNA into a helical ribonucleocapsid (RNP)
corona['nucleocapsid_phosphoprotein'] = translate(cc[28274-1:29533], True)  # orf9

# ORF10: Coronavirus 3' UTR pseudoknot stem-loop 1
corona['orf10'] = translate(cc[29558-1:29674], True)

