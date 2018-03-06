'''
General utility functions
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

import operator

def sort_coef(features, coefs):
    pairs = dict()
    for idx, val in enumerate(features):
        pairs[val] = coefs[idx]

    return sorted(pairs.items(), key=operator.itemgetter(1), reverse=True)
