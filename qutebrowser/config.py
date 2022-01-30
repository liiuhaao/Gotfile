c = c
config = config

config.load_autoconfig()

c.auto_save.session = True
c.content.proxy = "socks://localhost:9050"

c.completion.shrink = True
c.completion.use_best_match = True
c.completion.open_categories = [
    "quickmarks", "bookmarks", "history", "filesystem"
]

# c.content.pdfjs = True
c.content.plugins = True
c.content.blocking.method = "both"
c.content.javascript.can_access_clipboard = True

c.url.start_pages = ["www.google.com"]
c.url.default_page = "www.google.com"
c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
    "gg": "https://www.google.com/search?q={}",
    "wk": "https://wikipedia.org/wiki/{}",
    "gh": "https://github.com/search?q={}",
    "bd": "https://www.baidu.com/s?wd={}",
    "dd": "https://www.duckduckgo.com/?q={}",
    "aw": "https://wiki.archlinux.org/?search={}",
    "zh": "https://www.zhihu.com/search?q={}",
    "db": "https://www.douban.com/search?q={}",
    "tb": "https://s.taobao.com/search?q={}",
    "jd": "https://search.jd.com/Search?keyword={}",
}

# c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = "dark"

c.downloads.location.directory = "~/Downloads"

c.editor.command = ["st", "-e", "nvim", "{}"]

c.fileselect.folder.command = ["st", "-e", "ranger", "--choosedir={}"]
c.fileselect.multiple_files.command = ["st", "-e", "ranger", "--choosedir={}"]
c.fileselect.single_file.command = ["st", "-e", "ranger", "--choosedir={}"]

c.fonts.default_size = "20px"
c.fonts.default_family = "SauceCodePro Nerd Font"
# c.fonts.contextmenu = "SauceCodePro Nerd Font"
# c.fonts.web.family.cursive = "SauceCodePro Nerd Font"
# c.fonts.web.family.fantasy = "SauceCodePro Nerd Font"
# c.fonts.web.family.fixed = "SauceCodePro Nerd Font"
# c.fonts.web.family.sans_serif = "SauceCodePro Nerd Font"
# c.fonts.web.family.serif = "SauceCodePro Nerd Font"
# c.fonts.web.family.standard = "SauceCodePro Nerd Font"

c.scrolling.bar = "when-searching"

c.input.insert_mode.plugins = True
c.scrolling.smooth = True
c.tabs.indicator.width = 3
c.tabs.indicator.padding = {"bottom": 0, "left": 0, "right": 5, "top": 0}
c.tabs.padding = {"bottom": 0, "left": 0, "right": 0, "top": 0}

c.zoom.default = "100%"

config.unbind("D")
config.unbind("d")
config.unbind("J")
config.unbind("K")
config.unbind("<Ctrl-q>")
config.unbind("<Ctrl-n>")
config.unbind("u")

config.bind("<Alt-b>", "config-cycle tabs.show always switching")
config.bind("<Alt-Shift-b>", "config-cycle statusbar.show always in-mode")
config.bind("<Alt-h>", "back")
config.bind("<Alt-l>", "forward")
config.bind("<Alt-j>", "tab-next")
config.bind("<Alt-k>", "tab-prev")
config.bind("<Alt-Shift-j>", "tab-move +")
config.bind("<Alt-Shift-k>", "tab-move -")
config.bind("<Alt-q>", "tab-close")
config.bind("<Alt-Return>", "open -t")
config.bind("<Alt-p>", "tab-pin")
config.bind("<Alt-r>", "reload")
config.bind("<Alt-u>", "undo")

config.bind("zz", "zoom")
config.bind("<Ctrl-=>", "zoom-in")
config.bind("<Ctrl-->", "zoom-out")
config.bind("zi", "zoom-in")
config.bind("zo", "zoom-out")
config.unbind("<Ctrl-p>")
config.bind("tdm", "config-cycle colors.webpage.darkmode.enabled True False")
config.bind("<Ctrl-n>", "scroll down", mode="insert")
config.bind("<Ctrl-p>", "scroll up", mode="insert")
config.bind("<Ctrl-b>", "scroll left", mode="insert")
config.bind("<Ctrl-f>", "scroll right", mode="insert")
config.bind(
    "<ESC>",
    "clear-keychain ;; search ;; fullscreen --leave ;; jseval -q document.activeElement.blur()",
)
config.source("gruvbox.py")
