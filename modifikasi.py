# ==========================================================
# TUGAS MATA KULIAH MATEMATIKA DISKRIT (TB-B)
#
# Judul:
# Sistem Rekomendasi Film Menggunakan
# User-Based Collaborative Filtering
# dengan Jaccard Similarity dan Graf Bipartit
#
# Kelompok 7
# - Fuad Wigo Wicaksono
# - Muhammad Syarofi Kunaedi
# - Valent Ichsanul Fitri
#
# Program Studi Informatika
# Universitas Muhammadiyah Cirebon
# ==========================================================

# ==========================================================
# IMPLEMENTASI KONSEP MATEMATIKA DISKRIT
# - Teori Himpunan (Set Theory)
# - Jaccard Similarity
# - Graf Bipartit (Graph Theory)
# - Matriks Similaritas
# ==========================================================

import time
import networkx as nx # type: ignore
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# ==========================
# DATA PENGGUNA
# ==========================

# MATDIS:
# Representasi data menggunakan Teori Himpunan (Set Theory).
# Setiap pengguna direpresentasikan sebagai himpunan (set)
# yang berisi daftar film yang telah ditonton.

users = {
    "Andi": {"Avengers", "Batman", "Spiderman", "Iron Man"},
    "Budi": {"Batman", "Spiderman", "Superman", "Wonder Woman"},
    "Caca": {"Avengers", "Iron Man", "Batman", "Captain America"},
    "Dewi": {"Superman", "Wonder Woman", "Batman", "Avengers"},
    "Eko": {"Avengers", "Iron Man", "Captain America", "Spiderman"},
    "Fani": {"Spiderman", "Captain America", "Wonder Woman", "Superman"},
    "Gilang": {"Avengers", "Superman", "Iron Man", "Batman"},
    "Hana": {"Batman", "Wonder Woman", "Spiderman", "Iron Man"}
}

# ==========================================================
# FUNGSI JACCARD SIMILARITY
# ==========================================================

# MATDIS:
# Implementasi Similarity Jaccard.
#
# Rumus:
# J(A,B) = |A ∩ B| / |A ∪ B|
#
# Digunakan untuk mengukur tingkat kemiripan
# antara dua himpunan film.
def jaccard_similarity(user1, user2):
    # MATDIS: Operasi Irisan (∩) dan Gabungan (∪) pada himpunan
    set1 = users[user1]
    set2 = users[user2]
    intersection = set1 & set2  # MATDIS: Operasi irisan himpunan
    union = set1 | set2         # MATDIS: Operasi gabungan himpunan
    # MATDIS: Pembagian cardinalitas (jumlah elemen) untuk mendapatkan similarity
    return len(intersection) / len(union) if union else 0

# ==========================================================
# FUNGSI REKOMENDASI (USER-BASED COLLABORATIVE FILTERING)
# ==========================================================

# MATDIS:
# Menggunakan nilai Jaccard Similarity
# sebagai bobot untuk menentukan rekomendasi film.
def get_recommendations(target, top_n=2):
    """
    Menghasilkan rekomendasi film untuk target user.
    Mengambil top-N user paling mirip, lalu mengumpulkan film yang belum ditonton
    dengan bobot = similarity.
    """
    # MATDIS: Menghitung similarity matrix untuk semua pasangan user
    similarities = []
    for other in users:
        if other == target:
            continue
        sim = jaccard_similarity(target, other)
        similarities.append((other, sim))
    
    # MATDIS: Sorting berdasarkan nilai similarity (descending)
    # Konsep Ordering/Urutan dalam matematika diskrit
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_users = similarities[:top_n]  # MATDIS: Pengambilan top-N elemen
    
    # MATDIS: Weighted Voting / Aggregation
    # Menggunakan bobot similarity untuk memberi nilai pada setiap film
    movie_weight = defaultdict(float)
    for user, sim in top_users:
        if sim <= 0:
            continue
        for movie in users[user]:
            # MATDIS: Operasi selisih himpunan (difference) - film baru
            if movie not in users[target]:  # MATDIS: Keanggotaan (membership) dalam himpunan
                movie_weight[movie] += sim  # MATDIS: Penjumlahan bobot (linear combination)
    
    # MATDIS: Sorting final berdasarkan bobot (descending)
    sorted_movies = sorted(movie_weight.items(), key=lambda x: x[1], reverse=True)
    return sorted_movies, top_users

# ==========================================================
# FUNGSI VISUALISASI GRAF BIPARTIT
# ==========================================================

