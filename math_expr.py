from typing import List
def math_expr(expr: str) -> bool:
    





    print ("""
    ديك طريق دائري يحتوي على عدد "n" من محطات الوقود. كل محطة مُعرفة بكمية الوقود gas[i] المتوفرة فيها، وتكلفة الوقود cost[i] للانتقال من هذه المحطة إلى المحطة التالية. تبدأ الرحلة من أي محطة ولكن بخزان وقود فارغ.

الهدف من هذا التحدي : معطياتك هي مصفوفتان صحيحتان، gas و cost. المطلوب منك تحديد فهرس المحطة التي يمكنك أن تبدأ منها الرحلة، بحيث تستطيع الدوران حول الطريق مرة واحدة في اتجاه عقارب الساعة دون نفاد الوقود. إذا لم تجد أي محطة تُمكنك من إكمال الدورة، يجب أن تُرجع (-1)

(إن وجد، يكون فريدًا).

النص المساعد

استعادة

1234
from typing import List
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    # write your code here ^_^

المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
المخرجات (Outputs)

3
الاختبار 2

المدخلات (Inputs)
gas = [2, 3, 4]
cost = [3, 4, 3]
المخرجات (Outputs)

-1
الاختبار 3

المدخلات (Inputs)
gas = [2, 3, 4]
cost = [3, 4, 3]
المخرجات (Outputs)

-1
الاختبار 4

المدخلات (Inputs)
gas = [2, 3, 4]
cost = [3, 4, 3]
المخرجات (Outputs)

-1













وصف التحدي
قم بكتابة دالة function تستقبل قيمة نصية من نوع string. تقوم بالدالة ببناء وإرجاع قيمة نصية بناءًا على القيمة المدخلة. عن طريق تكرار الاحرف بعدد معين تحدده القيمة المدخلة. على سبيل المثال:

4a يعني أنه يجب تكرار الحرف "a" أربع مرات. النتيجة المتوقعة هي aaaa. تقوم الدالة بإنشاء النص المطلوب باتباع تلك التعليمات، باستخدام مبدأ Last-In, FirstOut

النص المساعد

استعادة

1234
from typing import List
def string_builder(expression: str) -> str:
    # write your code here ^_^

المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
expression = '3[a]2[bc]'
المخرجات (Outputs)

'aaabcbc'
الاختبار 2

المدخلات (Inputs)
expression = '3[a2[c]]'
المخرجات (Outputs)

'accaccacc'







سهل

https://coderhub.sa/icon-points.07c823af44c89da5f634392f7eed2ef4.svg5 نقاط
وصف التحدي
قم بكتابة دالة function تقوم باستقبال قيمتين نصية string. تقوم هذه الدالة بمقارنة عدد الخانات النصية لكل من هذين المدخلين ومن ثم تقوم بإرجاع العدد الأكبر لعدد الخانات.

النص المساعد

استعادة

1234
from typing import List
def returnStringLetters(string1: str, string2: str) -> int:
    # write your code here ^_^

المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
string1 = 'Ahmad'
string2 = 'Mohammad'
المخرجات (Outputs)

8
الاختبار 2

المدخلات (Inputs)
string1 = 'Khalid'
string2 = 'Asma'
المخرجات (Outputs)

6
الاختبار 3

المدخلات (Inputs)
string1 = 'Osama'
string2 = 'Hassan'
المخرجات (Outputs)

6
الاختبار 4

المدخلات (Inputs)
string1 = 'Ali'
string2 = 'Nasser'




قم بكتابة دالة function تستقبل متغيرين من نوع integer ، تقوم الدالة ـ function باختيار العملية الرياضية المناسبة التي تؤدي للرقم 24 ، ثم قم بارجاع النتيجة من نوع string حيث توضح نوع العملية الرياضية

   "divided"
   "multiplied"
   "added"
   "subtracted"
   "None"
النص المساعد

استعادة

1234
from typing import List
def operation(num1: int, num2: int) -> str:
    # write your code here ^_^

المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
num1 = 6
num2 = 7
المخرجات (Outputs)

'None'
الاختبار 2

المدخلات (Inputs)
num1 = 20
num2 = 4
المخرجات (Outputs)

'added'
الاختبار 3

المدخلات (Inputs)
num1 = 3
num2 = 8
المخرجات (Outputs)

'multiplied'
الاختبار 4

المدخلات (Inputs)
num1 = 24
num2 = 1
المخرجات (Outputs)

'divided'





أقصى عدد على اليسار
سهل

https://coderhub.sa/icon-points.07c823af44c89da5f634392f7eed2ef4.svg5 نقاط
وصف التحدي
قم بكتابة دالة function تستقبل قيمة نصية من نوع string ، تقوم الـدالة function باستخراج أول أقصى رقم على اليسار ، ثم تقوم الدالة بارجاع النتيجة من نوع integer

النص المساعد

استعادة

1234
from typing import List
def left_digit(strParam: str) -> int:
    # write your code here ^_^

المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
strParam = 'Welcome2back'
المخرجات (Outputs)

2
الاختبار 2

المدخلات (Inputs)
strParam = '5'
المخرجات (Outputs)

5
الاختبار 3

المدخلات (Inputs)
strParam = '9753'
المخرجات (Outputs)

9
الاختبار 4

المدخلات (Inputs)
strParam = 'nora30@gmail.com'
المخرجات (Outputs)

3





    
    
    
    
    
    
    """)