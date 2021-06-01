from pyengine.main_window.components.text_compnent import TextComponent


class LabelComponent(TextComponent):
    def __init__(self, parent, component):
        super().__init__(parent, component)
        self.name.setText("Label")
