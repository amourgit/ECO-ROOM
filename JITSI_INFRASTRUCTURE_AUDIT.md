# CIVITAS — Jitsi Infrastructure Audit

> Inventaire de l'installation Jitsi directement installée sur le système.

**Rapport :** `/opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md`

**Répertoire des données brutes :** `/opt/civitas/jitsi-audit`

**Date de début :** 2026-08-12 20:37:24 EDT

> Ce rapport est généré automatiquement.
>
> Le script est conçu pour effectuer des opérations de lecture uniquement.



---

# 1. INFORMATIONS SYSTÈME

**Date :** 2026-08-12 20:37:24 EDT


## Hostname


```text
$ hostname
```
meet.civitas.local


```text
$ hostnamectl
```
 Static hostname: meet.civitas.local
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 75d4a5dd322d4eeaaed42cd8225d7ff9
         Boot ID: cd24b7a7aee24c5f88c363addb32a3d7
    Product UUID: 10d629a6-57de-c047-91ef-5fd9ba6f7802
  Virtualization: oracle
Operating System: Debian GNU/Linux 13 (trixie)
          Kernel: Linux 6.12.74+deb13+1-amd64
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
 Hardware Serial: VirtualBox-a629d610-de57-47c0-91ef-5fd9ba6f7802
Firmware Version: VirtualBox
   Firmware Date: Fri 2006-12-01
    Firmware Age: 19y 8month 1w 4d


## OS


```text
$ cat /etc/os-release
```
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.6
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"


```text
$ uname -a
```
Linux meet.civitas.local 6.12.74+deb13+1-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.12.74-2 (2026-03-08) x86_64 GNU/Linux


```text
$ uname -m
```
x86_64


## CPU / RAM / DISQUE


```text
$ lscpu
```
Architecture:                            x86_64
CPU op-mode(s):                          32-bit, 64-bit
Address sizes:                           39 bits physical, 48 bits virtual
Byte Order:                              Little Endian
CPU(s):                                  4
On-line CPU(s) list:                     0-3
Vendor ID:                               GenuineIntel
Model name:                              Intel(R) Xeon(R) W-10855M CPU @ 2.80GHz
CPU family:                              6
Model:                                   165
Thread(s) per core:                      1
Core(s) per socket:                      4
Socket(s):                               1
Stepping:                                2
BogoMIPS:                                5615.99
Flags:                                   fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq vmx ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch tpr_shadow flexpriority ept vpid fsgsbase bmi1 avx2 bmi2 invpcid rdseed adx clflushopt arat vnmi md_clear flush_l1d arch_capabilities
Virtualization:                          VT-x
Hypervisor vendor:                       KVM
Virtualization type:                     full
L1d cache:                               128 KiB (4 instances)
L1i cache:                               128 KiB (4 instances)
L2 cache:                                1 MiB (4 instances)
L3 cache:                                48 MiB (4 instances)
NUMA node(s):                            1
NUMA node0 CPU(s):                       0-3
Vulnerability Gather data sampling:      Unknown: Dependent on hypervisor status
Vulnerability Indirect target selection: Mitigation; Aligned branch/return thunks
Vulnerability Itlb multihit:             KVM: Mitigation: Split huge pages
Vulnerability L1tf:                      Not affected
Vulnerability Mds:                       Not affected
Vulnerability Meltdown:                  Not affected
Vulnerability Mmio stale data:           Mitigation; Clear CPU buffers; SMT Host state unknown
Vulnerability Reg file data sampling:    Not affected
Vulnerability Retbleed:                  Vulnerable
Vulnerability Spec rstack overflow:      Not affected
Vulnerability Spec store bypass:         Vulnerable
Vulnerability Spectre v1:                Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:                Mitigation; Retpolines; STIBP disabled; RSB filling; PBRSB-eIBRS Not affected; BHI SW loop, KVM SW loop
Vulnerability Srbds:                     Unknown: Dependent on hypervisor status
Vulnerability Tsa:                       Not affected
Vulnerability Tsx async abort:           Not affected
Vulnerability Vmscape:                   Not affected


```text
$ free -h
```
               total        used        free      shared  buff/cache   available
Mem:           9.6Gi       4.7Gi       2.7Gi       103Mi       2.6Gi       4.9Gi
Swap:          5.1Gi          0B       5.1Gi


```text
$ lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINTS
```
NAME     SIZE FSTYPE TYPE MOUNTPOINTS
sda    100.3G        disk 
├─sda1  95.1G ext4   part /
├─sda2     1K        part 
└─sda5   5.1G swap   part [SWAP]
sr0     1024M        rom  


```text
$ df -hT
```
Filesystem     Type      Size  Used Avail Use% Mounted on
udev           devtmpfs  4.8G     0  4.8G   0% /dev
tmpfs          tmpfs     984M  2.6M  982M   1% /run
/dev/sda1      ext4       94G   19G   70G  22% /
tmpfs          tmpfs     4.9G     0  4.9G   0% /dev/shm
tmpfs          tmpfs     5.0M  8.0K  5.0M   1% /run/lock
tmpfs          tmpfs     1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
tmpfs          tmpfs     4.9G  4.0K  4.9G   1% /tmp
tmpfs          tmpfs     984M   96K  984M   1% /run/user/1000
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/969083c4e748172e72439e380e5e09bb54320a795ea14ee9b1ca0b93c7e43bfe/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/2fc1eb5a3804b35a7ddc2d319001eb42a78515b4657de3e274bab79c3f879db7/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/38a2115b5e0d99e455cc66e4b77b66ba9914b27cc673aab41128f2e50486ff5e/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/d6a5d4c38036177dab7f082987ec5f750f8f55f4f9f844f5c5c003220fe0b266/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/95c946734a37fdcfe11e0ac18fe00e98cd6a8fa9bf2d622e7f372e842b1a7a45/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/38a5f576dcdc29a095b3f3cc93166b1037d616918fa86be79cfe4dd382cb3e2c/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/91efcc38fd793dd3b4006388e377d83b4e262d8526f5e4618c2bc2d95ecce95c/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/b487b3a2e86b0030a649d2f82786bd706089b01e87cdf3bf0e347870d4d2b616/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/38b0260eb8e7bd46e4c5dc3f7575b960df3eb2d506fdc9f83901843e7ba8e387/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/b46fe020c83eb23dcc5bf173aef8fe85aaabcd6871869a134fd0c46cce8398a8/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/b5e7fea9626b7170045398a44122a9714f8b3f21cdaa8cadd3044746aaed1762/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/9a329cc2df1ec4ee42424119134cfe19e5be500fc7d0cdd472942c6a889739f9/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/bc92fd2d2b69e841aaed61ea22cdffa902f02597682065756964d307d854418c/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/f0191e968572bf04ae511551c0b8dc119ba479b9bfa22139640bb38e90d6aed6/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/e876910d5bce78838d5a04d3783aa7dec679e10d8236abf6beac62cf6d48fa03/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/6fcabb95e806c28fcc2014404781ea8d35aa4ec78fb2e9b00bbe5c9d42e6f29f/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/a0d035d02216d65220abff329474b6e273e33be814011ccab6621dc1ebf29643/merged
overlay        overlay    94G   19G   70G  22% /var/lib/docker/overlay2/1c0da3e626c4f13eaae26a56239ece5810d0cd4183d8f1b8b8861f0447723671/merged



---

# 2. PAQUETS INSTALLÉS

**Date :** 2026-08-12 20:37:24 EDT


## Recherche globale des paquets Jitsi


```text
$ dpkg -l 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|coturn|turnserver|nginx" || true
```
ii  coturn                                              4.6.1-2                              amd64        TURN and STUN server for VoIP
ii  xwaylandvideobridge                                 0.4.0-2+b1                           amd64        XWayland Video Bridge for X11 clients


## Recherche avec apt


```text
$ apt list --installed 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|coturn|turnserver|nginx" || true
```
coturn/stable,now 4.6.1-2 amd64 [installed]
xwaylandvideobridge/stable,now 0.4.0-2+b1 amd64 [installed,automatic]


## Versions


```text
$ dpkg-query -W -f="\${Package}\t\${Version}\n" 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|coturn|turnserver" || true
```
coturn	4.6.1-2
xwaylandvideobridge	0.4.0-2+b1



---

# 3. SERVICES SYSTEMD

**Date :** 2026-08-12 20:37:24 EDT


## Tous les services contenant Jitsi


```text
$ systemctl list-units --type=service --all 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|jvb|videobridge|coturn|turnserver|nginx" || true
```
● coturn.service                              loaded    failed   failed  coTURN STUN/TURN Server
● jicofo.service                              not-found inactive dead    jicofo.service
● jitsi-videobridge2.service                  not-found inactive dead    jitsi-videobridge2.service
● prosody.service                             not-found inactive dead    prosody.service


## Services activés


```text
$ systemctl list-unit-files 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|jvb|videobridge|coturn|turnserver|nginx" || true
```
coturn.service                                                                enabled         enabled
nginx.service                                                                 masked          enabled


## Fichiers systemd


```text
$ find /etc/systemd /lib/systemd /usr/lib/systemd -type f 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|jvb|videobridge|coturn|turnserver" || true
```
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf
/lib/systemd/system/coturn.service
/usr/lib/systemd/system/coturn.service


## Détails des services


### Service : prosody

```text
$ systemctl status prosody --no-pager
```
Unit prosody.service could not be found.


```text
$ systemctl cat prosody
```
No files found for prosody.service.


### Service : jicofo

```text
$ systemctl status jicofo --no-pager
```
Unit jicofo.service could not be found.


```text
$ systemctl cat jicofo
```
No files found for jicofo.service.


### Service : jitsi-videobridge2

```text
$ systemctl status jitsi-videobridge2 --no-pager
```
Unit jitsi-videobridge2.service could not be found.


```text
$ systemctl cat jitsi-videobridge2
```
No files found for jitsi-videobridge2.service.


### Service : jitsi-videobridge

```text
$ systemctl status jitsi-videobridge --no-pager
```
Unit jitsi-videobridge.service could not be found.


```text
$ systemctl cat jitsi-videobridge
```
No files found for jitsi-videobridge.service.


### Service : coturn

```text
$ systemctl status coturn --no-pager
```
× coturn.service - coTURN STUN/TURN Server
     Loaded: loaded (/usr/lib/systemd/system/coturn.service; enabled; preset: enabled)
     Active: failed (Result: exit-code) since Wed 2026-08-12 19:51:15 EDT; 46min ago
 Invocation: 87d8c0021ccf411287247d0267ea9661
       Docs: man:coturn(1)
             man:turnadmin(1)
             man:turnserver(1)
    Process: 955 ExecStart=/usr/bin/turnserver -c /etc/turnserver.conf --pidfile= (code=exited, status=255/EXCEPTION)
   Main PID: 955 (code=exited, status=255/EXCEPTION)

Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : WARNING: cannot start TLS and DTLS listeners because private key file is not set properly
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : NO EXPLICIT LISTENER ADDRESS(ES) ARE CONFIGURED
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : ===========Discovering listener addresses: =========
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Listener address to use: 127.0.0.1
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Listener address to use: ::1
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : ERROR: main: Cannot configure any meaningful IP listener address
Aug 12 19:51:15 meet.civitas.local systemd[1]: coturn.service: Scheduled restart job, restart counter is at 5.
Aug 12 19:51:15 meet.civitas.local systemd[1]: coturn.service: Start request repeated too quickly.
Aug 12 19:51:15 meet.civitas.local systemd[1]: coturn.service: Failed with result 'exit-code'.
Aug 12 19:51:15 meet.civitas.local systemd[1]: Failed to start coturn.service - coTURN STUN/TURN Server.


```text
$ systemctl cat coturn
```
# /usr/lib/systemd/system/coturn.service
[Unit]
Description=coTURN STUN/TURN Server
Documentation=man:coturn(1) man:turnadmin(1) man:turnserver(1)
After=network.target

[Service]
User=turnserver
Group=turnserver
Type=notify
ExecStart=/usr/bin/turnserver -c /etc/turnserver.conf --pidfile=
Restart=on-failure
InaccessibleDirectories=/home
PrivateTmp=yes

[Install]
WantedBy=multi-user.target


### Service : turnserver

```text
$ systemctl status turnserver --no-pager
```
Unit turnserver.service could not be found.


```text
$ systemctl cat turnserver
```
No files found for turnserver.service.


### Service : nginx

```text
$ systemctl status nginx --no-pager
```
○ nginx.service
     Loaded: masked (Reason: Unit nginx.service is masked.)
     Active: inactive (dead)


```text
$ systemctl cat nginx
```
# Unit nginx.service is masked.



---

# 4. PROSODY

**Date :** 2026-08-12 20:37:25 EDT


## Binaire


```text
$ command -v prosody 2>/dev/null || true
```


```text
$ prosodyctl --version 2>/dev/null || true
```


## Répertoires Prosody


```text
$ find /etc/prosody /usr/lib/prosody /usr/share/prosody /var/lib/prosody /var/log/prosody -maxdepth 4 -print 2>/dev/null || true
```


## Configuration Prosody


```text
$ find /etc/prosody -type f -print 2>/dev/null || true
```


## Configuration principale


```text
$ cat /etc/prosody/prosody.cfg.lua 2>/dev/null || true
```


## Configurations Jitsi Prosody


```text
$ find /etc/prosody -type f -iname "*jitsi*" -o -iname "*meet*" 2>/dev/null | sort
```


## Virtual hosts


```text
$ grep -RniE "VirtualHost|Component|authentication|admins" /etc/prosody 2>/dev/null || true
```


## Modules


```text
$ find /usr/lib/prosody /usr/share/prosody /etc/prosody -type f 2>/dev/null | grep -Ei "module|jitsi" | sort || true
```


## Utilisateurs Prosody


```text
$ prosodyctl list 2>/dev/null || true
```



---

# 5. JICOFO

**Date :** 2026-08-12 20:37:25 EDT


## Localisation


```text
$ find /etc/jitsi /usr/share/jicofo /usr/share/jitsi /usr/lib/jicofo -type f 2>/dev/null | sort | grep -Ei "jicofo|jitsi" || true
```


## Configuration


```text
$ find /etc/jitsi/jicofo -maxdepth 5 -type f -print 2>/dev/null || true
```


## Contenu configuration Jicofo


```text
$ for f in /etc/jitsi/jicofo/*; do [ -f "$f" ] && { echo "===== $f ====="; sed -n "1,240p" "$f"; }; done
```


## Service Jicofo


```text
$ systemctl status jicofo --no-pager
```
Unit jicofo.service could not be found.


```text
$ systemctl cat jicofo
```
No files found for jicofo.service.



---

# 6. JITSI VIDEOBRIDGE (JVB)

**Date :** 2026-08-12 20:37:25 EDT


## Localisation


```text
$ find /etc/jitsi /usr/share/jitsi /usr/share/jitsi-videobridge /usr/lib/jitsi-videobridge -type f 2>/dev/null | sort | grep -Ei "videobridge|jvb|jitsi" || true
```


## Configuration JVB


```text
$ find /etc/jitsi/videobridge -maxdepth 5 -type f -print 2>/dev/null || true
```


## Configurations JVB


```text
$ for f in /etc/jitsi/videobridge/*; do [ -f "$f" ] && { echo "===== $f ====="; sed -n "1,260p" "$f"; }; done
```


## JVB service


```text
$ systemctl status jitsi-videobridge2 --no-pager
```
Unit jitsi-videobridge2.service could not be found.


```text
$ systemctl cat jitsi-videobridge2
```
No files found for jitsi-videobridge2.service.



---

# 7. JITSI MEET WEB

**Date :** 2026-08-12 20:37:25 EDT


## Répertoires


```text
$ find /usr/share/jitsi-meet /etc/jitsi-meet /var/lib/jitsi-meet -maxdepth 4 -print 2>/dev/null || true
```
/usr/share/jitsi-meet
/usr/share/jitsi-meet/prosody-plugins
/usr/share/jitsi-meet/prosody-plugins/mod_muc_webhook.lua


## Package


```text
$ dpkg -L jitsi-meet 2>/dev/null || true
```


## Configuration


```text
$ find /etc/jitsi -maxdepth 4 -type f -print 2>/dev/null | sort
```


## Fichiers JavaScript


```text
$ find /usr/share/jitsi-meet -type f 2>/dev/null | grep -Ei "\.js$|config|interface_config|external_api" | head -500
```



---

# 8. NGINX

**Date :** 2026-08-12 20:37:26 EDT


## Status


```text
$ systemctl status nginx --no-pager
```
○ nginx.service
     Loaded: masked (Reason: Unit nginx.service is masked.)
     Active: inactive (dead)


## Configuration


```text
$ find /etc/nginx -type f -print 2>/dev/null | sort
```


## Sites


```text
$ find /etc/nginx/sites-enabled /etc/nginx/sites-available -type f -maxdepth 2 -print 2>/dev/null | sort
```


## Recherche Jitsi


```text
$ grep -RniE "jitsi|prosody|xmpp|websocket|colibri|bosh|focus|meet" /etc/nginx 2>/dev/null || true
```


## Configuration complète


```text
$ nginx -T
```
jitsi-infrastructure-audit.sh: line 84: nginx: command not found



---

# 9. CERTIFICATS TLS

**Date :** 2026-08-12 20:37:26 EDT


## Let's Encrypt


```text
$ find /etc/letsencrypt -maxdepth 5 -type f -print 2>/dev/null | sort || true
```


## Certificats


```text
$ certbot certificates 2>/dev/null || true
```


## Recherche certificats Jitsi


```text
$ find /etc/jitsi /etc/prosody -type f 2>/dev/null | grep -Ei "\.(crt|pem|key)$" | sort || true
```



---

# 10. COTURN / TURN

**Date :** 2026-08-12 20:37:26 EDT


## Paquet


```text
$ dpkg -l 2>/dev/null | grep -Ei "coturn|turnserver" || true
```
ii  coturn                                              4.6.1-2                              amd64        TURN and STUN server for VoIP


## Binaire


```text
$ command -v turnserver 2>/dev/null || true
```
/usr/bin/turnserver


## Configuration


```text
$ find /etc/turnserver /etc/coturn -type f -print 2>/dev/null || true
```
/etc/turnserver/turndb


## Configuration principale


```text
$ cat /etc/turnserver.conf 2>/dev/null || true
```


## Systemd


```text
$ systemctl status coturn --no-pager
```
× coturn.service - coTURN STUN/TURN Server
     Loaded: loaded (/usr/lib/systemd/system/coturn.service; enabled; preset: enabled)
     Active: failed (Result: exit-code) since Wed 2026-08-12 19:51:15 EDT; 46min ago
 Invocation: 87d8c0021ccf411287247d0267ea9661
       Docs: man:coturn(1)
             man:turnadmin(1)
             man:turnserver(1)
    Process: 955 ExecStart=/usr/bin/turnserver -c /etc/turnserver.conf --pidfile= (code=exited, status=255/EXCEPTION)
   Main PID: 955 (code=exited, status=255/EXCEPTION)

Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : WARNING: cannot start TLS and DTLS listeners because private key file is not set properly
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : NO EXPLICIT LISTENER ADDRESS(ES) ARE CONFIGURED
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : ===========Discovering listener addresses: =========
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Listener address to use: 127.0.0.1
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Listener address to use: ::1
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : ERROR: main: Cannot configure any meaningful IP listener address
Aug 12 19:51:15 meet.civitas.local systemd[1]: coturn.service: Scheduled restart job, restart counter is at 5.
Aug 12 19:51:15 meet.civitas.local systemd[1]: coturn.service: Start request repeated too quickly.
Aug 12 19:51:15 meet.civitas.local systemd[1]: coturn.service: Failed with result 'exit-code'.
Aug 12 19:51:15 meet.civitas.local systemd[1]: Failed to start coturn.service - coTURN STUN/TURN Server.


```text
$ systemctl status turnserver --no-pager
```
Unit turnserver.service could not be found.



---

# 11. PORTS RÉSEAU

**Date :** 2026-08-12 20:37:26 EDT


## Tous les ports en écoute


```text
$ ss -lntup
```
Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:PortProcess                                
udp   UNCONN 0      0          127.0.0.1:53         0.0.0.0:*    users:(("dnsmasq",pid=2138,fd=4))     
udp   UNCONN 0      0            0.0.0.0:50718      0.0.0.0:*    users:(("avahi-daemon",pid=739,fd=14))
udp   UNCONN 0      0            0.0.0.0:10000      0.0.0.0:*    users:(("dockerd",pid=2146,fd=60))    
udp   UNCONN 0      0            0.0.0.0:51841      0.0.0.0:*    users:(("kdeconnectd",pid=1483,fd=27))
udp   UNCONN 0      0            0.0.0.0:44038      0.0.0.0:*    users:(("kdeconnectd",pid=1483,fd=23))
udp   UNCONN 0      0            0.0.0.0:53619      0.0.0.0:*    users:(("kdeconnectd",pid=1483,fd=30))
udp   UNCONN 0      0            0.0.0.0:5353       0.0.0.0:*    users:(("kdeconnectd",pid=1483,fd=21))
udp   UNCONN 0      0            0.0.0.0:5353       0.0.0.0:*    users:(("avahi-daemon",pid=739,fd=12))
udp   UNCONN 0      0            0.0.0.0:38384      0.0.0.0:*    users:(("kdeconnectd",pid=1483,fd=28))
udp   UNCONN 0      0            0.0.0.0:47536      0.0.0.0:*    users:(("kdeconnectd",pid=1483,fd=25))
udp   UNCONN 0      0              [::1]:53            [::]:*    users:(("dnsmasq",pid=2138,fd=6))     
udp   UNCONN 0      0                  *:57697            *:*    users:(("kdeconnectd",pid=1483,fd=34))
udp   UNCONN 0      0                  *:33505            *:*    users:(("kdeconnectd",pid=1483,fd=24))
udp   UNCONN 0      0                  *:41907            *:*    users:(("kdeconnectd",pid=1483,fd=38))
udp   UNCONN 0      0                  *:1716             *:*    users:(("kdeconnectd",pid=1483,fd=19))
udp   UNCONN 0      0                  *:51405            *:*    users:(("kdeconnectd",pid=1483,fd=36))
udp   UNCONN 0      0                  *:59719            *:*    users:(("kdeconnectd",pid=1483,fd=35))
udp   UNCONN 0      0               [::]:51923         [::]:*    users:(("avahi-daemon",pid=739,fd=15))
udp   UNCONN 0      0                  *:60643            *:*    users:(("kdeconnectd",pid=1483,fd=37))
udp   UNCONN 0      0                  *:46138            *:*    users:(("kdeconnectd",pid=1483,fd=31))
udp   UNCONN 0      0                  *:46142            *:*    users:(("kdeconnectd",pid=1483,fd=26))
udp   UNCONN 0      0               [::]:5353          [::]:*    users:(("avahi-daemon",pid=739,fd=13))
udp   UNCONN 0      0                  *:5353             *:*    users:(("kdeconnectd",pid=1483,fd=22))
udp   UNCONN 0      0                  *:38649            *:*    users:(("kdeconnectd",pid=1483,fd=32))
udp   UNCONN 0      0                  *:47272            *:*    users:(("kdeconnectd",pid=1483,fd=33))
udp   UNCONN 0      0                  *:55960            *:*    users:(("kdeconnectd",pid=1483,fd=29))
tcp   LISTEN 0      4096         0.0.0.0:9308       0.0.0.0:*    users:(("dockerd",pid=2146,fd=89))    
tcp   LISTEN 0      4096         0.0.0.0:9091       0.0.0.0:*    users:(("dockerd",pid=2146,fd=145))   
tcp   LISTEN 0      4096         0.0.0.0:9092       0.0.0.0:*    users:(("dockerd",pid=2146,fd=71))    
tcp   LISTEN 0      4096       127.0.0.1:8080       0.0.0.0:*    users:(("dockerd",pid=2146,fd=43))    
tcp   LISTEN 0      4096         0.0.0.0:80         0.0.0.0:*    users:(("dockerd",pid=2146,fd=51))    
tcp   LISTEN 0      128          0.0.0.0:22         0.0.0.0:*    users:(("sshd",pid=922,fd=6))         
tcp   LISTEN 0      4096         0.0.0.0:443        0.0.0.0:*    users:(("dockerd",pid=2146,fd=55))    
tcp   LISTEN 0      4096         0.0.0.0:3100       0.0.0.0:*    users:(("dockerd",pid=2146,fd=123))   
tcp   LISTEN 0      4096         0.0.0.0:3000       0.0.0.0:*    users:(("dockerd",pid=2146,fd=141))   
tcp   LISTEN 0      4096       127.0.0.1:631        0.0.0.0:*    users:(("cupsd",pid=895,fd=7))        
tcp   LISTEN 0      4096       127.0.0.1:8888       0.0.0.0:*    users:(("dockerd",pid=2146,fd=58))    
tcp   LISTEN 0      4096         0.0.0.0:8100       0.0.0.0:*    users:(("dockerd",pid=2146,fd=170))   
tcp   LISTEN 0      4096         0.0.0.0:8090       0.0.0.0:*    users:(("dockerd",pid=2146,fd=90))    
tcp   LISTEN 0      4096         0.0.0.0:8002       0.0.0.0:*    users:(("dockerd",pid=2146,fd=181))   
tcp   LISTEN 0      4096         0.0.0.0:8011       0.0.0.0:*    users:(("dockerd",pid=2146,fd=165))   
tcp   LISTEN 0      4096         0.0.0.0:8010       0.0.0.0:*    users:(("dockerd",pid=2146,fd=150))   
tcp   LISTEN 0      32         127.0.0.1:53         0.0.0.0:*    users:(("dnsmasq",pid=2138,fd=5))     
tcp   LISTEN 0      50                 *:1716             *:*    users:(("kdeconnectd",pid=1483,fd=20))
tcp   LISTEN 0      128             [::]:22            [::]:*    users:(("sshd",pid=922,fd=7))         
tcp   LISTEN 0      4096           [::1]:631           [::]:*    users:(("cupsd",pid=895,fd=6))        
tcp   LISTEN 0      32             [::1]:53            [::]:*    users:(("dnsmasq",pid=2138,fd=7))     


## Ports Jitsi connus


```text
$ ss -lntup 2>/dev/null | grep -E ":80 |:443 |:5222 |:5269 |:5347 |:3478 |:5349 |:10000 |:4443 |:8080 |:8888 |:8443 " || true
```
udp   UNCONN 0      0            0.0.0.0:10000      0.0.0.0:*    users:(("dockerd",pid=2146,fd=60))    
tcp   LISTEN 0      4096       127.0.0.1:8080       0.0.0.0:*    users:(("dockerd",pid=2146,fd=43))    
tcp   LISTEN 0      4096         0.0.0.0:80         0.0.0.0:*    users:(("dockerd",pid=2146,fd=51))    
tcp   LISTEN 0      4096         0.0.0.0:443        0.0.0.0:*    users:(("dockerd",pid=2146,fd=55))    
tcp   LISTEN 0      4096       127.0.0.1:8888       0.0.0.0:*    users:(("dockerd",pid=2146,fd=58))    


## Processus liés aux ports


```text
$ lsof -nP -iTCP -sTCP:LISTEN 2>/dev/null | grep -Ei "java|prosody|nginx|turn|jitsi|node" || true
```
COMMAND    PID    USER  FD   TYPE DEVICE SIZE/OFF NODE NAME



---

# 12. PROCESSUS

**Date :** 2026-08-12 20:37:26 EDT


## Processus Jitsi


