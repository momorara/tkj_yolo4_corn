import os
import shutil

# 入力・出力フォルダ
INPUT_DIR = "dataset_j"
OUTPUT_DIR = "dataset_jn"

try:
    shutil.rmtree("dataset_jn")
except:
    pass

# 対象とする画像拡張子
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# フォルダごとに処理
for root, dirs, files in os.walk(INPUT_DIR):
    # 入力フォルダからの相対パス
    rel_dir = os.path.relpath(root, INPUT_DIR)
    output_dir = os.path.join(OUTPUT_DIR, rel_dir)

    os.makedirs(output_dir, exist_ok=True)

    # 画像ファイルのみ抽出・ソート
    images = sorted(
        [f for f in files if f.lower().endswith(IMAGE_EXTENSIONS)]
    )

    counter = 1
    for file in images:
        src_path = os.path.join(root, file)

        ext = os.path.splitext(file)[1].lower()
        new_name = f"{counter:04d}{ext}"  # 0001.jpg 形式
        dst_path = os.path.join(output_dir, new_name)

        shutil.copy2(src_path, dst_path)
        counter += 1

    if images:
        print(f"{rel_dir} : {len(images)} files processed")

print("すべて完了しました")
