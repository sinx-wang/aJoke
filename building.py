class Convert:

    def convert_to_ch(self, input_str):
        input_str = input_str.encode('latin-1').decode('unicode_escape')
        print(input_str)

    def convert_to_unicode(self, input_str):
        # input_str = input_str.replace('\\', '\\\\')
        str_bytes = input_str.encode(encoding='unicode_escape')
        result = str(str_bytes)[2:-1].replace('\\\\', '\\')
        print(result)

if __name__ == '__main__':
    while(True):
        content = input("请输入:")
        convertClass = Convert()
        if content.startswith('\\u'):
            convertClass.convert_to_ch(content)
        else:
            convertClass.convert_to_unicode(content)
        print()
