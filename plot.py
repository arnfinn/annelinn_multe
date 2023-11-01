#!/usr/bin/env python

import matplotlib.pyplot as plt
#import seaborn
#seaborn.set(style='ticks')

#plt.style.use('ggplot')

SIZE = 14
MEDIUM_SIZE = 16
BIGGER_SIZE = 18

plt.rc('font', size=SIZE)                # controls default text sizes
plt.rc('axes', titlesize=SIZE)           # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZE)          # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZE)          # fontsize of the tick labels
plt.rc('legend', fontsize=SIZE)          # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


datasett = [[[[0.3233,0.2244,0.1693],[0.3531,0.2183,0.1283],[0.4811,0.4217,0.3139],[0.4789,0.3959,0.2396]],[[0.1032,0.1305,0.0657],[0.0799,0.05226,0.12524],[0.1351,0.1108,0.0504],[0.2004,0.0962,0.1609]],[[0.094,0.08582,0.0798],[0.095,0.1321,0.0753],[0.1864,0.1264,0.0456],[0.2676,0.23,0.0917]]],[[[24.64,24.225,23.32],[21.85,18.84,22.04],[25.37,26.86,25.407],[23.61,19.486,20.626]],[[20.512,22.62,19.703],[19.729,18.17,14.527],[22.98,23.751,18.44],[22.75,19.005,19.86]],[[20.545,20.098,19.12],[19.161,17.91,17.794],[23.736,21.077,19.27],[19.833,18.921,17.253]]],[[[7.405,7.264,8.03],[7.478,7.175,7.109],[9.045,8.699,7.221],[6.469,5.716,4.959]],[[7.228,8.513,7.073],[7.297,6.145,5.674],[8.426,9.234,6.592],[6.175,5.902,4.567]],[[6.754,6.645,6.588],[7.467,6.027,6.386],[8.354,7.973,6.729],[5.53,5.126,4.608]]],[[[3.627,3.693,3.972],[3.457,3.536,3.535],[4.461,4.34,3.506],[3.059,2.682,2.471]],[[3.638,4.363,3.514],[3.57,2.931,2.338],[4.109,4.465,3.032],[3.037,2.864,2.209]],[[3.23,3.349,3.222],[3.244,2.643,2.793],[3.907,3.668,3.079],[2.6692,2.4392,2.0265]]]]

bw = True
col = ["#a6611a", "#dfc27d", "#80cdc1", "#018571"]
linestyle = ["-","-","-","-"]
if bw:
    col = ["black","black","black","black"]
    linestyle = ["-","--","-.",":"]


m = 0
navn = ["TA", "TP", "EA", "MS"]
aar = ["2012","2013","2014"]
multe = ["102","306","Fjellgull","Fjordgull"]
xakse = ["Early","Middle","Late","Early","Middle","Late","Early","Middle","Late"]

for i in navn:
    l = 0
    m += 1
    for j in aar:
        l += 1
        n = 0
        for k in multe:
            n += 1
            plt.plot([0+(l-1)*3,1+(l-1)*3,2+(l-1)*3], datasett[m-1][l-1][n-1], color = col[n-1], ls = linestyle[n-1], label = k if l == 1 else "")

    legloc = "lower left"
    print(i)
    if i == "TA":
        lab = "mg/g dw"
        ymax = 0.65
        legloc = "upper right"
        plotnr = "c"
    elif i == "TP":
        lab = "mg GA/g dw"
        ymax = 32
        plotnr = "a"
    elif i == "EA":
        lab = "mg/g dw"
        ymax = 11
        plotnr = "b"
    elif i == "MS":
        lab = ""
        ymax = 5
        
    plt.axvspan(2.5, 5.5, facecolor='grey', alpha=0.05)
    plt.xticks((0,1,2,3,4,5,6,7,8), xakse, rotation=70)

    plt.xlim(-0.5,8.5)
#    plt.legend(fancybox=True, shadow=True, loc = "lower left")
    plt.legend(loc = legloc)
    plt.ylim(ymin=0, ymax = ymax)
    plt.ylabel(lab)
    plt.annotate(plotnr, (0,0), (15, 255), xycoords='axes fraction', textcoords='offset points', va='top', fontsize = 22)

    if i == "TA":
        aarstall = 310
        aarstall = -70
        plt.annotate('2012', (0,0), (40, aarstall), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.annotate('2013', (0,0), (160, aarstall), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.annotate('2014', (0,0), (280, aarstall), xycoords='axes fraction', textcoords='offset points', va='top')
    else:
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelbottom='off') # labels along the bottom edge are off

    if i != "MS":
        plt.savefig(i+".pdf", bbox_inches='tight', transparent=True)
    plt.clf()


