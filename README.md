# TUGAS PENGKODEAAN DAN PEMROGRAMAN 
NAMA   : MUHAMMAD SOLEHUDIN

KELAS  : PEMROGRAMAN DAN PENGKODEAN / D

NIM    : 12030122130144

# BERIKUT ADALAH CARA MENJALANKAN  KODE PYTHON  YANG TERHUBUNG KE FILE JENIS CSV
1. masukan buka visual code dan tambhakan extension python pada visual code
2. domload library python yang dibutuhkan yang terdiri dari
   
   a. pandas
   
   b. matplotlib
   
   c. kmeans
   
   d. seaborn
   
3. buat tabel csv untuk kebutuhan pengkodiangan , berikan nama file data sesuai kodingan 
4. open folder tempat  kode python yang akan di jalankan  pada visual code
5. jalankan kode yang tertera di atas
6. langkah akhir jalankan terminal untuk menghasilkan output yang tertampil di bawah ini, yang terdiri dari
   
   a. histogram
   
   b. bar chart
   
   c. cluster
   
   d. box plot 


#berikut hasil dari kode python yang di jalankan 
## HISTOGRAM

![Cuplikan layar 2024-06-17 230058](https://github.com/muhammadsolehudin3123/TUGAS-UAS_MUHAMMAD_SOLEHUDIN_AKUNTANSI_144/assets/152485242/24c6284d-0657-44ef-969c-f51e598a6002)

Berdasarkan histogram yang ditampilkan di gambar tersebut, berikut adalah analisis dan pengamatan untuk masing-masing variabel dalam sistem penjualan:
1.	ID:
o	Distribusi ID terlihat merata dan seragam. Setiap ID dari 1 hingga 10 memiliki frekuensi yang sama. Ini menunjukkan bahwa tidak ada ID yang hilang atau duplikat dalam dataset penjualan.
2.	Quantity:
o	Distribusi Quantity juga merata dari 1 hingga 10. Setiap nilai Quantity muncul dengan frekuensi yang sama. Ini bisa menunjukkan bahwa data Quantity dalam sistem penjualan diinput secara konsisten dan tidak ada nilai yang menonjol atau hilang.
3.	Price:
o	Harga (Price) memiliki distribusi yang bervariasi dari sekitar 100 hingga 400. Meskipun setiap rentang harga memiliki frekuensi yang relatif sama, tidak ada outlier yang signifikan. Data harga terlihat terdistribusi secara merata tanpa adanya harga yang jauh lebih tinggi atau lebih rendah dibandingkan yang lain.
4.	Discount:
o	Diskon (Discount) memiliki beberapa nilai yang sama muncul lebih sering (misalnya 0, 5, 10, 15, 20, 25, 30). Ini menunjukkan bahwa diskon diberikan dalam kelipatan tertentu dan tidak ada variasi diskon di luar nilai-nilai tersebut. Ini mungkin disebabkan oleh kebijakan diskon yang diterapkan oleh perusahaan.
5.	Total:
o	Total (Total) nilai penjualan menunjukkan distribusi yang lebih bervariasi dibandingkan variabel lainnya. Ada beberapa puncak di histogram yang menunjukkan bahwa beberapa total nilai penjualan muncul lebih sering dibandingkan yang lain. Total nilai penjualan terlihat berkisar antara 800 hingga 1200.
Pengamatan Grafik:
•	Histogram menunjukkan bahwa data penjualan terdistribusi dengan baik tanpa adanya anomali yang mencolok.
•	Setiap variabel memiliki distribusi yang cukup seragam kecuali untuk total penjualan yang menunjukkan beberapa variasi lebih besar.
•	Tidak ada outlier yang signifikan atau nilai yang hilang yang memerlukan perhatian khusus berdasarkan histogram ini.



![Cuplikan layar 2024-06-17 230115](https://github.com/muhammadsolehudin3123/TUGAS-UAS_MUHAMMAD_SOLEHUDIN_AKUNTANSI_144/assets/152485242/9d269cf1-b797-433e-8688-4ecc58ed2e5c)

Berdasarkan histogram yang ditampilkan di gambar tersebut, berikut adalah analisis dan pengamatan untuk masing-masing variabel dalam sistem pembelian:
1.	ID:
o	Distribusi ID terlihat merata dan seragam dari 1 hingga 10. Setiap ID memiliki frekuensi yang sama. Ini menunjukkan bahwa tidak ada ID yang hilang atau duplikat dalam dataset pembelian.
2.	Quantity:
o	Distribusi Quantity juga merata dari 5 hingga 20. Setiap nilai Quantity muncul dengan frekuensi yang sama. Ini menunjukkan bahwa data Quantity dalam sistem pembelian diinput secara konsisten dan tidak ada nilai yang menonjol atau hilang.
3.	Cost:
o	Cost menunjukkan variasi yang lebih besar, dengan puncak frekuensi yang lebih tinggi pada nilai 100 dan distribusi yang lebih merata di nilai lainnya. Ada beberapa nilai cost yang muncul lebih sering dibandingkan yang lain, tetapi tidak ada outlier yang signifikan. Ini menunjukkan bahwa ada beberapa barang yang sering dibeli dengan harga sekitar 100, sementara yang lain memiliki variasi harga yang lebih luas.
4.	TotalCost:
o	TotalCost memiliki beberapa puncak frekuensi, khususnya pada nilai sekitar 1600 dan 1800. Ini menunjukkan bahwa ada beberapa transaksi pembelian dengan total biaya yang lebih umum dibandingkan yang lain. TotalCost menunjukkan variasi yang lebih besar dan bisa disebabkan oleh jumlah atau jenis barang yang dibeli dalam setiap transaksi.
Pengamatan Grafik:
•	Histogram menunjukkan bahwa data pembelian terdistribusi dengan baik tanpa adanya anomali yang mencolok.
•	Setiap variabel memiliki distribusi yang cukup seragam kecuali untuk Cost dan TotalCost yang menunjukkan beberapa variasi lebih besar.
•	Tidak ada outlier yang signifikan atau nilai yang hilang yang memerlukan perhatian khusus berdasarkan histogram ini.



![Cuplikan layar 2024-06-17 230129](https://github.com/muhammadsolehudin3123/TUGAS-UAS_MUHAMMAD_SOLEHUDIN_AKUNTANSI_144/assets/152485242/3ea167ce-2b13-4c4c-a10d-d95292feaa28)

Berdasarkan histogram yang ditampilkan pada gambar di atas, berikut adalah analisis dan pengamatan untuk masing-masing variabel dalam sistem persediaan:
1.1	ID:
o	Distribusi ID terlihat merata dan seragam dari 1 hingga 10. Setiap ID memiliki frekuensi yang sama. Ini menunjukkan bahwa tidak ada ID yang hilang atau duplikat dalam dataset persediaan.
2.1	StockIn:
o	Distribusi StockIn juga merata dari 5 hingga 30. Setiap nilai StockIn muncul dengan frekuensi yang sama. Ini menunjukkan bahwa data pemasukan stok dalam sistem persediaan diinput secara konsisten dan tidak ada nilai yang menonjol atau hilang.
3.1	StockOut:
o	Distribusi StockOut serupa dengan StockIn, menunjukkan distribusi yang merata dari 2 hingga 10. Ini menunjukkan bahwa data pengeluaran stok juga diinput secara konsisten.
4.1	StockBalance:
o	Distribusi StockBalance menunjukkan variasi yang serupa dengan StockIn dan StockOut, dengan nilai dari 5 hingga 22.5. Data ini juga menunjukkan konsistensi dalam pencatatan saldo stok.
Pengamatan Umum:
•	Histogram menunjukkan bahwa data persediaan terdistribusi dengan baik tanpa adanya anomali yang mencolok.
•	Setiap variabel memiliki distribusi yang cukup seragam, menunjukkan konsistensi dalam pencatatan data.
•	Tidak ada outlier yang signifikan atau nilai yang hilang yang memerlukan perhatian khusus berdasarkan histogram ini.


## SCATTER PLOT
![Cuplikan layar 2024-06-17 230226](https://github.com/muhammadsolehudin3123/TUGAS-UAS_MUHAMMAD_SOLEHUDIN_AKUNTANSI_144/assets/152485242/e70dcf8a-70e2-4b76-83d9-c68102264547)
![Cuplikan layar 2024-06-17 230238](https://github.com/muhammadsolehudin3123/TUGAS-UAS_MUHAMMAD_SOLEHUDIN_AKUNTANSI_144/assets/152485242/35d52b07-1f3e-46bf-9a4d-96d4755ace91)
![Cuplikan layar 2024-06-17 230252](https://github.com/muhammadsolehudin3123/TUGAS-UAS_MUHAMMAD_SOLEHUDIN_AKUNTANSI_144/assets/152485242/a22fb760-60bd-4ae0-9591-81918f4f7132)

Analisis dan Pengamatan dari Scatter Plot
1. Clustering Sistem Penjualan
•	Pengamatan:
o	Ada 10 produk (Product_A hingga Product_J) yang dikelompokkan ke dalam tiga kluster yang berbeda (0, 1, dan 2).
o	Kluster 0 ditandai dengan warna merah.
o	Kluster 1 ditandai dengan warna biru.
o	Kluster 2 ditandai dengan warna hijau.
o	Produk tersebar secara relatif merata dengan ID dari 1 hingga 10.
•	Analisis:
o	Produk A, B, dan C dikelompokkan dalam kluster 2 (hijau), menunjukkan bahwa mereka memiliki karakteristik serupa.
o	Produk D, E, G, dan J berada dalam kluster 0 (merah), menunjukkan mereka memiliki karakteristik serupa.
o	Produk F, H, dan I berada dalam kluster 1 (biru), menunjukkan mereka memiliki karakteristik yang berbeda dari dua kluster lainnya.
2. Clustering Sistem Pembelian
•	Pengamatan:
o	Ada 10 supplier (Supplier_A hingga Supplier_J) yang dikelompokkan ke dalam tiga kluster yang berbeda (0, 1, dan 2).
o	Kluster 0 ditandai dengan warna merah.
o	Kluster 1 ditandai dengan warna biru.
o	Kluster 2 ditandai dengan warna hijau.
o	Supplier tersebar secara relatif merata dengan ID dari 1 hingga 10.
•	Analisis:
o	Supplier A, B, dan C dikelompokkan dalam kluster 2 (hijau), menunjukkan bahwa mereka memiliki karakteristik serupa.
o	Supplier D, E, G, dan J berada dalam kluster 0 (merah), menunjukkan mereka memiliki karakteristik serupa.
o	Supplier F, H, dan I berada dalam kluster 1 (biru), menunjukkan mereka memiliki karakteristik yang berbeda dari dua kluster lainnya.
3. Clustering Sistem Persediaan
•	Pengamatan:
o	Ada 10 produk (Product_A hingga Product_J) yang dikelompokkan ke dalam tiga kluster yang berbeda (0, 1, dan 2).
o	Kluster 0 ditandai dengan warna merah.
o	Kluster 1 ditandai dengan warna biru.
o	Kluster 2 ditandai dengan warna hijau.
o	Produk tersebar secara relatif merata dengan ID dari 1 hingga 10.
•	Analisis:
o	Product_A dikelompokkan dalam kluster 2 (hijau), menunjukkan bahwa produk ini memiliki karakteristik yang unik dan berbeda dari produk lainnya.
o	Produk B dan F dikelompokkan dalam kluster 0 (merah), menunjukkan bahwa mereka memiliki karakteristik serupa.
o	Produk C, D, G, dan J berada dalam kluster 1 (biru), menunjukkan mereka memiliki karakteristik serupa.
o	Produk E, H, dan I berada dalam kluster 2 (hijau), menunjukkan mereka memiliki karakteristik serupa.



## BOX PLOT 
![Cuplikan layar 2024-06-17 230145](https://github.com/muhammadsolehudin3123/TUGAS-UAS_MUHAMMAD_SOLEHUDIN_AKUNTANSI_144/assets/152485242/145e9853-1c57-4ccc-9830-5423d1ed55f6)
![Cuplikan layar 2024-06-17 230159](https://github.com/muhammadsolehudin3123/TUGAS-UAS_MUHAMMAD_SOLEHUDIN_AKUNTANSI_144/assets/152485242/1d8d77ca-f061-4bf2-9adb-ad2458c9b565)
![Cuplikan layar 2024-06-17 230213](https://github.com/muhammadsolehudin3123/TUGAS-UAS_MUHAMMAD_SOLEHUDIN_AKUNTANSI_144/assets/152485242/d9776133-0abe-4222-b117-f1d13232d0d5)

1: Boxplot Sistem Penjualan
1.	ID:
o	Terlihat bahwa nilai ID memiliki rentang yang sangat kecil, dengan median dan kuartil yang hampir sama.
2.	Quantity:
o	Nilai quantity memiliki rentang yang sangat kecil dan hampir tidak ada variasi.
3.	Price:
o	Nilai price memiliki variasi yang cukup besar. Median berada di sekitar 100-200, dan ada beberapa pencilan.
4.	Discount:
o	Nilai discount memiliki rentang yang kecil dan hampir tidak ada variasi.
5.	Total:
o	Nilai total memiliki variasi terbesar. Median berada di sekitar 800-1000, dengan beberapa pencilan di atas 1200.
 2: Boxplot Sistem Pembelian
1.	ID:
o	Sama seperti pada sistem penjualan, nilai ID memiliki rentang yang sangat kecil dan hampir tidak ada variasi.
2.	Quantity:
o	Nilai quantity memiliki rentang yang sangat kecil dan hampir tidak ada variasi.
3.	Cost:
o	Nilai cost memiliki variasi yang cukup besar. Median berada di sekitar 100-200, dan ada beberapa pencilan.
4.	TotalCost:
o	Nilai total cost memiliki variasi terbesar. Median berada di sekitar 1500-2000, dengan beberapa pencilan di atas 2000.
 3: Boxplot Sistem Persediaan
1.	ID:
o	Nilai ID memiliki rentang yang kecil dengan median dan kuartil yang hampir sama.
2.	StockIn:
o	Nilai stock in memiliki variasi yang cukup besar. Median berada di sekitar 15-20.
3.	StockOut:
o	Nilai stock out memiliki variasi yang kecil. Median berada di sekitar 5-10.
4.	StockBalance:
o	Nilai stock balance memiliki variasi yang cukup besar. Median berada di sekitar 10-20.

Pengamatan Umum
1.	ID dan Quantity di semua sistem memiliki variasi yang sangat kecil, menunjukkan bahwa ID dan jumlah barang yang dijual/beli/di stok hampir seragam.
2.	Price, Cost, dan Total/ TotalCost memiliki variasi yang cukup besar, menunjukkan bahwa ada perbedaan yang signifikan dalam harga, biaya, dan total nilai transaksi.
3.	Discount memiliki variasi yang sangat kecil, menunjukkan bahwa diskon yang diberikan hampir seragam.
4.	StockIn, StockOut, dan StockBalance memiliki variasi yang lebih besar, menunjukkan perbedaan yang signifikan dalam stok masuk, stok keluar, dan keseimbangan stok.












