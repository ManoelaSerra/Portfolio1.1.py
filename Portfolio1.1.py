import plotly.express as px
from dash import Dash, html, dcc
import pandas as pd

df = pd.read_csv('C:/Users/SANSUNG/PycharmProjects/PythonProject6/pessoa_faker.csv')


def cria_grafico(df):
    figuras = []

    figuras.append(px.histogram(df, x='salario', nbins=100, title='Salários'))

    figuras.append(px.pie(df, names='nome', color='vendas', title='Avaliações',
                          color_discrete_sequence=px.colors.sequential.RdBu, hole=0.3))

    fig = px.scatter(df, x='idade', y='salario', size='vendas', color='avaliacao',
                     hover_name='nome', size_max=10)
    fig.update_layout(title='Salário por idade')
    figuras.append(fig)

    fig = px.line(df, x='vendas', y='idade', color='nome', hover_name='avaliacao')
    fig.update_layout(title='Salário por Vendas', xaxis_title='Vendas', yaxis_title='Idade')
    figuras.append(fig)

    fig = px.scatter_3d(df, x='salario', y='idade', z='vendas',
                        color='avaliacao', color_discrete_sequence=["blue"])
    figuras.append(fig)

    fig = px.bar(df, x='idade', y='salario', color='avaliacao', barmode='group',
                 color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(
        title='Salário por idade',
        xaxis_title='Idade',
        yaxis_title='Salário',
        legend_title='Avaliação de Salário por idade',
        plot_bgcolor='rgba(222, 255, 253, 1)',
        paper_bgcolor='rgba(186, 245, 241, 1)',
    )
    figuras.append(fig)

    return figuras


def cria_app(df):
    app = Dash(__name__)
    figuras = cria_grafico(df)

    app.layout = html.Div([
        html.H1('Dashboard de Salários por Idade'),
        *[dcc.Graph(figure=fig) for fig in figuras]
    ])
    return app


if __name__ == '__main__':
    app = cria_app(df)
    app.run(debug=True, port=8051)

