import datetime
import time

path_to_host = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

#blocking logic

def block(duration_hours, website_list):

    end_time = datetime.datetime.now() + datetime.timedelta(hours=duration_hours)

    while True:
        if datetime.datetime.now < end_time:
            with open(path_to_host, "r+") as fh:
                content = fh.read()
                for site in website_list:
                    if site in content:
                        pass
                    else:
                        fh.write(redirect + " " + site + "\n")
        
        else:  #unblock phase
            with open(path_to_host, "r+") as fo:
                content = fo.readlines()
                fo.seek(0)
                for line in content:
                    if not any(site in line for site in website_list):
                        fo.write(line)
                fo.truncate()

            break
        
        time.sleep(30)


