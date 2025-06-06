# Gesture-Controlled Hill Climbing Racing 
### Play Hill Climbing Racing Using Hand Gestures

Turn your hand into a natural game controller! This project lets you play Hill Climbing Racing using intuitive hand gestures captured through your webcam. Using MediaPipe's advanced hand tracking technology, it converts your hand movements into game controls, creating an immersive and unique gaming experience.

![Hand Gesture Control Demo](./docs/images/demo.gif)

## 🎮 How It Works

A webcam captures your hand movements in real-time, processing them through MediaPipe's hand tracking system. The detected gestures are converted into keyboard inputs that control your vehicle in Hill Climbing Racing. A visual feedback window shows your hand tracking while you play.

## ✨ Key Features

### 🖐️ Gesture Recognition System
- **Real-time Hand Tracking**
  - Powered by MediaPipe Hands for precise landmark detection
  - 21-point hand landmark tracking
  - Real-time visualization of hand position and movements
  - Optimized for low latency gaming response

### 🎯 Intuitive Controls
- **Simple Two-Gesture System**
  1. **Pointing Gesture (🫵)**
     - Action: Accelerate
     - Effect: Holds down right arrow key
     - Use for: Moving forward, climbing hills
  
  2. **Palm Gesture (✋)**
     - Action: Stop & Balance
     - Effect: Releases gas, taps down arrow
     - Use for: Preventing flips, controlling descent

  3. **No Gesture**
     - Action: Complete stop
     - Effect: Releases all controls
     - Use for: Precise control and resets

### 🛠️ Technical Features
- **Responsive Control System**
  - 0.3-second cooldown for smooth gameplay
  - State tracking for consistent acceleration
  - Auto-balance assistance
  - Automatic control release safety

- **Performance Optimizations**
  - Efficient gesture detection algorithms
  - Minimal input lag
  - Memory-efficient processing
  - CPU-friendly implementation

## 🚀 Getting Started

### Prerequisites
- Windows 10/11
- Python 3.7 or higher
- Webcam (built-in or external)
- Hill Climbing Racing game installed
- Basic Python knowledge

### Required Packages
```bash
opencv-python    # Computer vision and webcam interface
mediapipe       # Hand tracking and gesture detection
pyautogui       # Game control simulation
pynput          # Keyboard input handling
```

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/gesture-hill-climbing.git
   cd gesture-hill-climbing
   ```

2. **Set Up Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage Guide

1. **Launch the Game**
   - Start Hill Climbing Racing
   - Position the game window where you want it

2. **Start the Controller**
   ```bash
   python main.py
   ```

3. **Position Your Hand**
   - Keep your hand within camera view
   - Maintain good lighting
   - Position 20-40cm from camera

4. **Basic Controls**
   - Point forward (🫵) -> Accelerate
   - Show palm (✋) -> Stop & balance
   - Move hand away -> Complete stop

## 💡 Pro Tips

### For Better Control
- Make clear, distinct gestures
- Keep consistent distance from camera
- Use palm gesture early when tipping
- Practice timing for better balance
- Find comfortable hand position

### Common Issues
- **If gestures aren't detecting:**
  - Check lighting conditions
  - Adjust hand distance from camera
  - Ensure clear background
  - Verify webcam permissions

- **If controls feel laggy:**
  - Close background applications
  - Check CPU usage
  - Reduce webcam resolution if needed
  - Verify game is running smoothly

## 🔧 Configuration

Edit `config.py` to customize:
```python
COOLDOWN_TIME = 0.3        # Adjust control responsiveness
CAMERA_INDEX = 0           # Change webcam source
CONFIDENCE_THRESHOLD = 0.7 # Adjust gesture detection sensitivity
```

