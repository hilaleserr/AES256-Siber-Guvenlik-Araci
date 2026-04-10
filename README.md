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

</div>
=======
PK
     ���\               word/PK
     ���\            
   word/_rels/PK
    ���\ƚOe�   !     word/_rels/document.xml.rels���N!�_�pﲭZ�)�1�Y���?qL�}{1v+5
��93��29���fb��hQ�EUs�m;b/�[�r�ȷ��+L��DFX|�A��=	� F��:���7�b�{�~W=�e]��O=��'۵��]��9:�����Qó� HWV�@�	BtT� �������/K�ǃك�w�%8K9�ے�����3���]I��ì��f����4��ª$��滕 �J�l��� M�I�!��_�|PK
    ���\�)|%�!  ��    word/document.xml�][o�F��+�^ �[��K�;�	|�^�o�d&�Y�*$��b��i���<���`�z���4��or��������T)ɖmIfw�RAڶ(�H�S�չ�Ͽ�1
��	�ŋ'����\�^<��`kn�	I>
c�^<�X���}��{iĄ"���UKĒ6C��M}���/�7�����������I[���Z-��,�I5➌��PU�8�Ň��c�7��k������#c�%	<�:G4ɇ�.�w��/cQe�Q��9�Co�ƞ_·�_<I�xn��+/yn��ʯ����\�a���X�,�g�E���kL;|�� 9��%���ς���x�!���p����EQh�����cp�(����?ID���x*���4� ��tZ�cζ��N4~��^��
��cY&�Zr���o�N�����;o�浩T����� Y�=��\�1�@�����&j��Oui�1���.�4椾8҈�[�n��呞N7���V���t 	�������GxZ�b��
}0�/{l�呯��Xk^�}p>����,�����aH|�'��cs
����i�q28����E@#|�������'�Wҡ0��yN9��	|j2؊��u�\�3���
_<�`Cg�֊q�;f7?�ٲ�6�'��j��
�Q? ܮ#Y��{�����̹�^�>�ď.�b��Qi�q،V%�!��%M�j������H���M���z�{q��)�O6Wr��G���e��H�������2�f!w�?���!Ho,bdUR��trb��br�s1�n���l\$fc�21ͱ��C;	���S���!�@=�4,u���d��4�Gi7IW��/{�f�{x�u�V�����g
˖�p��WPg����?4J!�T÷~�*ƏI�œEsq��$�7c��h�+$o�'� ����|;�%�a�Ն�-�����z�7
8:��n�P�R��<����cX��F��}�c0r�7�r�5�3s�%�
}�������BFeN�]*�d�H����w��u}q��^5@�:W�P+���gc�� ����V͏��������]�<B��Խy�
�1N���y7����N�
v~����V ��ߛg���Vck��ޱ෱���4_�\���Y,�N=��6�6�6��~K����|uޡ�C����_��a���{�����:��Ȼ�C �v�	��e�
�P]��������{!U)�0�a�=���s��o�YQ��Y�%���4�GZ8<vx|O��F�m����B����X�!�hx~:��ف�� ��o^��ޙ�u�T��;�v}O0z=M� �0K ���?G����� �A���������L�����C��k��ڈp�Κ/ǘsk�
�O�	���0o�O�|���%�y�}��,���b����7
�8<��ɻX���0n���9��w��ܦ�#�<Q{TҖ���y�F�L��y��w��b
�G,.�ā�!,���	-��Z�d�#/i��
�:��B�<Z��Ӳ(��$
 �y4���T�a:�3��;9y���t+G�I){����#*�Nn�1�f�UAC�e(q��v'��v�O�1�0Q�!���i@�c4V
�[�����(��#��^�!L �¬U�'@�M�e
���3��"s��z�L*r�H���=����ϒ6�H��/�?N2J��g�z'��]��� �`H�څ�t��tr�V���%�9�]@(�u	���|X|-&{'�u�t1�2I��qH3�=�;Ah&h���8��uK��v�����Oe�1q��	�w�(pL!0	� C��m�<���)���.�j�аK�4��]�o��@s�Ż!GA�N�#�ij�{g�ǽ3҂���	�9�+�d-�%
a��G���i%*c�%0��;$�y����''f���ǌ��wǬ�~Ϗ9A���)̓����*��:�O���y�`A�~���qx�@�*�_Q����`�[O�zc$��w�>BN�ڛ�
!0l\�|�������js/��zc,�����\q�
��խ���z�6���J�|1��>W?�q�����и��0���W��[g�d��g�B"bX�[d�&	MH����L�La ����~���C�p�e`��	l����ݡYHA,�����^Z���p7W���H9��ຍwlQ6'����KC�/||Q�
����{��:y�P~��xL�6"��$I����z'q0 �J��RI.7X �1(o����) �l���9MNXh�V��B��Ҏ=<;�07+dx�n�\-��:|!�`�� 6�b����}���>$N31K^��? 
��P�<��׺ �
��
�𧟎!�g\Xx�ƅ�$`����0S�"	�ʪL�*+��\&
h3
��J����ޙcFĮ7V暰�.-�n �HE�֌^b#4�Wvp�:��Ė��N(��0#<F*�Ө	��M�|��)��
@:c�^94C�5b	��R���2��訂�:f�e� �� x���
��k\4`\�P�I]�Y$�&���pڨ���NXo����m��f�8P��^2٦�ŵ �vS�����@�4�"L�Ҵ�J���Мh3��}x�&ly���Z�q��/?� �6��K Բj!p�
J�l�)!�)!ZP2xTErώ4���.	P+� E*rXN+�ǧr���V�-�Zh10�w����w��p�$m����W�6�8&�sg8��Ô����Q
\��!c���i����L��K]
�a��N�*Y�ؚ%{��g�?����?̒����0K���>���[D��i����
���x���l��3Z���'��.���*H�T(��K�4$ԇO�|T��{+B�0�j�?$�����'����r� ��]�ӀG!F�`�0n/
�[h�D+LȄJzgHSCc�
��K!d����UA�q��,,#Riod6C� �h-�݈�̰�`%'�#,`��@�I�@�
&Xƣ���ͮq*q��3��Jf��1�m�d�l����8)�]�����8<ʫ'�6��9K:��i�s�$#��.��散{Is_+�Gy�l?J��D(�bh-��
ذ#�W:�Â��ɚR�ymyD��g�R�m��`p�,�TH��L�U���Łr��ҕ������D�9J%�v�!�jc��&�Z���Ņ*))��	�
�:��!F�4-ֺ��������L׽�u�[���\��[L`׽�v��ō3�E����7�0�+L�!������h�P<�b��:�LvE�>Jm}R�����j}q�|�L�JI}�:��Z�8�~ 8m�8pv�|O�y��b��La����?
��� �A�=���E��F*��K�PL��ā� �
�dU��H;��' �4�A:���A�������� ��J�97�u�L�X�C�W�b��a�����c(�cV����"С$u�&�@1������-���ǵ;�����0��N~�Ѕ����i�����W���糧�X�M�!;M�Ni��EA��[���l��m�%&\��
��B�t`�����u'�d�Q��,���a�]���*q���X�2%�u=����fҹ�R? �v�����SMpE$\�w��z�Z�D�;#��b��nӤ�Cl����_�ꖄTж��0 S���b��n�J��`?�6���zѼ�Ck������!�C� �����&>� ��.~o��
d�??���[;[����֥�t\X\|��y���#�8
��z��Qچ�鍴|@���Ջ\��1a:"%�P�&�����c��"l���w�~5~  RQ%=f5�-B}iZ�?�4�
X�[%yI��_I9o�j,������@6��v��U�Ϲ�b��z��'	�0Sw��(U!
4|Q�z�B�O�E��n����f��� �qr�+N>�@��]g;4��V	�\� ���,i�{������q6ы�lc�Q�>�X&��;EfĨy�q�(����gcr�ǩ�L���MN�
������%�����p}~�Yc�D��t��X0�I�>��ϥ2���>s��8��'�%�`��{S�49h-Z4���b�n��Nw���0�&Z�ىA��F�.FR��(܈r�ᆑ� :ڒ����)�2
�6���}'�}�
P7ÐEd�B�J���w7��r���L��7��q�e��O7G��js/��zc,�����\qɵ�ͭg�O�0��s��U����W�ˊ�4�����fOW�F� ������ￓ!���"�l[A�9m0�9�nUI��4�M$�䈂Ozo�*"c*rl,�3;������`���9��kQ
_�d�h"�-@�@�u�b'%L��
;����Ԛ� 4�wB@��3ŗ��� ��-׍|�;k �����{�#M��G�J#���:w=O�ƞ�{�,V��s�A��Qڽ�j�<)�X'��V������ʄD�M��)b���Rc�8H�(;e�Qc�wCNVmdeOw$�����LP���N�q2n��3Je��S+_��
U�3�Do�y�@s�(���;���ң�}˔ Ԭ$���O�
�:}�}�]�Y�dxy���bF��Jf�,
Ī�{r�b�T����;s�/���E�D�ZW�ą����{'ëE���v�q =��Y��1%c��J36�\���E�Ɛ��p�������V��+T�ae���.�fN+��EcX�L�5�HA�k���i��Y� ����]����Lj
�|X1�R�h�D��N��$�A��M��u"@!)x,���������:���~4ﭑ�`�ڧ�P��j2 z�A�J.!p�cp�����,a�:���zgh:�V�Z��3U�x0k�3�b�Ljy�k_cW��!���@ZpK�8a0yJ��:
����91}g��9��t߉o�kf��&kFZh�vTT� ʢ�,���| ��eS���@e�f{��΍)�F4��O1�t�Y�
���0�/�Lx$�,���MV��K���&g��O']'-	C}s�[1N$���7�-�����o�z��]�}��"ʅ-�����("[�G ���(�%�¦=��������'64>�uQ�.󁛡3;����`��w�`l��~MwS�_@@���	�[%�y���:���7��+8	���^�/�8IE��+e�q̽.j�t������*9`�����E�|�(؇�{s�SE/R�^�=\]������v��s��4A-+���٢F.:�9�E��d������&W��� �L��2��N�.��w����ފ�ٻc�k���%�O����_�����h��b��Tέ�?gF5q�������">�#/U�G�5��	�<�D�Q I�b�2;RDEm��/���dg��]5K
�{k;[�Y����&�cU�bр
���G�������;��A��Y�&f��F��0�6P���^���M	=?��\�Ɲ	�����i�S�_��H'��dؕ,��t@��>@���P�`~�;��I���1:gU�/_ÝZ@tR_�B61� �p�G��*c���b93��ӱ`|���D�5�L���r1�Nµ�[W���
�屠P&�<�D�#������4@ �HE����x�ǌ�l�Lp`Hj3d�V����\>'�@e�4�'�)�#0�"�\��XT��RҦ��)1�L��.�^�_��a��UG�(�!y�7'�^'�.
w[6�l$
���n�\��d�?����[��O���`�|\�F[���2k�$��v����#�SS_Z^Z�w��
Cb�36�R4�a����V6 Ů[� ��دQ�r@<��u
�>lð�>�٫��0��b��`|@��.p�w}.`;����}@[�\�C�F�ƕf�Y�ԭ(��ǽ���@�n;�~ �]�q}{mS�����o��0ċ�\y���Y�MÛ;�:�vx}��� �|B6ݾ���{�6o�|��
��&��G5�g�L,H�ڧ�7��"ɓ�m�#F6
Ũ���Xr!�{��v	�f&�$��4&�!��H-]���U����Q� �0R���9J͸��Q
G�^��u�P��x5f���=��x�aV���I��0e�R��9���A{:��dl?��{��8�f�GH�i<]�4�fc&�_0f��Ȼ\ϵ�� 	�nէ!K�L}qiu��ę_�J��h�*x7lLm,�-�bQ o('���e6�x�O��1l��j?O[���@2�L-!�2��1�4�PD� �]�%�fBq�*�&4<�X��!�M0uv��l/]�*=�}�J�tGm]-?�"����^CBʒ���\bV�=^sD�=�巟���-D�����
@5�;�^Q@2"A�fj��t��jG�uD�~�~�����Y��
sā���t䝞���9�R�!'U��*�KQ��B�����%Sd�:J�l)����������K�P��@���Px�d� d����|��� �C��i3�Q�¼�3f�N��Qޢ�C��.�{�Y_I���@1�/���>`h��dR�`����T$���Z�/��E)����yk��2ƪ��G,Ih�Uff
Cbqȱ�v\�q;a���|v�(��߼";������i��� ��!Bղ�Y�(�Iu"ͣ��l2S��C�d�V�>ʳ��6��ߒT���']b��
Wy
�e�Ǡ���⳥�K�iq�bZ����m�(�t�N�FUS�)���S��g<��1�_b�RY�NC��Է'��8���0��켅�鋍�f�D��G��o�C�̈́�8�3l	7*�?�q��.�jM�{��ӿ]
��v���ZB�}YM�5��Ch��3A�B�L�[�w���q���D��̳mpZ�2�"(hJh������G�gC�&�����	��*�� :��:h�M �,I{u)�@r��`����m|g�[gc��� �����u���T�:4�9y�Z`@0Aaz�u�c��;�-ٟam��C%����eV%�Lk#���hj�M�A��h���c�����D����@�wEp'6!vx�p�(�C\xL�p������Ɨ�c!��Z���<�f ���P��n�M5�Rqq�9:~�준[K���7;;�j�����(�r^1�	 ��2H0eI�](��g�۠N��i��F	�)ٛ���g%eS�����0����ՎŜ�
�@�}�HQI�w O����!a���v=|*I�>����~TZ��B�-Mu�S�*h:��Gb᪤N������LS5S�<C�*���5�\���nA�H��*��y�`��k�" }�J�N�g��;Q�t��`�=>E�kJF5���
������*�hK���an}�E��ٗ�	�2��L���2�� mY�w�5�/�
;���V���Uas����f��������A�Y(�����pN�JV�G���4�Ͷ>�����K�Vl�F{�� �&	���P	�'F
�}�@B�R���Y�C3�4�t^���t/�J��a�<̙磬�V7�����R1���%^ o=�Q2L^�P
*�^�b�����`�Z�F�n���B+���}Z̆Hs� -��y��
��5�?�ِ+Ræ����Aj�tƲ���X�?�4��A���m���@Y�	��
$�]��[%𩥅�¸�XSk��EJ*M�����톒���A
��Ģ�U�� � V� Ko�Jq�FWCs�a
�ҍۆ�)�ͅ��8띄��Km����m*LB��(�h�;3
�J��&֩Ҿ���
t��`���8l�ǁr8����A��X�$ �D>�Q�3�˸���n�';�	L3 �/_��[��%�"&/�fL�?C�P�e�n����m���"�_��r��þ�_9�U�xȻ�%�aD�g��B�w�޲��ҭ�Ϫd����D�5�>&�ZJ:XF$C��%�Պ�i�2a�Ab
�w�:wۧ�m^k�.�XAc��
�~p�}D�cs� ;	��Zr�����l��CFU*iJ������9iqE�6�8Ud�Ib\�2�v�~p�(��m�� H�*�]N�8��8�-3́��F�i&ڜ X��s��K9ۂ^���)�4i�D�%oa�S�>��>��!���9qָ�Sy^�sx�Pۮm�\�G\��%���9�#n�WIT�+{輸�Y*�dp4a:�WG���GS��Dt@B��f�EI�$(ZE<��"�{3��Q�y��#�[6���t�;�k�競 �cT1�����0�����ĥ   ܣR/� ���C��!� ���\0)���M���J���⼜h:�L��F����,���RQ��d��8�^6y�!�<����ᡭI~�y���Q�������F����?�D�v�h��d� �Z�y�
Ƌ���)�O�}|B�l�h,j����b��H
�K%)W�:�]�o���5�ꊹ�����MA��
@�,}:�;
Ʊ��J��8���ud�?���ՔqH.�W^�'�N�����L������ PK
    ���\���<�  �     word/styles.xml�XmO�0�+Q����(�+�@Bb�}v��H��v(���I�4�
-4�i�D}�>�瞻����siO�qL�H��L]CR��H��}9�5. �AD	�/���g�!/�Z��
B�Gһ�\miy�&Q	�p��B$C��0D1�G4AD:�b �-���4�i� ��8��ŰMsP��]Ph`�.)LcDD�}��H"R�C��m�
ڒ2?a"�e&�h�LJ�m �2�i �$Q%�n���8Zxo�
�,�>��( i$x�d�L-�*�3�Dpm9b<��y�rye� c�A��	/��ڿ��	D#ݶ
˄o�u�Q')W�]���J�P�%�%� $aH��G�=ʉ��ܕ5g8���-�R�Nгh�������iz�&͕�B3oW
Wd]e5X(�f��҈�R���ի+�(�ԕ|E���}`�v��v*:���h����E����E����'E�/���h�'���w���3�Ag����{��!%�F���c��V^?�
�sq[z�1g^m���:��0`(�@lSp�c&�M�KO���2-C̮����2L�|P{OO����G?CD$Vg!������)-�ٓhu�nOx;���P��P��|o6��@��X��/���
�>"[2!��b�EyO�2��}z�`/����ȼۊ-���^��ȴD�� �������*2:�h�]5��.�F �
�����x[�f˕e�QO%�zV�
Z�C[gg�r�Jto������nC�
�b�)V�~s�U@��N�3��T�{鳪tW�}��U+�����]S��Ȋ��)*o�ֲ����GY�i9>v��)�iԜ>���E�İ�
1�n1�OÞ8SϬ�a��t�^�����N16;����D1�=������'~� PK
     ���\            	   docProps/PK
    ���\���<;  �     docProps/core.xml��]o�0��
