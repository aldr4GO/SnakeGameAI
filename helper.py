import matplotlib.pyplot as plt
from IPython import display

plt.ion()
fig, ax = plt.subplots()
def plot(scores, mean_scores, record):
    fig.canvas.flush_events()  # flush GUI events for update
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=-1,ymax=record+1)
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    fig.canvas.draw()          # redraw the canvas