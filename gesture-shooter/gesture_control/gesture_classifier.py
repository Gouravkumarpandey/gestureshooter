def classify_gesture(landmarks):
    if not landmarks:
        return "UNKNOWN"

    wrist = landmarks[0]
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    # POINT: Index up, others down
    if (index_tip[1] < wrist[1] and
        middle_tip[1] > wrist[1] and
        ring_tip[1] > wrist[1] and
        pinky_tip[1] > wrist[1]):
        return "POINT"

    # BACK: Thumb out to side, index + middle down
    if (thumb_tip[0] < wrist[0] and
        index_tip[1] > wrist[1] and
        middle_tip[1] > wrist[1]):
        return "BACK"

    # SHOOT: Index and pinky up, middle and ring down
    if (index_tip[1] < wrist[1] and
        pinky_tip[1] < wrist[1] and
        middle_tip[1] > wrist[1] and
        ring_tip[1] > wrist[1]):
        return "SHOOT"

    # Default
    return "PALM"
