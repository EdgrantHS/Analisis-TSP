# Perbandingan Limitasi Solusi Algoritma pada Traveling Salesman Problem

## Abstract

Traveling Salesman Problem (TSP) adalah permasalahan yang meminta untuk menemukan jalur terpendek yang melalui semua titik yang diberikan dan kembali ke titik awal. TSP adalah salah satu contoh masalah NP-Complete yang paling terkenal. Beberapa algoritma yang sering digunakan untuk menyelesaikan TSP adalah brute force, dynamic programming, nearest neighbor algorithm, simulated annealing, ant colony optimization, dan genetic algorithm. Pada paper ini, akan dilakukan perbandingan antara running time dari algoritma brute force, dynamic programming, nearest neighbor algorithm, ant colony optimization, dan genetic algorithm. Selain itu juga akan dilakukan perbandingan antara solusi yang dihasilkan oleh algoritma brute force, dynamic programming, nearest neighbor algorithm, dan ACO. Berdasarkan hasil eksperimen, didapatkan bahwa algoritma brute force dan dynamic programming menghasilkan solusi yang optimal. Namun, kedua algoritma tersebut memiliki running time yang tinggi. Algoritma NNH memiliki running time yang paling rendah tetapi sering kali menghasilkan solusi yang tidak optimal. Algoritma ACO memiliki running time yang lebih tinggi dibandingkan dengan solusi yang paling optimal dibandingkan NNH.

### Index Terms

Ant Colony Optimization, Brute Force, Dynamic Programming, Genetic Algorithm, Greedy Algorithm, NP-Complete, P vs NP, Simulated Annealing, Traveling Salesman Problem

## I. INTRODUCTION

Pemasalahan P vs NP adalah permasalahan yang telah ada sejak lama dan belum terselesaikan. Ini adalah permasalahan atas kesulitan menentukan apakah suatu permasalahan tidak dapat diselesaikan dalam waktu polinomial (masalah yang komputer dapat mengkomputasi dengan cepat) atau solusi hanya belum ditemukan.
Traveling Salesman Problem (TSP) adalah salah satu permasalahan NP. Lebih khususnya lagi TSP masuk dalam kelompok permasalahan yang bernama NP-Complete. Solusi polinomial untuk permasalahan NP-Complete bisa merevolusi dunia ilmu komputer.

## II. BACKGROUND

### A. P vs NP

P vs NP adalah permasalahan yang belum terselesaikan dalam ilmu komputer. P adalah kelas masalah yang dapat diselesaikan dalam waktu polinomial. NP adalah kelas masalah yang tidak dapat diselesaikan dalam waktu polinomial tetapi solusinya dapat diverifikasi dalam waktu polinomial. P vs NP adalah pertanyaan apakah setiap masalah yang dapat diverifikasi dalam waktu polinomial juga dapat diselesaikan dalam waktu polinomial oleh komputer. Jika P = NP, setiap masalah yang dapat diverifikasi dalam waktu polinomial oleh komputer juga dapat diselesaikan dalam waktu polinomial oleh komputer. Jika P tidak sama dengan NP, setidaknya ada satu masalah yang dapat diverifikasi dalam waktu polinomial oleh komputer tetapi tidak dapat diselesaikan dalam waktu polinomial oleh komputer. [1] [2]

### B. NP-Complete

NP-Complete adalah kelas masalah yang merupakan gabungan dari masalah NP dan masalah NP-Hard. Masalah NP adalah masalah yang solusinya dapat diverifikasi dalam waktu polinomial oleh komputer. Masalah NP-Hard adalah masalah yang setidaknya sesuhan untuk dikomputasi dengan masalah NP. TSP adalah salah satu contoh masalah NP-Complete.
Seluruh masalah NP-Complete dapat diubah menjadi masalah NP-Conplete lainnya. Oleh karena itu, jika suatu masalah NP-Complete dapat diselesaikan dalam waktu polinomial, maka seluruh masalah NP-Complete dapat diselesaikan dalam waktu polinomial.
TSP merupakan masalah NP-Complete yang paling terkenal. Selain itu, TSP juga merupakan masalah yang paling banyak diaplikasikan dalam dunia nyata. Beberapa permasalahan NP-Complete lainnya adalah knapsack problem, graph coloring, dan hamiltonian cycle.

