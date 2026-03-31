import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, TextField, ElevatedButton, Text


def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # FUNÇÕES
    #  def msg_nome():
    #     text_msg = Text(f"Bom dia {input_nome.value}")
    #      input_nome.value = ""
    #      navegar("/tela_msg")

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    # COMPONENTES
    input_nome = TextField(label="Digite seu nome")
    #btn_salvar = ElevatedButton("Salvar", on_click=nome)



    # gerenciar telas(routes)

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
                    #Text("Digite seu nome"),
                    #btn_salvar,
                    input_nome,
                    Button("Salvar e Navegar", on_click=lambda: navegar("/segunda_tela"), color=Colors.PURPLE_400)

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
                        ),
                        #text_msg
                        Text(f"Bom Dia {input_nome.value}")

                    ]
                )
            )

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)



    # EVENTOS
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
