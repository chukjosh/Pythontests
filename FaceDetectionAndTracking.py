import cv2

class FaceDetectionAndTracking:
    def __init__(self, tracker_type="KCF"):
        """
        Initializes the FaceDetectionAndTracking system using OpenCV.
        
        Parameters:
        - tracker_type (str): Specifies the type of tracker to use (e.g., 'KCF', 'CSRT', etc.).
        """
        # Initialize face detection using OpenCV Haar Cascade
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Map of available OpenCV trackers
        self.tracker_type = tracker_type
        self.tracker = None
        self.tracking_face = False
        self.tracker_types = {
            "KCF": cv2.legacy.TrackerKCF_create,
            "CSRT": cv2.legacy.TrackerCSRT_create,
            "MIL": cv2.legacy.TrackerMIL_create
        }
        if tracker_type not in self.tracker_types:
            raise ValueError(f"Invalid tracker type: {tracker_type}. Available types: {list(self.tracker_types.keys())}")

    def create_tracker(self):
        """Creates an OpenCV tracker instance based on the specified type."""
        return self.tracker_types[self.tracker_type]()

    def detect_face_in_image(self, image):
        """
        Detects faces in a static image and returns the bounding box of the first face.
        
        Parameters:
        - image (numpy array): The image to detect the face from.

        Returns:
        - bbox (tuple): Bounding box of the detected face (x, y, w, h), or None if no face is detected.
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            return faces[0]  # Return the bounding box of the first detected face
        return None

    def initialize_tracker(self, frame, bbox):
        """Initializes the tracker with the given frame and bounding box."""
        self.tracker = self.create_tracker()
        self.tracker.init(frame, tuple(bbox))
        self.tracking_face = True

    def track_faces_with_webcam(self, image_path="passport.jpg", resize_factor=0.75):
        """
        Tracks faces in real-time using the webcam. Detects a face from an image and tracks it.
        
        Parameters:
        - image_path (str): Path to an image to detect the initial face. If None, the webcam will be used.
        - resize_factor (float): Scale down factor for frames to speed up processing.
        """
        # Load the image or capture from webcam for initial face detection
        if image_path:
            image = cv2.imread(image_path)
            if image is None:
                print("Error: Could not load the image.")
                return
        else:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Error: Could not open webcam.")
                return
            ret, image = cap.read()
            cap.release()

        # Detect face in the static image
        bbox = self.detect_face_in_image(image)
        if bbox is None:
            print("No face detected in the image.")
            return

        # Initialize tracker with the detected face
        self.initialize_tracker(image, bbox)

        # Start real-time tracking from the webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from webcam.")
                break

            # Optionally resize frame for faster processing
            frame = cv2.resize(frame, (int(frame.shape[1] * resize_factor), int(frame.shape[0] * resize_factor)))

            if self.tracking_face:
                success, bbox = self.tracker.update(frame)
                if success:
                    (x, y, w, h) = [int(v) for v in bbox]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                else:
                    print("Tracking failed. Re-detecting face.")
                    self.tracking_face = False
            else:
                bbox = self.detect_face_in_image(frame)
                if bbox is not None:
                    print("Re-detected face, resuming tracking.")
                    self.initialize_tracker(frame, bbox)

            # Display the frame with detected or tracked face
            cv2.imshow('Face Detection and Tracking', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

# Usage Example
face_system = FaceDetectionAndTracking(tracker_type="KCF")
face_system.track_faces_with_webcam()
