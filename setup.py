import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import os
from time import sleep
notified_file = "already_notified.txt"
cwd=os.getcwd()
user_data_dir=f"{cwd}\\linkdinusrdir"
options = uc.ChromeOptions()
options.add_argument(f"--user-data-dir={user_data_dir}")
driver = uc.Chrome(options=options,use_subprocess=False)
driver.get('https://www.linkedin.com/')
t=input("Press enter to continue")