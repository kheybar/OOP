"""



نکته اساسی:
زمانی که ما یک نمونه از یک کلاس میسازیم، هز نمونه(اینستس) یک کپی کامل از کلاس است با آدرس مجزا در مموری



در شی گرایی پایتون دو نوع متغیر وجود دارد
class variable:
    متغیرهای کلاسی به نوعی از متغیرها گفته میشود که مقدار آن در تمام آبجکت های ساخته شده از کلاس یکسان است
instance variable:
    متغیرهای آبجکتی به نوعی گفته میشود که مقدار آن مختص همان آبجکت است و بقیه آبجکت ها به آن دسترسی ندارند
هنگامی که انتظار داریم متغیرها در آبجکت‌ها ثابت باشند، یا زمانی که می خواهیم یک متغیر را راه اندازی کنیم
می توانیم آن متغیر را در سطح کلاس تعریف کنیم
وقتی پیش بینی می کنیم که متغیرها در موارد مختلف به طور قابل توجهی تغییر خواهند کرد
می توانیم آنها را در سطح آبجکت تعریف کنیم

Class Variables:
متغیرهای کلاس در ساختار کلاس تعریف می شوند
از آنجا که متعلق به خود کلاس است ، متغیرهای کلاس در تمام آبجکت‌های کلاس به اشتراک گذاشته می شود
بنابراین آنها به طور کلی برای هر آبجکت یک مقدار خواهند داشت مگر اینکه از متغیر کلاس برای راه اندازی اولیه یک متغیر استفاده کنید
برای استفاده از آن در خود کلاس یا باید از آبجکت یا از خود کلاس صدا زده بشوند
خارج از همه متدها ، متغیرهای کلاس ، طبق قرارداد ، معمولاً درست زیر کلاس و قبل از متد سازنده و سایر متدها قرار می گیرند
درست مانند هر متغیر دیگری ، متغیرهای کلاس می توانند شامل هر نوع داده ای باشند که در پایتون در دسترس ما است
متغیرهای کلاس به ما امکان می دهد تا متغیرها را بر اساس ساخت کلاس تعریف کنیم
سپس این متغیرها و مقادیر مرتبط با آنها برای هر نمونه از کلاس قابل دسترسی است
یکی از ساده ترین کاربرد های کلاس وریبل ها اینه که ما می توانیم بفهمیم از یک کلاس چند نمونه ساخته شده است

Instance Variables:
متغیرهای آبجکت متعلق به آبجکت‌های کلاس هستند
این بدان معناست که برای هر شیء یا نمونه از یک کلاس، آبجکت‌های نمونه متفاوت هستند
برخلاف متغیرهای کلاس ، متغیرهای آبجکت در متدها تعریف می شوند(مثلا متغیر هایی که در اینیت تعریف میکنیم)
هنگامی که یک شی ایجاد می کنیم، باید این متغیرها را که به عنوان پارامترها در متد سازنده یا متدی دیگر ارسال می شوند، تعریف کنیم
مانند متغیرهای کلاس ، ما می توانیم متغیرهای آبجکت را به صورت مشابه فراخوانی کنیم
متغیرهای آبجکت، متعلق به آبجکت کلاس، به هر شی یا نمونه اجازه می دهد که مقادیر متفاوتی به آن متغیرها اختصاص داده شود
هیچ آبجکتی به اینستنس وریبل های آبجکت دیگر دسترسی ندارد
ما می توانیم کلاس وریبل ها رو به نفع اینستنس ها تغییر بدهیم. یعنی بیایم و با استفاده از اینستنس، به 
کلاس وریبل دسترسی پیدا کنیم و آن را تغییر بدیم اما برای دسترسی به مقدار جدیدی که مربوط به اینستس است ما
باید از سلف استفاده کنیم تا مقدار جدید مربوط به اینستنس خوانده شود و اگر از خود کلاس برای صدا زدن آن
استفاده شود، معلوم است که برای ما کلاس وریبل اولیه را میاورد. اینکار باعث تغییر کلاس وریبل نمی شود، بلکه
اون آبجکت یک نسخه از کلاس وریبل رو برای خود برداشته(کپی کرده) و تبدیل به اینستنس وریبل خودش شده
حالا که ما اومدیم و اینکار رو انجام
دادیم، اگر از "داندر دیکت" رو دوباره صدا بزنیم، کلاس وریبل رو با مقدار تغییر داده شده، قابل مشاهده است

استفاده همزمان از هردو:
متغیرهای کلاس و متغیرهای آبجکت اغلب به طور همزمان استفاده می شوند
اگر ما بخوایم با اینستنس به وریبلی دست پیدا کنیم که در اینستنس وریبل ها نباشه، رفتارشون تغییر میکنه و
در کلاس پدر به دنبال آن می گردد. زمانی که ما از سلف برای دسترسی پیدا کردن به کلاس وریبل ها استفاده میکنیم چون
در اینستنس وجود ندارد، در کلاس پدر به دنبال آن می گردد. این ر فتار در ارث بری نیز وجود دارد


__dict__:
ما یک بیلت این متود به اسم 'داندر دیکت' داریم و کارش اینه که بیاد و اتربیوت هایی که داخل اینستنس هستند رو نشون بده
اگر برای اینستنس استفاده بشود، کلاس اتربیوت(وریبل) ها رو نمی شناسه، فقط اون هایی رو میاره که متعلق به اینستنس هستند
اگر هم برای خود کلاس استفاده بشه، فقط کلاس وریبل ها رو میشناسه و میاره



"""
class Car:
    object_nums = 0
    wheel = 4
    door = 4

    def __init__(self, name, price):
        Car.object_nums += 1
        self.name = name
        self.price = price
        print(f'FROM INIT: {self.name} has {Car.wheel} wheels and {Car.door} doors.') # use class-variable


    def show_wheel(self):
        # use instance variable. now we can change class-variable and save in instance
        print(f'FROM SHOW_WHEEL: {self.name} has {self.wheel} wheels.')



car_1 = Car('Benz', 45000)

# print(Car.__dict__)
print(F'FROM __DICT__: {car_1.__dict__}')

car_1.wheel = 6
car_1.show_wheel() # change class-variable and save in instance
print(F'FROM __DICT__: {car_1.__dict__}')