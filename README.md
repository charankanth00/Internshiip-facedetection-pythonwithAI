# 🎯 Computer Vision Projects — Summer Internship

A collection of **Python + OpenCV** computer vision projects built during a summer internship. The repository covers face detection (images & video), face recognition with training, real-time video filters & overlays, and interactive color detection.

---

## 📁 Project Structure

```
projects/
├── face detect/              # Face detection on static images
├── faceDtectVid/             # Real-time face detection on webcam video
├── faceDetect/               # Face recognition (train + detect) — basic version
├── faceRecognition/          # Face recognition suite (full-featured)
│   ├── cascades/data/        # Haar cascade XML classifiers
│   ├── images/               # Training images organized by person
│   ├── pickles/              # Serialized label mappings
│   ├── recognizers/          # Trained LBPH model (.yml)
│   ├── saved-media/          # Recorded video output
│   └── lessons/              # Standalone lesson scripts
└── python-project-color-detection/  # Interactive color detection tool
```

---

## 🚀 Projects Overview

### 1. Face Detection on Images — `face detect/`

Detects faces in a static image using the **Haar Cascade** classifier and draws bounding boxes around them.

| File | Description |
|------|-------------|
| `main.py` | Loads an image, detects faces, draws rectangles, and displays the result |

**Run:**

```bash
cd "face detect"
python main.py
```

> Press **`s`** to save or any other key to exit.

---

### 2. Real-Time Face Detection on Video — `faceDtectVid/`

Captures a live webcam feed and detects faces in real time, drawing green rectangles around each detected face.

| File | Description |
|------|-------------|
| `main.py` | Opens webcam, runs Haar Cascade face detection frame-by-frame |

**Run:**

```bash
cd faceDtectVid
python main.py
```

> The webcam window opens automatically. Close the window to exit.

---

### 3. Face Recognition (Basic) — `faceDetect/`

A basic face recognition pipeline: train on labeled images, then recognize known faces via webcam in real time using **LBPH (Local Binary Patterns Histograms)**.

| File | Description |
|------|-------------|
| `main.py` | **Training script** — scans `images/` folder, trains the LBPH recognizer, saves model & labels |
| `facesDetect.py` | **Recognition script** — opens webcam, recognizes faces, displays name labels |

**Run:**

```bash
cd faceDetect

# Step 1: Train the model (only needed once, or when you add new images)
python main.py

# Step 2: Run real-time face recognition
python facesDetect.py
```

> Press **`q`** to quit the webcam window.

---

### 4. Face Recognition Suite (Full-Featured) — `faceRecognition/`

A comprehensive computer vision toolkit with face recognition, video filters, AR overlays, recording, and more.

| File | Description |
|------|-------------|
| `faces-train.py` | Trains the LBPH face recognizer on images in `images/` (skips `fun/` and `logo/` folders) |
| `faces.py` | Real-time face recognition via webcam with name labels |
| `base.py` | Basic webcam feed display (camera test) |
| `camera-test.py` | Webcam test with both color and grayscale preview |
| `filter.py` | Applies real-time video filters: sepia, invert, color overlay, hue/saturation, portrait blur |
| `glasses_and_stash.py` | AR overlay — adds glasses & mustache on detected faces in real time |
| `record.py` | Records webcam video to a file |
| `res-change.py` | Demonstrates resolution rescaling on webcam feed |
| `watermark.py` | Watermark utility (see `lessons/`) |
| `timelapse.py` | Timelapse utility (see `lessons/`) |
| `utils.py` | Shared utilities — `image_resize()` helper and `CFEVideoConf` class for video config |

**Run:**

```bash
cd faceRecognition

# Step 1: Train the recognizer (required before running recognition)
python faces-train.py

# Step 2: Real-time face recognition
python faces.py

# Other standalone tools:
python camera-test.py          # Test your webcam
python filter.py               # Real-time video filters
python glasses_and_stash.py    # AR glasses & mustache overlay
python record.py               # Record webcam video
python res-change.py           # Resolution rescaling demo
```

> Press **`q`** to quit any webcam window.

#### Adding New People for Recognition

