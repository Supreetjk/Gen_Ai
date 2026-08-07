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

# CHUNKING
breaking the larger documents into meaningful data
Chunks: group of words or characters
Chunking is the process of grouping the words 

## uses:
use chunking before embeddings

### Types of Chunking
1. Fixed size chunking    ->100
ex: grouping the chunks based on fixed size
2. Fixed size + Overlapping    ->20
ex: grouping the chunks based on both fixed size+overlapping
3. Paragraph based     -> "\n\n"
ex: grouping the chunks where the newlines found in the data
4. Sentence based     -> ".\n"
ex: grouping the chunks where the both . and newlines found in the data
5. Recursive    
6. Semantic(used for large documents/data)
7. Page number or structured chunking


chunking types which we used in rag architectue
1. fixed size + overlapping
2. reccrsive
3. structure based
4. semantic chunking


# VECTORIZATION
numerical representation of chunks or tokens

### Embedding models:
It's used for sentiment analysis
step 1: which helps to convert chunks into vectors and this we use mostly for sentence based senarios

where we used this in real time project?
* in Rag architecture
* senetence based classification
* to understand the context inside the chunks

### types of Vectorization
1. Count vectorization
2. TF-IDF Vectorization

1. Count vectorization
it is ml preprocessing technique which converts sentence base column values into numerical values

how Count vectorization works?
step 1: selects unique words from the entire samples
the movie was good
life is booring
kapil sharma got placed
unique words=the,movie,was,good,life,is,booring,kapil sharma, got,placed
step 2: sort by alphabetical order
step 3: creating new columns based on unique values
booring | gooood | got  |   is  |  kapil | life | movie | placed | sharma | the | was |





step 4: transforms sentence values into numerical values based on word frequency
    booring | gooood | got  |   is  |  kapil | life | movie | placed | sharma | the | was |
1      0    |   1    |  0   |
2      1    |   0    |  0   |
3      0    |   0    |  1   |
step 5: training the model 

Eucledian formula
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}


what is temperature parameter?
it is a sampliing parameter that influences how confidently the model takes the next word of the token
* it helps to handle llm halucination problems
always use less than less to ignore imaginary content
temperature<0.2 or fully ignore use temperture=0.0
