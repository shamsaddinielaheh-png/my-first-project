import random

def generate_secret_code():
    # """تولید کد ۴ رقمی بدون تکرار از اعداد ۱ تا ۶ با استفاده از randrange"""
    digits = [1, 2, 3, 4, 5, 6]
    secret = []
    # استفاده از روش الحاق برای ساخت لیست بدون تکرار 
    for i in range(4):
        # انتخاب یک عدد تصادفی از لیست موجود
        idx = random.randrange(len(digits))
        num = digits[idx]
        secret += [num] # الحاق با استفاده از +=
        digits.pop(idx) # حذف برای جلوگیری از تکرار
    return secret

def get_valid_input():
    # دریافت ورودی معتبر از کاربر (فقط اعداد ۱ تا ۶، بدون تکرار، ۴ رقم 
    while True:
        user_input = input("Enter your guess for four digits (numbers one to six, no repeats)")
        
        # بررسی طول ورودی
        if len(user_input) != 4:
            print("Dear friend, you definitely have to enter four digits :)")
            continue
            
        # تبدیل رشته به لیست اعداد
        guess = []
        is_valid = True

        # در هر مرحله یکی از ایندکس ها از آن چهار کاراکتر ورودی را بررسی میکند
        for char in user_input: 
            if char.isdigit() and 1 <= int(char) <= 6:
                val = int(char)
                # بررسی تکراری نبودن با استفاده از چک کردن در لیست
                if val in guess:
                    is_valid = False
                    break
                guess += [val]
            else:
                is_valid = False
                break
        
        if is_valid and len(guess) == 4:
            return guess
        else:
            print("Enter the numbers from one to six without repeating them")

def check_guess(secret, guess):
    # بررسی میزان تطابق حدس با کد اصلی درست در مکان درست و اشتباه
    correct_pos = 0
    correct_val = 0
    
    for i in range(4):
        if guess[i] == secret[i]:
            correct_pos += 1
        elif guess[i] in secret:
            correct_val += 1
            
    return correct_pos, correct_val

def start_game():
    # تابع اصلی مدیریت چرخه بازی
    print("=== Welcome to the game Mastermind! === " \
    "elaheh shamsaddini")
    print("Rules: You must guess the 4-digit code in 10 steps")
    print("--------------------------------------------------------")
    
    secret_code = generate_secret_code()
    attempts = 0
    max_attempts = 10
    
    # چرخهٔ اصلی بازی: گرفتن حدس، شمارش تلاش‌ها و بررسی نتیجه تا برنده شدن یا تمام شدن ۱۰ فرصت
    while attempts < max_attempts:
        print(f"\nYour guess is{attempts + 1} out of {max_attempts}") # نمایش شماره تلاش فعلی
        user_guess = get_valid_input()  # دریافت حدس معتبر
        attempts += 1
        
        pos, val = check_guess(secret_code, user_guess) # مقایسه حدس با رمز
        
        if pos == 4:  # اگر هر ۴ رقم در مکان درست بود -> برنده
            print(f"🎉Congratulations! You won! The code was correct: {secret_code}")
            print(f"Number of your guesses: {attempts}")
            return
        else:
            print(f"Result: {pos} numbers in the right place| {val} numbers right but in the wrong place")
            
    print("\n❌ Unfortunately, the opportunity has run out!")
    print(f"The original code was: {secret_code}")  # اعلام رمز مخفی

# شروع اجرای بازی
if __name__ == "__main__":
    start_game()
