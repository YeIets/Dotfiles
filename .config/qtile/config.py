# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import hook

from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()


########################
###  BAR VARIABLES   ###
########################

widgets_font = "Agave"
widgets_font_sze = 16
widgets_padding = 4

bar_color = "#191919"
bar_sze = 26

#GroupBox
active_color = '#F47340'
inactive_color = '#000000'
current_screen_color = '#F47340'
groupbox_bg = '#191919'
icon_sze = 18

#Clock
clock_bg = '#C6D57E'
clock_padding = 0
clock_fg = '#000000'

#CPU
cpu_bg = '#D57E7E'
cpu_fg = '#000000'

#MEMORY
memory_bg = '#E6B566'
memory_fg = '#000000'

#VOLUME
volume_bg = '#FFE1AF'
volume_fg = '#000000'

#QUICK EXIT 
exit_bg = '#CAB8FF'
exit_fg = '#000000'

#WINDOW COUNT
wcount_bg = '#E6B566'
wcount_fg = '#000000'

#WINDOW NAME
wname_bg = '#D77FA1'
wname_fg = '#000000'

##########################
####  MOUSE CALLBACKS  ###
##########################

def open_powermenu():
    qtile.cmd_spawn('zsh .local/bin/powermenu.sh')



###########################
####        KEYS        ###
###########################

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #Volume  Keys
    Key([mod], "F11", lazy.spawn("pulsemixer --change-volume +5 --max-volume 100")),
    Key([mod], "F10", lazy.spawn("pulsemixer --change-volume -5 --max-volume 100")),
    Key([mod], "F9", lazy.spawn("pulsemixer --toggle-mute")),

    #Launch Rofi
    Key([mod,"control","shift"], "Up", lazy.spawn("rofi -show drun")),
    Key([mod,"control","shift"], "Down", lazy.spawn("rofi -show run")),

    #RhythymBOX KEys
    Key([mod], "F7", lazy.spawn("playerctl play-pause")),
    Key([mod], "F6", lazy.spawn("playerctl next")),
    Key([mod], "F5", lazy.spawn("playerctl previous")),

    #Screenshot Keys (Flameshot)
    Key([mod], "F1", lazy.spawn("flameshot full")),
    Key([mod], "F2", lazy.spawn("flameshot gui")),


]

groups = [
            Group("a", label = "  "),
            Group("s", label = "  "),
            Group("d", label = "  "),
            Group("f", label = "  "),
            Group("y", label = "  "),
            Group("u", label = "  "),
            Group("i", label = "  "),
            Group("o", label = "  "),
            Group("p", label = "  "),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
    

layouts = [
    layout.Columns(
        border_focus='#F47340', 
        border_normal='#FFF0AA', 
        border_width=3,
        border_on_single='#F47340',
        margin= [7, 5, 7, 10],
    ),
    layout.Max(),
]

widget_defaults = dict(
    font = widgets_font,
    fontsize = widgets_font_sze,
    padding = widgets_padding,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox( 
                    fontsize = icon_sze,
                    active = active_color,
                    inactive = inactive_color,
                    disable_drag = True,
                    highlight_method = 'line',
                    use_mouse_wheel = False,
                    this_current_screen_border = current_screen_color,
                    this_screen_border = current_screen_color,
                    background = groupbox_bg,
                    highlight_color = [groupbox_bg, groupbox_bg],
                    margin_x = 0,
                    margin_y = 4,
                    ),

                widget.TextBox(
                    text = "",
                    fontsize = 74,
                    background = wcount_bg,
                    foreground = groupbox_bg,
                    padding = -11,
                    ),

                widget.WindowCount(
                    fontsize = 20,
                    show_zero = True,
                    background = wcount_bg,
                    foreground = wcount_fg,
                    ),

                widget.TextBox(
                    text = "",
                    fontsize = 74,
                    foreground = wcount_bg,
                    padding = -11,
                    ),

                widget.Spacer(
                    bar.STRETCH,
                    background = None,
                    ),

                widget.TextBox(
                    text = "",
                    fontsize = 51,
                    foreground = clock_bg,
                    background = bar_color,
                    padding = 0,
                    ),

                widget.Clock(
                    format = "  %a %d %b %Y - %H:%H",
                    background = clock_bg,
                    padding = clock_padding,
                    foreground = clock_fg,
                    ),

                widget.TextBox(
                    text = "",
                    fontsize = 51,
                    foreground = clock_bg,
                    background = bar_color,
                    padding = 0,
                    ),

                widget.Spacer(
                    bar.STRETCH,
                    background = None,
                    ),

                widget.TextBox(
                    text = "",
                    fontsize = 74,
                    foreground = memory_bg,
                    padding = -11,
                    ),

                widget.Memory(
                    fontsize = 16,
                    format = '兩 {MemUsed: .0f}{mm} /{MemTotal: .0f}{mm} ',
                    background = memory_bg,
                    foreground = memory_fg,
                    padding = 4,
                    ),

                    widget.TextBox(
                    text = "",
                    fontsize = 74,
                    foreground = cpu_bg,
                    background = memory_bg,
                    padding = -11,
                    ),

                widget.CPU(
                    fontsize = 16,
                    format = ' 礪 {load_percent}% ',
                    background = cpu_bg,
                    foreground = cpu_fg,
                    padding = 4,
                    ),

                widget.TextBox(
                    text = "",
                    fontsize = 74,
                    foreground = volume_bg,
                    background = cpu_bg,
                    padding = -11,
                    ),

                widget.Volume(
                    fmt = ' - {} ',
                    background = volume_bg,
                    foreground = volume_fg,
                    ),

                widget.TextBox(
                    text = "",
                    fontsize = 74,
                    foreground = exit_bg,
                    background = volume_bg,
                    padding = -11,
                    ),

                widget.TextBox(
                    text = '  ',
                    fontsize = 18,
                    background = exit_bg,
                    foreground = exit_fg,
                    mouse_callbacks = {'Button1': open_powermenu},
                    ),

            ],

            bar_sze, 
            background = bar_color,

        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
    