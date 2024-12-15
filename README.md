

# 🔮 Invisibility Cloak using OpenCV and Python

This project demonstrates the creation of an **Invisibility Cloak** effect using Python and OpenCV. The program detects a red-colored object in the video feed and replaces it with the background, creating the illusion of invisibility.

---

## 📋 Requirements

Before running the project, make sure you have the following installed:

- Python 3.x
- OpenCV
- NumPy

You can install the required packages by running:

```bash
pip install -r requirements.txt
```

---

## 🚀 How It Works

1. **Capture the Background**: 
   The program captures the background for a few seconds when it starts. This background is used later to replace the red-colored object.

2. **Color Detection**: 
   The program uses the HSV color space to detect red color in the video feed.

3. **Masking**:
   - A binary mask is created to identify the red regions in the frame.
   - Morphological operations are applied to refine the mask.

4. **Invisibility Effect**:
   - The red-colored regions are replaced with the previously captured background.
   - The rest of the frame remains unchanged.

---

## 🛠️ Setup and Execution

1. Clone the repository:

   ```bash
   git clone git@github.com:srishtayal/invisbility-cloak.git
   cd invisbility-cloak
   ```

2. Activate your virtual environment (optional):

   ```bash
   source myenv/bin/activate  # macOS/Linux
   myenv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python invisibility_cloak.py
   ```

5. Wear a red cloth or object in front of the camera to experience the invisibility effect.

---

## 📂 Project Structure

```
invisibility-cloak/
├── .gitignore            # Ignored files/folders (e.g., myenv, .DS_Store)
├── invisibility_cloak.py # Main Python script
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

---

## 🎨 Color Configuration

If you'd like to change the cloak's color (e.g., to blue or green), update the HSV ranges in the script:

```python
lower_red1 = np.array([0, 120, 70])  
upper_red1 = np.array([10, 255, 255])  

lower_red2 = np.array([170, 120, 70])  
upper_red2 = np.array([180, 255, 255])  
```

Adjust these values according to your desired color.

---

## 💡 Features

- Real-time color detection and replacement.
- Simple and easy-to-understand implementation using OpenCV.
- Customizable color detection range.

---

## 👩🏼‍💻 Author

**Srishti Tayal**  
[GitHub Profile](https://github.com/srishtayal)  

Enjoy exploring the magic of invisibility! ✨
