set nu
syntax on
set shiftwidth=3
set ts=3
set autoindent
colorscheme film_noir
source ~/vimscript/htmltemp.vim
noremap ~ :<C-u>call append(expand('.'), '')<Cr>j