### C. Traveling Salesman Problem

Traveling Salesman Problem (TSP) adalah permasalahan yang meminta untuk menemukan jalur terpendek yang melalui semua titik yang diberikan dan kembali ke titik awal. Contoh kasus TSP dan sumber namanya adalah seorang salesman yang harus mengunjungi beberapa kota untuk menjual barang dan kembali ke kota asal, salesman tersebut ingin menemukan jalur terpendek untuk mengunjungi semua kota agar menghemat waktu dan biaya perjalanan.

## III. Theory

### A. Brute Force

Brute force adalah algoritma yang mencoba semua kemungkinan kombinasi solusi dan memilih solusi yang optimal. Brute force adalah algoritma yang paling sederhana dan paling mudah dipahami. Namun, brute force memiliki kompleksitas waktu yang tinggi. Kompleksitas waktu brute force adalah O(n!). Kompleksitas waktu brute force meningkat secara factorial dengan penambahan titik. Oleh karena itu, brute force tidak efisien untuk menyelesaikan TSP dengan jumlah titik yang besar.

### B. Dynamic Programming

Dynamic programming adalah algoritma yang memecah masalah menjadi submasalah yang lebih kecil dan menyimpan solusi submasalah tersebut. Solusi TSP dynamic programing salah satunya menggunakan algoritma Held-Karp. Kompleksitas waktu dynamic programming adalah O(n^2 * 2^n). Dynamic programming lebih efisien daripada brute force dengan tetap menghasilkan solusi yang optimal. Namun, dynamic programming tetap tidak efisien untuk menyelesaikan TSP dengan jumlah titik yang besar karena kompleksitas waktu yang eksponensial. [13]

### C. Greedy Algorithm

Greedy algorithm adalah algoritma yang memilih solusi yang optimal pada janjang waktu pendek. Jenis algorithm ini memilih solusi yang optimal pada setiap langkah tanpa memperhatikan solusi yang lebih optimal pada langkah selanjutnya. Namun, tergantung permasalahannya, greedy algorithm sering tidak selalu menghasilkan solusi yang optimal. Pada TSP, greedy algorithm sering menghasilkan solusi yang lebih panjang dibandingkan dengan solusi dengan algoritma yang lebih kompleks seperti SA, ACO, dan GA.
Pada TSP, greedy algorithm yang sering digunakan adalah nearest neighbor algorithm dan k-opt algorithm. Pada paper ini akan lebih dibahas nearest neighbor algorithm. Nearest neighbor heuristic algorithm (NNH) memilih titik terdekat dari titik saat ini sebagai titik selanjutnya. Algorithm ini memiliki kompleksitas waktu polinomial O(n^2) dan lebih efisien daripada dynamic programming dan brute force. Namun, nearest neighbor algorithm sering menghasilkan solusi yang tidak optimal. Secara praktis, karena kemudahan algoritmanya, NNH memiliki waktu komputasi yang paling cepat dibandingkan dengan algoritma lainnya. [8]

### D. Simulated Annealing

Simulated annealing (SA) adalah algoritma yang mengambil inspirasi dari proses pendinginan logam. Algoritma ini memiliki kemungkinan untuk menerima solusi yang lebih buruk daripada solusi saat ini berdasarkan suhu (probabilitas) tertentu. Suhu akan menurun seiring waktu dan kemungkinan menerima solusi yang lebih buruk juga akan menurun. Algoritma ini memiliki kompleksitas waktu polinomial O(n^2) dengan hasil yang lebih baik daripada nearest neighbor algorithm. Namun, algoritma ini memiliki parameter yang harus diatur dengan tepat agar menghasilkan solusi yang optimal yaitu suhu awal, suhu akhir, dan rasio penurunan suhu.
Jika dibandingkan dengan algoritma lainnya, SA memiliki keunggulan dalam menemukan solusi dengan lebih cepat, tetapi memiliki kelemahan dalam menemukan solusi yang lebih panjang dibandingkan dengan algoritma ACO dan GA. [11]

