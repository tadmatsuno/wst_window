import solara
from matplotlib.figure import Figure
import numpy as np

delwvl_cwvl = 0.1022

@solara.component
def Page():
    arms = []
    set_arms = []
    colors = ['C4','C0','C2','C1','C3']
    for cwvl in [4150.0,4725.0,5400.0,6550.0,7350.0]:
        _arm,_set_arm = solara.use_state(cwvl)
        arms.append(_arm)
        set_arms.append(_set_arm)
    fig = Figure(figsize=(15,10))
    ax = fig.subplots(1,1)
    ax.set_xlim(3500,10000)
    for ii in range(5):
       wvl_min = arms[ii]*(1-delwvl_cwvl*0.5)
       wvl_max = arms[ii]*(1+0.5*delwvl_cwvl)
       ax.fill_betweenx([0,1], wvl_min, wvl_max,color=colors[ii], alpha=0.1)
       ax.text(wvl_min,1.0+0.02*(ii%2),f'{wvl_min:.0f}',color=colors[ii],fontsize=8,ha='center',va='bottom')
       ax.text(wvl_max,1.0+0.02*(ii%2),f'{wvl_max:.0f}',color=colors[ii],fontsize=8,ha='center',va='bottom')
    with solara.Column() as main:
        with solara.Columns([1,3]):
            with solara.Card():
                for ii in range(5):
                    solara.SliderFloat('Arm'+str(ii+1), min=3500, max=10000, step=1.,
                        value=arms[ii], on_value=set_arms[ii])
            solara.FigureMatplotlib(fig,dependencies=arms)
    return 

Page()