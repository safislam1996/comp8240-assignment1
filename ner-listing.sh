#!/bin/bash
wikipedia_file="../wikipedia.txt"
fanwiki_file="../fanwiki.txt"

# Output files
ner_list_wikipedia="../ner-list-wikipedia.txt"
ner_list_fanwiki="ner-list-fanwiki.txt"


# Extract NERs from wikipedia file
echo "Extracting NERs from $wikipedia_file..."
grep -oE '\b\w+/LOCATION\b|\b\w+/PERSON\b|\b\w+/ORGANIZATION\b' "$wikipedia_file" | sed 's#/LOCATION##;s#/PERSON##;s#/ORGANIZATION##' > "$ner_list_wikipedia"
echo "NERs extracted to $ner_list_wikipedia."