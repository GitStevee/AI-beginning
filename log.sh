#!/bin/bash
# Использование: ./log.sh fitness-coach "что сделали и почему"
echo "" >> "$1/DEVLOG.md"
echo "## $(date '+%Y-%m-%d %H:%M')" >> "$1/DEVLOG.md"
echo "" >> "$1/DEVLOG.md"
echo "$2" >> "$1/DEVLOG.md"
git add . && git commit -m "log: $1 $(date '+%Y-%m-%d')"
