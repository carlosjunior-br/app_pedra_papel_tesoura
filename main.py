import flet as ft
import random
import time

def main(page: ft.Page):
    page.title = "Pedra, Papel, Tesoura"
    page.window_width = 375
    page.window_height = 667
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def mostrar_sobre(e):
        def fechar_dialogo(e):
            dlg_sobre.open = False
            page.update()
        
        dlg_sobre = ft.AlertDialog(
            title=ft.Text(
                "Sobre",
                text_align=ft.TextAlign.CENTER
                ),
            content=ft.Text(
                "Este é um aplicativo que simula o jogo pedra, papel, tesoura.\n\nDesenvolvido por Carlos Júnior.",
                text_align=ft.TextAlign.CENTER
                ),
            actions=[ft.TextButton("OK", on_click=fechar_dialogo)]
        )
        page.dialog = dlg_sobre
        dlg_sobre.open = True
        page.update()

    def jogar(e):
        progress_bar = ft.ProgressBar(value=0, width=300)
        def update_progress_bar(progress_bar):
            for i in range(4):
                progress_bar.value = i / 3
                progress_bar.page.update()
                time.sleep(1)
        dlg_aguarde = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            title=ft.Text("Jogo em andamento...", text_align=ft.TextAlign.CENTER),
            content=progress_bar,
            open=True,
            modal=True
        )
        page.dialog = dlg_aguarde
        page.update()
        update_progress_bar(progress_bar)
        
        dlg_aguarde.open = False
        page.update()
        
        executar_jogo()

    def executar_jogo():
        opcoes = ["pedra", "papel", "tesoura"]
        escolha_jogador = select_opcao.value
        escolha_maquina = random.choice(opcoes)

        jogador_image_path = f"/images/{escolha_jogador}.png"
        maquina_image_path = f"/images/{escolha_maquina}.png"
        
        img_jogador.src = jogador_image_path
        img_maquina.src = maquina_image_path

        if escolha_jogador == escolha_maquina:
            resultado.value = "Empate!"
        elif (escolha_jogador == "pedra" and escolha_maquina == "tesoura") or \
             (escolha_jogador == "papel" and escolha_maquina == "pedra") or \
             (escolha_jogador == "tesoura" and escolha_maquina == "papel"):
            resultado.value = "Você venceu!"
            placar["jogador"] += 1
        else:
            resultado.value = "Máquina venceu!"
            placar["maquina"] += 1

        placar_geral.value = f"Você {placar['jogador']} X {placar['maquina']} Máquina"
        page.update()

    header = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(ft.icons.INFO, on_click=mostrar_sobre),
                ft.Text(
                    "Pedra, Papel, Tesoura",
                    text_align=ft.TextAlign.CENTER,
                    theme_style = ft.TextThemeStyle.TITLE_LARGE,
                    color=ft.colors.BLUE_900
                ),
                ft.IconButton(ft.icons.INFO, on_click=mostrar_sobre)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        bgcolor=ft.colors.GREY_300
    )

    select_opcao = ft.Dropdown(
        label="Escolha sua jogada",
        options=[
            ft.dropdown.Option("pedra", text="Pedra"),
            ft.dropdown.Option("papel", text="Papel"),
            ft.dropdown.Option("tesoura", text="Tesoura")
        ],
        value="pedra"
    )

    btn_jogar = ft.ElevatedButton("Jogar", on_click=jogar)

    img_avatar_jogador = ft.Image(src=f"/images/jogador.png", width=120, height=120)
    img_avatar_maquina = ft.Image(src=f"/images/maquina.png", width=120, height=120)
    img_jogador = ft.Image(src=f"/images/placeholder.png", width=120, height=120)
    img_maquina = ft.Image(src=f"/images/placeholder.png", width=120, height=120)
    resultado = ft.Text(theme_style = ft.TextThemeStyle.TITLE_MEDIUM)
    placar = {"jogador": 0, "maquina": 0}
    placar_geral_titulo = ft.Text(
                            "Placar Geral",
                            theme_style = ft.TextThemeStyle.TITLE_LARGE,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.colors.BLUE_900
                        )
    placar_geral = ft.Text(
        "Você 0 X 0 Máquina",
        theme_style = ft.TextThemeStyle.TITLE_LARGE,
        color=ft.colors.BLUE_900
        )

    container_placar = ft.Container(
        content=ft.Column(
            [
                placar_geral_titulo,
                placar_geral
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=10,
        margin=10,
        border_radius=10,
        width=350,
        bgcolor=ft.colors.GREY_300
    )

    main_content = ft.Container(
        content=ft.Column(
            [
                header,
                select_opcao,
                btn_jogar,
                ft.Row(
                    [
                        ft.Text("Você",
                                text_align=ft.TextAlign.CENTER,
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM
                            ),
                        ft.Text("  ",
                                text_align=ft.TextAlign.CENTER,
                                theme_style=ft.TextThemeStyle.TITLE_LARGE
                            ),
                        ft.Text("Máquina",
                                text_align=ft.TextAlign.CENTER,
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM
                            )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                ft.Row(
                    [
                        img_avatar_jogador,
                        ft.Text("vs",
                                text_align=ft.TextAlign.CENTER,
                                theme_style=ft.TextThemeStyle.TITLE_LARGE
                            ),
                        img_avatar_maquina
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [
                        img_jogador,
                        ft.Text("  ",
                                text_align=ft.TextAlign.CENTER,
                                theme_style=ft.TextThemeStyle.TITLE_LARGE
                            ),
                        img_maquina
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                resultado,
                container_placar
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=375
    )

    page.add(main_content)

ft.app(target=main, assets_dir="assets")