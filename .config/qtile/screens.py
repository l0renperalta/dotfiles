from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.utils import guess_terminal
from libqtile import qtile

terminal = guess_terminal()

colors = [
    ["#2e3440", "#2e3440"],  # 0 background
    ["#d8dee9", "#d8dee9"],  # 1 foreground
    ["#3b4252", "#3b4252"],  # 2 background lighter
    ["#bf616a", "#bf616a"],  # 3 red
    ["#a3be8c", "#a3be8c"],  # 4 green
    ["#ebcb8b", "#ebcb8b"],  # 5 yellow
    ["#81a1c1", "#81a1c1"],  # 6 blue
    ["#b48ead", "#b48ead"],  # 7 magenta
    ["#88c0d0", "#88c0d0"],  # 8 cyan
    ["#e5e9f0", "#e5e9f0"],  # 9 white
    ["#4c566a", "#4c566a"],  # 10 grey
    ["#d08770", "#d08770"],  # 11 orange
    ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
    ["#5e81ac", "#5e81ac"],  # 13 super blue
    ["#242831", "#242831"],  # 14 super dark background
]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='text',
                    active='#ffffff',
                    inactive='#404040',
                    this_current_screen_border='#2ac3de',
                    # this_current_screen_border='#00FF00',
                ),
                widget.WindowName(
                    max_chars=60,
                    foreground='#ffffff',
                ),
                widget.Systray(),
                widget.TextBox(
                text=' ', 
                background="#51afef", 
                foreground="#282c34", 
                fontsize=16, 
                font="JetBrainsMonoNL Nerd Font Regular"
                ),
                widget.Memory(
                measure_mem='G', 
                background="#51afef", 
                foreground="#282c34", 
                format = '{MemUsed:.1f}G/{MemTotal:.1f}G ',
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}, 
                ),
                widget.TextBox(text='', 
                background="#ff6c6b", 
                foreground="#282c34", 
                fontsize=16, 
                font="JetBrainsMonoNL Nerd Font Regular", 
                padding=7
                ),
                widget.KeyboardLayout(
                background="#ff6c6b", 
                foreground="#282c34", 
                configured_keyboards=['us', 'rs alternatequotes'], 
                display_map={'us': ' US ', 'rs alternatequotes': 'СР'}, 
                ),
                 widget.TextBox(
                text='  ', 
                background="#e7d15f", 
                foreground="#282c34", 
                fontsize=16, 
                font="JetBrainsMonoNL Nerd Font Regular"
                ),
                widget.CheckUpdates(
                background="#e7d15f", 
                foreground="#282c34", 
                display_format="{updates} Updates ", 
                no_update_string='0 Updates', 
                custom_command='(checkupdates ; yay -Qua) | cat', 
                update_interval=300, 
                colour_have_updates="#282c34", 
                colour_no_updates="#282c34", 
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay -Syyyu')},
                ),
                widget.TextBox(
                text='  ', 
                background="#98be65", 
                foreground="#282c34", 
                fontsize=16, 
                font="JetBrainsMonoNL Nerd Font Regular"
                ),
                widget.Clock(
                format="%d/%m/%Y ", 
                background="#98be65", 
                foreground="#282c34", 
                ),
                widget.TextBox(
                text='  ', 
                background="#da8548", 
                foreground="#282c34", 
                fontsize=16, 
                font="JetBrainsMonoNL Nerd Font Regular"
                ),
                widget.Clock(
                format="%a %H:%M ", 
                background="#da8548", 
                foreground="#282c34", 
                ),
            ],
            22,
            background="#000000",
            opacity=0.9,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

