# ELMS 🎓📚 | E-Learning Management System  

[![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)](#)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)](#)
[![Visual Studio Code](https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=vsc&logoColor=white)](#)
[![Socket.io](https://img.shields.io/badge/Socket.io-010101?logo=socketdotio&logoColor=white)](#)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff)](#) 
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](#)

**ELMS (E-Learning Management System)** is a modern virtual classroom platform designed to facilitate **seamless online learning, collaboration, and communication** between students, teachers, and administrators. ELMS provides **live classes, document sharing, messaging, and course management**—all in one platform.

📂 [Frontend Repository](https://github.com/Mazen-Barakat/elms-front) 

---

## 📽️ Project Demo (Video)  

![ELMS Demo](https://github.com/user-attachments/assets/44284540-8071-4fdd-aa49-8625a22da86d)  

---

## 📖 Table of Contents  

- [🌟 Features](#-features)  
- [📽️ Project Demo](#️-project-demo-video)  
- [🛠 Installation & Setup](#️-installation--setup)  

---

## 🌟 Features  

✅ **Live Video Classes** – WebRTC-powered live classes with real-time interaction  
✅ **Course Management** – Teachers can create, update, and manage courses  
✅ **Instant Messaging** – Chat with students and teachers in real-time (powered by WebSockets)  
✅ **File Sharing** – Upload and share PDFs, presentations, and assignments  
✅ **Attendance Tracking** – Automatic logging of attendance for online classes  
✅ **Assignment Submission** – Students can submit assignments directly on the platform  
✅ **Admin Dashboard** – Manage users, monitor activities, and analyze platform usage  

---

## 🛠️ Installation & Setup

1. **Clone the repository**:

   ```bash
   https://github.com/Mazen-Barakat/elms-backend
   cd elms-backtend
   ```
2. **Create a virtual environment & activate it**:
    ```bash
    python -m venv env
    source env/bin/activate
    ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Open .env and configure your database credentials, WebSocket settings, and other configurations.

5. **Run database migrations**:

   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (optional, for admin access)**:

   ```bash
   python manage.py createsuperuser
   ```
7. **Start the Django server**:

   ```bash
   python manage.py runserver
   ```   
  The backend API should now be running at http://127.0.0.1:8000.
---

👨‍💻 Made by the ELMS Team
