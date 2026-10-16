TECTONIC ?= tectonic

.PHONY: preview
preview:
	$(TECTONIC) --keep-logs main.tex
