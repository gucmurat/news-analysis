<!-- omit in toc -->
<a href="https://github.com/gucmurat/news-analysis/blob/main/News_Analysis_Report.pdf" target="_blank">Project Report</a>

# Table of Contents
- [Hakkında](#hakkında)
- [Yükleme](#yükleme)
  - [Manuel Kurulum](#manuel-kurulum)
  - [Otomatik Kurulum](#otomatik-kurulum)
- [Nasıl Çalıştırılır](#nasıl-çalıştırılır)
  - [Manuel](#manuel)
  - [Otomatik](#otomatik)

# Hakkında
Yatırım kararları, kredi değerlendirmeleri ve finansal denetim süreçlerinde kullanılmak üzere belirli haber kaynaklarının taranması ve içeriklerin kaydedilerek veri bankası oluşturulması hedeflenmiştir. 

Elde edilen bu metin verisi üzerinde isim-varlık bilgileri çıkartılarak finansal seyir tahmin edilecektir.


# Yükleme
Gerekli klasörleri sıkıştırılmış dosyadan çıkarttıktan sonra:

## Manuel Kurulum
1. "newsanalysis" klasörü üzerinde Komut Satırı açıp "python setup_env.py" komutunu çalıştırın.
2. "news-analysis-api" klasörü üzerinde Komut Satırı açıp "npm install" komutunu çalıştırın.
3. "news-analysis-website" klasörü üzerinde Komut Satırı açıp "npm install" komutunu çalıştırın.
4. "newsanalysis" klasöründeki "taskScheduler.bat" uygulamasını çalıştırın.

## Otomatik Kurulum
1. "installation.bat" uygulamasını çalıştırın.

# Nasıl Çalıştırılır

## Manuel
1. "newsanalysis" klasörü üzerinde Komut Satırı açıp "python execute.py" komutunu çalıştırın.
2. execute.py dosyası çalışmayı bitirdikten sonra "news-analysis-api" klasörü üzerinde Komut Satırı açıp "npm start" komutunu çalıştırın.
3. "news-analysis-website" klasörü üzerinde Komut Satırı açıp "npm start" komutunu çalıştırın.
   
## Otomatik
1. "start.bat" uygulamasını çalıştırıp bütün gerekli her şeyi çalıştırabilirsiniz.
