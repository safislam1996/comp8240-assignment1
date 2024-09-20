# COMP8420 Assignment 1

## Step 1: Setting up the VM and the github repository
Connecting to the github codespace

## Step 2: Installing the NER system
Installing the system in the github codespace
### 2.1 : Get the ner zipfile
```
wget https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip
```
### 2.2: Extract from the zip file

```
unzip stanford-ner-4.2.0.zip
```
### 2.3 : Running the sample text
```
./ner.sh sample.txt
```
## Step 3: Gathering the data

### 3.1: Creating a wikipedia extraction python file
Create `extract_wik.py` in order to extract texts from an actor's wikipedia page. Setting the word limit to 500. In this example I used famed late night *Jon Stewart*. Don't forget to install wikipedia package via `pip install wikipedia`.
Running the code via
```
python extract_wiki.py
```
The following code performs the ner tagging of the extracted text from the `wikipedia.txt` file. In order to run the code . Firstly `cd stanford-ner-2020-11-17`
```
./ner.sh ../wikipedia.txt
```

### 3.2 : Creating fandom wiki python file
Creating `extract_wiki.py` for downloading information of a character of Jojo's Bizarre Adventure.
Firstly `pip install fandom-py`. The character I have chosen is Josuke Higashikata and printed out the text from the *Showdown with Kira* section of the character wiki.
Running the code via
```
python extract_wiki.py
```
The following code performs the ner tagging of the extracted text from the `wikipedia.txt` file. In order to run the code . Firstly `cd stanford-ner-2020-11-17`
```
./ner.sh ../fanwiki.txt
```
## Step 4: Indetify NER

Runnning the file `ner-listing.py` for extracting the list of NER inside each line for the files   `stanford-wikipedia.txt` and  `stanford-fanwiki.txt` .

```
python ner-listing.py
```
## Step 5: Evaluation of NER

| Entity | P            | R      | F1     | TP | FP | FN |
|---------------------|--------|--------|----|----|----|
| LOCATION | 0.6667     | 1.0000 | 0.8000 | 4  | 2  | 0  |
| ORGANIZATION | 0.6000 | 0.5000 | 0.5455 | 3  | 2  | 3  |
| PERSON | 0.9130       | 0.9545 | 0.9333 | 21 | 2  | 1  |
| Totals | 0.8235       | 0.8750 | 0.8485 | 28 | 6  | 4  |

| Entity |P        | R      | F1     | TP | FP | FN |
|-----------------|--------|--------|----|----|----|
| LOCATION | 0.0000 | 1.0000 | 0.0000 | 0  | 1  | 0  |
| PERSON |1.0000   | 0.9677 | 0.9836 | 30 | 0  | 1  |
| Totals |0.9677   | 0.9677 | 0.9677 | 30 | 1  | 1  |


