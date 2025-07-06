# 📁 webcam_streamlit_day_time.py

import streamlit as st
import cv2
from datetime import datetime  # ✅ Newly added

st.title("📷 Live Webcam with Day & Time Overlay")

start = st.button("Start Camera")

if start:
    camera = cv2.VideoCapture(0)  # 0 is default webcam
    frame_placeholder = st.image([])

    while True:
        # 🔄 Capture frame-by-frame
        _, frame = camera.read()

        # 🎨 Convert frame from BGR (OpenCV default) to RGB (Streamlit compatible)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 🕒 Get current date and time
        now = datetime.now()
        current_day = now.strftime("%A")         # e.g., 'Wednesday'
        current_time = now.strftime("%H:%M:%S")   # e.g., '14:45:30'

        # 🖍️ Put day text on the frame
        cv2.putText(img=frame,
                    text=current_day,           # 👉 e.g., 'Wednesday'
                    org=(30, 80),               # 👈 x=30, y=80
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1.2,
                    color=(255, 255, 255),      # 🔵⚪ white
                    thickness=2,
                    lineType=cv2.LINE_AA)

        # 🖍️ Put time text on the frame
        cv2.putText(img=frame,
                    text=current_time,          # 👉 e.g., '14:45:30'
                    org=(30, 130),              # 👈 x=30, y=130
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1.2,
                    color=(0, 0, 255),          # 🔴 red
                    thickness=2,
                    lineType=cv2.LINE_AA)

        # 🖼️ Display frame in the Streamlit app
        frame_placeholder.image(frame)
