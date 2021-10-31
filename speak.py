import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

text = '''
今天我，寒夜里看雪飘过
怀着冷却了的心窝漂远方
风雨里追赶，雾里分不清影踪
天空海阔你与我
可会变（谁没在变）
多少次，迎着冷眼与嘲笑
从没有放弃过心中的理想
一刹那恍惚， 若有所失的感觉
不知不觉已变淡
心里爱（谁明白我）
原谅我这一生不羁放纵爱自由
也会怕有一天会跌倒
背弃了理想 ，谁人都可以
哪会怕有一天只你共我
'''

if __name__ == '__main__':
    voices = engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()