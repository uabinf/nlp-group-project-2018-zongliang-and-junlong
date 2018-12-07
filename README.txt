README file

The script is 'AssembleFeatureBased.ipynb'
pre-request libraries:
python script has been tested use python 2.7
pandas, codecs, pprint, json, re, statistics, nltk, gensim, sklearn, sknn, sys, numpy, matplotlib

The input file includes:
1.'abstract10000.json' (exported from oracle database and original from the NCBI)
2.'gene2pubtatorTruncated.txt' (ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTator/)
3.'negationAnnotated' (human annotated)
4.'isolatorAnnotated.txt' (human annotated)
5.'regulationAnnotated.txt' (human annotated)
6.'regulationAnnotatedAll.txt' (human annotated)

Pre-processing:
1.'modify.py' is used for transferring one line json data to multiple-lines.
2.'w2v.ipynb' is used for getting vector presentation of words by reading 'modified_abstract.json'(the 13GB file that is not uploaded here)&'gene.csv'.
3.'w2v_load.ipynb' is used for get positive and negtive words by loading 'w2v.model'(the result of 'w2v.ipynb').
4.'HumanAnnotatedAnalysis.ipynb' is used for analysing the Human Annotated result.
