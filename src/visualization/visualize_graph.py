# visualize_graph.py
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
matplotlib.use('TkAgg')

def draw_graph_with_matplotlib(G):
    """
    Uses Matplotlib to draw the graph.
    """
    pos = nx.spring_layout(G)  # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue", alpha=0.6)
    # edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.3)
    # labels
    nx.draw_networkx_labels(G, pos, font_size=12)
    plt.title('Graph Visualization with Matplotlib')
    plt.show()

def draw_graph_with_plotly(G):
    """
    Uses Plotly to create an interactive graph visualization.
    """
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    node_text = []
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_x.append(x)
        node_y.append(y)
        node_text.append(f"{G.nodes[node]['type']}: {node}")

    node_trace = go.Scatter(
        x=node_x, y=node_y, text=node_text,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            color=[],
        ))

    for node, adjacencies in enumerate(G.adjacency()):
        node_trace.marker.color.append(len(adjacencies[1]))  # Color node by number of connections

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=0),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        title='Graph Visualization with Plotly'))
    fig.show()

def visualize_subgraph(G, title="Subgraph"):
    pos = nx.spring_layout(G)  # Layout for the subgraph
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    plt.title(title)
    plt.show()

def batch_process_graph(G, batch_size=10):
    nodes = list(G.nodes())
    for i in range(0, len(nodes), batch_size):
        subgraph_nodes = nodes[i:i + batch_size]
        subgraph = G.subgraph(subgraph_nodes)
        visualize_subgraph(subgraph, title=f"Subgraph {i // batch_size + 1}")

if __name__ == "__main__":
    G = nx.DiGraph()
    # Populate G with example data for demonstration
    G.add_node(1, type='User', pos=(1, 2))
    G.add_node(2, type='Transaction', pos=(2, 3))
    G.add_node(3, type='Product', pos=(3, 1))
    G.add_edge(1, 2)
    G.add_edge(2, 3)

    # Ensure all nodes have positions
    pos = nx.spring_layout(G)  # This will calculate positions if not already set
    for node in G.nodes():
        G.nodes[node]['pos'] = pos[node]  # Ensure each node has a 'pos' attribute

    draw_graph_with_matplotlib(G)
    draw_graph_with_plotly(G)
    batch_process_graph(G, batch_size=20)
