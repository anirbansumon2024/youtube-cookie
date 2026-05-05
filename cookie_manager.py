import os
import subprocess

def fetch_cookies():
    # যেকোনো একটি ভিডিও লিঙ্ক (এটি দিয়ে সব ভিডিও চলবে)
    test_url = "https://www.youtube.com/watch?v=jfKfPfyJRdk" 
    cookie_file = "cookies.txt"
    
    print(">>> Generating fresh cookies from GitHub runner...")
    
    # yt-dlp কমান্ড যা অ্যান্ড্রয়েড ক্লায়েন্ট ইমিটেট করে
    command = [
        "yt-dlp",
        "--cookies", cookie_file,
        "--extractor-args", "youtube:player_client=android,ios",
        "--get-url", 
        test_url
    ]
    
    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(cookie_file):
            print(">>> Success: cookies.txt generated.")
        else:
            print(">>> Failed to generate cookies.txt")
    except Exception as e:
        print(f">>> Error: {e}")

if __name__ == "__main__":
    fetch_cookies()
