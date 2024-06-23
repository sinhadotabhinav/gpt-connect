import unittest
from gpt_connect.main import GPTConnect

class TestGPTWrapper(unittest.TestCase):
    def setUp(self):
        self.gpt = GPTConnect()

    def test_generate_text(self):
        prompt = "Once upon a time"
        result = self.gpt.generate_text(prompt)
        self.assertIsInstance(result, str)

    def test_chat(self):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
        result = self.gpt.chat(messages)
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
