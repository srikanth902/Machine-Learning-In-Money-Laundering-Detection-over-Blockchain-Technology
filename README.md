# 🚨 Anti-Money Laundering (AML) Detection System

## 📌 Overview

Financial fraud and money laundering are major challenges in the banking sector. This project presents a **Machine Learning-based Anti-Money Laundering (AML) Detection System** that analyzes transaction data and identifies suspicious activities.

The system classifies transactions as:

* ✅ **Legitimate (0)**
* ⚠️ **Money Laundering (1)**

---

## 🎯 Objective

The main goal of this project is to:

* Detect suspicious financial transactions
* Reduce fraud risks in banking systems
* Improve accuracy using machine learning models

---

## 📊 Dataset Description

The dataset used in this project contains bank transaction details with the following features:

* 🏦 **From Bank** – Sender bank
* 🏦 **To Bank** – Receiver bank
* 💰 **Amount** – Transaction amount
* 💳 **Payment Format** – Mode of transaction (ACH, Cash, Credit Card, etc.)
* 🚩 **Is Laundering** – Target variable (0 = No, 1 = Yes)

---

## ⚙️ Technologies Used

* 🐍 **Python**
* 📊 **Pandas & NumPy** (Data Processing)
* 📈 **Matplotlib / Seaborn** (Visualization)
* 🤖 **Scikit-learn** (Machine Learning)

---

## 🧠 Machine Learning Approach

The project follows these steps:

1. **Data Preprocessing**

   * Handling missing values
   * Encoding categorical data
   * Feature scaling

2. **Model Building**

   * Train/Test split
   * Applying classification algorithms

3. **Evaluation**

   * Accuracy score
   * Confusion matrix
   * Performance comparison

---

## 📈 Key Insights

* Transaction amount and payment type play a crucial role in detecting fraud
* Certain payment methods show higher risk patterns
* Machine learning improves detection efficiency significantly

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/money-laundering-detection.git
cd money-laundering-detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Project

```bash
python main.py
```

---

## 📂 Project Structure

```
money-laundering-detection/
│── data/               # Dataset files
│── src/                # Source code
│── model/              # Trained models
│── main.py             # Main execution file
│── requirements.txt
│── README.md
```

---

## 📌 Applications

* 🏦 Banking & Financial Institutions
* 💳 Fraud Detection Systems
* 🔍 Transaction Monitoring Systems
* 🌐 FinTech Security Solutions

---

## 🔮 Future Scope

* Real-time fraud detection system
* Integration with live banking APIs
* Deep Learning-based detection models
* Dashboard for monitoring transactions

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repository and improve the project.

---


## ⭐ Acknowledgement

This project is developed as part of academic learning to understand real-world financial fraud detection using machine learning.

---

### 🌟 If you like this project, don’t forget to star the repository!
