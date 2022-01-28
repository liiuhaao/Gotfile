import subprocess

import my_widgets
from gruvbox import *
from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

keys = [
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "comma", lazy.next_screen()),
    Key([mod], "period", lazy.prev_screen()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    Key([mod, "control"], "space", lazy.window.toggle_fullscreen()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "b", lazy.hide_show_bar("top")),
    Key([mod], "space", lazy.spawn("rofi -show run -font 'SourceCodePro 15'")),
    Key([mod], "q", lazy.window.kill()),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("/home/liuhao/Scripts/light_up.sh")),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("/home/liuhao/Scripts/light_down.sh")),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("/home/liuhao/Scripts/volume_up.sh")),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("/home/liuhao/Scripts/volume_down.sh")),
    Key([], "XF86AudioMute",
        lazy.spawn("/home/liuhao/Scripts/volume_mute.sh")),
    Key([], "Print", lazy.spawn("flameshot gui")),

    # Tile
    Key([mod], "j", lazy.group.next_window()),
    Key([mod], "k", lazy.group.prev_window()),
    Key([mod], "h", lazy.layout.decrease_ratio()),
    Key([mod], "l", lazy.layout.increase_ratio()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod], "i", lazy.layout.increase_nmaster()),
    Key([mod], "d", lazy.layout.decrease_nmaster()),

    # # Bsp
    # Key([mod], "n", lazy.group.next_window()),
    # Key([mod], "p", lazy.group.prev_window()),
    # Key([mod], "j", lazy.layout.down()),
    # Key([mod], "k", lazy.layout.up()),
    # Key([mod], "h", lazy.layout.left()),
    # Key([mod], "l", lazy.layout.right()),
    # Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    # Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    # Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    # Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    # Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    # Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    # Key([mod, "control"], "j", lazy.layout.grow_down()),
    # Key([mod, "control"], "k", lazy.layout.grow_up()),
    # Key([mod, "control"], "h", lazy.layout.grow_left()),
    # Key([mod, "control"], "l", lazy.layout.grow_right()),
    # Key([mod, "shift"], "n", lazy.layout.normalize()),
    # Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
]

groups = [Group(i) for i in "123456789"]

for number, i in enumerate(groups):
    keys.append(
        Key([mod], str(number + 1), lazy.group[i.name].toscreen(toggle=False)))
    keys.append(
        Key([mod, "shift"], str(number + 1), lazy.window.togroup(i.name)))

layouts = [
    layout.Tile(
        ratio=0.50,
        border_normal=bg0_hard,
        border_focus=dark_gray,
        border_width=2,
        shift_windows=False,
        margin=10,
        border_on_single=False,
    ),
    # layout.Bsp(
    #     border_normal=bg0_hard,
    #     border_focus=dark_gray,
    #     border_width=2,
    #     ratio=1.6,
    #     margin=10,
    #     fair=False,
    # ),
    layout.Max(),
]

widget_defaults = dict(
    font="SauceCodePro Nerd Font",
    fontsize=20,
    padding=0,
)


# Run the autostart.sh script on startup
@hook.subscribe.startup_once
def startup():
    subprocess.call("~/Scripts/autostart.sh")


def get_top_bar():
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
                    "Button4":
                    lambda: qtile.cmd_spawn("/home/liuhao/Scripts/volume_up.sh"
                                            ),
                    "Button5":
                    lambda: qtile.cmd_spawn(
                        "/home/liuhao/Scripts/volume_down.sh"),
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
                    lambda: qtile.cmd_spawn("/home/liuhao/Scripts/light_up.sh"
                                            ),
                    "Button5":
                    lambda: qtile.cmd_spawn(
                        "/home/liuhao/Scripts/light_down.sh"),
                },
            ),
            my_widgets.Clock(
                background=bg0,
                foreground=fg2,
                format="  %m/%d %A  %H:%M:%S ",
                mouse_callbacks={
                    "Button1":
                    lambda: qtile.cmd_spawn("/home/liuhao/Scripts/date.sh"),
                },
            ),
            widget.Systray(
                background=bg0,
                foreground=fg2,
            ),
        ],
        30,
        # margin=[5, 5, 0, 5],
    )


screens = [
    Screen(
        wallpaper=
        "/home/liuhao/Pictures/Wallpapers/Nighthawks_by_Edward_Hopper_1942.jpg",
        wallpaper_mode="fill",
        top=get_top_bar(),
    ),
    Screen(
        wallpaper=
        "/home/liuhao/Pictures/Wallpapers/Nighthawks_by_Edward_Hopper_1942.jpg",
        wallpaper_mode="fill",
        top=get_top_bar(),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click(
        [mod],
        "Button2",
        lazy.window.bring_to_front(),
    ),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="PHONE"),  # scrcpy
    ],
    border_normal=bg0_hard,
    border_focus=dark_gray,
    border_width=4,
)

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = False
bring_front_click = True
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "qtile"
