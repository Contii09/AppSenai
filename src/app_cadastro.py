import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, TextField, Text, ElevatedButton
from flet.controls import page


def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700



    def cadastro():
        text1.value = f"""
        Nome: {input_nome.value}
        CPF: {input_cpf.value}
        Email: {input_email.value}
        Salário: {input_salario.value}"""

        tem_erro = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = "Campo obrigatorio"

        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Campo obrigatorio"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "Campo obrigatorio"

        if not (tem_erro):
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
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
                        title="Cadastro:",
                        bgcolor=Colors.PURPLE_600
                    ),
                    input_nome,
                    input_cpf,
                    input_email,
                    input_salario,
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
                            title="Segunda Página",
                            bgcolor=Colors.PURPLE_600
                        ),
                        text1
                    ]

                )
            )
    # COMPONENTES
    text1 = Text()
    input_nome = TextField(label="Digite seu nome")
    input_cpf = TextField(label="Digite seu cpf")
    input_email = TextField(label="Digite seu email")
    input_salario = TextField(label="Digite seu salario")
    bnt_salvar = ElevatedButton("Salvar e Navegar", on_click=cadastro, color=Colors.PURPLE_800)

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
