import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment
from flet.controls.border_radius import horizontal


def main(page: flet.Page):
    # Configurações
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def salvar_nome():
        text.value = f"Bom Dia {input_nome.value}+ {input_sobrenome.value}"
        page.update()

    def salvar():
        n1 = int(input_numero.value)
        if n1 % 2 == 0:
            text.value = f"O número {n1} é par"
            page.update()
        else:
            text.value = f"O número {n1} é impar"
            page.update()

    def nascimento():
        verif_idade = int(input_nascimento.value)
        idade = 2026 - verif_idade
        if idade >= 18:
            text.value = f"ele é maior de idade, a idade é {idade} anos"
            page.update()
        else:
            text.value = f"ele é menor de idade,  a idade é {idade} anos"
            page.update()



    #Componentes
    text = Text(" ")
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    input_numero = TextField(label="Digite um número")
    input_nascimento = TextField(label="Digite o ano de nascimento")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_salvar_dois = OutlinedButton("Salvar", on_click=salvar)
    btn_salvar_tres = OutlinedButton("Salvar", on_click=nascimento)

    # Contrução da tela
    page.add(
        Column(
            [
                input_nome,
                input_sobrenome,
                btn_salvar,
                input_numero,
                btn_salvar_dois,
                input_nascimento,
                btn_salvar_tres,
                text
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )



    )


flet.app(main)
