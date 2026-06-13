# 🎮 Tetris

Python ve Pygame ile geliştirilmiş klasik Tetris oyunu.

## Özellikler

- 7 farklı Tetris parçası (I, O, T, L, J, S, Z)
- Özel blok görselleri (assets klasöründen yüklenir)
- Skor sistemi (her tamamlanan satır 100 puan)
- Izgara tabanlı oyun alanı (10x20)

## Kurulum

### Gereksinimler

- Python 3.x
- Pygame

### Pygame Kurulumu

```bash
pip install pygame
```

### Oyunu Çalıştırma

```bash
python main.py
```

## Kontroller

| Tuş | İşlev |
|-----|-------|
| ← Sol ok | Bloğu sola hareket ettir |
| → Sağ ok | Bloğu sağa hareket ettir |
| ↓ Aşağı ok | Bloğu hızlı indir |
| ↑ Yukarı ok | Bloğu döndür |

## Proje Yapısı

```
tetris/
├── main.py
└── assets/
    └── blocks/
        ├── I.png
        ├── kare.png
        ├── L.png
        ├── tersL.png
        ├── tersT.png
        ├── yatay.png
        └── z.png
```

## Geliştirici

**ilaydacort** — kapsamında geliştirilmiştir.
