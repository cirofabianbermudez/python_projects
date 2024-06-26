import pyautogui
import shutil
import time
import os

def main():

    # Define the region you want to capture (left, top, width, height)
    region = (735+8, 0+8, 1060, 1371)  # Example region, adjust as needed

    # Delete de old directory if exist
    images_dir = os.path.join("..", "images")
    if os.path.exists(images_dir):
        shutil.rmtree(images_dir)
    
    # Create the captures directory
    os.makedirs(images_dir)

    # Delay to give you time to setup the screen
    time.sleep(5)

    # Repeat the process 130 times
    for _ in range(5):
        # Take a screenshot of the specified region
        screenshot = pyautogui.screenshot(region=region)

        # Save the screenshot with a unique name (you can adjust this as needed)
        filename = os.path.join(images_dir, f"page_{_+1}.png")
        screenshot.save(filename)

        # Press the right arrow key
        pyautogui.press('right')

        # Add a short delay to make sure the key press is registered
        time.sleep(1.0)

    print("> DONE")

if __name__ == "__main__":
    main()
