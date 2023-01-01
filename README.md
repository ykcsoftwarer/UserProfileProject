User Profile

Verilen Bilgiler
Django projenizi oluşturunuz ve bir userprofile app i ekleyiniz.
App içerisinde diagramı verilen modeli oluşturunuz.
Modele shell terminali üzerinden erişim sağlayıp fieldlara uygun 5 adet veri giriniz.
Bu verileri orm sorgularıyla listeleyiniz.Bu listelemeyi yaparken sizlerden beklenenler şu şekilde:
Tüm Profile bilgilerini sorgulamanız.
Id bilgisine göre tek tek sorgulama yapmanız(Burada tek bir id ile sorgulamanız yeterli)
Girdiğiniz bilgilere göre herhangi bir last_name bilgisini seçip last_name bilgisi aynı olan profile bilgilerini sorgulamanız.Örneğin; last_name i "harold" olan profile bilgileri
Shell komutlarınızın history.txt sini veya ekran görüntüsünü threadde paylaşınız.
İsteğe bağlı olarak oluşturduğunuz projeyi githuba pushlayıp yaptığınız işlemlerle alakalı readme.md hazırlayıp sergileyebilirsiniz

---------------------------------------------------------------------
Yukarıdaki bilgilerle bir proje çalışmasının yapılması istenilmiştir.
---------------------------------------------------------------------

&&& user_profile adında bir app çalışma ekledim ve gerekli importları ve benden istenen gerekli modelleri oluşturdum.

&&& UserProfile adında ve verilen özellikler kapsamında oluşturduğum modelleri terminalde python manage.py shell alanına girerek 5 adet kullanıcı ekledim.

&&&  Tüm UserProfile ait bilgilerini listelemek için:

python manage.py shell
from userprofile.models import Profile
profiles = Profile.objects.all()
for profile in profiles:
    print(profile)

&&&  Bir ID bilgisine göre tek tek sorgulama yapmak için:

python manage.py shell
from userprofile.models import Profile
profile = Profile.objects.get(id=1)
print(profile)


&&&  Last_name bilgisi aynı olan profile bilgilerini listelemek için:

python manage.py shell
from userprofile.models import Profile
profiles = Profile.objects.filter(last_name='harold')
for profile in profiles:
    print(profile)









