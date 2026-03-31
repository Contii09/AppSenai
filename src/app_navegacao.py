import asyncio

import flet
from flet import ThemeMode, View, Colors, Button


def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    #FUNÇÕES
    #navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)

        )


    #gerenciar telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Primeira Página",
                        bgcolor=Colors.PURPLE_600

                    ),
                    Button("Ir para segunda tela", on_click=lambda: navegar("/segunda_tela"), color=Colors.PURPLE_400),

                ]
            )
        )



        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Segunda Página",
                            bgcolor=Colors.PURPLE_600

                        )

                    ]
                )
            )





    #voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)


    #COMPONENTES


    #EVENTOS
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)