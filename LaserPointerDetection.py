import cv2
import numpy as np

# Define color range for detecting red laser in HSV
# You may need to fine-tune these values for specific laser pointers
lower_red = np.array([160, 100, 100])
upper_red = np.array([180, 255, 255])

# Focal length and real-world size of laser pointer spot for distance estimation
# These values require calibration for accuracy
focal_length = 600  # example focal length in pixels, adjust as necessary
real_laser_size = 0.5  # assumed size of laser dot in cm

# Distance tolerance in centimeters
distance_tolerance = 10

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask to isolate the red color (laser)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Optional: Apply morphological operations to reduce noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Find contours of the laser dot
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find the largest contour assuming it's the laser dot
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Get the bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Calculate the center of the laser dot
        center_x, center_y = x + w // 2, y + h // 2
        
        # Draw a circle around the laser dot
        cv2.circle(frame, (center_x, center_y), 10, (0, 255, 0), 2)
        
        # Estimate the distance based on the dot size (approximate method)
        perceived_size = max(w, h)
        if perceived_size > 0:
            distance = (real_laser_size * focal_length) / perceived_size
            
            # Display distance and tolerance check
            cv2.putText(frame, f"Distance: {distance:.2f} cm", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            # Check if the distance is within the required range
            if abs(distance - 200) <= distance_tolerance:
                cv2.putText(frame, "Laser within 2m +/- 10cm", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Laser out of range", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
    # Display the frame with laser detection and distance information
    cv2.imshow("Laser Pointer Detection", frame)
    
    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
