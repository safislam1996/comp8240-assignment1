#!/bin/bash

# Run ner.sh on wikipedia.txt and redirect output to stanford-wikipedia.txt
./eval.sh ../wikipedia-gold.txt > ../wikipedia-eval.txt

# Run ner.sh on fanwiki.txt and redirect output to stanford-fanwiki.txt
./eval.sh ../fanwiki-gold.txt > ../fanwiki-eval.txt
