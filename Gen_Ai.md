# Natural Language Processing (NLP) Notes

## What is NLP?

**Natural Language Processing (NLP)** is a branch of **Artificial Intelligence (AI)** that enables computers to understand, interpret, process, and generate human language (text or speech).

**Example Applications:**

* Chatbots (ChatGPT)
* Google Translate
* Voice assistants (Siri, Alexa)
* Sentiment analysis
* Spam email detection
* Text summarization

---

# NLTK (Natural Language Toolkit)

**NLTK (Natural Language Toolkit)** is one of the most popular Python libraries for NLP. It provides tools for text processing, including:

* Tokenization
* Stop word removal
* Stemming
* Lemmatization
* Part-of-Speech (POS) tagging
* Named Entity Recognition (NER)
* Text classification

It is widely used for learning, research, and prototyping NLP applications.

---

# Tokenization

**Definition:**

Tokenization is the process of breaking a large text into smaller units called **tokens**.

Tokens can be:

* Characters
* Words
* Sentences
* Subwords

**Example:**

Sentence:

```
I love learning NLP.
```

Word Tokens:

```
["I", "love", "learning", "NLP"]
```

Sentence Tokens:

```
["I love learning NLP."]
```

Character Tokens:

```
["I", " ", "l", "o", "v", "e", ...]
```

### Why is Tokenization Important?

* Helps NLP models understand text.
* Converts unstructured text into machine-readable units.
* Improves text analysis and feature extraction.
* Acts as the first preprocessing step in most NLP pipelines.

---

# Stop Word Removal
**Definition:**
Stop words are common words that usually do not add significant meaning to a sentence.
Examples:

```
is
am
are
the
a
an
of
to
in
and
for
```

Removing stop words reduces noise and improves processing efficiency.

**Example:**
Original:

```
I am learning Natural Language Processing.
```

After Stop Word Removal:

```
learning Natural Language Processing
```

---

# Stemming
**Definition:**
Stemming reduces a word to its **root (stem)** by removing prefixes or suffixes. The resulting stem may not be a valid dictionary word.

**Examples:**
| Original Word | Stem    |
| ------------- | ------- |
| Playing       | Play    |
| Running       | Run     |
| Studies       | Studi   |
| Connected     | Connect |

Common stemming algorithms:
* Porter Stemmer
* Snowball Stemmer
* Lancaster Stemmer

**Advantages**
* Faster
* Less computationally expensive

**Disadvantages**
* May produce incorrect or non-dictionary words.

---

# Lemmatization
**Definition:**
Lemmatization converts a word into its **base (dictionary) form**, known as the **lemma**.

Unlike stemming, it considers the word's meaning and grammatical context.

**Examples:**
| Original Word | Lemma |
| ------------- | ----- |
| Running       | Run   |
| Better        | Good  |
| Studies       | Study |
| Mice          | Mouse |

**Advantages**
* Produces meaningful dictionary words.
* More accurate than stemming.

**Disadvantages**
* Slower because it uses vocabulary and grammar rules.

---

# Difference Between Stemming and Lemmatization

| Stemming                                      | Lemmatization                   |
| --------------------------------------------- | ------------------------------- |
| Uses simple rules to remove prefixes/suffixes | Uses vocabulary and grammar     |
| Faster                                        | Slower                          |
| May produce non-dictionary words              | Produces valid dictionary words |
| Less accurate                                 | More accurate                   |

---

# NLTK vs spaCy
| NLTK                                    | spaCy                                           |
| --------------------------------------- | ----------------------------------------------- |
| Primarily for learning and research     | Designed for production applications            |
| Slower                                  | Faster                                          |
| Easy for beginners                      | Optimized for performance                       |
| Offers many educational algorithms      | Offers industrial-strength NLP pipelines        |
| Better for teaching and experimentation | Better for building real-world NLP applications |

### Which One Should You Use?
* **Choose NLTK** if you are learning NLP concepts or doing research.
* **Choose spaCy** if you are building production-ready NLP applications where speed and efficiency are important.

---

## NLP Preprocessing Pipeline
1. Collect text data
2. Convert text to lowercase
3. Tokenization
4. Remove punctuation
5. Remove stop words
6. Stemming or Lemmatization
7. Convert text into numerical features (e.g., Bag of Words, TF-IDF, Word Embeddings)
8. Train the machine learning or deep learning model

## CHUNKING
Chunks: group of words or characters
Chunking: the process of grouping the words 

### Types of Chunking
1. Fixed size chunking
2. Fixed size + Overlapping
3. Paragraph based
4. Sentence based
5. Recursive
6. Semantic
7. Page number or standard chunking


