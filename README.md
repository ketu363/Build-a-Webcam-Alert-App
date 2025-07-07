# 📷 Motion Detection & Email Alert System with OpenCV + Streamlit

This project is a real-time **motion detection system** built using **OpenCV**, **Streamlit**, and **Python threading**. The app captures video from a webcam, detects when an object appears and exits the frame, captures images of the object, and sends an **email with an image attachment** to the user.

---

## 🚀 Features

- ✅ Real-time webcam monitoring
- 🟥 Motion detection using contour analysis
- 📸 Capture multiple image frames when an object appears
- 📨 Automatically sends an email with the **best frame (middle image)** attached
- 🧹 Cleans up stored images after email is sent
- 🔁 Uses **Python threading** to avoid freezing UI during email transmission
- 📅 Adds current **day and time** on live video using OpenCV

---

## 🧠 Concepts Covered

- Computer Vision with OpenCV
- Real-time image capture and storage
- Email automation using `smtplib` with Gmail
- Attaching images using `EmailMessage`
- Folder cleanup with `os` and `glob`
- Threading for non-blocking execution
- Live webcam stream in **Streamlit**
- Adding text overlays (day/time) to images

---

## 📌 Real-World Relevance

This project demonstrates practical image processing and automation techniques, similar to how:

- **YouTube** detects video copyright violations
- **Facebook** auto-describes photos for visually impaired users
- **GIS** classifies satellite images (urban vs forest)
- **Phones** unlock using face recognition
- **Self-driving cars** detect objects in real-time

---

## 🛠 Technologies Used

- Python 3
- OpenCV (`cv2`)
- Streamlit
- `smtplib`, `email.message`, `imghdr`
- Threading
- Glob and OS modules

---

## 👨‍💻 Author

**Nishant Ketu**  
Data Science & AI Enthusiast  
GitHub: [@ketu363](https://github.com/ketu363)  
LinkedIn: [Nishant Ketu](https://www.linkedin.com/in/nishant-ketu-388a04152/)

---

## 💡 Future Ideas

- Upload multiple images in the email
- Add GUI controls to start/stop camera
- Integrate with a cloud server or database
- Add face recognition or object classification

---

📬 *Built with love and code, to learn and share the power of image processing.*
