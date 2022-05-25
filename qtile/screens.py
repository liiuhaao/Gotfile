import my_widgets
from gruvbox import color
from keys import mod, terminal
from libqtile import bar, qtile, widget
from libqtile.config import Screen

widget_defaults = dict(
    font="SauceCodePro Nerd Font",
    fontsize=20,
    padding=0,
)


def get_top_bar():
    return bar.Bar(
        [
            widget.TextBox(
                background=color.bg0,
                foreground=color.dark_blue,
                text=" ",
                mouse_callbacks={
                    "Button1":
                    lambda: qtile.cmd_simulate_keypress([mod], "space"),
                    "Button3": lambda: qtile.cmd_spawn(terminal),
                },
            ),
            widget.GroupBox(
                background=color.bg0,
                active=color.fg2,
                highlight_method="block",
                hide_unused=False,
                this_current_screen_border=color.bg2,
                markup_focused=False,
            ),
            widget.WindowCount(
                background=color.bg0,
                foreground=color.fg2,
                text_format="[{num}]",
                mouse_callbacks={
                    "Button2": lambda: qtile.cmd_simulate_keypress([mod], "q"),
                    "Button3": lambda: qtile.cmd_next_layout(),
                    "Button4": lambda: qtile.cmd_simulate_keypress([mod], "k"),
                    "Button5": lambda: qtile.cmd_simulate_keypress([mod], "j"),
                },
            ),
            widget.WindowName(
                background=color.bg0,
                foreground=color.fg2,
                margin=0,
                format=" {state}{name}",
                mouse_callbacks={
                    "Button2": lambda: qtile.cmd_simulate_keypress([mod], "q"),
                    "Button3": lambda: qtile.cmd_next_layout(),
                    "Button4": lambda: qtile.cmd_simulate_keypress([mod], "k"),
                    "Button5": lambda: qtile.cmd_simulate_keypress([mod], "j"),
                },
            ),
            my_widgets.Volume(
                background=color.bg0,
                foreground=color.fg2,
                fmt="{}",
                volume_down_command="volume_down.sh",
                volume_up_command="volume_up.sh",
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn("volume.sh toggle"),
                    "Button4": lambda: qtile.cmd_spawn("volume.sh up"),
                    "Button5": lambda: qtile.cmd_spawn("volume.sh down"),
                },
            ),
            my_widgets.Battery(
                background=color.bg0,
                foreground=color.fg2,
                low_forward=color.bright_red,
                charge_char="",
                unknown_char="",
                discharge_char="",
                full_char="",
                empty_char="",
                format="  {char} {percent:1.0%} ",
                show_short_text=False,
                update_interval=1,
                mouse_callbacks={
                    "Button4": lambda: qtile.cmd_spawn("brightness.sh up"),
                    "Button5": lambda: qtile.cmd_spawn("brightness.sh down"),
                },
            ),
            widget.Clock(
                background=color.bg0,
                foreground=color.fg2,
                format="  %m/%d ",
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn("date.sh curr"),
                    "Button4": lambda: qtile.cmd_spawn("date.sh prev"),
                    "Button5": lambda: qtile.cmd_spawn("date.sh next"),
                },
            ),
            my_widgets.AnalogueClock(
                background=color.bg0,
                foreground=color.fg2,
                face_border_colour=color.fg2,
                # face_shape="square",
                # face_shape="circle",
            ),
            widget.Clock(
                background=color.bg0,
                foreground=color.fg2,
                format="%H:%M:%S ",
            ),
            widget.Systray(
                background=color.bg0,
                foreground=color.fg2,
            ),
        ],
        30,
    )


screens = [
    Screen(
        wallpaper=
        "/home/liuhao/Pictures/Wallpapers/Nighthawks_by_Edward_Hopper_1942.jpg",
        wallpaper_mode="fill",
        top=get_top_bar(),
    ) for _ in range(2)
]
