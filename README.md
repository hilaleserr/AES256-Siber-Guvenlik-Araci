<<<<<<< HEAD
<div align="center">

# 🔒 AES-256 Gelişmiş Şifreleme Aracı

**Kapsamlı Kullanıcı ve Geliştirici Kılavuzu**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/Lisans-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=flat-square)
![Encryption](https://img.shields.io/badge/Şifreleme-AES--256--GCM-red?style=flat-square)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-purple?style=flat-square)

</div>

---

## 📋 İçindekiler

1. [Proje Hakkında](#1-proje-hakkında)
2. [Özellikler](#2-özellikler)
3. [Gereksinimler ve Kurulum](#3-gereksinimler-ve-kurulum)
4. [Kullanım Kılavuzu](#4-kullanım-kılavuzu)
5. [Teknik Mimari ve Güvenlik Analizi](#5-teknik-mimari-ve-güvenlik-analizi)
6. [Proje Yapısı](#6-proje-yapısı)
7. [Sık Sorulan Sorular (SSS)](#7-sık-sorulan-sorular-sss)
8. [Bilinen Kısıtlamalar ve Gelecek Planları](#8-bilinen-kısıtlamalar-ve-gelecek-planları)
9. [Katkıda Bulunma](#9-katkıda-bulunma)
10. [Lisans](#10-lisans)

---

## 1. Proje Hakkında

**AES-256 Gelişmiş Şifreleme Aracı**, hem metin hem de dosya şifreleme/çözme işlemlerini modern ve kullanıcı dostu bir grafik arayüz üzerinden gerçekleştirmenizi sağlayan açık kaynaklı bir Python uygulamasıdır.

Uygulama, endüstri standardı **AES-256-GCM (Galois/Counter Mode)** algoritmasını kullanarak hem gizlilik hem de veri bütünlüğü garantisi sunar. Bu, yalnızca doğru parolaya sahip kişilerin şifreli içeriğe erişebileceği anlamına gelir; üstelik verinin değiştirilip değiştirilmediği de otomatik olarak tespit edilir.

> ✅ Bu araç, kişisel notlardan hassas belgelere kadar geniş bir yelpazede güvenli veri saklama ve paylaşma ihtiyaçlarına yanıt verir.

### 1.1 Neden AES-256-GCM?

Günümüzde pek çok şifreleme uygulaması, yalnızca verinin gizliliğini sağlayan CBC veya ECB gibi eski modları kullanır. Bu modlar, verinin değiştirilip değiştirilmediğini **tespit edemez**. GCM (Galois/Counter Mode) ise şifreleme ile kimlik doğrulamayı tek seferde gerçekleştiren, NIST tarafından onaylanmış modern bir moddur.

- 🏛️ Askeri ve hükümet sistemlerinde standart olarak kabul görmüştür.
- 🏷️ 128-bit kimlik doğrulama etiketi (tag) ile veri bütünlüğünü garanti eder.
- 🎲 Rastgele nonce (Number Used Once) kullanımı sayesinde aynı mesaj farklı şifreli metinler üretir.
- ⚡ Paralel işleme desteği ile yüksek performans sunar.

---

## 2. Özellikler

### 2.1 Metin Şifreleme

- Herhangi bir uzunluktaki metni AES-256-GCM ile şifreler.
- Şifreli çıktı **Base64** formatında üretilir — kopyalayıp yapıştırmaya uygundur.
- Aynı parola ve metin her seferinde **farklı** şifreli çıktı üretir (rastgele nonce sayesinde).
- Yanlış parola girildiğinde açık ve anlaşılır hata mesajı gösterilir.
- Bozulmuş veya değiştirilmiş şifreli metin otomatik olarak tespit edilir.

### 2.2 Dosya Şifreleme

- PDF, PNG, JPG, TXT, DOCX, XLSX, MP4 ve daha fazlası dahil **her türlü dosyayı** şifreler.
- Şifreli dosya `.enc` uzantısıyla orijinal adla kaydedilir (örn. `belge.pdf` → `belge.pdf.enc`).
- Şifre çözme işleminde `.enc` uzantısı kaldırılarak orijinal dosya geri yüklenir.
- Büyük dosyalar için bellek açısından verimli ikili (binary) okuma/yazma kullanılır.

### 2.3 Arayüz ve Kullanıcı Deneyimi

- Modern **koyu tema (Dark Mode)** ile göz yorgunluğunu azaltır.
- CustomTkinter tabanlı, platform bağımsız GUI.
- Metin ve dosya işlemleri ayrı sekmelerde düzenlenmiştir.
- **Ortak parola alanı** — her iki sekme de aynı parolayı kullanır, tekrar girmeye gerek yoktur.
- Şifreli çıktı sarı renkte vurgulanır, kolayca fark edilir.

---

## 3. Gereksinimler ve Kurulum

### 3.1 Sistem Gereksinimleri

| Bileşen | Minimum Gereksinim |
|---|---|
| İşletim Sistemi | Windows 10, macOS 10.14, Ubuntu 18.04+ |
| Python | 3.8 veya üzeri |
| RAM | 64 MB (büyük dosyalar için daha fazla) |
| Disk Alanı | 50 MB (kütüphaneler dahil) |

### 3.2 Gerekli Python Kütüphaneleri

| Kütüphane | Açıklama |
|---|---|
| `customtkinter` | Modern ve özelleştirilebilir GUI bileşenleri |
| `pycryptodome` | AES-256-GCM şifreleme motoru (`Crypto.Cipher`) |
| `tkinter` | Python standart kütüphanesi — ayrıca kurulum gerekmez |
| `hashlib` | Python standart kütüphanesi — SHA-256 anahtar türetme |
| `base64` | Python standart kütüphanesi — metin kodlama/çözme |
| `os` | Python standart kütüphanesi — dosya işlemleri |

### 3.3 Adım Adım Kurulum

#### Adım 1 — Python Kurulumu

Python 3.8 veya daha yeni bir sürümün sisteminizde kurulu olduğundan emin olun. [python.org](https://www.python.org/downloads/) adresinden indirebilirsiniz.

> ⚠️ **Windows kullanıcıları:** Kurulum sırasında **"Add Python to PATH"** seçeneğini mutlaka işaretleyin.

#### Adım 2 — Projeyi İndirin

```bash
git clone <repo-url>
cd aes256-sifreleyici
```

#### Adım 3 — Bağımlılıkları Yükleyin

```bash
pip install customtkinter pycryptodome
```

> ⚠️ **Dikkat:** `pycryptodome` ve `pycrypto` aynı anda kurulu olmamalıdır. Çakışma varsa önce aşağıdaki komutu çalıştırın:
> ```bash
> pip uninstall pycrypto
> ```

#### Adım 4 — Uygulamayı Başlatın

```bash
python AES-256.py
```

Uygulama birkaç saniye içinde açılmalıdır. Herhangi bir hata alırsanız [SSS bölümüne](#7-sık-sorulan-sorular-sss) başvurun.

---

## 4. Kullanım Kılavuzu

### 4.1 Metin Şifreleme — Adım Adım

1. Uygulamayı açın.
2. **"Gizli Anahtar (Parola)"** alanına güçlü bir parola girin.
3. **"Metin İşlemleri"** sekmesinin seçili olduğundan emin olun.
4. **"İşlem Yapılacak Metin"** kutusuna şifrelemek istediğiniz metni yapıştırın veya yazın.
5. **"Kilitle (Şifrele)"** butonuna tıklayın.
6. Sarı renkle görünen **"Sonuç"** kutusundaki şifreli metni kopyalayın ve güvenli bir yere saklayın.

### 4.2 Metin Şifresi Çözme — Adım Adım

1. Parolanızı **"Gizli Anahtar"** alanına girin.
2. Şifreli metni (Base64 formatındaki uzun karakter dizisini) **"İşlem Yapılacak Metin"** kutusuna yapıştırın.
3. **"Kilidi Aç (Çöz)"** butonuna tıklayın.
4. Orijinal metin **"Sonuç"** kutusunda görünecektir.

> ⚠️ Parola yanlışsa veya şifreli metnin herhangi bir karakteri değiştirildiyse şifre çözülemez. Bu bir **özellik**, hata değildir — verinin değiştirilmediğini garanti eder.

### 4.3 Dosya Şifreleme

1. Parolanızı **"Gizli Anahtar"** alanına girin.
2. **"Dosya İşlemleri"** sekmesine geçin.
3. **"📄 Dosya Seç ve Şifrele"** butonuna tıklayın.
4. Şifrelemek istediğiniz dosyayı seçin.
5. İşlem tamamlandığında, orijinal dosyanın yanına `.enc` uzantılı yeni dosya oluşturulur.

### 4.4 Dosya Şifresi Çözme

1. Parolanızı **"Gizli Anahtar"** alanına girin.
2. **"🔓 Şifreli Dosyayı Seç ve Çöz"** butonuna tıklayın.
3. Çözmek istediğiniz `.enc` uzantılı dosyayı seçin.
4. Şifre çözme başarılıysa orijinal dosya, `.enc` uzantısı kaldırılarak aynı konuma kaydedilir.

> ⚠️ Dosya şifreleme işlemi orijinal dosyayı **silmez**. Güvenli depolama için orijinali kendiniz silmeyi unutmayın.

---

## 5. Teknik Mimari ve Güvenlik Analizi

### 5.1 Anahtar Türetme

Kullanıcının girdiği parola, SHA-256 özet fonksiyonu kullanılarak 256 bit (32 byte) uzunluğunda bir şifreleme anahtarına dönüştürülür:

```python
anahtar = SHA-256(parola.encode('utf-8'))
```

> ⚠️ **Güvenlik Notu:** Mevcut implementasyon tek iterasyonlu SHA-256 kullanmaktadır. Üretim ortamları için `PBKDF2`, `bcrypt` veya `Argon2` gibi yavaş anahtar türetme fonksiyonları önerilir. Bu, kaba kuvvet saldırılarına karşı önemli ek koruma sağlar.

### 5.2 Şifreleme Süreci

Uygulama AES-GCM modunu kullanır. Şifreleme süreci adım adım şöyle işler:

1. Rastgele **16 byte nonce** (initialization vector) oluşturulur.
2. Verilen anahtar ve nonce ile AES-GCM şifresi başlatılır.
3. Veri şifrelenir ve **16 byte kimlik doğrulama etiketi (tag)** üretilir.
4. Çıktı şu formatta birleştirilir:
   ```
   [nonce (16 byte)] + [tag (16 byte)] + [şifreli veri]
   ```
5. Bu ham veri Base64'e dönüştürülerek metin olarak temsil edilir.

### 5.3 Veri Formatı

| Bölüm | Boyut | Açıklama |
|---|---|---|
| Nonce | 16 byte | Rastgele üretilir, her şifreleme benzersizdir |
| Tag | 16 byte | GCM kimlik doğrulama etiketi, bütünlüğü garantiler |
| Şifreli Veri | Değişken | Orijinal verinin şifrelenmiş hali |
| **Toplam Ek Yük** | **32 byte +** | Orijinal veri boyutuna eklenir |

### 5.4 Şifre Çözme ve Doğrulama

Şifre çözme sırasında AES-GCM hem veriyi çözer hem de kimlik doğrulama etiketini doğrular. Etiket geçersizse (yanlış parola, bozulmuş veri, değiştirilmiş içerik) `decrypt_and_verify()` bir `ValueError` fırlatır ve işlem durdurulur.

> ✅ Bu mekanizma, uygulamanın yalnızca şifreleme değil aynı zamanda **veri bütünlüğü doğrulama** da sağladığı anlamına gelir — **kimliği doğrulanmış şifreleme (authenticated encryption)** olarak bilinir.

---

## 6. Proje Yapısı

```
aes256-sifreleyici/
├── main.py                 # Ana uygulama dosyası (tüm kod bu dosyada)
├── README.md               # Ana uygulama dosyası (tüm kod bu dosyada)
├── .gitignore              #Gereksiz dosyaları engellemek için)
├── requirements.txt        #Kütüphane listesi
├── LICENSE                 #Lisans metni        


`main.py` dosyasının iç yapısı işlevsel bölümlere ayrılmıştır:

| Bölüm | İçerik |
|---|---|
| Ortak Fonksiyonlar | `get_key()` ile parola → anahtar dönüşümü |
| Metin Şifreleme | `encrypt_message()`, `decrypt_message()` |
| Dosya Şifreleme | `encrypt_file()`, `decrypt_file()` |
| GUI Kurulumu | CustomTkinter ile arayüz tanımlamaları |

---

## 7. Sık Sorulan Sorular (SSS)

<details>
<summary><strong>S: Parolamı unuttum. Dosyamı kurtarabilir miyim?</strong></summary>

**Hayır.** AES-256 şifrelemesi doğru parola olmadan geri çözülemez. Bu, tasarım gereğidir ve güvenliğin temelidir. Parolanızı güvenli bir parola yöneticisinde saklayın.

</details>

<details>
<summary><strong>S: Şifreli metin her seferinde neden farklı görünüyor?</strong></summary>

Her şifrelemede rastgele bir nonce üretilir. Bu sayede aynı parola ve aynı metin bile her seferinde farklı çıktı verir. Bu, kalıp analizi saldırılarına karşı kritik bir güvenlik özelliğidir.

</details>

<details>
<summary><strong>S: "ModuleNotFoundError: No module named 'Crypto'" hatası alıyorum.</strong></summary>

Bu hata `pycryptodome` kütüphanesinin kurulu olmadığını gösterir.

```bash
pip install pycryptodome
```

Eğer `pycrypto` adıyla başka bir paket kuruluysa önce kaldırın:

```bash
pip uninstall pycrypto
pip install pycryptodome
```

</details>

<details>
<summary><strong>S: macOS'ta "Tkinter is not installed" hatası alıyorum.</strong></summary>

macOS'ta `tkinter` ayrıca yüklenmesi gerekebilir. Homebrew kullanıcıları için:

```bash
brew install python-tk
```

</details>

<details>
<summary><strong>S: Uygulama çok büyük dosyalarda ne kadar bellek kullanır?</strong></summary>

Mevcut implementasyon dosyanın tamamını belleğe okur. 1 GB'lık bir dosya için yaklaşık 1-2 GB RAM kullanımı beklenir. Çok büyük dosyalar için chunked (parçalı) okuma ile geliştirilmiş bir sürüm planlanmaktadır.

</details>

<details>
<summary><strong>S: Şifreli dosyayı başkasına nasıl güvenle iletebilirim?</strong></summary>

Şifreli dosyayı herhangi bir kanal üzerinden gönderebilirsiniz (e-posta, bulut depolama vb.) — içerik parolasız okunamaz. Ancak **parolayı asla aynı kanal üzerinden göndermeyin.** Parolayı yüz yüze, telefon aramasıyla veya ayrı şifreli bir kanaldan paylaşın.

</details>

---

## 8. Bilinen Kısıtlamalar ve Gelecek Planları

### 8.1 Mevcut Kısıtlamalar

| Kısıtlama | Açıklama |
|---|---|
| Anahtar türetme | Tek iterasyonlu SHA-256 — zayıf parolalar kaba kuvvet saldırısına açıktır |
| Bellek kullanımı | Dosyalar tek seferde belleğe okunur — 10 GB+ dosyalar için uygun değildir |
| Parola hafızası | Uygulama her açıldığında tekrar girilmesi gerekir |
| Toplu işlem | Birden fazla dosyayı aynı anda şifreleme desteği yoktur |

### 8.2 Planlanan Geliştirmeler

- [ ] PBKDF2 veya Argon2 tabanlı güçlü anahtar türetme
- [ ] Büyük dosyalar için parçalı (streaming) şifreleme desteği
- [ ] Birden fazla dosyayı aynı anda şifreleme (batch işlem)
- [ ] Sürükle-bırak (drag & drop) dosya desteği
- [ ] Şifreli metin için QR kod üretme
- [ ] Pano (clipboard) entegrasyonu — tek tıkla kopyalama
- [ ] Çoklu dil desteği (İngilizce, Almanca vb.)

---

## 9. Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz lütfen aşağıdaki adımları izleyin:

1. Projeyi **fork** edin.
2. Yeni bir feature branch oluşturun:
   ```bash
   git checkout -b ozellik/yeni-ozellik
   ```
3. Değişikliklerinizi commit edin:
   ```bash
   git commit -m 'Yeni özellik eklendi'
   ```
4. Branch'inizi push edin:
   ```bash
   git push origin ozellik/yeni-ozellik
   ```
5. **Pull Request** açın ve değişikliklerinizi açıklayın.

Hata bildirimi için **Issues** bölümünü kullanın. Mümkünse hatayı yeniden oluşturma adımlarını, işletim sistemi bilgisini ve Python sürümünü ekleyin.

---

## 10. Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Ticari ve kişisel projelerde serbestçe kullanılabilir, değiştirilebilir ve dağıtılabilir. Lisans metninin tam içeriği için [LICENSE](LICENSE) dosyasına başvurun.

---

<div align="center">

🔒 **Güvenli kalın. Parolalarınızı asla paylaşmayın.**

