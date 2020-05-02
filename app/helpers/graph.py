

def covid_graph(colors):
    return {
        "xaxis": {"tickformat": "%Y-%m-%d", "gridcolor": colors["grid"]},
        "yaxis": {"gridcolor": colors["grid"]},
        'plot_bgcolor': colors['background'],
        'paper_bgcolor': colors['background'],
        'font': {
            'color': colors['text']
        }
    }
