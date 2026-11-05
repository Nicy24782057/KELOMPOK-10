from datetime import datetime
from pathlib import Path
import hashlib
import sys
import traceback

ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = ROOT / "evidence" / "S02" / "lingkungan-ai.txt"
WEIGHTS_PATH = ROOT / "models" / "yolo11s.pt"

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
WEIGHTS_PATH.parent.mkdir(parents=True, exist_ok=True)


def catat(teks):
    print(teks, flush=True)
    with LOG_PATH.open("a", encoding="utf-8") as log:
        log.write(teks + "\n")


catat("\n" + "=" * 60)
catat("S02 / W04-T02 - Pemeriksaan kandidat YOLO11s")
catat("Mulai: " + datetime.now().astimezone().isoformat())

try:
    if sys.prefix == sys.base_prefix:
        raise RuntimeError("Jalankan dengan Python dari .venv proyek.")

    import cv2
    import torch
    import torchvision
    import ultralytics
    from ultralytics import YOLO

    catat("Python: " + sys.version.replace("\n", " "))
    catat("Interpreter: " + sys.executable)
    catat("Virtualenv: True")
    catat("Torch: " + torch.__version__)
    catat("Torchvision: " + torchvision.__version__)
    catat("OpenCV: " + cv2.__version__)
    catat("Ultralytics: " + ultralytics.__version__)
    catat("CUDA tersedia: " + str(torch.cuda.is_available()))
    catat("Bobot: " + str(WEIGHTS_PATH))

    model = YOLO(str(WEIGHTS_PATH))
    model.to("cpu")
    target_names = {"car", "motorcycle", "bus", "truck"}
    classes = {
        class_id: name
        for class_id, name in model.names.items()
        if name in target_names
    }

    if model.task != "detect" or set(classes.values()) != target_names:
        raise RuntimeError("Tugas model atau empat kelas kendaraan tidak sesuai.")

    catat("Tugas model: " + model.task)
    catat("Perangkat model: " + str(model.device))
    catat("Kelas kendaraan: " + str(classes))
    catat("SHA256: " + hashlib.sha256(WEIGHTS_PATH.read_bytes()).hexdigest())
    catat("Status pemilihan: kandidat_awal")
    catat("STATUS: PEMUATAN YOLO11s BERHASIL")

except Exception:
    catat("STATUS: PEMERIKSAAN GAGAL")
    catat(traceback.format_exc())
    raise SystemExit(1)

catat("Selesai: " + datetime.now().astimezone().isoformat())
catat("Lokasi log: " + str(LOG_PATH))
