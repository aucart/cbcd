""" Minimal example to compare Matplotlib and Plotly """

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import plotly.graph_objects as go
import plotly.io

## -------------------------------------------------------------

# Create dummy summary data
df = pd.DataFrame( np.array([ [10,15,3],
                               [5,7,4],
                               [5,8,5],]), columns=['cdt1','cdt2','ages'])


## -------------------------------------------------------------
## Option1: Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Some input data formatting
x = df['ages']
x = np.arange(len(x)) # label locations

width = 0.35     # width of the bars

# Plot
fig, ax = plt.subplots()
ax.bar(x - width/2, df['cdt1'], width, label='cdt1', color='blue', alpha=0.6)
ax.bar(x + width/2, df['cdt2'], width, label='cdt2', color='green', alpha=0.6)

# Arrange axes and titlesax.set_ylabel('Counts')
ax.set_title('Example with Matplotlib')
ax.set_xticks(x)
ax.set_xticklabels(x)
ax.legend()



## -------------------------------------------------------------
## Option2: Plotly

# Some input data formatting
x = df['ages']
x = list(range(len(x)))

# Specify the plots
bar_plots = [
    go.Bar(x=x, y=df['cdt1'], name='cdt1', marker=go.bar.Marker(color='blue')),
    go.Bar(x=x, y=df['cdt2'], name='cdt2', marker=go.bar.Marker(color='green'))
]

# Arrange axes and titles
layout = go.Layout(
    title=go.layout.Title(text="Example with Plotly", x=0.5),
    yaxis_title="Counts",
    xaxis_tickmode="array",
    xaxis_tickvals=list(range(len(x))),
    xaxis_ticktext=tuple(df['ages'].values),
)

# Actually makes the figure
fig = go.Figure(data=bar_plots, layout=layout)

# Put the figure in a html file
plotly.offline.plot(fig, filename='test.html')
