from __future__ import annotations

import os
import sys
import typing

import kdl

with io.open("boilerplate/doctypes.kdl", "r") as fh:
	text = fh.read()
	kdl.parse(text)