### E. Ant Colony Optimization

Ant Colony Optimization (ACO) adalah algoritma yang mengambil inspirasi dari perilaku semut dalam membuat jaringan jalur terpendek dari sarang ke sumber makanan. Algoritma ini memiliki kompleksitas waktu polinomial O(n^2) dengan hasil yang lebih baik daripada nearest neighbor algorithm dan simulated annealing. Algoritma ini juga memiliki parameter yang harus diatur dengan tepat agar menghasilkan solusi yang optimal yaitu alpha, beta, rho, dan Q.  
Jika dibandingkan dengan algoritma lainnya, ACO memiliki keunggulan dalam menemukan solusi yang paling optimal, tetapi memiliki kelemahan dalam waktu komputasi yang paling lama dibandingkan dengan algoritma SA dan GA. [11]

### F. Genetic Algorithm

Genetic Algorithm (GA) adalah algoritma yang mengambil inspirasi dari proses evolusi dalam alam. Algoritma ini memiliki populasi kromosom (dalam kasus TSP, kromosom adalah list jalur yang melalui semua titik) yang bereproduksi dan mengalami mutasi. GA memiliki kompleksitas waktu polinomial O(n^2) dengan hasil yang lebih baik daripada NNH algorithm dan SA. Algoritma ini juga memiliki parameter yang harus diatur dengan tepat agar menghasilkan solusi yang optimal yaitu ukuran populasi, probabilitas crossover, probabilitas mutasi, dan jumlah generasi.
Jika dibandingkan dengan algoritma lainnya, GA memiliki solusi yang paling tidak optimal dibanding dengan SA dan ACO, waktu komputasi yang lebih cepat dibandingkan dengan ACO, tetapi lebih lambat dibandingkan dengan SA. [11]

## IV. EXPERIMENT

### A. Metodologi

Pada paper ini, akan dilakukan perbandingan antara running time dari algorima brute force, dynamic programming, nearest neighbor algorithm, ant colony optimization, dan genetic algorithm. Selain itu juga akan dilakukan perbandingan antara solusi yang dihasilkan oleh algoritma brute force, dynamic programming, nearest neighbor algorithm, dan ACO. Solusi yang dihasilkan oleh algoritma SA dan GA tidak akan dibandingkan karena solusi yang dihasilkan oleh kedua algoritma tersebut tidak optimal oleh program yang digunakan.
Seluruh percobaan dengan seluruh algoritma akan dilakukan sebanyak 10 kali dan diambil rata-rata running time dan solusi yang dihasilkan. Percobaan brute force dilakukan sampai 10 titik, dynamic programming sampai 20 titik, ACO sampai 100 titik, dan NNH sampai 1000 titik.

### B. Alat Eksperimen

Pada paper ini, akan digunakan program Python untuk mengimplementasikan algoritma brute force, dynamic programming, nearest neighbor algorithm, simulated annealing, ant colony optimization, dan genetic algorithm. Program ini akan menggunakan library numpy untuk menghitung jarak antar titik dan itertools untuk menghitung semua kemungkinan kombinasi solusi pada brute force.
Data pada program ini dihitung menggunakan google sheet yang diimport dari program Python. Data yang dihitung adalah solusi yang dihasilkan, running time, dan jumlah titik.
Hardware yang digunakan adalah laptop dengan spesifikasi Intel Core i5-8265U, 12GB RAM, dan GPU NVIDIA GeForce MX230. Namun secara teori bottleneck dari program ini adalah memory dan clock speed CPU karena tidak seluruh core CPU/ GPU digunakan.

### C. Hasil Eksperimen

Berdasarkan hasil menjalan program, didapatkan hasil running time seluruh algoritma yang diimplementasikan. Berikut adalah hasil running time dari seluruh algoritma yang diimplementasikan:

![Figure 1](./Graph/Running%20Time%20of%20All%20Agorithm.png)  
Fig. 1. Running time dari seluruh algoritma yang diimplementasikan

