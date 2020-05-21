from easyprocess import EasyProcess

from pyvirtualdisplay.abstractdisplay import AbstractDisplay
import logging

log = logging.getLogger(__name__)

PROGRAM = "Xephyr"


class XephyrDisplay(AbstractDisplay):
    """
    Xephyr wrapper

    Xephyr is an X server outputting to a window on a pre-existing X display
    """

    def __init__(
        self,
        size=(1024, 768),
        color_depth=24,
        bgcolor="black",
        use_xauth=False,
        # check_startup=False,
        randomizer=None,
    ):
        """
        :param bgcolor: 'black' or 'white'
        """
        self.color_depth = color_depth
        self.size = size
        self.bgcolor = bgcolor
        # self.screen = 0
        # self.process = None
        # self.display = None

        AbstractDisplay.__init__(
            self,
            PROGRAM,
            use_xauth=use_xauth,
            # check_startup=check_startup,
            randomizer=randomizer,
        )

    def _check_flags(self, helptext):
        self.has_resizeable = "-resizeable" in helptext

    def _cmd(self, wfd):
        cmd = [
            PROGRAM,
            dict(black="-br", white="-wr")[self.bgcolor],
            "-screen",
            "x".join(map(str, list(self.size) + [self.color_depth])),
            # self.new_display_var,
        ]
        # if self.check_startup:
        if self.has_displayfd:
            cmd += ["-displayfd", str(wfd)]
        else:
            cmd += [self.new_display_var]

        if self.has_resizeable:
            cmd += ["-resizeable"]
        return cmd
