import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import os
from time import sleep
from datetime import datetime
notified_file = "already_notified.txt"
cwd=os.getcwd()
user_data_dir=f"{cwd}\\linkdinusrdir"
options = uc.ChromeOptions()
options.add_argument(f"--user-data-dir={user_data_dir}")
driver = uc.Chrome(options=options,use_subprocess=False)

while True:
	current_hour = datetime.now().hour
	if(current_hour==18):
							print("Sleeping...")
							driver.get('https://google.com')
							sleep(60*60*6)
	driver.get('https://www.linkedin.com/')
	sleep(5)
	driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4158123437&distance=25&f_E=1&f_TPR=r86400&geoId=100446352&keywords=software%20engineer%20intern&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')
	sleep(5)
	# Find all job elements with 'data-occludable-job-id' attribute
	job_elements = driver.find_elements(By.XPATH, "//*[@data-occludable-job-id]")
	
	# Read existing notified job IDs from file
	try:
		with open(notified_file, "r") as file:
			notified_jobs = set(file.read().splitlines())
	except FileNotFoundError:
		notified_jobs = set()
	
	# Open file in append mode to store new job IDs
	jobs=[]
	with open(notified_file, "a") as file:
		for job_element in job_elements:
			job_id = job_element.get_attribute("data-occludable-job-id")
			
			# If job_id is not already notified, print details and save it
			if job_id not in notified_jobs:
				print(job_element.text)  # Print job details
				try:
						print(job_element.find_element(By.XPATH,".//*[@data-control-id]").get_attribute('href'))
						job_description=job_element.text.replace('\n','-')+'          ' +job_element.find_element(By.XPATH,".//*[@data-control-id]").get_attribute('href')
				except:
					job_description=job_element.text.replace('\n','-')
					
				jobs.append(job_description)
				file.write(job_id + "\n")  # Save job_id to file
				
	if(len(jobs)>0):  
		driver.get('https://web.whatsapp.com/')
		sleep(10)
		driver.find_element(By.XPATH, "//*[@role='listitem']").click()
		sleep(5)
		for job in jobs:
				driver.find_element(By.XPATH, "//*[@aria-label='Type a message']").send_keys(job)
				driver.find_element(By.XPATH, "//*[@aria-label='Type a message']").send_keys('\n')
				sleep(3)
	sleep(180)             
