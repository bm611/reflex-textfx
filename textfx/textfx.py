import reflex as rx


class State(rx.State):
    color: str = ""

    bg_grid = {
        "Simile": "#DAEF68",
        "Explode": "#C0BAF2",
        "Unexpect": "#73D29E",
        "Chain": "#BAA694",
        "POV": "#FF8C67",
        "Alliteration": "#81C2EC",
        "Acronym": "#FA9CC6",
        "Fuse": "#FFCE00",
        "Scene": "#8F9BFF",
        "Unfold": "#91FAED",
    }

    opts = list(bg_grid.keys())

    def set_clicked_card(self, card_text: str):
        self.color = self.bg_grid[card_text]


@rx.page(route="/", title="Home")
def main() -> rx.Component:
    return rx.center(
        rx.grid(
            rx.foreach(
                State.opts,
                lambda i: rx.card(
                    f"{i}",
                    height="11vh",
                    class_name="border-1 hover:border-2 hover:border-black",
                    on_click=lambda: State.set_clicked_card(i),
                    bg=State.color,
                ),
            ),
            columns="10",
            spacing="3",
            width="80%",
        ),
        class_name="p-20",
    )


app = rx.App()
