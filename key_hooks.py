import keyboard

ctrl_pressed = False  # 用于记录Ctrl键状态


def on_ctrl_s(e):
    global ctrl_pressed

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'ctrl':
            ctrl_pressed = True
        elif ctrl_pressed and e.name == 's':
            keyboard.write('_')

    elif e.event_type == keyboard.KEY_UP:
        if e.name == 'ctrl':
            ctrl_pressed = False
