# آزمایشگاه مهندسی‌ نرم‌افزار - آزمایش دوم
آشنایی با اصول شیءگرایی SOLID و Test Driven Development

## بخش عملی
برای پیاده‌سازی کد از زبان پایتون و برای تست‌ها از فریم‌ورک unittest استفاده شده است.  
فایل‌های پیاده‌سازی هر مرحله (فایل تست و برنامه اصلی) در پوشه‌های phase + شماره مرحله موجود هستند. 
### مرحله اول: محاسبه مساحت یک مستطیل با داشتن طول و عرض

با توجه به TDD، ابتدا تست‌ها را طراحی کرده و ایرادات کامپایلری آنها را با اضافه کردن کد به فایل اصلی برطرف می‌کنیم. فایل تست در این مرحله به صورت زیر خواهد بود:  

<img width="488" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/cc6904ec-05c9-4c4e-b946-3a1d2afb6178">

کد اولیه:

<img width="429" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/f585137d-14b4-4b18-8143-e0bd384d27f5">

سپس تست‌ها را برای کد بالا اجرا می‌کنیم تا اشکالات برنامه مشخص شود. برای خوردن به ارور، از قصد بخش محاسبه مساحت را به جای ضرب، عملیات توان قرار می‌دهیم تا ارور خروجی را مشاهده کنیم:

<img width="625" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/c5750e7f-7a18-40ee-b396-51bea821514c">

همانطور که انتظار می‌رفت تست مدنظر فیل شد. پس برنامه اصلی را تغییر می‌دهیم و ضرب را جایگزین می‌کنیم. مشاهده می‌کنیم که تست پاس می‌شود:

<img width="305" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/335ba8fa-35e1-4983-a7a1-b775fb0339a2">

### مرحله دوم: تغییر طول و عرض مستطیل

مثل بخش قبل، ابتدا تست‌های تغییر طول و عرض مستطیل را اضافه می‌کنیم:

<img width="505" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/58a70688-0ae0-4f0d-a0a3-575dab3b4687">

حال کد اصلی برنامه را اضافه می‌کنیم تا تست‌ها پاس شوند:

<img width="459" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/b7260d96-d463-43c6-bb5c-6a60d43d2fbc">

می‌بینیم که هر سه تست پاس می‌شوند و کد درست است:

<img width="293" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/335770a3-a9a6-46b1-9039-b4f9ebe0e076">

### مرحله سوم: افزودن مربع

افزودن تست‌ها:  

<img width="473" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/8f1351bb-eeff-4b80-ae3f-7658859f8733">


تغییر فایل اصلی برنامه:  
در این مرحله باید توجه داشت نمی‌توان مربع را از مستطیل ارث‌بری کرد چرا که اصل سوم SOLID یعنی Liskov Substitution Principle زیرپا گذاشته می‌شود. این اصل می‌گوید که کلاس فرزند باید بدون اشکال به جای کلاس پدر قرار بگیرد و precondition ای اضافه نشده و postcondition ای حذف نشود. در اینجا با تغییر height کلاس باید width آن هم عوض شود پس نمی‌تواند به جای کلاس پدر قرار بگیرد.    
راه حل درست و بر اصول شیءگرایی افزودن یک پدر shape است که دو کلاس دیگر از آن ارث‌بری کنند.  

<img width="253" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/0b507aa0-38bd-4788-9e76-2a4cf8491cf0">

حال کلاس square را پیاده‌سازی می‌کنیم:

<img width="383" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/cbde1221-a27e-4076-92cb-98e5a9a8da24">

و در پایان میبینیم که تمامی ۵ تست اولیه پاس می‌شوند:

<img width="286" alt="image" src="https://github.com/ShayanEmzed/SEL-HW2/assets/60621655/8f3d0d37-317c-42ed-abfc-04b2e66fb7f8">


## بخش تئوری
