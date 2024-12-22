# ismp4.py
# To install all required packages in one go, run the following command in your terminal:
# pip install psutil Pillow nudenet

import threading
import os  # Importing os for taskkill command
import pygetwindow as gw  # For interacting with window titles
import time  # Importing time to use sleep function
import pprint
import psutil
import logging
import time
from PIL import ImageGrab  # Importing ImageGrab for taking screenshots
from nudenet import NudeDetector
detector = NudeDetector()

keywords = [
    "orgasm", "porn", "blowjob", "cumshot", "creampie", "cumshots", "gangbang",
    "handjob", "lesbian", "porno", "swingers", "threesome", "deepthroat", "tits",
    "pussy", "dildo", "anybunny", "fingering", "fisting", "rape", "hardcore",
    "hentai", "interracial", "licking", "squirt", "boobies", "boob", "clit",
    "nipples", "bikini", "rajwap", "vagina", "masturbating", "mastrubation",
    "sucking", "sluts", "penis", "sex videos", "sex video", "hot bikini",
    "hot videos", "nude", "titties", "gang bang", "downblouse", "doggystyle",
    "penetration", "erotic", "erotica", "escort", "bondage", "facefuck",
    "facesitting", "gagging", "cumming", "mastrubate", "peeing", "scissoring",
    "hooker", "naked", "webcam", "lapdance", "breastfeeding", "seduce",
    "seduction", "nude", "pissing", "nudity", "panties", "playboy", "urethra",
    "vaginal", "stripgirls", "xhamster", "wowgirls", "xnxx", "xtube", "xvideos",
    "xvideo", "tube8", "pornhub", "xxxbunker", "iwank", "redtube", "alohatube",
    "youjizz", "drtuber", "spankwire", "tnaflix", "nuvid", "tubegals",
    "kama sutra", "3movs", "sexvid", "4tube", "thumbzilla", "slutload", "camhub",
    "empflix", "dansmovies", "nsfw", "kamasutra", "fapster", "spankbang",
    "redporn", "megatube", "watchmygf", "nudevista", "bdsm", "bangbros",
    "realitykings", "badjojo", "iptorrents", "pussytorrent", "freeones",
    "kindgirls", "sexedchat", "jerkmate", "onlyfans", "stripchat", "slutroulette",
    "watch-my-gf", "iknowthatgirl", "assoass", "punishtube", "facialabuse",
    "lobstertube", "zzcartoon", "gelbooru", "fakku", "porcore", "sankakucomplex",
    "cartoonporno", "anal", "milf", "piss", "cock", "cocks", "clits", "nipple",
    "dick", "dicks", "bikinies", "suck", "slut", "condom", "condoms", "xxx",
    "panties", "cams", "lingerie", "swimwear", "movie"
]

arr = ['msedge', 'chrome', 'firefox', 'opera',
       'safari', 'brave', 'vivaldi', 'tor','arc']

log_dir = os.path.expanduser('~\\Documents')  # User's Documents folder
log_file = os.path.join(log_dir, 'mp4_playing.log')

logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(message)s')
logging.info("Logging started successfully.")
# Set up logging



def is_mp4_playing():
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            logging.info(f"Process: {proc.name()}, Executable: {proc.exe()}")
            if any(player in proc.exe().lower() for player in ['vlc', 'mpc', 'windows media player', 'potplayer', 'edge', 'chrome', 'arc']):
                logging.info(f"Media player detected: PID: {
                             proc.pid}, Name: {proc.name()}")
                return True
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return False


