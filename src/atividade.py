import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Icon, Text, Card, \
    Column, Container, Row, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, CrossAxisAlignment


class Perfil:
    def __init__(self, marca, preco, cor, tamanho, capacidade):
        self.marca = marca
        self.preco = preco
        self.cor = cor
        self.tamanho = tamanho
        self.capacidade = capacidade


def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo Cafeteira"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # FUNÇÕES
    # navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    def icone_tamanho(p1):
        if p1 == "Grande":
            return Icon(Icons.COFFEE_MAKER, color=Colors.BLUE_400)
        elif p1 == "Média":
            return Icon(Icons.COFFEE_OUTLINED, color=Colors.BLUE_400)
        elif p1 == "Pequena":
            return Icon(Icons.COFFEE, color=Colors.BLUE_400)


    def montar_lista_padrao():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=icone_tamanho(item.tamanho),
                    title=item.marca,
                    subtitle=item.preco,
                    trailing=PopupMenuButton(
                        icon=Icon(Icons.MORE_VERT, color=Colors.BLUE_400),
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icon(Icons.REMOVE_RED_EYE, color=Colors.BLUE_400,), on_click=lambda _, cafeteira=item:ver_detalhes(cafeteira)),
                            PopupMenuItem("Excluir", icon=Icon(Icons.DELETE, color=Colors.BLUE_400),
                                          on_click=lambda: excluir(item)),
                        ]
                    ),
                )
            )


    def ver_detalhes(cafeteira):
        text_marca.value = cafeteira.marca
        text_preco.value = cafeteira.preco
        text_cor.value = cafeteira.cor
        text_tamanho.value = cafeteira.tamanho
        text_capacidade.value = cafeteira.capacidade

        navegar("/detalhes")




    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        marca = input_marca.value
        preco = input_preco.value
        cor = input_cor.value
        tamanho = input_tamanho.value
        capacidade = input_capacidade.value

        tem_erro = False
        if marca:
            input_marca.error = None
        else:
            input_marca.error = "Campo Obrigatório"
            tem_erro = True

        if preco:
            input_preco.error = None
        else:
            input_preco.error = "Campo Obrigatório"
            tem_erro = True

        if cor:
            input_cor.error = None
        else:
            input_cor.error = "Campo Obrigatório"
            tem_erro = True

        if tamanho:
            input_tamanho.error = None
        else:
            input_tamanho.error = "Campo Obrigatório"
            tem_erro = True

        if capacidade:
            input_capacidade.error = None
        else:
            input_capacidade.error = "Campo Obrigatório"
            tem_erro = True

        if not tem_erro:
            p1 = Perfil(marca=marca.strip(), preco=preco.strip(), cor=cor.strip(), tamanho=tamanho.strip(), capacidade=capacidade.strip())
            lista_dados.append(p1)
        navegar("/lista_padrao")

        montar_lista_padrao()




    # gerenciar telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/lista_padrao",
                controls=[
                    flet.AppBar(
                        title="Cafeteiras",
                        bgcolor=Colors.BLUE_900

                    ),
                    list_view

                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )



        if page.route == "/form_cadastro":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                            bgcolor=Colors.BLUE_900

                        ),
                        input_marca,
                        input_preco,
                        input_cor,
                        input_tamanho,
                        input_capacidade,
                        btn_salvar,

                    ]
                )
            )


        elif page.route == "/detalhes":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                            bgcolor=Colors.BLUE_900

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
                            bgcolor=Colors.BLUE_900,
                            padding=10,
                            border_radius=5,
                            width=400
                        )

                    ]
                )
            )





    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # COMPONENTES

    text_marca = Text()
    text_preco = Text()
    text_cor = Text()
    text_tamanho = Text()
    text_capacidade = Text()

    input_marca = TextField(label="Digite a marca")
    input_preco = TextField(label="Digite o preço")
    input_cor = TextField(label="Digite a cor")
    input_tamanho = Dropdown(
        label="Tamanho",
        editable=True,
        options=[
            DropdownOption("Grande"),
            DropdownOption("Média"),
            DropdownOption("Pequena"),
        ],
    )
    input_capacidade = TextField(label="Digite seu capacidade")
    btn_salvar = Button("Salvar", width=400, on_click=lambda:salvar_dados() , color=Colors.BLUE_800)
    list_view = ListView(height=500)

    # EVENTOS
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
