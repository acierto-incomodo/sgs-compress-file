import os
import sys
import zipfile
import math

CHUNK_SIZE = 5 * 1024 * 1024  # 5MB

# -----------------------------
# ZIP CREATION
# -----------------------------
def create_zip(source, temp_zip):
    with zipfile.ZipFile(temp_zip, "w", zipfile.ZIP_DEFLATED) as z:
        if os.path.isfile(source):
            z.write(source, os.path.basename(source))
        else:
            for root, _, files in os.walk(source):
                for f in files:
                    full = os.path.join(root, f)
                    rel = os.path.relpath(full, source)
                    z.write(full, rel)

# -----------------------------
# SPLIT FILES (.001 .002 ...)
# -----------------------------
def split_file(file_path, output_dir, base_name):
    size = os.path.getsize(file_path)
    parts = math.ceil(size / CHUNK_SIZE)

    with open(file_path, "rb") as f:
        for i in range(parts):
            chunk = f.read(CHUNK_SIZE)
            out_file = os.path.join(output_dir, f"{base_name}.sgs.{i+1:03d}")
            with open(out_file, "wb") as o:
                o.write(chunk)

    return parts

# -----------------------------
# JOIN SPLIT FILES
# -----------------------------
def join_files(first_part, output_file):
    base = first_part[:-4]  # remove .001
    i = 1

    with open(output_file, "wb") as out:
        while True:
            part = f"{base}.{i:03d}"
            if not os.path.exists(part):
                break
            with open(part, "rb") as p:
                out.write(p.read())
            i += 1

# -----------------------------
# COMPRESS
# -----------------------------
def compress(path, out_dir=None, name=None, split=False):
    if not out_dir:
        out_dir = os.path.dirname(path)
    if not name:
        name = os.path.basename(path)

    temp_zip = os.path.join(out_dir, "__temp.sgszip")

    create_zip(path, temp_zip)

    if split:
        parts = split_file(temp_zip, out_dir, name)
        os.remove(temp_zip)
        return f"split:{parts}"

    final = os.path.join(out_dir, name + ".sgs-compressed-file")
    os.rename(temp_zip, final)
    return final

# -----------------------------
# DECOMPRESS
# -----------------------------
def decompress(path, out_dir=None):
    if not out_dir:
        out_dir = os.path.dirname(path)

    # SPLIT MODE
    if path.endswith(".001"):
        temp_zip = os.path.join(out_dir, "__rebuild.zip")
        join_files(path, temp_zip)

        with zipfile.ZipFile(temp_zip, "r") as z:
            z.extractall(out_dir)

        os.remove(temp_zip)
        return out_dir

    # NORMAL MODE
    with zipfile.ZipFile(path, "r") as z:
        z.extractall(out_dir)

    return out_dir

# -----------------------------
# CLI (7zr style)
# -----------------------------
if __name__ == "__main__":
    cmd = sys.argv[1]

    if cmd == "c":
        path = sys.argv[2]
        out = sys.argv[3] if len(sys.argv) > 3 else None
        name = sys.argv[4] if len(sys.argv) > 4 else None
        split = "--split" in sys.argv

        print(compress(path, out, name, split))

    elif cmd == "x":
        path = sys.argv[2]
        out = sys.argv[3] if len(sys.argv) > 3 else None

        print(decompress(path, out))

    else:
        print("Commands: c | x")