import reflex as rx


class State(rx.State):
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
    bg_color: str = "#FFFFFF"  # Default background color

    def set_bg_color(self, color: str):
        self.bg_color = color


def create_interactive_box(txt, background_color, icon):
    """Creates an interactive box with specified background color and click handler."""
    return rx.box(
        rx.text(
            txt,
            rx.icon(icon),
            align="center",
            class_name="text-sm font-bold flex flex-col items-center mt-8 gap-2",
            h="100%",
        ),
        on_click=lambda: State.set_bg_color(background_color),
        # background_color=background_color,
        cursor="pointer",
        height="7rem",
        _hover={"transform": "scale(1.05)", "border": "3px solid black"},
        border_radius="0.5rem",
        # box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        transition_property="transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        transition_duration="300ms",
        # class_name="border-2 border-black hover:border-2 hover:border-black",
        border="1px solid #000000",  # Light gray border
        # _hover={"border": "2px solid black"}
    )


@rx.page(route="/", title="Home")
def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.vstack(
                create_interactive_box("Simile", "#DAEF68", "activity"),
                create_interactive_box("Explode", "#C0BAF2", "alert-circle"),
                create_interactive_box("Unexpect", "#73D29E", "alert-triangle"),
                create_interactive_box("Chain", "#BAA694", "link"),
                create_interactive_box("POV", "#FF8C67", "eye"),
                create_interactive_box("Consonance", "#81C2EC", "align-center"),
                create_interactive_box("Acronym", "#FA9CC6", "award"),
                create_interactive_box("Fuse", "#FFCE00", "aperture"),
                create_interactive_box("Scene", "#8F9BFF", "airplay"),
                create_interactive_box("Unfold", "#91FAED", "chevron-down"),
                gap="0.5rem",
                display="grid",
                grid_template_columns="repeat(10, minmax(0, 1fr))",
                # max_width="48rem",
                width="80%",
            ),
            width="100%",
            align_items="center",
            # padding_top="2rem",  # Add some padding to the top
        ),
        background_color=State.bg_color,
        min_height="100vh",
        class_name="p-20",
    )


style = {
    "font_family": "MonaspaceArgon",
    "font_size": "16px",
}

app = rx.App(
    style=style,
    stylesheets=[
        "/fonts/font.css",
    ],
)