1. Create a new folder inside `faceRecognition/images/` named after the person (e.g., `images/john-doe/`).
2. Add 5–10 clear face images (`.jpg` or `.png`) to the folder.
3. Re-run the training script:
   ```bash
   python faces-train.py
   ```
4. Start recognition:
   ```bash
   python faces.py
   ```

---

### 5. Interactive Color Detection — `python-project-color-detection/`

Double-click anywhere on an image to identify the **color name** and **RGB values** of that pixel. Uses a dataset of 860+ color names from a CSV file.

| File | Description |
|------|-------------|
| `color_detection.py` | Main script — loads an image, detects color on double-click |
| `colors.csv` | Dataset with 860+ color names mapped to RGB/hex values |
| `colorpic.jpg` | Sample test image |

**Run:**

```bash
cd python-project-color-detection
python color_detection.py -i colorpic.jpg
```

You can use **any image** by passing its path:

```bash
python color_detection.py -i /path/to/your/image.jpg
```

> **Double-click** on a pixel to see its color name and RGB values. Press **`Esc`** to exit.

---

## 🛠️ Prerequisites

### Python Version

- **Python 3.7+** recommended

### Required Libraries

Install all dependencies at once:

```bash
pip install opencv-python opencv-contrib-python numpy Pillow pandas
```

Or install individually:

| Package | Purpose | Install Command |
|---------|---------|-----------------|
| `opencv-python` | Core computer vision functions | `pip install opencv-python` |
| `opencv-contrib-python` | Extra modules (LBPH Face Recognizer) | `pip install opencv-contrib-python` |
| `numpy` | Numerical array operations | `pip install numpy` |
| `Pillow` | Image loading and resizing | `pip install Pillow` |
| `pandas` | CSV reading (color detection) | `pip install pandas` |

### Hardware Requirements

- **Webcam** — required for all real-time detection/recognition projects
- **Display** — GUI windows are used to show results (not headless-compatible)

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/summer-internship-cv-projects.git
cd summer-internship-cv-projects

# 2. (Optional) Create a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install opencv-python opencv-contrib-python numpy Pillow pandas

# 4. Run any project (see individual project instructions above)
```

---

## 🧠 Technologies Used

| Technology | Usage |
|------------|-------|
| **Python 3** | Programming language |
| **OpenCV** | Face detection, recognition, video capture, image processing |
| **Haar Cascades** | Pre-trained XML classifiers for face/eye/smile detection |
| **LBPH Algorithm** | Face recognition (Local Binary Patterns Histograms) |
| **NumPy** | Array manipulation for image data |
| **Pillow (PIL)** | Image loading, format conversion, resizing |
| **Pandas** | CSV parsing for color detection dataset |

---

## 📸 How It Works

### Face Detection Pipeline

```
Image/Frame → Grayscale Conversion → Haar Cascade Detection → Bounding Box Drawing → Display
```

### Face Recognition Pipeline

```
Training:   Images → Grayscale → Face Detection → ROI Extraction → LBPH Training → Model (.yml)
Detection:  Webcam Frame → Grayscale → Face Detection → ROI → LBPH Predict → Display Name
```

### Color Detection Pipeline

```
Image Load → Mouse Double-Click → Get Pixel BGR → Match Closest Color from CSV → Display Name + RGB
```

---

## 📝 Notes

- The **Haar Cascade XML files** are included in the repository (inside `cascades/data/`). OpenCV also bundles them — `cv2.data.haarcascades` provides the default path.
- Trained model files (`.yml`) and label pickles (`.pickle`) are generated by the training scripts. Re-run training if you modify the image dataset.
- Video files (`.mov`, `.mp4`) in `faceDtectVid/` are large — consider adding them to `.gitignore` if pushing to GitHub.

---

## 📄 License

This project is open-source and available for educational purposes.

---

## 🤝 Acknowledgements

- [OpenCV Documentation](https://docs.opencv.org/)
- [Haar Cascade Classifiers](https://github.com/opencv/opencv/tree/master/data/haarcascades)
- Color detection CSV dataset sourced from community resources
