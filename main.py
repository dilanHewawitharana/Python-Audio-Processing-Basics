import os
import cv2
import time

def main():
    video_path = "video/dilan.MOV"
    output_folder = "short_video_clips"  # Specify the folder where you want to save short video clips

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Unable to open video file at {video_path}")
        return
    else:
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration_frames = int(cap.get(cv2.CAP_PROP_FPS))
        print(f"Total frames in the video: {total_frames}")

    space_records = []

    print("Press the space bar to mark specific places in the video and 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video.")
            break

        cv2.imshow("Video Player", frame)

        key = cv2.waitKey(1)

        if key == ord(' '):
            current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            space_records.append(current_frame)
            print(f"Space bar pressed at frame {current_frame}.")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    short_video_clips_frames = []
    for frame_num in space_records:
        start_frame = max(0, frame_num - duration_frames // 2)
        print(f"start_frame: {start_frame}  duration_frames: {duration_frames} total_frames: {total_frames}")
        end_frame = min(total_frames - 1, start_frame + duration_frames - 1)
        short_video_clips_frames.append((start_frame, end_frame))

    # At this point, you have both space_records and short_video_clips_frames lists.
    # Now, you can use these lists to create short video clips.

    # For each clip frame range, create a short video clip
    for idx, (start_frame, end_frame) in enumerate(short_video_clips_frames):
        print(f"Creating short video clip {idx+1}: Start Frame - {start_frame}, End Frame - {end_frame}")

        # Set the video capture back to the beginning
        cap = cv2.VideoCapture(video_path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        # Create a VideoWriter object for the short video clip
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can adjust the codec based on your needs
        clip_width, clip_height = int(cap.get(3)), int(cap.get(4))
        clip_writer = cv2.VideoWriter(os.path.join(output_folder, f"short_clip_{idx+1}.mp4"), fourcc, cap.get(cv2.CAP_PROP_FPS), (clip_width, clip_height))

        # Read frames and write to the short video clip
        for frame_num in range(start_frame, end_frame + 1):
            ret, frame = cap.read()
            if not ret:
                break
            clip_writer.write(frame)

        clip_writer.release()

    cap.release()

if __name__ == "__main__":
    main()
