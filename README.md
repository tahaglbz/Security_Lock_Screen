Lock Screen & Security System with Python and Tkinter
Bu proje, kullanıcının şifre girişi yapmasını sağlayarak bir bilgisayarın kilit ekranı işlevi görür. Eğer kullanıcı şifreyi girmezse, alarm çalmaya başlar ve kamerayı açar. Kameradan alınan kayıt, sistemin içine yüklenir. Bu sistem, bilgisayarın kısayollarını kilitleyerek kullanıcının çıkmasına engel olur. Bu, güvenlik amaçlı bir çözüm sunar ve kullanıcıların izinsiz girişlerini engellemeye yardımcı olur.

Özellikler
Kilit Ekranı: Kullanıcı şifre girmeden bilgisayarın ekranı kilitlenir.
Şifre Girişi: Kullanıcı, doğru şifreyi girene kadar sistem kapanmaz.
Alarm Sistemi: Eğer kullanıcı belirli bir süre içinde şifreyi girmezse, alarm çalar.
Kamera Entegrasyonu: Kullanıcı şifreyi girmezse, kamera otomatik olarak açılır ve video kaydı yapılır.
Kayıt Sistemi: Kameradan alınan video kaydı, sistem dosyasına kaydedilir.
Kısayol Kilidi: Bilgisayarın kısayolları kilitlenir, böylece kullanıcı sistemden çıkamaz.
Kullanım
Kurulum:
Python yüklü olmalıdır.

Tkinter ve OpenCV gibi gerekli kütüphaneler yüklenmelidir. Aşağıdaki komutla yükleyebilirsiniz:

bash
Kodu kopyala
pip install opencv-python tk
Çalıştırma:
Projeyi çalıştırmak için ana Python dosyasını açın.
Ekran kilidi açıldığında, kullanıcı şifresini girene kadar ekran kilitli kalacaktır.
Eğer şifre doğru girilmezse, sistem alarm verir ve kamera kaydı başlar.
Teknik Bilgiler
Tkinter: GUI (grafik kullanıcı arayüzü) oluşturmak için kullanıldı.
OpenCV: Kamera kaydını almak ve video işleme yapmak için kullanıldı.
Alarm Sistemi: Tkinter üzerinden bir zamanlayıcı ile alarm çalma işlemi gerçekleştirildi.
Kısayol Kilidi: Kullanıcı çıkış yapamasın diye kısayollar devre dışı bırakıldı.
Sistem Gereksinimleri
Python 3.x
Tkinter ve OpenCV kütüphaneleri
Webcam veya kamera cihazı
Notlar
Bu sistem yalnızca güvenlik amaçlı kullanılır. Kullanıcıların izinsiz erişimlerini engellemek için tasarlanmıştır.
Proje, kullanıcı şifresinin doğruluğunu kontrol eder, ancak şifreleme işlemi ve güvenlik açısından daha fazla geliştirme yapılabilir.
Kamera kaydının güvenliğini sağlamak için ek önlemler alınabilir.
