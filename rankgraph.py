import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def saveGraph(stations):
    # forces matplotlib to use noninteractive version, prevents attempted gui opening
    matplotlib.pyplot.switch_backend('Agg')
    # generates a bar graph of each station and its score, and saves it to a png file
    station_names = []
    scores = []
    stations.reverse()
    for station in stations:
        station_names.append(station['location'])
        scores.append(station['score'])
    y = np.arange(len(station_names))  
    fig, ax = plt.subplots(figsize=(8, 18))
    ax.barh(y, scores, color = '#008cba')
    ax.set_yticks(y)
    ax.set_yticklabels(station_names)
    ax.xaxis.tick_top()
    right_side = ax.spines['right']
    top_side = ax.spines['top']
    left_side = ax.spines['left']
    bottom_side = ax.spines['bottom']
    bottom_side.set_visible(False)
    right_side.set_visible(False)
    top_side.set_visible(False)
    left_side.set_visible(False)
    plt.margins(y=0)
    fig.tight_layout()
    plt.savefig('static/images/graph.png', transparent = True)
