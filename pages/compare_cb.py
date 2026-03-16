import pandas as pd
import pathlib
import plotly.express as px
from dash import callback, Input, Output

# Chemin absolu vers le fichier CSV
PATH = pathlib.Path(__file__).parent.parent
df = pd.read_csv(PATH / 'datas' / 'avocado.csv')

# Calcul de l'échelle globale pour garder la même échelle sur les deux graphiques
y_min = df.groupby(["region", "Date"])["AveragePrice"].mean().min()
y_max = df.groupby(["region", "Date"])["AveragePrice"].mean().max()


def make_figure(region):
    """Crée un graphique linéaire du prix moyen pour une région donnée."""
    df_filtered = df[df["region"] == region].copy()
    df_filtered["Date"] = pd.to_datetime(df_filtered["Date"])
    df_avg = df_filtered.groupby("Date")["AveragePrice"].mean().reset_index()
    fig = px.line(
        df_avg,
        x="Date",
        y="AveragePrice",
        title=f"Prix moyen dans le temps - {region}",
        labels={"AveragePrice": "Prix moyen ($)", "Date": "Date"},
        template="simple_white",
    )
    # Même échelle pour les deux graphiques pour une comparaison visuelle efficace
    fig.update_yaxes(range=[y_min * 0.95, y_max * 1.05])
    return fig


@callback(
    Output("graph-region1", "figure"),
    Input("region1-dropdown", "value"),
)
def update_graph1(region):
    """Met à jour le graphique de la région 1."""
    return make_figure(region)


@callback(
    Output("graph-region2", "figure"),
    Input("region2-dropdown", "value"),
)
def update_graph2(region):
    """Met à jour le graphique de la région 2."""
    return make_figure(region)