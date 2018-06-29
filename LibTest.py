"""
author  : kouui
date    : 2018-06
purpose : Functions for debugging
"""

import numpy as np

################################################################################
################################################################################

def makeTau(ND, e_max, relax=0):
    """
    make a 1D mesh of log scale from 0 to 1Ee_max with ND grid points.

    Input:
        ND: (,), number of grid points
        e_max: (,), with minvalue of 1Ee_max
        relax: (,), 0 -> 1  logspace -> linspace

    Output:
        Tau: (ND,), optical depth,
    """
    assert 0<=relax<=1, "let 0 <= relax <= 1 ."

    e_min = -4
    Tau = np.empty(ND,dtype=np.double)
    mid = e_max - np.log10(2)
    if relax ==0:
        Tau[:ND//2+1] = np.logspace(e_min,mid,ND//2+1)
    else:
        Tau[:ND//2+1] = np.logspace(e_min,mid,ND//2+1)*(1-relax) + np.linspace(10**e_min,10**mid,ND//2+1)*relax
    Tau[0] = 0
    Tau[ND//2+1:] = (-Tau[:ND//2+1][::-1]+2*Tau[ND//2])[1:]

    return Tau
