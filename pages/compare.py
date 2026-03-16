import dash
import pandas as pd
import pathlib
from dash import dcc, html
import dash_bootstrap_components as dbc

# Enregistrement de la page
dash.register_page(__name__, path="/compare", name="Comparaison entre région", order=1)

# Chemin absolu vers le fichier CSV
PATH = pathlib.Path(__file__).parent.parent
df = pd.read_csv(PATH / 'datas' / 'avocado.csv')

# Options des régions
regions = sorted(df['region'].drop_duplicates())
region_options = [{'label': r, 'value': r} for r in regions]

layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(
            html.H5("Prix moyen dans le temps", className="text-white mb-0"),
            className="bg-primary"
        ),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dbc.Badge("Région 1", color="primary", className="mb-2"),
                    dbc.Select(
                        id="region1-dropdown",
                        options=region_options,
                        value=regions[0],
                    ),
                ], xs=12, md=6),
                dbc.Col([
                    dbc.Badge("Région 2", color="primary", className="mb-2"),
                    dbc.Select(
                        id="region2-dropdown",
                        options=region_options,
                        value=regions[1],
                    ),
                ], xs=12, md=6),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="graph-region1"),
                ], xs=12, md=6),
                dbc.Col([
                    dcc.Graph(id="graph-region2"),
                ], xs=12, md=6),
            ])
        ])
    ])
], fluid=True)