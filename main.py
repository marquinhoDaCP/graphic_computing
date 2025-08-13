import cv2

VIDEO_PATH = "./media/race.mp4"
cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
  raise FileNotFoundError(f"Não foi possível localizar o vídeo em: {VIDEO_PATH}")

while True:
  ok, frame = cap.read()
  
  if not ok:
    cap.release()
    raise RuntimeError("Falha ao carregar o frame")
  
  cv2.imshow("Video", frame)
  
  if cv2.waitKey(25) & 0xFF == ord('q'):
    break
  
cap.release()
cv2.waitKey(0)
  