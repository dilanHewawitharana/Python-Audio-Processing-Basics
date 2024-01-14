import cv2

print("Package imported")

# Video read
cap = cv2.VideoCapture('video/IMG_1331.MOV')

# Get the frames per second (fps) of the video
fps = cap.get(cv2.CAP_PROP_FPS)

while True:
    success, img = cap.read()
    
    # Check if the video has reached the end
    if not success:
        break

    # Get the height and width of the original frame
    height, width, _ = img.shape

    # Define the cropping percentages
    top_percentage = 0.40  # 55% from the top
    left_percentage = 0.30  # 30% from left

    # Calculate the cropping dimensions
    top_crop = int(height * top_percentage)
    left_crop = int(width * left_percentage)

    # Crop the frame
    img_cropped = img[top_crop:, left_crop:, :]

    # Draw a black box on the cropped image
    box_width = int(0.5 * img_cropped.shape[1])  # 50% of the cropped image width
    box_height = int(0.25 * img_cropped.shape[0])  # 25% of the cropped image height

    # Coordinates for the top-left corner of the black box
    box_start_x = 0
    box_start_y = 0

    # Coordinates for the bottom-right corner of the black box
    box_end_x = box_start_x + box_width
    box_end_y = box_start_y + box_height

    # Draw the black box
    cv2.rectangle(img_cropped, (box_start_x, box_start_y), (box_end_x, box_end_y), (0, 0, 0), -1)

    # Display the cropped image with the black box
    cv2.imshow('Cropped Video with Black Box', img_cropped)

    # Calculate the delay based on the original frame rate
    delay = int(1000 / fps)  # Delay in milliseconds

    # Wait for a key event or delay, break the loop if 'q' is pressed
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()