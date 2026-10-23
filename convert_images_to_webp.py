#!/usr/bin/env python3
import os
import re
from pathlib import Path
from PIL import Image

# Extensions to convert
TARGET_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tiff", ".bmp"}

# Folders to ignore during scanning
EXCLUDE_DIRS = {".git", "_site", "node_modules", ".jekyll-cache", "venv"}

# Set to True if you want to automatically delete original files after successful conversion
DELETE_ORIGINALS = True

# Set to True to search Markdown and HTML files to replace references (e.g. .jpg -> .webp)
UPDATE_MARKDOWN_REFS = True
POSTS_EXTENSIONS = {".md", ".markdown", ".html"}


def convert_image(file_path: Path, quality: int = 80) -> Path | None:
    """Converts a single image file to WebP."""
    webp_path = file_path.with_suffix(".webp")
    
    # Avoid overwriting or redundant work if identical path
    if file_path.suffix.lower() == ".webp":
        return None

    try:
        with Image.open(file_path) as img:
            # Preserve transparency if present, otherwise ensure RGB
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                converted_img = img.convert("RGBA")
            else:
                converted_img = img.convert("RGB")

            converted_img.save(webp_path, "WEBP", quality=quality, method=6)
            print(f"[CONVERTED] {file_path} -> {webp_path.name}")
            return webp_path
    except Exception as e:
        print(f"[ERROR] Failed to convert {file_path}: {e}")
        return None


def update_references(repo_root: Path, mapping: dict[str, str]):
    """Replaces old image file references in posts and pages with new .webp paths."""
    if not mapping:
        return

    print("\nUpdating post references...")
    pattern = re.compile(
        r"\b(" + "|".join(re.escape(k) for k in mapping.keys()) + r")\b"
    )

    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            path = Path(root) / file
            if path.suffix.lower() in POSTS_EXTENSIONS:
                try:
                    content = path.read_text(encoding="utf-8")
                    new_content, count = pattern.subn(
                        lambda m: mapping[m.group(0)], content
                    )
                    if count > 0:
                        path.write_text(new_content, encoding="utf-8")
                        print(f"[UPDATED] {path} ({count} replacement{'s' if count > 1 else ''})")
                except Exception as e:
                    print(f"[WARN] Could not update {path}: {e}")


def main():
    repo_root = Path(__file__).resolve().parent
    name_mapping = {}
    converted_count = 0

    print(f"Scanning repository from: {repo_root}\n")

    for root, dirs, files in os.walk(repo_root):
        # Exclude internal / build directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in TARGET_EXTENSIONS:
                result = convert_image(file_path)
                if result:
                    name_mapping[file_path.name] = result.name
                    converted_count += 1
                    
                    if DELETE_ORIGINALS:
                        try:
                            file_path.unlink()
                            print(f"[REMOVED] Original file: {file_path}")
                        except OSError as e:
                            print(f"[WARN] Failed to delete {file_path}: {e}")

    print(f"\nDone. Successfully converted {converted_count} image(s).")

    if UPDATE_MARKDOWN_REFS and name_mapping:
        update_references(repo_root, name_mapping)


if __name__ == "__main__":
    main()
