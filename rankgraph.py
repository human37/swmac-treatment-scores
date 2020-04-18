import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def saveGraph(stations):
    # forces matplotlib to use noninteractive version, prevents attempted gui opening
    matplotlib.pyplot.switch_backend('Agg')
    # generates a bar graph of each station and its score, and saves it to a png file
    station_names = []
    scores = []
    for station in stations:
        station_names.append(station['q1'])
        scores.append(station['score'])
    x = np.arange(len(station_names))  
    fig, ax = plt.subplots()
    ax.bar(x, scores, width = 0.4, color = '#008cba')
    ax.set_ylabel('Score')
    ax.set_xticks(x)
    ax.set_xticklabels(station_names)
    fig.tight_layout()
    plt.savefig('static/images/graph.png', transparent = True)
