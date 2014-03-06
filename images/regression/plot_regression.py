from pylab import *
from mpltools import style
style.use('ggplot')
import numpy as np
X = np.linspace(0,1,100) + np.random.random(100)/8
y = X + np.random.random(100)/10-.05
def do_plot(X, y, name):
    clf()
    scatter(X, y)
    xlim(-.1,1.2)
    ylim(-.1,1.2)
    xlabel('Real')
    ylabel('Predicted')
    plot([0,1.1], [0,1.1],  lw=2)
    xticks([])
    yticks([])
    R2 = np.corrcoef(X, y)[0,1]**2
    text(.2,.8,r'$R^2 = {}\%$'.format(int(R2*100)), fontdict={'fontsize': 16})
    N = 1. - np.dot(X-y, X-y)/np.dot(X,X)
    N = max(N, 0)
    text(.2,.7,r'$N = {}\%$'.format(int(N*100)), fontdict={'fontsize': 16})
    savefig(name + '.png')


do_plot(X, y, 'base')
do_plot(X, X.mean()-X, 'null')
do_plot(X, y-.25, 'biased')
do_plot(X, .5 + .5*(y - .5), 'mean_regression')
