# NLP_labs

This repository contains three Natural Language Processing projects focused on Esperanto language analysis.

## Project 1: Text Analysis Tools

A collection of Python scripts for analyzing Esperanto text data:

### zipf.py

Analyzes word frequencies and calculates Zipf scores for words in a text file. The script:

- Reads tab-separated word frequency data
- Adjusts index values
- Calculates Zipf scores (frequency/rank)
- Outputs results to CSV

### percent.py

Calculates cumulative word frequency percentages to understand vocabulary coverage:

- Processes word frequency data
- Calculates how many words make up different percentage thresholds (10%, 20%, etc.)
- Saves results to CSV

### bigrams.py

Analyzes bigram frequencies in Esperanto sentences:

- Reads sentence data
- Extracts and counts bigrams
- Outputs top 10 most frequent bigrams to CSV

## Project 2: Esperanto Sentence Generator

A GUI application for generating grammatically correct Esperanto sentences:

- Uses Tkinter for the interface
- Includes comprehensive Esperanto vocabulary (nouns, verbs, adjectives)
- Supports different sentence structures:
  - Subject types (pronouns, noun phrases)
  - Verb tenses (present, past, future)
  - Optional objects
- Provides real-time sentence generation

Reference implementation:

```python:proj2/main.py
startLine: 5
endLine: 246
```

## Project 3: Verb-Noun Relationship Analyzer

An interactive tool for analyzing relationships between Esperanto verbs and their associated nouns:

- Features a modern GUI interface
- Supports set operations (show, intersection, union)
- Contains extensive verb-noun relationship data
- Allows exploration of semantic relationships

Reference implementation:

```python:proj3/main.py
startLine: 7
endLine: 164
```

## Installation

1. Clone the repository
2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install pandas tkinter
```

## Usage

Each project can be run independently:

```bash
# Project 1
python proj1/zipf.py
python proj1/percent.py
python proj1/bigrams.py

# Project 2
python proj2/main.py

# Project 3
python proj3/main.py
```
