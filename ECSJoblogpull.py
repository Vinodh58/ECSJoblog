jobname = input('Enter the Job name :')
# if jobname.isupper():
#     pass
# else:
#     job = jobname.upper()
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
reccount = file_len('Logfoldersactual.txt')
print(reccount)
f = open('Logfoldersactual.txt','r')
dict = {}
for data in range(reccount):
    a = f.readline().split("-")
    dict[a[0]] = a[1].rstrip("\n")
    a = []
print(dict)
print(jobname)
try:
    print(dict[jobname.upper()])
except KeyError as e:
    print(f'Couldn\'t find the logs for the job {jobname}')
finally:
    print("Done")
