import cv2
import os

# --- Configuration ---
# You need to replace this with the path to your downloaded Solitaire video file
VIDEO_PATH = "solitaire_gameplay.mp4" 

# The name of the folder where the extracted images will be saved
OUTPUT_DIR = "./resources/contextual_dataset" 

# Only save a frame every N frames (e.g., 100 means 1 frame saved for every 100 frames)
# Adjust this value based on your video length and desired dataset size.
FRAME_SKIP_RATE = 100 
# ---------------------

def extract_frames(video_path, output_dir, frame_skip):
    """
    Reads a video file and saves frames to a directory based on a skip rate.
    
    Args:
        video_path (str): Path to the source video file.
        output_dir (str): Directory where images will be saved.
        frame_skip (int): Number of frames to skip between saves.
    """
    
    # 1. Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # 2. Open the video file
    vidcap = cv2.VideoCapture(video_path)
    if not vidcap.isOpened():
        print(f"Error: Could not open video file at {video_path}. Check the path.")
        return

    # Get video properties (optional, for info)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video loaded. FPS: {fps}, Total Frames: {frame_count}")

    count = 0
    saved_count = 0
    
    # 3. Process video frames
    while True:
        # Read the next frame
        success, image = vidcap.read()
        
        # Break the loop if reading failed (end of video)
        if not success:
            break

        # Check if the current frame should be saved based on the skip rate
        if count % frame_skip == 0:
            # Generate a unique filename
            filename = os.path.join(output_dir, f"frame_{count:06d}.jpg")
            
            # Save the frame as a JPEG image
            cv2.imwrite(filename, image)
            saved_count += 1
            
            # Print progress every 100 saved frames
            if saved_count % 100 == 0:
                print(f"Status: Saved {saved_count} frames so far...")

        count += 1

    # 4. Cleanup and summary
    vidcap.release()
    print(f"\n--- Extraction Complete ---")
    print(f"Total frames processed: {count}")
    print(f"Total images saved to '{output_dir}': {saved_count}")

# Execute the function
extract_frames(VIDEO_PATH, OUTPUT_DIR, FRAME_SKIP_RATE)