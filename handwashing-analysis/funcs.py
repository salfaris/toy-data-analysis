# MIT License

# Copyright (c) 2020 Salman Ahmad Faris

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def timeseries_plot(ax,
                    x,
                    y,
                    xlabel,
                    ylabel,
                    color = 'black',
                    linestyle = 'solid',
                    alpha = 1,
                    color_ticks = True):
    '''Plots a timeseries.
    
    Args: 
        ax (axes): The axes to be plotted onto
        x (pandas Series): Dependent variable of plot 
            (expected a DatetimeIndex)
        y (pandas Series): Independent variable of plot
        xlabel (str): X label
        ylabel (str): Y label
        color (str, optional): Color of plot
        linestyle (str, optional): Linestyle of plot
        alpha (float, optional): Transparency of plot
        color_ticks (boolean, optional): If True, colors ylabel and ticks
            with color

    Returns:
        Plots y versus x as lines
    '''
    ax.plot(x, y, color, linestyle = linestyle, alpha = alpha)
    ax.set_xlabel(xlabel)
    
    if color_ticks == True:
        ax.set_ylabel(ylabel, color = color)
        ax.tick_params('y', colors = color)
    else:
        ax.set_ylabel(ylabel)

def func_diff_bootstrap_replicate(pre_series, post_series, func=np.mean):
    '''Generates bootstrap replicate of the difference in func applied
     to two pre-post pandas Series.
    
    Args:
        pre_series (pandas Series): Pre-Series to be replicated
        post_series (pandas Series): Post-Series to be replicated
        func (numpy function, optional): Statistic of interest
            (mean, median, std, var)

    Returns:
        float: Difference between func applied to replicated Post-Series
            and func applied to replicated Pre-Series
    '''
    pre_replicate =  pre_series.sample(frac=1, replace=True)
    post_replicate = post_series.sample(frac=1, replace=True)
    func_diff = func(post_replicate) - func(pre_replicate)
    return func_diff

def conf_interval(lst, conf=90, result='series'):
    '''Computes the confidence interval from a list and returns a
     pandas Series or a numpy array.
    
    Args:
        lst (list): Sample data to compute confidence interval on
        conf (float, optional): conf% confidence interval
        result (str, optional): Returns confidence interval in the 
            form of result (Series/array)
    
    Returns:
        pandas Series: If result='series' (default)
        numpy array: If result='array'
    '''
    if result == 'series':
        if conf == 90:
            return pd.Series(lst).quantile([0.05, 0.95])
        elif conf == 95:
            return pd.Series(lst).quantile([0.025, 0.975])
        elif conf == 97.5:
            return pd.Series(lst).quantile([0.0125, 0.9875])
        elif conf == 99:
            return pd.Series(lst).quantile([0.005, 0.995])

    if result == 'array':
        if conf == 90:
            return np.percentile(lst, [5, 95])
        elif conf == 95:
            return np.percentile(lst, [2.5, 97.5])
        elif conf == 97.5:
            return np.percentile(lst, [1.25, 98.75])
        elif conf == 99:
            return np.percentile(lst, [0.5, 99.5])