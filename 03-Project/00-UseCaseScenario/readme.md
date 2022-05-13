| Kullanım Senaryosu:        | Birden fazla şube merkezi bir sunucu altında toplanabilmeli, bir şubeden her şube ile ilgili işlem yapılabilmelidir. |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Birincil Aktör:            | Şubeler                                                                                                              |
| İlgililer ve Beklentileri: | İlgili 1: Kayıt Görevlisi. Tüm şubelerle ilgili kayıt işlemlerini yapabilmeyi beklemektedir.                         |
|                            | İlgili 2: Sistem Yöneticisi: Tüm şubelerle ilgili tüm işlemleri yapabilmeyi beklemektedir.                           |
| Ön Koşullar:               | Şube aktif olarak hizmet verebiliyor olmalıdır. Kapatılmış veya yeni açılacak bir şube olmamalıdır.                  |
| Son Koşullar:              | Şube ile ilgili işlemler tamamlanır. Öğrenci kaydı yapılabiliyor olmalıdır.                                          |
| Ana Senaryo:               |                                                                                                                      |
| Alternatif Senaryo:        |                                                                                                                      |

| Kullanım Senaryosu:        | Öğrencinin Ders Kaydı                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Birincil Aktör:            | Kayıt Görevlisi                                                                                     |
| İlgililer ve Beklentileri: | İlgili 1: Öğrenci. Kaydının düzgün bir şekilde tamamlanmış olmasını beklemektedir.                  |
|                            | İlgili 2: Kayıt Görevlisi: Sistemin kullanımının kolay olmasını beklemektedir.                      |
| Ön Koşullar:               | Şube aktif olarak hizmet verebiliyor olmalıdır. Kapatılmış veya yeni açılacak bir şube olmamalıdır. |
|                            | Öğrencinin belgeleri tamamlanmış olmalı ve kayıt koşullarını sağlamalıdır.                          |
|                            | Şubede öğrencinin kayıt olmak istediği dersin açılmış olması gerekmektedir.                         |
|                            | Öğrencinin kayıt olmak istediği dersin kotası dolmamış olmalıdır.                                   |
| Son Koşullar:              | Öğrenci kaydının başarılı bir şekilde tamamlanması.                                                 |
| Ana Senaryo:               | 1) Kayıt görevlisi sisteme kullanıcı adı ve şifresi ile giriş yapar.                                |
|                            | 2) Kayıt görevlisi öğrenci modülüne girer.                                                          |
|                            | 3) Yeni öğrenci kaydı bölümüne girer.                                                               |
|                            | 4) Öğrencinin adı, soyadı, doğum tarihi, ev ve cep telefonları, e-posta adresi bilgileri sisteme girilir.             |
|                            | 5) Öğrencinin kayıt yaptırmak istediği kursa ait, kurs adı, kur ve kurs saati bilgilerini girilir.                                                          |
|                            | 6) Ödeme bilgileri girilir.                                                          |
|                            | 7) Ders kaydı tamamlanır, öğrenci bilgileri ekranına geri dönülür.                                                    |
| Alternatif Senaryo:        | 1a) Kayıt görevlisi yanlış kullanıcı adı veya şifre girmiş ise.<br>  &emsp;  1) Kayıt görevlisine "Hatalı şifre veya kullanıcı adı" mesajı <br>  &emsp;  gösterilir.  <br>  &emsp; 2) 1. adımın tekrar etmesi beklenir.                                                    |
|                            | 4a) Öğrencinin kişisel bilgilerinden biri hatalı girilmiş ise. <br>  &emsp; 1) "İlgili kullanıcı bilgisini yanlış ya da eksik girdiniz" mesajı gösterilir.  <br>  &emsp; 2) 4. adımın tekrar edilmesi beklenir.   |
|                            | 5a) Kayıt yapılmak istenen kursun kotası dolmuş ise.  <br>  &emsp; 1) "Kursa kaydolabilecek öğrenci sayısını aşmaktasınız" mesajı gösterilir.  <br>  &emsp; 2) Ders kayıt ekranı kapatılır.                                 |
|                            | 6a) Ödeme bilgileri doğrulaması başarısız ise.    <br>  &emsp; 1) "Hatalı ödeme bilgisi" mesajı gösterilir. <br>  &emsp; 2) 6. adımın tekrar edilmesi beklenir.                                    |
