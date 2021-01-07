# pip install googletrans==3.1.0a0

from googletrans import Translator
translator = Translator()

out = translator.translate("كيف حالكم", dest='en')
print(out)

mystory = '''اجلس حيث يُؤْخَذُ بيدك وَتُبَرُّ ولا تجلس حيث يؤخذ برجلك وتُجَرُّ.'''
out = translator.translate(mystory, dest='ar')
print(out.text)

out = translator.translate("hi how are you ?", dest='ar')
print(out)
