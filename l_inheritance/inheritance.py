class A:
    def __init__(self, name):
        self.name = name
        print('부모 생성자')

    def print_intro(self):
        print('A')


class B(A):
    def __init__(self, name):
        super().__init__(name)
        print('자식 생성자')

    @staticmethod
    def add(number1, number2):
        return number1 + number2

    def print_intro(self):
        # 부모의 메소드를 그대로 사용하고자 할 때(선택 사항)
        super().print_intro()
        # 자식의 메소드에서 추가할 내용 작성
        print('B')



b = B('한동석')
print(b.name)
b.print_intro()



