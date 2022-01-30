import os

import my_widgets
from gruvbox import bg0, bg2, bright_red, dark_blue, fg2
from keys import mod, terminal
from libqtile import bar, qtile, widget
from libqtile.config import Screen

home = os.path.expanduser('~')

widget_defaults = dict(
    font="SauceCodePro Nerd Font",
    fontsize=20,
    padding=0,
)


def get_top_bar(margin):
    return bar.Bar(
        [
            widget.TextBox(
                background=bg0,
                foreground=dark_blue,
                text=" ",
                mouse_callbacks={
                    "Button1":
                    lambda: qtile.cmd_simulate_keypress([mod], "space"),
                    "Button3": lambda: qtile.cmd_spawn(terminal),
                },
            ),
            widget.GroupBox(
                background=bg0,
                active=fg2,
                highlight_method="block",
                hide_unused=False,
                this_current_screen_border=bg2,
                markup_focused=False,
            ),
            widget.WindowCount(
                background=bg0,
                foreground=fg2,
                text_format="[{num}]",
                mouse_callbacks={
                    "Button2": lambda: qtile.cmd_simulate_keypress([mod], "q"),
                    "Button3": lambda: qtile.cmd_next_layout(),
                    "Button4": lambda: qtile.cmd_simulate_keypress([mod], "k"),
                    "Button5": lambda: qtile.cmd_simulate_keypress([mod], "j"),
                },
            ),
            widget.WindowName(
                background=bg0,
                foreground=fg2,
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
                background=bg0,
                foreground=fg2,
                fmt="{}",
                volume_down_command="volume_down.sh",
                volume_up_command="volume_up.sh",
                mouse_callbacks={
                    "Button1":
                    lambda: qtile.cmd_spawn(home +
                                            "/.local/bin/volume.sh toggle"),
                    "Button4":
                    lambda: qtile.cmd_spawn(home + "/.local/bin/volume.sh up"),
                    "Button5":
                    lambda: qtile.cmd_spawn(home + "/.local/bin/volume.sh down"
                                            ),
                },
            ),
            my_widgets.Battery(
                background=bg0,
                foreground=fg2,
                low_forward=bright_red,
                charge_char="",
                unknown_char="",
                discharge_char="",
                full_char="",
                empty_char="",
                format="  {char} {percent:1.0%} ",
                show_short_text=False,
                update_interval=1,
                mouse_callbacks={
                    "Button4":
                    lambda: qtile.cmd_spawn(home +
                                            "/.local/bin/brightness.sh up"),
                    "Button5":
                    lambda: qtile.cmd_spawn(home +
                                            "/.local/bin/brightness.sh down"),
                },
            ),
            my_widgets.Clock(
                background=bg0,
                foreground=fg2,
                format="  %m/%d %A  %H:%M:%S ",
                mouse_callbacks={
                    "Button1":
                    lambda: qtile.cmd_spawn(home + "/.local/bin/date.sh curr"),
                    "Button4":
                    lambda: qtile.cmd_spawn(home + "/.local/bin/date.sh prev"),
                    "Button5":
                    lambda: qtile.cmd_spawn(home + "/.local/bin/date.sh next"),
                },
            ),
            widget.Systray(
                background=bg0,
                foreground=fg2,
            ),
        ],
        30,
        margin=[margin, margin, margin, margin],
    )


screens = [
    Screen(
        wallpaper=
        "/home/liuhao/Pictures/Wallpapers/Nighthawks_by_Edward_Hopper_1942.jpg",
        wallpaper_mode="fill",
        top=get_top_bar(0),
    ) for _ in range(2)
]
