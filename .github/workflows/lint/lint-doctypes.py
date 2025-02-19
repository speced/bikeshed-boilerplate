from __future__ import annotations

import kdl

with open("boilerplate/doctypes.kdl", "r") as fh:
	text = fh.read()
	kdl.parse(text)