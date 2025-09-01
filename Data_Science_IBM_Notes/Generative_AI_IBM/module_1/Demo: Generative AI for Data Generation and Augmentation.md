# 📊 Generative AI for Data Generation and Augmentation

Welcome to this video on **Generative AI as a useful tool for data generation and augmentation**.  
After watching this video, you will be able to:

- ✅ Explain how generative AI is used for data generation and augmentation  
- ✅ Generate synthetic data using GenAI tools  
- ✅ Augment data using GenAI-based platforms  

---

## 🌱 What is Data Augmentation?

- **Data Augmentation** is the process of **artificially increasing** the size of a training dataset.
- It is especially useful when:
  - Data is limited
  - Datasets are unbalanced
- Types of data:
  - **Structured** (e.g., tabular)
  - **Semi-structured** (e.g., text, code)
  - **Unstructured** (e.g., image, audio)

---

## 🏗️ Structured Data Augmentation

### 🔧 Tools:
- **CTGAN** – Conditional GAN for structured/tabular data
- **SDV (Synthetic Data Vault)** – Generates synthetic data preserving real statistical traits

### 🧠 Use Cases:
- Handling missing values
- Addressing class imbalance
- Preserving privacy in datasets

---

## 📄 Semi-Structured Data Augmentation

### 🔧 Tools:
- **GPT-3 / ChatGPT**
- **GitHub Copilot**

### 🧠 Use Cases:
- Generating realistic **text descriptions** and **code snippets**
- Enhancing NLP and code-generation ML models

---

## 🎨 Unstructured Data Augmentation

### 🔧 Tools:
- **StyleGAN2**, **BigGAN** – For image generation
- **SoundGAN** – For audio generation

### 🧠 Use Cases:
- Creating high-resolution images
- Generating synthetic audio
- Boosting training data for vision/audio models

---

## 🔍 Hands-on Tool Demonstrations

### 1. 🧪 Universal Data (generate.universaldata.io)
- Prompt: `"Patient dataset for symptoms of diabetes"`
- Output: Synthetic data downloadable in CSV format

### 2. 🤖 ChatGPT
- Prompt example:
```plaintext
Create a dataset with temperature, humidity, wind speed, fog, rain, snow... 
Generate 100 observations in CSV format.