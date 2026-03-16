import pandas as pd
import pathlib
from dash import callback, Input, Output

# Chemin absolu vers le fichier CSV
PATH = pathlib.Path(__file__).parent.parent
df = pd.read_csv(PATH / 'datas' / 'avocado.csv')


@callback(
    Output("avocado-table", "data"),
    Input("region-dropdown", "value"),
    Input("type-dropdown", "value"),
)
def update_table(region, type_):
    """Filtre le tableau selon la région et le type sélectionnés."""
    # Filtre par région
    df_filtered = df[df["region"] == region]
    # Filtre par type si "Tous" n'est pas sélectionné
    if type_ != "Tous":
        df_filtered = df_filtered[df_filtered["type"] == type_]
    return df_filtered.to_dict("records")