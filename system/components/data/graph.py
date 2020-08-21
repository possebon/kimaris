# Python Standard Libraries

# External Libraries
import igraph as ig
import chart_studio.plotly as py
import plotly.graph_objs as go
import dash_core_components as dcc

# Database
from components.database.graph import get_standard_graph


def get_figure(nodes=None, links=None, sizes_=None, name="", standard=False, source="https://scholar.google.com.br/"):
    # Standard graph
    if standard:
        nodes, links, sizes_ =  get_standard_graph()
    
    # Re-scale sizes
    # Big values (x > 40) make the graph awful
    MAX = max(sizes_)
    sizes = []
    if MAX > 3000:
        DIVIDE = 100
    elif MAX > 1500:
        DIVIDE = 50
    elif MAX > 750:
        DIVIDE = 40
    elif MAX > 300:
        DIVIDE = 20
    elif MAX > 100:
        DIVIDE = 10
    elif MAX > 30:
        DIVIDE = 5
    else:
        DIVIDE = 1
    for size in sizes_:
        size = (size+1)//(MAX//DIVIDE)
        sizes.append(size+6)
        
    N=len(nodes)
    L=len(links)
    Edges=[(links[k]['source'], links[k]['target']) for k in range(L)]

    G=ig.Graph(Edges, directed=False)

    labels=[]
    group=[]
    for node in nodes:
        labels.append(node['name'])
        group.append(node['group'])
        
    layt=G.layout_auto(dim=3)

    Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
    Yn=[layt[k][1] for k in range(N)]# y-coordinates
    Zn=[layt[k][2] for k in range(N)]# z-coordinates
    Xe=[]
    Ye=[]
    Ze=[]
    for e in Edges:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]
        Ze+=[layt[e[0]][2],layt[e[1]][2], None]
    
    
    
    if len(labels) == 2:
        Xn=[0,1]
        Yn=[0,2]
        Zn=[0,1]
        Xe=[0,1, None]
        Ye=[0,2, None]
        Ze=[0,1, None]

    trace1=go.Scatter3d(x=Xe,
                y=Ye,
                z=Ze,
                mode='lines',
                line=dict(color='rgb(125,125,125)', width=1),
                hoverinfo='skip',
                )

    trace2=go.Scatter3d(x=Xn,
                y=Yn,
                z=Zn,
                mode='markers',
                name='actors',
                marker=dict(symbol='circle',
                                size=sizes,
                                color=group,
                                colorscale='Viridis',
                                line=dict(color='rgb(50,50,50)', width=0.5)
                                ),
                text=labels,
                hoverinfo='text'
                )

    axis=dict(showbackground=False,
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title=''
            )

    layout = go.Layout(
            title=name,
            showlegend=False,
            scene=dict(
                xaxis=dict(axis),
                yaxis=dict(axis),
                zaxis=dict(axis),
            ),
        margin=dict(l=0, r=0, t=0, b=0),
        hovermode='closest',
        annotations=[
            dict(
            showarrow=False,
                text=f"Data source: <a href='{source}'>Google Scholar</a>",
                xref='paper',
                yref='paper',
                x=0,
                y=0.1,
                xanchor='left',
                yanchor='bottom',
                font=dict(
                size=14
                )
                )
            ],    )


    

    data=[trace1, trace2]
    fig=go.Figure(data=data, layout=layout)
    fig.update_layout(
    autosize=True)
    
    return fig

def get_graph(figure):
    config = {'responsive': True}
    graph = dcc.Graph(figure=figure, id="graph", config = config, style={"height": "92vh", "width": "100%", "padding-left": "2em"})
    
    return graph