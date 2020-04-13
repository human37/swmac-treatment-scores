import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def saveGraph(stations):
    matplotlib.pyplot.switch_backend('Agg')
    # generates a bar graph of each station and its score, and saves it to a png file
    station_names = []
    scores = []
    for station in stations:
        station_names.append(station['q1'])
        scores.append(station['score'])
    x = np.arange(len(station_names))  
    fig, ax = plt.subplots()
    ax.bar(x, scores)
    ax.set_ylabel('Score')
    ax.set_xticks(x)
    ax.set_xticklabels(station_names)
    fig.tight_layout()
    plt.savefig('static/images/graph.png', transparent = True)
