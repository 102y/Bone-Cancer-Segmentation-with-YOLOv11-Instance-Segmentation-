from ultralytics import YOLO

# Load a model
model = YOLO("C://Users//NITRO//Desktop//AI Proj//test//BONE CANCER SEGMENTATION.v1i.yolov11//yolo11n-seg.pt")

# Train the model
train_results = model.train(
    data="C://Users//NITRO//Desktop//AI Proj//test//BONE CANCER SEGMENTATION.v1i.yolov11//data.yaml",  # path to dataset YAML
    epochs=10,  # number of training epochs
    imgsz=640,  # training image size
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

model = YOLO('runs//segment//train//weights//best.pt')
results = model("C://Users//NITRO//Desktop//AI Proj//test//BONE CANCER SEGMENTATION.v1i.yolov11//train//images//C01_png.rf.30b378eb272884b9d8b8a7605a8432b6.jpg", save=True)
results[0].show()

model = YOLO('runs//segment//train//weights//best.pt')
results = model("test_images", save=True)

