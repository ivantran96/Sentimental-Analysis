# Sentimental-Analysis
DataRes Project

## Download Dependencies
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- I would recommend creating the virtual environment in a directory (folder) that is specific for the project
- **Might need to do** `python3 -m venv venv` **instead**
- More about virtual environments [here](https://www.youtube.com/watch?v=Kg1Yvry_Ydk&t=367s)

## TranscriptCleaner.py
- Tolkenizes and lemmatizes the transcript while filtering out stop words
- Imports the list into a new CSV file
`python TranscriptCleaner.py`
- **Make sure you are in the virtual environment that you created (venv)**

## Importing Data from CSV 
This imports the data from a csv file as a list 
```
from csv import reader
with open(____) as file:
    read_file = reader(file)
    list_file = list(read_file)
    data = list_file[0]
 ```
 - The reason behind `data = list_file[0]` is that `list_file` is a list with another list inside (nested list)
    - The list inside `list_file` (`list_file[0]`) contains the separated words (tokens)
  
## Frequency Distribution with NLTK
This creates a frequency distrubution of unique words in `data`
```
from nltk.probability improt FreqDist
data_freqdist = FreqDist(data)
data_freqdist
```
  
## Notes
- When opening files, surround the file name with "..."
  - i.e. "file.txt"



