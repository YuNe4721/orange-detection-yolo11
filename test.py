from ultralytics import YOLO

# Eğitilmiş modeli yükle
model = YOLO("best.pt")

# Test seti üzerinde metrikleri (Precision, Recall, mAP) hesapla
metrics = model.val(data="orange-1/data.yaml", split="test")

# Test görselleri üzerinde tahmin yap ve kaydet
model.predict(source="orange-1/test/images", save=True)
