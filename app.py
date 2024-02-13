from dash_extensions.enrich import DashProxy
from dash_extensions import Purify, DeferScript
from dash import html


app = DashProxy(assets_folder='assets')
app.layout = html.Div([
                html.Div(className="card card-calendar", style={"height": "100%"}, children=[
                        html.Div(className="card-body p-3", children=[
                            html.Div(id="calendar", **{"data-bs-toggle": "calendar"})
                        ])
                    ]),
                DeferScript(src='assets/full_calendar_deferscript.js')
])

if __name__ == "__main__":
    app.run_server()