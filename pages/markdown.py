import pathlib
from dash import dcc, html
import dash_bootstrap_components as dbc

# Chemin absolu vers les fichiers Markdown
PATH = pathlib.Path(__file__).parent.parent


def read_md(filename):
    with open(PATH / filename, encoding="utf-8") as f:
        return f.read()


expli1 = read_md("expli1.md")
expli2 = read_md("expli2.md")
expli3 = read_md("expli3.md")

layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(
            html.H5(
                "Présentation de Dash",
                className="text-white text-center text-uppercase mb-0"
            ),
            style={
                "backgroundImage": "url('/assets/dash.jpg')",
                "backgroundSize": "cover",
                "padding": "30px",
            },
        ),
        dbc.CardBody([
            dbc.Accordion([
                dbc.AccordionItem(
                    dcc.Markdown(expli1),
                    title="Accueil",
                ),
                dbc.AccordionItem(
                    dcc.Markdown(expli2),
                    title="Layout",
                ),
                dbc.AccordionItem(
                    dcc.Markdown(expli3),
                    title="CallBack",
                ),
            ], start_collapsed=True),
        ])
    ])
], fluid=True)