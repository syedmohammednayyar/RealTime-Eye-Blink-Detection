# RealTime-Eye-Blink-Detection

A real-time eye blink detection system that uses computer vision techniques to detect and count human eye blinks. The project is suitable for applications such as fatigue detection, attention monitoring, and human–computer interaction research or prototypes.

## Project Overview

This repository contains a Python-based system that detects eye blinks from live video (webcam) or pre-recorded video. It uses classical computer-vision techniques (facial landmark detection, Eye Aspect Ratio) and OpenCV for real-time processing. The implementation is oriented toward clarity and extensibility, making it suitable for demos, prototypes, and portfolio projects.

## Features

- Real-time blink detection from webcam or video file
- Blink counting and simple visualization overlay (blink count, EAR indicator)
- Lightweight implementation using facial landmarks (no heavy deep-learning model required)
- Easily extensible thresholds and parameters for tuning sensitivity

## Technologies Used

- Python 3.8+
- OpenCV (`opencv-python`)
- dlib (facial landmark detection) or compatible landmark detector
- NumPy
- Optional: `imutils` for convenience utilities

## Installation Instructions

1. Clone the repository:

```bash
git clone https://github.com/syedmohammednayyar/RealTime-Eye-Blink-Detection.git
cd RealTime-Eye-Blink-Detection
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install opencv-python numpy dlib imutils
```

Note: Installing `dlib` may require CMake and a C++ build toolchain. On Windows, use a wheel if available or follow dlib installation instructions for your platform.

4. Place the facial landmark model in `shape_predictor_model/` (if required):

 - If your implementation uses dlib's 68-point predictor, download `shape_predictor_68_face_landmarks.dat` and place it into the `shape_predictor_model/` folder.

## How to Run the Project

Run the provided entry script. Examples:

```bash
# Run webcam live detection
python run_blink_detection.py

# Or run the core script directly
python blink_detection.py
```

If the scripts accept arguments (e.g., video file path, model path, or threshold values), run `python run_blink_detection.py --help` to view available options.

## Folder Structure

- `blink_detection.py` - Core blink detection logic (EAR calculation, landmark processing).
- `run_blink_detection.py` - Entry point for running the real-time detection (webcam/video wrapper).
- `shape_predictor_model/` - Directory for facial landmark model files (e.g., `shape_predictor_68_face_landmarks.dat`).
- `README.md` - Project documentation (this file).

Adjust names above if your local files differ; the structure lists the primary files included in this repository.

## Usage Instructions

1. Ensure dependencies are installed and the landmark model (if required) is available in `shape_predictor_model/`.
2. Start the script with your preferred input source (default is webcam).
3. Monitor the overlay in the displayed video window. The program typically shows:
	- Current Eye Aspect Ratio (EAR)
	- Blink count
	- A visual indicator (rectangle/marker) around detected eyes
4. To stop the program, press the configured quit key (usually `q` or `ESC`).

## Example Output (description only)

When running, the application opens a live video window that overlays real-time metrics: the current EAR is shown near the face, a running blink count is displayed in the corner, and brief on-screen text notifies when a blink is detected. The output is intended for quick visual verification rather than polished UI screenshots.

## Future Enhancements

- Add configurable command-line arguments for thresholds and input sources
- Provide support for multiple face tracking and per-subject blink statistics
- Replace or augment landmark detector with a lightweight neural model for increased robustness
- Add data logging and export (CSV/json) for post-processing and analysis
- Add unit tests and CI workflow for reproducibility

## Contributing

Contributions are welcome. Open an issue to discuss proposed changes, then submit a pull request with a clear description of the change. Please follow standard GitHub forking and PR workflow.

## License

This project is provided under the MIT License. See the `LICENSE` file for details. If you prefer a different license for your repository, replace this section with the appropriate license text and include a `LICENSE` file.

## Contact

For questions or collaboration, open an issue or contact the repository owner https://www.linkedin.com/in/syedmohammednayyar/.

---

Thank you for using RealTime-Eye-Blink-Detection — designed for clarity, extendibility, and real-time performance testing.
