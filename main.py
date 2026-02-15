from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# 문장 리스트
texts = [
    "Hello",
    "I like my dad and mom",
    "I like computers",
    "Thank you (introducing Jeong Da-sol)"
]

class EnglishApp(App):
    def build(self):
        self.index = 0  # 현재 문장 인덱스
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # 문장 표시 라벨
        self.label = Label(text=texts[self.index], font_size=32)
        self.layout.add_widget(self.label)
        
        # 버튼
        self.button = Button(text="→", size_hint=(1, 0.3), font_size=32)
        self.button.bind(on_press=self.next_text)
        self.layout.add_widget(self.button)
        
        return self.layout

    def next_text(self, instance):
        self.index += 1
        if self.index < len(texts):
            self.label.text = texts[self.index]
        else:
            self.label.text = "End"  # 마지막 문장 이후
            self.button.disabled = True  # 버튼 비활성화

if __name__ == "__main__":
    EnglishApp().run()
