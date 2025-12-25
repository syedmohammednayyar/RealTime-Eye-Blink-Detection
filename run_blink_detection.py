import cv2
import dlib
import blink_detection

# Initialize face detector
detector = dlib.get_frontal_face_detector()

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, frame = cap.read()
    if not ret:
        break
        
    # Convert to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = detector(gray)
    
    # Check for blinks
    if faces:
        ratio = blink_detection.isBlinking(faces, gray)
        # Display the ratio information
        if ratio:
            cv2.putText(frame, f"L: {ratio[0]:.2f}, R: {ratio[1]:.2f}, Status: {ratio[2]}", 
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # Display the frame
    cv2.imshow('Blink Detection', frame)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()