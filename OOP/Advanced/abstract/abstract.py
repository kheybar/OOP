"""



مفهوم انتزاع:
فشرده و خلاصه سازی بصورتی که جزئیات در کلیات پنهان شده باشند

Abstract Class:
کلاس های انتزاعی در پایتون به کلاس هایی گفته می شوند که پایه کلاس های دیگر هستند
کلاس های انتزاعی به خودی خود کار خاصی انجام نمی دهند فقط رفتار کلی کلاس های فرزند را مشخص می کنند تا به
فانکشنالیتی کامل تری برسیم. بقیه کلاس ها ارث بری می کنند تا فانکشن ها رو کامل تر کنند
درواقع حالت کلی رو ایجاد می کنیم و بقیه رو می سپاریم به دست کلاس فرزند
**کلاس های هستند که میان و کلاس های فرزند رو مجبور می کنند که متود های خودشون را یک بار دیگر آورراید کنند**

Abstract Method:
زمانی که کار ما از خواهش و تمنا گذشت و برنامه نویس بصورت اجباری باید متود کلاس ابسترکت رو آورراید کنه از
ابسترکت متود استفاده می کنیم
کلاس فرزند می تونه کل متود را بازنویسی کند یا تنها قسمتی از آن را

روش کار ابسترکت کلاس:
برای ابسترکت کردن کلاس ها در پایتون باید ماژول زیر رو ایمپورت کنیم و از داخلش متود مورد نظر رو بیاریم
بعد کلاسمون از اون متود ارث بری کنه
با این کار، پایتون کلاس فرزند رو مجبور نمی کنه ولی به برنامه نویس میفهمونه که این متود باید بازنویسی بشه

روش کار ابسترکت متود:
از همون ماژول، ابسترکت متود که یک دکوریتور هست رو اضافه اش می کنیم و بر روی متود های مدنظر قرارش می دهیم

نکته:
اگر یک زمانی نمی خواستیم از ابسترکت استفاده کنیم و همچنان برنامه نویس رو مجبور به بازنویسی متود کنیم، میشه
بیایم و در متود یک ارور رو ریز کنیم(نات ایمپلیمنتت ارور) و اینطوری زمانی که اون متود فراخوانی میشه، به ارور می خوره

نمونه های کاربردی:
در دیزاین پترن های کریشنال به مراتب استفاده میشه مثل فکتوری یا ابسترکت فکتوری



"""

from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def show(self):
        print('abstract method')
    
    def no_abstract(self):
        raise NotImplementedError


class B(A):
    
    def show(self):
        super().show()
        print('show method in B')


b1 = B()
b1.no_abstract() # NotImplementedError