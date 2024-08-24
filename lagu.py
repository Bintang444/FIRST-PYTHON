import time

def print_lyrics():
    lines = [
        ("Tiba-tiba aku jatuh cinta", 0.1),
        ("Diam-diam kau pun juga cinta", 0.1),
        ("Kita berdua belum punya kekasih", 0.11),
        ("Saling mendekati", 0.1),

        ("Perasaan tak bisa berdusta", 0.11),
        ("Bahagia terasa sempurna", 0.11),
        ("Kita berdua belum punya kekasih", 0.11),
        ("Tunggu apa lagi", 0.14),

        ("Katakan cinta bila kau cinta", 0.12),
        ("Hati ini meminta", 0.12),
        ("Kau lebih dari teman berbagi", 0.12),
        ("Jadi kekasihku saja", 0.12),

        ("Perasaan tak bisa berdusta", 0.12),
        ("Bahagia terasa sempurna", 0.12),
        ("Kita berdua belum punya kekasih", 0.12),
        ("Tunggu apalagi", 0.12),

        ("Katakan cinta bila kau cinta", 0.12),
        ("Hati ini meminta", 0.13),
        ("Kau lebih dari teman berbagi", 0.14),
        ("Jadi kekasihku saja", 0.12),

        ("Cinta katakan cinta", 0.12),
        ("Hati ini meminta", 0.12),
        ("Kau lebih dari teman berbagi", 0.17),
        ("Jadilah kekasihku", 0.11),

        ("Katakan (Cinta bila kau cinta) cinta", 0.12),
        ("Hati ini meminta", 0.13),
        ("Kau lebih dari teman berbagi", 0.12),
        ("Jadi kekasihku saja", 0.12),

        ("Cinta katakan cinta", 0.12),
        ("Hati ini meminta", 0.18),
        ("Kau lebih dari teman berbagi", 0.17),
        ("Jadi kekasihku saja", 0.15),

        ("Jadi kekasihku saja", 0.15),
        ("Jadi kekasihku saja", 0.14),
    ]

    delays = [
        0.6, 0.6, 0.5, 1.6,
        0.6, 0.7, 0.7, 1.4,
        0.7, 0.5, 0.5, 3.6,
        0.5, 0.6, 0.6, 0.6,
        0.8, 0.9, 0.9, 0.8,
        0.8, 0.9, 0.9, 16.0,
        1.4, 0.9, 0.9, 0.8,
        0.8, 0.6, 0.5, 0.5,
        0.6, 5.0,
    ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        time.sleep(delays[i % len(delays)])
        print()

if __name__ == "__main__":
    print_lyrics()