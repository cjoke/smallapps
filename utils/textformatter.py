class TextFormatter:
    def __init__(self, text):
        self.text = text

    def format_output(self):
        # Split the text into chunks of 100 characters
        chunks = [self.text[i:i+100] for i in range(0, len(self.text), 100)]

        # Join the chunks with new lines
        formatted_text = '\n'.join(chunks)

        return formatted_text


if __name__ == "__main__":
    formatter = TextFormatter("something not important in this string of text \
                                - just a test")
    formatted_output = formatter.format_output()
    print(formatted_output)

