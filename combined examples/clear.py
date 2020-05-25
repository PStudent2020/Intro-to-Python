# -*- coding: utf-8 -*-
"""
Created on Sun May 24 12:26:47 2020

@author: Troy
"""


def cls():
    try:
        from IPython import get_ipython
        get_ipython().magic('clear')
        get_ipython().magic('reset -f')
    except:
        pass
    %reset -f