# from lib2to3.widget.Battery import BatteryState

from libqtile import widget


class Battery(widget.Battery):

    def __init__(self, **config) -> None:
        import warnings

        from libqtile.widget import base
        if "update_delay" in config:
            warnings.warn(
                "Change from using update_delay to update_interval for battery widget, removed in 0.15",
                DeprecationWarning,
            )
            config["update_interval"] = config.pop("update_delay")

        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(self.defaults)

        self._battery = self._load_battery(**config)
        self._has_notified = False
        self.epoch = 0
        self.char_list = [" ", " ", " ", " ", " "]

    def build_string(self, status) -> str:
        if self.hide_threshold is not None and status.percent > self.hide_threshold:
            return ""

        state = str(status.state)
        if self.layout is not None:
            if state == "BatteryState.DISCHARGING" and status.percent < self.low_percentage:
                self.layout.colour = self.low_foreground
                self.background = self.low_background
            else:
                self.layout.colour = self.foreground
                self.background = self.normal_background

        if state == "BatteryState.CHARGING":
            self.epoch = (self.epoch + 1) % len(self.char_list)
            char = self.char_list[self.epoch]
        elif state == "BatteryState.DISCHARGING":
            char = self.char_list[int(status.percent * len(self.char_list))]
        elif state == "BatteryState.FULL":
            if self.show_short_text:
                return "Full"
            char = self.char_list[-1]
        elif state == "BatteryState.EMPTY" or (state == "BatteryState.UNKNOWN"
                                               and status.percent == 0):
            if self.show_short_text:
                return "Empty"
            char = self.char_list[0]
        else:
            self.epoch = (self.epoch + 1) % len(self.char_list)
            char = self.char_list[self.epoch]

        hour = status.time // 3600
        minute = (status.time // 60) % 60

        return self.format.format(char=char,
                                  percent=status.percent,
                                  watt=status.power,
                                  hour=hour,
                                  min=minute)
