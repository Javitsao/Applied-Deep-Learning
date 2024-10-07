# Applied-Deep-Learning

## Homework Assignments

### HW1: Chinese Extractive Question Answering (QA)
- **Description**: Implement a system to extract answers from Chinese text based on given questions.
    - Paragraph Selection: Determine which paragraph is relevant.
    - Span Selection: Determine the start and end position of the answer span.


### HW2: Chinese News Summarization (Title Generation)
- **Description**: Develop a model to generate titles for Chinese news articles.
- **Data**: 
    - Source: news articles scraped from udn.com
    - Train: 21710 articles from 2015-03-02 to 2021-01-13

### HW3: Instruction Tuning (Classical Chinese)
- **Description**: Fine-tuning(QLoRA) the LLaMa model for the bidirectional translation between vernacular Chinese and Classical Chinese.
- **Model**: Traditional Mandarin support LLM based on LLaMa 2(https://ai.meta.com/llama/)


## Final Project

### Fake News Detection
- **Description**: Create a system to detect fake news in Chinese media.
**Abstract:**
The abundance of fake news in the digital age hinders reliable information flow. This research delves into Natural Language Processing (NLP) techniques for detecting fake news and discerning human-generated content. We explore the efficacy of models like `bert-base-uncased` and language-specific variants (e.g., `BERT-based-Japanese`) in differentiating between genuine and deceptive news articles. Through rigorous experimentation and evaluation, we unveil the strengths and limitations of diverse NLP approaches, shedding light on their performance across various linguistic landscapes. The findings contribute to the advancement of fake news detection systems, bolstering information integrity in the digital era.

- **Introduction:**
Technological advancements have made it effortless to access global information via social media. Consequently, detecting fake news is crucial. Our team leverages NLP and machine learning to build an accurate fake news detection model, empowering users to discern truth from falsehood. While we lack a journalism background, a teammate's experience in a human-vs.-ChatGPT paragraph classification contest inspired our venture into text classification tasks.

We employ two datasets featuring genuine and fake news:

1. **Anomaly Detection Dataset (English):** Possesses a small proportion of fake news (human-generated)
2. **Balanced Dataset (Japanese):** Contains roughly equal amounts of true and fake news (GPT2-generated)
