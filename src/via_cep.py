import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, TextField, Text, ElevatedButton, FontWeight
from flet.controls import page
from endpoints_cep import get_enderecos


def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700



    def cadastro():
        cep = input_cep.value
        Numero= input_numero.value

        tem_erro = False
        if input_cep.value:
            input_cep.error = None
        else:
            tem_erro = True
            input_cep.error = "Campo obrigatorio"

        if input_numero.value:
            input_numero.error = None
        else:
            tem_erro = True
            input_numero.error = "Campo obrigatorio"


        if not tem_erro:
            endereco = get_enderecos(cep)
            text_cidade.value = endereco["localidade"]
            text_uf.value = endereco["uf"]
            text_logradouro.value = endereco["logradouro"]
            text_bairro.value = endereco["bairro"]


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
                        title="Cadastro:",
                        bgcolor=Colors.PURPLE_600
                    ),
                    input_cep,
                    input_numero,
                    text_cidade,
                    text_uf,
                    text_logradouro,
                    text_bairro,
                    bnt_salvar

                ]
            )
        )


    # COMPONENTES
    text_cidade = TextField(label="Cidade:", disabled= True, color= Colors.WHITE_70)
    text_uf = TextField(label="Uf:", disabled= True, color= Colors.WHITE_70)
    text_logradouro = TextField(label="Rua:", disabled= True, color= Colors.WHITE_70)
    text_bairro = TextField(label="Bairro:", disabled= True, color= Colors.WHITE_70)

    input_cep = TextField(label="Digite seu Cep", on_submit=cadastro)
    input_numero = TextField(label="Digite o numero da Casa", on_submit=cadastro)

    bnt_salvar = ElevatedButton("Salvar", on_click=lambda: cadastro(), color=Colors.PURPLE_800)

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
