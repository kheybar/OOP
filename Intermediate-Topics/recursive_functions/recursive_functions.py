"""



توابع بازگشتی در پایتون:
یک تابع بازگشتی، تابعی است که خودش را صدا میزند
در این حالت، یک تابع برای ادامه کار نیاز به انجام کاری دیگر توسط خودش دارد
به طور معمول، شما از یک تابع بازگشتی برای تقسیم یک مشکل بزرگ که حل آن دشوار است به مسائل کوچکتر که حل آن آسان تر است، استفاده می کنید
کاربرد توابع بازگشتی در برنامه نویسی، اغلب در کنار ساختارهای داده و الگوریتم هایی مانند نمودارها و جستجوهای باینری است
در استفاده از توابع بازگشتی باید هوشیار باشید چون ممکن است یک حلقه بی نهایت ایجاد کنید و حتما باید شرایطی را برقرار کنید تا اجرای تابع متوقف شود

مثال فانکشن فکت مثال خیلی خوبی است و لینک آن در استک آور فلو:
https://stackoverflow.com/questions/11693819/understanding-recursion-in-python



"""

def count_down(start):
    print(start)
    start -= 1
    if not start == 0:
        count_down(start)
    else:
        print('done')


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
