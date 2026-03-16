from dash import Dash
import dash_bootstrap_components as dbc
from pages.compare import layout
import pages.compare_cb

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)