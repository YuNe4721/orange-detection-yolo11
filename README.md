# Portakal Tespiti (YOLO11)

Roboflow'dan alınan bir veri setiyle eğittiğim nesne tespiti modeli.

## Veri seti
- Kaynak: https://universe.roboflow.com/fruit-5mit8/orange-kxh32
- Lisans: CC BY 4.0
- 994 görsel, 1 sınıf (portakal)
- Doğrulama seti: 199 görsel, 388 nesne

## Model ve eğitim
- Model: YOLO11n (Ultralytics)
- 30 epoch, görsel boyutu 640
- Ortam: Google Colab, T4 GPU

## Sonuçlar

| Metrik | Değer |
|---|---|
| Precision | 0.93 |
| Recall | 0.91 |
| mAP50 | 0.97 |
| mAP50-95 | 0.92 |

![Tahminler](val_batch0_pred.jpg)
![Eğitim grafikleri](results.png)
![Karışıklık matrisi](confusion_matrix.png)

## Sınırlamalar
- Veri setindeki görseller çoğunlukla net ve sade arka planlı, gerçek ortamda sonuçlar daha düşük olabilir.
- Üst üste duran portakallarda ve yarım dilimlerde güven skorları düşüyor.
- Doğrulama setinde eğitim setine çok benzeyen görseller olabilir, sonuçlar bu yüzden iyimser olabilir.

## Dosyalar
- `Orange.ipynb`: Eğitim kodu (Google Colab'da açılıp çalıştırılabilir)
- `best.pt`: Eğitilmiş model

## Test Seti Sonuçları (Unseen Data)

Modelin eğitim sürecinde hiç görmediği **Test** veri seti üzerindeki performans metrikleri:

| Metrik | Değer |
| :--- | :--- |
| **Precision** | 0.91 |
| **Recall** | 0.89 |
| **mAP50** | 0.94 |
| **mAP50-95** | 0.88 |

### Test Görseli Örnekleri
<img width="640" height="640" alt="000134_jpg rf 249b21b91d1e1f08a87c8e871ec0229a" src="https://github.com/user-attachments/assets/34ba093a-e312-423e-a6f4-ff704320097e" />
<img width="640" height="640" alt="000042_jpg rf 07c6d17ab1c8b8af4d78dce947c323d7" src="https://github.com/user-attachments/assets/d0e51dcc-33a0-4272-8189-a322f01bc47b" />
<img width="640" height="640" alt="000016_jpg rf 283739de221a0bbb165412acf96d7b9d" src="https://github.com/user-attachments/assets/2c20e70c-e23d-4af4-80d4-a9f3bad52f29" />


