# aws-serverless-book-recommendation-system
A serverless personalized book recommendation service built using AWS Lambda, DynamoDB, and Amazon Comprehend that suggests books based on user reading preferences and NLP analysis of book summaries and reviews.
# 📚 Serverless Personalized Book Recommendation System

A serverless book recommendation service built using AWS Lambda, Amazon DynamoDB, and Amazon Comprehend.  
This system analyzes user reading preferences using Natural Language Processing (NLP) and provides personalized book recommendations based on book summaries and reviews.

---

## 🚀 Project Overview

This project allows users to enter their reading preferences (for example: genres, interests, or topics).
The backend uses Amazon Comprehend to analyze the text and understand user intent.
Based on this analysis, relevant books are fetched from DynamoDB and returned as personalized recommendations.

The entire system is built using a serverless architecture, making it scalable, cost-effective, and easy to maintain.

---

## 🛠️ Technologies Used

- AWS Lambda (Python)
- Amazon API Gateway
- Amazon DynamoDB
- Amazon Comprehend (NLP)
- AWS IAM
- Amazon CloudWatch

---

## ✨ Features

- Accepts user reading preferences as input
- Uses NLP to analyze text and extract key topics
- Recommends books based on summaries and reviews
- Fully serverless architecture
- Highly scalable and cost-efficient
- REST API based implementation

---

## 🏗️ Architecture

User → API Gateway → AWS Lambda → Amazon Comprehend → DynamoDB → Recommendation Response

(Architecture diagram is included in the repository)

---

## 🔄 How the System Works

1. User submits reading preference through API request
2. API Gateway triggers AWS Lambda function
3. Lambda sends text to Amazon Comprehend for NLP analysis
4. Extracted keywords are matched with book data in DynamoDB
5. Personalized book recommendations are returned to the user

---

## 📥 Sample API Request

```json
{
  "preference": "I like self improvement and productivity books"
}
🔹 Project Overview
This project is a serverless book recommendation service built on AWS.
It analyzes user reading preferences using Amazon Comprehend (NLP)
and suggests personalized book recommendations stored in DynamoDB.
🔹 Features
Accepts user reading preferences
Uses NLP to analyze text
Generates personalized book recommendations
Fully serverless architecture
Scalable and cost-efficient
🔹 Technologies Used
AWS Lambda (Python)
Amazon API Gateway
Amazon DynamoDB
Amazon Comprehend
IAM
CloudWatch
🔹 Project Folder Structure (EXACT FILES)
Copy code

aws-serverless-book-recommendation-system/
│
├── lambda/
│   ├── handler.py
│   ├── comprehend_utils.py
│   ├── dynamodb_utils.py
│   └── requirements.txt
│
├── data/
│   └── books.json
│
├── infrastructure/
│   ├── dynamodb.yaml
│   └── lambda-role-policy.json
│
├── tests/
│   └── test_handler.py
│
├── .gitignore
├── README.md
└── architecture.png
🔹 Project Architecture (Interviewer को impress करने वाला flow)
Copy code

User Input (Reading Preference)
        ↓
API Gateway (REST API)
        ↓
AWS Lambda (Python)
        ↓
Amazon Comprehend (NLP analysis)
        ↓
DynamoDB (Books + User Preferences)
        ↓
Personalized Book Recommendations (JSON Response)
🔹 How It Works
User submits reading preference
API Gateway triggers Lambda
Lambda analyzes text via Comprehend
Matching books fetched from DynamoDB
Personalized recommendations returned
• Built a serverless personalized book recommendation system using AWS Lambda,
  DynamoDB, and Amazon Comprehend for NLP-based user preference analysis.
• Designed REST APIs with API Gateway and implemented scalable cloud architecture.
🚧 Future Enhancements
User authentication and profiles
Recommendation ranking system
Machine learning based recommendation engine
Frontend web or mobile application
Caching using Amazon ElastiCache
🧪 Testing
Unit tests are included for Lambda functions
API can be tested using sample JSON requests
⚙️ Setup Instructions
Create a DynamoDB table for storing book data
Upload sample book data (books.json)
Create an IAM role with access to DynamoDB and Comprehend
Deploy AWS Lambda function using Python
Configure API Gateway to trigger Lambda
Test the API using Postman or curl
📤 Sample API Response
{
  "recommendedBooks": [
    "Atomic Habits",
    "Deep Work"
  ]
}
