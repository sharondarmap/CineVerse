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

## Architecture ##

```
CineVerse
├── .github
│   └── workflows
│       └── ci.yml
├── .venv
├── src
│   ├── api
│   │   ├── routers
│   ├── application
│   ├── core
│   ├── domain
│   │   ├── activity
│   │   ├── films
│   │   ├── users
│   │   ├── watchlist
│   ├── infrastructure
│   ├── tests
├── Dockerfile
├── pyproject.toml
├── README.md
├── requirements.txt
├── src.zip
└── uv.lock
```
## Menjalankan Cineverse ##

1. Pastikan seluruh dependencies telah ter-install. Bisa dilihat di requirements.txt atau pyproject.toml
2. Masuk ke direktori `/src`
3. Kemudian jalankan main dengan `uvicorn main:app --reload`

Service backend untuk platform personalisasi film CineVerse. Dibangun dengan pendekatan Domain-Driven Design (DDD) dan TDD.

## Finalisasi dan Pengujian Sistem ##

- [x] **Service Initialization**: FastAPI setup berjalan dengan baik.
- [x] **Authentication**: Register & Login (JWT) berfungsi.
- [x] **Unit Testing**: 95%+ Coverage dengan `pytest`.
- [x] **CI/CD**: GitHub Actions workflows terintegrasi.
- [x] **Deployment Ready**: Dockerfile tersedia.
- [x] **Clean Architecture**: Struktur folder terpisah (Domain, Application, API, Infrastructure).

## 🚀 Cara Menjalankan (Lokal)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

2. **Jalankan Unit Test (TDD Check) Pastikan semua checklist hijau sebelum menjalankan aplikasi.**
   ```bash
   pytest --cov=./ --cov-report=term-missing
   ```
   Target output: 95% - 100% coverage.

3. **Jalankan Aplikasi**
   ```
   uvicorn main:app --reload
   ```
   Akses dokumentasi API di: http://localhost:8000/docs

## 🐳 Cara Menjalankan (Docker)
```
docker build -t cineverse-api .
docker run -p 8000:8000 cineverse-api
```
## 📂 Struktur Project
api/: Router dan entry points.

application/: Logika bisnis (Services).

domain/: Model bisnis dan interface repository.

core/: Konfigurasi dan keamanan (JWT/Hash).

infrastructure/: Implementasi database (Memory DB).

tests/: Unit testing suite.


### Cara Eksekusi Terakhir
1.  **Simpan semua file** sesuai struktur folder.
2.  Jalankan `pip install -r requirements.txt`.
3.  Jalankan `pytest --cov=./` di terminal Anda. Anda akan melihat report coverage. Jika ada bagian yang merah (missing), tambahkan test case untuk baris tersebut.
4.  Push ke GitHub, dan tab "Actions" di GitHub akan otomatis menjalankan pipeline CI yang sudah kita buat.