```text
$ ps auxww | grep -Ei "jitsi|prosody|jicofo|videobridge|jvb|turnserver|coturn|nginx" | grep -v grep || true
```
civitas     1490  0.0  1.5 1513560 153548 ?      Ssl  19:51   0:00 /usr/bin/xwaylandvideobridge
root        2729  0.0  0.0  25376  9700 ?        Ss   19:52   0:00 nginx: master process nginx -g daemon off;
civitas     3008  0.0  0.0    224    84 ?        S    19:52   0:00 s6-supervise jvb
civitas     3043  0.0  0.0    224    80 ?        S    19:52   0:00 s6-supervise jicofo
civitas     3106  0.0  0.0    224    80 ?        S    19:52   0:00 s6-supervise prosody
civitas     3167  0.0  0.0    224    76 ?        S    19:52   0:00 s6-supervise nginx
tss         3249  0.0  0.0  25916  7856 ?        S    19:52   0:00 nginx: worker process
tss         3250  0.0  0.0  26200  8220 ?        S    19:52   0:00 nginx: worker process
tss         3251  0.0  0.0  25916  7856 ?        S    19:52   0:00 nginx: worker process
tss         3252  0.0  0.0  26172  8004 ?        S    19:52   0:00 nginx: worker process
civitas     3319  0.0  0.2 196988 28596 ?        Ss   19:52   0:00 nginx: master process nginx -c /run/web/config/nginx/nginx.conf
civitas     3326  0.6  2.1 6869116 212992 ?      Ssl  19:52   0:17 java -Xmx3072m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Djava.util.logging.config.file=/run/jicofo/config/logging.properties -Dconfig.file=/run/jicofo/config/jicofo.conf -cp /usr/share/jicofo/jicofo.jar:/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar:/usr/share/jicofo/lib/annotations-23.0.0.jar:/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar:/usr/share/jicofo/lib/commons-lang3-3.12.0.jar:/usr/share/jicofo/lib/config-1.4.3.jar:/usr/share/jicofo/lib/gson-2.8.5.jar:/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar:/usr/share/jicofo/lib/jackson-core-2.18.0.jar:/usr/share/jicofo/lib/jackson-databind-2.18.0.jar:/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar:/usr/share/jicofo/lib/jansi-2.4.1.jar:/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar:/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar:/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar:/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar:/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar:/usr/share/jicofo/lib/jjwt-api-0.12.6.jar:/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar:/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar:/usr/share/jicofo/lib/jna-5.9.0.jar:/usr/share/jicofo/lib/jsr305-3.0.2.jar:/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar:/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar:/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar:/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar:/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar:/usr/share/jicofo/lib/minidns-core-1.0.5.jar:/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar:/usr/share/jicofo/lib/precis-1.1.0.jar:/usr/share/jicofo/lib/sentry-5.4.0.jar:/usr/share/jicofo/lib/simpleclient-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar:/usr/share/jicofo/lib/slf4j-api-1.7.32.jar:/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar:/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar org.jitsi.jicofo.Main
civitas     3344  0.9  2.3 6874456 233876 ?      Ssl  19:52   0:25 java -Xmx3072m -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/run/jvb -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=config -Djava.util.logging.config.file=/run/jvb/config/logging.properties -Dconfig.file=/run/jvb/config/jvb.conf -Djava.io.tmpdir=/run/jvb/tmp -Djna.tmpdir=/run/jvb/tmp -cp /usr/share/jitsi-videobridge/jitsi-videobridge.jar:/usr/share/jitsi-videobridge/lib/* org.jitsi.videobridge.MainKt
civitas     3436  0.0  0.1 197688 12016 ?        S    19:52   0:00 nginx: worker process
civitas     3437  0.0  0.1 197676 11828 ?        S    19:52   0:00 nginx: worker process
civitas     3438  0.0  0.1 197708 12040 ?        S    19:52   0:00 nginx: worker process
civitas     3439  0.0  0.1 197676 11836 ?        S    19:52   0:00 nginx: worker process
civitas     3475  0.1  0.4  85256 46200 ?        Ss   19:52   0:05 lua /usr/bin/prosody --config /run/prosody/config/prosody.cfg.lua -F
root       20184  0.4  0.0  21820  7960 pts/2    S+   20:37   0:00 sudo bash jitsi-infrastructure-audit.sh
root       20188  0.0  0.0  21820  2580 pts/3    Ss   20:37   0:00 sudo bash jitsi-infrastructure-audit.sh
root       20189  8.0  0.0   7208  3432 pts/3    S+   20:37   0:00 bash jitsi-infrastructure-audit.sh
root       21275  0.0  0.0   5576  2032 pts/3    S+   20:37   0:00 tee -a /opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md


## Processus Java


```text
$ ps auxww | grep java | grep -v grep || true
```
civitas     3326  0.6  2.1 6869116 212992 ?      Ssl  19:52   0:17 java -Xmx3072m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Djava.util.logging.config.file=/run/jicofo/config/logging.properties -Dconfig.file=/run/jicofo/config/jicofo.conf -cp /usr/share/jicofo/jicofo.jar:/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar:/usr/share/jicofo/lib/annotations-23.0.0.jar:/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar:/usr/share/jicofo/lib/commons-lang3-3.12.0.jar:/usr/share/jicofo/lib/config-1.4.3.jar:/usr/share/jicofo/lib/gson-2.8.5.jar:/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar:/usr/share/jicofo/lib/jackson-core-2.18.0.jar:/usr/share/jicofo/lib/jackson-databind-2.18.0.jar:/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar:/usr/share/jicofo/lib/jansi-2.4.1.jar:/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar:/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar:/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar:/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar:/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar:/usr/share/jicofo/lib/jjwt-api-0.12.6.jar:/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar:/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar:/usr/share/jicofo/lib/jna-5.9.0.jar:/usr/share/jicofo/lib/jsr305-3.0.2.jar:/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar:/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar:/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar:/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar:/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar:/usr/share/jicofo/lib/minidns-core-1.0.5.jar:/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar:/usr/share/jicofo/lib/precis-1.1.0.jar:/usr/share/jicofo/lib/sentry-5.4.0.jar:/usr/share/jicofo/lib/simpleclient-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar:/usr/share/jicofo/lib/slf4j-api-1.7.32.jar:/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar:/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar org.jitsi.jicofo.Main
civitas     3344  0.9  2.3 6874456 233876 ?      Ssl  19:52   0:25 java -Xmx3072m -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/run/jvb -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=config -Djava.util.logging.config.file=/run/jvb/config/logging.properties -Dconfig.file=/run/jvb/config/jvb.conf -Djava.io.tmpdir=/run/jvb/tmp -Djna.tmpdir=/run/jvb/tmp -cp /usr/share/jitsi-videobridge/jitsi-videobridge.jar:/usr/share/jitsi-videobridge/lib/* org.jitsi.videobridge.MainKt
civitas     3710  3.9  5.1 6464040 519080 ?      Ssl  19:52   1:45 java -Xmx1G -Xms1G -server -XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent -XX:MaxInlineLevel=15 -Djava.awt.headless=true -Xlog:gc*:file=/var/log/kafka/kafkaServer-gc.log:time,tags:filecount=10,filesize=100M -Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dkafka.logs.dir=/var/log/kafka -Dlog4j.configuration=file:/etc/kafka/log4j.properties -cp /usr/bin/../share/java/kafka/*:/usr/bin/../share/java/confluent-telemetry/* kafka.Kafka /etc/kafka/kafka.properties
dhcpcd      4049  1.3  3.4 4274992 348408 ?      Ssl  19:52   0:36 java --add-opens java.rmi/javax.rmi.ssl=ALL-UNNAMED -jar kafka-ui-api.jar


## Processus Prosody


```text
$ ps auxww | grep prosody | grep -v grep || true
```
civitas     3106  0.0  0.0    224    80 ?        S    19:52   0:00 s6-supervise prosody
civitas     3475  0.1  0.4  85256 46200 ?        Ss   19:52   0:05 lua /usr/bin/prosody --config /run/prosody/config/prosody.cfg.lua -F



---

# 13. RECHERCHE GLOBALE DES FICHIERS JITSI

**Date :** 2026-08-12 20:37:26 EDT


## Noms contenant jitsi


```text
$ find / -xdev \( -iname "*jitsi*" -o -iname "*jicofo*" -o -iname "*videobridge*" -o -iname "*prosody*" \) -print 2>/dev/null | sort
```
/etc/apt/keyrings/jitsi.gpg
/etc/apt/sources.list.d/jitsi-stable.list
/etc/systemd/system/jitsi-videobridge2.service.d
/etc/xdg/autostart/org.kde.xwaylandvideobridge.desktop
/home/civitas/.cache/xwaylandvideobridge
/home/civitas/ystemctl restart jitsi-videobridge2
/opt/civitas/GuidePowerJitsiCivitas.md
/opt/civitas/jitsi
/opt/civitas/jitsi-audit
/opt/civitas/jitsi/data/jicofo
/opt/civitas/jitsi/data/prosody
/opt/civitas/jitsi/data/prosody/prosody-plugins-custom
/opt/civitas/jitsi/data/storage/prosody
/opt/civitas/jitsi/data/storage/prosody/auth%2emeet%2ejitsi
/opt/civitas/jitsi/data/storage/prosody/prosody.sock
/opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md
/opt/civitas/jitsi-infrastructure-audit.sh
/opt/civitas/nginx/jitsi-meet-host-backup
/opt/civitas/nginx/jitsi-meet-host-backup/images/jitsilogo.png
/opt/civitas/nginx/jitsi-meet-host-backup/libs/lib-jitsi-meet.e2ee-worker.js
/opt/civitas/nginx/jitsi-meet-host-backup/libs/lib-jitsi-meet.min.js
/opt/civitas/nginx/jitsi-meet-host-backup/libs/lib-jitsi-meet.min.js.LICENSE.txt
/opt/civitas/nginx/jitsi-meet-host-backup/libs/lib-jitsi-meet.min.map
/opt/civitas/nginx/jitsi-meet-host-backup/prosody-plugins
/opt/civitas/nginx/jitsi-meet-host-backup/prosody-plugins/luajwtjitsi.lib.lua
/opt/civitas/nginx/jitsi-meet-host-backup/prosody-plugins/mod_auth_jitsi-anonymous.lua
/opt/civitas/nginx/jitsi-meet-host-backup/prosody-plugins/mod_auth_jitsi-shared-secret.lua
/opt/civitas/nginx/jitsi-meet-host-backup/prosody-plugins/mod_jitsi_permissions.lua
/opt/civitas/nginx/jitsi-meet-host-backup/prosody-plugins/mod_jitsi_session.lua
/opt/civitas/PLAN_SYNCHRONISATION_ROOMS_JITSI.md
/opt/civitas/scripts/jitsi_boot.sh
/opt/civitas/scripts/jitsi_reset_prosody.sh
/opt/civitas/scripts/jitsi_stop.sh
/opt/civitas/scripts/lib/jitsi_common.sh
/opt/civitas/services/peer/event-jitsi.txt
/usr/bin/xwaylandvideobridge
/usr/local/lib/prosody
/usr/share/applications/org.kde.xwaylandvideobridge.desktop
/usr/share/doc/xwaylandvideobridge
/usr/share/icons/hicolor/scalable/apps/xwaylandvideobridge.svg
/usr/share/jitsi-meet
/usr/share/jitsi-meet/prosody-plugins
/usr/share/jitsi-videobridge
/usr/share/lintian/overrides/xwaylandvideobridge
/usr/share/locale/ca/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/ca@valencia/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/cs/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/de/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/en_GB/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/eo/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/es/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/eu/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/fi/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/fr/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/gl/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/it/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/ja/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/ka/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/ko/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/nl/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/nn/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/pl/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/pt_BR/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/pt/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/sk/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/sl/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/sv/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/tr/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/uk/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/locale/zh_CN/LC_MESSAGES/xwaylandvideobridge.mo
/usr/share/metainfo/org.kde.xwaylandvideobridge.appdata.xml
/usr/share/qlogging-categories6/xwaylandvideobridge.categories
/var/cache/apt/archives/jicofo_1.0-1169-1_all.deb
/var/cache/apt/archives/jicofo_1.0-1183-1_all.deb
/var/cache/apt/archives/jicofo_1.0-1189-1_all.deb
/var/cache/apt/archives/jitsi-meet_2.0.10741-1_all.deb
/var/cache/apt/archives/jitsi-meet_2.0.11031-1_all.deb
/var/cache/apt/archives/jitsi-meet_2.0.11146-1_all.deb
/var/cache/apt/archives/jitsi-meet-prosody_1.0.9008-1_all.deb
/var/cache/apt/archives/jitsi-meet-prosody_1.0.9268-1_all.deb
/var/cache/apt/archives/jitsi-meet-prosody_1.0.9365-1_all.deb
/var/cache/apt/archives/jitsi-meet-turnserver_1.0.9008-1_all.deb
/var/cache/apt/archives/jitsi-meet-turnserver_1.0.9268-1_all.deb
/var/cache/apt/archives/jitsi-meet-turnserver_1.0.9365-1_all.deb
/var/cache/apt/archives/jitsi-meet-web_1.0.9008-1_all.deb
/var/cache/apt/archives/jitsi-meet-web_1.0.9268-1_all.deb
/var/cache/apt/archives/jitsi-meet-web_1.0.9365-1_all.deb
/var/cache/apt/archives/jitsi-meet-web-config_1.0.9008-1_all.deb
/var/cache/apt/archives/jitsi-meet-web-config_1.0.9268-1_all.deb
/var/cache/apt/archives/jitsi-meet-web-config_1.0.9365-1_all.deb
/var/cache/apt/archives/jitsi-videobridge2_2.3-272-g0360d0488-1_all.deb
/var/cache/apt/archives/jitsi-videobridge2_2.3-295-g8d5c0037b-1_all.deb
/var/cache/apt/archives/jitsi-videobridge2_2.3-307-g4bb0aead1-1_all.deb
/var/cache/apt/archives/lua-basexx_0.4.1-jitsi1_all.deb
/var/cache/apt/archives/lua-cjson_2.1.0.10-jitsi1_amd64.deb
/var/cache/apt/archives/prosody_13.0.1-1+deb131u_amd64.deb
/var/lib/apt/lists/download.jitsi.org_stable_InRelease
/var/lib/apt/lists/download.jitsi.org_stable_Packages
/var/lib/docker/overlay2/0672ed0c8b1c13cd392a37914adc8aaa990bc42e6c75abe37e2096b9f7a32974/diff/usr/share/doc/jitsi-meet-web
/var/lib/docker/overlay2/0672ed0c8b1c13cd392a37914adc8aaa990bc42e6c75abe37e2096b9f7a32974/diff/usr/share/jitsi-meet
/var/lib/docker/overlay2/0672ed0c8b1c13cd392a37914adc8aaa990bc42e6c75abe37e2096b9f7a32974/diff/usr/share/jitsi-meet/images/jitsilogo.png
/var/lib/docker/overlay2/0672ed0c8b1c13cd392a37914adc8aaa990bc42e6c75abe37e2096b9f7a32974/diff/usr/share/jitsi-meet/libs/lib-jitsi-meet.e2ee-worker.js
/var/lib/docker/overlay2/0672ed0c8b1c13cd392a37914adc8aaa990bc42e6c75abe37e2096b9f7a32974/diff/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.js
/var/lib/docker/overlay2/0672ed0c8b1c13cd392a37914adc8aaa990bc42e6c75abe37e2096b9f7a32974/diff/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.js.LICENSE.txt
/var/lib/docker/overlay2/0672ed0c8b1c13cd392a37914adc8aaa990bc42e6c75abe37e2096b9f7a32974/diff/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.map
/var/lib/docker/overlay2/0672ed0c8b1c13cd392a37914adc8aaa990bc42e6c75abe37e2096b9f7a32974/diff/var/lib/dpkg/info/jitsi-meet-web.list
/var/lib/docker/overlay2/0672ed0c8b1c13cd392a37914adc8aaa990bc42e6c75abe37e2096b9f7a32974/diff/var/lib/dpkg/info/jitsi-meet-web.md5sums
/var/lib/docker/overlay2/1736b9e9503a97accb9676796dfbb2c2e84844827d9851dd77c8e7f33c4187d8/diff/etc/apt/sources.list.d/jitsi.sources
/var/lib/docker/overlay2/1736b9e9503a97accb9676796dfbb2c2e84844827d9851dd77c8e7f33c4187d8/diff/usr/share/keyrings/jitsi.gpg
/var/lib/docker/overlay2/200c400242a0b50a77385c599b44067e5c5c764fd34df7bd3e41f2a79d5ef30a/diff/defaults/conf.d/jitsi-meet.cfg.lua
/var/lib/docker/overlay2/200c400242a0b50a77385c599b44067e5c5c764fd34df7bd3e41f2a79d5ef30a/diff/defaults/prosody.cfg.lua
/var/lib/docker/overlay2/200c400242a0b50a77385c599b44067e5c5c764fd34df7bd3e41f2a79d5ef30a/diff/etc/apt/sources.list.d/prosody.sources
/var/lib/docker/overlay2/200c400242a0b50a77385c599b44067e5c5c764fd34df7bd3e41f2a79d5ef30a/diff/etc/s6-overlay/s6-rc.d/prosody
/var/lib/docker/overlay2/200c400242a0b50a77385c599b44067e5c5c764fd34df7bd3e41f2a79d5ef30a/diff/etc/s6-overlay/s6-rc.d/user/contents.d/prosody
/var/lib/docker/overlay2/200c400242a0b50a77385c599b44067e5c5c764fd34df7bd3e41f2a79d5ef30a/diff/etc/s6-overlay/scripts/prosody
/var/lib/docker/overlay2/200c400242a0b50a77385c599b44067e5c5c764fd34df7bd3e41f2a79d5ef30a/diff/prosody-plugins
/var/lib/docker/overlay2/6cfcab3d459aad624491bfd4e92bd576dbad40196b6079ecae00ecea2484fa86/diff/defaults/jicofo.conf
/var/lib/docker/overlay2/6cfcab3d459aad624491bfd4e92bd576dbad40196b6079ecae00ecea2484fa86/diff/etc/s6-overlay/s6-rc.d/jicofo
/var/lib/docker/overlay2/6cfcab3d459aad624491bfd4e92bd576dbad40196b6079ecae00ecea2484fa86/diff/etc/s6-overlay/s6-rc.d/user/contents.d/jicofo
/var/lib/docker/overlay2/6cfcab3d459aad624491bfd4e92bd576dbad40196b6079ecae00ecea2484fa86/diff/etc/s6-overlay/scripts/jicofo
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/etc/init.d/jitsi-videobridge2
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/etc/jitsi
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/etc/jitsi/videobridge
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/etc/logrotate.d/jitsi-videobridge
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/etc/systemd/system/multi-user.target.wants/jitsi-autoscaler-sidecar.service
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/etc/systemd/system/multi-user.target.wants/jitsi-videobridge2.service
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/lib/systemd/system/jitsi-autoscaler-sidecar.service
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/lib/systemd/system/jitsi-videobridge2.service
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/doc/jitsi-autoscaler-sidecar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/doc/jitsi-videobridge2
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-autoscaler-sidecar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-autoscaler-sidecar/node_modules/@jitsi
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/jitsi-videobridge.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/jain-sip-ri-ossonly-1.2.279-jitsi-oss1.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/jitsi-dcsctp-1.0-7-gb548df2.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/jitsi-media-transform-2.3-307-g4bb0aead1.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/jitsi-metaconfig-1.0-11-g8cf950e.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/jitsi-srtp-1.1-23-gaf3cd06.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/jitsi-utils-1.0-150-g4ab9a3b.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-core-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-extensions-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-im-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-java8-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-resolver-javax-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-sasl-javax-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-streammanagement-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-tcp-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-xmlparser-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/usr/share/jitsi-videobridge/lib/videobridge.rc
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-autoscaler-sidecar.list
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-autoscaler-sidecar.md5sums
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-autoscaler-sidecar.postinst
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-autoscaler-sidecar.postrm
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-videobridge2.conffiles
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-videobridge2.config
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-videobridge2.list
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-videobridge2.md5sums
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-videobridge2.postinst
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-videobridge2.postrm
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-videobridge2.prerm
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/dpkg/info/jitsi-videobridge2.templates
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/systemd/deb-systemd-helper-enabled/jitsi-autoscaler-sidecar.service.dsh-also
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/systemd/deb-systemd-helper-enabled/jitsi-videobridge2.service.dsh-also
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants/jitsi-autoscaler-sidecar.service
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants/jitsi-videobridge2.service
/var/lib/docker/overlay2/6ef7e36be9b8e40006ec210f3a2888044a5c62e48f2382090ac33971b256187b/diff/var/log/jitsi
/var/lib/docker/overlay2/7ecad7e3f99941ce34e977fd0d4db7e73ecd9932e3f6427a61fe7fda723d7a6f/diff/etc/apt/sources.list.d/jitsi.sources
/var/lib/docker/overlay2/8d53c73aa465da60c9b6e0315882d4beca2a87638cc63f65011a472ef691e291/diff/opt/jitsi
/var/lib/docker/overlay2/95c946734a37fdcfe11e0ac18fe00e98cd6a8fa9bf2d622e7f372e842b1a7a45/diff/usr/share/jitsi-meet
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/init.d/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/logrotate.d/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/rc0.d/K01prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/rc1.d/K01prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/rc2.d/S01prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/rc3.d/S01prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/rc4.d/S01prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/rc5.d/S01prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/rc6.d/K01prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/etc/systemd/system/multi-user.target.wants/prosody.service
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/prosody-plugins
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/prosody-plugins-contrib
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/prosody-plugins/luajwtjitsi.lib.lua
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/prosody-plugins/mod_auth_jitsi-anonymous.lua
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/prosody-plugins/mod_auth_jitsi-shared-secret.lua
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/prosody-plugins/mod_jitsi_permissions.lua
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/prosody-plugins/mod_jitsi_session.lua
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/bin/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/bin/prosodyctl
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/prosody/prosody.version
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/systemd/system/prosody.service
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-compat.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-compat.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-crand.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-crand.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-crypto.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-crypto.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-encodings.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-encodings.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-hashes.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-hashes.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-net.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-net.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-poll.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-poll.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-pposix.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-pposix.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-ringbuffer.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-ringbuffer.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-signal.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-signal.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-strbitop.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-strbitop.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-struct.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-struct.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-table.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-table.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-time.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.2-prosody-util-time.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-compat.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-compat.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-crand.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-crand.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-crypto.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-crypto.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-encodings.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-encodings.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-hashes.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-hashes.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-net.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-net.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-poll.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-poll.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-pposix.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-pposix.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-ringbuffer.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-ringbuffer.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-signal.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-signal.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-strbitop.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-strbitop.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-struct.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-struct.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-table.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-table.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-time.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.3-prosody-util-time.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-compat.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-compat.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-crand.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-crand.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-crypto.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-crypto.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-encodings.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-encodings.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-hashes.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-hashes.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-net.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-net.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-poll.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-poll.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-pposix.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-pposix.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-ringbuffer.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-ringbuffer.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-signal.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-signal.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-strbitop.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-strbitop.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-struct.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-struct.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-table.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-table.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-time.so.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/liblua5.4-prosody-util-time.so.0.0.0
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/lua/5.2/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/lua/5.3/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/lib/x86_64-linux-gnu/lua/5.4/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/doc/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/keyrings/prosody.gpg
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/lua/5.2/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/lua/5.2/prosody/util/prosodyctl
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/lua/5.2/prosody/util/prosodyctl.lua
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/lua/5.3/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/lua/5.3/prosody/util/prosodyctl
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/lua/5.3/prosody/util/prosodyctl.lua
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/lua/5.4/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/lua/5.4/prosody/util/prosodyctl
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/usr/share/lua/5.4/prosody/util/prosodyctl.lua
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/dpkg/info/prosody.conffiles
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/dpkg/info/prosody.list
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/dpkg/info/prosody.md5sums
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/dpkg/info/prosody.postinst
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/dpkg/info/prosody.postrm
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/dpkg/info/prosody.preinst
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/dpkg/info/prosody.prerm
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/dpkg/info/prosody.shlibs
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/dpkg/info/prosody.triggers
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/prosody
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants/prosody.service
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/lib/systemd/deb-systemd-helper-enabled/prosody.service.dsh-also
/var/lib/docker/overlay2/a5c41b0c5c46c01e71c1653de978e048f6bcffb1ea30eb77c02dfd55cff95645/diff/var/log/prosody
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/init.d/jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/jitsi
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/jitsi/jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/jitsi/jicofo/jicofo.conf
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/logrotate.d/jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/rc0.d/K01jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/rc1.d/K01jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/rc2.d/S01jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/rc3.d/S01jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/rc4.d/S01jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/rc5.d/S01jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/etc/rc6.d/K01jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/doc/jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/jicofo.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/jicofo.sh
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/var/lib/dpkg/info/jicofo.conffiles
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/var/lib/dpkg/info/jicofo.list
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/var/lib/dpkg/info/jicofo.md5sums
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/var/lib/dpkg/info/jicofo.postinst
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/var/lib/dpkg/info/jicofo.postrm
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/var/lib/dpkg/info/jicofo.preinst
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/var/lib/dpkg/info/jicofo.prerm
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/var/lib/dpkg/info/jicofo.templates
/var/lib/docker/overlay2/a7fcc5a1246aba1c8e76dac0037beb53a4e0c3b3d44f92c5e8ada183f012f710/diff/var/log/jitsi
/var/lib/docker/overlay2/d6a5d4c38036177dab7f082987ec5f750f8f55f4f9f844f5c5c003220fe0b266/diff/prosody-plugins-custom
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.chat.events-0
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.chat.events-1
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.chat.events-2
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.participant.events-0
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.participant.events-1
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.participant.events-2
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.room.events-0
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.room.events-1
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.room.events-2
/var/lib/dpkg/info/xwaylandvideobridge.conffiles
/var/lib/dpkg/info/xwaylandvideobridge.list
/var/lib/dpkg/info/xwaylandvideobridge.md5sums
/var/lib/swcatalog/icons/debian-trixie-main/128x128/xwaylandvideobridge_xwaylandvideobridge.png
/var/lib/swcatalog/icons/debian-trixie-main/48x48/xwaylandvideobridge_xwaylandvideobridge.png
/var/lib/swcatalog/icons/debian-trixie-main/64x64/xwaylandvideobridge_xwaylandvideobridge.png


## Configurations


```text
$ find /etc -xdev -type f 2>/dev/null | grep -Ei "jitsi|jicofo|videobridge|prosody|turnserver" | sort
```
/etc/apt/keyrings/jitsi.gpg
/etc/apt/sources.list.d/jitsi-stable.list
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf
/etc/turnserver.conf.bak
/etc/turnserver/turndb
/etc/ufw/applications.d/turnserver
/etc/xdg/autostart/org.kde.xwaylandvideobridge.desktop


## Services


```text
$ find /etc/systemd /lib/systemd /usr/lib/systemd -type f 2>/dev/null | grep -Ei "jitsi|jicofo|videobridge|prosody|turn" | sort
```
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf
/lib/systemd/system/coturn.service
/usr/lib/systemd/system/coturn.service



---

# 14. /ETC/JITSI

**Date :** 2026-08-12 20:37:39 EDT


```text
$ find /etc/jitsi -print 2>/dev/null | sort || true
```



---

# 15. DONNÉES /VAR/LIB

**Date :** 2026-08-12 20:37:39 EDT


```text
$ find /var/lib -maxdepth 4 \( -iname "*jitsi*" -o -iname "*prosody*" -o -iname "*jicofo*" \) -print 2>/dev/null | sort
```
/var/lib/apt/lists/download.jitsi.org_stable_InRelease
/var/lib/apt/lists/download.jitsi.org_stable_Packages



---

# 16. LOGS

**Date :** 2026-08-12 20:37:39 EDT


## Répertoires


```text
$ find /var/log -maxdepth 4 \( -iname "*jitsi*" -o -iname "*prosody*" -o -iname "*jicofo*" -o -iname "*videobridge*" -o -iname "*turn*" \) -print 2>/dev/null | sort
```
/var/log/turnserver
/var/log/turnserver/turn_1001_2026-08-11.log
/var/log/turnserver/turn_1026_2026-07-27.log
/var/log/turnserver/turn_1031_2026-08-07.log
/var/log/turnserver/turn_1034_2026-08-03.log
/var/log/turnserver/turn_1041_2026-07-30.log
/var/log/turnserver/turn_1042_2026-08-03.log
/var/log/turnserver/turn_1045_2026-08-07.log
/var/log/turnserver/turn_1049_2026-07-30.log
/var/log/turnserver/turn_1050_2026-08-07.log
/var/log/turnserver/turn_1052_2026-08-03.log
/var/log/turnserver/turn_1056_2026-08-07.log
/var/log/turnserver/turn_1057_2026-07-30.log
/var/log/turnserver/turn_1059_2026-08-03.log
/var/log/turnserver/turn_1063_2026-07-30.log
/var/log/turnserver/turn_19351_2026-03-22.log
/var/log/turnserver/turn_20392_2026-07-26.log
/var/log/turnserver/turn_894_2026-08-12.log
/var/log/turnserver/turn_896_2026-08-11.log
/var/log/turnserver/turn_897_2026-08-11.log
/var/log/turnserver/turn_899_2026-08-12.log
/var/log/turnserver/turn_901_2026-08-12.log
/var/log/turnserver/turn_915_2026-08-09.log
/var/log/turnserver/turn_920_2026-07-28.log
/var/log/turnserver/turn_925_2026-07-28.log
/var/log/turnserver/turn_926_2026-07-30.log
/var/log/turnserver/turn_927_2026-08-09.log
/var/log/turnserver/turn_934_2026-07-28.log
/var/log/turnserver/turn_935_2026-08-11.log
/var/log/turnserver/turn_935_2026-08-12.log
/var/log/turnserver/turn_936_2026-08-12.log
/var/log/turnserver/turn_938_2026-08-11.log
/var/log/turnserver/turn_939_2026-08-12.log
/var/log/turnserver/turn_942_2026-08-12.log
/var/log/turnserver/turn_945_2026-08-11.log
/var/log/turnserver/turn_945_2026-08-12.log
/var/log/turnserver/turn_949_2026-08-12.log
/var/log/turnserver/turn_951_2026-08-11.log
/var/log/turnserver/turn_951_2026-08-12.log
/var/log/turnserver/turn_953_2026-08-12.log
/var/log/turnserver/turn_955_2026-08-11.log
/var/log/turnserver/turn_955_2026-08-12.log
/var/log/turnserver/turn_959_2026-08-12.log
/var/log/turnserver/turn_961_2026-07-28.log
/var/log/turnserver/turn_964_2026-07-28.log
/var/log/turnserver/turn_964_2026-08-09.log
/var/log/turnserver/turn_966_2026-07-30.log
/var/log/turnserver/turn_966_2026-08-09.log
/var/log/turnserver/turn_971_2026-07-28.log
/var/log/turnserver/turn_973_2026-07-28.log
/var/log/turnserver/turn_977_2026-07-27.log
/var/log/turnserver/turn_978_2026-08-09.log
/var/log/turnserver/turn_978_2026-08-11.log
/var/log/turnserver/turn_979_2026-07-28.log
/var/log/turnserver/turn_979_2026-07-30.log
/var/log/turnserver/turn_981_2026-07-28.log
/var/log/turnserver/turn_984_2026-07-28.log
/var/log/turnserver/turn_984_2026-07-30.log
/var/log/turnserver/turn_985_2026-07-28.log
/var/log/turnserver/turn_985_2026-08-03.log
/var/log/turnserver/turn_985_2026-08-09.log
/var/log/turnserver/turn_988_2026-07-28.log
/var/log/turnserver/turn_989_2026-08-11.log
/var/log/turnserver/turn_990_2026-07-28.log
/var/log/turnserver/turn_990_2026-07-30.log
/var/log/turnserver/turn_990_2026-08-09.log
/var/log/turnserver/turn_993_2026-08-07.log
/var/log/turnserver/turn_995_2026-08-11.log
/var/log/turnserver/turn_996_2026-07-28.log
/var/log/turnserver/turn_998_2026-07-30.log
/var/log/turnserver/turn.log


## Journalctl


```text
$ journalctl -u jicofo --no-pager -n 300 2>/dev/null || true
```
Mar 22 22:26:53 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 22 22:26:53 meet.civitas.local systemd[1]: jicofo.service: Unit process 94506 (java) remains running after unit stopped.
Mar 22 22:26:53 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:26:53 meet.civitas.local systemd[1]: jicofo.service: Consumed 15.965s CPU time, 433.3M memory peak.
Mar 22 22:26:53 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 94506 (java) in control group while starting unit. Ignoring.
Mar 22 22:26:53 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Mar 22 22:26:53 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:26:53 meet.civitas.local jicofo[97414]: Starting jicofo: jicofo started.
Mar 22 22:26:53 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:29:15 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:29:15 meet.civitas.local jicofo[98791]: Stopping jicofo: jicofo stopped.
Mar 22 22:29:15 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 22 22:29:15 meet.civitas.local systemd[1]: jicofo.service: Unit process 97423 (java) remains running after unit stopped.
Mar 22 22:29:15 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:29:15 meet.civitas.local systemd[1]: jicofo.service: Consumed 13.190s CPU time, 433.3M memory peak.
Mar 22 22:29:15 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 97423 (java) in control group while starting unit. Ignoring.
Mar 22 22:29:15 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Mar 22 22:29:15 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:29:15 meet.civitas.local jicofo[98807]: Starting jicofo: jicofo started.
Mar 22 22:29:15 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:35:41 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:35:41 meet.civitas.local jicofo[99677]: Stopping jicofo: jicofo stopped.
Mar 22 22:35:41 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 22 22:35:41 meet.civitas.local systemd[1]: jicofo.service: Unit process 98816 (java) remains running after unit stopped.
Mar 22 22:35:41 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:35:41 meet.civitas.local systemd[1]: jicofo.service: Consumed 9.094s CPU time, 433.3M memory peak.
Mar 22 22:35:41 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 98816 (java) in control group while starting unit. Ignoring.
Mar 22 22:35:41 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Mar 22 22:35:41 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:35:41 meet.civitas.local jicofo[99685]: Starting jicofo: jicofo started.
Mar 22 22:35:41 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:39:36 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:39:36 meet.civitas.local jicofo[100175]: Stopping jicofo: jicofo stopped.
Mar 22 22:39:36 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 22 22:39:36 meet.civitas.local systemd[1]: jicofo.service: Unit process 99693 (java) remains running after unit stopped.
Mar 22 22:39:36 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:39:36 meet.civitas.local systemd[1]: jicofo.service: Consumed 9.332s CPU time, 433.3M memory peak.
Mar 22 22:39:36 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 99693 (java) in control group while starting unit. Ignoring.
Mar 22 22:39:36 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Mar 22 22:39:36 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:39:36 meet.civitas.local jicofo[100184]: Starting jicofo: jicofo started.
Mar 22 22:39:36 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:53:12 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:53:12 meet.civitas.local jicofo[101668]: Stopping jicofo: jicofo stopped.
Mar 22 22:53:12 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 22 22:53:12 meet.civitas.local systemd[1]: jicofo.service: Unit process 100191 (java) remains running after unit stopped.
Mar 22 22:53:12 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:53:12 meet.civitas.local systemd[1]: jicofo.service: Consumed 10.334s CPU time, 433.3M memory peak.
Mar 22 22:53:12 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 100191 (java) in control group while starting unit. Ignoring.
Mar 22 22:53:12 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Mar 22 22:53:12 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:53:12 meet.civitas.local jicofo[101678]: Starting jicofo: jicofo started.
Mar 22 22:53:12 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:57:50 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:57:50 meet.civitas.local jicofo[102275]: Stopping jicofo: jicofo stopped.
Mar 22 22:57:50 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 22 22:57:50 meet.civitas.local systemd[1]: jicofo.service: Unit process 101684 (java) remains running after unit stopped.
Mar 22 22:57:50 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:57:50 meet.civitas.local systemd[1]: jicofo.service: Consumed 8.463s CPU time, 433.3M memory peak.
Mar 22 22:57:50 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 101684 (java) in control group while starting unit. Ignoring.
Mar 22 22:57:50 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Mar 22 22:57:50 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:57:51 meet.civitas.local jicofo[102285]: Starting jicofo: jicofo started.
Mar 22 22:57:51 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 22 23:04:06 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 22 23:04:06 meet.civitas.local jicofo[103041]: Stopping jicofo: jicofo stopped.
Mar 22 23:04:06 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 22 23:04:06 meet.civitas.local systemd[1]: jicofo.service: Unit process 102291 (java) remains running after unit stopped.
Mar 22 23:04:06 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 22 23:04:06 meet.civitas.local systemd[1]: jicofo.service: Consumed 8.661s CPU time, 433.3M memory peak.
Mar 22 23:04:06 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 102291 (java) in control group while starting unit. Ignoring.
Mar 22 23:04:06 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Mar 22 23:04:06 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 22 23:04:06 meet.civitas.local jicofo[103051]: Starting jicofo: jicofo started.
Mar 22 23:04:06 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 23 12:45:46 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 23 12:45:48 meet.civitas.local jicofo[284902]: Stopping jicofo: jicofo stopped.
Mar 23 12:45:48 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 23 12:45:48 meet.civitas.local systemd[1]: jicofo.service: Unit process 103057 (java) remains running after unit stopped.
Mar 23 12:45:48 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 23 12:45:48 meet.civitas.local systemd[1]: jicofo.service: Consumed 2min 51.760s CPU time, 433.3M memory peak.
-- Boot 9286f364297e4b8c9fe1cccd67828118 --
Mar 23 16:59:54 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 23 16:59:54 meet.civitas.local jicofo[752]: Starting jicofo: jicofo started.
Mar 23 16:59:54 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot 4ae73edac0c84a74baf7f2914fe6b03d --
Mar 24 15:31:02 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 24 15:31:02 meet.civitas.local jicofo[757]: Starting jicofo: jicofo started.
Mar 24 15:31:02 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 24 15:47:09 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 24 15:47:09 meet.civitas.local jicofo[10361]: Stopping jicofo: jicofo stopped.
Mar 24 15:47:09 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 24 15:47:09 meet.civitas.local systemd[1]: jicofo.service: Unit process 795 (java) remains running after unit stopped.
Mar 24 15:47:09 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 24 15:47:09 meet.civitas.local systemd[1]: jicofo.service: Consumed 16.969s CPU time, 241.7M memory peak.
-- Boot 568cd1ca264f48ec9180909763535afe --
Mar 24 15:47:29 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 24 15:47:30 meet.civitas.local jicofo[746]: Starting jicofo: jicofo started.
Mar 24 15:47:30 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 24 16:11:51 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 24 16:11:51 meet.civitas.local jicofo[14068]: Stopping jicofo: jicofo stopped.
Mar 24 16:11:51 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 24 16:11:51 meet.civitas.local systemd[1]: jicofo.service: Unit process 789 (java) remains running after unit stopped.
Mar 24 16:11:51 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 24 16:11:51 meet.civitas.local systemd[1]: jicofo.service: Consumed 14.367s CPU time, 249M memory peak.
-- Boot 08b67ad3b83f49c5839534ae66de410b --
Mar 24 16:14:08 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 24 16:14:08 meet.civitas.local jicofo[758]: Starting jicofo: jicofo started.
Mar 24 16:14:08 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot 6794de94ea1b429592d3c06baf21dadf --
Mar 24 19:42:50 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 24 19:42:50 meet.civitas.local jicofo[759]: Starting jicofo: jicofo started.
Mar 24 19:42:50 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot 57a5210cbd994cc09b58cb1121fe5762 --
Mar 25 15:13:23 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 25 15:13:23 meet.civitas.local jicofo[752]: Starting jicofo: jicofo started.
Mar 25 15:13:23 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 25 20:54:13 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 25 20:54:13 meet.civitas.local jicofo[80323]: Stopping jicofo: jicofo stopped.
Mar 25 20:54:13 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 25 20:54:13 meet.civitas.local systemd[1]: jicofo.service: Unit process 785 (java) remains running after unit stopped.
Mar 25 20:54:13 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 25 20:54:13 meet.civitas.local systemd[1]: jicofo.service: Consumed 53.451s CPU time, 271.7M memory peak.
-- Boot 301e6bd333fb41548b9fa74557909cd8 --
Mar 29 20:31:43 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 29 20:31:43 meet.civitas.local jicofo[750]: Starting jicofo: jicofo started.
Mar 29 20:31:43 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 29 21:18:02 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 29 21:18:03 meet.civitas.local jicofo[16797]: Stopping jicofo: jicofo stopped.
Mar 29 21:18:03 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 29 21:18:03 meet.civitas.local systemd[1]: jicofo.service: Unit process 805 (java) remains running after unit stopped.
Mar 29 21:18:03 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 29 21:18:03 meet.civitas.local systemd[1]: jicofo.service: Consumed 20.966s CPU time, 289.3M memory peak.
-- Boot e39a62a52ead4a1d8fa5eaecb27705df --
Mar 29 21:19:09 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 29 21:19:09 meet.civitas.local jicofo[751]: Starting jicofo: jicofo started.
Mar 29 21:19:09 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 29 21:23:18 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 29 21:23:18 meet.civitas.local jicofo[5545]: Stopping jicofo: jicofo stopped.
Mar 29 21:23:18 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 29 21:23:18 meet.civitas.local systemd[1]: jicofo.service: Unit process 786 (java) remains running after unit stopped.
Mar 29 21:23:18 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 29 21:23:18 meet.civitas.local systemd[1]: jicofo.service: Consumed 9.186s CPU time, 233.5M memory peak.
-- Boot 8a03c0f89e2c45eb80df3e5142baca53 --
Mar 29 21:23:37 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 29 21:23:37 meet.civitas.local jicofo[746]: Starting jicofo: jicofo started.
Mar 29 21:23:37 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 29 21:27:22 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 29 21:27:22 meet.civitas.local jicofo[6875]: Stopping jicofo: jicofo stopped.
Mar 29 21:27:22 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 29 21:27:22 meet.civitas.local systemd[1]: jicofo.service: Unit process 787 (java) remains running after unit stopped.
Mar 29 21:27:22 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 29 21:27:22 meet.civitas.local systemd[1]: jicofo.service: Consumed 10.159s CPU time, 252.4M memory peak.
-- Boot bf5a91c7a1414c8ebcab4db759fa8a3f --
Mar 29 21:27:39 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 29 21:27:39 meet.civitas.local jicofo[747]: Starting jicofo: jicofo started.
Mar 29 21:27:39 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 29 21:33:32 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 29 21:33:32 meet.civitas.local jicofo[5711]: Stopping jicofo: jicofo stopped.
Mar 29 21:33:32 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 29 21:33:32 meet.civitas.local systemd[1]: jicofo.service: Unit process 778 (java) remains running after unit stopped.
Mar 29 21:33:32 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 29 21:33:32 meet.civitas.local systemd[1]: jicofo.service: Consumed 10.728s CPU time, 262M memory peak.
-- Boot 57137ae7f61e48c4a7025e5ce47f91ea --
Mar 29 21:33:50 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 29 21:33:50 meet.civitas.local jicofo[743]: Starting jicofo: jicofo started.
Mar 29 21:33:50 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 29 22:14:46 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 29 22:14:47 meet.civitas.local jicofo[18502]: Stopping jicofo: jicofo stopped.
Mar 29 22:14:47 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 29 22:14:47 meet.civitas.local systemd[1]: jicofo.service: Unit process 777 (java) remains running after unit stopped.
Mar 29 22:14:47 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 29 22:14:47 meet.civitas.local systemd[1]: jicofo.service: Consumed 18.695s CPU time, 261.9M memory peak.
-- Boot ae946aac51d841d294ce09308edb77fe --
Mar 30 06:44:13 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 30 06:44:13 meet.civitas.local jicofo[743]: Starting jicofo: jicofo started.
Mar 30 06:44:13 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot 7c117163ac96474798b75f818b5e53a8 --
Mar 30 07:10:30 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 30 07:10:30 meet.civitas.local jicofo[761]: Starting jicofo: jicofo started.
Mar 30 07:10:30 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 30 07:39:41 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 30 07:39:41 meet.civitas.local jicofo[12216]: Stopping jicofo: jicofo stopped.
Mar 30 07:39:41 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 30 07:39:41 meet.civitas.local systemd[1]: jicofo.service: Unit process 802 (java) remains running after unit stopped.
Mar 30 07:39:41 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 30 07:39:41 meet.civitas.local systemd[1]: jicofo.service: Consumed 17.463s CPU time, 265.9M memory peak.
-- Boot 7646a62e86944797826df153d2564574 --
Jun 07 18:11:33 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jun 07 18:11:33 meet.civitas.local jicofo[753]: Starting jicofo: jicofo started.
Jun 07 18:11:33 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot 19ac8219f53647f8be0b730507a4038a --
Jun 07 18:14:48 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jun 07 18:14:48 meet.civitas.local jicofo[754]: Starting jicofo: jicofo started.
Jun 07 18:14:48 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Jun 08 05:07:32 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Jun 08 05:07:32 meet.civitas.local jicofo[83654]: Stopping jicofo: jicofo stopped.
Jun 08 05:07:32 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Jun 08 05:07:32 meet.civitas.local systemd[1]: jicofo.service: Unit process 783 (java) remains running after unit stopped.
Jun 08 05:07:32 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Jun 08 05:07:32 meet.civitas.local systemd[1]: jicofo.service: Consumed 1min 8.609s CPU time, 261M memory peak.
-- Boot 831c701f6afe41d797ed8e696f31da03 --
Jun 08 05:09:14 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jun 08 05:09:14 meet.civitas.local jicofo[748]: Starting jicofo: jicofo started.
Jun 08 05:09:14 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Jun 08 05:44:12 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Jun 08 05:44:12 meet.civitas.local jicofo[16673]: Stopping jicofo: jicofo stopped.
Jun 08 05:44:12 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Jun 08 05:44:12 meet.civitas.local systemd[1]: jicofo.service: Unit process 784 (java) remains running after unit stopped.
Jun 08 05:44:12 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Jun 08 05:44:12 meet.civitas.local systemd[1]: jicofo.service: Consumed 15.843s CPU time, 264.2M memory peak.
-- Boot 66f55ceb4625476e959db6db6759fd56 --
Jun 08 05:53:03 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jun 08 05:53:03 meet.civitas.local jicofo[744]: Starting jicofo: jicofo started.
Jun 08 05:53:03 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Jun 08 06:11:22 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Jun 08 06:11:22 meet.civitas.local jicofo[8487]: Stopping jicofo: jicofo stopped.
Jun 08 06:11:22 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Jun 08 06:11:22 meet.civitas.local systemd[1]: jicofo.service: Unit process 776 (java) remains running after unit stopped.
Jun 08 06:11:22 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Jun 08 06:11:22 meet.civitas.local systemd[1]: jicofo.service: Consumed 13.340s CPU time, 254M memory peak.
-- Boot bd2833f114004427a0aeb5378dc68895 --
Jun 08 06:11:38 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jun 08 06:11:38 meet.civitas.local jicofo[745]: Starting jicofo: jicofo started.
Jun 08 06:11:38 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Jun 08 06:55:01 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Jun 08 06:55:01 meet.civitas.local jicofo[15894]: Stopping jicofo: jicofo stopped.
Jun 08 06:55:01 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Jun 08 06:55:01 meet.civitas.local systemd[1]: jicofo.service: Unit process 776 (java) remains running after unit stopped.
Jun 08 06:55:01 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Jun 08 06:55:01 meet.civitas.local systemd[1]: jicofo.service: Consumed 14.623s CPU time, 260.4M memory peak.
-- Boot 30e0bdf29e0d4c35a10a8ce8ff8d05e2 --
Jul 26 19:47:12 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jul 26 19:47:12 meet.civitas.local jicofo[745]: Starting jicofo: jicofo started.
Jul 26 19:47:12 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Jul 26 20:06:21 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Jul 26 20:06:21 meet.civitas.local jicofo[18231]: Stopping jicofo: jicofo stopped.
Jul 26 20:06:21 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Jul 26 20:06:21 meet.civitas.local systemd[1]: jicofo.service: Unit process 787 (java) remains running after unit stopped.
Jul 26 20:06:21 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Jul 26 20:06:21 meet.civitas.local systemd[1]: jicofo.service: Consumed 11.586s CPU time, 257.4M memory peak.
Jul 26 20:06:21 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 787 (java) in control group while starting unit. Ignoring.
Jul 26 20:06:21 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Jul 26 20:06:21 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jul 26 20:06:22 meet.civitas.local jicofo[18340]: Starting jicofo: jicofo started.
Jul 26 20:06:22 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Jul 26 21:22:30 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Jul 26 21:22:30 meet.civitas.local jicofo[47859]: Stopping jicofo: jicofo stopped.
Jul 26 21:22:30 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Jul 26 21:22:30 meet.civitas.local systemd[1]: jicofo.service: Unit process 18346 (java) remains running after unit stopped.
Jul 26 21:22:30 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Jul 26 21:22:30 meet.civitas.local systemd[1]: jicofo.service: Consumed 22.062s CPU time, 398M memory peak.
-- Boot ddc43200d1934264a634da29e620643b --
Jul 27 11:23:27 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jul 27 11:23:27 meet.civitas.local jicofo[741]: Starting jicofo: jicofo started.
Jul 27 11:23:27 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot a5e61fb0f1594bc8a5d623704c530484 --
Jul 28 04:01:13 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jul 28 04:01:13 meet.civitas.local jicofo[759]: Starting jicofo: jicofo started.
Jul 28 04:01:13 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot d703551f0f2b4263a30c0caa6ee9da59 --
Jul 28 05:11:54 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jul 28 05:11:54 meet.civitas.local jicofo[755]: Starting jicofo: jicofo started.
Jul 28 05:11:54 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Jul 28 14:29:39 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Jul 28 14:29:39 meet.civitas.local jicofo[22879]: Stopping jicofo: jicofo stopped.
Jul 28 14:29:39 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Jul 28 14:29:39 meet.civitas.local systemd[1]: jicofo.service: Unit process 777 (java) remains running after unit stopped.
Jul 28 14:29:39 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Jul 28 14:29:39 meet.civitas.local systemd[1]: jicofo.service: Consumed 36.977s CPU time, 263.9M memory peak.
-- Boot 9b460f1d92544d3391903b33dfc6fc60 --
Jul 28 14:29:56 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jul 28 14:29:56 meet.civitas.local jicofo[748]: Starting jicofo: jicofo started.
Jul 28 14:29:56 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot 762fb21cee3f48d0af2c2687e37135e5 --
Jul 30 08:23:34 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jul 30 08:23:34 meet.civitas.local jicofo[755]: Starting jicofo: jicofo started.
Jul 30 08:23:34 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot ccc64a87080542548178ba881d657c44 --
Jul 30 14:46:23 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Jul 30 14:46:23 meet.civitas.local jicofo[750]: Starting jicofo: jicofo started.
Jul 30 14:46:23 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot 90f8ed02531e486e82360bc834a91d21 --
Aug 03 10:25:28 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Aug 03 10:25:28 meet.civitas.local jicofo[759]: Starting jicofo: jicofo started.
Aug 03 10:25:28 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Aug 03 11:28:31 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Aug 03 11:28:31 meet.civitas.local jicofo[21058]: Stopping jicofo: jicofo stopped.
Aug 03 11:28:31 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Aug 03 11:28:31 meet.civitas.local systemd[1]: jicofo.service: Unit process 834 (java) remains running after unit stopped.
Aug 03 11:28:31 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Aug 03 11:28:31 meet.civitas.local systemd[1]: jicofo.service: Consumed 15.931s CPU time, 244.8M memory peak.
Aug 03 11:28:32 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 834 (java) in control group while starting unit. Ignoring.
Aug 03 11:28:32 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Aug 03 11:28:32 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Aug 03 11:28:32 meet.civitas.local jicofo[21167]: Starting jicofo: jicofo started.
Aug 03 11:28:32 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Aug 03 11:31:06 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Aug 03 11:31:06 meet.civitas.local jicofo[26246]: Stopping jicofo: jicofo stopped.
Aug 03 11:31:06 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Aug 03 11:31:06 meet.civitas.local systemd[1]: jicofo.service: Unit process 21173 (java) remains running after unit stopped.
Aug 03 11:31:06 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Aug 03 11:31:06 meet.civitas.local systemd[1]: jicofo.service: Consumed 6.480s CPU time, 389.3M memory peak.
Aug 03 11:31:06 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 21173 (java) in control group while starting unit. Ignoring.
Aug 03 11:31:06 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Aug 03 11:31:06 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Aug 03 11:31:06 meet.civitas.local jicofo[26268]: Starting jicofo: jicofo started.
Aug 03 11:31:06 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot ea55d1d83e93437491adcc1394ac26f6 --
Aug 07 05:25:27 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Aug 07 05:25:27 meet.civitas.local jicofo[748]: Starting jicofo: jicofo started.
Aug 07 05:25:27 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot ecc7bebb588040ce87f8c1989b6b6e2b --
Aug 09 14:39:04 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Aug 09 14:39:04 meet.civitas.local jicofo[756]: Starting jicofo: jicofo started.
Aug 09 14:39:04 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot b032f81b9b694164bab7ff2db793668a --
Aug 09 15:09:01 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Aug 09 15:09:01 meet.civitas.local jicofo[753]: Starting jicofo: jicofo started.
Aug 09 15:09:01 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
-- Boot 138ff78abc0a41c4a9100fe18f4bfa2a --
Aug 11 06:23:48 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Aug 11 06:23:48 meet.civitas.local jicofo[762]: Starting jicofo: jicofo started.
Aug 11 06:23:48 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Aug 11 07:32:07 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Aug 11 07:32:07 meet.civitas.local jicofo[44139]: Stopping jicofo: jicofo stopped.
Aug 11 07:32:07 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Aug 11 07:32:07 meet.civitas.local systemd[1]: jicofo.service: Unit process 800 (java) remains running after unit stopped.
Aug 11 07:32:07 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Aug 11 07:32:07 meet.civitas.local systemd[1]: jicofo.service: Consumed 16.657s CPU time, 250.4M memory peak.


```text
$ journalctl -u jitsi-videobridge2 --no-pager -n 300 2>/dev/null || true
```
Mar 22 20:12:01 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:12:01 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:12:01 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 22 20:12:01 meet.civitas.local (bash)[12334]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 22 20:12:01 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 22 20:12:02 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:12:13 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:12:17 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:12:18 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:12:32 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 22 20:12:32 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 22 20:12:32 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 22 20:12:32 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 9.692s CPU time, 201.3M memory peak.
Mar 22 20:12:32 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 22 20:12:32 meet.civitas.local (bash)[14907]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 22 20:12:32 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 22 20:12:35 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:12:36 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:20:34 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:20:34 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:20:34 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 23 12:45:46 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 23 12:45:51 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 23 12:45:51 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 23 12:45:51 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 7min 19.992s CPU time, 360.4M memory peak.
-- Boot 9286f364297e4b8c9fe1cccd67828118 --
Mar 23 16:59:55 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 23 16:59:55 meet.civitas.local (bash)[970]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 23 16:59:56 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot 4ae73edac0c84a74baf7f2914fe6b03d --
Mar 24 15:32:03 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 24 15:32:03 meet.civitas.local (bash)[1091]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 24 15:32:03 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 24 15:47:09 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 24 15:47:10 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 24 15:47:10 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 24 15:47:10 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 23.018s CPU time, 231.4M memory peak.
-- Boot 568cd1ca264f48ec9180909763535afe --
Mar 24 15:48:30 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 24 15:48:30 meet.civitas.local (bash)[1763]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 24 15:48:30 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 24 16:11:51 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 24 16:11:52 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 24 16:11:52 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 24 16:11:52 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 23.413s CPU time, 249.2M memory peak.
-- Boot 08b67ad3b83f49c5839534ae66de410b --
Mar 24 16:14:11 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 24 16:14:11 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 24 16:14:11 meet.civitas.local (bash)[1042]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
-- Boot 6794de94ea1b429592d3c06baf21dadf --
Mar 24 19:42:51 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 24 19:42:51 meet.civitas.local (bash)[978]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 24 19:42:51 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot 57a5210cbd994cc09b58cb1121fe5762 --
Mar 25 15:13:24 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 25 15:13:25 meet.civitas.local (bash)[976]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 25 15:13:25 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 25 20:54:13 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 25 20:54:19 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 25 20:54:19 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 25 20:54:19 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 8min 51.739s CPU time, 389.5M memory peak.
-- Boot 301e6bd333fb41548b9fa74557909cd8 --
Mar 29 20:32:44 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 20:32:44 meet.civitas.local (bash)[1374]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 29 20:32:44 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:02:39 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:02:39 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 29 21:02:39 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:02:39 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 20.860s CPU time, 245.6M memory peak.
Mar 29 21:02:39 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:02:39 meet.civitas.local (bash)[12551]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 29 21:02:39 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:11:17 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 29 21:14:07 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 29 21:14:08 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 29 21:18:01 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:18:02 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 29 21:18:02 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:18:02 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 44.866s CPU time, 302.8M memory peak.
-- Boot e39a62a52ead4a1d8fa5eaecb27705df --
Mar 29 21:19:10 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:19:10 meet.civitas.local (bash)[991]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 29 21:19:10 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:23:13 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 29 21:23:18 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:23:18 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 29 21:23:18 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:23:18 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 13.833s CPU time, 220M memory peak.
-- Boot 8a03c0f89e2c45eb80df3e5142baca53 --
Mar 29 21:23:38 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:23:38 meet.civitas.local (bash)[994]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 29 21:23:38 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:27:21 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:27:22 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 29 21:27:22 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:27:22 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 19.259s CPU time, 320M memory peak.
-- Boot bf5a91c7a1414c8ebcab4db759fa8a3f --
Mar 29 21:28:19 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:28:19 meet.civitas.local (bash)[1763]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 29 21:28:19 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:30:34 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 29 21:33:32 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:33:32 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 29 21:33:32 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:33:32 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 19.935s CPU time, 313.2M memory peak.
-- Boot 57137ae7f61e48c4a7025e5ce47f91ea --
Mar 29 21:33:51 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:33:51 meet.civitas.local (bash)[992]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 29 21:33:51 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:41:30 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:41:30 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 29 21:41:30 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 21:41:30 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 54.949s CPU time, 343.1M memory peak.
Mar 29 21:41:30 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 21:41:30 meet.civitas.local (bash)[6848]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 29 21:41:30 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 22:03:18 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 22:03:18 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 29 22:03:18 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 22:03:18 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 37.353s CPU time, 268.3M memory peak.
Mar 29 22:03:18 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 22:03:18 meet.civitas.local (bash)[14812]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 29 22:03:18 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 22:03:23 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 22:03:23 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 29 22:03:23 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 22:03:23 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 8.521s CPU time, 195.2M memory peak.
Mar 29 22:03:23 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 22:03:23 meet.civitas.local (bash)[14947]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 29 22:03:23 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 22:14:46 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 29 22:14:46 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 29 22:14:46 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 29 22:14:46 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 1min 9.168s CPU time, 313.7M memory peak.
-- Boot ae946aac51d841d294ce09308edb77fe --
Mar 30 06:44:14 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 30 06:44:14 meet.civitas.local (bash)[1048]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 30 06:44:14 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot 7c117163ac96474798b75f818b5e53a8 --
Mar 30 07:10:31 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Mar 30 07:10:31 meet.civitas.local (bash)[998]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Mar 30 07:10:31 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Mar 30 07:39:41 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Mar 30 07:39:41 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Mar 30 07:39:41 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Mar 30 07:39:41 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 50.924s CPU time, 314.8M memory peak.
-- Boot 7646a62e86944797826df153d2564574 --
Jun 07 18:11:36 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jun 07 18:11:36 meet.civitas.local (bash)[1083]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jun 07 18:11:36 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot 19ac8219f53647f8be0b730507a4038a --
Jun 07 18:14:49 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jun 07 18:14:49 meet.civitas.local (bash)[1001]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jun 07 18:14:49 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Jun 08 05:07:31 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Jun 08 05:07:32 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Jun 08 05:07:32 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Jun 08 05:07:32 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 2min 46.612s CPU time, 355.2M memory peak.
-- Boot 831c701f6afe41d797ed8e696f31da03 --
Jun 08 05:09:55 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jun 08 05:09:55 meet.civitas.local (bash)[2139]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jun 08 05:09:55 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Jun 08 05:44:12 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Jun 08 05:44:12 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Jun 08 05:44:12 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Jun 08 05:44:12 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 1min 22.395s CPU time, 345.8M memory peak.
-- Boot 66f55ceb4625476e959db6db6759fd56 --
Jun 08 05:54:04 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jun 08 05:54:04 meet.civitas.local (bash)[1100]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jun 08 05:54:04 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Jun 08 06:11:22 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Jun 08 06:11:22 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Jun 08 06:11:22 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Jun 08 06:11:22 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 17.445s CPU time, 223.7M memory peak.
-- Boot bd2833f114004427a0aeb5378dc68895 --
Jun 08 06:11:40 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jun 08 06:11:40 meet.civitas.local (bash)[999]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jun 08 06:11:40 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Jun 08 06:55:00 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Jun 08 06:55:01 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Jun 08 06:55:01 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Jun 08 06:55:01 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 2min 14.897s CPU time, 345.8M memory peak.
-- Boot 30e0bdf29e0d4c35a10a8ce8ff8d05e2 --
Jul 26 19:47:50 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 26 19:47:50 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Jul 26 19:47:50 meet.civitas.local (bash)[2168]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 26 20:04:11 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:04:11 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:04:12 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Jul 26 20:04:12 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Jul 26 20:04:12 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Jul 26 20:04:12 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 17.183s CPU time, 225.3M memory peak.
Jul 26 20:04:13 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:04:13 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 26 20:04:13 meet.civitas.local (bash)[10933]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 26 20:04:13 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Jul 26 20:04:13 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:04:13 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Jul 26 20:04:13 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Jul 26 20:04:13 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Jul 26 20:04:13 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 1.113s CPU time, 62.8M memory peak.
Jul 26 20:04:13 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 26 20:04:13 meet.civitas.local (bash)[11061]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 26 20:04:13 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Jul 26 20:05:54 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:05:56 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:05:56 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:05:57 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:05:57 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:05:57 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Jul 26 20:05:58 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Jul 26 20:05:58 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Jul 26 20:05:58 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 9.011s CPU time, 210.8M memory peak.
Jul 26 20:05:58 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 26 20:05:58 meet.civitas.local (bash)[15485]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 26 20:05:58 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Jul 26 20:06:02 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:03 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:04 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:05 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:06 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:07 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:08 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:11 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:12 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:14 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:14 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:15 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:15 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:19 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:21 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:26 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:26 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 20:06:42 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Jul 26 21:22:29 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Jul 26 21:22:30 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Jul 26 21:22:30 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Jul 26 21:22:30 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 2min 24.342s CPU time, 333.5M memory peak.
-- Boot ddc43200d1934264a634da29e620643b --
Jul 27 11:23:29 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 27 11:23:29 meet.civitas.local (bash)[1061]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 27 11:23:29 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot a5e61fb0f1594bc8a5d623704c530484 --
Jul 28 04:02:14 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 28 04:02:14 meet.civitas.local (bash)[1127]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 28 04:02:14 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot d703551f0f2b4263a30c0caa6ee9da59 --
Jul 28 05:12:56 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 28 05:12:56 meet.civitas.local (bash)[2218]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 28 05:12:56 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Jul 28 14:29:38 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Jul 28 14:29:39 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Jul 28 14:29:39 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Jul 28 14:29:39 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 49.040s CPU time, 254.8M memory peak.
-- Boot 9b460f1d92544d3391903b33dfc6fc60 --
Jul 28 14:30:57 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 28 14:30:57 meet.civitas.local (bash)[2166]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 28 14:30:57 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot 762fb21cee3f48d0af2c2687e37135e5 --
Jul 30 08:24:09 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 30 08:24:09 meet.civitas.local (bash)[2246]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 30 08:24:09 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot ccc64a87080542548178ba881d657c44 --
Jul 30 14:47:23 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Jul 30 14:47:23 meet.civitas.local (bash)[1118]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Jul 30 14:47:23 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot 90f8ed02531e486e82360bc834a91d21 --
Aug 03 10:25:31 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 03 10:25:31 meet.civitas.local (bash)[1169]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Aug 03 10:25:31 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Aug 03 11:28:18 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 03 11:28:18 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 03 11:28:19 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Aug 03 11:28:19 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Aug 03 11:28:19 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Aug 03 11:28:19 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 26.797s CPU time, 259.9M memory peak.
Aug 03 11:28:19 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 03 11:28:20 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 03 11:28:20 meet.civitas.local (bash)[20572]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Aug 03 11:28:20 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Aug 03 11:28:20 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 03 11:28:20 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Aug 03 11:28:20 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Aug 03 11:28:20 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Aug 03 11:28:20 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 03 11:28:20 meet.civitas.local (bash)[20703]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Aug 03 11:28:20 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Aug 03 11:28:32 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 03 11:28:32 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 03 11:28:33 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 03 11:31:05 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Aug 03 11:31:06 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Aug 03 11:31:06 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Aug 03 11:31:06 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 10.054s CPU time, 206.7M memory peak.
Aug 03 11:31:06 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 03 11:31:06 meet.civitas.local (bash)[26234]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Aug 03 11:31:06 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot ea55d1d83e93437491adcc1394ac26f6 --
Aug 07 05:25:31 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 07 05:25:31 meet.civitas.local (bash)[1162]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Aug 07 05:25:31 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot ecc7bebb588040ce87f8c1989b6b6e2b --
Aug 09 14:40:04 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 09 14:40:04 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Aug 09 14:40:04 meet.civitas.local (bash)[2180]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
-- Boot b032f81b9b694164bab7ff2db793668a --
Aug 09 15:09:02 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 09 15:09:02 meet.civitas.local (bash)[998]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Aug 09 15:09:02 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
-- Boot 138ff78abc0a41c4a9100fe18f4bfa2a --
Aug 11 06:24:49 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 11 06:24:49 meet.civitas.local (bash)[1130]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Aug 11 06:24:49 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.
Aug 11 06:35:05 meet.civitas.local systemd[1]: Stopping jitsi-videobridge2.service - Jitsi Videobridge...
Aug 11 06:35:06 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Deactivated successfully.
Aug 11 06:35:06 meet.civitas.local systemd[1]: Stopped jitsi-videobridge2.service - Jitsi Videobridge.
Aug 11 06:35:06 meet.civitas.local systemd[1]: jitsi-videobridge2.service: Consumed 15.375s CPU time, 244.3M memory peak.
Aug 11 06:35:54 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 06:35:54 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 06:35:54 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 06:36:20 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 06:36:20 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 06:36:20 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 07:46:31 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 07:46:31 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 07:46:31 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 07:46:32 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 07:46:32 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 07:46:32 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Aug 11 07:46:33 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.


```text
$ journalctl -u prosody --no-pager -n 300 2>/dev/null || true
```
Mar 22 22:39:31 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 22 22:39:31 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 22 22:39:31 meet.civitas.local systemd[1]: prosody.service: Consumed 4.306s CPU time, 15.9M memory peak.
Mar 22 22:39:31 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 22 22:39:31 meet.civitas.local prosody[100156]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 22 22:39:31 meet.civitas.local prosody[100156]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 22 22:39:31 meet.civitas.local prosody[100156]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 22 22:39:31 meet.civitas.local prosody[100156]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 22 22:57:45 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 22 22:57:45 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 22 22:57:45 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 22 22:57:45 meet.civitas.local systemd[1]: prosody.service: Consumed 5.958s CPU time, 16.1M memory peak.
Mar 22 22:57:45 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 22 22:57:46 meet.civitas.local prosody[102259]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 22 22:57:46 meet.civitas.local prosody[102259]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 22 22:57:46 meet.civitas.local prosody[102259]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 22 22:57:46 meet.civitas.local prosody[102259]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 22 23:04:01 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 22 23:04:01 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 22 23:04:01 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 22 23:04:01 meet.civitas.local systemd[1]: prosody.service: Consumed 2.854s CPU time, 17.3M memory peak.
Mar 22 23:04:01 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 22 23:04:02 meet.civitas.local prosody[103025]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 22 23:04:02 meet.civitas.local prosody[103025]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 22 23:04:02 meet.civitas.local prosody[103025]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 22 23:04:02 meet.civitas.local prosody[103025]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 23 12:45:46 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 23 12:45:46 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 23 12:45:46 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 23 12:45:46 meet.civitas.local systemd[1]: prosody.service: Consumed 4min 17.211s CPU time, 17.6M memory peak.
-- Boot 9286f364297e4b8c9fe1cccd67828118 --
Mar 23 16:59:56 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 23 16:59:57 meet.civitas.local prosody[1022]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 23 16:59:57 meet.civitas.local prosody[1022]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 23 16:59:57 meet.civitas.local prosody[1022]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 23 16:59:57 meet.civitas.local prosody[1022]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
-- Boot 4ae73edac0c84a74baf7f2914fe6b03d --
Mar 24 15:32:04 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 24 15:32:06 meet.civitas.local prosody[1140]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 24 15:32:06 meet.civitas.local prosody[1140]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 24 15:32:06 meet.civitas.local prosody[1140]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 24 15:32:06 meet.civitas.local prosody[1140]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 24 15:47:09 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 24 15:47:09 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 24 15:47:09 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 24 15:47:09 meet.civitas.local systemd[1]: prosody.service: Consumed 6.777s CPU time, 25.2M memory peak.
-- Boot 568cd1ca264f48ec9180909763535afe --
Mar 24 15:48:30 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 24 15:48:31 meet.civitas.local prosody[1811]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 24 15:48:31 meet.civitas.local prosody[1811]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 24 15:48:31 meet.civitas.local prosody[1811]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 24 15:48:31 meet.civitas.local prosody[1811]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 24 16:11:51 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 24 16:11:51 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 24 16:11:51 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 24 16:11:51 meet.civitas.local systemd[1]: prosody.service: Consumed 7.379s CPU time, 23.2M memory peak.
-- Boot 08b67ad3b83f49c5839534ae66de410b --
Mar 24 16:14:11 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 24 16:14:13 meet.civitas.local prosody[1105]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 24 16:14:13 meet.civitas.local prosody[1105]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 24 16:14:13 meet.civitas.local prosody[1105]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 24 16:14:13 meet.civitas.local prosody[1105]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
-- Boot 6794de94ea1b429592d3c06baf21dadf --
Mar 24 19:42:51 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 24 19:42:53 meet.civitas.local prosody[1026]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 24 19:42:53 meet.civitas.local prosody[1026]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 24 19:42:53 meet.civitas.local prosody[1026]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 24 19:42:53 meet.civitas.local prosody[1026]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
-- Boot 57a5210cbd994cc09b58cb1121fe5762 --
Mar 25 15:13:25 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 25 15:13:26 meet.civitas.local prosody[1026]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 25 15:13:26 meet.civitas.local prosody[1026]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 25 15:13:26 meet.civitas.local prosody[1026]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 25 15:13:26 meet.civitas.local prosody[1026]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 25 20:54:13 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 25 20:54:13 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 25 20:54:13 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 25 20:54:13 meet.civitas.local systemd[1]: prosody.service: Consumed 1min 4.597s CPU time, 25.7M memory peak.
-- Boot 301e6bd333fb41548b9fa74557909cd8 --
Mar 29 20:32:44 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 29 20:32:45 meet.civitas.local prosody[1422]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 29 20:32:45 meet.civitas.local prosody[1422]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 29 20:32:45 meet.civitas.local prosody[1422]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 29 20:32:45 meet.civitas.local prosody[1422]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 29 21:11:18 meet.civitas.local systemd[1]: Reloading prosody.service - Prosody XMPP Server...
Mar 29 21:11:18 meet.civitas.local systemd[1]: Reloaded prosody.service - Prosody XMPP Server.
Mar 29 21:18:02 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 29 21:18:02 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 29 21:18:02 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 29 21:18:02 meet.civitas.local systemd[1]: prosody.service: Consumed 13.383s CPU time, 24.6M memory peak.
-- Boot e39a62a52ead4a1d8fa5eaecb27705df --
Mar 29 21:19:10 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 29 21:19:12 meet.civitas.local prosody[990]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 29 21:19:12 meet.civitas.local prosody[990]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 29 21:19:12 meet.civitas.local prosody[990]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 29 21:19:12 meet.civitas.local prosody[990]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 29 21:23:18 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 29 21:23:18 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 29 21:23:18 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 29 21:23:18 meet.civitas.local systemd[1]: prosody.service: Consumed 2.188s CPU time, 25.1M memory peak.
-- Boot 8a03c0f89e2c45eb80df3e5142baca53 --
Mar 29 21:23:38 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 29 21:23:39 meet.civitas.local prosody[993]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 29 21:23:39 meet.civitas.local prosody[993]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 29 21:23:39 meet.civitas.local prosody[993]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 29 21:23:39 meet.civitas.local prosody[993]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 29 21:27:22 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 29 21:27:22 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 29 21:27:22 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 29 21:27:22 meet.civitas.local systemd[1]: prosody.service: Consumed 2.283s CPU time, 23.8M memory peak.
-- Boot bf5a91c7a1414c8ebcab4db759fa8a3f --
Mar 29 21:28:19 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 29 21:28:19 meet.civitas.local prosody[1762]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 29 21:28:19 meet.civitas.local prosody[1762]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 29 21:28:19 meet.civitas.local prosody[1762]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 29 21:28:19 meet.civitas.local prosody[1762]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 29 21:33:32 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 29 21:33:32 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 29 21:33:32 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 29 21:33:32 meet.civitas.local systemd[1]: prosody.service: Consumed 2.680s CPU time, 22M memory peak.
-- Boot 57137ae7f61e48c4a7025e5ce47f91ea --
Mar 29 21:33:51 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 29 21:33:51 meet.civitas.local prosody[991]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 29 21:33:51 meet.civitas.local prosody[991]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 29 21:33:51 meet.civitas.local prosody[991]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 29 21:33:51 meet.civitas.local prosody[991]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 29 22:14:46 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 29 22:14:46 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 29 22:14:46 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 29 22:14:46 meet.civitas.local systemd[1]: prosody.service: Consumed 14.883s CPU time, 27.1M memory peak.
-- Boot ae946aac51d841d294ce09308edb77fe --
Mar 30 06:44:14 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 30 06:44:15 meet.civitas.local prosody[1047]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 30 06:44:15 meet.civitas.local prosody[1047]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 30 06:44:15 meet.civitas.local prosody[1047]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 30 06:44:15 meet.civitas.local prosody[1047]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
-- Boot 7c117163ac96474798b75f818b5e53a8 --
Mar 30 07:10:31 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 30 07:10:33 meet.civitas.local prosody[997]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 30 07:10:33 meet.civitas.local prosody[997]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 30 07:10:33 meet.civitas.local prosody[997]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 30 07:10:33 meet.civitas.local prosody[997]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 30 07:39:41 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 30 07:39:41 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 30 07:39:41 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 30 07:39:41 meet.civitas.local systemd[1]: prosody.service: Consumed 8.531s CPU time, 25.3M memory peak.
-- Boot 7646a62e86944797826df153d2564574 --
Jun 07 18:11:36 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jun 07 18:11:37 meet.civitas.local prosody[1081]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jun 07 18:11:37 meet.civitas.local prosody[1081]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jun 07 18:11:37 meet.civitas.local prosody[1081]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jun 07 18:11:37 meet.civitas.local prosody[1081]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
-- Boot 19ac8219f53647f8be0b730507a4038a --
Jun 07 18:14:49 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jun 07 18:14:50 meet.civitas.local prosody[1000]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jun 07 18:14:50 meet.civitas.local prosody[1000]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jun 07 18:14:50 meet.civitas.local prosody[1000]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jun 07 18:14:50 meet.civitas.local prosody[1000]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jun 07 18:37:35 meet.civitas.local systemd[1]: Reloading prosody.service - Prosody XMPP Server...
Jun 07 18:37:35 meet.civitas.local systemd[1]: Reloaded prosody.service - Prosody XMPP Server.
Jun 08 05:07:32 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Jun 08 05:07:32 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Jun 08 05:07:32 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Jun 08 05:07:32 meet.civitas.local systemd[1]: prosody.service: Consumed 1min 36.106s CPU time, 26.9M memory peak.
-- Boot 831c701f6afe41d797ed8e696f31da03 --
Jun 08 05:09:55 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jun 08 05:09:56 meet.civitas.local prosody[2138]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jun 08 05:09:56 meet.civitas.local prosody[2138]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jun 08 05:09:56 meet.civitas.local prosody[2138]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jun 08 05:09:56 meet.civitas.local prosody[2138]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jun 08 05:44:12 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Jun 08 05:44:12 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Jun 08 05:44:12 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Jun 08 05:44:12 meet.civitas.local systemd[1]: prosody.service: Consumed 8.787s CPU time, 24.8M memory peak.
-- Boot 66f55ceb4625476e959db6db6759fd56 --
Jun 08 05:54:04 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jun 08 05:54:05 meet.civitas.local prosody[1099]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jun 08 05:54:05 meet.civitas.local prosody[1099]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jun 08 05:54:05 meet.civitas.local prosody[1099]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jun 08 05:54:05 meet.civitas.local prosody[1099]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jun 08 06:11:22 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Jun 08 06:11:22 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Jun 08 06:11:22 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Jun 08 06:11:22 meet.civitas.local systemd[1]: prosody.service: Consumed 5.941s CPU time, 25.2M memory peak.
-- Boot bd2833f114004427a0aeb5378dc68895 --
Jun 08 06:11:39 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jun 08 06:11:40 meet.civitas.local prosody[998]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jun 08 06:11:40 meet.civitas.local prosody[998]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jun 08 06:11:40 meet.civitas.local prosody[998]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jun 08 06:11:40 meet.civitas.local prosody[998]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jun 08 06:55:01 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Jun 08 06:55:01 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Jun 08 06:55:01 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Jun 08 06:55:01 meet.civitas.local systemd[1]: prosody.service: Consumed 9.338s CPU time, 26.1M memory peak.
-- Boot 30e0bdf29e0d4c35a10a8ce8ff8d05e2 --
Jul 26 19:47:50 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jul 26 19:47:51 meet.civitas.local prosody[2167]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jul 26 19:47:51 meet.civitas.local prosody[2167]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jul 26 19:47:51 meet.civitas.local prosody[2167]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jul 26 19:47:51 meet.civitas.local prosody[2167]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jul 26 20:04:12 meet.civitas.local systemd[1]: Reloading prosody.service - Prosody XMPP Server...
Jul 26 20:04:12 meet.civitas.local systemd[1]: Reloaded prosody.service - Prosody XMPP Server.
Jul 26 20:05:58 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Jul 26 20:05:58 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Jul 26 20:05:58 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Jul 26 20:05:58 meet.civitas.local systemd[1]: prosody.service: Consumed 5.386s CPU time, 23.3M memory peak.
Jul 26 20:05:58 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jul 26 20:05:59 meet.civitas.local prosody[15484]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Jul 26 20:05:59 meet.civitas.local prosody[15484]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jul 26 20:05:59 meet.civitas.local prosody[15484]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Jul 26 20:05:59 meet.civitas.local prosody[15484]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jul 26 20:05:59 meet.civitas.local prosody[15484]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jul 26 20:05:59 meet.civitas.local prosody[15484]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jul 26 20:05:59 meet.civitas.local prosody[15484]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Jul 26 21:22:30 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Jul 26 21:22:30 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Jul 26 21:22:30 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Jul 26 21:22:30 meet.civitas.local systemd[1]: prosody.service: Consumed 19.052s CPU time, 19.5M memory peak.
-- Boot ddc43200d1934264a634da29e620643b --
Jul 27 11:23:28 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jul 27 11:23:30 meet.civitas.local prosody[1060]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jul 27 11:23:30 meet.civitas.local prosody[1060]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jul 27 11:23:30 meet.civitas.local prosody[1060]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jul 27 11:23:30 meet.civitas.local prosody[1060]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jul 27 11:23:30 meet.civitas.local prosody[1060]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Jul 27 11:23:30 meet.civitas.local prosody[1060]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Jul 27 11:23:30 meet.civitas.local prosody[1060]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
-- Boot a5e61fb0f1594bc8a5d623704c530484 --
Jul 28 04:02:14 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jul 28 04:02:14 meet.civitas.local prosody[1126]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Jul 28 04:02:14 meet.civitas.local prosody[1126]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Jul 28 04:02:14 meet.civitas.local prosody[1126]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jul 28 04:02:15 meet.civitas.local prosody[1126]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jul 28 04:02:15 meet.civitas.local prosody[1126]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Jul 28 04:02:15 meet.civitas.local prosody[1126]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jul 28 04:02:15 meet.civitas.local prosody[1126]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
-- Boot d703551f0f2b4263a30c0caa6ee9da59 --
Jul 28 05:12:56 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jul 28 05:12:58 meet.civitas.local prosody[2217]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Jul 28 05:12:58 meet.civitas.local prosody[2217]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jul 28 05:12:58 meet.civitas.local prosody[2217]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jul 28 05:12:58 meet.civitas.local prosody[2217]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jul 28 05:12:58 meet.civitas.local prosody[2217]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jul 28 05:12:58 meet.civitas.local prosody[2217]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Jul 28 05:12:58 meet.civitas.local prosody[2217]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Jul 28 14:29:39 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Jul 28 14:29:39 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Jul 28 14:29:39 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Jul 28 14:29:39 meet.civitas.local systemd[1]: prosody.service: Consumed 31.212s CPU time, 23.5M memory peak.
-- Boot 9b460f1d92544d3391903b33dfc6fc60 --
Jul 28 14:30:57 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jul 28 14:30:58 meet.civitas.local prosody[2165]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jul 28 14:30:58 meet.civitas.local prosody[2165]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jul 28 14:30:59 meet.civitas.local prosody[2165]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Jul 28 14:30:59 meet.civitas.local prosody[2165]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jul 28 14:30:59 meet.civitas.local prosody[2165]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Jul 28 14:30:59 meet.civitas.local prosody[2165]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Jul 28 14:30:59 meet.civitas.local prosody[2165]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
-- Boot 762fb21cee3f48d0af2c2687e37135e5 --
Jul 30 08:24:09 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jul 30 08:24:10 meet.civitas.local prosody[2245]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Jul 30 08:24:10 meet.civitas.local prosody[2245]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Jul 30 08:24:10 meet.civitas.local prosody[2245]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Jul 30 08:24:10 meet.civitas.local prosody[2245]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jul 30 08:24:10 meet.civitas.local prosody[2245]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jul 30 08:24:10 meet.civitas.local prosody[2245]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jul 30 08:24:10 meet.civitas.local prosody[2245]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
-- Boot ccc64a87080542548178ba881d657c44 --
Jul 30 14:47:23 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Jul 30 14:47:25 meet.civitas.local prosody[1117]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Jul 30 14:47:25 meet.civitas.local prosody[1117]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Jul 30 14:47:25 meet.civitas.local prosody[1117]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Jul 30 14:47:25 meet.civitas.local prosody[1117]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Jul 30 14:47:25 meet.civitas.local prosody[1117]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Jul 30 14:47:25 meet.civitas.local prosody[1117]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Jul 30 14:47:25 meet.civitas.local prosody[1117]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
-- Boot 90f8ed02531e486e82360bc834a91d21 --
Aug 03 10:25:31 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Aug 03 10:25:32 meet.civitas.local prosody[1167]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Aug 03 10:25:32 meet.civitas.local prosody[1167]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Aug 03 10:25:32 meet.civitas.local prosody[1167]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Aug 03 10:25:32 meet.civitas.local prosody[1167]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Aug 03 10:25:32 meet.civitas.local prosody[1167]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Aug 03 10:25:32 meet.civitas.local prosody[1167]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Aug 03 10:25:32 meet.civitas.local prosody[1167]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Aug 03 10:51:51 meet.civitas.local systemd[1]: Reloading prosody.service - Prosody XMPP Server...
Aug 03 10:51:51 meet.civitas.local systemd[1]: Reloaded prosody.service - Prosody XMPP Server.
-- Boot ea55d1d83e93437491adcc1394ac26f6 --
Aug 07 05:25:31 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Aug 07 05:25:31 meet.civitas.local prosody[1161]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Aug 07 05:25:31 meet.civitas.local prosody[1161]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Aug 07 05:25:31 meet.civitas.local prosody[1161]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Aug 07 05:25:31 meet.civitas.local prosody[1161]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Aug 07 05:25:31 meet.civitas.local prosody[1161]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Aug 07 05:25:31 meet.civitas.local prosody[1161]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Aug 07 05:25:31 meet.civitas.local prosody[1161]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
-- Boot ecc7bebb588040ce87f8c1989b6b6e2b --
Aug 09 14:40:04 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Aug 09 14:40:05 meet.civitas.local prosody[2179]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Aug 09 14:40:05 meet.civitas.local prosody[2179]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Aug 09 14:40:05 meet.civitas.local prosody[2179]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Aug 09 14:40:05 meet.civitas.local prosody[2179]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Aug 09 14:40:05 meet.civitas.local prosody[2179]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Aug 09 14:40:05 meet.civitas.local prosody[2179]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Aug 09 14:40:05 meet.civitas.local prosody[2179]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
-- Boot b032f81b9b694164bab7ff2db793668a --
Aug 09 15:09:02 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Aug 09 15:09:03 meet.civitas.local prosody[997]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Aug 09 15:09:03 meet.civitas.local prosody[997]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Aug 09 15:09:03 meet.civitas.local prosody[997]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Aug 09 15:09:03 meet.civitas.local prosody[997]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Aug 09 15:09:03 meet.civitas.local prosody[997]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Aug 09 15:09:03 meet.civitas.local prosody[997]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Aug 09 15:09:03 meet.civitas.local prosody[997]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
-- Boot 138ff78abc0a41c4a9100fe18f4bfa2a --
Aug 11 06:24:49 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Aug 11 06:24:49 meet.civitas.local prosody[1129]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Aug 11 06:24:49 meet.civitas.local prosody[1129]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Aug 11 06:24:49 meet.civitas.local prosody[1129]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Aug 11 06:24:49 meet.civitas.local prosody[1129]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Aug 11 06:24:50 meet.civitas.local prosody[1129]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Aug 11 06:24:50 meet.civitas.local prosody[1129]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Aug 11 06:24:50 meet.civitas.local prosody[1129]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Aug 11 06:36:21 meet.civitas.local systemd[1]: Reloading prosody.service - Prosody XMPP Server...
Aug 11 06:36:21 meet.civitas.local systemd[1]: Reloaded prosody.service - Prosody XMPP Server.
Aug 11 07:32:07 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Aug 11 07:32:07 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Aug 11 07:32:07 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Aug 11 07:32:07 meet.civitas.local systemd[1]: prosody.service: Consumed 3.349s CPU time, 26.7M memory peak.
Aug 11 07:46:48 meet.civitas.local systemd[1]: prosody.service: Unit cannot be reloaded because it is inactive.


```text
$ journalctl -u coturn --no-pager -n 300 2>/dev/null || true
```
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Valid formats are 1.2.3.4:5555 for IPv4 and [1:2::3:4]:5555 for IPv6.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --udp-self-balance                                (recommended for older Linuxes only) Automatically balance UDP traffic
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 over auxiliary servers (if configured).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The load balancing is using the ALTERNATE-SERVER mechanism.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The TURN client must support 300 ALTERNATE-SERVER response for this functionality.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -i, --relay-device                <device-name>        Relay interface device for relay sockets (NOT RECOMMENDED. Optional, Linux only).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -E, --relay-ip                <ip>                        Relay address (the local IP address that will be used to relay the
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 packets to the peer).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Multiple relay addresses may be used.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The same IP(s) can be used as both listening IP(s) and relay IP(s).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 If no relay IP(s) specified, then the turnserver will apply the default
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 policy: it will decide itself which relay addresses to be used, and it
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 will always be using the client socket IP address as the relay IP address
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 of the TURN session (if the requested relay address family is the same
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 as the family of the client socket).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -X, --external-ip  <public-ip[/private-ip]>        TURN Server public/private address mapping, if the server is behind NAT.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 In that situation, if a -X is used in form "-X ip" then that ip will be reported
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 as relay IP address of all allocations. This scenario works only in a simple case
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 when one single relay address is be used, and no STUN CHANGE_REQUEST
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 functionality is required.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 That single relay address must be mapped by NAT to the 'external' IP.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 For that 'external' IP, NAT must forward ports directly (relayed port 12345
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 must be always mapped to the same 'external' port 12345).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 In more complex case when more than one IP address is involved,
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 that option must be used several times in the command line, each entry must
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 have form "-X public-ip/private-ip", to map all involved addresses.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --allow-loopback-peers                                Allow peers on the loopback addresses (127.x.x.x and ::1).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-multicast-peers                                Disallow peers on well-known broadcast addresses (224.0.0.0 and above, and FFXX:*).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -m, --relay-threads                <number>        Number of relay threads to handle the established connections
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 (in addition to authentication thread and the listener thread).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 If explicitly set to 0 then application runs in single-threaded mode.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 If not set then a default OS-dependent optimal algorithm will be employed.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The default thread number is the number of CPUs.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 In older systems (pre-Linux 3.9) the number of UDP relay threads always equals
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 the number of listening endpoints (unless -m 0 is set).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --min-port                        <port>                Lower bound of the UDP port range for relay endpoints allocation.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Default value is 49152, according to RFC 5766.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --max-port                        <port>                Upper bound of the UDP port range for relay endpoints allocation.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Default value is 65535, according to RFC 5766.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -v, --verbose                                        'Moderate' verbose mode.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -V, --Verbose                                        Extra verbose mode, very annoying (for debug purposes only).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -o, --daemon                                        Start process as daemon (detach from current shell).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-software-attribute                         Production mode: hide the software version (formerly --prod).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -f, --fingerprint                                Use fingerprints in the TURN messages.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -a, --lt-cred-mech                                Use the long-term credential mechanism.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -z, --no-auth                                        Do not use any credential mechanism, allow anonymous access.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -u, --user                        <user:pwd>        User account, in form 'username:password', for long-term credentials.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Cannot be used with TURN REST API.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -r, --realm                        <realm>                The default realm to be used for the users when no explicit
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 origin/realm relationship was found in the database.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Must be used with long-term credentials
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 mechanism or with TURN REST API.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --check-origin-consistency                        The flag that sets the origin consistency check:
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 across the session, all requests must have the same
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 main ORIGIN attribute value (if the ORIGIN was
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 initially used by the session).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -q, --user-quota                <number>        Per-user allocation quota: how many concurrent allocations a user can create.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This option can also be set through the database, for a particular realm.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -Q, --total-quota                <number>        Total allocations quota: global limit on concurrent allocations.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This option can also be set through the database, for a particular realm.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -s, --max-bps                        <number>        Default max bytes-per-second bandwidth a TURN session is allowed to handle
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 (input and output network streams are treated separately). Anything above
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 that limit will be dropped or temporary suppressed
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 (within the available buffer limits).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This option can also be set through the database, for a particular realm.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -B, --bps-capacity                <number>        Maximum server capacity.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Total bytes-per-second bandwidth the TURN server is allowed to allocate
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 for the sessions, combined (input and output network streams are treated separately).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -c                                <filename>        Configuration file name (default - turnserver.conf).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -b, , --db, --userdb        <filename>                SQLite database file name; default - /var/db/turndb or
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                     /usr/local/var/db/turndb or /var/lib/turn/turndb.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -e, --psql-userdb, --sql-userdb <conn-string>        PostgreSQL database connection string, if used (default - empty, no PostreSQL DB used).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This database can be used for long-term credentials mechanism users,
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 and it can store the secret value(s) for secret-based timed authentication in TURN REST API.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 See http://www.postgresql.org/docs/8.4/static/libpq-connect.html for 8.x PostgreSQL
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 versions format, see
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 http://www.postgresql.org/docs/9.2/static/libpq-connect.html#LIBPQ-CONNSTRING
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 for 9.x and newer connection string formats.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -M, --mysql-userdb        <connection-string>        MySQL database connection string, if used (default - empty, no MySQL DB used).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This database can be used for long-term credentials mechanism users,
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 and it can store the secret value(s) for secret-based timed authentication in TURN REST API.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The connection string my be space-separated list of parameters:
Aug 12 19:51:14 meet.civitas.local systemd[1]: coturn.service: Main process exited, code=exited, status=255/EXCEPTION
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                   "host=<ip-addr> dbname=<database-name> user=<database-user> \
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                         password=<database-user-password> port=<db-port> connect_timeout=<seconds> read_timeout=<seconds>".
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The connection string parameters for the secure communications (SSL):
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 ca, capath, cert, key, cipher
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 (see http://dev.mysql.com/doc/refman/5.1/en/ssl-options.html for the
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 command options description).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                   All connection-string parameters are optional.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --secret-key-file        <filename>                This is the file path which contain secret key of aes encryption while using MySQL password encryption.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 If you want to use in the MySQL connection string the password in encrypted format,
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 then set in this option the file path of the secret key. The key which is used to encrypt MySQL password.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Warning: If this option is set, then MySQL password must be set in "mysql-userdb" option in encrypted format!
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 If you want to use cleartext password then do not set this option!
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -N, --redis-userdb        <connection-string>        Redis user database connection string, if used (default - empty, no Redis DB used).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This database can be used for long-term credentials mechanism users,
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 and it can store the secret value(s) for secret-based timed authentication in TURN REST API.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The connection string my be space-separated list of parameters:
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                   "host=<ip-addr> dbname=<db-number> \
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                                 password=<database-user-password> port=<db-port> connect_timeout=<seconds>".
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                   All connection-string parameters are optional.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -O, --redis-statsdb        <connection-string>        Redis status and statistics database connection string, if used
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 (default - empty, no Redis stats DB used).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This database keeps allocations status information, and it can be also used for publishing
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 and delivering traffic and allocation event notifications.
Aug 12 19:51:14 meet.civitas.local systemd[1]: coturn.service: Failed with result 'exit-code'.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The connection string has the same parameters as redis-userdb connection string.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --use-auth-secret                                TURN REST API flag.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Flag that sets a special authorization option that is based upon authentication secret
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 (TURN Server REST API, see TURNServerRESTAPI.pdf). This option is used with timestamp.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --static-auth-secret                <secret>        'Static' authentication secret value (a string) for TURN REST API only.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 If not set, then the turn server will try to use the 'dynamic' value
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 in turn_secret table in user database (if present).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 That database value can be changed on-the-fly
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 by a separate program, so this is why it is 'dynamic'.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Multiple shared secrets can be used (both in the database and in the "static" fashion).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-auth-pings                                Disable periodic health checks to 'dynamic' auth secret tables.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-dynamic-ip-list                                Do not use dynamic allowed/denied peer ip list.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-dynamic-realms                                Do not use dynamic realm assignment and options.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --server-name                                        Server name used for
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 the oAuth authentication purposes.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The default value is the realm name.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --oauth                                        Support oAuth authentication.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -n                                                Do not use configuration file, take all parameters from the command line only.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --cert                        <filename>                Certificate file, PEM format. Same file search rules
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 applied as for the configuration file.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 If both --no-tls and --no_dtls options
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 are specified, then this parameter is not needed.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --pkey                        <filename>                Private key file, PEM format. Same file search rules
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 applied as for the configuration file.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 If both --no-tls and --no-dtls options
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --pkey-pwd                <password>                If the private key file is encrypted, then this password to be used.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --cipher-list        <"cipher-string">                Allowed OpenSSL cipher list for TLS/DTLS connections.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Default value is "DEFAULT".
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --CA-file                <filename>                CA file in OpenSSL format.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Forces TURN server to verify the client SSL certificates.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 By default, no CA is set and no client certificate check is performed.
Aug 12 19:51:14 meet.civitas.local systemd[1]: Failed to start coturn.service - coTURN STUN/TURN Server.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --ec-curve-name        <curve-name>                Curve name for EC ciphers, if supported by OpenSSL
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 library (TLS and DTLS). The default value is prime256v1,
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 if pre-OpenSSL 1.0.2 is used. With OpenSSL 1.0.2+,
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 an optimal curve will be automatically calculated, if not defined
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 by this option.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --dh566                                        Use 566 bits predefined DH TLS key. Default size of the predefined key is 2066.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --dh1066                                        Use 1066 bits predefined DH TLS key. Default size of the predefined key is 2066.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --dh-file        <dh-file-name>                        Use custom DH TLS key, stored in PEM format in the file.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Flags --dh566 and --dh1066 are ignored when the DH key is taken from a file.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-tlsv1                                        Do not allow TLSv1/DTLSv1 protocol.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-tlsv1_1                                        Do not allow TLSv1.1 protocol.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-tlsv1_2                                        Do not allow TLSv1.2/DTLSv1.2 protocol.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-udp                                        Do not start UDP client listeners.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-tcp                                        Do not start TCP client listeners.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-tls                                        Do not start TLS client listeners.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-dtls                                        Do not start DTLS client listeners.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-udp-relay                                        Do not allow UDP relay endpoints, use only TCP relay option.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-tcp-relay                                        Do not allow TCP relay endpoints, use only UDP relay options.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -l, --log-file                <filename>                Option to set the full path name of the log file.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 By default, the turnserver tries to open a log file in
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 /var/log/turnserver/, /var/log, /var/tmp, /tmp and . (current) directories
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 (which open operation succeeds first that file will be used).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 With this option you can set the definite log file name.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The special names are "stdout" and "-" - they will force everything
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 to the stdout; and "syslog" name will force all output to the syslog.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-stdout-log                                Flag to prevent stdout log messages.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 By default, all log messages are going to both stdout and to
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 a log file. With this option everything will be going to the log file only
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 (unless the log file itself is stdout).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --syslog                                        Output all log information into the system log (syslog), do not use the file output.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --syslog-facility             <value>          Set syslog facility for syslog messages. Default is ''.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --simple-log                                        This flag means that no log file rollover will be used, and the log file
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 name will be constructed as-is, without PID and date appendage.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This option can be used, for example, together with the logrotate tool.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --new-log-timestamp                                Enable full ISO-8601 timestamp in all logs.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --new-log-timestamp-format            <format>        Set timestamp format (in strftime(1) format). Depends on --new-log-timestamp to be enabled.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --log-binding                                        Log STUN binding request. It is now disabled by default to avoid DoS attacks.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --stale-nonce[=<value>]                        Use extra security with nonce value having limited lifetime (default 600 secs).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --max-allocate-lifetime        <value>                Set the maximum value for the allocation lifetime. Default to 3600 secs.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --channel-lifetime                <value>                Set the lifetime for channel binding, default to 600 secs.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This value MUST not be changed for production purposes.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --permission-lifetime                <value>                Set the value for the lifetime of the permission. Default to 300 secs.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This MUST not be changed for production purposes.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -S, --stun-only                                Option to set standalone STUN operation only, all TURN requests will be ignored.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:      --no-stun                                        Option to suppress STUN functionality, only TURN requests will be processed.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --alternate-server                <ip:port>        Set the TURN server to redirect the allocate requests (UDP and TCP services).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Multiple alternate-server options can be set for load balancing purposes.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 See the docs for more information.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --tls-alternate-server        <ip:port>                Set the TURN server to redirect the allocate requests (DTLS and TLS services).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Multiple alternate-server options can be set for load balancing purposes.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 See the docs for more information.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -C, --rest-api-separator        <SYMBOL>        This is the timestamp/username separator symbol (character) in TURN REST API.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The default value is ':'.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --max-allocate-timeout=<seconds>                Max time, in seconds, allowed for full allocation establishment. Default is 60.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --allowed-peer-ip=<ip[-ip]>                         Specifies an ip or range of ips that are explicitly allowed to connect to the
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 turn server. Multiple allowed-peer-ip can be set.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --denied-peer-ip=<ip[-ip]>                         Specifies an ip or range of ips that are not allowed to connect to the turn server.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Multiple denied-peer-ip can be set.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --pidfile <"pid-file-name">                        File name to store the pid of the process.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Default is /var/run/turnserver.pid (if superuser account is used) or
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 /var/tmp/turnserver.pid .
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --acme-redirect <URL>                                Redirect ACME, i.e. HTTP GET requests matching '^/.well-known/acme-challenge/(.*)' to '<URL>$1'.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Default is '', i.e. no special handling for such requests.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --secure-stun                                        Require authentication of the STUN Binding request.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 By default, the clients are allowed anonymous access to the STUN Binding functionality.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --proc-user <user-name>                        User name to run the turnserver process.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 After the initialization, the turnserver process
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 will make an attempt to change the current user ID to that user.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --proc-group <group-name>                        Group name to run the turnserver process.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 After the initialization, the turnserver process
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 will make an attempt to change the current group ID to that group.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --mobility                                        Mobility with ICE (MICE) specs support.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -K, --keep-address-family                        Deprecated in favor of --allocation-default-address-family!!
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 TURN server allocates address family according TURN
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Client <=> Server communication address family.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 !! It breaks RFC6156 section-4.2 (violates default IPv4) !!
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -A --allocation-default-address-family=<ipv4|ipv6|keep>                 Default is IPv4
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 TURN server allocates address family according TURN client requested address family.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 If address family is not requested explicitly by client, then it falls back to this default.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The standard RFC explicitly define actually that this default must be IPv4,
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                        so use other option values with care!
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-cli                                        Turn OFF the CLI support. By default it is always ON.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --cli-ip=<IP>                                        Local system IP address to be used for CLI server endpoint. Default value
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 is 127.0.0.1.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --cli-port=<port>                                CLI server port. Default is 5766.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --cli-password=<password>                        CLI access password. Default is empty (no password).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 For the security reasons, it is recommended to use the encrypted
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 for of the password (see the -P command in the turnadmin utility).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 The dollar signs in the encrypted form must be escaped.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --web-admin                                        Enable Turn Web-admin support. By default it is disabled.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --web-admin-ip=<IP>                                Local system IP address to be used for Web-admin server endpoint. Default value
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 is 127.0.0.1.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --web-admin-port=<port>                        Web-admin server port. Default is 8080.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --web-admin-listen-on-workers                        Enable for web-admin server to listens on STUN/TURN workers STUN/TURN ports.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 By default it is disabled for security reasons!
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 (This behavior used to be the default behavior, and was enabled by default.)
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --server-relay                                        Server relay. NON-STANDARD AND DANGEROUS OPTION. Only for those applications
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 when we want to run server applications on the relay endpoints.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This option eliminates the IP permissions check on the packets
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 incoming to the relay endpoints.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --cli-max-output-sessions                        Maximum number of output sessions in ps CLI command.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This value can be changed on-the-fly in CLI. The default value is 256.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --ne=[1|2|3]                                        Set network engine type for the process (for internal purposes).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-rfc5780                                        Disable RFC5780 (NAT behavior discovery).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Originally, if there are more than one listener address from the same
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 address family, then by default the NAT behavior discovery feature enabled.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 This option disables this original behavior, because the NAT behavior discovery
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 adds attributes to response, and this increase the possibility of an amplification attack.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 Strongly encouraged to use this option to decrease gain factor in STUN binding responses.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --no-stun-backward-compatibility                Disable handling old STUN Binding requests and disable MAPPED-ADDRESS attribute
Aug 12 19:51:14 meet.civitas.local turnserver[955]:                                                 in binding response (use only the XOR-MAPPED-ADDRESS).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --response-origin-only-with-rfc5780                Only send RESPONSE-ORIGIN attribute in binding response if RFC5780 is enabled.
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  --version                                        Print version (and exit).
Aug 12 19:51:14 meet.civitas.local turnserver[955]:  -h                                                Help
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : WARNING: Cannot find config file: /etc/turnserver.conf. Default and command-line settings will be used.
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : log file opened: /var/log/turnserver/turn_955_2026-08-12.log
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : WARNING: Cannot find config file: /etc/turnserver.conf. Default and command-line settings will be used.
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : WARNING: Cannot find config file: /etc/turnserver.conf. Default and command-line settings will be used.
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: :
Aug 12 19:51:14 meet.civitas.local turnserver[955]: RFC 3489/5389/5766/5780/6062/6156 STUN/TURN Server
Aug 12 19:51:14 meet.civitas.local turnserver[955]: Version Coturn-4.6.1 'Gorst'
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: :
Aug 12 19:51:14 meet.civitas.local turnserver[955]: Max number of open files/sockets allowed for this process: 524288
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: :
Aug 12 19:51:14 meet.civitas.local turnserver[955]: Due to the open files/sockets limitation,
Aug 12 19:51:14 meet.civitas.local turnserver[955]: max supported number of TURN Sessions possible is: 262000 (approximately)
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: :
Aug 12 19:51:14 meet.civitas.local turnserver[955]: ==== Show him the instruments, Practical Frost: ====
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : TLS supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : DTLS supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : DTLS 1.2 supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : TURN/STUN ALPN supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Third-party authorization (oAuth) supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : GCM (AEAD) supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : OpenSSL compile-time version: OpenSSL 3.2.2-dev  (0x30200020)
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: :
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : SQLite supported, default database location is /var/lib/turn/turndb
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Redis supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : PostgreSQL supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : MySQL supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : MongoDB is not supported
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: :
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Default Net Engine version: 3 (UDP thread per CPU core)
Aug 12 19:51:14 meet.civitas.local turnserver[955]: =====================================================
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Domain name:
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Default realm:
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : ERROR:
Aug 12 19:51:14 meet.civitas.local turnserver[955]: CONFIG ERROR: Empty cli-password, and so telnet cli interface is disabled! Please set a non empty cli-password!
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : WARNING: cannot find certificate file: turn_server_cert.pem (1)
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : WARNING: cannot start TLS and DTLS listeners because certificate file is not set properly
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : WARNING: cannot find private key file: turn_server_pkey.pem (1)
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : WARNING: cannot start TLS and DTLS listeners because private key file is not set properly
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : NO EXPLICIT LISTENER ADDRESS(ES) ARE CONFIGURED
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : ===========Discovering listener addresses: =========
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Listener address to use: 127.0.0.1
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : Listener address to use: ::1
Aug 12 19:51:14 meet.civitas.local turnserver[955]: 0: : ERROR: main: Cannot configure any meaningful IP listener address
Aug 12 19:51:15 meet.civitas.local systemd[1]: coturn.service: Scheduled restart job, restart counter is at 5.
Aug 12 19:51:15 meet.civitas.local systemd[1]: coturn.service: Start request repeated too quickly.
Aug 12 19:51:15 meet.civitas.local systemd[1]: coturn.service: Failed with result 'exit-code'.
Aug 12 19:51:15 meet.civitas.local systemd[1]: Failed to start coturn.service - coTURN STUN/TURN Server.


```text
$ journalctl -u nginx --no-pager -n 300 2>/dev/null || true
```
Mar 24 15:47:09 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 24 15:47:09 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 24 15:47:09 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
-- Boot 568cd1ca264f48ec9180909763535afe --
Mar 24 15:48:30 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 24 15:48:30 meet.civitas.local nginx[1810]: 2026/03/24 15:48:30 [warn] 1810#1810: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 24 15:48:30 meet.civitas.local nginx[1810]: 2026/03/24 15:48:30 [warn] 1810#1810: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 24 15:48:30 meet.civitas.local nginx[1810]: 2026/03/24 15:48:30 [warn] 1810#1810: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 24 15:48:30 meet.civitas.local nginx[1817]: 2026/03/24 15:48:30 [warn] 1817#1817: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 24 15:48:30 meet.civitas.local nginx[1817]: 2026/03/24 15:48:30 [warn] 1817#1817: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 24 15:48:30 meet.civitas.local nginx[1817]: 2026/03/24 15:48:30 [warn] 1817#1817: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 24 15:48:30 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 24 16:11:51 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 24 16:11:51 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 24 16:11:51 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
-- Boot 08b67ad3b83f49c5839534ae66de410b --
Mar 24 16:14:11 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 24 16:14:11 meet.civitas.local nginx[1104]: 2026/03/24 16:14:11 [warn] 1104#1104: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 24 16:14:11 meet.civitas.local nginx[1104]: 2026/03/24 16:14:11 [warn] 1104#1104: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 24 16:14:11 meet.civitas.local nginx[1104]: 2026/03/24 16:14:11 [warn] 1104#1104: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 24 16:14:11 meet.civitas.local nginx[1112]: 2026/03/24 16:14:11 [warn] 1112#1112: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 24 16:14:11 meet.civitas.local nginx[1112]: 2026/03/24 16:14:11 [warn] 1112#1112: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 24 16:14:11 meet.civitas.local nginx[1112]: 2026/03/24 16:14:11 [warn] 1112#1112: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 24 16:14:11 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot 6794de94ea1b429592d3c06baf21dadf --
Mar 24 19:42:51 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 24 19:42:51 meet.civitas.local nginx[1024]: 2026/03/24 19:42:51 [warn] 1024#1024: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 24 19:42:51 meet.civitas.local nginx[1024]: 2026/03/24 19:42:51 [warn] 1024#1024: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 24 19:42:51 meet.civitas.local nginx[1024]: 2026/03/24 19:42:51 [warn] 1024#1024: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 24 19:42:52 meet.civitas.local nginx[1034]: 2026/03/24 19:42:52 [warn] 1034#1034: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 24 19:42:52 meet.civitas.local nginx[1034]: 2026/03/24 19:42:52 [warn] 1034#1034: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 24 19:42:52 meet.civitas.local nginx[1034]: 2026/03/24 19:42:52 [warn] 1034#1034: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 24 19:42:52 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot 57a5210cbd994cc09b58cb1121fe5762 --
Mar 25 15:13:25 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 25 15:13:25 meet.civitas.local nginx[1025]: 2026/03/25 15:13:25 [warn] 1025#1025: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 25 15:13:25 meet.civitas.local nginx[1025]: 2026/03/25 15:13:25 [warn] 1025#1025: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 25 15:13:25 meet.civitas.local nginx[1025]: 2026/03/25 15:13:25 [warn] 1025#1025: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 25 15:13:25 meet.civitas.local nginx[1029]: 2026/03/25 15:13:25 [warn] 1029#1029: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 25 15:13:25 meet.civitas.local nginx[1029]: 2026/03/25 15:13:25 [warn] 1029#1029: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 25 15:13:25 meet.civitas.local nginx[1029]: 2026/03/25 15:13:25 [warn] 1029#1029: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 25 15:13:25 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 25 20:54:13 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 25 20:54:13 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 25 20:54:13 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Mar 25 20:54:13 meet.civitas.local systemd[1]: nginx.service: Consumed 2.696s CPU time, 18.9M memory peak.
-- Boot 301e6bd333fb41548b9fa74557909cd8 --
Mar 29 20:32:44 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 29 20:32:44 meet.civitas.local nginx[1421]: 2026/03/29 20:32:44 [warn] 1421#1421: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 20:32:44 meet.civitas.local nginx[1421]: 2026/03/29 20:32:44 [warn] 1421#1421: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 20:32:44 meet.civitas.local nginx[1421]: 2026/03/29 20:32:44 [warn] 1421#1421: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 20:32:44 meet.civitas.local nginx[1432]: 2026/03/29 20:32:44 [warn] 1432#1432: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 20:32:44 meet.civitas.local nginx[1432]: 2026/03/29 20:32:44 [warn] 1432#1432: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 20:32:44 meet.civitas.local nginx[1432]: 2026/03/29 20:32:44 [warn] 1432#1432: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 20:32:44 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 29 21:18:01 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 29 21:18:02 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 29 21:18:02 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Mar 29 21:18:02 meet.civitas.local systemd[1]: nginx.service: Consumed 2.513s CPU time, 36.7M memory peak.
-- Boot e39a62a52ead4a1d8fa5eaecb27705df --
Mar 29 21:19:10 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 29 21:19:10 meet.civitas.local nginx[989]: 2026/03/29 21:19:10 [warn] 989#989: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 21:19:10 meet.civitas.local nginx[989]: 2026/03/29 21:19:10 [warn] 989#989: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 21:19:10 meet.civitas.local nginx[989]: 2026/03/29 21:19:10 [warn] 989#989: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 21:19:10 meet.civitas.local nginx[1017]: 2026/03/29 21:19:10 [warn] 1017#1017: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 21:19:10 meet.civitas.local nginx[1017]: 2026/03/29 21:19:10 [warn] 1017#1017: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 21:19:10 meet.civitas.local nginx[1017]: 2026/03/29 21:19:10 [warn] 1017#1017: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 21:19:10 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 29 21:23:18 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 29 21:23:18 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 29 21:23:18 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
-- Boot 8a03c0f89e2c45eb80df3e5142baca53 --
Mar 29 21:23:38 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 29 21:23:38 meet.civitas.local nginx[992]: 2026/03/29 21:23:38 [warn] 992#992: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 21:23:38 meet.civitas.local nginx[992]: 2026/03/29 21:23:38 [warn] 992#992: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 21:23:38 meet.civitas.local nginx[992]: 2026/03/29 21:23:38 [warn] 992#992: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 21:23:38 meet.civitas.local nginx[1027]: 2026/03/29 21:23:38 [warn] 1027#1027: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 21:23:38 meet.civitas.local nginx[1027]: 2026/03/29 21:23:38 [warn] 1027#1027: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 21:23:38 meet.civitas.local nginx[1027]: 2026/03/29 21:23:38 [warn] 1027#1027: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 21:23:38 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 29 21:27:09 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 29 21:27:14 meet.civitas.local systemd[1]: nginx.service: Stopping timed out. Terminating.
Mar 29 21:27:14 meet.civitas.local systemd[1]: nginx.service: Failed with result 'timeout'.
Mar 29 21:27:14 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
-- Boot bf5a91c7a1414c8ebcab4db759fa8a3f --
Mar 29 21:28:19 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 29 21:28:19 meet.civitas.local nginx[1761]: 2026/03/29 21:28:19 [warn] 1761#1761: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 21:28:19 meet.civitas.local nginx[1761]: 2026/03/29 21:28:19 [warn] 1761#1761: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 21:28:19 meet.civitas.local nginx[1761]: 2026/03/29 21:28:19 [warn] 1761#1761: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 21:28:19 meet.civitas.local nginx[1779]: 2026/03/29 21:28:19 [warn] 1779#1779: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 21:28:19 meet.civitas.local nginx[1779]: 2026/03/29 21:28:19 [warn] 1779#1779: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 21:28:19 meet.civitas.local nginx[1779]: 2026/03/29 21:28:19 [warn] 1779#1779: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 21:28:19 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 29 21:33:12 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 29 21:33:17 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 29 21:33:17 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Mar 29 21:33:17 meet.civitas.local systemd[1]: nginx.service: Consumed 1.012s CPU time, 17.3M memory peak.
-- Boot 57137ae7f61e48c4a7025e5ce47f91ea --
Mar 29 21:33:51 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 29 21:33:51 meet.civitas.local nginx[989]: 2026/03/29 21:33:51 [warn] 989#989: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 21:33:51 meet.civitas.local nginx[989]: 2026/03/29 21:33:51 [warn] 989#989: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 21:33:51 meet.civitas.local nginx[989]: 2026/03/29 21:33:51 [warn] 989#989: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 21:33:51 meet.civitas.local nginx[1013]: 2026/03/29 21:33:51 [warn] 1013#1013: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 29 21:33:51 meet.civitas.local nginx[1013]: 2026/03/29 21:33:51 [warn] 1013#1013: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 29 21:33:51 meet.civitas.local nginx[1013]: 2026/03/29 21:33:51 [warn] 1013#1013: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 29 21:33:51 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 29 22:14:34 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 29 22:14:35 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 29 22:14:35 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Mar 29 22:14:35 meet.civitas.local systemd[1]: nginx.service: Consumed 5.460s CPU time, 21.5M memory peak.
-- Boot ae946aac51d841d294ce09308edb77fe --
Mar 30 06:44:14 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 30 06:44:14 meet.civitas.local nginx[1046]: 2026/03/30 06:44:14 [warn] 1046#1046: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 30 06:44:14 meet.civitas.local nginx[1046]: 2026/03/30 06:44:14 [warn] 1046#1046: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 30 06:44:14 meet.civitas.local nginx[1046]: 2026/03/30 06:44:14 [warn] 1046#1046: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 30 06:44:14 meet.civitas.local nginx[1080]: 2026/03/30 06:44:14 [warn] 1080#1080: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 30 06:44:14 meet.civitas.local nginx[1080]: 2026/03/30 06:44:14 [warn] 1080#1080: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 30 06:44:14 meet.civitas.local nginx[1080]: 2026/03/30 06:44:14 [warn] 1080#1080: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 30 06:44:14 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot 7c117163ac96474798b75f818b5e53a8 --
Mar 30 07:10:31 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 30 07:10:31 meet.civitas.local nginx[996]: 2026/03/30 07:10:31 [warn] 996#996: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 30 07:10:31 meet.civitas.local nginx[996]: 2026/03/30 07:10:31 [warn] 996#996: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 30 07:10:31 meet.civitas.local nginx[996]: 2026/03/30 07:10:31 [warn] 996#996: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 30 07:10:31 meet.civitas.local nginx[1018]: 2026/03/30 07:10:31 [warn] 1018#1018: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 30 07:10:31 meet.civitas.local nginx[1018]: 2026/03/30 07:10:31 [warn] 1018#1018: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 30 07:10:31 meet.civitas.local nginx[1018]: 2026/03/30 07:10:31 [warn] 1018#1018: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 30 07:10:31 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 30 07:39:30 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 30 07:39:31 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 30 07:39:31 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
-- Boot 7646a62e86944797826df153d2564574 --
Jun 07 18:11:36 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jun 07 18:11:36 meet.civitas.local nginx[1080]: 2026/06/07 18:11:36 [warn] 1080#1080: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 07 18:11:36 meet.civitas.local nginx[1080]: 2026/06/07 18:11:36 [warn] 1080#1080: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 07 18:11:36 meet.civitas.local nginx[1080]: 2026/06/07 18:11:36 [warn] 1080#1080: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 07 18:11:36 meet.civitas.local nginx[1119]: 2026/06/07 18:11:36 [warn] 1119#1119: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 07 18:11:36 meet.civitas.local nginx[1119]: 2026/06/07 18:11:36 [warn] 1119#1119: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 07 18:11:36 meet.civitas.local nginx[1119]: 2026/06/07 18:11:36 [warn] 1119#1119: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 07 18:11:36 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot 19ac8219f53647f8be0b730507a4038a --
Jun 07 18:14:49 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jun 07 18:14:49 meet.civitas.local nginx[999]: 2026/06/07 18:14:49 [warn] 999#999: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 07 18:14:49 meet.civitas.local nginx[999]: 2026/06/07 18:14:49 [warn] 999#999: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 07 18:14:49 meet.civitas.local nginx[999]: 2026/06/07 18:14:49 [warn] 999#999: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 07 18:14:49 meet.civitas.local nginx[1022]: 2026/06/07 18:14:49 [warn] 1022#1022: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 07 18:14:49 meet.civitas.local nginx[1022]: 2026/06/07 18:14:49 [warn] 1022#1022: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 07 18:14:49 meet.civitas.local nginx[1022]: 2026/06/07 18:14:49 [warn] 1022#1022: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 07 18:14:49 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Jun 08 05:07:20 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Jun 08 05:07:22 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Jun 08 05:07:22 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Jun 08 05:07:22 meet.civitas.local systemd[1]: nginx.service: Consumed 2.216s CPU time, 18.3M memory peak.
-- Boot 831c701f6afe41d797ed8e696f31da03 --
Jun 08 05:09:55 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jun 08 05:09:55 meet.civitas.local nginx[2137]: 2026/06/08 05:09:55 [warn] 2137#2137: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 08 05:09:55 meet.civitas.local nginx[2137]: 2026/06/08 05:09:55 [warn] 2137#2137: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 08 05:09:55 meet.civitas.local nginx[2137]: 2026/06/08 05:09:55 [warn] 2137#2137: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 08 05:09:55 meet.civitas.local nginx[2165]: 2026/06/08 05:09:55 [warn] 2165#2165: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 08 05:09:55 meet.civitas.local nginx[2165]: 2026/06/08 05:09:55 [warn] 2165#2165: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 08 05:09:55 meet.civitas.local nginx[2165]: 2026/06/08 05:09:55 [warn] 2165#2165: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 08 05:09:55 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Jun 08 05:44:02 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Jun 08 05:44:02 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Jun 08 05:44:02 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Jun 08 05:44:02 meet.civitas.local systemd[1]: nginx.service: Consumed 1.829s CPU time, 18.5M memory peak.
-- Boot 66f55ceb4625476e959db6db6759fd56 --
Jun 08 05:54:04 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jun 08 05:54:04 meet.civitas.local nginx[1098]: 2026/06/08 05:54:04 [warn] 1098#1098: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 08 05:54:04 meet.civitas.local nginx[1098]: 2026/06/08 05:54:04 [warn] 1098#1098: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 08 05:54:04 meet.civitas.local nginx[1098]: 2026/06/08 05:54:04 [warn] 1098#1098: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 08 05:54:04 meet.civitas.local nginx[1118]: 2026/06/08 05:54:04 [warn] 1118#1118: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 08 05:54:04 meet.civitas.local nginx[1118]: 2026/06/08 05:54:04 [warn] 1118#1118: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 08 05:54:04 meet.civitas.local nginx[1118]: 2026/06/08 05:54:04 [warn] 1118#1118: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 08 05:54:04 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Jun 08 06:11:21 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Jun 08 06:11:21 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Jun 08 06:11:21 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Jun 08 06:11:21 meet.civitas.local systemd[1]: nginx.service: Consumed 1.341s CPU time, 37.1M memory peak.
-- Boot bd2833f114004427a0aeb5378dc68895 --
Jun 08 06:11:39 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jun 08 06:11:40 meet.civitas.local nginx[997]: 2026/06/08 06:11:40 [warn] 997#997: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 08 06:11:40 meet.civitas.local nginx[997]: 2026/06/08 06:11:40 [warn] 997#997: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 08 06:11:40 meet.civitas.local nginx[997]: 2026/06/08 06:11:40 [warn] 997#997: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 08 06:11:40 meet.civitas.local nginx[1020]: 2026/06/08 06:11:40 [warn] 1020#1020: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jun 08 06:11:40 meet.civitas.local nginx[1020]: 2026/06/08 06:11:40 [warn] 1020#1020: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jun 08 06:11:40 meet.civitas.local nginx[1020]: 2026/06/08 06:11:40 [warn] 1020#1020: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jun 08 06:11:40 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Jun 08 06:55:00 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Jun 08 06:55:01 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Jun 08 06:55:01 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Jun 08 06:55:01 meet.civitas.local systemd[1]: nginx.service: Consumed 1.318s CPU time, 19.1M memory peak.
-- Boot 30e0bdf29e0d4c35a10a8ce8ff8d05e2 --
Jul 26 19:47:50 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jul 26 19:47:50 meet.civitas.local nginx[2165]: 2026/07/26 19:47:50 [warn] 2165#2165: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 26 19:47:50 meet.civitas.local nginx[2165]: 2026/07/26 19:47:50 [warn] 2165#2165: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 26 19:47:50 meet.civitas.local nginx[2165]: 2026/07/26 19:47:50 [warn] 2165#2165: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 26 19:47:50 meet.civitas.local nginx[2184]: 2026/07/26 19:47:50 [warn] 2184#2184: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 26 19:47:50 meet.civitas.local nginx[2184]: 2026/07/26 19:47:50 [warn] 2184#2184: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 26 19:47:50 meet.civitas.local nginx[2184]: 2026/07/26 19:47:50 [warn] 2184#2184: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 26 19:47:50 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Jul 26 20:05:56 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Jul 26 20:05:56 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Jul 26 20:05:56 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Jul 26 20:05:56 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jul 26 20:05:56 meet.civitas.local nginx[15225]: 2026/07/26 20:05:56 [warn] 15225#15225: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 26 20:05:56 meet.civitas.local nginx[15225]: 2026/07/26 20:05:56 [warn] 15225#15225: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 26 20:05:56 meet.civitas.local nginx[15225]: 2026/07/26 20:05:56 [warn] 15225#15225: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 26 20:05:56 meet.civitas.local nginx[15227]: 2026/07/26 20:05:56 [warn] 15227#15227: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 26 20:05:56 meet.civitas.local nginx[15227]: 2026/07/26 20:05:56 [warn] 15227#15227: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 26 20:05:56 meet.civitas.local nginx[15227]: 2026/07/26 20:05:56 [warn] 15227#15227: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 26 20:05:56 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Jul 26 21:22:12 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Jul 26 21:22:17 meet.civitas.local systemd[1]: nginx.service: Stopping timed out. Terminating.
Jul 26 21:22:17 meet.civitas.local systemd[1]: nginx.service: Failed with result 'timeout'.
Jul 26 21:22:17 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Jul 26 21:22:17 meet.civitas.local systemd[1]: nginx.service: Consumed 1.886s CPU time, 15.2M memory peak.
-- Boot ddc43200d1934264a634da29e620643b --
Jul 27 11:23:28 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jul 27 11:23:29 meet.civitas.local nginx[1059]: 2026/07/27 11:23:29 [warn] 1059#1059: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 27 11:23:29 meet.civitas.local nginx[1059]: 2026/07/27 11:23:29 [warn] 1059#1059: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 27 11:23:29 meet.civitas.local nginx[1059]: 2026/07/27 11:23:29 [warn] 1059#1059: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 27 11:23:29 meet.civitas.local nginx[1088]: 2026/07/27 11:23:29 [warn] 1088#1088: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 27 11:23:29 meet.civitas.local nginx[1088]: 2026/07/27 11:23:29 [warn] 1088#1088: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 27 11:23:29 meet.civitas.local nginx[1088]: 2026/07/27 11:23:29 [warn] 1088#1088: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 27 11:23:29 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot a5e61fb0f1594bc8a5d623704c530484 --
Jul 28 04:02:14 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jul 28 04:02:14 meet.civitas.local nginx[1125]: 2026/07/28 04:02:14 [warn] 1125#1125: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 28 04:02:14 meet.civitas.local nginx[1125]: 2026/07/28 04:02:14 [warn] 1125#1125: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 28 04:02:14 meet.civitas.local nginx[1125]: 2026/07/28 04:02:14 [warn] 1125#1125: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 28 04:02:14 meet.civitas.local nginx[1151]: 2026/07/28 04:02:14 [warn] 1151#1151: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 28 04:02:14 meet.civitas.local nginx[1151]: 2026/07/28 04:02:14 [warn] 1151#1151: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 28 04:02:14 meet.civitas.local nginx[1151]: 2026/07/28 04:02:14 [warn] 1151#1151: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 28 04:02:14 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot d703551f0f2b4263a30c0caa6ee9da59 --
Jul 28 05:12:56 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jul 28 05:12:56 meet.civitas.local nginx[2216]: 2026/07/28 05:12:56 [warn] 2216#2216: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 28 05:12:56 meet.civitas.local nginx[2216]: 2026/07/28 05:12:56 [warn] 2216#2216: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 28 05:12:56 meet.civitas.local nginx[2216]: 2026/07/28 05:12:56 [warn] 2216#2216: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 28 05:12:56 meet.civitas.local nginx[2226]: 2026/07/28 05:12:56 [warn] 2226#2226: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 28 05:12:56 meet.civitas.local nginx[2226]: 2026/07/28 05:12:56 [warn] 2226#2226: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 28 05:12:56 meet.civitas.local nginx[2226]: 2026/07/28 05:12:56 [warn] 2226#2226: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 28 05:12:56 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Jul 28 14:29:38 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Jul 28 14:29:39 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Jul 28 14:29:39 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
-- Boot 9b460f1d92544d3391903b33dfc6fc60 --
Jul 28 14:30:57 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jul 28 14:30:57 meet.civitas.local nginx[2164]: 2026/07/28 14:30:57 [warn] 2164#2164: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 28 14:30:57 meet.civitas.local nginx[2164]: 2026/07/28 14:30:57 [warn] 2164#2164: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 28 14:30:57 meet.civitas.local nginx[2164]: 2026/07/28 14:30:57 [warn] 2164#2164: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 28 14:30:58 meet.civitas.local nginx[2176]: 2026/07/28 14:30:58 [warn] 2176#2176: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 28 14:30:58 meet.civitas.local nginx[2176]: 2026/07/28 14:30:58 [warn] 2176#2176: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 28 14:30:58 meet.civitas.local nginx[2176]: 2026/07/28 14:30:58 [warn] 2176#2176: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 28 14:30:58 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot 762fb21cee3f48d0af2c2687e37135e5 --
Jul 30 08:24:09 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jul 30 08:24:09 meet.civitas.local nginx[2244]: 2026/07/30 08:24:09 [warn] 2244#2244: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 30 08:24:09 meet.civitas.local nginx[2244]: 2026/07/30 08:24:09 [warn] 2244#2244: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 30 08:24:09 meet.civitas.local nginx[2244]: 2026/07/30 08:24:09 [warn] 2244#2244: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 30 08:24:09 meet.civitas.local nginx[2266]: 2026/07/30 08:24:09 [warn] 2266#2266: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 30 08:24:09 meet.civitas.local nginx[2266]: 2026/07/30 08:24:09 [warn] 2266#2266: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 30 08:24:09 meet.civitas.local nginx[2266]: 2026/07/30 08:24:09 [warn] 2266#2266: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 30 08:24:09 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot ccc64a87080542548178ba881d657c44 --
Jul 30 14:47:23 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Jul 30 14:47:23 meet.civitas.local nginx[1116]: 2026/07/30 14:47:23 [warn] 1116#1116: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 30 14:47:23 meet.civitas.local nginx[1116]: 2026/07/30 14:47:23 [warn] 1116#1116: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 30 14:47:23 meet.civitas.local nginx[1116]: 2026/07/30 14:47:23 [warn] 1116#1116: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 30 14:47:23 meet.civitas.local nginx[1143]: 2026/07/30 14:47:23 [warn] 1143#1143: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Jul 30 14:47:23 meet.civitas.local nginx[1143]: 2026/07/30 14:47:23 [warn] 1143#1143: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Jul 30 14:47:23 meet.civitas.local nginx[1143]: 2026/07/30 14:47:23 [warn] 1143#1143: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Jul 30 14:47:23 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot 90f8ed02531e486e82360bc834a91d21 --
Aug 03 10:25:31 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Aug 03 10:25:31 meet.civitas.local nginx[1166]: 2026/08/03 10:25:31 [warn] 1166#1166: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 03 10:25:31 meet.civitas.local nginx[1166]: 2026/08/03 10:25:31 [warn] 1166#1166: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 03 10:25:31 meet.civitas.local nginx[1166]: 2026/08/03 10:25:31 [warn] 1166#1166: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 03 10:25:31 meet.civitas.local nginx[1187]: 2026/08/03 10:25:31 [warn] 1187#1187: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 03 10:25:31 meet.civitas.local nginx[1187]: 2026/08/03 10:25:31 [warn] 1187#1187: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 03 10:25:31 meet.civitas.local nginx[1187]: 2026/08/03 10:25:31 [warn] 1187#1187: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 03 10:25:31 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot ea55d1d83e93437491adcc1394ac26f6 --
Aug 07 05:25:31 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Aug 07 05:25:31 meet.civitas.local nginx[1160]: 2026/08/07 05:25:31 [warn] 1160#1160: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 07 05:25:31 meet.civitas.local nginx[1160]: 2026/08/07 05:25:31 [warn] 1160#1160: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 07 05:25:31 meet.civitas.local nginx[1160]: 2026/08/07 05:25:31 [warn] 1160#1160: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 07 05:25:31 meet.civitas.local nginx[1189]: 2026/08/07 05:25:31 [warn] 1189#1189: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 07 05:25:31 meet.civitas.local nginx[1189]: 2026/08/07 05:25:31 [warn] 1189#1189: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 07 05:25:31 meet.civitas.local nginx[1189]: 2026/08/07 05:25:31 [warn] 1189#1189: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 07 05:25:31 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot ecc7bebb588040ce87f8c1989b6b6e2b --
Aug 09 14:40:04 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Aug 09 14:40:04 meet.civitas.local nginx[2178]: 2026/08/09 14:40:04 [warn] 2178#2178: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 09 14:40:04 meet.civitas.local nginx[2178]: 2026/08/09 14:40:04 [warn] 2178#2178: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 09 14:40:04 meet.civitas.local nginx[2178]: 2026/08/09 14:40:04 [warn] 2178#2178: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 09 14:40:04 meet.civitas.local nginx[2190]: 2026/08/09 14:40:04 [warn] 2190#2190: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 09 14:40:04 meet.civitas.local nginx[2190]: 2026/08/09 14:40:04 [warn] 2190#2190: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 09 14:40:04 meet.civitas.local nginx[2190]: 2026/08/09 14:40:04 [warn] 2190#2190: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 09 14:40:04 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot b032f81b9b694164bab7ff2db793668a --
Aug 09 15:09:02 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Aug 09 15:09:02 meet.civitas.local nginx[996]: 2026/08/09 15:09:02 [warn] 996#996: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 09 15:09:02 meet.civitas.local nginx[996]: 2026/08/09 15:09:02 [warn] 996#996: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 09 15:09:02 meet.civitas.local nginx[996]: 2026/08/09 15:09:02 [warn] 996#996: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 09 15:09:02 meet.civitas.local nginx[1014]: 2026/08/09 15:09:02 [warn] 1014#1014: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 09 15:09:02 meet.civitas.local nginx[1014]: 2026/08/09 15:09:02 [warn] 1014#1014: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 09 15:09:02 meet.civitas.local nginx[1014]: 2026/08/09 15:09:02 [warn] 1014#1014: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 09 15:09:02 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot 138ff78abc0a41c4a9100fe18f4bfa2a --
Aug 11 06:24:49 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Aug 11 06:24:49 meet.civitas.local nginx[1128]: 2026/08/11 06:24:49 [warn] 1128#1128: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 11 06:24:49 meet.civitas.local nginx[1128]: 2026/08/11 06:24:49 [warn] 1128#1128: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 11 06:24:49 meet.civitas.local nginx[1128]: 2026/08/11 06:24:49 [warn] 1128#1128: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 11 06:24:49 meet.civitas.local nginx[1155]: 2026/08/11 06:24:49 [warn] 1155#1155: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 11 06:24:49 meet.civitas.local nginx[1155]: 2026/08/11 06:24:49 [warn] 1155#1155: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 11 06:24:49 meet.civitas.local nginx[1155]: 2026/08/11 06:24:49 [warn] 1155#1155: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 11 06:24:49 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Aug 11 07:15:05 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Aug 11 07:15:05 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Aug 11 07:15:05 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Aug 11 07:46:48 meet.civitas.local systemd[1]: nginx.service: Unit cannot be reloaded because it is inactive.
-- Boot df45595302474309b94a701ef0965efb --
Aug 11 07:53:12 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Aug 11 07:53:13 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Aug 11 08:01:36 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Aug 11 08:01:36 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Aug 11 08:01:36 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.



---

# 17. UTILISATEURS ET GROUPES

**Date :** 2026-08-12 20:37:40 EDT


## Utilisateurs Jitsi


```text
$ getent passwd | grep -Ei "jitsi|prosody|jicofo|turn" || true
```
turnserver:x:112:116:turnserver daemon:/:/bin/false


## Groupes


```text
$ getent group | grep -Ei "jitsi|prosody|jicofo|turn" || true
```
jitsi:x:1001:
turnserver:x:116:


## Home directories


```text
$ for u in jitsi jicofo prosody turnserver; do getent passwd "$u" 2>/dev/null; done
```
turnserver:x:112:116:turnserver daemon:/:/bin/false



---

# 18. JAVA

**Date :** 2026-08-12 20:37:40 EDT


```text
$ java -version 2>&1 || true
```
openjdk version "21.0.12" 2026-07-21
OpenJDK Runtime Environment (build 21.0.12+8-1-deb13u1-Debian)
OpenJDK 64-Bit Server VM (build 21.0.12+8-1-deb13u1-Debian, mixed mode, sharing)


```text
$ update-alternatives --list java 2>/dev/null || true
```
/usr/lib/jvm/java-21-openjdk-amd64/bin/java


```text
$ dpkg -l 2>/dev/null | grep -Ei "openjdk|java" || true
```
ii  ca-certificates-java                                20240118                             all          Common CA certificates (JKS keystore)
ii  java-common                                         0.76                                 all          Base package for Java runtimes
ii  javascript-common                                   12+nmu1                              all          Base support for JavaScript library packages
ii  libduktape207:amd64                                 2.7.0-2+b2                           amd64        embeddable Javascript engine, library
ii  libjavascriptcoregtk-4.1-0:amd64                    2.52.5-1~deb13u1                     amd64        JavaScript engine library from WebKitGTK
ii  libjs-jquery                                        3.6.1+dfsg+~3.5.14-1                 all          JavaScript library for dynamic web applications
ii  libjs-underscore                                    1.13.4~dfsg+~1.11.4-3                all          JavaScript's functional programming helper library
ii  openjdk-17-jre-headless                             17.999                               all          Fake openjdk-17 satisfied by openjdk-21
ii  openjdk-21-jre-headless:amd64                       21.0.12+8-1~deb13u1                  amd64        OpenJDK Java runtime, using Hotspot JIT (headless)



---

# 19. NODE.JS

**Date :** 2026-08-12 20:37:40 EDT


```text
$ node --version 2>/dev/null || true
```


```text
$ npm --version 2>/dev/null || true
```


```text
$ command -v node 2>/dev/null || true
```


```text
$ npm list -g --depth=0 2>/dev/null || true
```



---

# 20. LUA / PROSODY DEPENDENCIES

**Date :** 2026-08-12 20:37:40 EDT


```text
$ lua -v 2>&1 || true
```
bash: line 1: lua: command not found


```text
$ dpkg -l 2>/dev/null | grep -Ei "lua|prosody" || true
```
ii  liblua5.2-0:amd64                                   5.2.4-3+b3                           amd64        Shared library for the Lua interpreter version 5.2
ii  liblua5.4-0:amd64                                   5.4.7-1+b2                           amd64        Shared library for the Lua interpreter version 5.4


```text
$ find /usr/lib /usr/share -type f 2>/dev/null | grep -Ei "/lua/|prosody" | head -1000 || true
```
/usr/lib/x86_64-linux-gnu/vlc/lua/sd/jamendo.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/sd/icecast.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/modules/sandbox.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/modules/simplexml.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/modules/dkjson.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/modules/common.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/vocaroo.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/koreus.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/vimeo.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/dailymotion.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/soundcloud.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/jamendo.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/appletrailers.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/twitch.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/anevia_xml.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/bbc_co_uk.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/cue.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/anevia_streams.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/youtube.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/liveleak.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/rockbox_fm_presets.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/playlist/newgrounds.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/extensions/VLSub.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/meta/art/01_googleimage.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/meta/art/03_lastfm.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/meta/art/00_musicbrainz.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/meta/art/02_frenchtv.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/meta/reader/filename.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/intf/modules/httprequests.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/intf/modules/host.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/intf/cli.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/intf/dummy.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/intf/http.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/intf/telnet.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/intf/luac.luac
/usr/lib/x86_64-linux-gnu/vlc/lua/intf/dumpmeta.luac
/usr/lib/x86_64-linux-gnu/vlc/plugins/lua/liblua_plugin.so
/usr/share/doc/vlc/lua/sd/icecast.lua
/usr/share/doc/vlc/lua/sd/README.txt
/usr/share/doc/vlc/lua/sd/icast.lua.gz
/usr/share/doc/vlc/lua/playlist/README.txt
/usr/share/doc/vlc/lua/playlist/youtube.lua.gz
/usr/share/doc/vlc/lua/playlist/liveleak.lua
/usr/share/doc/vlc/lua/http/requests/README.txt.gz
/usr/share/doc/vlc/lua/extensions/README.txt
/usr/share/doc/vlc/lua/README.txt.gz
/usr/share/doc/vlc/lua/meta/art/README.txt
/usr/share/doc/vlc/lua/meta/art/01_googleimage.lua
/usr/share/doc/vlc/lua/meta/README.txt
/usr/share/doc/vlc/lua/meta/reader/README.txt
/usr/share/doc/vlc/lua/meta/reader/filename.lua
/usr/share/doc/vlc/lua/meta/fetcher/README.txt
/usr/share/doc/vlc/lua/intf/README.txt
/usr/share/doc/vlc/lua/intf/dumpmeta.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_webhook.lua
/usr/share/vlc/lua/http/vlm_export.html
/usr/share/vlc/lua/http/js/common.js
/usr/share/vlc/lua/http/js/controllers.js
/usr/share/vlc/lua/http/js/ui.js
/usr/share/vlc/lua/http/js/jquery.jstree.js
/usr/share/vlc/lua/http/mobile.html
/usr/share/vlc/lua/http/requests/playlist_jstree.xml
/usr/share/vlc/lua/http/requests/status.xml
/usr/share/vlc/lua/http/requests/vlm.xml
/usr/share/vlc/lua/http/requests/vlm_cmd.xml
/usr/share/vlc/lua/http/requests/README.txt
/usr/share/vlc/lua/http/requests/playlist.json
/usr/share/vlc/lua/http/requests/playlist.xml
/usr/share/vlc/lua/http/requests/browse.xml
/usr/share/vlc/lua/http/requests/browse.json
/usr/share/vlc/lua/http/requests/status.json
/usr/share/vlc/lua/http/view.html
/usr/share/vlc/lua/http/index.html
/usr/share/vlc/lua/http/dialogs/create_stream.html
/usr/share/vlc/lua/http/dialogs/offset_window.html
/usr/share/vlc/lua/http/dialogs/error_window.html
/usr/share/vlc/lua/http/dialogs/batch_window.html
/usr/share/vlc/lua/http/dialogs/equalizer_window.html
/usr/share/vlc/lua/http/dialogs/browse_window.html
/usr/share/vlc/lua/http/dialogs/stream_config_window.html
/usr/share/vlc/lua/http/dialogs/stream_window.html
/usr/share/vlc/lua/http/dialogs/mosaic_window.html
/usr/share/vlc/lua/http/mobile_browse.html
/usr/share/vlc/lua/http/favicon.ico
/usr/share/vlc/lua/http/css/mobile.css
/usr/share/vlc/lua/http/css/ui-lightness/jquery-ui-1.8.13.custom.css
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-bg_flat_10_000000_40x100.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-icons_ffd27a_256x240.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-bg_glass_100_fdf5ce_1x400.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-icons_228ef1_256x240.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-bg_diagonals-thick_20_666666_40x40.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-bg_highlight-soft_100_eeeeee_1x100.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-icons_ef8c08_256x240.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-bg_diagonals-thick_18_b81900_40x40.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-bg_glass_100_f6f6f6_1x400.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-bg_highlight-soft_75_ffe45c_1x100.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-icons_ffffff_256x240.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-bg_gloss-wave_35_f6a828_500x100.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-bg_glass_65_ffffff_1x400.png
/usr/share/vlc/lua/http/css/ui-lightness/images/ui-icons_222222_256x240.png
/usr/share/vlc/lua/http/css/main.css
/usr/share/vlc/lua/http/custom.lua
/usr/share/vlc/lua/http/mobile_view.html
/usr/share/vlc/lua/http/images/speaker-32.png
/usr/share/vlc/lua/http/images/Audio-48.png
/usr/share/vlc/lua/http/images/Back-48.png
/usr/share/vlc/lua/http/images/vlc-48.png
/usr/share/vlc/lua/http/images/Video-48.png
/usr/share/vlc/lua/http/images/buttons.png
/usr/share/vlc/lua/http/images/Folder-48.png
/usr/share/vlc/lua/http/images/Other-48.png
/usr/share/vlc/lua/http/images/vlc16x16.png
/usr/share/vlc/lua/http/vlm.html
/usr/share/vlc/lua/http/mobile_equalizer.html



---

# 21. FIREWALL

**Date :** 2026-08-12 20:37:41 EDT


## UFW


```text
$ ufw status verbose 2>/dev/null || true
```
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere                   # SSH
80/tcp                     ALLOW IN    Anywhere                   # HTTP
443/tcp                    ALLOW IN    Anywhere                   # HTTPS
10000/udp                  ALLOW IN    Anywhere                   # JVB media
3478/tcp                   ALLOW IN    Anywhere                   # TURN TCP
3478/udp                   ALLOW IN    Anywhere                   # TURN UDP
5349/tcp                   ALLOW IN    Anywhere                   # TURNS TLS
5349/udp                   ALLOW IN    Anywhere                   # TURNS TLS UDP
9092                       ALLOW IN    192.168.1.0/24             # Kafka
3000                       ALLOW IN    192.168.1.0/24             # Grafana
8080                       ALLOW IN    192.168.1.0/24             # Kafka UI
8090                       ALLOW IN    192.168.1.0/24             # Kafka UI
22/tcp (v6)                ALLOW IN    Anywhere (v6)              # SSH
80/tcp (v6)                ALLOW IN    Anywhere (v6)              # HTTP
443/tcp (v6)               ALLOW IN    Anywhere (v6)              # HTTPS
10000/udp (v6)             ALLOW IN    Anywhere (v6)              # JVB media
3478/tcp (v6)              ALLOW IN    Anywhere (v6)              # TURN TCP
3478/udp (v6)              ALLOW IN    Anywhere (v6)              # TURN UDP
5349/tcp (v6)              ALLOW IN    Anywhere (v6)              # TURNS TLS
5349/udp (v6)              ALLOW IN    Anywhere (v6)              # TURNS TLS UDP



## iptables


```text
$ iptables -S 2>/dev/null || true
```
-P INPUT DROP
-P FORWARD DROP
-P OUTPUT ACCEPT
-N DOCKER
-N DOCKER-BRIDGE
-N DOCKER-CT
-N DOCKER-FORWARD
-N DOCKER-INTERNAL
-N DOCKER-USER
-N ufw-after-forward
-N ufw-after-input
-N ufw-after-logging-forward
-N ufw-after-logging-input
-N ufw-after-logging-output
-N ufw-after-output
-N ufw-before-forward
-N ufw-before-input
-N ufw-before-logging-forward
-N ufw-before-logging-input
-N ufw-before-logging-output
-N ufw-before-output
-N ufw-logging-allow
-N ufw-logging-deny
-N ufw-not-local
-N ufw-reject-forward
-N ufw-reject-input
-N ufw-reject-output
-N ufw-skip-to-policy-forward
-N ufw-skip-to-policy-input
-N ufw-skip-to-policy-output
-N ufw-track-forward
-N ufw-track-input
-N ufw-track-output
-N ufw-user-forward
-N ufw-user-input
-N ufw-user-limit
-N ufw-user-limit-accept
-N ufw-user-logging-forward
-N ufw-user-logging-input
-N ufw-user-logging-output
-N ufw-user-output
-A INPUT -j ufw-before-logging-input
-A INPUT -j ufw-before-input
-A INPUT -j ufw-after-input
-A INPUT -j ufw-after-logging-input
-A INPUT -j ufw-reject-input
-A INPUT -j ufw-track-input
-A FORWARD -j DOCKER-USER
-A FORWARD -j DOCKER-FORWARD
-A FORWARD -j ufw-before-logging-forward
-A FORWARD -j ufw-before-forward
-A FORWARD -j ufw-after-forward
-A FORWARD -j ufw-after-logging-forward
-A FORWARD -j ufw-reject-forward
-A FORWARD -j ufw-track-forward
-A OUTPUT -j ufw-before-logging-output
-A OUTPUT -j ufw-before-output
-A OUTPUT -j ufw-after-output
-A OUTPUT -j ufw-after-logging-output
-A OUTPUT -j ufw-reject-output
-A OUTPUT -j ufw-track-output
-A DOCKER -d 172.20.0.16/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8002 -j ACCEPT
-A DOCKER -d 172.20.0.15/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8100 -j ACCEPT
-A DOCKER -d 172.20.0.14/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8011 -j ACCEPT
-A DOCKER -d 172.20.0.13/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8010 -j ACCEPT
-A DOCKER -d 172.20.0.11/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 3000 -j ACCEPT
-A DOCKER -d 172.20.0.8/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 9090 -j ACCEPT
-A DOCKER -d 172.20.0.7/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 3100 -j ACCEPT
-A DOCKER -d 172.20.0.6/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8090 -j ACCEPT
-A DOCKER -d 172.20.0.5/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 9308 -j ACCEPT
-A DOCKER -d 172.20.0.4/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 9092 -j ACCEPT
-A DOCKER -d 172.19.0.3/32 ! -i br-ef751dcb2c14 -o br-ef751dcb2c14 -p tcp -m tcp --dport 8888 -j ACCEPT
-A DOCKER -d 172.20.0.2/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 443 -j ACCEPT
-A DOCKER -d 172.20.0.2/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 80 -j ACCEPT
-A DOCKER -d 172.19.0.2/32 ! -i br-ef751dcb2c14 -o br-ef751dcb2c14 -p udp -m udp --dport 10000 -j ACCEPT
-A DOCKER -d 172.19.0.2/32 ! -i br-ef751dcb2c14 -o br-ef751dcb2c14 -p tcp -m tcp --dport 8080 -j ACCEPT
-A DOCKER ! -i br-9f19243faf15 -o br-9f19243faf15 -j DROP
-A DOCKER ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -j DROP
-A DOCKER ! -i br-ef751dcb2c14 -o br-ef751dcb2c14 -j DROP
-A DOCKER ! -i docker0 -o docker0 -j DROP
-A DOCKER-BRIDGE -o br-9f19243faf15 -j DOCKER
-A DOCKER-BRIDGE -o br-c8ba5432ed86 -j DOCKER
-A DOCKER-BRIDGE -o br-ef751dcb2c14 -j DOCKER
-A DOCKER-BRIDGE -o docker0 -j DOCKER
-A DOCKER-CT -o br-9f19243faf15 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A DOCKER-CT -o br-c8ba5432ed86 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A DOCKER-CT -o br-ef751dcb2c14 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A DOCKER-CT -o docker0 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A DOCKER-FORWARD -j DOCKER-CT
-A DOCKER-FORWARD -j DOCKER-INTERNAL
-A DOCKER-FORWARD -j DOCKER-BRIDGE
-A DOCKER-FORWARD -i br-9f19243faf15 -j ACCEPT
-A DOCKER-FORWARD -i br-c8ba5432ed86 -j ACCEPT
-A DOCKER-FORWARD -i br-ef751dcb2c14 -j ACCEPT
-A DOCKER-FORWARD -i docker0 -j ACCEPT
-A ufw-after-input -p udp -m udp --dport 137 -j ufw-skip-to-policy-input
-A ufw-after-input -p udp -m udp --dport 138 -j ufw-skip-to-policy-input
-A ufw-after-input -p tcp -m tcp --dport 139 -j ufw-skip-to-policy-input
-A ufw-after-input -p tcp -m tcp --dport 445 -j ufw-skip-to-policy-input
-A ufw-after-input -p udp -m udp --dport 67 -j ufw-skip-to-policy-input
-A ufw-after-input -p udp -m udp --dport 68 -j ufw-skip-to-policy-input
-A ufw-after-input -m addrtype --dst-type BROADCAST -j ufw-skip-to-policy-input
-A ufw-after-logging-forward -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[UFW BLOCK] "
-A ufw-after-logging-input -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[UFW BLOCK] "
-A ufw-before-forward -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A ufw-before-forward -p icmp -m icmp --icmp-type 3 -j ACCEPT
-A ufw-before-forward -p icmp -m icmp --icmp-type 11 -j ACCEPT
-A ufw-before-forward -p icmp -m icmp --icmp-type 12 -j ACCEPT
-A ufw-before-forward -p icmp -m icmp --icmp-type 8 -j ACCEPT
-A ufw-before-forward -j ufw-user-forward
-A ufw-before-input -i lo -j ACCEPT
-A ufw-before-input -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A ufw-before-input -m conntrack --ctstate INVALID -j ufw-logging-deny
-A ufw-before-input -m conntrack --ctstate INVALID -j DROP
-A ufw-before-input -p icmp -m icmp --icmp-type 3 -j ACCEPT
-A ufw-before-input -p icmp -m icmp --icmp-type 11 -j ACCEPT
-A ufw-before-input -p icmp -m icmp --icmp-type 12 -j ACCEPT
-A ufw-before-input -p icmp -m icmp --icmp-type 8 -j ACCEPT
-A ufw-before-input -p udp -m udp --sport 67 --dport 68 -j ACCEPT
-A ufw-before-input -j ufw-not-local
-A ufw-before-input -d 224.0.0.251/32 -p udp -m udp --dport 5353 -j ACCEPT
-A ufw-before-input -d 239.255.255.250/32 -p udp -m udp --dport 1900 -j ACCEPT
-A ufw-before-input -j ufw-user-input
-A ufw-before-output -o lo -j ACCEPT
-A ufw-before-output -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A ufw-before-output -j ufw-user-output
-A ufw-logging-allow -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[UFW ALLOW] "
-A ufw-logging-deny -m conntrack --ctstate INVALID -m limit --limit 3/min --limit-burst 10 -j RETURN
-A ufw-logging-deny -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[UFW BLOCK] "
-A ufw-not-local -m addrtype --dst-type LOCAL -j RETURN
-A ufw-not-local -m addrtype --dst-type MULTICAST -j RETURN
-A ufw-not-local -m addrtype --dst-type BROADCAST -j RETURN
-A ufw-not-local -m limit --limit 3/min --limit-burst 10 -j ufw-logging-deny
-A ufw-not-local -j DROP
-A ufw-skip-to-policy-forward -j DROP
-A ufw-skip-to-policy-input -j DROP
-A ufw-skip-to-policy-output -j ACCEPT
-A ufw-track-output -p tcp -m conntrack --ctstate NEW -j ACCEPT
-A ufw-track-output -p udp -m conntrack --ctstate NEW -j ACCEPT
-A ufw-user-input -p tcp -m tcp --dport 22 -j ACCEPT
-A ufw-user-input -p tcp -m tcp --dport 80 -j ACCEPT
-A ufw-user-input -p tcp -m tcp --dport 443 -j ACCEPT
-A ufw-user-input -p udp -m udp --dport 10000 -j ACCEPT
-A ufw-user-input -p tcp -m tcp --dport 3478 -j ACCEPT
-A ufw-user-input -p udp -m udp --dport 3478 -j ACCEPT
-A ufw-user-input -p tcp -m tcp --dport 5349 -j ACCEPT
-A ufw-user-input -p udp -m udp --dport 5349 -j ACCEPT
-A ufw-user-input -s 192.168.1.0/24 -p tcp -m tcp --dport 9092 -j ACCEPT
-A ufw-user-input -s 192.168.1.0/24 -p udp -m udp --dport 9092 -j ACCEPT
-A ufw-user-input -s 192.168.1.0/24 -p tcp -m tcp --dport 3000 -j ACCEPT
-A ufw-user-input -s 192.168.1.0/24 -p udp -m udp --dport 3000 -j ACCEPT
-A ufw-user-input -s 192.168.1.0/24 -p tcp -m tcp --dport 8080 -j ACCEPT
-A ufw-user-input -s 192.168.1.0/24 -p udp -m udp --dport 8080 -j ACCEPT
-A ufw-user-input -s 192.168.1.0/24 -p tcp -m tcp --dport 8090 -j ACCEPT
-A ufw-user-input -s 192.168.1.0/24 -p udp -m udp --dport 8090 -j ACCEPT
-A ufw-user-limit -m limit --limit 3/min -j LOG --log-prefix "[UFW LIMIT BLOCK] "
-A ufw-user-limit -j REJECT --reject-with icmp-port-unreachable
-A ufw-user-limit-accept -j ACCEPT


## iptables NAT


```text
$ iptables -t nat -S 2>/dev/null || true
```
-P PREROUTING ACCEPT
-P INPUT ACCEPT
-P OUTPUT ACCEPT
-P POSTROUTING ACCEPT
-N DOCKER
-A PREROUTING -m addrtype --dst-type LOCAL -j DOCKER
-A OUTPUT -m addrtype --dst-type LOCAL -j DOCKER
-A POSTROUTING -o docker0 -m addrtype --src-type LOCAL -j MASQUERADE
-A POSTROUTING -s 172.17.0.0/16 ! -o docker0 -j MASQUERADE
-A POSTROUTING -o br-ef751dcb2c14 -m addrtype --src-type LOCAL -j MASQUERADE
-A POSTROUTING -s 172.19.0.0/16 ! -o br-ef751dcb2c14 -j MASQUERADE
-A POSTROUTING -o br-c8ba5432ed86 -m addrtype --src-type LOCAL -j MASQUERADE
-A POSTROUTING -s 172.20.0.0/16 ! -o br-c8ba5432ed86 -j MASQUERADE
-A POSTROUTING -o br-9f19243faf15 -m addrtype --src-type LOCAL -j MASQUERADE
-A POSTROUTING -s 172.18.0.0/16 ! -o br-9f19243faf15 -j MASQUERADE
-A POSTROUTING -s 172.19.0.2/32 -d 172.19.0.2/32 -p tcp -m tcp --dport 8080 -j MASQUERADE
-A POSTROUTING -s 172.19.0.2/32 -d 172.19.0.2/32 -p udp -m udp --dport 10000 -j MASQUERADE
-A POSTROUTING -s 172.20.0.2/32 -d 172.20.0.2/32 -p tcp -m tcp --dport 80 -j MASQUERADE
-A POSTROUTING -s 172.20.0.2/32 -d 172.20.0.2/32 -p tcp -m tcp --dport 443 -j MASQUERADE
-A POSTROUTING -s 172.19.0.3/32 -d 172.19.0.3/32 -p tcp -m tcp --dport 8888 -j MASQUERADE
-A POSTROUTING -s 172.20.0.4/32 -d 172.20.0.4/32 -p tcp -m tcp --dport 9092 -j MASQUERADE
-A POSTROUTING -s 172.20.0.5/32 -d 172.20.0.5/32 -p tcp -m tcp --dport 9308 -j MASQUERADE
-A POSTROUTING -s 172.20.0.6/32 -d 172.20.0.6/32 -p tcp -m tcp --dport 8090 -j MASQUERADE
-A POSTROUTING -s 172.20.0.7/32 -d 172.20.0.7/32 -p tcp -m tcp --dport 3100 -j MASQUERADE
-A POSTROUTING -s 172.20.0.8/32 -d 172.20.0.8/32 -p tcp -m tcp --dport 9090 -j MASQUERADE
-A POSTROUTING -s 172.20.0.11/32 -d 172.20.0.11/32 -p tcp -m tcp --dport 3000 -j MASQUERADE
-A POSTROUTING -s 172.20.0.13/32 -d 172.20.0.13/32 -p tcp -m tcp --dport 8010 -j MASQUERADE
-A POSTROUTING -s 172.20.0.14/32 -d 172.20.0.14/32 -p tcp -m tcp --dport 8011 -j MASQUERADE
-A POSTROUTING -s 172.20.0.15/32 -d 172.20.0.15/32 -p tcp -m tcp --dport 8100 -j MASQUERADE
-A POSTROUTING -s 172.20.0.16/32 -d 172.20.0.16/32 -p tcp -m tcp --dport 8002 -j MASQUERADE
-A DOCKER -d 127.0.0.1/32 -p tcp -m tcp --dport 8080 -j DNAT --to-destination 172.19.0.2:8080
-A DOCKER -p udp -m udp --dport 10000 -j DNAT --to-destination 172.19.0.2:10000
-A DOCKER -p tcp -m tcp --dport 80 -j DNAT --to-destination 172.20.0.2:80
-A DOCKER -p tcp -m tcp --dport 443 -j DNAT --to-destination 172.20.0.2:443
-A DOCKER -d 127.0.0.1/32 -p tcp -m tcp --dport 8888 -j DNAT --to-destination 172.19.0.3:8888
-A DOCKER -p tcp -m tcp --dport 9092 -j DNAT --to-destination 172.20.0.4:9092
-A DOCKER -p tcp -m tcp --dport 9308 -j DNAT --to-destination 172.20.0.5:9308
-A DOCKER -p tcp -m tcp --dport 8090 -j DNAT --to-destination 172.20.0.6:8090
-A DOCKER -p tcp -m tcp --dport 3100 -j DNAT --to-destination 172.20.0.7:3100
-A DOCKER -p tcp -m tcp --dport 9091 -j DNAT --to-destination 172.20.0.8:9090
-A DOCKER -p tcp -m tcp --dport 3000 -j DNAT --to-destination 172.20.0.11:3000
-A DOCKER -p tcp -m tcp --dport 8010 -j DNAT --to-destination 172.20.0.13:8010
-A DOCKER -p tcp -m tcp --dport 8011 -j DNAT --to-destination 172.20.0.14:8011
-A DOCKER -p tcp -m tcp --dport 8100 -j DNAT --to-destination 172.20.0.15:8100
-A DOCKER -p tcp -m tcp --dport 8002 -j DNAT --to-destination 172.20.0.16:8002


## nftables


```text
$ nft list ruleset 2>/dev/null || true
```
table ip filter {
	chain ufw-before-logging-input {
	}

	chain ufw-before-logging-output {
	}

	chain ufw-before-logging-forward {
	}

	chain ufw-before-input {
		iifname "lo" counter packets 45 bytes 6722 accept
		ct state related,established counter packets 6162 bytes 1231583 accept
		ct state invalid counter packets 0 bytes 0 jump ufw-logging-deny
		ct state invalid counter packets 0 bytes 0 drop
		ip protocol icmp icmp type destination-unreachable counter packets 0 bytes 0 accept
		ip protocol icmp icmp type time-exceeded counter packets 0 bytes 0 accept
		ip protocol icmp icmp type parameter-problem counter packets 0 bytes 0 accept
		ip protocol icmp icmp type echo-request counter packets 0 bytes 0 accept
		udp sport 67 udp dport 68 counter packets 0 bytes 0 accept
		counter packets 2506 bytes 225275 jump ufw-not-local
		ip daddr 224.0.0.251 udp dport 5353 counter packets 534 bytes 98645 accept
		ip daddr 239.255.255.250 udp dport 1900 counter packets 0 bytes 0 accept
		counter packets 1972 bytes 126630 jump ufw-user-input
	}

	chain ufw-before-output {
		oifname "lo" counter packets 1594 bytes 223824 accept
		ct state related,established counter packets 5269 bytes 864091 accept
		counter packets 375 bytes 33359 jump ufw-user-output
	}

	chain ufw-before-forward {
		ct state related,established counter packets 0 bytes 0 accept
		ip protocol icmp icmp type destination-unreachable counter packets 0 bytes 0 accept
		ip protocol icmp icmp type time-exceeded counter packets 0 bytes 0 accept
		ip protocol icmp icmp type parameter-problem counter packets 0 bytes 0 accept
		ip protocol icmp icmp type echo-request counter packets 0 bytes 0 accept
		counter packets 0 bytes 0 jump ufw-user-forward
	}

	chain ufw-after-input {
		udp dport 137 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		udp dport 138 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		tcp dport 139 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		tcp dport 445 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		udp dport 67 counter packets 8 bytes 2560 jump ufw-skip-to-policy-input
		udp dport 68 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		fib daddr type broadcast counter packets 2 bytes 4274 jump ufw-skip-to-policy-input
	}

	chain ufw-after-output {
	}

	chain ufw-after-forward {
	}

	chain ufw-after-logging-input {
		limit rate 3/minute burst 10 packets counter packets 145 bytes 8700 log prefix "[UFW BLOCK] "
	}

	chain ufw-after-logging-output {
	}

	chain ufw-after-logging-forward {
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 log prefix "[UFW BLOCK] "
	}

	chain ufw-reject-input {
	}

	chain ufw-reject-output {
	}

	chain ufw-reject-forward {
	}

	chain ufw-track-input {
	}

	chain ufw-track-output {
		ip protocol tcp ct state new counter packets 46 bytes 2760 accept
		ip protocol udp ct state new counter packets 319 bytes 30135 accept
	}

	chain ufw-track-forward {
	}

	chain INPUT {
		type filter hook input priority filter; policy drop;
		counter packets 8713 bytes 1463580 jump ufw-before-logging-input
		counter packets 8713 bytes 1463580 jump ufw-before-input
		counter packets 1971 bytes 126570 jump ufw-after-input
		counter packets 1961 bytes 119736 jump ufw-after-logging-input
		counter packets 1961 bytes 119736 jump ufw-reject-input
		counter packets 1961 bytes 119736 jump ufw-track-input
	}

	chain OUTPUT {
		type filter hook output priority filter; policy accept;
		counter packets 7238 bytes 1121274 jump ufw-before-logging-output
		counter packets 7238 bytes 1121274 jump ufw-before-output
		counter packets 375 bytes 33359 jump ufw-after-output
		counter packets 375 bytes 33359 jump ufw-after-logging-output
		counter packets 375 bytes 33359 jump ufw-reject-output
		counter packets 375 bytes 33359 jump ufw-track-output
	}

	chain FORWARD {
		type filter hook forward priority filter; policy drop;
		counter packets 125162 bytes 32176325 jump DOCKER-USER
		counter packets 125162 bytes 32176325 jump DOCKER-FORWARD
		counter packets 0 bytes 0 jump ufw-before-logging-forward
		counter packets 0 bytes 0 jump ufw-before-forward
		counter packets 0 bytes 0 jump ufw-after-forward
		counter packets 0 bytes 0 jump ufw-after-logging-forward
		counter packets 0 bytes 0 jump ufw-reject-forward
		counter packets 0 bytes 0 jump ufw-track-forward
	}

	chain ufw-logging-deny {
		ct state invalid limit rate 3/minute burst 10 packets counter packets 0 bytes 0 return
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 log prefix "[UFW BLOCK] "
	}

	chain ufw-logging-allow {
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 log prefix "[UFW ALLOW] "
	}

	chain ufw-skip-to-policy-input {
		counter packets 10 bytes 6834 drop
	}

	chain ufw-skip-to-policy-output {
		counter packets 0 bytes 0 accept
	}

	chain ufw-skip-to-policy-forward {
		counter packets 0 bytes 0 drop
	}

	chain ufw-not-local {
		fib daddr type local counter packets 1962 bytes 119796 return
		fib daddr type multicast counter packets 534 bytes 98645 return
		fib daddr type broadcast counter packets 10 bytes 6834 return
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 jump ufw-logging-deny
		counter packets 0 bytes 0 drop
	}

	chain ufw-user-input {
		tcp dport 22 counter packets 1 bytes 60 accept
		tcp dport 80 counter packets 0 bytes 0 accept
		tcp dport 443 counter packets 0 bytes 0 accept
		udp dport 10000 counter packets 0 bytes 0 accept
		tcp dport 3478 counter packets 0 bytes 0 accept
		udp dport 3478 counter packets 0 bytes 0 accept
		tcp dport 5349 counter packets 0 bytes 0 accept
		udp dport 5349 counter packets 0 bytes 0 accept
		ip saddr 192.168.1.0/24 tcp dport 9092 counter packets 0 bytes 0 accept
		ip saddr 192.168.1.0/24 udp dport 9092 counter packets 0 bytes 0 accept
		ip saddr 192.168.1.0/24 tcp dport 3000 counter packets 0 bytes 0 accept
		ip saddr 192.168.1.0/24 udp dport 3000 counter packets 0 bytes 0 accept
		ip saddr 192.168.1.0/24 tcp dport 8080 counter packets 0 bytes 0 accept
		ip saddr 192.168.1.0/24 udp dport 8080 counter packets 0 bytes 0 accept
		ip saddr 192.168.1.0/24 tcp dport 8090 counter packets 0 bytes 0 accept
		ip saddr 192.168.1.0/24 udp dport 8090 counter packets 0 bytes 0 accept
	}

	chain ufw-user-output {
	}

	chain ufw-user-forward {
	}

	chain ufw-user-logging-input {
	}

	chain ufw-user-logging-output {
	}

	chain ufw-user-logging-forward {
	}

	chain ufw-user-limit {
		limit rate 3/minute burst 5 packets counter packets 0 bytes 0 log prefix "[UFW LIMIT BLOCK] "
		counter packets 0 bytes 0 reject
	}

	chain ufw-user-limit-accept {
		counter packets 0 bytes 0 accept
	}

	chain DOCKER {
		ip daddr 172.20.0.16 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8002 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.15 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8100 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.14 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8011 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.13 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8010 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.11 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 3000 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.8 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 9090 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.7 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 3100 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.6 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8090 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.5 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 9308 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.4 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 9092 counter packets 0 bytes 0 accept
		ip daddr 172.19.0.3 iifname != "br-ef751dcb2c14" oifname "br-ef751dcb2c14" tcp dport 8888 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.2 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 443 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.2 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 80 counter packets 0 bytes 0 accept
		ip daddr 172.19.0.2 iifname != "br-ef751dcb2c14" oifname "br-ef751dcb2c14" udp dport 10000 counter packets 0 bytes 0 accept
		ip daddr 172.19.0.2 iifname != "br-ef751dcb2c14" oifname "br-ef751dcb2c14" tcp dport 8080 counter packets 0 bytes 0 accept
		iifname != "br-9f19243faf15" oifname "br-9f19243faf15" counter packets 0 bytes 0 drop
		iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		iifname != "br-ef751dcb2c14" oifname "br-ef751dcb2c14" counter packets 0 bytes 0 drop
		iifname != "docker0" oifname "docker0" counter packets 0 bytes 0 drop
	}

	chain DOCKER-FORWARD {
		counter packets 125162 bytes 32176325 jump DOCKER-CT
		counter packets 648 bytes 52105 jump DOCKER-INTERNAL
		counter packets 648 bytes 52105 jump DOCKER-BRIDGE
		iifname "br-9f19243faf15" counter packets 0 bytes 0 accept
		iifname "br-c8ba5432ed86" counter packets 579 bytes 47917 accept
		iifname "br-ef751dcb2c14" counter packets 69 bytes 4188 accept
		iifname "docker0" counter packets 0 bytes 0 accept
	}

	chain DOCKER-BRIDGE {
		oifname "br-9f19243faf15" counter packets 0 bytes 0 jump DOCKER
		oifname "br-c8ba5432ed86" counter packets 443 bytes 26580 jump DOCKER
		oifname "br-ef751dcb2c14" counter packets 66 bytes 3960 jump DOCKER
		oifname "docker0" counter packets 0 bytes 0 jump DOCKER
	}

	chain DOCKER-CT {
		oifname "br-9f19243faf15" ct state related,established counter packets 0 bytes 0 accept
		oifname "br-c8ba5432ed86" ct state related,established counter packets 110560 bytes 23868021 accept
		oifname "br-ef751dcb2c14" ct state related,established counter packets 13954 bytes 8256199 accept
		oifname "docker0" ct state related,established counter packets 0 bytes 0 accept
	}

	chain DOCKER-INTERNAL {
	}

	chain DOCKER-USER {
	}
}
table ip6 filter {
	chain ufw6-before-logging-input {
	}

	chain ufw6-before-logging-output {
	}

	chain ufw6-before-logging-forward {
	}

	chain ufw6-before-input {
		iifname "lo" counter packets 4 bytes 292 accept
		rt type 0 counter packets 0 bytes 0 drop
		ct state related,established counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type echo-reply counter packets 0 bytes 0 accept
		ct state invalid counter packets 0 bytes 0 jump ufw6-logging-deny
		ct state invalid counter packets 0 bytes 0 drop
		meta l4proto ipv6-icmp icmpv6 type destination-unreachable counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type packet-too-big counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type time-exceeded counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type parameter-problem counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type echo-request counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type nd-router-solicit ip6 hoplimit 255 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type nd-router-advert ip6 hoplimit 255 counter packets 18 bytes 1712 accept
		meta l4proto ipv6-icmp icmpv6 type nd-neighbor-solicit ip6 hoplimit 255 counter packets 546 bytes 39312 accept
		meta l4proto ipv6-icmp icmpv6 type nd-neighbor-advert ip6 hoplimit 255 counter packets 67 bytes 4288 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp icmpv6 type mld-listener-query counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp icmpv6 type mld-listener-report counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp icmpv6 type mld-listener-done counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 1 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 1 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 1 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 ip6 daddr fe80::/10 udp sport 547 udp dport 546 counter packets 0 bytes 0 accept
		ip6 daddr ff02::fb udp dport 5353 counter packets 838 bytes 147646 accept
		ip6 daddr ff02::f udp dport 1900 counter packets 0 bytes 0 accept
		counter packets 0 bytes 0 jump ufw6-user-input
	}

	chain ufw6-before-output {
		oifname "lo" counter packets 4 bytes 292 accept
		rt type 0 counter packets 0 bytes 0 drop
		ct state related,established counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type destination-unreachable counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type packet-too-big counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type time-exceeded counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type parameter-problem counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type echo-request counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type echo-reply counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type nd-router-solicit ip6 hoplimit 255 counter packets 208 bytes 11584 accept
		meta l4proto ipv6-icmp icmpv6 type nd-neighbor-advert ip6 hoplimit 255 counter packets 546 bytes 34952 accept
		meta l4proto ipv6-icmp icmpv6 type nd-neighbor-solicit ip6 hoplimit 255 counter packets 93 bytes 6696 accept
		meta l4proto ipv6-icmp icmpv6 type nd-router-advert ip6 hoplimit 255 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp icmpv6 type mld-listener-query counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp icmpv6 type mld-listener-report counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp icmpv6 type mld-listener-done counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 98 bytes 8148 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 1 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 1 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 1 counter packets 0 bytes 0 accept
		counter packets 489 bytes 58717 jump ufw6-user-output
	}

	chain ufw6-before-forward {
		rt type 0 counter packets 0 bytes 0 drop
		ct state related,established counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type destination-unreachable counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type packet-too-big counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type time-exceeded counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type parameter-problem counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type echo-request counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type echo-reply counter packets 0 bytes 0 accept
		counter packets 0 bytes 0 jump ufw6-user-forward
	}

	chain ufw6-after-input {
		udp dport 137 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		udp dport 138 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		tcp dport 139 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		tcp dport 445 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		udp dport 546 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
		udp dport 547 counter packets 0 bytes 0 jump ufw6-skip-to-policy-input
	}

	chain ufw6-after-output {
	}

	chain ufw6-after-forward {
	}

	chain ufw6-after-logging-input {
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 log prefix "[UFW BLOCK] "
	}

	chain ufw6-after-logging-output {
	}

	chain ufw6-after-logging-forward {
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 log prefix "[UFW BLOCK] "
	}

	chain ufw6-reject-input {
	}

	chain ufw6-reject-output {
	}

	chain ufw6-reject-forward {
	}

	chain ufw6-track-input {
	}

	chain ufw6-track-output {
		meta l4proto tcp ct state new counter packets 0 bytes 0 accept
		meta l4proto udp ct state new counter packets 432 bytes 54085 accept
	}

	chain ufw6-track-forward {
	}

	chain INPUT {
		type filter hook input priority filter; policy drop;
		counter packets 1473 bytes 193250 jump ufw6-before-logging-input
		counter packets 1473 bytes 193250 jump ufw6-before-input
		counter packets 0 bytes 0 jump ufw6-after-input
		counter packets 0 bytes 0 jump ufw6-after-logging-input
		counter packets 0 bytes 0 jump ufw6-reject-input
		counter packets 0 bytes 0 jump ufw6-track-input
	}

	chain OUTPUT {
		type filter hook output priority filter; policy accept;
		counter packets 1438 bytes 120389 jump ufw6-before-logging-output
		counter packets 1438 bytes 120389 jump ufw6-before-output
		counter packets 489 bytes 58717 jump ufw6-after-output
		counter packets 489 bytes 58717 jump ufw6-after-logging-output
		counter packets 489 bytes 58717 jump ufw6-reject-output
		counter packets 489 bytes 58717 jump ufw6-track-output
	}

	chain FORWARD {
		type filter hook forward priority filter; policy drop;
		counter packets 0 bytes 0 jump DOCKER-USER
		counter packets 0 bytes 0 jump DOCKER-FORWARD
		counter packets 0 bytes 0 jump ufw6-before-logging-forward
		counter packets 0 bytes 0 jump ufw6-before-forward
		counter packets 0 bytes 0 jump ufw6-after-forward
		counter packets 0 bytes 0 jump ufw6-after-logging-forward
		counter packets 0 bytes 0 jump ufw6-reject-forward
		counter packets 0 bytes 0 jump ufw6-track-forward
	}

	chain ufw6-logging-deny {
		ct state invalid limit rate 3/minute burst 10 packets counter packets 0 bytes 0 return
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 log prefix "[UFW BLOCK] "
	}

	chain ufw6-logging-allow {
		limit rate 3/minute burst 10 packets counter packets 0 bytes 0 log prefix "[UFW ALLOW] "
	}

	chain ufw6-skip-to-policy-input {
		counter packets 0 bytes 0 drop
	}

	chain ufw6-skip-to-policy-output {
		counter packets 0 bytes 0 accept
	}

	chain ufw6-skip-to-policy-forward {
		counter packets 0 bytes 0 drop
	}

	chain ufw6-user-input {
		tcp dport 22 counter packets 0 bytes 0 accept
		tcp dport 80 counter packets 0 bytes 0 accept
		tcp dport 443 counter packets 0 bytes 0 accept
		udp dport 10000 counter packets 0 bytes 0 accept
		tcp dport 3478 counter packets 0 bytes 0 accept
		udp dport 3478 counter packets 0 bytes 0 accept
		tcp dport 5349 counter packets 0 bytes 0 accept
		udp dport 5349 counter packets 0 bytes 0 accept
	}

	chain ufw6-user-output {
	}

	chain ufw6-user-forward {
	}

	chain ufw6-user-logging-input {
	}

	chain ufw6-user-logging-output {
	}

	chain ufw6-user-logging-forward {
	}

	chain ufw6-user-limit {
		limit rate 3/minute burst 5 packets counter packets 0 bytes 0 log prefix "[UFW LIMIT BLOCK] "
		counter packets 0 bytes 0 reject
	}

	chain ufw6-user-limit-accept {
		counter packets 0 bytes 0 accept
	}

	chain DOCKER {
	}

	chain DOCKER-FORWARD {
		counter packets 0 bytes 0 jump DOCKER-CT
		counter packets 0 bytes 0 jump DOCKER-INTERNAL
		counter packets 0 bytes 0 jump DOCKER-BRIDGE
	}

	chain DOCKER-BRIDGE {
	}

	chain DOCKER-CT {
	}

	chain DOCKER-INTERNAL {
	}

	chain DOCKER-USER {
	}
}
table ip nat {
	chain DOCKER {
		ip daddr 127.0.0.1 tcp dport 8080 counter packets 1 bytes 60 dnat to 172.19.0.2:8080
		udp dport 10000 counter packets 0 bytes 0 dnat to 172.19.0.2:10000
		tcp dport 80 counter packets 0 bytes 0 dnat to 172.20.0.2:80
		tcp dport 443 counter packets 16 bytes 960 dnat to 172.20.0.2:443
		ip daddr 127.0.0.1 tcp dport 8888 counter packets 0 bytes 0 dnat to 172.19.0.3:8888
		tcp dport 9092 counter packets 0 bytes 0 dnat to 172.20.0.4:9092
		tcp dport 9308 counter packets 0 bytes 0 dnat to 172.20.0.5:9308
		tcp dport 8090 counter packets 0 bytes 0 dnat to 172.20.0.6:8090
		tcp dport 3100 counter packets 0 bytes 0 dnat to 172.20.0.7:3100
		tcp dport 9091 counter packets 0 bytes 0 dnat to 172.20.0.8:9090
		tcp dport 3000 counter packets 0 bytes 0 dnat to 172.20.0.11:3000
		tcp dport 8010 counter packets 0 bytes 0 dnat to 172.20.0.13:8010
		tcp dport 8011 counter packets 0 bytes 0 dnat to 172.20.0.14:8011
		tcp dport 8100 counter packets 0 bytes 0 dnat to 172.20.0.15:8100
		tcp dport 8002 counter packets 0 bytes 0 dnat to 172.20.0.16:8002
	}

	chain PREROUTING {
		type nat hook prerouting priority dstnat; policy accept;
		fib daddr type local counter packets 1962 bytes 119796 jump DOCKER
	}

	chain OUTPUT {
		type nat hook output priority dstnat; policy accept;
		fib daddr type local counter packets 33 bytes 4188 jump DOCKER
	}

	chain POSTROUTING {
		type nat hook postrouting priority srcnat; policy accept;
		oifname "docker0" fib saddr type local counter packets 8 bytes 574 masquerade
		ip saddr 172.17.0.0/16 oifname != "docker0" counter packets 2 bytes 568 masquerade
		oifname "br-ef751dcb2c14" fib saddr type local counter packets 11 bytes 755 masquerade
		ip saddr 172.19.0.0/16 oifname != "br-ef751dcb2c14" counter packets 3 bytes 632 masquerade
		oifname "br-c8ba5432ed86" fib saddr type local counter packets 26 bytes 1655 masquerade
		ip saddr 172.20.0.0/16 oifname != "br-c8ba5432ed86" counter packets 10 bytes 1048 masquerade
		oifname "br-9f19243faf15" fib saddr type local counter packets 10 bytes 695 masquerade
		ip saddr 172.18.0.0/16 oifname != "br-9f19243faf15" counter packets 2 bytes 552 masquerade
		ip saddr 172.19.0.2 ip daddr 172.19.0.2 tcp dport 8080 counter packets 0 bytes 0 masquerade
		ip saddr 172.19.0.2 ip daddr 172.19.0.2 udp dport 10000 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.2 ip daddr 172.20.0.2 tcp dport 80 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.2 ip daddr 172.20.0.2 tcp dport 443 counter packets 0 bytes 0 masquerade
		ip saddr 172.19.0.3 ip daddr 172.19.0.3 tcp dport 8888 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.4 ip daddr 172.20.0.4 tcp dport 9092 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.5 ip daddr 172.20.0.5 tcp dport 9308 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.6 ip daddr 172.20.0.6 tcp dport 8090 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.7 ip daddr 172.20.0.7 tcp dport 3100 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.8 ip daddr 172.20.0.8 tcp dport 9090 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.11 ip daddr 172.20.0.11 tcp dport 3000 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.13 ip daddr 172.20.0.13 tcp dport 8010 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.14 ip daddr 172.20.0.14 tcp dport 8011 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.15 ip daddr 172.20.0.15 tcp dport 8100 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.16 ip daddr 172.20.0.16 tcp dport 8002 counter packets 0 bytes 0 masquerade
	}
}
table ip6 nat {
	chain DOCKER {
	}

	chain PREROUTING {
		type nat hook prerouting priority dstnat; policy accept;
		fib daddr type local counter packets 0 bytes 0 jump DOCKER
	}

	chain OUTPUT {
		type nat hook output priority dstnat; policy accept;
		fib daddr type local counter packets 1 bytes 80 jump DOCKER
	}
}
table ip raw {
	chain PREROUTING {
		type filter hook prerouting priority raw; policy accept;
		ip daddr 172.19.0.2 iifname != "br-ef751dcb2c14" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.2 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.19.0.3 iifname != "br-ef751dcb2c14" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.3 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 127.0.0.1 iifname != "lo" tcp dport 8080 counter packets 0 bytes 0 drop
		ip daddr 172.19.0.4 iifname != "br-ef751dcb2c14" counter packets 0 bytes 0 drop
		ip daddr 127.0.0.1 iifname != "lo" tcp dport 8888 counter packets 0 bytes 0 drop
		ip daddr 172.18.0.2 iifname != "br-9f19243faf15" counter packets 0 bytes 0 drop
		ip daddr 172.19.0.5 iifname != "br-ef751dcb2c14" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.4 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.5 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.6 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.7 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.8 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.9 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.10 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.11 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.12 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.13 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.14 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.15 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.16 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
	}
}



---

# 22. CRON / TIMERS

**Date :** 2026-08-12 20:37:41 EDT


## Cron


```text
$ grep -RniE "jitsi|prosody|jicofo|videobridge|turn|certbot" /etc/cron* /var/spool/cron* 2>/dev/null || true
```
/etc/cron.daily/apt-compat:16:    # laptop check, on_ac_power returns:
/etc/cron.daily/apt-compat:20:    # Desktop systems always return 255 it seems
/etc/cron.daily/apt-compat:25:            return 1
/etc/cron.daily/apt-compat:28:    return 0
/etc/cron.daily/apt-compat:38:	return


## Systemd timers


```text
$ systemctl list-timers --all --no-pager 2>/dev/null
```
NEXT                            LEFT LAST                              PASSED UNIT                         ACTIVATES
Wed 2026-08-12 21:15:02 EDT    37min Wed 2026-08-12 20:29:01 EDT     8min ago fwupd-refresh.timer          fwupd-refresh.service
Wed 2026-08-12 21:32:59 EDT    55min Wed 2026-08-12 20:34:00 EDT 3min 40s ago anacron.timer                anacron.service
Thu 2026-08-13 00:00:00 EDT 3h 22min Wed 2026-08-12 00:00:02 EDT            - dpkg-db-backup.timer         dpkg-db-backup.service
Thu 2026-08-13 00:29:42 EDT 3h 52min Wed 2026-08-12 02:38:52 EDT            - logrotate.timer              logrotate.service
Thu 2026-08-13 06:08:29 EDT       9h Wed 2026-08-12 07:15:21 EDT            - apt-daily-upgrade.timer      apt-daily-upgrade.service
Thu 2026-08-13 08:12:56 EDT      11h Wed 2026-08-12 08:47:16 EDT            - man-db.timer                 man-db.service
Thu 2026-08-13 10:31:06 EDT      13h Wed 2026-08-12 20:22:43 EDT    14min ago apt-daily.timer              apt-daily.service
Thu 2026-08-13 20:06:16 EDT      23h Wed 2026-08-12 20:06:16 EDT    31min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Sun 2026-08-16 03:10:02 EDT   3 days Sun 2026-08-09 14:39:53 EDT            - e2scrub_all.timer            e2scrub_all.service
Mon 2026-08-17 01:10:57 EDT   4 days Tue 2026-08-11 06:35:54 EDT            - fstrim.timer                 fstrim.service

10 timers listed.



---

# 23. CERTBOT

**Date :** 2026-08-12 20:37:41 EDT


```text
$ certbot --version 2>&1 || true
```
bash: line 1: certbot: command not found


```text
$ find /etc/letsencrypt -type f -maxdepth 5 -print 2>/dev/null | sort || true
```


```text
$ systemctl list-unit-files 2>/dev/null | grep -i certbot || true
```



---

# 24. DOCKER — POUR VÉRIFIER UNE INSTALLATION EXISTANTE

**Date :** 2026-08-12 20:37:42 EDT


```text
$ docker --version 2>/dev/null || true
```
Docker version 29.7.2, build a7dcaa6


```text
$ docker ps -a 2>/dev/null || true
```
CONTAINER ID   IMAGE                             COMMAND                  CREATED          STATUS                    PORTS                                                NAMES
8fff25cf117f   peer-peer                         "uvicorn app.main:ap…"   44 minutes ago   Up 44 minutes             0.0.0.0:8002->8002/tcp                               civitas-peer
0514d05cdb89   event-bridge-event-bridge         "uvicorn main:app --…"   44 minutes ago   Up 44 minutes             0.0.0.0:8100->8100/tcp                               civitas-event-bridge
ac6dd6db04f3   room-spawner-room-spawner         "uvicorn app.main:ap…"   44 minutes ago   Up 44 minutes             0.0.0.0:8011->8011/tcp                               civitas-room-spawner
84d063a086a7   room-config-room-config           "uvicorn app.main:ap…"   44 minutes ago   Up 44 minutes             0.0.0.0:8010->8010/tcp                               civitas-room-config
6fea6a7b261b   postgres:16-alpine                "docker-entrypoint.s…"   44 minutes ago   Up 44 minutes (healthy)   5432/tcp                                             civitas-postgres
bc68d4943974   grafana/grafana:latest            "/run.sh"                44 minutes ago   Up 44 minutes             0.0.0.0:3000->3000/tcp                               civitas-grafana
187008602bcc   grafana/loki:2.9.0                "/usr/bin/loki -conf…"   44 minutes ago   Up 44 minutes             0.0.0.0:3100->3100/tcp                               civitas-loki
0e5db5416b17   grafana/promtail:2.9.0            "/usr/bin/promtail -…"   44 minutes ago   Up 44 minutes                                                                  civitas-promtail
ccb029548cfc   prom/prometheus:latest            "/bin/prometheus --c…"   44 minutes ago   Up 44 minutes             0.0.0.0:9091->9090/tcp                               civitas-prometheus
95759a15da2d   prom/node-exporter:latest         "/bin/node_exporter …"   44 minutes ago   Up 44 minutes             9100/tcp                                             civitas-node-exporter
d4c557cfbf24   provectuslabs/kafka-ui:latest     "/bin/sh -c 'java --…"   45 minutes ago   Up 44 minutes             8080/tcp, 0.0.0.0:8090->8090/tcp                     civitas-kafka-ui
d1c0ef7e71d0   danielqsj/kafka-exporter:latest   "/bin/kafka_exporter…"   45 minutes ago   Up 44 minutes             0.0.0.0:9308->9308/tcp                               civitas-kafka-exporter
28d459c48c57   confluentinc/cp-kafka:7.6.0       "/etc/confluent/dock…"   45 minutes ago   Up 45 minutes (healthy)   0.0.0.0:9092->9092/tcp                               civitas-kafka
a2fe9ceff8b5   jitsi-nginx                       "/docker-entrypoint.…"   18 hours ago     Up 45 minutes             0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp             civitas-nginx
b407af57f78a   ghcr.io/jitsi/web:stable          "/init"                  18 hours ago     Up 45 minutes             8000/tcp, 8443/tcp                                   jitsi-web-1
37b31adb4ffb   ghcr.io/jitsi/jvb:stable          "/init"                  18 hours ago     Up 45 minutes             127.0.0.1:8080->8080/tcp, 0.0.0.0:10000->10000/udp   jitsi-jvb-1
a1351ad12314   ghcr.io/jitsi/jicofo:stable       "/init"                  18 hours ago     Up 45 minutes             127.0.0.1:8888->8888/tcp                             jitsi-jicofo-1
e0938236825a   ghcr.io/jitsi/prosody:stable      "/init"                  18 hours ago     Up 45 minutes             5222/tcp, 5269/tcp, 5280/tcp, 5347/tcp               jitsi-prosody-1


```text
$ docker images 2>/dev/null || true
```
IMAGE                              ID             DISK USAGE   CONTENT SIZE   EXTRA
confluentinc/cp-kafka:7.6.0        d87a8d474634        806MB             0B   U    
curlimages/curl:latest             5c3599497451       23.8MB             0B        
danielqsj/kafka-exporter:latest    a3e635c3de94       27.5MB             0B   U    
event-bridge-event-bridge:latest   d2a50dd903c3        172MB             0B   U    
ghcr.io/jitsi/jicofo:stable        792df0b19cb7        684MB             0B   U    
ghcr.io/jitsi/jvb:stable           610e5f7254b8        804MB             0B   U    
ghcr.io/jitsi/prosody:stable       c4b61d76fd6e        169MB             0B   U    
ghcr.io/jitsi/web:stable           0ef2534f9ea9        369MB             0B   U    
grafana/grafana:latest             beafdfed0240        761MB             0B   U    
grafana/loki:2.9.0                 21abbe8487a0       74.8MB             0B   U    
grafana/promtail:2.9.0             e48aaa4dcb3b        198MB             0B   U    
jitsi-nginx:latest                 7f367bb7678d        161MB             0B   U    
nginx:stable                       886dbea595a1        161MB             0B        
peer-peer:latest                   a1af3591b306       1.47GB             0B   U    
postgres:16-alpine                 108b27c919e6        276MB             0B   U    
prom/node-exporter:latest          696e69e899e0       25.7MB             0B   U    
prom/prometheus:latest             5a2c7fe42427        390MB             0B   U    
provectuslabs/kafka-ui:latest      99307ab28a49        291MB             0B   U    
room-config-room-config:latest     4c2ba2b1a93b        208MB             0B   U    
room-spawner-room-spawner:latest   f179ac0f2753        174MB             0B   U    


```text
$ docker compose version 2>/dev/null || true
```
Docker Compose version v5.4.0



---

# 25. DNS / HOSTNAME

**Date :** 2026-08-12 20:37:42 EDT


```text
$ hostname -f
```
meet.civitas.local


```text
$ cat /etc/hosts
```
127.0.0.1       localhost
127.0.1.1       meet.civitas.local meet
192.168.1.89    meet.civitas.local meet


```text
$ cat /etc/resolv.conf
```
# Generated by NetworkManager
search civitas.local
nameserver 192.168.1.254


```text
$ grep -RniE "meet\.|jitsi|xmpp|conference\.|auth\.|focus\.|jvb\." /etc/hosts /etc/jitsi /etc/prosody 2>/dev/null || true
```
/etc/hosts:2:127.0.1.1       meet.civitas.local meet
/etc/hosts:3:192.168.1.89    meet.civitas.local meet



---

# 26. RÉSEAU

**Date :** 2026-08-12 20:37:42 EDT


```text
$ ip addr
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:d0:1a:71 brd ff:ff:ff:ff:ff:ff
    altname enx080027d01a71
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:46:cc:3e brd ff:ff:ff:ff:ff:ff
    altname enx08002746cc3e
4: enp0s9: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:59:54:fd brd ff:ff:ff:ff:ff:ff
    altname enx0800275954fd
    inet 192.168.1.64/24 brd 192.168.1.255 scope global dynamic noprefixroute enp0s9
       valid_lft 83671sec preferred_lft 83671sec
    inet6 fe80::a00:27ff:fe59:54fd/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
5: br-9f19243faf15: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 22:c5:b2:3e:9d:af brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-9f19243faf15
       valid_lft forever preferred_lft forever
    inet6 fe80::20c5:b2ff:fe3e:9daf/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
6: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 5e:02:db:5a:2d:81 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
7: br-c8ba5432ed86: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 6a:73:08:77:67:a5 brd ff:ff:ff:ff:ff:ff
    inet 172.20.0.1/16 brd 172.20.255.255 scope global br-c8ba5432ed86
       valid_lft forever preferred_lft forever
    inet6 fe80::6873:8ff:fe77:67a5/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
8: br-ef751dcb2c14: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 8e:15:50:41:fd:27 brd ff:ff:ff:ff:ff:ff
    inet 172.19.0.1/16 brd 172.19.255.255 scope global br-ef751dcb2c14
       valid_lft forever preferred_lft forever
    inet6 fe80::8c15:50ff:fe41:fd27/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
9: veth1b69f54@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 8e:cb:4e:8a:f0:1c brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::8ccb:4eff:fe8a:f01c/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
10: vethe4fd647@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-ef751dcb2c14 state UP group default 
    link/ether 7a:16:41:2d:6e:a9 brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::7816:41ff:fe2d:6ea9/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
11: veth0b2f8c9@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-ef751dcb2c14 state UP group default 
    link/ether 66:0e:be:a6:5c:77 brd ff:ff:ff:ff:ff:ff link-netnsid 2
    inet6 fe80::640e:beff:fea6:5c77/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
12: veth253427e@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether ae:d6:99:da:8b:2f brd ff:ff:ff:ff:ff:ff link-netnsid 3
    inet6 fe80::acd6:99ff:feda:8b2f/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
13: vethb7e627e@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-ef751dcb2c14 state UP group default 
    link/ether c6:02:5e:f5:8c:74 brd ff:ff:ff:ff:ff:ff link-netnsid 4
    inet6 fe80::c402:5eff:fef5:8c74/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
14: veth5c44ec6@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-9f19243faf15 state UP group default 
    link/ether da:05:34:7e:35:82 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::d805:34ff:fe7e:3582/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
15: veth9e4d226@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-ef751dcb2c14 state UP group default 
    link/ether ba:af:88:00:be:61 brd ff:ff:ff:ff:ff:ff link-netnsid 3
    inet6 fe80::b8af:88ff:fe00:be61/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
16: veth293f740@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether a2:bc:aa:68:8c:ec brd ff:ff:ff:ff:ff:ff link-netnsid 5
    inet6 fe80::a0bc:aaff:fe68:8cec/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
17: veth1152acf@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 0e:c6:f7:bf:ca:a1 brd ff:ff:ff:ff:ff:ff link-netnsid 6
    inet6 fe80::cc6:f7ff:febf:caa1/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
18: vethcbdfa81@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 46:cf:92:0e:91:a1 brd ff:ff:ff:ff:ff:ff link-netnsid 7
    inet6 fe80::44cf:92ff:fe0e:91a1/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
19: veth541118e@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether e6:85:48:f4:24:3e brd ff:ff:ff:ff:ff:ff link-netnsid 8
    inet6 fe80::e485:48ff:fef4:243e/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
20: veth2b7bc44@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether ba:c0:c6:03:bd:c2 brd ff:ff:ff:ff:ff:ff link-netnsid 9
    inet6 fe80::b8c0:c6ff:fe03:bdc2/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
21: veth4376298@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 56:75:2b:5e:b9:2d brd ff:ff:ff:ff:ff:ff link-netnsid 10
    inet6 fe80::5475:2bff:fe5e:b92d/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
22: veth277d359@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 02:fb:fa:73:95:1b brd ff:ff:ff:ff:ff:ff link-netnsid 11
    inet6 fe80::fb:faff:fe73:951b/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
23: veth7dacd9c@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 62:4a:50:b9:1a:60 brd ff:ff:ff:ff:ff:ff link-netnsid 12
    inet6 fe80::604a:50ff:feb9:1a60/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
24: veth69c2a22@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether f2:f9:ca:dc:42:e4 brd ff:ff:ff:ff:ff:ff link-netnsid 13
    inet6 fe80::f0f9:caff:fedc:42e4/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
25: vethfa5af70@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 8a:f3:e3:29:43:d1 brd ff:ff:ff:ff:ff:ff link-netnsid 14
    inet6 fe80::88f3:e3ff:fe29:43d1/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
26: veth1f04dcf@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 6e:3c:49:f3:45:2c brd ff:ff:ff:ff:ff:ff link-netnsid 15
    inet6 fe80::6c3c:49ff:fef3:452c/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
27: veth0002f51@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 1a:e7:84:76:4c:0a brd ff:ff:ff:ff:ff:ff link-netnsid 16
    inet6 fe80::18e7:84ff:fe76:4c0a/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
28: veth8239bf5@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 1e:62:93:7e:53:8f brd ff:ff:ff:ff:ff:ff link-netnsid 17
    inet6 fe80::1c62:93ff:fe7e:538f/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever


```text
$ ip route
```
default via 192.168.1.254 dev enp0s9 proto dhcp src 192.168.1.64 metric 101 
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
172.18.0.0/16 dev br-9f19243faf15 proto kernel scope link src 172.18.0.1 
172.19.0.0/16 dev br-ef751dcb2c14 proto kernel scope link src 172.19.0.1 
172.20.0.0/16 dev br-c8ba5432ed86 proto kernel scope link src 172.20.0.1 
192.168.1.0/24 dev enp0s9 proto kernel scope link src 192.168.1.64 metric 101 


```text
$ ip -6 route
```
fe80::/64 dev vethe4fd647 proto kernel metric 256 pref medium
fe80::/64 dev br-ef751dcb2c14 proto kernel metric 256 pref medium
fe80::/64 dev veth1b69f54 proto kernel metric 256 pref medium
fe80::/64 dev br-c8ba5432ed86 proto kernel metric 256 pref medium
fe80::/64 dev veth0b2f8c9 proto kernel metric 256 pref medium
fe80::/64 dev veth253427e proto kernel metric 256 pref medium
fe80::/64 dev vethb7e627e proto kernel metric 256 pref medium
fe80::/64 dev veth5c44ec6 proto kernel metric 256 pref medium
fe80::/64 dev br-9f19243faf15 proto kernel metric 256 pref medium
fe80::/64 dev veth9e4d226 proto kernel metric 256 pref medium
fe80::/64 dev veth293f740 proto kernel metric 256 pref medium
fe80::/64 dev veth1152acf proto kernel metric 256 pref medium
fe80::/64 dev vethcbdfa81 proto kernel metric 256 pref medium
fe80::/64 dev veth541118e proto kernel metric 256 pref medium
fe80::/64 dev veth2b7bc44 proto kernel metric 256 pref medium
fe80::/64 dev veth4376298 proto kernel metric 256 pref medium
fe80::/64 dev veth277d359 proto kernel metric 256 pref medium
fe80::/64 dev veth7dacd9c proto kernel metric 256 pref medium
fe80::/64 dev veth69c2a22 proto kernel metric 256 pref medium
fe80::/64 dev vethfa5af70 proto kernel metric 256 pref medium
fe80::/64 dev veth1f04dcf proto kernel metric 256 pref medium
fe80::/64 dev veth0002f51 proto kernel metric 256 pref medium
fe80::/64 dev veth8239bf5 proto kernel metric 256 pref medium
fe80::/64 dev enp0s9 proto kernel metric 1024 pref medium


## NetworkManager / systemd-networkd


```text
$ nmcli connection show 2>/dev/null || true
```
NAME                UUID                                  TYPE      DEVICE          
Wired connection 1  e40cfa8b-9095-44bb-a153-ad58dc706b95  ethernet  enp0s9          
br-9f19243faf15     6d02f48a-b543-4e6d-9205-4eb544e1deeb  bridge    br-9f19243faf15 
br-c8ba5432ed86     7fd1e213-d511-46f9-a009-54e20e289e2e  bridge    br-c8ba5432ed86 
br-ef751dcb2c14     c37802b4-2b70-4de1-bf09-a4a5b89d98db  bridge    br-ef751dcb2c14 
lo                  7158fad1-1d0a-4248-9f39-83a2b5ea598e  loopback  lo              
docker0             9088c0fa-66bf-49a6-bb38-8a3f76c3b00b  bridge    docker0         


```text
$ networkctl list 2>/dev/null || true
```
IDX LINK            TYPE     OPERATIONAL SETUP
  1 lo              loopback -           unmanaged
  2 enp0s3          ether    -           unmanaged
  3 enp0s8          ether    -           unmanaged
  4 enp0s9          ether    -           unmanaged
  5 br-9f19243faf15 bridge   -           unmanaged
  6 docker0         bridge   -           unmanaged
  7 br-c8ba5432ed86 bridge   -           unmanaged
  8 br-ef751dcb2c14 bridge   -           unmanaged
  9 veth1b69f54     ether    -           unmanaged
 10 vethe4fd647     ether    -           unmanaged
 11 veth0b2f8c9     ether    -           unmanaged
 12 veth253427e     ether    -           unmanaged
 13 vethb7e627e     ether    -           unmanaged
 14 veth5c44ec6     ether    -           unmanaged
 15 veth9e4d226     ether    -           unmanaged
 16 veth293f740     ether    -           unmanaged
 17 veth1152acf     ether    -           unmanaged
 18 vethcbdfa81     ether    -           unmanaged
 19 veth541118e     ether    -           unmanaged
 20 veth2b7bc44     ether    -           unmanaged
 21 veth4376298     ether    -           unmanaged
 22 veth277d359     ether    -           unmanaged
 23 veth7dacd9c     ether    -           unmanaged
 24 veth69c2a22     ether    -           unmanaged
 25 vethfa5af70     ether    -           unmanaged
 26 veth1f04dcf     ether    -           unmanaged
 27 veth0002f51     ether    -           unmanaged
 28 veth8239bf5     ether    -           unmanaged

28 links listed.



---

# 27. VARIABLES D'ENVIRONNEMENT

**Date :** 2026-08-12 20:37:42 EDT


## Environnement global


```text
$ env | sort
```
COLORTERM=truecolor
HOME=/root
LANG=en_US.UTF-8
LOGNAME=root
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=00:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.7z=01;31:*.ace=01;31:*.alz=01;31:*.apk=01;31:*.arc=01;31:*.arj=01;31:*.bz=01;31:*.bz2=01;31:*.cab=01;31:*.cpio=01;31:*.crate=01;31:*.deb=01;31:*.drpm=01;31:*.dwm=01;31:*.dz=01;31:*.ear=01;31:*.egg=01;31:*.esd=01;31:*.gz=01;31:*.jar=01;31:*.lha=01;31:*.lrz=01;31:*.lz=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.lzo=01;31:*.pyz=01;31:*.rar=01;31:*.rpm=01;31:*.rz=01;31:*.sar=01;31:*.swm=01;31:*.t7z=01;31:*.tar=01;31:*.taz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tgz=01;31:*.tlz=01;31:*.txz=01;31:*.tz=01;31:*.tzo=01;31:*.tzst=01;31:*.udeb=01;31:*.war=01;31:*.whl=01;31:*.wim=01;31:*.xz=01;31:*.z=01;31:*.zip=01;31:*.zoo=01;31:*.zst=01;31:*.avif=01;35:*.jpg=01;35:*.jpeg=01;35:*.jxl=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:*~=00;90:*#=00;90:*.bak=00;90:*.crdownload=00;90:*.dpkg-dist=00;90:*.dpkg-new=00;90:*.dpkg-old=00;90:*.dpkg-tmp=00;90:*.old=00;90:*.orig=00;90:*.part=00;90:*.rej=00;90:*.rpmnew=00;90:*.rpmorig=00;90:*.rpmsave=00;90:*.swp=00;90:*.tmp=00;90:*.ucf-dist=00;90:*.ucf-new=00;90:*.ucf-old=00;90:
MAIL=/var/mail/root
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/opt/civitas
SHELL=/bin/bash
SHLVL=2
SUDO_COMMAND=/usr/bin/bash jitsi-infrastructure-audit.sh
SUDO_GID=1000
SUDO_HOME=/home/civitas
SUDO_UID=1000
SUDO_USER=civitas
TERM=xterm-256color
USER=root
_=/usr/bin/env


## Variables Jitsi


```text
$ env | grep -Ei "jitsi|jicofo|jvb|prosody|xmpp|turn" || true
```
SUDO_COMMAND=/usr/bin/bash jitsi-infrastructure-audit.sh



---

# 28. FICHIERS ENVIRONNEMENT

**Date :** 2026-08-12 20:37:42 EDT


```text
$ find /etc /opt /var/lib /usr/local -type f \( -name ".env" -o -name "*.env" \) -print 2>/dev/null | sort
```
/opt/civitas/config/civitas.env
/opt/civitas/jitsi/.env
/opt/civitas/services/peer/.env
/opt/civitas/services/room-config/.env
/opt/civitas/services/room-spawner/.env



---

# 29. RECHERCHE DE MOTS-CLÉS JITSI

**Date :** 2026-08-12 20:37:43 EDT


## Configuration globale


```text
$ grep -RniE "jitsi|jicofo|videobridge|prosody|xmpp|colibri|bosh|conference\.|focus\." /etc 2>/dev/null | head -5000 || true
```
/etc/xdg/autostart/org.kde.xwaylandvideobridge.desktop:60:Icon=xwaylandvideobridge
/etc/xdg/autostart/org.kde.xwaylandvideobridge.desktop:61:Exec=xwaylandvideobridge
/etc/services:225:xmpp-client	5222/tcp	jabber-client	# Jabber Client Connection
/etc/services:226:xmpp-server	5269/tcp	jabber-server	# Jabber Server Connection
/etc/libreoffice/registry/main.xcd:2417:          <prop oor:name="JumboSheets" oor:type="xs:boolean" oor:nillable="false">
/etc/libreoffice/registry/main.xcd:4784:            the focus.
/etc/passwd-:39:jicofo:x:996:1001::/usr/share/jicofo:/bin/bash
/etc/gimp/3.0/gimprc:646:# receives the focus. This is useful for window managers using "click to
/etc/mime.types:1752:application/xmpp+xml
/etc/gshadow-:68:jitsi:!::
/etc/gshadow-:69:prosody:!::
/etc/ufw/applications.d/ufw-chat:31:[XMPP]
/etc/ufw/applications.d/ufw-chat:32:title=XMPP Chat
/etc/ufw/applications.d/ufw-chat:33:description=XMPP protocol (Jabber and Google Talk)
/etc/group-:68:jitsi:x:1001:
/etc/group-:69:prosody:x:115:
/etc/ssl/certs/ca-certificates.crt:3476:yKsi2XMPpfRaAok/T54igu6idFMqPVMnaR1sjjIsZAAmY2E2TqNGtz99sy2sbZCi
/etc/ssl/certs/TWCA_Global_Root_CA.pem:13:yKsi2XMPpfRaAok/T54igu6idFMqPVMnaR1sjjIsZAAmY2E2TqNGtz99sy2sbZCi
/etc/ssl/certs/5f15c80c.0:13:yKsi2XMPpfRaAok/T54igu6idFMqPVMnaR1sjjIsZAAmY2E2TqNGtz99sy2sbZCi
/etc/gshadow:68:jitsi:!::
/etc/fail2ban/action.d/firewallcmd-common.conf:45:#          telnet tftp tftp-client tinc tor-socks transmission-client vdsm vnc-server wbem-https xmpp-bosh xmpp-client xmpp-local xmpp-server
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf:2:# S'assurer que Prosody et le réseau sont prêts avant JVB
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf:3:After=network-online.target prosody.service jicofo.service
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf:4:Requires=network-online.target prosody.service
/etc/systemd/system/civitas.service:3:After=network-online.target jitsi-videobridge2.service jicofo.service prosody.service docker.service
/etc/systemd/system/civitas.service:5:Wants=jitsi-videobridge2.service jicofo.service
/etc/systemd/system/multi-user.target.wants/civitas.service:3:After=network-online.target jitsi-videobridge2.service jicofo.service prosody.service docker.service
/etc/systemd/system/multi-user.target.wants/civitas.service:5:Wants=jitsi-videobridge2.service jicofo.service
/etc/shadow-:39:jicofo:!:20535::::::
/etc/dictionaries-common/words:10503:bosh
/etc/dictionaries-common/words:10504:bosh's
/etc/dictionaries-common/words:50443:kibosh
/etc/dictionaries-common/words:50444:kibosh's
/etc/dictionaries-common/words:72708:prosody
/etc/dictionaries-common/words:72709:prosody's
/etc/group:68:jitsi:x:1001:
/etc/apt/sources.list.d/jitsi-stable.list:1:deb [signed-by=/etc/apt/keyrings/jitsi.gpg] https://download.jitsi.org stable/



---

# 30. ARBRE DE L'INSTALLATION

**Date :** 2026-08-12 20:37:44 EDT


## /etc/jitsi


```text
$ tree -a -L 6 /etc/jitsi 2>/dev/null || find /etc/jitsi -maxdepth 6 -print 2>/dev/null | sort
```
/etc/jitsi  [error opening dir]

0 directories, 0 files


## /etc/prosody


```text
$ tree -a -L 6 /etc/prosody 2>/dev/null || find /etc/prosody -maxdepth 6 -print 2>/dev/null | sort
```
/etc/prosody  [error opening dir]

0 directories, 0 files


## /usr/share/jitsi-meet


```text
$ tree -a -L 4 /usr/share/jitsi-meet 2>/dev/null || find /usr/share/jitsi-meet -maxdepth 4 -print 2>/dev/null | sort
```
/usr/share/jitsi-meet
└── prosody-plugins
    └── mod_muc_webhook.lua

2 directories, 1 file



---

# 31. FICHIERS FOURNIS PAR LES PAQUETS

**Date :** 2026-08-12 20:37:44 EDT


## Package : jitsi-meet


```text
$ dpkg -L 'jitsi-meet' 2>/dev/null || true
```


## Package : jitsi-meet-web


```text
$ dpkg -L 'jitsi-meet-web' 2>/dev/null || true
```


## Package : jitsi-meet-web-config


```text
$ dpkg -L 'jitsi-meet-web-config' 2>/dev/null || true
```


## Package : jitsi-meet-prosody


```text
$ dpkg -L 'jitsi-meet-prosody' 2>/dev/null || true
```


## Package : jitsi-meet-turnserver


```text
$ dpkg -L 'jitsi-meet-turnserver' 2>/dev/null || true
```


## Package : jicofo


```text
$ dpkg -L 'jicofo' 2>/dev/null || true
```


## Package : jitsi-videobridge2


```text
$ dpkg -L 'jitsi-videobridge2' 2>/dev/null || true
```


## Package : prosody


```text
$ dpkg -L 'prosody' 2>/dev/null || true
```


## Package : coturn


```text
$ dpkg -L 'coturn' 2>/dev/null || true
```
/.
/etc
/etc/default
/etc/default/coturn
/etc/init.d
/etc/init.d/coturn
/etc/turnserver.conf
/etc/ufw
/etc/ufw/applications.d
/etc/ufw/applications.d/turnserver
/usr
/usr/bin
/usr/bin/turnserver
/usr/bin/turnutils_natdiscovery
/usr/bin/turnutils_oauth
/usr/bin/turnutils_peer
/usr/bin/turnutils_stunclient
/usr/bin/turnutils_uclient
/usr/include
/usr/include/turn
/usr/include/turn/TurnMsgLib.h
/usr/include/turn/ns_turn_defs.h
/usr/include/turn/ns_turn_ioaddr.h
/usr/include/turn/ns_turn_msg.h
/usr/include/turn/ns_turn_msg_addr.h
/usr/include/turn/ns_turn_msg_defs.h
/usr/include/turn/ns_turn_msg_defs_experimental.h
/usr/lib
/usr/lib/libturnclient.a
/usr/lib/systemd
/usr/lib/systemd/system
/usr/lib/systemd/system/coturn.service
/usr/share
/usr/share/coturn
/usr/share/coturn/schema.mongo.sh
/usr/share/coturn/schema.sql
/usr/share/coturn/schema.stats.redis
/usr/share/coturn/schema.userdb.redis
/usr/share/coturn/testmongosetup.sh
/usr/share/coturn/testredisdbsetup.sh
/usr/share/coturn/testsqldbsetup.sql
/usr/share/doc
/usr/share/doc/coturn
/usr/share/doc/coturn/README.Debian
/usr/share/doc/coturn/README.turnadmin.gz
/usr/share/doc/coturn/README.turnserver.gz
/usr/share/doc/coturn/README.turnutils.gz
/usr/share/doc/coturn/changelog.Debian.gz
/usr/share/doc/coturn/changelog.gz
/usr/share/doc/coturn/copyright
/usr/share/doc/coturn/examples
/usr/share/doc/coturn/examples/ca
/usr/share/doc/coturn/examples/ca/CA.pl.diff
/usr/share/doc/coturn/examples/ca/openssl.conf
/usr/share/doc/coturn/examples/ca/run.sh
/usr/share/doc/coturn/examples/cpu-mem.sh
/usr/share/doc/coturn/examples/etc
/usr/share/doc/coturn/examples/etc/coturn.service
/usr/share/doc/coturn/examples/etc/turnserver.conf
/usr/share/doc/coturn/examples/run_all_clients.sh
/usr/share/doc/coturn/examples/run_tests.sh
/usr/share/doc/coturn/examples/scripts
/usr/share/doc/coturn/examples/scripts/basic
/usr/share/doc/coturn/examples/scripts/basic/dos_attack.sh
/usr/share/doc/coturn/examples/scripts/basic/relay.sh
/usr/share/doc/coturn/examples/scripts/basic/tcp_client.sh
/usr/share/doc/coturn/examples/scripts/basic/tcp_client_c2c_tcp_relay.sh
/usr/share/doc/coturn/examples/scripts/basic/udp_c2c_client.sh
/usr/share/doc/coturn/examples/scripts/basic/udp_client.sh
/usr/share/doc/coturn/examples/scripts/loadbalance
/usr/share/doc/coturn/examples/scripts/loadbalance/master_relay.sh
/usr/share/doc/coturn/examples/scripts/loadbalance/slave_relay_1.sh
/usr/share/doc/coturn/examples/scripts/loadbalance/slave_relay_2.sh
/usr/share/doc/coturn/examples/scripts/loadbalance/tcp_c2c_tcp_relay.sh
/usr/share/doc/coturn/examples/scripts/loadbalance/udp_c2c.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_dos_attack.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_dtls_client.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_dtls_client_cert.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_relay.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_relay_cert.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_sctp_client.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_tcp_client.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_tcp_client_c2c_tcp_relay.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_tls_client.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_tls_client_c2c_tcp_relay.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_tls_client_cert.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_udp_c2c.sh
/usr/share/doc/coturn/examples/scripts/longtermsecure/secure_udp_client.sh
/usr/share/doc/coturn/examples/scripts/longtermsecuredb
/usr/share/doc/coturn/examples/scripts/longtermsecuredb/secure_relay_with_db_mongo.sh
/usr/share/doc/coturn/examples/scripts/longtermsecuredb/secure_relay_with_db_mysql.sh
/usr/share/doc/coturn/examples/scripts/longtermsecuredb/secure_relay_with_db_mysql_ssl.sh
/usr/share/doc/coturn/examples/scripts/longtermsecuredb/secure_relay_with_db_psql.sh
/usr/share/doc/coturn/examples/scripts/longtermsecuredb/secure_relay_with_db_redis.sh
/usr/share/doc/coturn/examples/scripts/longtermsecuredb/secure_relay_with_db_sqlite.sh
/usr/share/doc/coturn/examples/scripts/mobile
/usr/share/doc/coturn/examples/scripts/mobile/mobile_dtls_client.sh
/usr/share/doc/coturn/examples/scripts/mobile/mobile_relay.sh
/usr/share/doc/coturn/examples/scripts/mobile/mobile_tcp_client.sh
/usr/share/doc/coturn/examples/scripts/mobile/mobile_tls_client_c2c_tcp_relay.sh
/usr/share/doc/coturn/examples/scripts/mobile/mobile_udp_client.sh
/usr/share/doc/coturn/examples/scripts/oauth.sh
/usr/share/doc/coturn/examples/scripts/pack.sh
/usr/share/doc/coturn/examples/scripts/peer.sh
/usr/share/doc/coturn/examples/scripts/readme.txt
/usr/share/doc/coturn/examples/scripts/restapi
/usr/share/doc/coturn/examples/scripts/restapi/secure_relay_secret.sh
/usr/share/doc/coturn/examples/scripts/restapi/secure_relay_secret_with_db_mongo.sh
/usr/share/doc/coturn/examples/scripts/restapi/secure_relay_secret_with_db_mysql.sh
/usr/share/doc/coturn/examples/scripts/restapi/secure_relay_secret_with_db_psql.sh
/usr/share/doc/coturn/examples/scripts/restapi/secure_relay_secret_with_db_redis.sh
/usr/share/doc/coturn/examples/scripts/restapi/secure_relay_secret_with_db_sqlite.sh
/usr/share/doc/coturn/examples/scripts/restapi/secure_udp_client_with_secret.sh
/usr/share/doc/coturn/examples/scripts/restapi/shared_secret_maintainer.pl
/usr/share/doc/coturn/examples/scripts/rfc5769.sh
/usr/share/doc/coturn/examples/scripts/selfloadbalance
/usr/share/doc/coturn/examples/scripts/selfloadbalance/secure_dos_attack.sh
/usr/share/doc/coturn/examples/scripts/selfloadbalance/secure_relay.sh
/usr/share/doc/coturn/examples/var
/usr/share/doc/coturn/examples/var/db
/usr/share/doc/coturn/examples/var/db/turndb
/usr/share/doc/coturn/schema.mongo.sh
/usr/share/doc/coturn/schema.sql
/usr/share/doc/coturn/schema.stats.redis
/usr/share/doc/coturn/schema.userdb.redis.gz
/usr/share/doc-base
/usr/share/doc-base/coturn.coturn
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/coturn.1.gz
/usr/share/man/man1/turnadmin.1.gz
/usr/share/man/man1/turnserver.1.gz
/usr/share/man/man1/turnutils.1.gz
/usr/share/man/man1/turnutils_natdiscovery.1.gz
/usr/share/man/man1/turnutils_oauth.1.gz
/usr/share/man/man1/turnutils_peer.1.gz
/usr/share/man/man1/turnutils_stunclient.1.gz
/usr/share/man/man1/turnutils_uclient.1.gz
/var
/var/lib
/var/lib/turn
/usr/bin/coturn
/usr/bin/turnadmin
/usr/bin/turnutils
/usr/share/doc/coturn/examples/etc/cacert.pem
/usr/share/doc/coturn/examples/etc/turn_client_cert.pem
/usr/share/doc/coturn/examples/etc/turn_client_pkey.pem
/usr/share/doc/coturn/examples/etc/turn_server_cert.pem
/usr/share/doc/coturn/examples/etc/turn_server_pkey.pem


## Package : nginx


```text
$ dpkg -L 'nginx' 2>/dev/null || true
```



---

# 32. DÉPENDANCES DES PAQUETS

**Date :** 2026-08-12 20:37:44 EDT


## jitsi-meet


```text
$ apt-cache depends 'jitsi-meet' 2>/dev/null || true
```
jitsi-meet
  PreDepends: jitsi-videobridge2
  Depends: jicofo
  Depends: jitsi-meet-web
  Depends: jitsi-meet-web-config
  Depends: jitsi-meet-prosody
  Recommends: jitsi-meet-turnserver


## jicofo


```text
$ apt-cache depends 'jicofo' 2>/dev/null || true
```
jicofo
 |Depends: debconf
  Depends: <debconf-2.0>
    cdebconf
    debconf
 |Depends: openjdk-17-jre-headless
 |Depends: <openjdk-17-jre>
 |Depends: openjdk-21-jre-headless
  Depends: openjdk-21-jre
  Depends: ruby-hocon
  Depends: jq


## jitsi-videobridge2


```text
$ apt-cache depends 'jitsi-videobridge2' 2>/dev/null || true
```
jitsi-videobridge2
 |PreDepends: openjdk-17-jre-headless
 |PreDepends: <openjdk-17-jre>
 |PreDepends: openjdk-21-jre-headless
  PreDepends: openjdk-21-jre
 |PreDepends: <libssl3>
    libssl3t64
  PreDepends: <libssl1.1>
 |Depends: debconf
  Depends: <debconf-2.0>
    cdebconf
    debconf
  Depends: procps
  Depends: uuid-runtime
  Depends: ruby-hocon
  Conflicts: jitsi-videobridge
  Recommends: <libpcap0.8>
    libpcap0.8t64
  Replaces: jitsi-videobridge


## jitsi-meet-prosody


```text
$ apt-cache depends 'jitsi-meet-prosody' 2>/dev/null || true
```
jitsi-meet-prosody
  Depends: openssl
 |Depends: prosody
 |Depends: <prosody-trunk>
 |Depends: <prosody-0.12>
  Depends: <prosody-13.0>
  Depends: ca-certificates-java
  Depends: lua-sec
  Depends: lua-basexx
  Depends: lua-luaossl
  Depends: lua-cjson
  Depends: lua-inspect
  Replaces: jitsi-meet-tokens


## jitsi-meet-turnserver


```text
$ apt-cache depends 'jitsi-meet-turnserver' 2>/dev/null || true
```
jitsi-meet-turnserver
  PreDepends: jitsi-meet-web-config
 |Depends: debconf
  Depends: <debconf-2.0>
    cdebconf
    debconf
  Depends: jitsi-meet-prosody
  Depends: coturn
  Depends: <dnsutils>
    bind9-dnsutils



---

# 33. VERSIONS EXACTES

**Date :** 2026-08-12 20:37:46 EDT


```text
$ dpkg-query -W -f="${Package} ${Version}\n" 2>/dev/null | grep -Ei "jitsi|jicofo|prosody|coturn" || true
```


```text
$ uname -r
```
6.12.74+deb13+1-amd64


```text
$ cat /etc/os-release
```
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.6
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"


```text
$ java -version 2>&1 || true
```
openjdk version "21.0.12" 2026-07-21
OpenJDK Runtime Environment (build 21.0.12+8-1-deb13u1-Debian)
OpenJDK 64-Bit Server VM (build 21.0.12+8-1-deb13u1-Debian, mixed mode, sharing)


```text
$ node -v 2>/dev/null || true
```


```text
$ prosodyctl --version 2>/dev/null || true
```



---

# 34. RÉSUMÉ AUTOMATIQUE

**Date :** 2026-08-12 20:37:46 EDT


## Services détectés


```text
$ systemctl list-unit-files 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|jvb|coturn|turnserver|nginx" || true
```
coturn.service                                                                enabled         enabled
nginx.service                                                                 masked          enabled


## Ports détectés


```text
$ ss -lntup 2>/dev/null | grep -Ei "java|prosody|nginx|turn|jitsi|node" || true
```


## Processus détectés


```text
$ ps auxww 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|jvb|turnserver|coturn|nginx" | grep -v grep || true
```
civitas     1490  0.0  1.5 1513560 153548 ?      Ssl  19:51   0:00 /usr/bin/xwaylandvideobridge
root        2729  0.0  0.0  25376  9700 ?        Ss   19:52   0:00 nginx: master process nginx -g daemon off;
civitas     3008  0.0  0.0    224    84 ?        S    19:52   0:00 s6-supervise jvb
civitas     3043  0.0  0.0    224    80 ?        S    19:52   0:00 s6-supervise jicofo
civitas     3106  0.0  0.0    224    80 ?        S    19:52   0:00 s6-supervise prosody
civitas     3167  0.0  0.0    224    76 ?        S    19:52   0:00 s6-supervise nginx
tss         3249  0.0  0.0  25916  7856 ?        S    19:52   0:00 nginx: worker process
tss         3250  0.0  0.0  26200  8220 ?        S    19:52   0:00 nginx: worker process
tss         3251  0.0  0.0  25916  7856 ?        S    19:52   0:00 nginx: worker process
tss         3252  0.0  0.0  26172  8004 ?        S    19:52   0:00 nginx: worker process
civitas     3319  0.0  0.2 196988 28596 ?        Ss   19:52   0:00 nginx: master process nginx -c /run/web/config/nginx/nginx.conf
civitas     3326  0.6  2.1 6869116 212992 ?      Ssl  19:52   0:17 java -Xmx3072m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Djava.util.logging.config.file=/run/jicofo/config/logging.properties -Dconfig.file=/run/jicofo/config/jicofo.conf -cp /usr/share/jicofo/jicofo.jar:/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar:/usr/share/jicofo/lib/annotations-23.0.0.jar:/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar:/usr/share/jicofo/lib/commons-lang3-3.12.0.jar:/usr/share/jicofo/lib/config-1.4.3.jar:/usr/share/jicofo/lib/gson-2.8.5.jar:/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar:/usr/share/jicofo/lib/jackson-core-2.18.0.jar:/usr/share/jicofo/lib/jackson-databind-2.18.0.jar:/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar:/usr/share/jicofo/lib/jansi-2.4.1.jar:/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar:/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar:/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar:/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar:/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar:/usr/share/jicofo/lib/jjwt-api-0.12.6.jar:/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar:/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar:/usr/share/jicofo/lib/jna-5.9.0.jar:/usr/share/jicofo/lib/jsr305-3.0.2.jar:/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar:/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar:/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar:/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar:/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar:/usr/share/jicofo/lib/minidns-core-1.0.5.jar:/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar:/usr/share/jicofo/lib/precis-1.1.0.jar:/usr/share/jicofo/lib/sentry-5.4.0.jar:/usr/share/jicofo/lib/simpleclient-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar:/usr/share/jicofo/lib/slf4j-api-1.7.32.jar:/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar:/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar org.jitsi.jicofo.Main
civitas     3344  0.9  2.3 6874456 233876 ?      Ssl  19:52   0:25 java -Xmx3072m -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/run/jvb -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=config -Djava.util.logging.config.file=/run/jvb/config/logging.properties -Dconfig.file=/run/jvb/config/jvb.conf -Djava.io.tmpdir=/run/jvb/tmp -Djna.tmpdir=/run/jvb/tmp -cp /usr/share/jitsi-videobridge/jitsi-videobridge.jar:/usr/share/jitsi-videobridge/lib/* org.jitsi.videobridge.MainKt
civitas     3436  0.0  0.1 197688 12016 ?        S    19:52   0:00 nginx: worker process
civitas     3437  0.0  0.1 197676 11828 ?        S    19:52   0:00 nginx: worker process
civitas     3438  0.0  0.1 197708 12040 ?        S    19:52   0:00 nginx: worker process
civitas     3439  0.0  0.1 197676 11836 ?        S    19:52   0:00 nginx: worker process
civitas     3475  0.1  0.4  85256 46200 ?        Ss   19:52   0:05 lua /usr/bin/prosody --config /run/prosody/config/prosody.cfg.lua -F
root       20184  0.1  0.0  21820  7972 pts/2    S+   20:37   0:00 sudo bash jitsi-infrastructure-audit.sh
root       20188  0.0  0.0  21820  2580 pts/3    Ss   20:37   0:00 sudo bash jitsi-infrastructure-audit.sh
root       20189  1.7  0.0   7208  3436 pts/3    S+   20:37   0:00 bash jitsi-infrastructure-audit.sh
root       22698  0.0  0.0   5576  2032 pts/3    S+   20:37   0:00 tee -a /opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md


---

# FIN DE L'AUDIT

**Date de fin :** 2026-08-12 20:37:46 EDT

## Fichiers générés

- Rapport principal :
  `/opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md`

- Données brutes :
  `/opt/civitas/jitsi-audit/`

## Objectif suivant

À partir de cet inventaire, reconstruire l'architecture Jitsi sous Docker Compose :

```
Internet
   |
   v
Reverse Proxy / Nginx
   |
   +-----------------------+
   |                       |
   v                       v
Jitsi Meet Web          Prosody
                           |
                           +---- Jicofo
                           |
                           +---- JVB
                           |
                           +---- TURN / Coturn
```

L'objectif est de reproduire les fonctionnalités de l'installation actuelle
sans modifier cette dernière pendant la phase d'analyse.

