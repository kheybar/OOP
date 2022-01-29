"""



module __init__.py in python3

بطور کلی این سند، یک دایرکتوری را به یک پکیج پایتونی تبدیل می کند
زمانی که یک دایرکتوری تبدیل به یک پکیج شود، ما می توانیم کدهایی را که نیاز داریم از داخل آن ایمپورت کنیم
بدون این سند، نمی توانیم چیزی را از داخل آن دایرکتوری در سندی دیگر ایمپورت کنیم(از پایتون سه.سه به بعد این رفتار تغییر کرد)
از پایتون ۳.۳ به بعد تمامی دایرکتوری ها یک پکیج شناخته می شوند و دیگر نیازی به ماژول اینیت نیست
اینیت.پای دقیقا مثل همون داندر اینیتی است که در کلاس ها وجود دارد. یک مقدمه ساز است و سریع فعال می شود
زمانی که ما کتابخانه را ایمپورت کنیم، سریع اینیت.پای فعال می شود


موارد استفاده:
زمانی که ما یک کتابخانه مثل ریکوئست رو نصب می کنیم، با دستور ایمپورت ریکوئست می توانیم به متودهایی که در
ماژول های مختلف آن است به طور مستقیم از طریق صدا زدن خود کتابخانه دسترسی داشته باشیم

import requests

requests.api.get() # explicit
requests.get() # Implicit, how that possible?!!

بصورت عادی ما باید اسم تک تک ماژول ها رو صدا بزنیم تا برسیم به اون چیزی که می خواهیم
علت اینکه کتابخانه ریکوئست همچین رفتاری داره، اینه که برنامه نویساش زحمت کشیدند و در ماژول اینیت
همه رو ایمپورت کردند که دیگه نیازی نباشه ما بیایم اسم تک تک ماژول ها رو حفظ کنیم تا به متود موردنظر برسیم
البته اینکار برای پکیج های کوچک است نه فریمورکی مثل جنگو
زمانی که داریم ایمپورت می کنیم در اینیت، ترتیب ها مهم هستند. اگر وابستگی بین ماژول ها وجود دارد باید آن
را در نظر گرفته و به ترتیب ایمپورت شوند
https://github.com/psf/requests/blob/main/requests/__init__.py

در بعضی مواقع می شود کل سورس برنامه را در اینیت.پای نوشت! برای مثال خود پایتون در ماژول کالکشنز، تمام
ماژول را در اینیت.پای نوشته اند. این برای موارد خاص هست وقتی که واقعا میدونیم داریم چیکار می کنیم
https://github.com/python/cpython/blob/main/Lib/collections/__init__.py



"""