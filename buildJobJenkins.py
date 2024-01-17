import pyjenkins

j = pyjenkins.Jenkins('http://localhost:8080/job/student_integration/', 'ssadia1', 'Corp@123')
print(j.get_jobs())
url=j.build_job_url('test_api', parameters=None, token=None)
print(url)
last_build_number = j.get_job_info('test_api')['lastCompletedBuild'] ['number']
print("last_build_number" ,last_build_number)
build_info=j.get_build_info('test_api',last_build_number)
if build_info['result']=='SUCCESS':
    print(" Build Success ")
else:
    print(" Build Failed ")
    log=j.get_build_console_output('test_api',last_build_number)
    f=open('log_buildFail.txt','w')
f.write(log)
f.close()
