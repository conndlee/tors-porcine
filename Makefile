TECTONIC ?= tectonic
PANDOC ?= pandoc

.DEFAULT_GOAL := all
.PHONY: all preview word

all: preview word

preview:
	$(TECTONIC) --keep-logs main.tex

word:
	python3 pandoc/export.py --pandoc "$(PANDOC)" --tectonic "$(TECTONIC)"