Pada gambar diatas, dapat dilihat bahwa running time dari seluruh algoritma yang diimplementasikan. Perlu diperhatikan bahwa sumbu x dan y bersifat logaritmik dengan skala 2. Berdasarkan hasil eksperimen, perbandingan running time dari seluruh algoritma yang diimplementasikan adalah sebagai berikut:

1. Brute force memiliki running time yang paling tinggi dibandingkan dengan algoritma lainnya. karena kompleksitas waktu O(n!) yang meningkat secara factorial.
2. Dynamic programming memiliki running time yang lebih rendah dibandingkan dengan brute force, tetapi tetap memiliki running time yang tinggi karena kompleksitas waktu O(n^2 * 2^n) yang meningkat secara eksponensial.
3. ACO memiliki running time yang lebih rendah dibandingkan dengan dynamic programming pada jumlah titik yang besar. Pada jumlah titik yang kecil, running time ACO lebih tinggi karena waktu komputasi yang dibutuhkan untuk mengsimulasikan semut.
4. GA, seperti ACO, memiliki running time yang lebih rendah dibandingkan dengan dynamic programming pada jumlah titik yang besar dan pada jumlah titik yang kecil, running time lebih tinggi karena waktu komputasi untuk menghitung populasi kromosom. GA memiliki running time yang lebih rendah dibandingkan dengan ACO pada jumlah titik yang besar sesuai dengan percobaan H. H. A. Mukhairez and A. Y. A. Maghari [11].
5. NNH memiliki running time yang paling rendah tetapi pada grafik ini data yang didapatkan bersifat outlier. Hal ini disebabkan oleh kecepatan algoritma yang jauh lebih cepat dibandingkan dengan algoritma lainnya. Oleh karena itu, data sangat bergantung pada noise.

Data NNH dengan titik yang lebih banyak sebagai berikut:

![Figure 2](./Graph/Running%20Time%20of%20Nearest%20Neighbor.png)  
Fig. 2. Running time dari nearest neighbor algorithm

Berdasarkan hasil eksperimen running time, didapatkan hasil solusi yang dihasilkan oleh seluruh algoritma yang diimplementasikan. Dapat dilihat bahwa algorithm brute force dan dynamic programming menghasilkan solusi dengan running time yang bertambah secara eksponensial. ACO, GA, dan NNH menghasilkan solusi dengan running time yang bertumbuh secara kuadrat (pada grafik terlihat linear karena sumbu x dan y bersifat logaritmik).

Berikut adalah hasil solusi yang dihasilkan oleh algoritma brute force, dynamic programming, NNH, dan ACO:

![Figure 3](./Graph/Algoritm%20∆Cost%20From%20Optimal%20Solution.png)  
Fig. 3. Solusi yang dihasilkan oleh algoritma brute force, dynamic programming, NNH, dan ACO

Berdasarkan hasil eksperimen, didapatkan bahwa solusi yang dihasilkan oleh algoritma brute force dan dynamic programming adalah solusi yang optimal jadi ∆Cost dengan solusi optimal adalah 0. Solusi yang dihasilkan oleh algoritma NNH dan ACO sering kali tidak optimal. ∆Cost yang dihasilkan oleh NNH lebih tinggi dibandingkan dengan ACO. Hal ini disebabkan oleh greedy algorithm yang sederhana NNH dibandingkan dengan ACO yang lebih kompleks.

## V. CONCLUSION

Berdasarkan hasil eksperimen, didapatkan bahwa algoritma brute force dan dynamic programming menghasilkan solusi yang optimal. Namun, kedua algoritma tersebut memiliki running time yang tinggi. Algoritma NNH memiliki running time yang paling rendah tetapi sering kali menghasilkan solusi yang tidak optimal. Algoritma ACO memiliki running time yang lebih tinggi dibandingkan dengan solusi yang paling optimal dibandingkan NNH.
Secara keseluruhan, algoritma brute force sangat tidak disarankan untuk menyelesaikan Traveling Salesman Problem (TSP) karena hasil yang optimal dapat dicapai dengan algoritma dynamic programming. Namun, algoritma dynamic programming juga tidak disarankan karena running time yang tinggi. Algoritma Nearest Neighbor Heuristic (NNH) disarankan jika ingin solusi yang cepat dengan catatan solusi yang tidak optimal. Algoritma Ant Colony Optimization (ACO) disarankan jika ingin solusi yang optimal dengan running time yang lebih tinggi dibandingkan dengan NNH.

