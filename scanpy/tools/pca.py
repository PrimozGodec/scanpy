# Copyright 2016-2017 F. Alexander Wolf (http://falexwolf.de).
"""
Principal Component Analysis

Notes
-----
There are two PCA versions, which are automatically chosen
- sklearn.decomposition.PCA
- function _pca_fallback
"""

from ..compat.matplotlib import pyplot as pl
from .. import settings as sett
from .. import plotting as plott
from .. import utils
from .. import preprocess as pp
from ..ann_data import AnnData

def pca(adata_or_X, nr_comps=10):
    """
    Embed data using PCA.

    Parameters
    ----------
    adata_or_X : dict containing
        X : np.ndarray
            Data array, rows store observations, columns variables.
    nr_comps : int, optional (default: 2)
        Number of PCs.

    Returns
    -------
    dtsne : dict containing
        Y : np.ndarray
            PCA representation of the data.
    """
    if isinstance(adata_or_X, AnnData):
        X = adata_or_X.X
        isadata = True
    else:
        X = adata_or_X
        isadata = False
    Y = pp.pca(X, nr_comps)
    if isadata:
        return {'type': 'pca', 'Y': Y}
    else:
        return Y

def plot(dplot, adata,
         smp='',
         comps='1,2',
         layout='2d',
         legendloc='lower right',
         cmap='jet',
         adjust_right=0.75):
    """
    Plot the results of a DPT analysis.

    Parameters
    ----------
    dplot : dict
        Dict returned by plotting tool.
    adata : dict
        Data dictionary.
    smp : str, optional (default: first anntotated group)
        Sample annotation for coloring, possible are all keys in adata.smp_keys(),
        or gene names.
    comps : str, optional (default: "1,2")
         String in the form "comp1,comp2,comp3".
    layout : {'2d', '3d', 'unfolded 3d'}, optional (default: '2d')
         Layout of plot.
    legendloc : {none, see matplotlib.legend}, optional (default: 'lower right')
         Options for keyword argument 'loc'.
    cmap : str (default: "jet")
         String denoting matplotlib color map.
    adjust_right : float, optional (default: 0.75)
         Increase to increase the right margin.
    """
    from .. import plotting as plott
    plott.plot_tool(dplot, adata,
                    smp,
                    comps,
                    layout,
                    legendloc,
                    cmap,
                    adjust_right,
                    # defined in plotting
                    subtitles=['PCA'],
                    component_name='PC')
