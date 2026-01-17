# -*- coding: utf-8 -*-
"""
元のarchiveデータが非常に大きいので、yolo用に128*128にリサイズします。


"""
from PIL import Image
import os

# 入力・出力フォルダ
INPUT_DIR = "archive"
OUTPUT_DIR = "dataset"

try:
    shutil.rmtree("dataset")
except:
    pass

# 対象とする画像拡張子
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

# 出力先のベースフォルダを作成
os.makedirs(OUTPUT_DIR, exist_ok=True)

total = 0
done = 0

# まず総数を数える（進捗表示用）
for root, _, files in os.walk(INPUT_DIR):
    for file in files:
        if file.lower().endswith(IMAGE_EXTENSIONS):
            total += 1

# 画像処理
for root, _, files in os.walk(INPUT_DIR):
    for file in files:
        if not file.lower().endswith(IMAGE_EXTENSIONS):
            continue

        input_path = os.path.join(root, file)

        # archive からの相対パスを取得
        relative_path = os.path.relpath(input_path, INPUT_DIR)
        output_path = os.path.join(OUTPUT_DIR, relative_path)

        # 出力先フォルダを作成
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        try:
            with Image.open(input_path) as img:
                # 128x128 にリサイズ（縦横比は無視）
                img_resized = img.resize((128, 128), Image.LANCZOS)
                img_resized.save(output_path)

            done += 1
            print(f"[{done}/{total}] saved: {output_path}")

        except Exception as e:
            print(f"ERROR: {input_path} -> {e}")

print("すべて完了しました")
