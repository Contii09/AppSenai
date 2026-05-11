import asyncio

import flet
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, TextOverflow, Card, Row, \
    Icon

from src.api_endpoints import get_planetas, get_personagens


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de API"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    def genero(gender):
        if gender == "Male":
            return "#e0eff1"
        elif gender == "Female":
            return "#fbd9ee"



    def montar_lista_personagens():
        print("Fazer")
        list_view.controls.clear()
        lista_dados = get_personagens()

        for item in lista_dados["items"]:
            list_view.controls.append(
                Card(
                    bgcolor=genero(item["gender"]),
                    content=Row(
                        margin=flet.Margin.all(8),
                        controls = [
                            Image(src=item["image"], width=90, height=90),
                            Column([
                            Text(item["name"], weight=FontWeight.BOLD, color=Colors.BLACK_87),
                            Text(f"Ki: {item['ki']}", color=Colors.BLACK_87),
                            Text(f"MaxKi: {item['maxKi']}", color=Colors.BLACK_87),
                            Text(f"Race: {item['race']}", color=Colors.BLACK_87),
                            Text(f"Gender: {item['gender']}", color=Colors.BLACK_87),

                        ])
                    ])
                )
            )



        # TODO: Montar a lista de personagens do seu jeito, capricha ein


    def montar_lista_planetas():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_planetas()

        # item é um apelido para o objeto que esta vindo da api
        for item in lista_dados["items"]:
            list_view.controls.append(
                ListTile(
                    leading=Image(src=item["image"], width=70),
                    title=Text(item["name"], weight=FontWeight.BOLD, color=Colors.AMBER_800),
                    subtitle=Text(item["description"], max_lines=3, overflow=TextOverflow.ELLIPSIS, color=Colors.BLACK_87),
                )
            )

    def define_lista(e):
        # Muda a lista de acordo com o indice do NavigationBar
        return montar_lista_planetas() if e.data == 1 else montar_lista_personagens()

    # Gerenciar as telas(routes)
    def route_change():

        #Carrega a primeira lista
        montar_lista_personagens()

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Dragon Ball Z", weight=FontWeight.BOLD),
                        bgcolor=Colors.ORANGE
                    ),
                    Column([
                        pagelet,
                    ])
                ],
                padding=0
            )
        )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes

    list_view = ListView(height=500)


    pagelet = Pagelet(
        navigation_bar=NavigationBar(
            destinations=[
                NavigationBarDestination(icon=Icons.MAN, label="Personagens"),
                NavigationBarDestination(icon=Icons.BLUR_ON, label="Planetas"),
            ],
            on_change=define_lista,
        ),
        content=Column([
            list_view,
        ],
            scroll=ScrollMode.HIDDEN,
            height=500
        ),
        height=600,
    )

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
