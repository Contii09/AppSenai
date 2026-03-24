import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    Alignment
from flet.controls.border_radius import horizontal
from datetime import datetime


def main(page: flet.Page):
    #CONFIGURAÇÕES
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    #FUNÇÕES
    def nome():
        text.value = f"Bom Dia {input_nome.value} {input_sobrenome.value}"
        page.update()

    def numero():
        n1 = int(input_numero.value)
        if n1 % 2 == 0:
            text_numero.value = f"O número {n1} é par"
            page.update()
        else:
            text.value = f"O número {n1} é impar"
            page.update()


    def nascimento():
        verif_idade = int(input_nascimento.value)
        idade = datetime.now().year - verif_idade
        if idade >= 18:
            text_nascimento.value = f"É maior de idade, a idade é {idade} anos"
            page.update()
        else:
            text_nascimento.value = f"É menor de idade,  a idade é {idade} anos"
            page.update()



    #COMPONENTES
    text = Text(" ")
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=nome)

    text_numero = Text(" ")
    input_numero = TextField(label="Digite um número", hint_text="Verifique se é par ou ímpar")
    btn_salvar_dois = OutlinedButton("Verificar", on_click=numero)

    text_nascimento = Text(" ")
    input_nascimento = TextField(label="Digite o ano de nascimento", hint_text="Ex: 2009")
    btn_salvar_tres = OutlinedButton("Salvar", on_click=nascimento)



    #CONSTRUÇÃO DA TELA
    page.add(
        Column(
            [
                Container(
                    Column(
                        [
                            Text("Atividade 1", weight=FontWeight.BOLD, size=18),
                            text,
                            input_nome,
                            input_sobrenome,
                            btn_salvar,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.PURPLE_800,
                    padding=10,
                    border_radius=5,
                    width=400
                ),

                Container(
                    Column(
                        [
                            Text("Atividade 2", weight=FontWeight.BOLD, size=18),
                            text_numero,
                            input_numero,
                            btn_salvar_dois,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.PURPLE_600,
                    padding=10,
                    border_radius=5,
                    width=400
                ),

                Container(
                    Column(
                        [
                            Text("Atividade 3", weight=FontWeight.BOLD, size=18),
                            text_nascimento,
                            input_nascimento,
                            btn_salvar_tres
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.PURPLE_400,
                    padding=10,
                    border_radius=5,
                    width=400
                ),





            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )


flet.run(main)
