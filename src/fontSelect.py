def font_style(custom_font, font):
    custom_font.config(family=font)
    return custom_font


def font_size(custom_font, fsize):
    custom_font.config(size=fsize)
    return custom_font


def font_color(label, fcolor):
    label.config(fg=fcolor)
    return label
