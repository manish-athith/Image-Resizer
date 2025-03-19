import cv2

# Load the image
src = cv2.imread("C:\\Users\\MANISH CHOUDHARY\\Desktop\\Python Projects\\Image Resizer\\choudhary.jpg", cv2.IMREAD_UNCHANGED)

# Verify if the image was loaded
if src is None:
    print("Error: Image not found or could not be loaded. Check the file path.")
else:
    # Proceed with resizing
    scale_percent = 50  # Resize percentage
    # cv2.imshow("title", src)
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    # Take user input for custom dimensions
    new_height = int(input("Enter new height: "))
    new_width = int(input("Enter new width: "))

    output = cv2.resize(src, (new_width, new_height))

    # Save the new image
output_path = "C:\\Users\\MANISH CHOUDHARY\\Desktop\\Python Projects\\Image Resizer\\newimage.jpg"
cv2.imwrite(output_path, output)
print(f"Resized image saved at: {output_path}")

