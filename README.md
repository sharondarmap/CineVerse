# 🎬 CineVerse API – Domain-Driven Design + JWT Authentication

![CI Pipeline](https://github.com/sharondarmap/CineVerse/actions/workflows/ci-pipeline.yml/badge.svg)

CineVerse API adalah implementasi awal dari beberapa bounded context utama:  
**Identity**, **Film Catalog**, dan **Journaling Context**, berdasarkan desain Domain-Driven Design (DDD).

API menyediakan fitur:

- Registrasi dan Login User  
- Pengelolaan Film  
- FilmActivity (menonton film, log aktivitas, review)  
- Watchlist  
- Sistem Autentikasi Sederhana menggunakan JWT  
- Struktur proyek mengikuti DDD (Domain, Application, Infrastructure, API)

## Menjalankan Cineverse ##

1. Pastikan seluruh dependencies telah ter-install. Bisa dilihat di requirements.txt atau pyproject.toml
2. Masuk ke direktori `/src`
3. Kemudian jalankan main dengan `uvicorn main:app --reload`
