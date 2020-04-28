def font_style(
        custom_font, font):
    """
    Changes font family
    :param custom_font: font used by Message in Tkinter GUI
    :param font: font the user selects
    :return: font used by GUI
    """
    custom_font.config(family=font)
    return custom_font


def font_size(
        custom_font, f_size):
    """
    Changes font size
    :param custom_font: font used by Message in Tkinter GUI
    :param f_size: font size the user selects
    :return: font used by GUI
    """
    custom_font.config(size=f_size)
    return custom_font


def font_color(
        label, f_color):
    """
    Changes font color in Message object attached to GUI
    :param label: font used by Message in Tkinter GUI
    :param f_color: font color the user selects
    :return: label with new font color
    """
    label.config(fg=f_color)
    return label