# MATDIS:
# Implementasi Graph Theory menggunakan Graf Bipartit.
#
# Graf terdiri atas dua himpunan simpul:
# - User
# - Film
#
# Edge hanya menghubungkan User dengan Film.
def plot_bipartite_graph():
    # MATDIS: Membuat graf kosong menggunakan NetworkX
    G = nx.Graph()
    
    # MATDIS: Menambahkan node untuk partisi pertama (User) dengan atribut bipartite=0
    for user in users:
        G.add_node(user, bipartite=0)
    
    # MATDIS: Menambahkan node untuk partisi kedua (Film) dengan atribut bipartite=1
    all_movies = set()
    for movie_set in users.values():
        all_movies.update(movie_set)
    for movie in all_movies:
        G.add_node(movie, bipartite=1)
    
    # MATDIS: Menambahkan edge (sisi) antara user dan film yang ditonton
    # Relasi ini membentuk graf bipartit karena edge hanya menghubungkan dua partisi berbeda
    for user, movie_set in users.items():
        for movie in movie_set:
            G.add_edge(user, movie)
    
    # MATDIS: Layout untuk visualisasi bipartite graph
    # User di posisi x=0, Film di posisi x=1
    pos = {}
    user_list = list(users.keys())
    movie_list = list(all_movies)
    for i, user in enumerate(user_list):
        pos[user] = (0, i / max(1, len(user_list)-1))
    for i, movie in enumerate(movie_list):
        pos[movie] = (1, i / max(1, len(movie_list)-1))
    
    # MATDIS: Pewarnaan node berdasarkan partisi
    node_colors = ['skyblue' if node in users else 'salmon' for node in G.nodes]
    
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colors,
            node_size=2000, font_size=9, font_weight='bold')
    plt.title("Graf Bipartit User (Biru) – Film (Merah)", fontsize=14)
    plt.tight_layout()
    plt.show()

# ==========================================================
# FUNGSI HEATMAP SIMILARITAS
# ==========================================================

# MATDIS:
# Matriks Similaritas merepresentasikan
# hubungan antar pengguna berdasarkan
# nilai Jaccard Similarity.
def plot_similarity_heatmap():
    user_list = list(users.keys())
    n = len(user_list)
    # MATDIS: Membuat matriks n x n untuk menyimpan nilai similarity
    matrix = np.zeros((n, n))
    for i, u1 in enumerate(user_list):
        for j, u2 in enumerate(user_list):
            if i == j:
                matrix[i, j] = 1.0  # MATDIS: Diagonal matriks = 1 (similarity sempurna)
            else:
                matrix[i, j] = jaccard_similarity(u1, u2)
    
    # MATDIS: Visualisasi matriks sebagai heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(matrix, cmap='Blues', vmin=0, vmax=1)
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(user_list, rotation=45, ha='right')
    ax.set_yticklabels(user_list)
    
    # MATDIS: Menampilkan nilai setiap sel matriks
    for i in range(n):
        for j in range(n):
            ax.text(j, i, f'{matrix[i, j]:.2f}',
                    ha='center', va='center',
                    color='white' if matrix[i, j] > 0.6 else 'black')
    
    plt.colorbar(im)
    ax.set_title("Matriks Similaritas Jaccard antar User")
    plt.tight_layout()
    plt.show()

# ==========================================
# PROGRAM UTAMA
# ==========================================

# MATDIS:
# Mengintegrasikan seluruh konsep
# Matematika Diskrit ke dalam
# Sistem Rekomendasi Film.

def main():
    print("=" * 60)
    print("SISTEM REKOMENDASI FILM BERBASIS GRAF BIPARTIT")
    print("=" * 60)
    
    while True:
        print("\nMENU:")
        print("1. Lihat semua user dan film")
        print("2. Rekomendasi untuk user tertentu")
        print("3. Tampilkan graf bipartit")
        print("4. Tampilkan heatmap similaritas")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            print("\nDaftar User dan Film:")
            for user, movies in users.items():
                print(f"  {user}: {', '.join(movies)}")
        
        elif pilihan == '2':
            print("\nDaftar User:")
            for user in users:
                print(f"  - {user}")
            target = input("Masukkan nama user target: ").strip()
            if target not in users:
                print("User tidak ditemukan!")
                continue
            
            # MATDIS: Analisis kompleksitas waktu (Time Complexity)
            # O(n*m) dimana n = jumlah user, m = jumlah film per user
            start = time.perf_counter()  # MATDIS: Pengukuran runtime
            
            # MATDIS: Memanggil fungsi rekomendasi
            recs, top_users = get_recommendations(target, top_n=2)
            
            end = time.perf_counter()
            exec_time = end - start
            
            print(f"\n--- Rekomendasi untuk {target} ---")
            print(f"Film yang sudah ditonton: {', '.join(users[target])}")
            print("\nUser paling mirip:")
            for user, sim in top_users:
                print(f"  {user} (similarity = {sim:.2f})")
            
            print("\nFilm rekomendasi (dengan bobot):")
            if recs:
                for movie, weight in recs:
                    print(f"  - {movie} (bobot {weight:.2f})")
            else:
                print("  Tidak ada rekomendasi baru.")
            
            print(f"\nWaktu eksekusi: {exec_time:.6f} detik")
        
        elif pilihan == '3':
            plot_bipartite_graph()
        
        elif pilihan == '4':
            plot_similarity_heatmap()
        
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem!")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()