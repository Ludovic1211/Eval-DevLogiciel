import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

# Import des callbacks (nécessaire pour l'enregistrement auprès de Dash)
import pages.table_cb
import pages.compare_cb

# Initialisation de l'application en mode multipages
app = Dash(
    __name__,
    use_pages=True,
    pages_folder="pages",
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

# Barre de navigation principale
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Affichage des données", href="/", active="exact")),
        dbc.NavItem(dbc.NavLink("Comparaison entre région", href="/compare", active="exact")),
        dbc.NavItem(dbc.NavLink("Aide en ligne", href="/markdown", active="exact")),
    ],
    brand="Application des M2 MECEN",
    brand_href="/",
    color="primary",
    dark=True,
    fluid=True,
)

# Layout principal — la navbar + le contenu de la page active
app.layout = dbc.Container([
    navbar,
    html.Div(className="mt-3"),
    dash.page_container,
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)