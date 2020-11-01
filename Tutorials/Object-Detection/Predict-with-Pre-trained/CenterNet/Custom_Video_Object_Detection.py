from xtreme_vision.Detection import Object_Detection
from PIL import Image

model = Object_Detection()
model.Use_CenterNet()
custom_obj = model.Custom_Objects(car=True)
model.Detect_Custom_Objects_From_Video(custom_obj, 
                                       input_path = 'road.mp4',
                                       output_path = './custom_video.mp4')