import os
import time
from datetime import datetime

# URL dasar situs GitHub Pages Anda
BASE_URL = "https://indonewsupdate.github.io"

# Folder tempat artikel disimpan (ubah jika berbeda)
CONTENT_DIR = "."

# Template dasar sitemap
SITEMAP_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{}
</urlset>
"""

# Fungsi untuk membuat entri sitemap berdasarkan file yang ada
def generate_sitemap():
    url_entries = []
    
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".html") and file not in ["index.html", "404.html"]:  # Hindari 404.html
                file_path = os.path.relpath(os.path.join(root, file), CONTENT_DIR)
                file_url = f"{BASE_URL}/{file_path.replace(os.sep, '/')}"
                
                # Ambil waktu modifikasi terakhir dari file
                lastmod_unix = os.path.getmtime(os.path.join(root, file))
                lastmod = datetime.utcfromtimestamp(lastmod_unix).strftime("%Y-%m-%dT%H:%M:%S+00:00")
                
                url_entry = f"""  <url>
    <loc>{file_url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.7</priority>
  </url>"""
                
                url_entries.append(url_entry)
    
    sitemap_content = SITEMAP_TEMPLATE.format("\n".join(url_entries))
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    print("✅ Sitemap berhasil diperbarui!")

if __name__ == "__main__":
    generate_sitemap()
