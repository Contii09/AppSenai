import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, TextField, Text, ElevatedButton, Container, Column, Icon, Icons, Row, \
    CrossAxisAlignment
from flet.controls import page
from flet.controls.border_radius import horizontal


def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    def cafeteira():
        text_marca.value = input_marca.value
        text_preco.value = input_preco.value
        text_cor.value = input_cor.value
        text_tamanho.value = input_tamanho.value
        text_capacidade.value = input_capacidade.value

        tem_erro = False

        # MARCA
        if input_marca.value:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatorio"

        # PREÇO
        if input_preco.value:
            input_preco.error = None
        else:
            tem_erro = True
            input_preco.error = "Campo obrigatorio"

        # COR
        if input_cor.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatorio"

        # TAMANHO
        if input_tamanho.value:
            input_tamanho.error = None
        else:
            tem_erro = True
            input_tamanho.error = "Campo obrigatorio"

        # CAPACIDADE
        if input_capacidade.value:
            input_capacidade.error = None
        else:
            tem_erro = True
            input_capacidade.error = "Campo obrigatorio"

        if not (tem_erro):
            input_marca.value = ""
            input_preco.value = ""
            input_cor.value = ""
            input_tamanho.value = ""
            input_capacidade.value = ""
            navegar("/segunda_tela")

    # navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)

        )

    # gerenciar telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Cafeteira:",
                        bgcolor=Colors.PURPLE_600
                    ),
                    input_marca,
                    input_preco,
                    input_cor,
                    input_tamanho,
                    input_capacidade,
                    bnt_salvar


                ]
            )
        )

        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="CAFETEIRA",
                            bgcolor=Colors.PURPLE_600
                        ),
                        Container(
                            Column([
                                text_marca,
                                    Row([
                                        Icon(Icons.ATTACH_MONEY, color=Colors.BLACK, size=20),
                                        text_preco,
                                    ]),
                                    Row([
                                        Icon(Icons.COLOR_LENS, color=Colors.BLACK, size=20),
                                        text_cor,
                                    ]),
                                    Row([
                                        Icon(Icons.FORMAT_SIZE, color=Colors.BLACK, size=20),
                                        text_tamanho,

                                    ]),
                                    Row([
                                        Icon(Icons.STORAGE_ROUNDED, color=Colors.BLACK, size=20),
                                        text_capacidade,
                                    ]),
                                ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                ),
                                bgcolor=Colors.PURPLE_200,
                                padding=10,
                                border_radius=5,
                                width=400
                            )


                        ]

                    )
                )

    # COMPONENTES
    text_marca = Text(" ")
    text_preco = Text(" ")
    text_cor = Text(" ")
    text_tamanho = Text(" ")
    text_capacidade = Text(" ")
    input_marca = TextField(label="Digite a marca")
    input_preco = TextField(label="Digite o preço")
    input_cor = TextField(label="Digite seu cor")
    input_tamanho = TextField(label="Digite seu tamanho")
    input_capacidade = TextField(label="Digite seu capacidade")
    bnt_salvar = ElevatedButton("Salvar e Navegar", on_click=cafeteira, color=Colors.PURPLE_800)

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
