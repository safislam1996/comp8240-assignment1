import re

def extract_ners(input_file, output_file):
    ner_pattern = re.compile(r'(\S+?)/([A-Z]+)')
    previous_entity=""
    previous_tag=None
    named_entities=[]
    try:
        with open(input_file, "r") as ner_output, open(output_file, "w") as ner_list:
            for line in ner_output:
                matches = ner_pattern.findall(line)
            
                for match in matches:
                    # print(match)
                    entity,tag=match
                    # print(entity,tag)
                    if tag != 'O':  # Only process non-'O' tags
                         if tag == previous_tag:
                       # If the tag is the same, join the word to the previous entity
                            previous_entity += " " + entity
                         else:
                                    # If the tag is different, save the previous entity (if any)
                                    if previous_entity:
                                            named_entities.append(previous_entity)
                                    # Start a new entity with the current word
                                    previous_entity = entity
                                    previous_tag = tag
                    else:       
                         #If tag is 'O', finalize the previous entity (if any)
                        if previous_entity:
                           named_entities.append(previous_entity)
                           previous_entity = ""
                           previous_tag = None

                    # add a check for previous match and current match
                    # ner_list.write(re.sub(r"/LOCATION|/PERSON|/ORGANIZATION", "", match) + "\n")
            print(f"NERs extracted to {output_file}")
            for entity in set(named_entities):
                ner_list.write(entity+"\n")
    
    except Exception as e:
        print(f"Error processing file: {e}")
        exit(1)

extract_ners('stanford-wikipedia.txt', 'ner-list-wikipedia.txt')
extract_ners('stanford-fanwiki.txt', 'ner-list-fanwiki.txt')