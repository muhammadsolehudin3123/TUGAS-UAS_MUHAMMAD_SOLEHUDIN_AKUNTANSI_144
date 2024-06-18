import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Membaca file CSV
penjualan = pd.read_csv('sistem_penjualan.csv')
pembelian = pd.read_csv('sistem_pembelian.csv')
persediaan = pd.read_csv('sistem_persediaan.csv')

# Menampilkan informasi dasar dari data
print("Info Penjualan")
print(penjualan.info())
print("\nInfo Pembelian")
print(pembelian.info())
print("\nInfo Persediaan")
print(persediaan.info())

# Membuat histogram untuk setiap dataset
def plot_histogram(data, title):
    data.hist(figsize=(10, 8), bins=30, edgecolor='black')
    plt.suptitle(title)
    plt.show()

plot_histogram(penjualan, 'Histogram Sistem Penjualan')
plot_histogram(pembelian, 'Histogram Sistem Pembelian')
plot_histogram(persediaan, 'Histogram Sistem Persediaan')

# Membuat boxplot untuk setiap dataset
def plot_boxplot(data, title):
    plt.figure(figsize=(10, 8))
    sns.boxplot(data=data, palette='Set2')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

plot_boxplot(penjualan, 'Boxplot Sistem Penjualan')
plot_boxplot(pembelian, 'Boxplot Sistem Pembelian')
plot_boxplot(persediaan, 'Boxplot Sistem Persediaan')

# Melakukan clustering untuk setiap dataset
def plot_clusters(data, title):
    # Standarisasi data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data.select_dtypes(include=[int, float]))
    
    # Menentukan jumlah kluster
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)
    
    # Menambahkan kolom cluster ke data asli
    data['Cluster'] = clusters
    
    # Plot hasil clustering
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=data, x=data.columns[0], y=data.columns[1], hue='Cluster', palette='Set1')
    plt.title(title)
    plt.show()

plot_clusters(penjualan, 'Clustering Sistem Penjualan')
plot_clusters(pembelian, 'Clustering Sistem Pembelian')
plot_clusters(persediaan, 'Clustering Sistem Persediaan')

# Membuat barchart untuk setiap dataset
def plot_barchart(data, title):
    plt.figure(figsize=(10, 8))
    data.mean().plot(kind='bar', color=sns.color_palette('Set2'))
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

plot_barchart(penjualan, 'Barchart Sistem Penjualan')
plot_barchart(pembelian, 'Barchart Sistem Pembelian')
plot_barchart(persediaan, 'Barchart Sistem Persediaan')

# Simpan plot sebagai gambar
def save_plots():
    plot_histogram(penjualan, 'Histogram Sistem Penjualan')
    plt.savefig('histogram_penjualan.png')
    plot_histogram(pembelian, 'Histogram Sistem Pembelian')
    plt.savefig('histogram_pembelian.png')
    plot_histogram(persediaan, 'Histogram Sistem Persediaan')
    plt.savefig('histogram_persediaan.png')

    plot_boxplot(penjualan, 'Boxplot Sistem Penjualan')
    plt.savefig('boxplot_penjualan.png')
    plot_boxplot(pembelian, 'Boxplot Sistem Pembelian')
    plt.savefig('boxplot_pembelian.png')
    plot_boxplot(persediaan, 'Boxplot Sistem Persediaan')
    plt.savefig('boxplot_persediaan.png')

    plot_clusters(penjualan, 'Clustering Sistem Penjualan')
    plt.savefig('clustering_penjualan.png')
    plot_clusters(pembelian, 'Clustering Sistem Pembelian')
    plt.savefig('clustering_pembelian.png')
    plot_clusters(persediaan, 'Clustering Sistem Persediaan')
    plt.savefig('clustering_persediaan.png')

    plot_barchart(penjualan, 'Barchart Sistem Penjualan')
    plt.savefig('barchart_penjualan.png')
    plot_barchart(pembelian, 'Barchart Sistem Pembelian')
    plt.savefig('barchart_pembelian.png')
    plot_barchart(persediaan, 'Barchart Sistem Persediaan')
    plt.savefig('barchart_persediaan.png')

save_plots()
