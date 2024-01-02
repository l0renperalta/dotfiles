from libqtile.config import Key, Group
from libqtile.command import lazy
from keys import mod, keys

groups = [
    Group("1", label="一", layout='monadtall'),
    Group("2", label="二", layout='monadtall'),
    Group("3", label="三", layout='monadtall'),
    Group("4", label="四", layout='monadtall'),
    Group("5", label="五", layout='monadtall'),
    Group("6", label="六", layout='monadtall'),
    Group("7", label="七", layout='monadtall'),
    Group("8", label="八", layout='monadtall'),
    Group("9", label="九", layout='monadtall'),
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