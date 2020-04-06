def fontStyle(customfont, font):
    customfont.config(family=font)
    return customfont


def fontSize(customfont, fsize):
    customfont.config(size=fsize)
    return customfont


def fontColor(label, fcolor):
    label.config(fg=fcolor)
    return label
