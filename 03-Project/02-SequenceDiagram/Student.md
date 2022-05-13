```mermaid
sequenceDiagram
    autonumber
    actor Kayıt Görevlisi
    participant Bilgi Sistemi
    participant Öğrenci Modülü
    participant Öğrenci Kaydı
    participant Ders Kaydı
    participant Ödeme Modülü

    Kayıt Görevlisi->>+Bilgi Sistemi: Login(userName, Password)
    alt Login Başarısız
        Note right of Kayıt Görevlisi: Hatalı şifre veya kullanıcı adı
        Bilgi Sistemi-->>-Kayıt Görevlisi: errorMessage()
    else Login Başarılı
        Note right of Kayıt Görevlisi: Hoşgeldiniz
        Bilgi Sistemi-->>Kayıt Görevlisi: 
    end
    Kayıt Görevlisi->>+Öğrenci Modülü: registerStudent()
    Öğrenci Modülü->>+Öğrenci Kaydı: addNewStudent(name, surname, ...)
    alt Yanlış kişisel bilgiler
        Note right of Kayıt Görevlisi: İlgili kullanıcı bilgisini yanlış ya da eksik girdiniz
        Öğrenci Kaydı-->>-Kayıt Görevlisi: errorMessage()        
    else Öğrenci kaydı başarılı
        Öğrenci Kaydı-->>Kayıt Görevlisi: 
    end     

    Kayıt Görevlisi->>+Ders Kaydı: addToCourse(courseName)
    alt Kurs kotası aşıldı
         Note right of Kayıt Görevlisi: Kursa kaydolabilecek öğrenci sayısını aşmaktasınız
        Ders Kaydı-->>-Kayıt Görevlisi: errorMessage()
    else Öğrenci kaydı başarılı
        Ders Kaydı-->>Kayıt Görevlisi:       
    end 

    Kayıt Görevlisi->>+Ödeme Modülü: newPayment(paymentCredentials)
    alt Ödeme bilgisi doğrulaması başarısız
         Note right of Kayıt Görevlisi: Hatalı ödeme bilgisi
        Ödeme Modülü-->>-Kayıt Görevlisi: errorMessage()
    else Öğrenci kaydı başarılı
        Ödeme Modülü-->>Kayıt Görevlisi:       
    end
    
```
