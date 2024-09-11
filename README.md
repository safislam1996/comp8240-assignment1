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
