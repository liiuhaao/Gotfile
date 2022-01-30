from gruvbox import bg0_hard, dark_gray
from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.Tile(
        ratio=0.50,
        border_normal=bg0_hard,
        border_focus=dark_gray,
        border_width=2,
        shift_windows=False,
        margin=5,
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

floating_layout = layout.Floating(
    float_rules=[
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
