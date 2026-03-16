import dash
import pandas as pd
import pathlib
from dash import html, dash_table
import dash_bootstrap_components as dbc

# Enregistrement de la page
dash.register_page(__name__, path="/", name="Affichage des données", order=0)

# Chemin absolu vers le fichier CSV
PATH = pathlib.Path(__file__).parent.parent
df = pd.read_csv(PATH / 'datas' / 'avocado.csv')

# Colonnes à masquer dans le tableau
COLUMNS_TO_HIDE = ["Unnamed: 0", "4046", "4225", "4770",
                   "Small Bags", "Large Bags", "XLarge Bags"]

# Options des dropdowns
regions = sorted(df['region'].drop_duplicates())
region_options = [{'label': r, 'value': r} for r in regions]

types = sorted(df['type'].drop_duplicates())
type_options = [{'label': 'Tous', 'value': 'Tous'}] + [{'label': t, 'value': t} for t in types]

# Colonnes affichées dans le tableau
columns = [{"name": col, "id": col}
           for col in df.columns
           if col not in COLUMNS_TO_HIDE]

layout = dbc.Container([
    dbc.Card([
        dbc.CardBody([
            # Ligne des filtres
            dbc.Row([
                dbc.Col([
                    dbc.Label("Sélectionner une région:", className="fw-bold"),
                    dbc.Select(
                        id="region-dropdown",
                        options=region_options,
                        value=regions[0],
                    ),
                ], xs=12, md=6, className="mb-3 mb-md-0"),
                dbc.Col([
                    dbc.Label("Sélectionner un type:", className="fw-bold"),
                    dbc.Select(
                        id="type-dropdown",
                        options=type_options,
                        value="Tous",
                    ),
                ], xs=12, md=6),
            ], className="mb-4"),
            # Tableau de données
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dash_table.DataTable(
                            id="avocado-table",
                            columns=columns,
                            data=df.to_dict("records"),
                            page_size=10,
                            sort_action="native",
                            style_header={
                                "backgroundColor": "#0d6efd",
                                "color": "white",
                                "fontWeight": "bold",
                                "textAlign": "left",
                            },
                            style_cell={
                                "textAlign": "left",
                                "padding": "8px",
                                "fontFamily": "sans-serif",
                            },
                            style_data_conditional=[
                                {"if": {"row_index": "odd"},
                                "backgroundColor": "#f8f9fa"}
                            ],
                        )
                    ], style={"borderRadius": "8px", "overflow": "hidden"})
                ])
            ])
        ])
    ], className="shadow-sm rounded-3", style={"overflow": "hidden"})
], fluid=True)