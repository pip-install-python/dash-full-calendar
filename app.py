from dash_extensions.enrich import DashProxy
from dash_extensions import Purify, DeferScript
from dash import html


app = DashProxy(assets_folder='assets')
app.layout = html.Div([Purify('<div class="card card-calendar" style="height: 75vh"><div class="card-body p-3"><div class="calendar" data-bs-toggle="calendar" id="calendar" ></div></div></div>'),
DeferScript(src='assets/full_calendar_deferscript.js')
])

if __name__ == "__main__":
    app.run_server()