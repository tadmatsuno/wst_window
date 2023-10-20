import solara
import matplotlib.pyplot as plt


all_resolutions = ['2k','3k','5k','10k','20k','40k']
all_feh = ['-3','-1','0']

@solara.component
def Page():
    feh,set_feh = solara.use_state('-1')
    res,set_res = solara.use_state('40k')
    st,set_st = solara.use_state('Giant')
    fig = plt.figure(figsize=(10,6),dpi=300)
    img = plt.imread(f'./pngfiles/{st}_MH{feh}_R{res}_v3.png')
    plt.axis('off')
    plt.imshow(img)
    with solara.Column() as main:
        with solara.Columns([1,2]):
            with solara.Card():
                solara.SliderValue('Resolution',value=res,
                                 values = all_resolutions,
                                 on_value=set_res)
                solara.SliderValue('[M/H]',value=feh,
                                 values = all_feh,
                                 on_value=set_feh)        
                solara.Select('Giant/Sun',
                              values=['Giant','Sun'],
                              value=st,on_value=set_st)
                solara.SelectMultiple('Element',
                            values=['C','N','O','Mg','Al','Sc','Mn','Cu','Zn','Sr','Y','Zr','Ba','La','Sm','Eu'],
                            all_values=['C','N','O','Mg','Al','Sc','Mn','Cu','Zn','Sr','Y','Zr','Ba','La','Sm','Eu'])
            solara.FigureMatplotlib(fig,dependencies=[res,feh,st])
    return 

Page()





