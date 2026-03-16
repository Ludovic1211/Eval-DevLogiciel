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

# Options des dropdowns
regions = sorted(df['region'].drop_duplicates())
region_options = [{'label': region, 'value': region} for region in regions]

types = sorted(df['type'].drop_duplicates())
type_options = [{'label': 'Tous', 'value': 'Tous'}] + [{'label': t, 'value': t} for t in types]

# Colonnes à masquer
COLUMNS_TO_HIDE = ["Unnamed: 0", "4046", "4225", "4770",
                   "Small Bags", "Large Bags", "XLarge Bags"]

columns = [{"name": col, "id": col}
           for col in df.columns
           if col not in COLUMNS_TO_HIDE]

layout = dbc.Container([
    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label("Sélectionner une région:"),
                    dbc.Select(
                        id="region-dropdown",
                        options=region_options,
                        value=regions[0],
                    ),
                ], xs=12, md=6),
                dbc.Col([
                    dbc.Label("Sélectionner un type:"),
                    dbc.Select(
                        id="type-dropdown",
                        options=type_options,
                        value="Tous",
                    ),
                ], xs=12, md=6),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col([
                    dash_table.DataTable(
                        id="avocado-table",
                        columns=columns,
                        data=df.to_dict("records"),
                        page_size=10,
                        style_header={
                            "backgroundColor": "#0d6efd",
                            "color": "white",
                            "fontWeight": "bold",
                        },
                        style_cell={"textAlign": "left"},
                        style_data_conditional=[
                            {"if": {"row_index": "odd"},
                             "backgroundColor": "#f8f9fa"}
                        ],
                    )
                ])
            ])
        ])
    ])
], fluid=True)