def check_nsfw_conditions(nsfw_results):
    """
    Check if the NSFW conditions are met:
    - Female breasts exposed > 50%
    - Buttocks exposed > 40%
    """
    female_genitalia_exposed = any(
        pred['class'] == 'FEMALE_GENITALIA_EXPOSED' and pred['score'] >= 0.4 for pred in nsfw_results)
    anus_exposed = any(
        pred['class'] == 'ANUS_EXPOSED' and pred['score'] >= 0.4 for pred in nsfw_results)
    male_genitalia_exposed = any(
        pred['class'] == 'MALE_GENITALIA_EXPOSED' and pred['score'] >= 0.4 for pred in nsfw_results)

    female_breast_exposed = any(
        pred['class'] == 'FEMALE_BREAST_EXPOSED' and pred['score'] >= 0.5 for pred in nsfw_results)
    # print(female_breast_exposed)
    buttocks_exposed = any(
        pred['class'] == 'BUTTOCKS_EXPOSED' and pred['score'] >= 0.4 for pred in nsfw_results)
    # print(buttocks_exposed);
    female_genitalia_exposed = any(
        pred['class'] == 'FEMALE_GENITALIA_EXPOSED' and pred['score'] > 0.5 for pred in nsfw_results)
    male_genitalia_exposed = any(
        pred['class'] == 'MALE_GENITALIA_EXPOSED' and pred['score'] > 0.6 for pred in nsfw_results)
    belly_exposed = any(
        pred['class'] == 'BELLY_EXPOSED' and pred['score'] > 0.55 for pred in nsfw_results)
    face_female = any(
        pred['class'] == 'FACE_FEMALE' and pred['score'] >= 0.59 for pred in nsfw_results)
    female_breast_covered = any(
        pred['class'] == 'FEMALE_BREAST_COVERED' and pred['score'] >= 0.4 for pred in nsfw_results)
    female_genitalia_covered = any(
        pred['class'] == 'FEMALE_GENITALIA_COVERED' and pred['score'] > 0.3 for pred in nsfw_results)

    if (female_genitalia_exposed or (buttocks_exposed or male_genitalia_exposed) or anus_exposed or female_breast_exposed):

        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                if any(player in proc.exe().lower() for player in ['vlc', 'mpc', 'windows media player', 'potplayer', 'edge', 'chrome', 'arc']):
                    proc.kill()
                    logging.info(f"Killed media player process: PID: {
                                 proc.pid}, Name: {proc.name()}")
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                continue
    if (belly_exposed and female_breast_covered and face_female):
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                if any(player in proc.exe().lower() for player in ['vlc', 'mpc', 'windows media player', 'potplayer', 'edge', 'chrome', 'arc']):
                    proc.kill()
                    logging.info(f"Killed media player process: PID: {
                                 proc.pid}, Name: {proc.name()}")
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                continue
    if (female_genitalia_covered and face_female):
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                if any(player in proc.exe().lower() for player in ['vlc', 'mpc', 'windows media player', 'potplayer', 'edge', 'chrome', 'arc']):
                    proc.kill()
                    logging.info(f"Killed media player process: PID: {
                                 proc.pid}, Name: {proc.name()}")
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                continue

    return female_breast_exposed and buttocks_exposed


def monitor_windows():
    """Monitor windows for specific keywords and close them if necessary."""
    print("Monitoring active windows. Press Ctrl+C to stop.")
    try:
        while True:
            windows = gw.getWindowsWithTitle("")  # Get all windows
            for window in windows:
                title = window.title.lower()  # Convert to lowercase for case-insensitive matching
                for keyword in keywords:
                    if keyword in title:
                        print(f"Keyword '{keyword}' found in title '{
                              title}'. Closing app...")
                        # Find the process ID using psutil
                        for i in arr:
                            os.system(f"taskkill /f /im {i}.exe")
                        else:
                            print(
                                f"No matching process found for title: {title}")
                        continue
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


def start_monitoring():
    """Start the monitoring in a separate thread."""
    monitor_thread = threading.Thread(target=monitor_windows)
    monitor_thread.daemon = True  # Allow thread to exit when the main program does
    monitor_thread.start()


# Start the monitoring in a separate thread
start_monitoring()

while True:
    if is_mp4_playing():
        print("MP4 file is being played.")
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f'C:\\Users\\profe\\Downloads\\screenshot_1.png'
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        logging.info(f"Screenshot taken: {screenshot_path}")

        # Check if the screenshot is NSFW
        nsfw_result = detector.detect(screenshot_path)
        nd = detector.censor(screenshot_path)

        # Beautify and print the predictions for debugging
        pprint.pprint(nsfw_result)
        for prediction in nsfw_result:
            print(f"Label: {prediction['class']}, Score: {
                  prediction['score']}")

        # Check the NSFW score
        check_nsfw_conditions(nsfw_result)

        if check_nsfw_conditions(nsfw_result):
            print(f"Condition met at {
                  timestamp}: Female breasts exposed > 50% and buttocks exposed > 40%.")

        time.sleep(10)  # Wait for 10 seconds before taking the next screenshot
    else:
        print("No MP4 file is currently being played.")

    time.sleep(5)  # Check every 5 seconds


# List of words to match against window titles
