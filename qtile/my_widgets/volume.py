from libqtile import widget


class Volume(widget.Volume):

    def _update_drawer(self):
        char_list = ["奔 ", "墳 ", " "]
        if self.volume == -1:
            self.text = " 婢 MUTE"
        else:
            char = char_list[int(self.volume / 101 * len(char_list))]
            self.text = char + "{:>3d}%".format(self.volume)
