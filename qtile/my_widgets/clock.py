from datetime import datetime, timezone

from libqtile import widget


class Clock(widget.Clock):

    def poll(self):
        if self.timezone:
            now = datetime.now(timezone.utc).astimezone(self.timezone)
        else:
            now = datetime.now(timezone.utc).astimezone()
        hour = (int(now.strftime("%H")) - 12) % 12
        char_list = [
            "", "", "", "", "", "", "", "", "", "", "", ""
        ]
        self.format = "  %m/%d  " + char_list[hour] + " %H:%M:%S "
        return (now + self.DELTA).strftime(self.format)
