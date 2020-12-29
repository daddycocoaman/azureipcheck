from click_help_colors import HelpColorsCommand, HelpColorsGroup


class CustomHelpColorsGroup(HelpColorsGroup):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.help_headers_color = "blue"
        self.help_options_color = "yellow"


class CustomHelpColorsCommand(HelpColorsCommand):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.help_headers_color = "blue"
        self.help_options_color = "yellow"