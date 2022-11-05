import random

import panel as pn
pn.extension()

alert = pn.pane.Alert("Panel appears to be working!")

rcolor = lambda: "#%06x" % random.randint(0, 0xFFFFFF)
box = pn.GridBox(*[pn.pane.HTML(background=rcolor(), width=50, height=50) for i in range(24)], ncols=6)

dashboard = pn.Column(alert, box)

dashboard.servable()
