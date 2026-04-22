# 🔐 Real-Time Face Identification Login System

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Inter&size=26&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=Biometric+Authentication+System;Computer+Vision+%2B+AI+%2B+Backend;Real-Time+Face+Verification" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/DeepFace-Face%20Recognition-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/FastAPI-Backend-teal?style=for-the-badge&logo=fastapi">
</p>

---

## 🚀 Overview

A **real-time biometric authentication system** that enables secure login using face recognition.  
Built using **DeepFace, OpenCV, and FastAPI**, the system simulates a **production-style authentication pipeline**.

---

## 🧠 System Flow

Camera → Face Detection → Liveness Check → Face Verification → Access Granted / Denied

---

## 🧠 Key Features  

- Real-Time Processing
- Live webcam-based face detection
- Continuous frame analysis
- Intelligent Verification
- Multi-frame validation for higher accuracy
- Threshold tuning to reduce false positives

---

## ⚙️ Installation  

bash
- git clone https://github.com/yourusername/face-id-auth-system
- cd face-id-auth-system
- pip install -r requirements.txt
- python app.py 

---

## 🔐 Security Layer
- Motion-based liveness detection (anti-spoofing)
- Prevents static image attacks

---

## ⚙️ System Design
- Modular architecture (clean separation of logic)
- Multi-user authentication support
- Scalable backend-ready structure

---

## 🌐 Backend Integration
- FastAPI endpoints for authentication
- Latency tracking for performance insights

---

## 📊 Evaluation
- Tested on subset of LFW dataset
- Real-world conditions: lighting, pose, expressions

---

## 📊 Dataset

Uses a subset of Labeled Faces in the Wild (LFW):

- 👤 5 identities
- 🖼 1 training image per user
- 🔍 5–10 test images per user

---

## ▶️ Run Application
- GUI Mode -- python app.py
- API Mode -- uvicorn api:app --reload
- Evaluation -- python evaluation.py

---

## 🧠 What I Learned
- Designing real-time computer vision pipelines
- Handling noisy predictions using multi-frame logic
- Structuring scalable Python applications
- Integrating AI models with backend systems
- Evaluating models using real-world datasets

---

## 🚧 Future Improvements
- Advanced liveness detection (eye-blink / depth-based)
- Face embedding caching for faster inference
- Database integration (MongoDB / SQL)
- Cloud deployment (AWS / Azure)
- Multi-camera support

---

## 👤 Author

Lohith Reddy Bodumallu

<p align="center"> <a href="mailto:lohithreddyb@gmail.com"> <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"> </a> <a href="https://linkedin.com/in/lohith-reddy-mrnobody"> <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"> </a> <a href="https://github.com/Mr-Nobody0409"> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"> </a> </p>
