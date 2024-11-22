.PHONY: all

include config.mk
BUILD_CMD := ./build.py $(EXTENSIONS) $(JS) $(CSS)

all:
	@for md_file in $$(find $(DIR) -type f -name *.md); do \
		output_file=$$(echo $${md_file%.md} | sed -e 's/src/html/;s/$$/.html/'); \
		$(BUILD_CMD) $$md_file > $$output_file; \
	done

