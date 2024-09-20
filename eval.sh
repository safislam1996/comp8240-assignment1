# file folde for the jar and classifier
scriptdir=$(dirname "$0")
stanford_jar="$scriptdir/stanford-ner.jar:$scriptdir/lib/*"
stanford_classifier="$scriptdir/classifiers/english.all.3class.distsim.crf.ser.gz"

input_file=$1
output_file=$2

java -cp "$stanford_jar" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier "$stanford_classifier"  -testFile $input_file 

