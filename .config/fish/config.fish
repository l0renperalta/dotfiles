if status is-interactive
    # Commands to run in interactive sessions can go here

    set fish_greeting

    starship init fish | source

    alias ls='lsd'
    alias cat='bat'
    set -x PATH /home/loren/.local/share/bob/nvim-bin $PATH

end