## APPENDIX

### A. Program Python

### B. Data Hasil Eksperimen

https://docs.google.com/spreadsheets/d/1XSQOoqWclDc2vwvHzkxgoCZrsmxRmv2FqB7JONnY-BI/edit?usp=sharing

## REFERENCES

1. Quanta Magazine, “P vs. NP: The Biggest Puzzle in Computer Science,” YouTube. Dec. 01, 2023. Available: https://www.youtube.com/watch?v=pQsdygaYcE4
2. “Explained: P vs. NP,” MIT News | Massachusetts Institute of Technology, Oct. 29, 2009. Available: https://news.mit.edu/2009/explainer-pnp
3. Reducible, “The Traveling Salesman Problem: When Good Enough Beats Perfect,” YouTube. Jul. 26, 2022. Available: https://www.youtube.com/watch?v=GiDsjIBOVoA
4. Learn by Example, “Solving the Travelling Salesman Problem using Ant Colony Optimization,” YouTube. May 18, 2021. Available: https://www.youtube.com/watch?v=oXb2nC-e_EA
5. P. Kilby and P. Shaw, “Vehicle Routing,” in Foundations of artificial intelligence, 2006, pp. 801–836. doi: 10.1016/s1574-6526(06)80027-1. Available: https://www.sciencedirect.com/topics/computer-science/traveling-salesman-problem
6. A. R. Karlin, N. Klein, and S. O. Gharan, “A (slightly) improved approximation algorithm for metric TSP,” Jun. 2021, doi: 10.1145/3406325.3451009. Available: https://doi.org/10.1145/3406325.3451009
7. GeeksforGeeks, “Traveling Salesman Problem (TSP) Implementation,” GeeksforGeeks, Jan. 31, 2023. Available: https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/?ref=ml_lbp
8. Z. Shaolin, “Best Algorithms for the Traveling Salesman Problem - NextBillion.ai,” NextBillion.ai, Apr. 10, 2024. Available: https://nextbillion.ai/post/algorithms-for-the-traveling-salesman-problem
9. Physics for the Birds, “James Webb Space Telescope and the Traveling Salesman Problem,” YouTube. Jan. 18, 2023. Available: https://www.youtube.com/watch?v=Ov0EetgMws4
10. MihailoGrbic, “GitHub - MihailoGrbic/Traveling-Salesman-Problem-Visualization: An interactive learning tool for the Traveling Salesman Problem and various exact and approximative algorithms used to solve it, including ant colony optimization.,” GitHub. Available: https://github.com/MihailoGrbic/Traveling-Salesman-Problem-Visualization
11. H. H. A. Mukhairez and A. Y. A. Maghari, “Performance Comparison of Simulated Annealing, GA and ACO Applied to TSP,” International Journal of Intelligent Computing Research, vol. 6, no. 4, pp. 647–654, Dec. 2015, doi: 10.20533/ijicr.2042.4655.2015.0080. Available: https://doi.org/10.20533/ijicr.2042.4655.2015.0080
12. James Cutajar, “Evolutionary Algorithm for the Travelling Salesperson Problem (Genetic Algorithm),” YouTube. Dec. 03, 2023. Available: https://www.youtube.com/watch?v=Wgn_aPH3OEk
13. GeeksforGeeks, “Travelling Salesman Problem using Dynamic Programming,” GeeksforGeeks, Apr. 19, 2023. Available: https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/
14. A. Davis, “Traveling Salesman Problem With the 2-opt Algorithm,” Medium, May 21, 2022. Available: https://slowandsteadybrain.medium.com/traveling-salesman-problem-ce78187cf1f3
