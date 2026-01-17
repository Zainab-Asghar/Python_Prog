import time

print("=== Typing Speed Mini Tester ===")
print("Type the sentence below as fast as you can and press Enter.")
print()

sentence = "Python is easy and fun to learn"
print("Sentence:")
print(sentence)
print()

input("Press Enter when you are ready...")

start_time = time.time()
typed_text = input("\nStart typing here: ")
end_time = time.time()

time_taken = end_time - start_time
words = len(typed_text.split())
wpm = (words / time_taken) * 60

print("\n--- Result ---")
print(f"Time taken: {time_taken:.2f} seconds")
print(f"Words typed: {words}")
print(f"Typing Speed: {wpm:.2f} WPM")

if typed_text == sentence:
    print("Accuracy: 100% ✅")
else:
    print("Accuracy: Not perfect ❌ (Keep practicing!)")