�=��s� &���L�L3���=j3�����+���7�lߧO�s��d��:�U�҄��\�m�V�y��"���
Jt�fU�Lδ�w�
X/�E��\�L�vޛc�v �K�B��VR�v�
e�t
xD�K�SOq+�MoDg%g���غp��	�;�&)���twtɀ��
�E/aO����i�&���?����G7j,T�)�*8˙국V*VT/��]`M�_�Mo���������h�R�vD,�C����P6?�vI>����U#2��d�d�N�,'��8�~��nW�<���uL֋����8�/PK
    ���\���ѫ  �     word/numbering.xml�X�n�0��@�1EY^ D	�)\t�~ -�6a.EI��zk�E��~IIْ�,��PN493�=�pH�痷�99Q)�"����H�TLC����l�Tcc&	������D��D7�G�h*��cf
�;�9E�|�t�E�`�u@�F3�q��4R2�݉$�r2���T1�\䖟%#����59N+8~M&D�D*����)�Xͳ�̠'X�1eT/�ۯ`d2%��Y-ȆKA���P��.C�d�q"t�aF��&�m4E3�Y�?����u	�\
�.̰�G~��l��iD��Q
QG�#a��R�1k�F��H.���$���F�,Y����Fb^c٦? kU�ͭ�ǉ�<�	����T+�w�f��\]�^;�"�Rvqy;��h�^)��!pK�1Mߑ���EBP��Q�+��6fm Z_�3�@�`�Km���rN,��)�*��3��5��cD׈7�6���^����UF&+�䓲����<�$�a1-/�nߵ�p�K�]��4�*�~��I���y�z�����x�a�~KN��@}�%'��6��~KNN�mҵ���4��aK�����n���|.���\~������ ?��I��mo�cQ�ك	|�:'�����2o��n���Q��	�����6i!I���a[G���r. �'��8�������
PK
     ���\               _rels/PK
    ���\����   �  
   _rels/.rels���J1�_%̽;�VD�i/R�M�>@Hfw��&S�oo(�V��C�����7C�CةW��S�0mZPmr>��������'���2�\Tm�E� ���(�ҤL��t���z���/�'���-�O�2��i����ھg�����[zHv(ʙ'~%*�pO��-�C�Yn*���r��'�@b��61M2�nO�[��<�r9&Ƅ��\��#7�dr3�����I�3_Jx�1�PK
    ���\�����  8     [Content_Types].xml�V�N�0��(WԸp@�����\{�b�eo
�=��!�R��e=3;�F������B4��i1�3p
�q�4~�]�W��Ӈ��1��i� �BD� +c�#%+��P	/ի�@����B�#p4��#�Mn��MM���<����&�wU�ݾ��*N��^ŋ���=���'����"���);�T�W�eu���Q�Y�Jz_%��b���9��3(�-'.���� 9|���ɰ,����,)p^6�٠�I�5Q{m���h����*�������Ҹ��<�@��ro��bKY�� 9"}�w Xa���,�� #6����』�F���|a�DB{�uK=�9�mҠ��փN�5v��w{
�D$�Էq[x�<�=6谟�S߇�F ���&�'�x����з
kxB���OPK
    ���\Xy�"�   �      docProps/custom.xml��A
�0�᫔��T"�i7��Eu�ihfB&-��F�����k��_�
�8&
ǲ����h���o�
�
faB
;
tms�0&�Rd�DÜR��;�7R�L���Iy�I�8:�W��GJ�TUgeWI����׫��/9����g����
PK
    ���\���ړ   �      docProps/app.xml��A
�0�᫄�m�
�Ҵq���ɴ
43!K{{#� p������BbO�屪� ��<NZ>���"g��,���,���'��� @�r�96J��!�J�RFJ��2Ӥh��+�W ��T�g[t�� ʯج�_ԑ�������
PK
    ���\��ɑ�  �     word/footnotes.xmlՔ�N�0�_%�uRZEM9�@��} �8����l'�o���M�,�
=q��f~����w��V8/�$[�$�C)ͮ ~?,~�� fJ�����'��u�W �@>A��ygyA�lN����/��<Ta�AS�*����t�f�0�����1�2O"N�O+V�4
�t;��{k���*�{d�7 �q&���$�w�GAq8x�s�.��-L"R'j �ki�4�K��� iO%�jE�dW���ޱ�x��rt�jT~���gt�GL�H�7�A�f�́�U���f�_�>���<:h�L��ў����/�X��ǩ���lkf�j�?�8��P�,��'�oM������ޢ��9�ܒeA�`h�ϳ� o�h�� �v����}Ϋ�i���!Y��͚N��'ηa���-Sy�j^D%��":F�j>��n�=�A3��>M��	�4�+���z�2�4�SU8Z��_PK
    ���\�w��m   {      word/_rels/footnotes.xml.relsM�A!E�B�w�.�1��n`� 
V �Pb<�,]�����~�n>�4qp�,_�I���};\`]��ԇ�1U5#u{�WD��3�T*� ��2�1[�J�M��d��� ��PK
    ���\?J���  �     word/endnotes.xml͔�n� �_��>����ʊӋV���� �Ǩ� ����w|ζU�67�1��o��1�o�j���y	� �2%�0Jiv���a��l�].Li ����ygyA�lN����/��<Ta�AS�*����t�f�0����̴̓	����
��8�.ݎj�^�@�eA�H%����i��'�"
�]�Q�4<�9qG�;��&�
5��s_��a}����h�"���e=�s��a�#�����&f����	��<(�L�9�JsT���� �� ���9�4v���h��5���kj�qj�21ۚY����;��(T�-K��I�[��'��h��e�p�dY�E6�������[�1 �*��io�d���*.��>"k�Y��>~��6�U�e� ���gQ	��&[O��������Q�L����۴�����OT`���?PK
    ���\�w��m   {      word/_rels/endnotes.xml.relsM�A!E�B�w�.�1��n`� 
V �Pb<�,]�����~�n>�4qp�,_�I���};\`]��ԇ�1U5#u{�WD��3�T*� ��2�1[�J�M��d��� ��PK
    ���\M��ʡ  s     word/settings.xml���n�0�_��}"�X���[t+��b�E� `%�"Q�$��ۏ��?@�4W�A�;G�����d�
Q;�X��Y�P8�����??V_Y��PUl�"���ʨR�C1# �r�bmJ��<�VY�k�Ep��i-�宮�P|pA��w;�P1�;`��q�=�y��]���34�B�t~EtI?k�Ӗ��Ռq��{��`hL)'C�e���N)�NtVa�)�yp[�k|�F�v��]���ZP|9� �Z�1��d���cb�ёq�8��k�ى���J���i��� ߜל��:���y�G�X�>��o�˫���<���ZQ>6�<rD-˨���[�q�H���7��j�r��ǐ�ޡ�-�O��Y6�=���`�b�3ӔXvO� �O�����_
�_N�1ԅJ>J�E�/���?PK
    ���\��9��  �     word/comments.xml���r� �[q8W�XS7Ӵ'���x�
���4��ѻ_R%I��N�G�$ߓ�����I4�#5�+Y�|���X.�5x��܂�uH�(Ikp�<=>�VBP����V�T朮 ��Q��Jpl�U;���B��qL!1��6,��b���'��ld�m	P��"���l��]��K�|�HڤI�Y\�&�t�&�ci�&E����4���N���i�P �y�Kk�� o�;{3+���LH�zA��l�
Eh�&AQ58Y]��|���_?����ȳn;���.���k�י���, ǟqM�������*C����o�(L��>_��)�����g1�&�#�OL����!��o���jF��� Pb:����j@<�����Fp���d䤅�8�f)E�v��!�,�t^�MϝŨ#��m#�uЃ�o�^�c���������ma�0�)��PK
    ���\�w��m   {      word/_rels/comments.xml.relsM�A!E�B�w�.�1��n`� 
V �Pb<�,]�����~�n>�4qp�,_�I���};\`]��ԇ�1U5#u{�WD��3�T*� ��2�1[�J�M��d��� ��PK
    ���\c�^�  C     word/fontTable.xml���n�  �W!�+���i��,Kv�= �D���Է��k�����|l�Wp����+�Zf��P[�����b�E�t�M�o��~���5�H,�=��*��ؖB�jHZbk|��1����d8�ۅBhe� �l��<�
�`�+
ֵU����}^㒈��Ҡ]^�.tP��1�� ���Y�=A`U@�:.S3��z*�WY� ���P(s�gl�Hɩc�<��'���� ��nf)�0W�ee���f*�yE�G�݌@��G�A\���YZ�av�\w��2���_PK
    ���\�w��m   {      word/_rels/fontTable.xml.relsM�A!E�B�w�.�1��n`� 
V �Pb<�,]�����~�n>�4qp�,_�I���};\`]��ԇ�1U5#u{�WD��3�T*� ��2�1[�J�M��d��� ��PK 
     ���\                            word/PK 
     ���\            
            #   word/_rels/PK 
    ���\ƚOe�   !               L   word/_rels/document.xml.relsPK 
    ���\�)|%�!  ��              �  word/document.xmlPK 
    ���\���<�  �               ]#  word/styles.xmlPK 
     ���\            	            
'  docProps/PK 
    ���\���<;  �               1'  docProps/core.xmlPK 
    ���\���ѫ  �               �(  word/numbering.xmlPK 
     ���\                        v+  _rels/PK 
    ���\����   �  
             �+  _rels/.relsPK 
    ���\�����  8               �,  [Content_Types].xmlPK 
    ���\Xy�"�   �                t.  docProps/custom.xmlPK 
    ���\���ړ   �                7/  docProps/app.xmlPK 
    ���\��ɑ�  �               �/  word/footnotes.xmlPK 
    ���\�w��m   {                �1  word/_rels/footnotes.xml.relsPK 
    ���\?J���  �               �2  word/endnotes.xmlPK 
    ���\�w��m   {                �4  word/_rels/endnotes.xml.relsPK 
    ���\M��ʡ  s               55  word/settings.xmlPK 
    ���\��9��  �               7  word/comments.xmlPK 
    ���\�w��m   {                �8  word/_rels/comments.xml.relsPK 
    ���\c�^�  C               �9  word/fontTable.xmlPK 
    ���\�w��m   {                �:  word/_rels/fontTable.xml.relsPK      |  �;    
>>>>>>> 0e71fc0 (AES-256 GCM kaynak kodları ve dokümantasyon yüklendi)
