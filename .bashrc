# ~/.bashrc: executed by bash(1) for non-login shells.

# Note: PS1 and umask are already set in /etc/profile. You should not
# need this unless you want different defaults for root.
# PS1='${debian_chroot:+($debian_chroot)}\h:\w\$ '
# umask 022

# You may uncomment the following lines if you want `ls' to be colorized:
export LS_OPTIONS='--color=auto'
# eval "`dircolors`"
alias ls='ls $LS_OPTIONS'
# alias ll='ls $LS_OPTIONS -l'
# alias l='ls $LS_OPTIONS -lA'
#
# Some more alias to avoid making mistakes:
# alias rm='rm -i'
# alias cp='cp -i'
# alias mv='mv -i'

PS1_COLOR_BEGIN="\[\033[1;32m\]"
PS1_COLOR_END="\[\e[m\]"
PS1_HOST_NAME="eaglepro"
export PS1="${PS1_COLOR_BEGIN}[<<${PS1_HOST_NAME}>> \${PWD}:]${PS1_COLOR_END}\\$"
export LS_COLORS="di=01;32"
