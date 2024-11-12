.PHONY: all

DIR := $(shell pwd)
CSS_DIR := $(DIR)/html/css
JS_DIR := $(DIR)/html/js
EXTENSIONS := -x markdown_mermaid -x fenced_code -x tables -x codehilite
BUILD_CMD := ./build.py $(EXTENSIONS) -j $(JS_DIR)/mermaid.min.js -j $(JS_DIR)/script.js -c $(CSS_DIR)/style.css -c $(CSS_DIR)/highlights-dracula.css

all:
	@for md_file in $$(find $(DIR) -type f -name *.md); do \
		output_file=$$(echo $${md_file%.md} | sed -e 's/src/html/;s/$$/.html/'); \
		$(BUILD_CMD) $$md_file > $$output_file; \
	done

