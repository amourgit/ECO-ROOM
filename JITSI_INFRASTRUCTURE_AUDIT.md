# CIVITAS — Jitsi Infrastructure Audit

> Inventaire de l'installation Jitsi directement installée sur le système.

**Rapport :** `/opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md`

**Répertoire des données brutes :** `/opt/civitas/jitsi-audit`

**Date de début :** 2026-08-08 06:56:23 EDT

> Ce rapport est généré automatiquement.
>
> Le script est conçu pour effectuer des opérations de lecture uniquement.



---

# 1. INFORMATIONS SYSTÈME

**Date :** 2026-08-08 06:56:23 EDT


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
         Boot ID: ea55d1d83e93437491adcc1394ac26f6
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
    Firmware Age: 19y 8month 1w


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
Mem:           9.6Gi       5.5Gi       1.4Gi       115Mi       3.1Gi       4.1Gi
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
tmpfs          tmpfs     984M  2.2M  982M   1% /run
/dev/sda1      ext4       94G   16G   73G  18% /
tmpfs          tmpfs     4.9G     0  4.9G   0% /dev/shm
tmpfs          tmpfs     5.0M  8.0K  5.0M   1% /run/lock
tmpfs          tmpfs     1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
tmpfs          tmpfs     4.9G  180K  4.9G   1% /tmp
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/cce1f25b3d6c6c5cf3a1d39a1007f384b5de528fdd379d1554dbd304ac1dadfa/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/f35a21cc1abf73fbf0bf5d2f605f58572e01251be1ce25ed0dc053ccc20f4394/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/b9592cd4aaa5c942338fa31a1cf6bd8e1b42bbfb5438785728e9b75a1dd1487a/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/a0f56025920b4319eb1d14bf616690289f028535b26238ea655586be37bd28ca/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/5df95633279b56f799e59c925895ba6cb2a0b6ce120d9a7e688f2b93cdc2b57d/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/bb35e187ac16a87c4921b9b7f40ae86309d69510c4f0a22130aecd2369e0adde/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/e564f9ae0b200fe1bbd3f641cb068df2b773e9b475f4d20085fd7ec87ee90781/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/469c4c951ca1c689e4a9fcc34bd30b958ec5e3f39aae3889f4a5155d847bb46e/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/60f17c8eb3af0bd4a590f7147d4b949d0999730953d49e81eaf680cf70f2a4fa/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/1423505fb7ec740a30c6e0ed7a283eea985a94e116a5965f611de4e7cee275e2/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/6e1c4ae069f0ba44b4b1b46f3d956a339cc550fe953144da23922e2d9c22fba1/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/d0c020cb0d3a6f08a26835ca9a44d364b5967c6f79b539258a538dd73a665d9b/merged
overlay        overlay    94G   16G   73G  18% /var/lib/docker/overlay2/36437be6a501c900d9c82f8628b98968a89b6ade763daa0809e74f0d7b4b45cb/merged
tmpfs          tmpfs     984M   96K  984M   1% /run/user/1000



---

# 2. PAQUETS INSTALLÉS

**Date :** 2026-08-08 06:56:23 EDT


## Recherche globale des paquets Jitsi


```text
$ dpkg -l 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|coturn|turnserver|nginx" || true
```
ii  coturn                                              4.6.1-2                              amd64        TURN and STUN server for VoIP
ii  jicofo                                              1.0-1189-1                           all          JItsi Meet COnference FOcus
ii  jitsi-meet                                          2.0.11146-1                          all          WebRTC JavaScript video conferences
ii  jitsi-meet-prosody                                  1.0.9365-1                           all          Prosody configuration for Jitsi Meet
ii  jitsi-meet-turnserver                               1.0.9365-1                           all          Configures coturn to be used with Jitsi Meet
ii  jitsi-meet-web                                      1.0.9365-1                           all          WebRTC JavaScript video conferences
ii  jitsi-meet-web-config                               1.0.9365-1                           all          Configuration for web serving of Jitsi Meet
ii  jitsi-videobridge2                                  2.3-307-g4bb0aead1-1                 all          WebRTC compatible Selective Forwarding Unit (SFU)
ii  lua-basexx                                          0.4.1-jitsi1                         all          baseXX encoding/decoding library for Lua
ii  lua-cjson:amd64                                     2.1.0.10-jitsi1                      amd64        JSON parser/encoder for Lua
ii  nginx                                               1.26.3-3+deb13u7                     amd64        small, powerful, scalable web/proxy server
ii  nginx-common                                        1.26.3-3+deb13u7                     all          small, powerful, scalable web/proxy server - common files
ii  prosody                                             13.0.1-1+deb131u                     amd64        Lightweight Jabber/XMPP server
ii  xwaylandvideobridge                                 0.4.0-2+b1                           amd64        XWayland Video Bridge for X11 clients


## Recherche avec apt


```text
$ apt list --installed 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|coturn|turnserver|nginx" || true
```
coturn/stable,now 4.6.1-2 amd64 [installed]
jicofo/stable,now 1.0-1189-1 all [installed,automatic]
jitsi-meet-prosody/stable,now 1.0.9365-1 all [installed,automatic]
jitsi-meet-turnserver/stable,now 1.0.9365-1 all [installed,automatic]
jitsi-meet-web-config/stable,now 1.0.9365-1 all [installed,automatic]
jitsi-meet-web/stable,now 1.0.9365-1 all [installed,automatic]
jitsi-meet/stable,now 2.0.11146-1 all [installed]
jitsi-videobridge2/stable,now 2.3-307-g4bb0aead1-1 all [installed,automatic]
lua-basexx/stable,now 0.4.1-jitsi1 all [installed,automatic]
lua-cjson/stable,now 2.1.0.10-jitsi1 amd64 [installed,automatic]
nginx-common/stable,stable-security,now 1.26.3-3+deb13u7 all [installed,automatic]
nginx/stable,stable-security,now 1.26.3-3+deb13u7 amd64 [installed,automatic]
prosody/stable,stable-security,now 13.0.1-1+deb131u amd64 [installed,automatic]
xwaylandvideobridge/stable,now 0.4.0-2+b1 amd64 [installed,automatic]


## Versions


```text
$ dpkg-query -W -f="\${Package}\t\${Version}\n" 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|coturn|turnserver" || true
```
coturn	4.6.1-2
jicofo	1.0-1189-1
jitsi-meet	2.0.11146-1
jitsi-meet-prosody	1.0.9365-1
jitsi-meet-turnserver	1.0.9365-1
jitsi-meet-web	1.0.9365-1
jitsi-meet-web-config	1.0.9365-1
jitsi-videobridge2	2.3-307-g4bb0aead1-1
lua-basexx	0.4.1-jitsi1
lua-cjson	2.1.0.10-jitsi1
prosody	13.0.1-1+deb131u
xwaylandvideobridge	0.4.0-2+b1



---

# 3. SERVICES SYSTEMD

**Date :** 2026-08-08 06:56:24 EDT


## Tous les services contenant Jitsi


```text
$ systemctl list-units --type=service --all 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|jvb|videobridge|coturn|turnserver|nginx" || true
```
● coturn.service                              loaded    failed   failed  coTURN STUN/TURN Server
  jicofo.service                              loaded    active   running LSB: Jitsi conference Focus
  jitsi-videobridge2.service                  loaded    active   running Jitsi Videobridge
  nginx.service                               loaded    active   running A high performance web server and a reverse proxy server
  prosody.service                             loaded    active   running Prosody XMPP Server


## Services activés


```text
$ systemctl list-unit-files 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|jvb|videobridge|coturn|turnserver|nginx" || true
```
coturn.service                                                                enabled         enabled
jicofo.service                                                                generated       -
jitsi-videobridge2.service                                                    enabled         enabled
nginx.service                                                                 enabled         enabled
prosody.service                                                               enabled         enabled


## Fichiers systemd


```text
$ find /etc/systemd /lib/systemd /usr/lib/systemd -type f 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|jvb|videobridge|coturn|turnserver" || true
```
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf
/lib/systemd/system/jitsi-videobridge2.service
/lib/systemd/system/coturn.service
/lib/systemd/system/prosody.service
/usr/lib/systemd/system/jitsi-videobridge2.service
/usr/lib/systemd/system/coturn.service
/usr/lib/systemd/system/prosody.service


## Détails des services


### Service : prosody

```text
$ systemctl status prosody --no-pager
```
● prosody.service - Prosody XMPP Server
     Loaded: loaded (/usr/lib/systemd/system/prosody.service; enabled; preset: enabled)
     Active: active (running) since Fri 2026-08-07 05:25:31 EDT; 1 day 1h ago
 Invocation: 7d65306fc6d445fbb87a632a854502c5
       Docs: https://prosody.im/doc
   Main PID: 1161 (lua5.4)
      Tasks: 1 (limit: 11719)
     Memory: 23.4M (peak: 25.4M)
        CPU: 1min 5.365s
     CGroup: /system.slice/prosody.service
             └─1161 lua5.4 /usr/bin/prosody -F

Aug 07 05:25:31 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Aug 07 05:25:31 meet.civitas.local prosody[1161]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Aug 07 05:25:31 meet.civitas.local prosody[1161]: modulemanager: Unable to load module 'room_metadata': /usr/lib/prosody/modules/share/lua/5.4/mod_room_metadata/mod_room_metadata.lua: No such file or directory
Aug 07 05:25:31 meet.civitas.local prosody[1161]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Aug 07 05:25:31 meet.civitas.local prosody[1161]: modulemanager: Unable to load module 'av_moderation': /usr/lib/prosody/modules/share/lua/5.4/mod_av_moderation/mod_av_moderation.lua: No such file or directory
Aug 07 05:25:31 meet.civitas.local prosody[1161]: modulemanager: Unable to load module 'speakerstats': /usr/lib/prosody/modules/share/lua/5.4/mod_speakerstats/mod_speakerstats.lua: No such file or directory
Aug 07 05:25:31 meet.civitas.local prosody[1161]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Aug 07 05:25:31 meet.civitas.local prosody[1161]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config


```text
$ systemctl cat prosody
```
# /usr/lib/systemd/system/prosody.service
[Unit]
### see man systemd.unit
Description=Prosody XMPP Server
After=network-online.target nss-lookup.target remote-fs.target postgresql.service mariadb.service mysql.service
Wants=network-online.target
Documentation=https://prosody.im/doc

[Service]
### See man systemd.service ###
# With this configuration, systemd takes care of daemonization
# so Prosody should be configured with daemonize = false
Type=simple

# Not sure if this is needed for 'simple'
RuntimeDirectory=prosody
PIDFile=/run/prosody/prosody.pid

# Start by executing the main executable
# Note: -F option requires Prosody 0.11.5 or later
ExecStart=/usr/bin/prosody -F

ExecReload=/bin/kill -HUP $MAINPID

# Restart on crashes
Restart=on-abnormal

# Set O_NONBLOCK flag on sockets passed via socket activation
NonBlocking=true

### See man systemd.exec ###

WorkingDirectory=/var/lib/prosody

User=prosody
Group=prosody

# Nice=0

# Set stdin to /dev/null since Prosody does not need it
StandardInput=null

# Direct stdout/-err to journald for use with log = "*stdout"
StandardOutput=journal
StandardError=inherit

# This usually defaults to 4k or so
# LimitNOFILE=1M

## Interesting protection methods
# Finding a useful combo of these settings would be nice
#
# Needs read access to /etc/prosody for config
# Needs write access to /var/lib/prosody for storing data (for internal storage)
# Needs write access to /var/log/prosody for writing logs (depending on config)
# Needs read access to code and libraries loaded

# ReadWriteDirectories=/var/lib/prosody /var/log/prosody
# InaccessibleDirectories=/boot /home /media /mnt /root /srv
# ReadOnlyDirectories=/usr /etc/prosody

# PrivateTmp=true
# PrivateDevices=true
# PrivateNetwork=false

# ProtectSystem=full
# ProtectHome=true
# ProtectKernelTunables=true
# ProtectControlGroups=true
# SystemCallFilter=

# This should break LuaJIT
# MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target


### Service : jicofo

```text
$ systemctl status jicofo --no-pager
```
● jicofo.service - LSB: Jitsi conference Focus
     Loaded: loaded (/etc/init.d/jicofo; generated)
     Active: active (running) since Fri 2026-08-07 05:25:27 EDT; 1 day 1h ago
 Invocation: 58fa6f5e50ba41e79878f53f2a0a1c9b
       Docs: man:systemd-sysv-generator(8)
    Process: 748 ExecStart=/etc/init.d/jicofo start (code=exited, status=0/SUCCESS)
      Tasks: 37 (limit: 11719)
     Memory: 256.6M (peak: 263.8M)
        CPU: 51.888s
     CGroup: /system.slice/jicofo.service
             └─786 java -Xmx3072m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=jicofo -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/jicofo/logging.properties -Dconfig.file=/etc/jitsi/jicofo/jicofo.conf -cp /usr/share/jicofo/jicofo.jar:/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar:/usr/share/jicofo/lib/annotations-23.0.0.jar:/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar:/usr/share/jicofo/lib/commons-lang3-3.12.0.jar:/usr/share/jicofo/lib/config-1.4.3.jar:/usr/share/jicofo/lib/gson-2.8.5.jar:/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar:/usr/share/jicofo/lib/jackson-core-2.18.0.jar:/usr/share/jicofo/lib/jackson-databind-2.18.0.jar:/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar:/usr/share/jicofo/lib/jansi-2.4.1.jar:/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar:/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar:/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar:/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar:/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar:/usr/share/jicofo/lib/jjwt-api-0.12.6.jar:/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar:/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar:/usr/share/jicofo/lib/jna-5.9.0.jar:/usr/share/jicofo/lib/jsr305-3.0.2.jar:/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar:/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar:/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar:/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar:/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar:/usr/share/jicofo/lib/minidns-core-1.0.5.jar:/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar:/usr/share/jicofo/lib/precis-1.1.0.jar:/usr/share/jicofo/lib/sentry-5.4.0.jar:/usr/share/jicofo/lib/simpleclient-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar:/usr/share/jicofo/lib/slf4j-api-1.7.32.jar:/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar:/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar org.jitsi.jicofo.Main

Aug 07 05:25:27 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Aug 07 05:25:27 meet.civitas.local jicofo[748]: Starting jicofo: jicofo started.
Aug 07 05:25:27 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.


```text
$ systemctl cat jicofo
```
# /run/systemd/generator.late/jicofo.service
# Automatically generated by systemd-sysv-generator

[Unit]
Documentation=man:systemd-sysv-generator(8)
SourcePath=/etc/init.d/jicofo
Description=LSB: Jitsi conference Focus
Before=multi-user.target
Before=multi-user.target
Before=multi-user.target
Before=graphical.target
After=remote-fs.target

[Service]
Type=forking
Restart=no
TimeoutSec=5min
IgnoreSIGPIPE=no
KillMode=process
GuessMainPID=no
RemainAfterExit=yes
SuccessExitStatus=5 6
ExecStart=/etc/init.d/jicofo start
ExecStop=/etc/init.d/jicofo stop
ExecReload=/etc/init.d/jicofo reload


### Service : jitsi-videobridge2

```text
$ systemctl status jitsi-videobridge2 --no-pager
```
● jitsi-videobridge2.service - Jitsi Videobridge
     Loaded: loaded (/usr/lib/systemd/system/jitsi-videobridge2.service; enabled; preset: enabled)
    Drop-In: /etc/systemd/system/jitsi-videobridge2.service.d
             └─override.conf
     Active: active (running) since Fri 2026-08-07 05:25:31 EDT; 1 day 1h ago
 Invocation: a874d1f62f09442dbb84e8c7f0d5b7f6
    Process: 1163 ExecStartPost=/bin/bash -c echo $MAINPID > /var/run/jitsi-videobridge/jitsi-videobridge.pid (code=exited, status=0/SUCCESS)
   Main PID: 1162 (java)
      Tasks: 52 (limit: 65000)
     Memory: 250.1M (peak: 260.1M)
        CPU: 1min 20.864s
     CGroup: /system.slice/jitsi-videobridge2.service
             └─1162 java -Xmx3072m -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dconfig.file=/etc/jitsi/videobridge/jvb.conf -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=videobridge -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/videobridge/logging.properties -cp "/usr/share/jitsi-videobridge/jitsi-videobridge.jar:/usr/share/jitsi-videobridge/lib/*" org.jitsi.videobridge.MainKt

Aug 07 05:25:31 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 07 05:25:31 meet.civitas.local (bash)[1162]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Aug 07 05:25:31 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.


```text
$ systemctl cat jitsi-videobridge2
```
# /usr/lib/systemd/system/jitsi-videobridge2.service
[Unit]
Description=Jitsi Videobridge
After=network-online.target
Wants=network-online.target

[Service]
SuccessExitStatus=143
# configuration error prevents restart loops
RestartPreventExitStatus=78
# allow bind to 80 and 443
AmbientCapabilities=CAP_NET_BIND_SERVICE
EnvironmentFile=/etc/jitsi/videobridge/config
Environment=LOGFILE=/var/log/jitsi/jvb.log
User=jvb
RuntimeDirectory=jitsi-videobridge
RuntimeDirectoryMode=0750
PIDFile=/var/run/jitsi-videobridge/jitsi-videobridge.pid
# more threads for this process
TasksMax=65000
# allow more open files for this process
LimitNPROC=65000
LimitNOFILE=65000
ExecStart=/bin/bash -c "exec /usr/share/jitsi-videobridge/jvb.sh ${JVB_OPTS} < /dev/null >> ${LOGFILE} 2>&1"
ExecStartPost=/bin/bash -c "echo $MAINPID > /var/run/jitsi-videobridge/jitsi-videobridge.pid"
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target

# /etc/systemd/system/jitsi-videobridge2.service.d/override.conf
[Unit]
# S'assurer que Prosody et le réseau sont prêts avant JVB
After=network-online.target prosody.service jicofo.service
Requires=network-online.target prosody.service

[Service]
# Redémarrer automatiquement si crash
Restart=on-failure
RestartSec=10
# Attendre jusqu'à 3 minutes au boot
TimeoutStartSec=180


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
     Active: failed (Result: exit-code) since Fri 2026-08-07 05:25:29 EDT; 1 day 1h ago
 Invocation: bbf5ccc9e1d84d7f932b7407b0480faa
       Docs: man:coturn(1)
             man:turnadmin(1)
             man:turnserver(1)
    Process: 1056 ExecStart=/usr/bin/turnserver -c /etc/turnserver.conf --pidfile= (code=exited, status=255/EXCEPTION)
   Main PID: 1056 (code=exited, status=255/EXCEPTION)

Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot start TLS and DTLS listeners because private key file is not set properly
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : NO EXPLICIT LISTENER ADDRESS(ES) ARE CONFIGURED
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : ===========Discovering listener addresses: =========
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Listener address to use: 127.0.0.1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Listener address to use: ::1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : ERROR: main: Cannot configure any meaningful IP listener address
Aug 07 05:25:29 meet.civitas.local systemd[1]: coturn.service: Scheduled restart job, restart counter is at 5.
Aug 07 05:25:29 meet.civitas.local systemd[1]: coturn.service: Start request repeated too quickly.
Aug 07 05:25:29 meet.civitas.local systemd[1]: coturn.service: Failed with result 'exit-code'.
Aug 07 05:25:29 meet.civitas.local systemd[1]: Failed to start coturn.service - coTURN STUN/TURN Server.


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
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: enabled)
     Active: active (running) since Fri 2026-08-07 05:25:31 EDT; 1 day 1h ago
 Invocation: 3ddfc18dbb1b46a7b05da931eb39030d
       Docs: man:nginx(8)
    Process: 1160 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Process: 1189 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
   Main PID: 1194 (nginx)
      Tasks: 5 (limit: 11719)
     Memory: 10M (peak: 10.7M)
        CPU: 225ms
     CGroup: /system.slice/nginx.service
             ├─1194 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             ├─1195 "nginx: worker process"
             ├─1197 "nginx: worker process"
             ├─1198 "nginx: worker process"
             └─1199 "nginx: worker process"

Aug 07 05:25:31 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Aug 07 05:25:31 meet.civitas.local nginx[1160]: 2026/08/07 05:25:31 [warn] 1160#1160: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 07 05:25:31 meet.civitas.local nginx[1160]: 2026/08/07 05:25:31 [warn] 1160#1160: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 07 05:25:31 meet.civitas.local nginx[1160]: 2026/08/07 05:25:31 [warn] 1160#1160: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 07 05:25:31 meet.civitas.local nginx[1189]: 2026/08/07 05:25:31 [warn] 1189#1189: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 07 05:25:31 meet.civitas.local nginx[1189]: 2026/08/07 05:25:31 [warn] 1189#1189: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 07 05:25:31 meet.civitas.local nginx[1189]: 2026/08/07 05:25:31 [warn] 1189#1189: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 07 05:25:31 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.


```text
$ systemctl cat nginx
```
# /usr/lib/systemd/system/nginx.service
# Stop dance for nginx
# =======================
#
# ExecStop sends SIGQUIT (graceful stop) to the nginx process.
# If, after 5s (--retry QUIT/5) nginx is still running, systemd takes control
# and sends SIGTERM (fast shutdown) to the main process.
# After another 5s (TimeoutStopSec=5), and if nginx is alive, systemd sends
# SIGKILL to all the remaining processes in the process group (KillMode=mixed).
#
# nginx signals reference doc:
# http://nginx.org/en/docs/control.html
#
[Unit]
Description=A high performance web server and a reverse proxy server
Documentation=man:nginx(8)
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target
ConditionFileIsExecutable=/usr/sbin/nginx

[Service]
Type=forking
PIDFile=/run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t -q -g 'daemon on; master_process on;'
ExecStart=/usr/sbin/nginx -g 'daemon on; master_process on;'
ExecReload=/usr/sbin/nginx -g 'daemon on; master_process on;' -s reload
ExecStop=-/sbin/start-stop-daemon --quiet --stop --retry QUIT/5 --pidfile /run/nginx.pid
TimeoutStopSec=5
KillMode=mixed

[Install]
WantedBy=multi-user.target



---

# 4. PROSODY

**Date :** 2026-08-08 06:56:25 EDT


## Binaire


```text
$ command -v prosody 2>/dev/null || true
```
/usr/bin/prosody


```text
$ prosodyctl --version 2>/dev/null || true
```
prosodyctl - Manage a Prosody server

Usage: /usr/bin/prosodyctl COMMAND [OPTIONS]

Where COMMAND may be one of:

Process management:
 reload            Reload Prosody's configuration and re-open log files
 status            Reports the running status of Prosody
 shell             Interact with a running Prosody

User management:
 adduser JID       Create the specified user account in Prosody
 passwd JID        Set the password for the specified user account in Prosody
 deluser JID       Permanently remove the specified user account from Prosody

Plugin management:
 install           Installs a prosody/luarocks plugin
 remove            Removes a module installed in the working directory's plugins folder
 list              Shows installed rocks

Informative:
 check             Perform basic checks on your Prosody installation
 version [-v]      Show current Prosody version, or more

Other:
 cert              Certificate management commands
 about             Show information about this Prosody installation


## Répertoires Prosody


```text
$ find /etc/prosody /usr/lib/prosody /usr/share/prosody /var/lib/prosody /var/log/prosody -maxdepth 4 -print 2>/dev/null || true
```
/etc/prosody
/etc/prosody/README
/etc/prosody/certs
/etc/prosody/certs/meet.civitas.local.key
/etc/prosody/certs/auth.meet.civitas.local.crt
/etc/prosody/certs/meet.civitas.local.crt
/etc/prosody/certs/auth.meet.civitas.local.key
/etc/prosody/migrator.cfg.lua
/etc/prosody/conf.d
/etc/prosody/conf.d/localhost.cfg.lua
/etc/prosody/conf.d/meet.civitas.local.cfg.lua
/etc/prosody/conf.avail
/etc/prosody/conf.avail/example.com.cfg.lua
/etc/prosody/conf.avail/localhost.cfg.lua
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua
/etc/prosody/conf.avail/jaas.cfg.lua
/etc/prosody/prosody.cfg.lua
/usr/lib/prosody
/usr/lib/prosody/net
/usr/lib/prosody/net/dns.lua
/usr/lib/prosody/net/server.lua
/usr/lib/prosody/net/adns.lua
/usr/lib/prosody/net/http
/usr/lib/prosody/net/http/parser.lua
/usr/lib/prosody/net/http/server.lua
/usr/lib/prosody/net/http/errors.lua
/usr/lib/prosody/net/http/files.lua
/usr/lib/prosody/net/http/codes.lua
/usr/lib/prosody/net/server_epoll.lua
/usr/lib/prosody/net/server_event.lua
/usr/lib/prosody/net/server_select.lua
/usr/lib/prosody/net/connect.lua
/usr/lib/prosody/net/stun.lua
/usr/lib/prosody/net/tls_luasec.lua
/usr/lib/prosody/net/cqueues.lua
/usr/lib/prosody/net/unbound.lua
/usr/lib/prosody/net/websocket
/usr/lib/prosody/net/websocket/frames.lua
/usr/lib/prosody/net/websocket.lua
/usr/lib/prosody/net/resolvers
/usr/lib/prosody/net/resolvers/service.lua
/usr/lib/prosody/net/resolvers/basic.lua
/usr/lib/prosody/net/resolvers/chain.lua
/usr/lib/prosody/net/resolvers/manual.lua
/usr/lib/prosody/net/http.lua
/usr/lib/prosody/core
/usr/lib/prosody/core/moduleapi.lua
/usr/lib/prosody/core/hostmanager.lua
/usr/lib/prosody/core/storagemanager.lua
/usr/lib/prosody/core/modulemanager.lua
/usr/lib/prosody/core/loggingmanager.lua
/usr/lib/prosody/core/stanza_router.lua
/usr/lib/prosody/core/portmanager.lua
/usr/lib/prosody/core/rostermanager.lua
/usr/lib/prosody/core/statsmanager.lua
/usr/lib/prosody/core/sessionmanager.lua
/usr/lib/prosody/core/features.lua
/usr/lib/prosody/core/s2smanager.lua
/usr/lib/prosody/core/configmanager.lua
/usr/lib/prosody/core/certmanager.lua
/usr/lib/prosody/core/usermanager.lua
/usr/lib/prosody/modules
/usr/lib/prosody/modules/mod_vcard.lua
/usr/lib/prosody/modules/mod_muc_mam.lua
/usr/lib/prosody/modules/mod_admin_adhoc.lua
/usr/lib/prosody/modules/mod_uptime.lua
/usr/lib/prosody/modules/mod_http.lua
/usr/lib/prosody/modules/mod_csi_simple.lua
/usr/lib/prosody/modules/mod_http_files.lua
/usr/lib/prosody/modules/mod_http_altconnect.lua
/usr/lib/prosody/modules/mod_storage_xep0227.lua
/usr/lib/prosody/modules/mod_vcard4.lua
/usr/lib/prosody/modules/mod_account_activity.lua
/usr/lib/prosody/modules/mod_flags.lua
/usr/lib/prosody/modules/mod_dialback.lua
/usr/lib/prosody/modules/mod_version.lua
/usr/lib/prosody/modules/mod_announce.lua
/usr/lib/prosody/modules/mod_net_multiplex.lua
/usr/lib/prosody/modules/mod_blocklist.lua
/usr/lib/prosody/modules/mod_time.lua
/usr/lib/prosody/modules/mod_tls.lua
/usr/lib/prosody/modules/mod_saslauth.lua
/usr/lib/prosody/modules/mod_proxy65.lua
/usr/lib/prosody/modules/mod_tokenauth.lua
/usr/lib/prosody/modules/mod_admin_socket.lua
/usr/lib/prosody/modules/mod_storage_memory.lua
/usr/lib/prosody/modules/mod_bosh.lua
/usr/lib/prosody/modules/mod_roster.lua
/usr/lib/prosody/modules/muc
/usr/lib/prosody/modules/muc/hidden.lib.lua
/usr/lib/prosody/modules/muc/subject.lib.lua
/usr/lib/prosody/modules/muc/name.lib.lua
/usr/lib/prosody/modules/muc/whois.lib.lua
/usr/lib/prosody/modules/muc/history.lib.lua
/usr/lib/prosody/modules/muc/mod_muc.lua
/usr/lib/prosody/modules/muc/hats.lib.lua
/usr/lib/prosody/modules/muc/config_form_sections.lib.lua
/usr/lib/prosody/modules/muc/occupant_id.lib.lua
/usr/lib/prosody/modules/muc/moderated.lib.lua
/usr/lib/prosody/modules/muc/persistent.lib.lua
/usr/lib/prosody/modules/muc/language.lib.lua
/usr/lib/prosody/modules/muc/presence_broadcast.lib.lua
/usr/lib/prosody/modules/muc/request.lib.lua
/usr/lib/prosody/modules/muc/password.lib.lua
/usr/lib/prosody/modules/muc/vcard.lib.lua
/usr/lib/prosody/modules/muc/members_only.lib.lua
/usr/lib/prosody/modules/muc/description.lib.lua
/usr/lib/prosody/modules/muc/util.lib.lua
/usr/lib/prosody/modules/muc/lock.lib.lua
/usr/lib/prosody/modules/muc/register.lib.lua
/usr/lib/prosody/modules/muc/occupant.lib.lua
/usr/lib/prosody/modules/muc/restrict_pm.lib.lua
/usr/lib/prosody/modules/muc/muc.lib.lua
/usr/lib/prosody/modules/mod_auth_anonymous.lua
/usr/lib/prosody/modules/mod_authz_internal.lua
/usr/lib/prosody/modules/mod_carbons.lua
/usr/lib/prosody/modules/mod_auth_insecure.lua
/usr/lib/prosody/modules/mod_mimicking.lua
/usr/lib/prosody/modules/mod_groups.lua
/usr/lib/prosody/modules/mod_s2s_auth_certs.lua
/usr/lib/prosody/modules/mod_smacks.lua
/usr/lib/prosody/modules/mod_cron.lua
/usr/lib/prosody/modules/mod_unknown.lua
/usr/lib/prosody/modules/mod_s2s.lua
/usr/lib/prosody/modules/mod_http_errors.lua
/usr/lib/prosody/modules/mod_windows.lua
/usr/lib/prosody/modules/mod_server_contact_info.lua
/usr/lib/prosody/modules/mod_storage_sql.lua
/usr/lib/prosody/modules/mod_component.lua
/usr/lib/prosody/modules/mod_turn_external.lua
/usr/lib/prosody/modules/mod_storage_none.lua
/usr/lib/prosody/modules/mod_pep.lua
/usr/lib/prosody/modules/mod_vcard_legacy.lua
/usr/lib/prosody/modules/mod_lastactivity.lua
/usr/lib/prosody/modules/mod_auth_internal_plain.lua
/usr/lib/prosody/modules/mod_debug_reset.lua
/usr/lib/prosody/modules/mod_storage_internal.lua
/usr/lib/prosody/modules/mod_scansion_record.lua
/usr/lib/prosody/modules/mod_disco.lua
/usr/lib/prosody/modules/mod_invites.lua
/usr/lib/prosody/modules/mod_s2s_bidi.lua
/usr/lib/prosody/modules/mod_s2s_auth_dane_in.lua
/usr/lib/prosody/modules/mod_http_file_share.lua
/usr/lib/prosody/modules/mod_auth_ldap.lua
/usr/lib/prosody/modules/mod_ping.lua
/usr/lib/prosody/modules/mod_cloud_notify.lua
/usr/lib/prosody/modules/mod_http_openmetrics.lua
/usr/lib/prosody/modules/mod_iq.lua
/usr/lib/prosody/modules/mod_message.lua
/usr/lib/prosody/modules/mod_register.lua
/usr/lib/prosody/modules/mod_legacyauth.lua
/usr/lib/prosody/modules/mod_pep_simple.lua
/usr/lib/prosody/modules/mod_invites_adhoc.lua
/usr/lib/prosody/modules/mod_stanza_debug.lua
/usr/lib/prosody/modules/mod_welcome.lua
/usr/lib/prosody/modules/mod_register_ibr.lua
/usr/lib/prosody/modules/mod_server_info.lua
/usr/lib/prosody/modules/mod_muc_unique.lua
/usr/lib/prosody/modules/adhoc
/usr/lib/prosody/modules/adhoc/adhoc.lib.lua
/usr/lib/prosody/modules/adhoc/mod_adhoc.lua
/usr/lib/prosody/modules/mod_pubsub
/usr/lib/prosody/modules/mod_pubsub/pubsub.lib.lua
/usr/lib/prosody/modules/mod_pubsub/commands.lib.lua
/usr/lib/prosody/modules/mod_pubsub/mod_pubsub.lua
/usr/lib/prosody/modules/mod_c2s.lua
/usr/lib/prosody/modules/mod_motd.lua
/usr/lib/prosody/modules/mod_websocket.lua
/usr/lib/prosody/modules/mod_debug_stanzas
/usr/lib/prosody/modules/mod_debug_stanzas/watcher.lib.lua
/usr/lib/prosody/modules/mod_watchregistrations.lua
/usr/lib/prosody/modules/mod_user_account_management.lua
/usr/lib/prosody/modules/mod_admin_telnet.lua
/usr/lib/prosody/modules/mod_posix.lua
/usr/lib/prosody/modules/mod_offline.lua
/usr/lib/prosody/modules/mod_admin_shell.lua
/usr/lib/prosody/modules/mod_auth_internal_hashed.lua
/usr/lib/prosody/modules/mod_private.lua
/usr/lib/prosody/modules/mod_tombstones.lua
/usr/lib/prosody/modules/mod_bookmarks.lua
/usr/lib/prosody/modules/mod_pep_plus.lua
/usr/lib/prosody/modules/mod_external_services.lua
/usr/lib/prosody/modules/mod_limits.lua
/usr/lib/prosody/modules/mod_csi.lua
/usr/lib/prosody/modules/mod_presence.lua
/usr/lib/prosody/modules/mod_invites_register.lua
/usr/lib/prosody/modules/mod_debug_sql.lua
/usr/lib/prosody/modules/mod_mam
/usr/lib/prosody/modules/mod_mam/mamprefs.lib.lua
/usr/lib/prosody/modules/mod_mam/mamprefsxml.lib.lua
/usr/lib/prosody/modules/mod_mam/mod_mam.lua
/usr/lib/prosody/modules/mod_register_limits.lua
/usr/lib/prosody/prosody.version
/usr/lib/prosody/util
/usr/lib/prosody/util/dataforms.lua
/usr/lib/prosody/util/timer.lua
/usr/lib/prosody/util/rsm.lua
/usr/lib/prosody/util/xtemplate.lua
/usr/lib/prosody/util/stanza.lua
/usr/lib/prosody/util/template.lua
/usr/lib/prosody/util/openmetrics.lua
/usr/lib/prosody/util/openssl.lua
/usr/lib/prosody/util/jsonpointer.lua
/usr/lib/prosody/util/dns.lua
/usr/lib/prosody/util/array.lua
/usr/lib/prosody/util/statistics.lua
/usr/lib/prosody/util/roles.lua
/usr/lib/prosody/util/gc.lua
/usr/lib/prosody/util/signal.so
/usr/lib/prosody/util/paseto.lua
/usr/lib/prosody/util/sql.lua
/usr/lib/prosody/util/envload.lua
/usr/lib/prosody/util/datamapper.lua
/usr/lib/prosody/util/smqueue.lua
/usr/lib/prosody/util/iterators.lua
/usr/lib/prosody/util/paths.lua
/usr/lib/prosody/util/events.lua
/usr/lib/prosody/util/sslconfig.lua
/usr/lib/prosody/util/poll.so
/usr/lib/prosody/util/mathcompat.lua
/usr/lib/prosody/util/sqlite3.lua
/usr/lib/prosody/util/net.so
/usr/lib/prosody/util/hashring.lua
/usr/lib/prosody/util/human
/usr/lib/prosody/util/human/io.lua
/usr/lib/prosody/util/human/units.lua
/usr/lib/prosody/util/id.lua
/usr/lib/prosody/util/throttle.lua
/usr/lib/prosody/util/argparse.lua
/usr/lib/prosody/util/promise.lua
/usr/lib/prosody/util/bit53.lua
/usr/lib/prosody/util/format.lua
/usr/lib/prosody/util/debug.lua
/usr/lib/prosody/util/bitcompat.lua
/usr/lib/prosody/util/session.lua
/usr/lib/prosody/util/table.so
/usr/lib/prosody/util/dnsregistry.lua
/usr/lib/prosody/util/dbuffer.lua
/usr/lib/prosody/util/hex.lua
/usr/lib/prosody/util/async.lua
/usr/lib/prosody/util/pluginloader.lua
/usr/lib/prosody/util/time.so
/usr/lib/prosody/util/xml.lua
/usr/lib/prosody/util/queue.lua
/usr/lib/prosody/util/startup.lua
/usr/lib/prosody/util/hashes.so
/usr/lib/prosody/util/xpcall.lua
/usr/lib/prosody/util/set.lua
/usr/lib/prosody/util/caps.lua
/usr/lib/prosody/util/prosodyctl.lua
/usr/lib/prosody/util/multitable.lua
/usr/lib/prosody/util/crypto.so
/usr/lib/prosody/util/compat.so
/usr/lib/prosody/util/presence.lua
/usr/lib/prosody/util/ringbuffer.so
/usr/lib/prosody/util/erlparse.lua
/usr/lib/prosody/util/interpolation.lua
/usr/lib/prosody/util/logger.lua
/usr/lib/prosody/util/serialization.lua
/usr/lib/prosody/util/xmppstream.lua
/usr/lib/prosody/util/x509.lua
/usr/lib/prosody/util/sasl
/usr/lib/prosody/util/sasl/external.lua
/usr/lib/prosody/util/sasl/oauthbearer.lua
/usr/lib/prosody/util/sasl/anonymous.lua
/usr/lib/prosody/util/sasl/plain.lua
/usr/lib/prosody/util/sasl/scram.lua
/usr/lib/prosody/util/watchdog.lua
/usr/lib/prosody/util/pposix.so
/usr/lib/prosody/util/random.lua
/usr/lib/prosody/util/json.lua
/usr/lib/prosody/util/mercurial.lua
/usr/lib/prosody/util/jsonschema.lua
/usr/lib/prosody/util/fsm.lua
/usr/lib/prosody/util/jwt.lua
/usr/lib/prosody/util/hmac.lua
/usr/lib/prosody/util/import.lua
/usr/lib/prosody/util/cache.lua
/usr/lib/prosody/util/adminstream.lua
/usr/lib/prosody/util/jid.lua
/usr/lib/prosody/util/error.lua
/usr/lib/prosody/util/indexedbheap.lua
/usr/lib/prosody/util/prosodyctl
/usr/lib/prosody/util/prosodyctl/cert.lua
/usr/lib/prosody/util/prosodyctl/shell.lua
/usr/lib/prosody/util/prosodyctl/check.lua
/usr/lib/prosody/util/termcolours.lua
/usr/lib/prosody/util/adhoc.lua
/usr/lib/prosody/util/filters.lua
/usr/lib/prosody/util/pubsub.lua
/usr/lib/prosody/util/helpers.lua
/usr/lib/prosody/util/statsd.lua
/usr/lib/prosody/util/dependencies.lua
/usr/lib/prosody/util/sasl.lua
/usr/lib/prosody/util/uuid.lua
/usr/lib/prosody/util/datetime.lua
/usr/lib/prosody/util/encodings.so
/usr/lib/prosody/util/datamanager.lua
/usr/lib/prosody/util/struct.so
/usr/lib/prosody/util/ip.lua
/usr/lib/prosody/util/strbitop.so
/usr/lib/prosody/util/http.lua
/usr/lib/prosody/loader.lua
/var/lib/prosody
/var/lib/prosody/meet%2ecivitas%2elocal
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/8058a145%2d1ee5%2d4d9a%2d949c%2d86cdd8552ebb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/5fc3334a%2d8085%2d4609%2d8f37%2d474dea332028.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/62cc2459%2d0b9b%2d4b46%2d8cd9%2d17f2a920b417.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/7f49d7a9%2d1606%2d4646%2d927d%2d25c529c622f4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/f3bc7584%2dd808%2d4734%2d8b34%2d207d36e412f2.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/12665ee2%2d488d%2d4871%2d8afe%2d2e74a7c58fd2.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/e7c59026%2db739%2d4456%2dbf3b%2df0720c4ae40e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/cd92958e%2dbb31%2d4480%2d9ca8%2d03f249662a1e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/bb17de8c%2db394%2d46cb%2d9b0e%2d585ca62c79f0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/3587fa7e%2d99d4%2d4e71%2dbaea%2d1fe926f9a887.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/d194017b%2d5843%2d439f%2db0d1%2dc093df5e41c5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/0eecc217%2dfa1c%2d4654%2dbfee%2da3f9a4a38179.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/f637a0c1%2d28f4%2d47a5%2db852%2d7b80384fc2c4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/653f7066%2d9792%2d41bb%2da921%2de348d992c8c7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/c6b4504b%2d862d%2d44fc%2d9df6%2d68e5178b10d5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/6b01d1f5%2d1435%2d46ce%2d8c68%2d52a227349b04.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/b4f83f9b%2ddf86%2d4bc1%2db8e5%2d858cfbf78bb6.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/df8a809c%2de960%2d4077%2d8338%2dcffd69937874.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/3277d864%2d2be9%2d4153%2d800b%2daee4e8c55d0b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/481a6a0e%2d4b78%2d43c0%2dac24%2da67813260faf.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/f469cc08%2dc01d%2d4d9e%2d88ed%2d2b0e7b41f788.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/949a07c4%2dde79%2d4112%2d964f%2d14ada1024210.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/4110c797%2dd3ff%2d47c4%2d86e5%2da74701c75e16.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/8044bf48%2dd6b4%2d4f61%2d8269%2d56edf001209f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/ed09c322%2dc342%2d494b%2d8d8b%2d2d66fa9d768e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/0acea27b%2de3d4%2d4cc4%2db735%2d514d1c639017.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/4ae8ad62%2da4ec%2d4187%2da312%2de1562c7291b8.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/099347ec%2d34bb%2d45bb%2dab76%2d7de6786546fa.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/8d33e1d6%2d7393%2d4bf4%2d81e5%2da16c4a28ff55.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/be3e692c%2dc57f%2d48d0%2d85ca%2dc1c6309c9bc7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/9543cecd%2dfcb4%2d4614%2dbba4%2db448009cc18f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/fe635a56%2d9310%2d4480%2d9c6a%2d9416ff619644.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/bf83bd47%2dfc72%2d4176%2daa4e%2dc7feea6314e3.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/4e9ad804%2daaf9%2d4935%2dbd88%2d9ceee1410006.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/155e33c9%2d13cb%2d4850%2da3bc%2d5033fbb94aa8.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/9e7a0392%2d921a%2d41ba%2d8b62%2d959c4420d589.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/715eea4f%2dd17a%2d49e4%2d93f6%2d531a9870935a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/a536f7fe%2d0f10%2d48c0%2d9059%2d3f4f2b21b651.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/ff74c6af%2d7a25%2d4cbd%2da116%2d001b6a312869.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/88b775ea%2d2392%2d44ae%2d8d2e%2d81a2081d8ed5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/8ebc7209%2d0199%2d4b99%2d9302%2d100b77c6375e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/8a0878e4%2df4f5%2d4a7e%2d9fc3%2d1079422fe1b0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/9c018a65%2d640d%2d4554%2da72f%2d5cb7fe62cd36.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/8750a3c4%2d58c5%2d4114%2d962b%2d93b558e9df24.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/92fac3d4%2d9745%2d4e15%2dac2d%2d474e067d2a63.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/6fbd8b62%2de8d7%2d4302%2d9ec6%2d582203c3b0c0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/bcfefbde%2df47c%2d4a28%2db445%2d698d201d2e2d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/dda2e365%2d72b7%2d469d%2d95b3%2d15c54d3acc57.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/3730688d%2df5fa%2d498e%2dac40%2d450da7e18309.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/699993f3%2ddff9%2d4ad4%2db846%2deae84aaf5f8b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/1dedc4f1%2d81e6%2d46d8%2d8050%2d5fea77cca88a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/f62169ed%2d67ad%2d40ce%2db47e%2d79e1ed291a9c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/e87520bc%2def28%2d49b7%2d96cf%2d4ebb1de070c9.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/7d1550fb%2dabb8%2d43fa%2d8e96%2dfd988cfad5d7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/f002af29%2d039c%2d4395%2d86e8%2d8d15acd23777.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/12a5c7a7%2d4be8%2d47b3%2db461%2dbcef7be9392b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/e2909e8b%2db081%2d4705%2daa76%2d445acec52dbb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/18a0600e%2de9a1%2d4460%2d9234%2dd67973011adb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/b8d0a309%2d3c6a%2d44fd%2da2fe%2d55cd2d9c863c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/3af0b58e%2df15b%2d4ec5%2d85bb%2db384936813a7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/6c5cd0cb%2dff23%2d4f56%2daed3%2d38a72a851f15.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/678447d5%2d8207%2d4b39%2d9c81%2dc7f544524c5c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/smacks_h/21d542aa%2df3cb%2d45ba%2d9df4%2d7503372a4b04.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8d954902%2ddccc%2d4f71%2dbc6b%2d7d0c574aff00.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/f8a9aea6%2d79af%2d497a%2da97b%2d533e3c4aee58.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/5cd294e8%2d9251%2d4cde%2d95e9%2d4008a936949c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/f865bad1%2d28b6%2d407c%2d836e%2d7ccf5b632399.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8058a145%2d1ee5%2d4d9a%2d949c%2d86cdd8552ebb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/57a7503d%2db3c6%2d4929%2db2e1%2d9c48d613ac02.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/6643b6b5%2dbc4f%2d42ed%2d90b3%2d05008eedf66b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/5fc3334a%2d8085%2d4609%2d8f37%2d474dea332028.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/dab4acbf%2dbb7e%2d41ff%2d9315%2dd6eb06a55273.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/03630069%2d85ae%2d41c3%2dada4%2d899dd291552d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/62cc2459%2d0b9b%2d4b46%2d8cd9%2d17f2a920b417.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/7f49d7a9%2d1606%2d4646%2d927d%2d25c529c622f4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/a53baf1c%2d3e26%2d40f8%2d9ed5%2d53e3521b7ce1.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/f3bc7584%2dd808%2d4734%2d8b34%2d207d36e412f2.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/12665ee2%2d488d%2d4871%2d8afe%2d2e74a7c58fd2.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/90eefea2%2d3f78%2d4d36%2dbdce%2d231dbaa27af4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/e7c59026%2db739%2d4456%2dbf3b%2df0720c4ae40e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/cd92958e%2dbb31%2d4480%2d9ca8%2d03f249662a1e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/419d8f79%2d20d8%2d4641%2dbbf6%2d9472150641a0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/e401f06e%2dfec3%2d4c31%2d8681%2dd72e0caa5741.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/bbf4624f%2dde6a%2d4dbe%2da3e0%2dc2041664d8fb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/67e5a807%2d8d40%2d4881%2da902%2df6235382eddc.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/84763e59%2d4543%2d4339%2dac8a%2dbddd08c386cc.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/e43e5070%2d6ab2%2d41eb%2d9cf2%2d9d6794e2a76c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/bb17de8c%2db394%2d46cb%2d9b0e%2d585ca62c79f0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/c0ffb135%2d7192%2d4e09%2d83f9%2d76d3d4d18e1e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/be8832d5%2db2f5%2d4299%2dbe02%2d87c29d43dbf6.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/428bb04c%2d9161%2d42dd%2d9043%2d9307f8e913ae.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/dca28e1a%2db540%2d4f6a%2da6db%2ddfbd6a8003e0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/991ac953%2de40e%2d4bcf%2d8318%2d6a0f7702e2a1.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/987cb4f9%2da3c4%2d444f%2d9f79%2d5e17f9f80244.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/0c850591%2dd38b%2d4ee1%2d969c%2db024bf953fb1.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/a6f64cfa%2dd5b1%2d446c%2daaed%2d935943f2658e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/4a9cce98%2d7212%2d4632%2d814f%2dcf04f57db3dc.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/3587fa7e%2d99d4%2d4e71%2dbaea%2d1fe926f9a887.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/d194017b%2d5843%2d439f%2db0d1%2dc093df5e41c5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/0aaba1c7%2d80d4%2d4c80%2d9f67%2dd98d5fe9a2ee.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/0eecc217%2dfa1c%2d4654%2dbfee%2da3f9a4a38179.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/cb5f16fb%2d242e%2d4d7a%2d9922%2dc8f41852f70d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/6f5f9c56%2d7d86%2d409d%2dbb9b%2d021f30ba71b6.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/f637a0c1%2d28f4%2d47a5%2db852%2d7b80384fc2c4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/653f7066%2d9792%2d41bb%2da921%2de348d992c8c7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/7bb3649f%2db284%2d4f97%2d9db4%2d3ce6a587d927.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/533f847d%2d6344%2d4b6b%2d860e%2df2b676596826.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/78589660%2df813%2d42ba%2d842a%2d8bbdf417ad78.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/51514e64%2d43d6%2d411d%2db643%2dc5754dbfc292.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/c6b4504b%2d862d%2d44fc%2d9df6%2d68e5178b10d5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/926d3fcc%2d871e%2d4135%2d80ec%2df3c934529695.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/bc291b53%2d60f6%2d4dc0%2d8f7f%2d28165c9ed1e8.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/1a8854fc%2d49e3%2d46c5%2d83d5%2de9c8fe160e6c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/3f0ae356%2d9bf5%2d47fd%2da33f%2de94943d20829.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/079cd9c7%2d558a%2d484c%2d9ec2%2d8827863e8a47.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/6b01d1f5%2d1435%2d46ce%2d8c68%2d52a227349b04.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/b4f83f9b%2ddf86%2d4bc1%2db8e5%2d858cfbf78bb6.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/b43b32b1%2d5ec4%2d42be%2d82dc%2d817120c40071.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/df8a809c%2de960%2d4077%2d8338%2dcffd69937874.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/14131147%2db76b%2d4377%2dbdfd%2d7bbe5abaef44.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/d2f6abf9%2d0e98%2d419d%2d8519%2d93ded06318a7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/3277d864%2d2be9%2d4153%2d800b%2daee4e8c55d0b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/d151df02%2dc8e3%2d46b6%2db0f0%2da57e04e99516.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/54b6f931%2df4d2%2d41ba%2daddf%2ded139c0c8ffa.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/481a6a0e%2d4b78%2d43c0%2dac24%2da67813260faf.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/801b8594%2d878e%2d4de0%2d81bb%2db4d1aa34bfc5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/e321b093%2dcd5b%2d448f%2d8aaa%2dddfa6af6a526.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/eaca6f90%2d8a85%2d4345%2d9bc0%2d4305c0eeab0d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/37af6573%2d395c%2d4666%2d94eb%2d05488af58731.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/24565a5b%2dae43%2d4698%2d8e66%2d177280688d1e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/f469cc08%2dc01d%2d4d9e%2d88ed%2d2b0e7b41f788.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/743f5896%2d354d%2d4e9b%2d8736%2dc9c7db60aee9.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/925e8c07%2d95c7%2d4fc5%2da5d3%2dcdb2c1abbd32.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/949a07c4%2dde79%2d4112%2d964f%2d14ada1024210.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/4110c797%2dd3ff%2d47c4%2d86e5%2da74701c75e16.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/23a992c8%2d6275%2d4500%2d93ff%2d0936bae605b0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/af94b4a5%2d3aac%2d422f%2d9908%2d15fa10a57cf0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/c6f847bb%2d1981%2d445d%2db4a3%2d8fd985546c89.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8044bf48%2dd6b4%2d4f61%2d8269%2d56edf001209f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/ed09c322%2dc342%2d494b%2d8d8b%2d2d66fa9d768e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/6362e303%2d4e39%2d4bbd%2d8ef7%2d2ccb748d0f17.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/62216c11%2d0b4d%2d4458%2d981a%2d737a7dce372a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/0acea27b%2de3d4%2d4cc4%2db735%2d514d1c639017.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/d9a00995%2dd1bc%2d4c18%2db6c8%2d263c98123c0e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/4ae8ad62%2da4ec%2d4187%2da312%2de1562c7291b8.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/099347ec%2d34bb%2d45bb%2dab76%2d7de6786546fa.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/03ca09cd%2d69e7%2d48dc%2dbd2d%2d1b2cee04eca0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/c957bcfe%2dc366%2d4af4%2da619%2dbc98301d6a2b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/fa01c8c8%2d4586%2d4435%2d8b99%2df2bf083ded93.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/0edd63b3%2de90b%2d44d6%2daa3c%2dd5d2cecd7c69.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/b406b5a5%2d18b2%2d44e0%2dbd19%2dbb799b807966.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/4d51aab4%2d7210%2d43d6%2d8b24%2dbe582dcf62fe.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8d33e1d6%2d7393%2d4bf4%2d81e5%2da16c4a28ff55.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/a92ca5be%2d4b85%2d49cc%2d9b97%2d943c9d14e582.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/13f1fe81%2dfff2%2d42e0%2da65d%2ddba653560fc7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/be3e692c%2dc57f%2d48d0%2d85ca%2dc1c6309c9bc7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8cee4f4e%2d85cd%2d4e93%2d8ddb%2dfb529f226c6f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/dc4e0a12%2d3d8b%2d4f80%2da0e7%2dee7a14f36202.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/2b0c1f4f%2df495%2d4588%2db7fe%2dc834cf8c34b4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/9543cecd%2dfcb4%2d4614%2dbba4%2db448009cc18f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/6d944db0%2df1f6%2d4cc2%2d9dc7%2d33a39ed6d7ee.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/fe635a56%2d9310%2d4480%2d9c6a%2d9416ff619644.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/fb4e75dc%2d0d54%2d4ed9%2d9be2%2dc4ab3a66aa71.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/bf83bd47%2dfc72%2d4176%2daa4e%2dc7feea6314e3.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/4e9ad804%2daaf9%2d4935%2dbd88%2d9ceee1410006.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/f745c4a0%2d9c18%2d4af3%2db0c8%2d50913ec88e3f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/155e33c9%2d13cb%2d4850%2da3bc%2d5033fbb94aa8.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/abcf0a8b%2d824d%2d4375%2d8e75%2d503637440392.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/9e7a0392%2d921a%2d41ba%2d8b62%2d959c4420d589.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/d5a4477e%2db944%2d43eb%2d8a36%2dc5bca11c47ab.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/6c9bcbb2%2d3f33%2d4905%2da102%2da38fc7299e27.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/2ebf479a%2d9bcf%2d4524%2dabdf%2dad5bf79b9e0c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/715eea4f%2dd17a%2d49e4%2d93f6%2d531a9870935a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/a536f7fe%2d0f10%2d48c0%2d9059%2d3f4f2b21b651.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/ff74c6af%2d7a25%2d4cbd%2da116%2d001b6a312869.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/88b775ea%2d2392%2d44ae%2d8d2e%2d81a2081d8ed5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8ebc7209%2d0199%2d4b99%2d9302%2d100b77c6375e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/0b93a398%2d8bf8%2d48e8%2d836b%2d0a3c01b59788.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/4a3b05dd%2d0401%2d4603%2db7eb%2d80903891e60e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8a0878e4%2df4f5%2d4a7e%2d9fc3%2d1079422fe1b0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/b8941da8%2d206f%2d43a3%2d90c2%2d3d8c797909f1.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/9c018a65%2d640d%2d4554%2da72f%2d5cb7fe62cd36.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/50a1107b%2de1a4%2d48b9%2db348%2da8d0fdc1d2a5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8750a3c4%2d58c5%2d4114%2d962b%2d93b558e9df24.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/52c6c286%2d51e0%2d41d7%2daf5f%2deb9d1b84d13a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/5deeaf7b%2df774%2d4a4c%2d9d87%2d1d1206f7d103.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/92fac3d4%2d9745%2d4e15%2dac2d%2d474e067d2a63.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/6fbd8b62%2de8d7%2d4302%2d9ec6%2d582203c3b0c0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/7269f52a%2d1eaf%2d425c%2d820e%2dd424bb0b4e18.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/fbe4057f%2db037%2d4f48%2dbe64%2d8124944ac62d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/bcfefbde%2df47c%2d4a28%2db445%2d698d201d2e2d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/dda2e365%2d72b7%2d469d%2d95b3%2d15c54d3acc57.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/db00070c%2d7bdd%2d4429%2da13a%2d9540784ed277.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/3730688d%2df5fa%2d498e%2dac40%2d450da7e18309.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/bf1add98%2dabcc%2d44a4%2d8a82%2dbfb8430c5aff.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/9a21948d%2d9d69%2d49c9%2da678%2d688f5953519c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/150deb0c%2d4f98%2d4ca5%2db88d%2d032b1a745c78.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/1deb9ea7%2d67a1%2d4d56%2d9de9%2d6a3d7ea33dce.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/f1ffa37f%2d3ae9%2d4f47%2d8825%2da3d51234a6f4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/40e3142d%2ddd1a%2d4f72%2db074%2d4430160fffbf.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/728ff9e1%2d8834%2d4a85%2db23d%2d006ce74f07af.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/699993f3%2ddff9%2d4ad4%2db846%2deae84aaf5f8b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/1dedc4f1%2d81e6%2d46d8%2d8050%2d5fea77cca88a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/414f8474%2de0a7%2d405b%2dad2a%2d12e984b2ee6e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/f62169ed%2d67ad%2d40ce%2db47e%2d79e1ed291a9c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/378893e4%2d4620%2d4f38%2da322%2d39781f750df2.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/525146cd%2d13be%2d4a68%2d8dfc%2d6a1cd338f38b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/e87520bc%2def28%2d49b7%2d96cf%2d4ebb1de070c9.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/189e1dc6%2d5c94%2d45b0%2d9322%2dad9674dce20d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/b228d66a%2dbf4a%2d428f%2da8b0%2d6c52d55d2489.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/d240dd85%2dd97f%2d41d8%2d917b%2d07c0d6052281.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/e0ecc5b0%2dedd4%2d4c52%2d9f4f%2d3589d1bd5c1e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/36e65a33%2d8048%2d4a6d%2d96ad%2d36b28b355e9b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/7d1550fb%2dabb8%2d43fa%2d8e96%2dfd988cfad5d7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/11823e8c%2daa5c%2d47b5%2d8f21%2d13fd30248876.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8c092dd8%2d3475%2d48a5%2dbb23%2d08418f0cd3eb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/f002af29%2d039c%2d4395%2d86e8%2d8d15acd23777.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/12a5c7a7%2d4be8%2d47b3%2db461%2dbcef7be9392b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/e2909e8b%2db081%2d4705%2daa76%2d445acec52dbb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/18a0600e%2de9a1%2d4460%2d9234%2dd67973011adb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/693add15%2d8bf1%2d4c6e%2d9614%2d9d98b368c3e7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/0868fc52%2d4a74%2d402e%2d8d53%2dc67026ed6148.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/4d5285c9%2d5655%2d40d2%2d9192%2dc4007ff3b537.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/4bc6786c%2d9778%2d4890%2d987e%2dce803fcbe27b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/b8d0a309%2d3c6a%2d44fd%2da2fe%2d55cd2d9c863c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8ee4c369%2dab71%2d428b%2d9352%2da8558155ec5d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/3af0b58e%2df15b%2d4ec5%2d85bb%2db384936813a7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/6c5cd0cb%2dff23%2d4f56%2daed3%2d38a72a851f15.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/678447d5%2d8207%2d4b39%2d9c81%2dc7f544524c5c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/eb1ca8b1%2d2ec1%2d4512%2d9afb%2dc22046fe1bf7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/5681673b%2da738%2d4b59%2da72a%2d98f3f9f96051.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/21d542aa%2df3cb%2d45ba%2d9df4%2d7503372a4b04.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8ae5c900%2d8df6%2d45e3%2dad14%2d3c2f19b3cdd0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/8ab70611%2d6c13%2d4c6c%2d9abb%2d4d6b6ea66b29.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/cdbc2a8a%2d32b8%2d4e46%2db053%2d25ced4fdb976.dat
/var/lib/prosody/meet%2ecivitas%2elocal/pep/7a6d73a6%2d674d%2d4273%2d94da%2d4e412daf5865.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8d954902%2ddccc%2d4f71%2dbc6b%2d7d0c574aff00.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/f8a9aea6%2d79af%2d497a%2da97b%2d533e3c4aee58.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/5cd294e8%2d9251%2d4cde%2d95e9%2d4008a936949c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/f865bad1%2d28b6%2d407c%2d836e%2d7ccf5b632399.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/d6f6a9f1%2d12e5%2d4e5a%2d8426%2de2e912eb5a44.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8058a145%2d1ee5%2d4d9a%2d949c%2d86cdd8552ebb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/57a7503d%2db3c6%2d4929%2db2e1%2d9c48d613ac02.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/6643b6b5%2dbc4f%2d42ed%2d90b3%2d05008eedf66b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/5fc3334a%2d8085%2d4609%2d8f37%2d474dea332028.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/dab4acbf%2dbb7e%2d41ff%2d9315%2dd6eb06a55273.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/03630069%2d85ae%2d41c3%2dada4%2d899dd291552d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/62cc2459%2d0b9b%2d4b46%2d8cd9%2d17f2a920b417.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/7f49d7a9%2d1606%2d4646%2d927d%2d25c529c622f4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/a53baf1c%2d3e26%2d40f8%2d9ed5%2d53e3521b7ce1.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/f3bc7584%2dd808%2d4734%2d8b34%2d207d36e412f2.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/12665ee2%2d488d%2d4871%2d8afe%2d2e74a7c58fd2.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/90eefea2%2d3f78%2d4d36%2dbdce%2d231dbaa27af4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/e7c59026%2db739%2d4456%2dbf3b%2df0720c4ae40e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/cd92958e%2dbb31%2d4480%2d9ca8%2d03f249662a1e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/419d8f79%2d20d8%2d4641%2dbbf6%2d9472150641a0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/e401f06e%2dfec3%2d4c31%2d8681%2dd72e0caa5741.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/bbf4624f%2dde6a%2d4dbe%2da3e0%2dc2041664d8fb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/67e5a807%2d8d40%2d4881%2da902%2df6235382eddc.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/84763e59%2d4543%2d4339%2dac8a%2dbddd08c386cc.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/61e7cbe3%2d3708%2d4e24%2d9cb4%2dca1ce61f4bc4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/e43e5070%2d6ab2%2d41eb%2d9cf2%2d9d6794e2a76c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/bb17de8c%2db394%2d46cb%2d9b0e%2d585ca62c79f0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/c0ffb135%2d7192%2d4e09%2d83f9%2d76d3d4d18e1e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/be8832d5%2db2f5%2d4299%2dbe02%2d87c29d43dbf6.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/428bb04c%2d9161%2d42dd%2d9043%2d9307f8e913ae.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/dca28e1a%2db540%2d4f6a%2da6db%2ddfbd6a8003e0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/991ac953%2de40e%2d4bcf%2d8318%2d6a0f7702e2a1.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/987cb4f9%2da3c4%2d444f%2d9f79%2d5e17f9f80244.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/0c850591%2dd38b%2d4ee1%2d969c%2db024bf953fb1.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/a6f64cfa%2dd5b1%2d446c%2daaed%2d935943f2658e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/4a9cce98%2d7212%2d4632%2d814f%2dcf04f57db3dc.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/3587fa7e%2d99d4%2d4e71%2dbaea%2d1fe926f9a887.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/d194017b%2d5843%2d439f%2db0d1%2dc093df5e41c5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/0aaba1c7%2d80d4%2d4c80%2d9f67%2dd98d5fe9a2ee.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/0eecc217%2dfa1c%2d4654%2dbfee%2da3f9a4a38179.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/cb5f16fb%2d242e%2d4d7a%2d9922%2dc8f41852f70d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/6f5f9c56%2d7d86%2d409d%2dbb9b%2d021f30ba71b6.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/f637a0c1%2d28f4%2d47a5%2db852%2d7b80384fc2c4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/653f7066%2d9792%2d41bb%2da921%2de348d992c8c7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/7bb3649f%2db284%2d4f97%2d9db4%2d3ce6a587d927.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/533f847d%2d6344%2d4b6b%2d860e%2df2b676596826.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/78589660%2df813%2d42ba%2d842a%2d8bbdf417ad78.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/51514e64%2d43d6%2d411d%2db643%2dc5754dbfc292.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/c6b4504b%2d862d%2d44fc%2d9df6%2d68e5178b10d5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/926d3fcc%2d871e%2d4135%2d80ec%2df3c934529695.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/bc291b53%2d60f6%2d4dc0%2d8f7f%2d28165c9ed1e8.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/1a8854fc%2d49e3%2d46c5%2d83d5%2de9c8fe160e6c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/3f0ae356%2d9bf5%2d47fd%2da33f%2de94943d20829.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/079cd9c7%2d558a%2d484c%2d9ec2%2d8827863e8a47.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/6b01d1f5%2d1435%2d46ce%2d8c68%2d52a227349b04.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/b4f83f9b%2ddf86%2d4bc1%2db8e5%2d858cfbf78bb6.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/b43b32b1%2d5ec4%2d42be%2d82dc%2d817120c40071.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/df8a809c%2de960%2d4077%2d8338%2dcffd69937874.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/14131147%2db76b%2d4377%2dbdfd%2d7bbe5abaef44.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/d2f6abf9%2d0e98%2d419d%2d8519%2d93ded06318a7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/3277d864%2d2be9%2d4153%2d800b%2daee4e8c55d0b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/d151df02%2dc8e3%2d46b6%2db0f0%2da57e04e99516.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/54b6f931%2df4d2%2d41ba%2daddf%2ded139c0c8ffa.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/481a6a0e%2d4b78%2d43c0%2dac24%2da67813260faf.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/801b8594%2d878e%2d4de0%2d81bb%2db4d1aa34bfc5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/e321b093%2dcd5b%2d448f%2d8aaa%2dddfa6af6a526.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/eaca6f90%2d8a85%2d4345%2d9bc0%2d4305c0eeab0d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/37af6573%2d395c%2d4666%2d94eb%2d05488af58731.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/24565a5b%2dae43%2d4698%2d8e66%2d177280688d1e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/f469cc08%2dc01d%2d4d9e%2d88ed%2d2b0e7b41f788.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/743f5896%2d354d%2d4e9b%2d8736%2dc9c7db60aee9.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/925e8c07%2d95c7%2d4fc5%2da5d3%2dcdb2c1abbd32.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/949a07c4%2dde79%2d4112%2d964f%2d14ada1024210.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/4110c797%2dd3ff%2d47c4%2d86e5%2da74701c75e16.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/c37708bc%2db674%2d45fa%2d9597%2d4c7394937d8c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/23a992c8%2d6275%2d4500%2d93ff%2d0936bae605b0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/af94b4a5%2d3aac%2d422f%2d9908%2d15fa10a57cf0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/c6f847bb%2d1981%2d445d%2db4a3%2d8fd985546c89.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8044bf48%2dd6b4%2d4f61%2d8269%2d56edf001209f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/ed09c322%2dc342%2d494b%2d8d8b%2d2d66fa9d768e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/6362e303%2d4e39%2d4bbd%2d8ef7%2d2ccb748d0f17.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/62216c11%2d0b4d%2d4458%2d981a%2d737a7dce372a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/0acea27b%2de3d4%2d4cc4%2db735%2d514d1c639017.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/d9a00995%2dd1bc%2d4c18%2db6c8%2d263c98123c0e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/4ae8ad62%2da4ec%2d4187%2da312%2de1562c7291b8.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/099347ec%2d34bb%2d45bb%2dab76%2d7de6786546fa.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/db3994d2%2d9f36%2d46e0%2daac5%2dd446c1c20190.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/03ca09cd%2d69e7%2d48dc%2dbd2d%2d1b2cee04eca0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/c957bcfe%2dc366%2d4af4%2da619%2dbc98301d6a2b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/fa01c8c8%2d4586%2d4435%2d8b99%2df2bf083ded93.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/0edd63b3%2de90b%2d44d6%2daa3c%2dd5d2cecd7c69.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/b406b5a5%2d18b2%2d44e0%2dbd19%2dbb799b807966.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/4d51aab4%2d7210%2d43d6%2d8b24%2dbe582dcf62fe.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8d33e1d6%2d7393%2d4bf4%2d81e5%2da16c4a28ff55.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/a92ca5be%2d4b85%2d49cc%2d9b97%2d943c9d14e582.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/13f1fe81%2dfff2%2d42e0%2da65d%2ddba653560fc7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/be3e692c%2dc57f%2d48d0%2d85ca%2dc1c6309c9bc7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8cee4f4e%2d85cd%2d4e93%2d8ddb%2dfb529f226c6f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/dc4e0a12%2d3d8b%2d4f80%2da0e7%2dee7a14f36202.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/2b0c1f4f%2df495%2d4588%2db7fe%2dc834cf8c34b4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/9543cecd%2dfcb4%2d4614%2dbba4%2db448009cc18f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/6d944db0%2df1f6%2d4cc2%2d9dc7%2d33a39ed6d7ee.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/fe635a56%2d9310%2d4480%2d9c6a%2d9416ff619644.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/fb4e75dc%2d0d54%2d4ed9%2d9be2%2dc4ab3a66aa71.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/bf83bd47%2dfc72%2d4176%2daa4e%2dc7feea6314e3.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/4e9ad804%2daaf9%2d4935%2dbd88%2d9ceee1410006.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/f745c4a0%2d9c18%2d4af3%2db0c8%2d50913ec88e3f.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/155e33c9%2d13cb%2d4850%2da3bc%2d5033fbb94aa8.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/abcf0a8b%2d824d%2d4375%2d8e75%2d503637440392.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/9e7a0392%2d921a%2d41ba%2d8b62%2d959c4420d589.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/d5a4477e%2db944%2d43eb%2d8a36%2dc5bca11c47ab.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/6c9bcbb2%2d3f33%2d4905%2da102%2da38fc7299e27.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/2ebf479a%2d9bcf%2d4524%2dabdf%2dad5bf79b9e0c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/715eea4f%2dd17a%2d49e4%2d93f6%2d531a9870935a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/a536f7fe%2d0f10%2d48c0%2d9059%2d3f4f2b21b651.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/ff74c6af%2d7a25%2d4cbd%2da116%2d001b6a312869.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/88b775ea%2d2392%2d44ae%2d8d2e%2d81a2081d8ed5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8ebc7209%2d0199%2d4b99%2d9302%2d100b77c6375e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/0b93a398%2d8bf8%2d48e8%2d836b%2d0a3c01b59788.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/ebf43a31%2dadfc%2d48ce%2da178%2d0d69aed74e86.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/4a3b05dd%2d0401%2d4603%2db7eb%2d80903891e60e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8a0878e4%2df4f5%2d4a7e%2d9fc3%2d1079422fe1b0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/b8941da8%2d206f%2d43a3%2d90c2%2d3d8c797909f1.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/9c018a65%2d640d%2d4554%2da72f%2d5cb7fe62cd36.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/50a1107b%2de1a4%2d48b9%2db348%2da8d0fdc1d2a5.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8750a3c4%2d58c5%2d4114%2d962b%2d93b558e9df24.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/52c6c286%2d51e0%2d41d7%2daf5f%2deb9d1b84d13a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/5deeaf7b%2df774%2d4a4c%2d9d87%2d1d1206f7d103.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/92fac3d4%2d9745%2d4e15%2dac2d%2d474e067d2a63.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/6fbd8b62%2de8d7%2d4302%2d9ec6%2d582203c3b0c0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/7269f52a%2d1eaf%2d425c%2d820e%2dd424bb0b4e18.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/fbe4057f%2db037%2d4f48%2dbe64%2d8124944ac62d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/bcfefbde%2df47c%2d4a28%2db445%2d698d201d2e2d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/dda2e365%2d72b7%2d469d%2d95b3%2d15c54d3acc57.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/db00070c%2d7bdd%2d4429%2da13a%2d9540784ed277.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/3730688d%2df5fa%2d498e%2dac40%2d450da7e18309.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/bf1add98%2dabcc%2d44a4%2d8a82%2dbfb8430c5aff.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/9a21948d%2d9d69%2d49c9%2da678%2d688f5953519c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/150deb0c%2d4f98%2d4ca5%2db88d%2d032b1a745c78.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/1deb9ea7%2d67a1%2d4d56%2d9de9%2d6a3d7ea33dce.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/f1ffa37f%2d3ae9%2d4f47%2d8825%2da3d51234a6f4.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/40e3142d%2ddd1a%2d4f72%2db074%2d4430160fffbf.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/728ff9e1%2d8834%2d4a85%2db23d%2d006ce74f07af.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/afd2af77%2d5545%2d4e73%2d9118%2da50fd4b13270.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/699993f3%2ddff9%2d4ad4%2db846%2deae84aaf5f8b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/1dedc4f1%2d81e6%2d46d8%2d8050%2d5fea77cca88a.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/414f8474%2de0a7%2d405b%2dad2a%2d12e984b2ee6e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/f62169ed%2d67ad%2d40ce%2db47e%2d79e1ed291a9c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/378893e4%2d4620%2d4f38%2da322%2d39781f750df2.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/525146cd%2d13be%2d4a68%2d8dfc%2d6a1cd338f38b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/e87520bc%2def28%2d49b7%2d96cf%2d4ebb1de070c9.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/189e1dc6%2d5c94%2d45b0%2d9322%2dad9674dce20d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/b228d66a%2dbf4a%2d428f%2da8b0%2d6c52d55d2489.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/e9b18e55%2d0598%2d4b8b%2d9f11%2de7fe813b3b77.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/d240dd85%2dd97f%2d41d8%2d917b%2d07c0d6052281.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/e0ecc5b0%2dedd4%2d4c52%2d9f4f%2d3589d1bd5c1e.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/36e65a33%2d8048%2d4a6d%2d96ad%2d36b28b355e9b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/7d1550fb%2dabb8%2d43fa%2d8e96%2dfd988cfad5d7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/11823e8c%2daa5c%2d47b5%2d8f21%2d13fd30248876.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8c092dd8%2d3475%2d48a5%2dbb23%2d08418f0cd3eb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/f002af29%2d039c%2d4395%2d86e8%2d8d15acd23777.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/12a5c7a7%2d4be8%2d47b3%2db461%2dbcef7be9392b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/e2909e8b%2db081%2d4705%2daa76%2d445acec52dbb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/18a0600e%2de9a1%2d4460%2d9234%2dd67973011adb.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/693add15%2d8bf1%2d4c6e%2d9614%2d9d98b368c3e7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/0868fc52%2d4a74%2d402e%2d8d53%2dc67026ed6148.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/4d5285c9%2d5655%2d40d2%2d9192%2dc4007ff3b537.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/4bc6786c%2d9778%2d4890%2d987e%2dce803fcbe27b.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/b8d0a309%2d3c6a%2d44fd%2da2fe%2d55cd2d9c863c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8ee4c369%2dab71%2d428b%2d9352%2da8558155ec5d.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/3af0b58e%2df15b%2d4ec5%2d85bb%2db384936813a7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/6c5cd0cb%2dff23%2d4f56%2daed3%2d38a72a851f15.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/678447d5%2d8207%2d4b39%2d9c81%2dc7f544524c5c.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/eb1ca8b1%2d2ec1%2d4512%2d9afb%2dc22046fe1bf7.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/5681673b%2da738%2d4b59%2da72a%2d98f3f9f96051.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/21d542aa%2df3cb%2d45ba%2d9df4%2d7503372a4b04.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8ae5c900%2d8df6%2d45e3%2dad14%2d3c2f19b3cdd0.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/8ab70611%2d6c13%2d4c6c%2d9abb%2d4d6b6ea66b29.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/cdbc2a8a%2d32b8%2d4e46%2db053%2d25ced4fdb976.dat
/var/lib/prosody/meet%2ecivitas%2elocal/account_activity/7a6d73a6%2d674d%2d4273%2d94da%2d4e412daf5865.dat
/var/lib/prosody/meet%2ecivitas%2elocal/cron.dat
/var/lib/prosody/meet%2ecivitas%2elocal/offline
/var/lib/prosody/meet%2ecivitas%2elocal/offline/7a6d73a6%2d674d%2d4273%2d94da%2d4e412daf5865.lidx
/var/lib/prosody/meet%2ecivitas%2elocal/offline/11823e8c%2daa5c%2d47b5%2d8f21%2d13fd30248876.list
/var/lib/prosody/meet%2ecivitas%2elocal/offline/36e65a33%2d8048%2d4a6d%2d96ad%2d36b28b355e9b.lidx
/var/lib/prosody/meet%2ecivitas%2elocal/offline/84763e59%2d4543%2d4339%2dac8a%2dbddd08c386cc.list
/var/lib/prosody/meet%2ecivitas%2elocal/offline/7a6d73a6%2d674d%2d4273%2d94da%2d4e412daf5865.list
/var/lib/prosody/meet%2ecivitas%2elocal/offline/11823e8c%2daa5c%2d47b5%2d8f21%2d13fd30248876.lidx
/var/lib/prosody/meet%2ecivitas%2elocal/offline/2b0c1f4f%2df495%2d4588%2db7fe%2dc834cf8c34b4.lidx
/var/lib/prosody/meet%2ecivitas%2elocal/offline/36e65a33%2d8048%2d4a6d%2d96ad%2d36b28b355e9b.list
/var/lib/prosody/meet%2ecivitas%2elocal/offline/2b0c1f4f%2df495%2d4588%2db7fe%2dc834cf8c34b4.list
/var/lib/prosody/meet%2ecivitas%2elocal/offline/84763e59%2d4543%2d4339%2dac8a%2dbddd08c386cc.lidx
/var/lib/prosody/localhost
/var/lib/prosody/localhost/cron.dat
/var/lib/prosody/recorder%2emeet%2ecivitas%2elocal
/var/lib/prosody/recorder%2emeet%2ecivitas%2elocal/cron.dat
/var/lib/prosody/meet.civitas.local.key
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/account_roles
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/account_roles/focus.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/account_roles/jvb.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/accounts_cleanup
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/smacks_h
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/smacks_h/focus.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/smacks_h/jvb.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/accounts
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/accounts/focus.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/accounts/jvb.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/pep
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/pep/focus.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/pep/jvb.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/account_activity
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/account_activity/focus.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/account_activity/jvb.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/cron.dat
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/offline
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/roster
/var/lib/prosody/auth%2emeet%2ecivitas%2elocal/roster/focus.dat
/var/lib/prosody/auth.meet.civitas.local.crt
/var/lib/prosody/auth.meet.civitas.local.cnf
/var/lib/prosody/.shell_history
/var/lib/prosody/meet.civitas.local.crt
/var/lib/prosody/meet.civitas.local.cnf
/var/lib/prosody/prosody.sock
/var/lib/prosody/auth.meet.civitas.local.key
/var/log/prosody
/var/log/prosody/prosody.err.4.gz
/var/log/prosody/prosody.err.1
/var/log/prosody/prosody.log.4.gz
/var/log/prosody/prosody.err.3.gz
/var/log/prosody/prosody.log.3.gz
/var/log/prosody/prosody.err
/var/log/prosody/prosody.err.2.gz
/var/log/prosody/prosody.log.2.gz
/var/log/prosody/prosody.log
/var/log/prosody/prosody.log.1


## Configuration Prosody


```text
$ find /etc/prosody -type f -print 2>/dev/null || true
```
/etc/prosody/README
/etc/prosody/migrator.cfg.lua
/etc/prosody/conf.d/meet.civitas.local.cfg.lua
/etc/prosody/conf.avail/example.com.cfg.lua
/etc/prosody/conf.avail/localhost.cfg.lua
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua
/etc/prosody/conf.avail/jaas.cfg.lua
/etc/prosody/prosody.cfg.lua


## Configuration principale


```text
$ cat /etc/prosody/prosody.cfg.lua 2>/dev/null || true
```
-- Prosody Example Configuration File
--
-- Information on configuring Prosody can be found on our
-- website at https://prosody.im/doc/configure
--
-- Tip: You can check that the syntax of this file is correct
-- when you have finished by running this command:
--     prosodyctl check config
-- If there are any errors, it will let you know what and where
-- they are, otherwise it will keep quiet.
--
-- Upgrading from a previous release? Check https://prosody.im/doc/upgrading
--
-- The only thing left to do is rename this file to remove the .dist ending, and fill in the
-- blanks. Good luck, and happy Jabbering!


---------- Server-wide settings ----------
-- Settings in this section apply to the whole server and are the default settings
-- for any virtual hosts

-- This is a (by default, empty) list of accounts that are admins
-- for the server. Note that you must create the accounts separately
-- (see https://prosody.im/doc/creating_accounts for info)
-- Example: admins = { "user1@example.com", "user2@example.net" }
admins = { }

-- This option allows you to specify additional locations where Prosody
-- will search first for modules. For additional modules you can install, see
-- the community module repository at https://modules.prosody.im/
-- For a local administrator it's common to place local modifications
-- under /usr/local/ hierarchy:
plugin_paths = { "/usr/local/lib/prosody/modules", "/usr/share/jitsi-meet/prosody-plugins/" }

-- This is the list of modules Prosody will load on startup.
-- Documentation for bundled modules can be found at: https://prosody.im/doc/modules
modules_enabled = {

	-- Generally required
		"disco"; -- Service discovery
		"roster"; -- Allow users to have a roster. Recommended ;)
		"saslauth"; -- Authentication for clients and servers. Recommended if you want to log in.
		"tls"; -- Add support for secure TLS on c2s/s2s connections

	-- Not essential, but recommended
		"blocklist"; -- Allow users to block communications with other users
		"bookmarks"; -- Synchronise the list of open rooms between clients
		"carbons"; -- Keep multiple online clients in sync
		"dialback"; -- Support for verifying remote servers using DNS
		"limits"; -- Enable bandwidth limiting for XMPP connections
		"pep"; -- Allow users to store public and private data in their account
		"private"; -- Legacy account storage mechanism (XEP-0049)
		"smacks"; -- Stream management and resumption (XEP-0198)
		"vcard4"; -- User profiles (stored in PEP)
		"vcard_legacy"; -- Conversion between legacy vCard and PEP Avatar, vcard

	-- Nice to have
		"account_activity"; -- Record time when an account was last used
		"cloud_notify"; -- Push notifications for mobile devices
		"csi_simple"; -- Simple but effective traffic optimizations for mobile devices
		"invites"; -- Create and manage invites
		"invites_adhoc"; -- Allow admins/users to create invitations via their client
		"invites_register"; -- Allows invited users to create accounts
		"ping"; -- Replies to XMPP pings with pongs
		"register"; -- Allow users to register on this server using a client and change passwords
		"time"; -- Let others know the time here on this server
		"uptime"; -- Report how long server has been running
		"version"; -- Replies to server version requests
		--"mam"; -- Store recent messages to allow multi-device synchronization
		--"turn_external"; -- Provide external STUN/TURN service for e.g. audio/video calls

	-- Admin interfaces
		"admin_adhoc"; -- Allows administration via an XMPP client that supports ad-hoc commands
		"admin_shell"; -- Allow secure administration via 'prosodyctl shell'

	-- HTTP modules
		"bosh"; -- Enable BOSH clients, aka "Jabber over HTTP"
		--"http_openmetrics"; -- for exposing metrics to stats collectors
		"websocket"; -- XMPP over WebSockets

	-- Other specific functionality
		"posix"; -- POSIX functionality, sends server to background, enables syslog, etc.
		--"announce"; -- Send announcement to all online users
		--"groups"; -- Shared roster support
		--"mimicking"; -- Prevent address spoofing
		--"motd"; -- Send a message to users when they log in
		--"proxy65"; -- Enables a file transfer proxy service which clients behind NAT can use
		--"s2s_bidi"; -- Bi-directional server-to-server (XEP-0288)
		--"server_contact_info"; -- Publish contact information for this service
		--"tombstones"; -- Prevent registration of deleted accounts
		--"watchregistrations"; -- Alert admins of registrations
		--"welcome"; -- Welcome users who register accounts
}

-- These modules are auto-loaded, but should you want
-- to disable them then uncomment them here:
modules_disabled = {
	-- "offline"; -- Store offline messages
	-- "c2s"; -- Handle client connections
	-- "s2s"; -- Handle server-to-server connections
}

-- Debian:
--   Please, don't change this option since /run/prosody/
--   is one of the few directories Prosody is allowed to write to
--
pidfile = "/run/prosody/prosody.pid";

-- Server-to-server authentication
-- Require valid certificates for server-to-server connections?
-- If false, other methods such as dialback (DNS) may be used instead.

s2s_secure_auth = true

-- Some servers have invalid or self-signed certificates. You can list
-- remote domains here that will not be required to authenticate using
-- certificates. They will be authenticated using other methods instead,
-- even when s2s_secure_auth is enabled.

--s2s_insecure_domains = { "insecure.example" }

-- Even if you disable s2s_secure_auth, you can still require valid
-- certificates for some domains by specifying a list here.

--s2s_secure_domains = { "jabber.org" }


-- Rate limits
-- Enable rate limits for incoming client and server connections. These help
-- protect from excessive resource consumption and denial-of-service attacks.

limits = {
	c2s = {
		rate = "10kb/s";
	};
	s2sin = {
		rate = "30kb/s";
	};
}

-- Authentication
-- Select the authentication backend to use. The 'internal' providers
-- use Prosody's configured data storage to store the authentication data.
-- For more information see https://prosody.im/doc/authentication

authentication = "internal_hashed"

-- Many authentication providers, including the default one, allow you to
-- create user accounts via Prosody's admin interfaces. For details, see the
-- documentation at https://prosody.im/doc/creating_accounts


-- Storage
-- Select the storage backend to use. By default Prosody uses flat files
-- in its configured data directory, but it also supports more backends
-- through modules. An "sql" backend is included by default, but requires
-- additional dependencies. See https://prosody.im/doc/storage for more info.

--storage = "sql" -- Default is "internal" (Debian: "sql" requires one of the
-- lua-dbi-sqlite3, lua-dbi-mysql or lua-dbi-postgresql packages to work)

-- For the "sql" backend, you can uncomment *one* of the below to configure:
--sql = { driver = "SQLite3", database = "prosody.sqlite" } -- Default. 'database' is the filename.
--sql = { driver = "MySQL", database = "prosody", username = "prosody", password = "secret", host = "localhost" }
--sql = { driver = "PostgreSQL", database = "prosody", username = "prosody", password = "secret", host = "localhost" }


-- Archiving configuration
-- If mod_mam is enabled, Prosody will store a copy of every message. This
-- is used to synchronize conversations between multiple clients, even if
-- they are offline. This setting controls how long Prosody will keep
-- messages in the archive before removing them.

archive_expires_after = "1w" -- Remove archived messages after 1 week

-- You can also configure messages to be stored in-memory only. For more
-- archiving options, see https://prosody.im/doc/modules/mod_mam


-- Audio/video call relay (STUN/TURN)
-- To ensure clients connected to the server can establish connections for
-- low-latency media streaming (such as audio and video calls), it is
-- recommended to run a STUN/TURN server for clients to use. If you do this,
-- specify the details here so clients can discover it.
-- Find more information at https://prosody.im/doc/turn

-- Specify the address of the TURN service (you may use the same domain as XMPP)
--turn_external_host = "turn.example.com"

-- This secret must be set to the same value in both Prosody and the TURN server
--turn_external_secret = "your-secret-turn-access-token"


-- Logging configuration
-- For advanced logging see https://prosody.im/doc/logging
--
-- Debian:
--  Logs info and higher to /var/log
--  Logs errors to syslog also
log = {
	-- Log files (change 'info' to 'debug' for debug logs):
	info = "/var/log/prosody/prosody.log";
	error = "/var/log/prosody/prosody.err";
	-- Syslog:
	{ levels = { "error" }; to = "syslog";  };
}


-- Uncomment to enable statistics
-- For more info see https://prosody.im/doc/statistics
-- statistics = "internal"


-- Certificates
-- Every virtual host and component needs a certificate so that clients and
-- servers can securely verify its identity. Prosody will automatically load
-- certificates/keys from the directory specified here.
-- For more information, including how to use 'prosodyctl' to auto-import certificates
-- (from e.g. Let's Encrypt) see https://prosody.im/doc/certificates

-- Location of directory to find certificates in (relative to main config file):
certificates = "certs"

----------- Virtual hosts -----------
-- You need to add a VirtualHost entry for each domain you wish Prosody to serve.
-- Settings under each VirtualHost entry apply *only* to that host.
-- It's customary to maintain VirtualHost entries in separate config files
-- under /etc/prosody/conf.d/ directory. Examples of such config files can
-- be found in /etc/prosody/conf.avail/ directory.

------ Additional config files ------
-- For organizational purposes you may prefer to add VirtualHost and
-- Component definitions in their own config files. This line includes
-- all config files in /etc/prosody/conf.d/

VirtualHost "localhost"
-- Prosody requires at least one enabled VirtualHost to function. You can
-- safely remove or disable 'localhost' once you have added another.


--VirtualHost "example.com"

------ Components ------
-- You can specify components to add hosts that provide special services,
-- like multi-user conferences, and transports.
-- For more information on components, see https://prosody.im/doc/components

---Set up a MUC (multi-user chat) room server on conference.example.com:
--Component "conference.example.com" "muc"
--- Store MUC messages in an archive and allow users to access it
--modules_enabled = { "muc_mam" }

---Set up a file sharing component
--Component "share.example.com" "http_file_share"

---Set up an external component (default component port is 5347)
--
-- External components allow adding various services, such as gateways/
-- bridges to non-XMPP networks and services. For more info
-- see: https://prosody.im/doc/components#adding_an_external_component
--
--Component "gateway.example.com"
--	component_secret = "password"

Include "conf.d/*.cfg.lua"

---------- End of the Prosody Configuration file ----------
-- You usually **DO NOT** want to add settings here at the end, as they would
-- only apply to the last defined VirtualHost or Component.
--
-- Settings for the global section should go higher up, before the first
-- VirtualHost or Component line, while settings intended for specific hosts
-- should go under the corresponding VirtualHost or Component line.
--
-- For more information see https://prosody.im/doc/configure


## Configurations Jitsi Prosody


```text
$ find /etc/prosody -type f -iname "*jitsi*" -o -iname "*meet*" 2>/dev/null | sort
```
/etc/prosody/certs/auth.meet.civitas.local.crt
/etc/prosody/certs/auth.meet.civitas.local.key
/etc/prosody/certs/meet.civitas.local.crt
/etc/prosody/certs/meet.civitas.local.key
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua
/etc/prosody/conf.d/meet.civitas.local.cfg.lua


## Virtual hosts


```text
$ grep -RniE "VirtualHost|Component|authentication|admins" /etc/prosody 2>/dev/null || true
```
/etc/prosody/conf.d/localhost.cfg.lua:4:VirtualHost "localhost"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:1:component_admins_as_room_owners = true
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:23:VirtualHost "meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:24:    authentication = "jitsi-anonymous"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:41:VirtualHost "auth.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:42:    authentication = "internal_hashed"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:44:Component "conference.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:54:    admins = { "focus@auth.meet.civitas.local" }
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:58:Component "internal.auth.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:61:    admins = { "focus@auth.meet.civitas.local", "jvb@auth.meet.civitas.local" }
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:65:Component "focus.meet.civitas.local" "client_proxy"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:68:Component "speakerstats.meet.civitas.local" "speakerstats_component"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:69:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:71:Component "endconference.meet.civitas.local" "end_conference"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:72:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:74:Component "muc.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:77:Component "breakout.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:84:    admins = { "focus@auth.meet.civitas.local" }
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:88:Component "lobby.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:95:Component "metadata.meet.civitas.local" "room_metadata_component"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:96:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:98:Component "avmoderation.meet.civitas.local" "av_moderation_component"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:99:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:101:Component "polls.meet.civitas.local" "polls_component"
/etc/prosody/conf.avail/example.com.cfg.lua:3:VirtualHost "example.com"
/etc/prosody/conf.avail/example.com.cfg.lua:15:------ Components ------
/etc/prosody/conf.avail/example.com.cfg.lua:16:-- You can specify components to add hosts that provide special services,
/etc/prosody/conf.avail/example.com.cfg.lua:18:-- For more information on components, see http://prosody.im/doc/components
/etc/prosody/conf.avail/example.com.cfg.lua:21:Component "conference.example.com" "muc"
/etc/prosody/conf.avail/example.com.cfg.lua:24:--Component "proxy.example.com" "proxy65"
/etc/prosody/conf.avail/example.com.cfg.lua:26:---Set up an external component (default component port is 5347)
/etc/prosody/conf.avail/example.com.cfg.lua:27:--Component "gateway.example.com"
/etc/prosody/conf.avail/example.com.cfg.lua:28:--	component_secret = "password"
/etc/prosody/conf.avail/localhost.cfg.lua:4:VirtualHost "localhost"
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:1:component_admins_as_room_owners = true
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:6:Component "conference.meet.civitas.local" "muc"
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:19:Component "internal.auth.meet.civitas.local" "muc"
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:22:    admins = { "focus@auth.meet.civitas.local", "jvb@auth.meet.civitas.local" }
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:26:Component "polls.meet.civitas.local" "polls_component"
/etc/prosody/conf.avail/jaas.cfg.lua:1:-- Enables dial-in for Jitsi meet components customers
/etc/prosody/conf.avail/jaas.cfg.lua:2:VirtualHost "jigasi.meet.jitsi"
/etc/prosody/conf.avail/jaas.cfg.lua:8:    authentication = "token"
/etc/prosody/conf.avail/jaas.cfg.lua:10:    asap_key_server = "https://jaas-public-keys.jitsi.net/jitsi-components/prod-8x8"
/etc/prosody/conf.avail/jaas.cfg.lua:11:    asap_accepted_issuers = { "jaas-components" }
/etc/prosody/prosody.cfg.lua:22:-- This is a (by default, empty) list of accounts that are admins
/etc/prosody/prosody.cfg.lua:25:-- Example: admins = { "user1@example.com", "user2@example.net" }
/etc/prosody/prosody.cfg.lua:26:admins = { }
/etc/prosody/prosody.cfg.lua:42:		"saslauth"; -- Authentication for clients and servers. Recommended if you want to log in.
/etc/prosody/prosody.cfg.lua:62:		"invites_adhoc"; -- Allow admins/users to create invitations via their client
/etc/prosody/prosody.cfg.lua:91:		--"watchregistrations"; -- Alert admins of registrations
/etc/prosody/prosody.cfg.lua:109:-- Server-to-server authentication
/etc/prosody/prosody.cfg.lua:141:-- Authentication
/etc/prosody/prosody.cfg.lua:142:-- Select the authentication backend to use. The 'internal' providers
/etc/prosody/prosody.cfg.lua:143:-- use Prosody's configured data storage to store the authentication data.
/etc/prosody/prosody.cfg.lua:144:-- For more information see https://prosody.im/doc/authentication
/etc/prosody/prosody.cfg.lua:146:authentication = "internal_hashed"
/etc/prosody/prosody.cfg.lua:148:-- Many authentication providers, including the default one, allow you to
/etc/prosody/prosody.cfg.lua:215:-- Every virtual host and component needs a certificate so that clients and
/etc/prosody/prosody.cfg.lua:225:-- You need to add a VirtualHost entry for each domain you wish Prosody to serve.
/etc/prosody/prosody.cfg.lua:226:-- Settings under each VirtualHost entry apply *only* to that host.
/etc/prosody/prosody.cfg.lua:227:-- It's customary to maintain VirtualHost entries in separate config files
/etc/prosody/prosody.cfg.lua:232:-- For organizational purposes you may prefer to add VirtualHost and
/etc/prosody/prosody.cfg.lua:233:-- Component definitions in their own config files. This line includes
/etc/prosody/prosody.cfg.lua:236:VirtualHost "localhost"
/etc/prosody/prosody.cfg.lua:237:-- Prosody requires at least one enabled VirtualHost to function. You can
/etc/prosody/prosody.cfg.lua:241:--VirtualHost "example.com"
/etc/prosody/prosody.cfg.lua:243:------ Components ------
/etc/prosody/prosody.cfg.lua:244:-- You can specify components to add hosts that provide special services,
/etc/prosody/prosody.cfg.lua:246:-- For more information on components, see https://prosody.im/doc/components
/etc/prosody/prosody.cfg.lua:249:--Component "conference.example.com" "muc"
/etc/prosody/prosody.cfg.lua:253:---Set up a file sharing component
/etc/prosody/prosody.cfg.lua:254:--Component "share.example.com" "http_file_share"
/etc/prosody/prosody.cfg.lua:256:---Set up an external component (default component port is 5347)
/etc/prosody/prosody.cfg.lua:258:-- External components allow adding various services, such as gateways/
/etc/prosody/prosody.cfg.lua:260:-- see: https://prosody.im/doc/components#adding_an_external_component
/etc/prosody/prosody.cfg.lua:262:--Component "gateway.example.com"
/etc/prosody/prosody.cfg.lua:263:--	component_secret = "password"
/etc/prosody/prosody.cfg.lua:269:-- only apply to the last defined VirtualHost or Component.
/etc/prosody/prosody.cfg.lua:272:-- VirtualHost or Component line, while settings intended for specific hosts
/etc/prosody/prosody.cfg.lua:273:-- should go under the corresponding VirtualHost or Component line.


## Modules


```text
$ find /usr/lib/prosody /usr/share/prosody /etc/prosody -type f 2>/dev/null | grep -Ei "module|jitsi" | sort || true
```
/usr/lib/prosody/core/moduleapi.lua
/usr/lib/prosody/core/modulemanager.lua
/usr/lib/prosody/modules/adhoc/adhoc.lib.lua
/usr/lib/prosody/modules/adhoc/mod_adhoc.lua
/usr/lib/prosody/modules/mod_account_activity.lua
/usr/lib/prosody/modules/mod_admin_adhoc.lua
/usr/lib/prosody/modules/mod_admin_shell.lua
/usr/lib/prosody/modules/mod_admin_socket.lua
/usr/lib/prosody/modules/mod_admin_telnet.lua
/usr/lib/prosody/modules/mod_announce.lua
/usr/lib/prosody/modules/mod_auth_anonymous.lua
/usr/lib/prosody/modules/mod_auth_insecure.lua
/usr/lib/prosody/modules/mod_auth_internal_hashed.lua
/usr/lib/prosody/modules/mod_auth_internal_plain.lua
/usr/lib/prosody/modules/mod_auth_ldap.lua
/usr/lib/prosody/modules/mod_authz_internal.lua
/usr/lib/prosody/modules/mod_blocklist.lua
/usr/lib/prosody/modules/mod_bookmarks.lua
/usr/lib/prosody/modules/mod_bosh.lua
/usr/lib/prosody/modules/mod_c2s.lua
/usr/lib/prosody/modules/mod_carbons.lua
/usr/lib/prosody/modules/mod_cloud_notify.lua
/usr/lib/prosody/modules/mod_component.lua
/usr/lib/prosody/modules/mod_cron.lua
/usr/lib/prosody/modules/mod_csi.lua
/usr/lib/prosody/modules/mod_csi_simple.lua
/usr/lib/prosody/modules/mod_debug_reset.lua
/usr/lib/prosody/modules/mod_debug_sql.lua
/usr/lib/prosody/modules/mod_debug_stanzas/watcher.lib.lua
/usr/lib/prosody/modules/mod_dialback.lua
/usr/lib/prosody/modules/mod_disco.lua
/usr/lib/prosody/modules/mod_external_services.lua
/usr/lib/prosody/modules/mod_flags.lua
/usr/lib/prosody/modules/mod_groups.lua
/usr/lib/prosody/modules/mod_http_altconnect.lua
/usr/lib/prosody/modules/mod_http_errors.lua
/usr/lib/prosody/modules/mod_http_file_share.lua
/usr/lib/prosody/modules/mod_http_files.lua
/usr/lib/prosody/modules/mod_http.lua
/usr/lib/prosody/modules/mod_http_openmetrics.lua
/usr/lib/prosody/modules/mod_invites_adhoc.lua
/usr/lib/prosody/modules/mod_invites.lua
/usr/lib/prosody/modules/mod_invites_register.lua
/usr/lib/prosody/modules/mod_iq.lua
/usr/lib/prosody/modules/mod_lastactivity.lua
/usr/lib/prosody/modules/mod_legacyauth.lua
/usr/lib/prosody/modules/mod_limits.lua
/usr/lib/prosody/modules/mod_mam/mamprefs.lib.lua
/usr/lib/prosody/modules/mod_mam/mamprefsxml.lib.lua
/usr/lib/prosody/modules/mod_mam/mod_mam.lua
/usr/lib/prosody/modules/mod_message.lua
/usr/lib/prosody/modules/mod_mimicking.lua
/usr/lib/prosody/modules/mod_motd.lua
/usr/lib/prosody/modules/mod_muc_mam.lua
/usr/lib/prosody/modules/mod_muc_unique.lua
/usr/lib/prosody/modules/mod_net_multiplex.lua
/usr/lib/prosody/modules/mod_offline.lua
/usr/lib/prosody/modules/mod_pep.lua
/usr/lib/prosody/modules/mod_pep_plus.lua
/usr/lib/prosody/modules/mod_pep_simple.lua
/usr/lib/prosody/modules/mod_ping.lua
/usr/lib/prosody/modules/mod_posix.lua
/usr/lib/prosody/modules/mod_presence.lua
/usr/lib/prosody/modules/mod_private.lua
/usr/lib/prosody/modules/mod_proxy65.lua
/usr/lib/prosody/modules/mod_pubsub/commands.lib.lua
/usr/lib/prosody/modules/mod_pubsub/mod_pubsub.lua
/usr/lib/prosody/modules/mod_pubsub/pubsub.lib.lua
/usr/lib/prosody/modules/mod_register_ibr.lua
/usr/lib/prosody/modules/mod_register_limits.lua
/usr/lib/prosody/modules/mod_register.lua
/usr/lib/prosody/modules/mod_roster.lua
/usr/lib/prosody/modules/mod_s2s_auth_certs.lua
/usr/lib/prosody/modules/mod_s2s_auth_dane_in.lua
/usr/lib/prosody/modules/mod_s2s_bidi.lua
/usr/lib/prosody/modules/mod_s2s.lua
/usr/lib/prosody/modules/mod_saslauth.lua
/usr/lib/prosody/modules/mod_scansion_record.lua
/usr/lib/prosody/modules/mod_server_contact_info.lua
/usr/lib/prosody/modules/mod_server_info.lua
/usr/lib/prosody/modules/mod_smacks.lua
/usr/lib/prosody/modules/mod_stanza_debug.lua
/usr/lib/prosody/modules/mod_storage_internal.lua
/usr/lib/prosody/modules/mod_storage_memory.lua
/usr/lib/prosody/modules/mod_storage_none.lua
/usr/lib/prosody/modules/mod_storage_sql.lua
/usr/lib/prosody/modules/mod_storage_xep0227.lua
/usr/lib/prosody/modules/mod_time.lua
/usr/lib/prosody/modules/mod_tls.lua
/usr/lib/prosody/modules/mod_tokenauth.lua
/usr/lib/prosody/modules/mod_tombstones.lua
/usr/lib/prosody/modules/mod_turn_external.lua
/usr/lib/prosody/modules/mod_unknown.lua
/usr/lib/prosody/modules/mod_uptime.lua
/usr/lib/prosody/modules/mod_user_account_management.lua
/usr/lib/prosody/modules/mod_vcard4.lua
/usr/lib/prosody/modules/mod_vcard_legacy.lua
/usr/lib/prosody/modules/mod_vcard.lua
/usr/lib/prosody/modules/mod_version.lua
/usr/lib/prosody/modules/mod_watchregistrations.lua
/usr/lib/prosody/modules/mod_websocket.lua
/usr/lib/prosody/modules/mod_welcome.lua
/usr/lib/prosody/modules/mod_windows.lua
/usr/lib/prosody/modules/muc/config_form_sections.lib.lua
/usr/lib/prosody/modules/muc/description.lib.lua
/usr/lib/prosody/modules/muc/hats.lib.lua
/usr/lib/prosody/modules/muc/hidden.lib.lua
/usr/lib/prosody/modules/muc/history.lib.lua
/usr/lib/prosody/modules/muc/language.lib.lua
/usr/lib/prosody/modules/muc/lock.lib.lua
/usr/lib/prosody/modules/muc/members_only.lib.lua
/usr/lib/prosody/modules/muc/moderated.lib.lua
/usr/lib/prosody/modules/muc/mod_muc.lua
/usr/lib/prosody/modules/muc/muc.lib.lua
/usr/lib/prosody/modules/muc/name.lib.lua
/usr/lib/prosody/modules/muc/occupant_id.lib.lua
/usr/lib/prosody/modules/muc/occupant.lib.lua
/usr/lib/prosody/modules/muc/password.lib.lua
/usr/lib/prosody/modules/muc/persistent.lib.lua
/usr/lib/prosody/modules/muc/presence_broadcast.lib.lua
/usr/lib/prosody/modules/muc/register.lib.lua
/usr/lib/prosody/modules/muc/request.lib.lua
/usr/lib/prosody/modules/muc/restrict_pm.lib.lua
/usr/lib/prosody/modules/muc/subject.lib.lua
/usr/lib/prosody/modules/muc/util.lib.lua
/usr/lib/prosody/modules/muc/vcard.lib.lua
/usr/lib/prosody/modules/muc/whois.lib.lua


## Utilisateurs Prosody


```text
$ prosodyctl list 2>/dev/null || true
```



---

# 5. JICOFO

**Date :** 2026-08-08 06:56:25 EDT


## Localisation


```text
$ find /etc/jitsi /usr/share/jicofo /usr/share/jitsi /usr/lib/jicofo -type f 2>/dev/null | sort | grep -Ei "jicofo|jitsi" || true
```
/etc/jitsi/jicofo/config
/etc/jitsi/jicofo/jicofo.conf
/etc/jitsi/jicofo/logging.properties
/etc/jitsi/meet/meet.civitas.local-config.js
/etc/jitsi/videobridge/config
/etc/jitsi/videobridge/jvb.conf
/etc/jitsi/videobridge/logging.properties
/usr/share/jicofo/collect-dump-logs.sh
/usr/share/jicofo/jicofo.jar
/usr/share/jicofo/jicofo.sh
/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar
/usr/share/jicofo/lib/annotations-23.0.0.jar
/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar
/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar
/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar
/usr/share/jicofo/lib/commons-lang3-3.12.0.jar
/usr/share/jicofo/lib/config-1.4.3.jar
/usr/share/jicofo/lib/gson-2.8.5.jar
/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar
/usr/share/jicofo/lib/jackson-core-2.18.0.jar
/usr/share/jicofo/lib/jackson-databind-2.18.0.jar
/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar
/usr/share/jicofo/lib/jansi-2.4.1.jar
/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar
/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar
/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar
/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar
/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar
/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar
/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar
/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar
/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar
/usr/share/jicofo/lib/jjwt-api-0.12.6.jar
/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar
/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar
/usr/share/jicofo/lib/jna-5.9.0.jar
/usr/share/jicofo/lib/jsr305-3.0.2.jar
/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar
/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar
/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar
/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar
/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar
/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar
/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar
/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar
/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar
/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar
/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar
/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar
/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar
/usr/share/jicofo/lib/minidns-core-1.0.5.jar
/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar
/usr/share/jicofo/lib/precis-1.1.0.jar
/usr/share/jicofo/lib/sentry-5.4.0.jar
/usr/share/jicofo/lib/simpleclient-0.16.0.jar
/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar
/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar
/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar
/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar
/usr/share/jicofo/lib/slf4j-api-1.7.32.jar
/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar
/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar


## Configuration


```text
$ find /etc/jitsi/jicofo -maxdepth 5 -type f -print 2>/dev/null || true
```
/etc/jitsi/jicofo/config
/etc/jitsi/jicofo/logging.properties
/etc/jitsi/jicofo/jicofo.conf


## Contenu configuration Jicofo


```text
$ for f in /etc/jitsi/jicofo/*; do [ -f "$f" ] && { echo "===== $f ====="; sed -n "1,240p" "$f"; }; done
```
===== /etc/jitsi/jicofo/config =====
# adds java system props that are passed to jicofo (default are for home and logging config file)
JAVA_SYS_PROPS="-Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=jicofo -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/jicofo/logging.properties"
===== /etc/jitsi/jicofo/jicofo.conf =====
jicofo {
  xmpp: {
    client: {
      client-proxy: "focus.meet.civitas.local"
      xmpp-domain: "meet.civitas.local"
      domain: "auth.meet.civitas.local"
      username: "focus"
      password: "om6g0shu31tCT1id"
      disable-certificate-verification: true
    }
    service: {
      domain: "meet.civitas.local"
      disable-certificate-verification: true
    }
    trusted-domains: [ "recorder.meet.civitas.local" ]
  }
  bridge: {
    brewery-jid: "JvbBrewery@internal.auth.meet.civitas.local"
  }
}
===== /etc/jitsi/jicofo/logging.properties =====

handlers= java.util.logging.ConsoleHandler

# Handlers with XMPP debug enabled:
#handlers= java.util.logging.ConsoleHandler, org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler

# Handlers with sentry enabled:
#handlers= java.util.logging.ConsoleHandler, io.sentry.jul.SentryHandler

java.util.logging.ConsoleHandler.level = ALL
java.util.logging.ConsoleHandler.formatter = org.jitsi.utils.logging2.JitsiLogFormatter
java.util.logging.ConsoleHandler.filter = org.jitsi.impl.protocol.xmpp.log.ExcludeXmppPackets

org.jitsi.utils.logging2.JitsiLogFormatter.programname=Jicofo
.level=INFO

# To enable XMPP packets logging add XmppPacketsFileHandler to the handlers property
org.jitsi.impl.protocol.xmpp.log.PacketDebugger.level=ALL
org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.pattern=/var/log/jitsi/jicofo-xmpp.log
org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.append=true
org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.limit=200000000
org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.count=3

# Sentry (uncomment handler to use)
io.sentry.jul.SentryHandler.level=WARNING

# uncomment to see how Jicofo talks to the JVB
#org.jitsi.impl.protocol.xmpp.colibri.level=ALL


## Service Jicofo


```text
$ systemctl status jicofo --no-pager
```
● jicofo.service - LSB: Jitsi conference Focus
     Loaded: loaded (/etc/init.d/jicofo; generated)
     Active: active (running) since Fri 2026-08-07 05:25:27 EDT; 1 day 1h ago
 Invocation: 58fa6f5e50ba41e79878f53f2a0a1c9b
       Docs: man:systemd-sysv-generator(8)
    Process: 748 ExecStart=/etc/init.d/jicofo start (code=exited, status=0/SUCCESS)
      Tasks: 37 (limit: 11719)
     Memory: 256.6M (peak: 263.8M)
        CPU: 51.888s
     CGroup: /system.slice/jicofo.service
             └─786 java -Xmx3072m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=jicofo -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/jicofo/logging.properties -Dconfig.file=/etc/jitsi/jicofo/jicofo.conf -cp /usr/share/jicofo/jicofo.jar:/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar:/usr/share/jicofo/lib/annotations-23.0.0.jar:/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar:/usr/share/jicofo/lib/commons-lang3-3.12.0.jar:/usr/share/jicofo/lib/config-1.4.3.jar:/usr/share/jicofo/lib/gson-2.8.5.jar:/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar:/usr/share/jicofo/lib/jackson-core-2.18.0.jar:/usr/share/jicofo/lib/jackson-databind-2.18.0.jar:/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar:/usr/share/jicofo/lib/jansi-2.4.1.jar:/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar:/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar:/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar:/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar:/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar:/usr/share/jicofo/lib/jjwt-api-0.12.6.jar:/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar:/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar:/usr/share/jicofo/lib/jna-5.9.0.jar:/usr/share/jicofo/lib/jsr305-3.0.2.jar:/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar:/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar:/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar:/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar:/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar:/usr/share/jicofo/lib/minidns-core-1.0.5.jar:/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar:/usr/share/jicofo/lib/precis-1.1.0.jar:/usr/share/jicofo/lib/sentry-5.4.0.jar:/usr/share/jicofo/lib/simpleclient-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar:/usr/share/jicofo/lib/slf4j-api-1.7.32.jar:/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar:/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar org.jitsi.jicofo.Main

Aug 07 05:25:27 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Aug 07 05:25:27 meet.civitas.local jicofo[748]: Starting jicofo: jicofo started.
Aug 07 05:25:27 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.


```text
$ systemctl cat jicofo
```
# /run/systemd/generator.late/jicofo.service
# Automatically generated by systemd-sysv-generator

[Unit]
Documentation=man:systemd-sysv-generator(8)
SourcePath=/etc/init.d/jicofo
Description=LSB: Jitsi conference Focus
Before=multi-user.target
Before=multi-user.target
Before=multi-user.target
Before=graphical.target
After=remote-fs.target

[Service]
Type=forking
Restart=no
TimeoutSec=5min
IgnoreSIGPIPE=no
KillMode=process
GuessMainPID=no
RemainAfterExit=yes
SuccessExitStatus=5 6
ExecStart=/etc/init.d/jicofo start
ExecStop=/etc/init.d/jicofo stop
ExecReload=/etc/init.d/jicofo reload



---

# 6. JITSI VIDEOBRIDGE (JVB)

**Date :** 2026-08-08 06:56:25 EDT


## Localisation


```text
$ find /etc/jitsi /usr/share/jitsi /usr/share/jitsi-videobridge /usr/lib/jitsi-videobridge -type f 2>/dev/null | sort | grep -Ei "videobridge|jvb|jitsi" || true
```
/etc/jitsi/jicofo/config
/etc/jitsi/jicofo/jicofo.conf
/etc/jitsi/jicofo/logging.properties
/etc/jitsi/meet/meet.civitas.local-config.js
/etc/jitsi/videobridge/config
/etc/jitsi/videobridge/jvb.conf
/etc/jitsi/videobridge/logging.properties
/usr/share/jitsi-videobridge/collect-dump-logs.sh
/usr/share/jitsi-videobridge/graceful_shutdown.sh
/usr/share/jitsi-videobridge/jitsi-videobridge.jar
/usr/share/jitsi-videobridge/jvb.sh
/usr/share/jitsi-videobridge/lib/annotations-24.1.0.jar
/usr/share/jitsi-videobridge/lib/aopalliance-repackaged-3.0.6.jar
/usr/share/jitsi-videobridge/lib/asm-9.9.1.jar
/usr/share/jitsi-videobridge/lib/asm-commons-9.9.1.jar
/usr/share/jitsi-videobridge/lib/asm-tree-9.9.1.jar
/usr/share/jitsi-videobridge/lib/bcpkix-jdk18on-1.83.jar
/usr/share/jitsi-videobridge/lib/bcprov-jdk18on-1.83.jar
/usr/share/jitsi-videobridge/lib/bctls-jdk18on-1.83.jar
/usr/share/jitsi-videobridge/lib/bcutil-jdk18on-1.83.jar
/usr/share/jitsi-videobridge/lib/cglib-nodep-2.2.jar
/usr/share/jitsi-videobridge/lib/checker-qual-3.43.0.jar
/usr/share/jitsi-videobridge/lib/commons-lang3-3.12.0.jar
/usr/share/jitsi-videobridge/lib/config-1.4.2.jar
/usr/share/jitsi-videobridge/lib/error_prone_annotations-2.36.0.jar
/usr/share/jitsi-videobridge/lib/failureaccess-1.0.2.jar
/usr/share/jitsi-videobridge/lib/guava-33.4.0-jre.jar
/usr/share/jitsi-videobridge/lib/hk2-api-3.0.6.jar
/usr/share/jitsi-videobridge/lib/hk2-locator-3.0.6.jar
/usr/share/jitsi-videobridge/lib/hk2-utils-3.0.6.jar
/usr/share/jitsi-videobridge/lib/ice4j-3.2-15-g6da2b08.jar
/usr/share/jitsi-videobridge/lib/j2objc-annotations-3.0.0.jar
/usr/share/jitsi-videobridge/lib/jackson-annotations-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jackson-core-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jackson-databind-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jackson-module-jakarta-xmlbind-annotations-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jackson-module-kotlin-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jain-sip-ri-ossonly-1.2.279-jitsi-oss1.jar
/usr/share/jitsi-videobridge/lib/jakarta.activation-api-2.1.3.jar
/usr/share/jitsi-videobridge/lib/jakarta.annotation-api-2.1.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.el-api-5.0.0.jar
/usr/share/jitsi-videobridge/lib/jakarta.enterprise.cdi-api-4.0.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.enterprise.lang-model-4.0.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.inject-api-2.0.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.interceptor-api-2.1.0.jar
/usr/share/jitsi-videobridge/lib/jakarta.servlet-api-6.0.0.jar
/usr/share/jitsi-videobridge/lib/jakarta.transaction-api-2.0.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.validation-api-3.0.2.jar
/usr/share/jitsi-videobridge/lib/jakarta.ws.rs-api-3.1.0.jar
/usr/share/jitsi-videobridge/lib/jakarta.xml.bind-api-4.0.2.jar
/usr/share/jitsi-videobridge/lib/java-sdp-nist-bridge-1.2.jar
/usr/share/jitsi-videobridge/lib/javassist-3.28.0-GA.jar
/usr/share/jitsi-videobridge/lib/jcl-core-2.8.jar
/usr/share/jitsi-videobridge/lib/jersey-client-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-common-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-container-jetty-http-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-container-servlet-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-container-servlet-core-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-entity-filtering-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-hk2-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-media-json-jackson-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-server-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jetty-alpn-client-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-client-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-annotations-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-plus-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-servlet-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-servlets-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-webapp-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-websocket-jetty-server-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-websocket-servlet-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-http-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-io-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-jndi-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-plus-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-proxy-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-rewrite-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-security-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-server-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-session-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-util-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-core-client-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-core-common-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-core-server-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-jetty-api-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-jetty-client-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-jetty-common-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-xml-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jicoco-config-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-health-checker-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-jetty-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-mediajson-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-metrics-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-mucclient-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jitsi-dcsctp-1.0-7-gb548df2.jar
/usr/share/jitsi-videobridge/lib/jitsi-media-transform-2.3-307-g4bb0aead1.jar
/usr/share/jitsi-videobridge/lib/jitsi-metaconfig-1.0-11-g8cf950e.jar
/usr/share/jitsi-videobridge/lib/jitsi-srtp-1.1-23-gaf3cd06.jar
/usr/share/jitsi-videobridge/lib/jitsi-utils-1.0-150-g4ab9a3b.jar
/usr/share/jitsi-videobridge/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar
/usr/share/jitsi-videobridge/lib/jna-5.9.0.jar
/usr/share/jitsi-videobridge/lib/jsr305-3.0.2.jar
/usr/share/jitsi-videobridge/lib/jxmpp-core-1.0.3.jar
/usr/share/jitsi-videobridge/lib/jxmpp-jid-1.0.3.jar
/usr/share/jitsi-videobridge/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar
/usr/share/jitsi-videobridge/lib/jxmpp-util-cache-1.0.3.jar
/usr/share/jitsi-videobridge/lib/kotlin-reflect-2.2.20.jar
/usr/share/jitsi-videobridge/lib/kotlin-stdlib-2.2.20.jar
/usr/share/jitsi-videobridge/lib/kotlin-stdlib-jdk7-1.9.10.jar
/usr/share/jitsi-videobridge/lib/kotlin-stdlib-jdk8-1.9.10.jar
/usr/share/jitsi-videobridge/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
/usr/share/jitsi-videobridge/lib/minidns-core-1.0.5.jar
/usr/share/jitsi-videobridge/lib/object-cloner-0.1.jar
/usr/share/jitsi-videobridge/lib/objenesis-2.1.jar
/usr/share/jitsi-videobridge/lib/osgi-resource-locator-1.0.3.jar
/usr/share/jitsi-videobridge/lib/pcap4j-core-1.8.2.jar
/usr/share/jitsi-videobridge/lib/pcap4j-packetfactory-static-1.8.2.jar
/usr/share/jitsi-videobridge/lib/precis-1.1.0.jar
/usr/share/jitsi-videobridge/lib/reflections-0.9.11.jar
/usr/share/jitsi-videobridge/lib/rtp-2.3-307-g4bb0aead1.jar
/usr/share/jitsi-videobridge/lib/sdp-api-1.0.jar
/usr/share/jitsi-videobridge/lib/sentry-7.20.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient-0.16.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient_common-0.16.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient_tracer_common-0.16.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient_tracer_otel-0.16.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient_tracer_otel_agent-0.16.0.jar
/usr/share/jitsi-videobridge/lib/slf4j-api-2.0.16.jar
/usr/share/jitsi-videobridge/lib/slf4j-jdk14-2.0.16.jar
/usr/share/jitsi-videobridge/lib/smack-core-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-extensions-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-im-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-java8-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-resolver-javax-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-sasl-javax-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-streammanagement-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-tcp-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-xmlparser-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smjni-jnigen-annotations-3.9.jar
/usr/share/jitsi-videobridge/lib/smjni-jnigen-processor-3.9.jar
/usr/share/jitsi-videobridge/lib/spotbugs-annotations-4.9.4.jar
/usr/share/jitsi-videobridge/lib/videobridge.rc
/usr/share/jitsi-videobridge/lib/weupnp-0.1.4.jar


## Configuration JVB


```text
$ find /etc/jitsi/videobridge -maxdepth 5 -type f -print 2>/dev/null || true
```
/etc/jitsi/videobridge/jvb.conf
/etc/jitsi/videobridge/config
/etc/jitsi/videobridge/logging.properties


## Configurations JVB


```text
$ for f in /etc/jitsi/videobridge/*; do [ -f "$f" ] && { echo "===== $f ====="; sed -n "1,260p" "$f"; }; done
```
===== /etc/jitsi/videobridge/config =====

# adds java system props that are passed to jvb (default are for home and logging config file)
JAVA_SYS_PROPS="-Dconfig.file=/etc/jitsi/videobridge/jvb.conf -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=videobridge -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/videobridge/logging.properties"
===== /etc/jitsi/videobridge/jvb.conf =====
videobridge {
    http-servers {
        public {
            port = 9090
        }
    }
    websockets {
        enabled = true
        domain = "meet.civitas.local:443"
        tls = true
    }
    apis.xmpp-client.configs {
        shard {
            HOSTNAME=localhost
            DOMAIN="auth.meet.civitas.local"
            USERNAME=jvb
            PASSWORD="eH8fQtA1"
            MUC_JIDS="jvbbrewery@internal.auth.meet.civitas.local"
            MUC_NICKNAME=930940fd-c7d5-497d-9599-e2314adbf95b
        }
    }
}
ice4j {
    harvest {
        mapping {
            aws {
                enabled = false
            }
            stun {
                addresses = ["meet-jit-si-turnrelay.jitsi.net:443"]
            }
        }
    }
}
===== /etc/jitsi/videobridge/logging.properties =====
handlers= java.util.logging.ConsoleHandler
#handlers= java.util.logging.ConsoleHandler, io.sentry.jul.SentryHandler

java.util.logging.ConsoleHandler.level = ALL
java.util.logging.ConsoleHandler.formatter = org.jitsi.utils.logging2.JitsiLogFormatter

org.jitsi.utils.logging2.JitsiLogFormatter.programname=JVB
.level=INFO

# Sentry (uncomment handler to use)
io.sentry.jul.SentryHandler.level=WARNING

# time series logging
java.util.logging.SimpleFormatter.format= %5$s%n
java.util.logging.FileHandler.level = ALL
java.util.logging.FileHandler.formatter = java.util.logging.SimpleFormatter
java.util.logging.FileHandler.pattern = /tmp/jvb-series.log
java.util.logging.FileHandler.limit = 200000000
java.util.logging.FileHandler.count = 1
java.util.logging.FileHandler.append = false

timeseries.level=OFF
timeseries.useParentHandlers = false
# time series logging is disabled by default. Uncomment the line below to enable it.
#timeseries.handlers = java.util.logging.FileHandler


## JVB service


```text
$ systemctl status jitsi-videobridge2 --no-pager
```
● jitsi-videobridge2.service - Jitsi Videobridge
     Loaded: loaded (/usr/lib/systemd/system/jitsi-videobridge2.service; enabled; preset: enabled)
    Drop-In: /etc/systemd/system/jitsi-videobridge2.service.d
             └─override.conf
     Active: active (running) since Fri 2026-08-07 05:25:31 EDT; 1 day 1h ago
 Invocation: a874d1f62f09442dbb84e8c7f0d5b7f6
    Process: 1163 ExecStartPost=/bin/bash -c echo $MAINPID > /var/run/jitsi-videobridge/jitsi-videobridge.pid (code=exited, status=0/SUCCESS)
   Main PID: 1162 (java)
      Tasks: 52 (limit: 65000)
     Memory: 250.1M (peak: 260.1M)
        CPU: 1min 20.865s
     CGroup: /system.slice/jitsi-videobridge2.service
             └─1162 java -Xmx3072m -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dconfig.file=/etc/jitsi/videobridge/jvb.conf -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=videobridge -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/videobridge/logging.properties -cp "/usr/share/jitsi-videobridge/jitsi-videobridge.jar:/usr/share/jitsi-videobridge/lib/*" org.jitsi.videobridge.MainKt

Aug 07 05:25:31 meet.civitas.local systemd[1]: Starting jitsi-videobridge2.service - Jitsi Videobridge...
Aug 07 05:25:31 meet.civitas.local (bash)[1162]: jitsi-videobridge2.service: Referenced but unset environment variable evaluates to an empty string: JVB_OPTS
Aug 07 05:25:31 meet.civitas.local systemd[1]: Started jitsi-videobridge2.service - Jitsi Videobridge.


```text
$ systemctl cat jitsi-videobridge2
```
# /usr/lib/systemd/system/jitsi-videobridge2.service
[Unit]
Description=Jitsi Videobridge
After=network-online.target
Wants=network-online.target

[Service]
SuccessExitStatus=143
# configuration error prevents restart loops
RestartPreventExitStatus=78
# allow bind to 80 and 443
AmbientCapabilities=CAP_NET_BIND_SERVICE
EnvironmentFile=/etc/jitsi/videobridge/config
Environment=LOGFILE=/var/log/jitsi/jvb.log
User=jvb
RuntimeDirectory=jitsi-videobridge
RuntimeDirectoryMode=0750
PIDFile=/var/run/jitsi-videobridge/jitsi-videobridge.pid
# more threads for this process
TasksMax=65000
# allow more open files for this process
LimitNPROC=65000
LimitNOFILE=65000
ExecStart=/bin/bash -c "exec /usr/share/jitsi-videobridge/jvb.sh ${JVB_OPTS} < /dev/null >> ${LOGFILE} 2>&1"
ExecStartPost=/bin/bash -c "echo $MAINPID > /var/run/jitsi-videobridge/jitsi-videobridge.pid"
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target

# /etc/systemd/system/jitsi-videobridge2.service.d/override.conf
[Unit]
# S'assurer que Prosody et le réseau sont prêts avant JVB
After=network-online.target prosody.service jicofo.service
Requires=network-online.target prosody.service

[Service]
# Redémarrer automatiquement si crash
Restart=on-failure
RestartSec=10
# Attendre jusqu'à 3 minutes au boot
TimeoutStartSec=180



---

# 7. JITSI MEET WEB

**Date :** 2026-08-08 06:56:25 EDT


## Répertoires


```text
$ find /usr/share/jitsi-meet /etc/jitsi-meet /var/lib/jitsi-meet -maxdepth 4 -print 2>/dev/null || true
```
/usr/share/jitsi-meet
/usr/share/jitsi-meet/plugin.head.html
/usr/share/jitsi-meet/fonts
/usr/share/jitsi-meet/fonts/.placeholder
/usr/share/jitsi-meet/body.html
/usr/share/jitsi-meet/head.html
/usr/share/jitsi-meet/robots.txt
/usr/share/jitsi-meet/manifest.json
/usr/share/jitsi-meet/sounds
/usr/share/jitsi-meet/sounds/reactions-love.opus
/usr/share/jitsi-meet/sounds/joined.mp3
/usr/share/jitsi-meet/sounds/incomingMessage.mp3
/usr/share/jitsi-meet/sounds/recordingOn_frCA.opus
/usr/share/jitsi-meet/sounds/outgoingRinging.opus
/usr/share/jitsi-meet/sounds/reactions-thumbs-up.opus
/usr/share/jitsi-meet/sounds/left.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn.mp3
/usr/share/jitsi-meet/sounds/e2eeOff_fr.opus
/usr/share/jitsi-meet/sounds/liveStreamingOff_fr.opus
/usr/share/jitsi-meet/sounds/reactions-crickets.mp3
/usr/share/jitsi-meet/sounds/talkWhileMuted.opus
/usr/share/jitsi-meet/sounds/liveStreamingOff_frCA.opus
/usr/share/jitsi-meet/sounds/incomingMessage.opus
/usr/share/jitsi-meet/sounds/reactions-surprise.opus
/usr/share/jitsi-meet/sounds/reactions-crickets.opus
/usr/share/jitsi-meet/sounds/transcriptionOn_fr.mp3
/usr/share/jitsi-meet/sounds/liveStreamingOn_fr.opus
/usr/share/jitsi-meet/sounds/asked-unmute.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff.mp3
/usr/share/jitsi-meet/sounds/talkWhileMuted.mp3
/usr/share/jitsi-meet/sounds/incomingMessage.wav
/usr/share/jitsi-meet/sounds/liveStreamingOn_frCA.opus
/usr/share/jitsi-meet/sounds/transcriptionOn_frCA.mp3
/usr/share/jitsi-meet/sounds/e2eeOn_fr.opus
/usr/share/jitsi-meet/sounds/reactions-surprise.mp3
/usr/share/jitsi-meet/sounds/e2eeOff.opus
/usr/share/jitsi-meet/sounds/liveStreamingOn.opus
/usr/share/jitsi-meet/sounds/liveStreamingOn_frCA.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff_fr.mp3
/usr/share/jitsi-meet/sounds/recordingOff_fr.opus
/usr/share/jitsi-meet/sounds/recordingOn_fr.opus
/usr/share/jitsi-meet/sounds/recordingOn.mp3
/usr/share/jitsi-meet/sounds/e2eeOff_fr.mp3
/usr/share/jitsi-meet/sounds/reactions-raised-hand.opus
/usr/share/jitsi-meet/sounds/recordingOff.opus
/usr/share/jitsi-meet/sounds/reactions-boo.opus
/usr/share/jitsi-meet/sounds/liveStreamingOff_fr.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn_fr.mp3
/usr/share/jitsi-meet/sounds/e2eeOn.opus
/usr/share/jitsi-meet/sounds/transcriptionOff.mp3
/usr/share/jitsi-meet/sounds/e2eeOff.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff_frCA.mp3
/usr/share/jitsi-meet/sounds/rejected.opus
/usr/share/jitsi-meet/sounds/left.opus
/usr/share/jitsi-meet/sounds/transcriptionOn.mp3
/usr/share/jitsi-meet/sounds/asked-unmute.opus
/usr/share/jitsi-meet/sounds/reactions-raised-hand.mp3
/usr/share/jitsi-meet/sounds/e2eeOn_fr.mp3
/usr/share/jitsi-meet/sounds/left.wav
/usr/share/jitsi-meet/sounds/reactions-applause.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn_frCA.mp3
/usr/share/jitsi-meet/sounds/README.md
/usr/share/jitsi-meet/sounds/noAudioSignal.mp3
/usr/share/jitsi-meet/sounds/noAudioSignal.opus
/usr/share/jitsi-meet/sounds/recordingOn_fr.mp3
/usr/share/jitsi-meet/sounds/ring.opus
/usr/share/jitsi-meet/sounds/transcriptionOff.opus
/usr/share/jitsi-meet/sounds/ring.wav
/usr/share/jitsi-meet/sounds/recordingOn.opus
/usr/share/jitsi-meet/sounds/transcriptionOff_fr.mp3
/usr/share/jitsi-meet/sounds/ring.mp3
/usr/share/jitsi-meet/sounds/transcriptionOn_frCA.opus
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff_frCA.opus
/usr/share/jitsi-meet/sounds/reactions-love.mp3
/usr/share/jitsi-meet/sounds/transcriptionOff_frCA.mp3
/usr/share/jitsi-meet/sounds/liveStreamingOn.mp3
/usr/share/jitsi-meet/sounds/joined.opus
/usr/share/jitsi-meet/sounds/liveStreamingOff_frCA.mp3
/usr/share/jitsi-meet/sounds/reactions-laughter.opus
/usr/share/jitsi-meet/sounds/e2eeOff_frCA.opus
/usr/share/jitsi-meet/sounds/reactions-thumbs-up.mp3
/usr/share/jitsi-meet/sounds/recordingOff_fr.mp3
/usr/share/jitsi-meet/sounds/transcriptionOff_fr.opus
/usr/share/jitsi-meet/sounds/recordingOn_frCA.mp3
/usr/share/jitsi-meet/sounds/recordingOff_frCA.mp3
/usr/share/jitsi-meet/sounds/e2eeOn_frCA.mp3
/usr/share/jitsi-meet/sounds/outgoingStart.wav
/usr/share/jitsi-meet/sounds/recordingOff.mp3
/usr/share/jitsi-meet/sounds/knock.mp3
/usr/share/jitsi-meet/sounds/outgoingRinging.wav
/usr/share/jitsi-meet/sounds/reactions-applause.opus
/usr/share/jitsi-meet/sounds/liveStreamingOff.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn.opus
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn_frCA.opus
/usr/share/jitsi-meet/sounds/noisyAudioInput.mp3
/usr/share/jitsi-meet/sounds/joined.wav
/usr/share/jitsi-meet/sounds/liveStreamingOff.opus
/usr/share/jitsi-meet/sounds/e2eeOn.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn_fr.opus
/usr/share/jitsi-meet/sounds/outgoingStart.mp3
/usr/share/jitsi-meet/sounds/reactions-boo.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff_fr.opus
/usr/share/jitsi-meet/sounds/reactions-laughter.mp3
/usr/share/jitsi-meet/sounds/e2eeOn_frCA.opus
/usr/share/jitsi-meet/sounds/outgoingStart.opus
/usr/share/jitsi-meet/sounds/outgoingRinging.mp3
/usr/share/jitsi-meet/sounds/noisyAudioInput.opus
/usr/share/jitsi-meet/sounds/rejected.mp3
/usr/share/jitsi-meet/sounds/transcriptionOff_frCA.opus
/usr/share/jitsi-meet/sounds/rejected.wav
/usr/share/jitsi-meet/sounds/liveStreamingOn_fr.mp3
/usr/share/jitsi-meet/sounds/recordingOff_frCA.opus
/usr/share/jitsi-meet/sounds/e2eeOff_frCA.mp3
/usr/share/jitsi-meet/sounds/transcriptionOn_fr.opus
/usr/share/jitsi-meet/sounds/knock.opus
/usr/share/jitsi-meet/sounds/transcriptionOn.opus
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff.opus
/usr/share/jitsi-meet/scripts
/usr/share/jitsi-meet/scripts/update-mobile-rnsdk-version.sh
/usr/share/jitsi-meet/scripts/update-asap-daily.sh
/usr/share/jitsi-meet/scripts/register-jaas-account.sh
/usr/share/jitsi-meet/scripts/encode-sound.sh
/usr/share/jitsi-meet/scripts/update-mobile-sdk-version.sh
/usr/share/jitsi-meet/scripts/move-to-jaas.sh
/usr/share/jitsi-meet/scripts/update-mobile-version.sh
/usr/share/jitsi-meet/scripts/lang-sort.sh
/usr/share/jitsi-meet/scripts/install-letsencrypt-cert.sh
/usr/share/jitsi-meet/scripts/update-ljm.sh
/usr/share/jitsi-meet/scripts/coturn-le-update.sh
/usr/share/jitsi-meet/pwa-worker.js
/usr/share/jitsi-meet/index.html
/usr/share/jitsi-meet/static
/usr/share/jitsi-meet/static/planLimit.html
/usr/share/jitsi-meet/static/prejoin.html
/usr/share/jitsi-meet/static/webrtcUnsupported.html
/usr/share/jitsi-meet/static/404.html
/usr/share/jitsi-meet/static/close2.html
/usr/share/jitsi-meet/static/whiteboard.html
/usr/share/jitsi-meet/static/close3.js
/usr/share/jitsi-meet/static/recommendedBrowsers.html
/usr/share/jitsi-meet/static/pwa
/usr/share/jitsi-meet/static/pwa/icons
/usr/share/jitsi-meet/static/pwa/icons/icon512.png
/usr/share/jitsi-meet/static/pwa/icons/iconMask.png
/usr/share/jitsi-meet/static/pwa/icons/icon192.png
/usr/share/jitsi-meet/static/dialInInfo.html
/usr/share/jitsi-meet/static/close.html
/usr/share/jitsi-meet/static/offline.html
/usr/share/jitsi-meet/static/close3.html
/usr/share/jitsi-meet/static/oauth.html
/usr/share/jitsi-meet/static/welcomePageAdditionalContent.html
/usr/share/jitsi-meet/static/logout.html
/usr/share/jitsi-meet/static/sso.html
/usr/share/jitsi-meet/static/settingsToolbarAdditionalContent.html
/usr/share/jitsi-meet/static/close.js
/usr/share/jitsi-meet/static/msredirect.html
/usr/share/jitsi-meet/static/welcomePageAdditionalCard.html
/usr/share/jitsi-meet/base.html
/usr/share/jitsi-meet/interface_config.js
/usr/share/jitsi-meet/css
/usr/share/jitsi-meet/css/all.css
/usr/share/jitsi-meet/title.html
/usr/share/jitsi-meet/lang
/usr/share/jitsi-meet/lang/countries-sr.json
/usr/share/jitsi-meet/lang/main-oc.json
/usr/share/jitsi-meet/lang/countries-fr-CA.json
/usr/share/jitsi-meet/lang/main-es-US.json
/usr/share/jitsi-meet/lang/countries-de.json
/usr/share/jitsi-meet/lang/countries-es.json
/usr/share/jitsi-meet/lang/main-dsb.json
/usr/share/jitsi-meet/lang/main-ko.json
/usr/share/jitsi-meet/lang/main-it.json
/usr/share/jitsi-meet/lang/main-sq.json
/usr/share/jitsi-meet/lang/main-el.json
/usr/share/jitsi-meet/lang/main-gl.json
/usr/share/jitsi-meet/lang/translation-languages.json
/usr/share/jitsi-meet/lang/countries-be.json
/usr/share/jitsi-meet/lang/main-mn.json
/usr/share/jitsi-meet/lang/main-fi.json
/usr/share/jitsi-meet/lang/countries-sq.json
/usr/share/jitsi-meet/lang/main-hr.json
/usr/share/jitsi-meet/lang/countries-lt.json
/usr/share/jitsi-meet/lang/main-vi.json
/usr/share/jitsi-meet/lang/countries-no.json
/usr/share/jitsi-meet/lang/main-be.json
/usr/share/jitsi-meet/lang/main-tr.json
/usr/share/jitsi-meet/lang/countries-is.json
/usr/share/jitsi-meet/lang/countries-cs.json
/usr/share/jitsi-meet/lang/main-kab.json
/usr/share/jitsi-meet/lang/countries-et.json
/usr/share/jitsi-meet/lang/countries-hi.json
/usr/share/jitsi-meet/lang/main.json
/usr/share/jitsi-meet/lang/countries-fa.json
/usr/share/jitsi-meet/lang/main-nl.json
/usr/share/jitsi-meet/lang/main-et.json
/usr/share/jitsi-meet/lang/main-id.json
/usr/share/jitsi-meet/lang/countries-hr.json
/usr/share/jitsi-meet/lang/main-de.json
/usr/share/jitsi-meet/lang/countries-hy.json
/usr/share/jitsi-meet/lang/main-fa.json
/usr/share/jitsi-meet/lang/countries-tr.json
/usr/share/jitsi-meet/lang/countries-pt.json
/usr/share/jitsi-meet/lang/countries-gl.json
/usr/share/jitsi-meet/lang/countries-pt-BR.json
/usr/share/jitsi-meet/lang/main-da.json
/usr/share/jitsi-meet/lang/main-sl.json
/usr/share/jitsi-meet/lang/main-zh-TW.json
/usr/share/jitsi-meet/lang/main-lv.json
/usr/share/jitsi-meet/lang/main-nb.json
/usr/share/jitsi-meet/lang/main-bg.json
/usr/share/jitsi-meet/lang/main-fr-CA.json
/usr/share/jitsi-meet/lang/main-kk.json
/usr/share/jitsi-meet/lang/countries-pl.json
/usr/share/jitsi-meet/lang/countries-en.json
/usr/share/jitsi-meet/lang/countries-eu.json
/usr/share/jitsi-meet/lang/countries-kab.json
/usr/share/jitsi-meet/lang/update-translation.js
/usr/share/jitsi-meet/lang/main-hi.json
/usr/share/jitsi-meet/lang/main-ja.json
/usr/share/jitsi-meet/lang/main-hu.json
/usr/share/jitsi-meet/lang/countries-uk.json
/usr/share/jitsi-meet/lang/countries-mn.json
/usr/share/jitsi-meet/lang/countries-sv.json
/usr/share/jitsi-meet/lang/main-cs.json
/usr/share/jitsi-meet/lang/main-sc.json
/usr/share/jitsi-meet/lang/main-sv.json
/usr/share/jitsi-meet/lang/main-pt.json
/usr/share/jitsi-meet/lang/main-pt-BR.json
/usr/share/jitsi-meet/lang/countries-vi.json
/usr/share/jitsi-meet/lang/countries-kk.json
/usr/share/jitsi-meet/lang/main-hy.json
/usr/share/jitsi-meet/lang/main-fr.json
/usr/share/jitsi-meet/lang/countries-ro.json
/usr/share/jitsi-meet/lang/main-pl.json
/usr/share/jitsi-meet/lang/main-af.json
/usr/share/jitsi-meet/lang/countries-bg.json
/usr/share/jitsi-meet/lang/main-lt.json
/usr/share/jitsi-meet/lang/main-is.json
/usr/share/jitsi-meet/lang/countries-id.json
/usr/share/jitsi-meet/lang/main-sr.json
/usr/share/jitsi-meet/lang/countries-nb.json
/usr/share/jitsi-meet/lang/countries-sk.json
/usr/share/jitsi-meet/lang/main-sk.json
/usr/share/jitsi-meet/lang/countries-zh-TW.json
/usr/share/jitsi-meet/lang/main-zh-CN.json
/usr/share/jitsi-meet/lang/main-ml.json
/usr/share/jitsi-meet/lang/main-no.json
/usr/share/jitsi-meet/lang/countries-nl.json
/usr/share/jitsi-meet/lang/countries-ml.json
/usr/share/jitsi-meet/lang/countries-he.json
/usr/share/jitsi-meet/lang/countries-ar.json
/usr/share/jitsi-meet/lang/countries-ja.json
/usr/share/jitsi-meet/lang/countries-fr.json
/usr/share/jitsi-meet/lang/countries-ru.json
/usr/share/jitsi-meet/lang/countries-lv.json
/usr/share/jitsi-meet/lang/countries-zh-CN.json
/usr/share/jitsi-meet/lang/main-ru.json
/usr/share/jitsi-meet/lang/countries-it.json
/usr/share/jitsi-meet/lang/main-ca.json
/usr/share/jitsi-meet/lang/main-hsb.json
/usr/share/jitsi-meet/lang/main-he.json
/usr/share/jitsi-meet/lang/main-eu.json
/usr/share/jitsi-meet/lang/main-ro.json
/usr/share/jitsi-meet/lang/countries-es-US.json
/usr/share/jitsi-meet/lang/countries-ca.json
/usr/share/jitsi-meet/lang/main-es.json
/usr/share/jitsi-meet/lang/main-uk.json
/usr/share/jitsi-meet/lang/countries-ko.json
/usr/share/jitsi-meet/lang/main-eo.json
/usr/share/jitsi-meet/lang/main-mr.json
/usr/share/jitsi-meet/lang/countries-hu.json
/usr/share/jitsi-meet/lang/countries-el.json
/usr/share/jitsi-meet/lang/countries-da.json
/usr/share/jitsi-meet/lang/languages.json
/usr/share/jitsi-meet/lang/readme.md
/usr/share/jitsi-meet/lang/main-te.json
/usr/share/jitsi-meet/lang/countries-sl.json
/usr/share/jitsi-meet/lang/countries-af.json
/usr/share/jitsi-meet/lang/main-ar.json
/usr/share/jitsi-meet/lang/countries-fi.json
/usr/share/jitsi-meet/prosody-plugins
/usr/share/jitsi-meet/prosody-plugins/mod_measure_message_count.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jitsi_session.lua
/usr/share/jitsi-meet/prosody-plugins/luajwtjitsi.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_conference_duration.lua
/usr/share/jitsi-meet/prosody-plugins/mod_speakerstats_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_token_verification.lua
/usr/share/jitsi-meet/prosody-plugins/mod_test_observer_http.lua
/usr/share/jitsi-meet/prosody-plugins/mod_visitors.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_census.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_resource_validate.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_jitsi-anonymous.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_meeting_id.lua
/usr/share/jitsi-meet/prosody-plugins/mod_system_chat_message.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jiconop.lua
/usr/share/jitsi-meet/prosody-plugins/mod_turncredentials_http.lua
/usr/share/jitsi-meet/prosody-plugins/mod_features_identity.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_password_check.lua
/usr/share/jitsi-meet/prosody-plugins/mod_s2s_whitelist.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_flip.lua
/usr/share/jitsi-meet/prosody-plugins/mod_short_lived_token.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_webhook.lua
/usr/share/jitsi-meet/prosody-plugins/mod_limits_exception.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filter_messages.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filter_iq_jibri.lua
/usr/share/jitsi-meet/prosody-plugins/mod_secure_interfaces.lua
/usr/share/jitsi-meet/prosody-plugins/mod_certs_s2soutinjection.lua
/usr/share/jitsi-meet/prosody-plugins/mod_room_metadata_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_kick_participant.lua
/usr/share/jitsi-meet/prosody-plugins/mod_roster_command.patch
/usr/share/jitsi-meet/prosody-plugins/mod_muc_domain_mapper.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jibri_session.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filesharing_component.lua
/usr/share/jitsi-meet/prosody-plugins/muc_owner_allow_kick-0.12.patch
/usr/share/jitsi-meet/prosody-plugins/README.md
/usr/share/jitsi-meet/prosody-plugins/mod_firewall
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/actions.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/marks.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/definitions.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/test.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/mod_firewall.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/conditions.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_debug_traceback.lua
/usr/share/jitsi-meet/prosody-plugins/mod_room_destroy.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_hide_all.lua
/usr/share/jitsi-meet/prosody-plugins/mod_test_observer.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_cleanup_backend_services.lua
/usr/share/jitsi-meet/prosody-plugins/mod_polls_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_roster_command.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_lobby_rooms.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_jitsi-shared-secret.lua
/usr/share/jitsi-meet/prosody-plugins/token
/usr/share/jitsi-meet/prosody-plugins/token/jwk.lib.lua
/usr/share/jitsi-meet/prosody-plugins/token/util.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_token.lua
/usr/share/jitsi-meet/prosody-plugins/mod_av_moderation_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_end_conference.lua
/usr/share/jitsi-meet/prosody-plugins/mod_reservations.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_size.lua
/usr/share/jitsi-meet/prosody-plugins/util.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_log_ringbuffer.lua
/usr/share/jitsi-meet/prosody-plugins/mod_visitors_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_wait_for_host.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jitsi_permissions.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_end_meeting.lua
/usr/share/jitsi-meet/prosody-plugins/mod_fmuc.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_breakout_rooms.lua
/usr/share/jitsi-meet/prosody-plugins/mod_rate_limit.lua
/usr/share/jitsi-meet/prosody-plugins/mod_measure_stanza_counts.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_filter_access.lua
/usr/share/jitsi-meet/prosody-plugins/mod_persistent_lobby.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_displayname.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_password_whitelist.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_allowners.lua
/usr/share/jitsi-meet/prosody-plugins/mod_audio_translation_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_token_affiliation.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filter_iq_rayo.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_rate_limit.lua
/usr/share/jitsi-meet/prosody-plugins/mod_presence_identity.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_jigasi_invite.lua
/usr/share/jitsi-meet/prosody-plugins/mod_s2sout_override.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_limit_messages.lua
/usr/share/jitsi-meet/prosody-plugins/stanza_router_no-log.patch
/usr/share/jitsi-meet/prosody-plugins/mod_muc_max_occupants.lua
/usr/share/jitsi-meet/prosody-plugins/mod_client_proxy.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_auth_ban.lua
/usr/share/jitsi-meet/images
/usr/share/jitsi-meet/images/app-store-badge.png
/usr/share/jitsi-meet/images/logo-deep-linking-mobile.png
/usr/share/jitsi-meet/images/icon-cloud.png
/usr/share/jitsi-meet/images/dropboxLogo_square.png
/usr/share/jitsi-meet/images/GIPHY_icon.png
/usr/share/jitsi-meet/images/virtual-background
/usr/share/jitsi-meet/images/virtual-background/background-3.jpg
/usr/share/jitsi-meet/images/virtual-background/background-2.jpg
/usr/share/jitsi-meet/images/virtual-background/background-5.jpg
/usr/share/jitsi-meet/images/virtual-background/background-6.jpg
/usr/share/jitsi-meet/images/virtual-background/background-1.jpg
/usr/share/jitsi-meet/images/virtual-background/background-4.jpg
/usr/share/jitsi-meet/images/virtual-background/background-7.jpg
/usr/share/jitsi-meet/images/downloadLocalRecording.png
/usr/share/jitsi-meet/images/btn_google_signin_dark_normal.png
/usr/share/jitsi-meet/images/avatar.png
/usr/share/jitsi-meet/images/flags.png
/usr/share/jitsi-meet/images/jitsilogo.png
/usr/share/jitsi-meet/images/chromeLogo.svg
/usr/share/jitsi-meet/images/share-audio.gif
/usr/share/jitsi-meet/images/apple-touch-icon.png
/usr/share/jitsi-meet/images/f-droid-badge.png
/usr/share/jitsi-meet/images/welcome-background.png
/usr/share/jitsi-meet/images/calendar.svg
/usr/share/jitsi-meet/images/logo-deep-linking.png
/usr/share/jitsi-meet/images/google-play-badge.png
/usr/share/jitsi-meet/images/icon-info.png
/usr/share/jitsi-meet/images/googleLogo.svg
/usr/share/jitsi-meet/images/flags@2x.png
/usr/share/jitsi-meet/images/microsoftLogo.svg
/usr/share/jitsi-meet/images/GIPHY_logo.png
/usr/share/jitsi-meet/images/favicon.svg
/usr/share/jitsi-meet/images/icon-users.png
/usr/share/jitsi-meet/images/watermark.svg
/usr/share/jitsi-meet/fonts.html
/usr/share/jitsi-meet/libs
/usr/share/jitsi-meet/libs/blazeface-front.bin
/usr/share/jitsi-meet/libs/noise-suppressor-worklet.min.js
/usr/share/jitsi-meet/libs/external_api.min.js.map
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.js
/usr/share/jitsi-meet/libs/tfjs-backend-wasm.wasm
/usr/share/jitsi-meet/libs/tflite-simd.wasm
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.map
/usr/share/jitsi-meet/libs/screenshot-capture-worker.min.js
/usr/share/jitsi-meet/libs/olm.wasm
/usr/share/jitsi-meet/libs/close3.min.js
/usr/share/jitsi-meet/libs/app.bundle.min.js.map
/usr/share/jitsi-meet/libs/emotion.bin
/usr/share/jitsi-meet/libs/blazeface-front.json
/usr/share/jitsi-meet/libs/tfjs-backend-wasm-threaded-simd.wasm
/usr/share/jitsi-meet/libs/chunks
/usr/share/jitsi-meet/libs/chunks/8298.min.js.map
/usr/share/jitsi-meet/libs/chunks/3347.min.js.map
/usr/share/jitsi-meet/libs/chunks/6770.min.js
/usr/share/jitsi-meet/libs/chunks/493.min.js.map
/usr/share/jitsi-meet/libs/chunks/1455.min.js
/usr/share/jitsi-meet/libs/chunks/9105.min.js.map
/usr/share/jitsi-meet/libs/chunks/9828.min.js
/usr/share/jitsi-meet/libs/chunks/1987.min.js
/usr/share/jitsi-meet/libs/chunks/8882.min.js.map
/usr/share/jitsi-meet/libs/chunks/9976.min.js.map
/usr/share/jitsi-meet/libs/chunks/1489.min.js.map
/usr/share/jitsi-meet/libs/chunks/1689.min.js
/usr/share/jitsi-meet/libs/chunks/2725.min.js
/usr/share/jitsi-meet/libs/chunks/5544.min.js
/usr/share/jitsi-meet/libs/chunks/9828.min.js.map
/usr/share/jitsi-meet/libs/chunks/3687.min.js
/usr/share/jitsi-meet/libs/chunks/9596.min.js
/usr/share/jitsi-meet/libs/chunks/3687.min.js.map
/usr/share/jitsi-meet/libs/chunks/6220.min.js.map
/usr/share/jitsi-meet/libs/chunks/8846.min.js
/usr/share/jitsi-meet/libs/chunks/8005.min.js
/usr/share/jitsi-meet/libs/chunks/4106.min.js.map
/usr/share/jitsi-meet/libs/chunks/3259.min.js.map
/usr/share/jitsi-meet/libs/chunks/7358.min.js.map
/usr/share/jitsi-meet/libs/chunks/3292.min.js.map
/usr/share/jitsi-meet/libs/chunks/1121.min.js.map
/usr/share/jitsi-meet/libs/chunks/6322.min.js.map
/usr/share/jitsi-meet/libs/chunks/1080.min.js
/usr/share/jitsi-meet/libs/chunks/4337.min.js.map
/usr/share/jitsi-meet/libs/chunks/239.min.js
/usr/share/jitsi-meet/libs/chunks/5301.min.js
/usr/share/jitsi-meet/libs/chunks/2803.min.js.map
/usr/share/jitsi-meet/libs/chunks/6322.min.js
/usr/share/jitsi-meet/libs/chunks/8528.min.js
/usr/share/jitsi-meet/libs/chunks/6586.min.js.map
/usr/share/jitsi-meet/libs/chunks/5301.min.js.map
/usr/share/jitsi-meet/libs/chunks/9612.min.js.map
/usr/share/jitsi-meet/libs/chunks/8146.min.js
/usr/share/jitsi-meet/libs/chunks/3292.min.js
/usr/share/jitsi-meet/libs/chunks/7897.min.js
/usr/share/jitsi-meet/libs/chunks/2203.min.js.map
/usr/share/jitsi-meet/libs/chunks/8024.min.js
/usr/share/jitsi-meet/libs/chunks/4695.min.js.map
/usr/share/jitsi-meet/libs/chunks/544.min.js.map
/usr/share/jitsi-meet/libs/chunks/3138.min.js.map
/usr/share/jitsi-meet/libs/chunks/1689.min.js.map
/usr/share/jitsi-meet/libs/chunks/1080.min.js.map
/usr/share/jitsi-meet/libs/chunks/6220.min.js
/usr/share/jitsi-meet/libs/chunks/9706.min.js
/usr/share/jitsi-meet/libs/chunks/544.min.js
/usr/share/jitsi-meet/libs/chunks/5860.min.js
/usr/share/jitsi-meet/libs/chunks/1329.min.js
/usr/share/jitsi-meet/libs/chunks/7256.min.js
/usr/share/jitsi-meet/libs/chunks/3567.min.js
/usr/share/jitsi-meet/libs/chunks/8890.min.js.map
/usr/share/jitsi-meet/libs/chunks/475.min.js
/usr/share/jitsi-meet/libs/chunks/5950.min.js.map
/usr/share/jitsi-meet/libs/chunks/7134.min.js
/usr/share/jitsi-meet/libs/chunks/796.min.js.map
/usr/share/jitsi-meet/libs/chunks/4130.min.js.map
/usr/share/jitsi-meet/libs/chunks/6625.min.js
/usr/share/jitsi-meet/libs/chunks/4259.min.js
/usr/share/jitsi-meet/libs/chunks/3659.min.js
/usr/share/jitsi-meet/libs/chunks/493.min.js
/usr/share/jitsi-meet/libs/chunks/247.min.js
/usr/share/jitsi-meet/libs/chunks/8882.min.js
/usr/share/jitsi-meet/libs/chunks/4207.min.js.map
/usr/share/jitsi-meet/libs/chunks/1060.min.js
/usr/share/jitsi-meet/libs/chunks/9698.min.js
/usr/share/jitsi-meet/libs/chunks/4104.min.js.map
/usr/share/jitsi-meet/libs/chunks/547.min.js
/usr/share/jitsi-meet/libs/chunks/5628.min.js
/usr/share/jitsi-meet/libs/chunks/5857.min.js.map
/usr/share/jitsi-meet/libs/chunks/167.min.js.map
/usr/share/jitsi-meet/libs/chunks/167.min.js
/usr/share/jitsi-meet/libs/chunks/5163.min.js.map
/usr/share/jitsi-meet/libs/chunks/8090.min.js
/usr/share/jitsi-meet/libs/chunks/5857.min.js
/usr/share/jitsi-meet/libs/chunks/8528.min.js.map
/usr/share/jitsi-meet/libs/chunks/3138.min.js
/usr/share/jitsi-meet/libs/chunks/4073.min.js
/usr/share/jitsi-meet/libs/chunks/3471.min.js
/usr/share/jitsi-meet/libs/chunks/239.min.js.map
/usr/share/jitsi-meet/libs/chunks/9698.min.js.map
/usr/share/jitsi-meet/libs/chunks/2144.min.js
/usr/share/jitsi-meet/libs/chunks/2775.min.js
/usr/share/jitsi-meet/libs/chunks/9890.min.js.map
/usr/share/jitsi-meet/libs/chunks/8989.min.js
/usr/share/jitsi-meet/libs/chunks/1121.min.js
/usr/share/jitsi-meet/libs/chunks/5322.min.js
/usr/share/jitsi-meet/libs/chunks/2130.min.js.map
/usr/share/jitsi-meet/libs/chunks/8995.min.js.map
/usr/share/jitsi-meet/libs/chunks/2603.min.js.map
/usr/share/jitsi-meet/libs/chunks/3417.min.js
/usr/share/jitsi-meet/libs/chunks/7358.min.js
/usr/share/jitsi-meet/libs/chunks/4690.min.js.map
/usr/share/jitsi-meet/libs/chunks/2203.min.js
/usr/share/jitsi-meet/libs/chunks/9013.min.js.map
/usr/share/jitsi-meet/libs/chunks/922.min.js
/usr/share/jitsi-meet/libs/chunks/5163.min.js
/usr/share/jitsi-meet/libs/chunks/1818.min.js
/usr/share/jitsi-meet/libs/chunks/9706.min.js.map
/usr/share/jitsi-meet/libs/chunks/2144.min.js.map
/usr/share/jitsi-meet/libs/chunks/5544.min.js.map
/usr/share/jitsi-meet/libs/chunks/7115.min.js
/usr/share/jitsi-meet/libs/chunks/7134.min.js.map
/usr/share/jitsi-meet/libs/chunks/4762.min.js
/usr/share/jitsi-meet/libs/chunks/9890.min.js
/usr/share/jitsi-meet/libs/chunks/9105.min.js
/usr/share/jitsi-meet/libs/chunks/1818.min.js.map
/usr/share/jitsi-meet/libs/chunks/3347.min.js
/usr/share/jitsi-meet/libs/chunks/922.min.js.map
/usr/share/jitsi-meet/libs/chunks/7897.min.js.map
/usr/share/jitsi-meet/libs/chunks/547.min.js.map
/usr/share/jitsi-meet/libs/chunks/4106.min.js
/usr/share/jitsi-meet/libs/chunks/5114.min.js.map
/usr/share/jitsi-meet/libs/chunks/2775.min.js.map
/usr/share/jitsi-meet/libs/chunks/5388.min.js.map
/usr/share/jitsi-meet/libs/chunks/3207.min.js
/usr/share/jitsi-meet/libs/chunks/1329.min.js.map
/usr/share/jitsi-meet/libs/chunks/3207.min.js.map
/usr/share/jitsi-meet/libs/chunks/8024.min.js.map
/usr/share/jitsi-meet/libs/chunks/5322.min.js.map
/usr/share/jitsi-meet/libs/chunks/475.min.js.map
/usr/share/jitsi-meet/libs/chunks/8995.min.js
/usr/share/jitsi-meet/libs/chunks/8846.min.js.map
/usr/share/jitsi-meet/libs/chunks/141.min.js
/usr/share/jitsi-meet/libs/chunks/141.min.js.map
/usr/share/jitsi-meet/libs/chunks/4104.min.js
/usr/share/jitsi-meet/libs/chunks/8090.min.js.map
/usr/share/jitsi-meet/libs/chunks/4762.min.js.map
/usr/share/jitsi-meet/libs/chunks/4226.min.js.map
/usr/share/jitsi-meet/libs/chunks/1060.min.js.map
/usr/share/jitsi-meet/libs/chunks/4564.min.js
/usr/share/jitsi-meet/libs/chunks/4564.min.js.map
/usr/share/jitsi-meet/libs/chunks/6675.min.js.map
/usr/share/jitsi-meet/libs/chunks/7256.min.js.map
/usr/share/jitsi-meet/libs/chunks/6625.min.js.map
/usr/share/jitsi-meet/libs/chunks/3471.min.js.map
/usr/share/jitsi-meet/libs/chunks/7899.min.js
/usr/share/jitsi-meet/libs/chunks/4690.min.js
/usr/share/jitsi-meet/libs/chunks/2783.min.js
/usr/share/jitsi-meet/libs/chunks/3760.min.js
/usr/share/jitsi-meet/libs/chunks/7899.min.js.map
/usr/share/jitsi-meet/libs/chunks/3645.min.js.map
/usr/share/jitsi-meet/libs/chunks/6586.min.js
/usr/share/jitsi-meet/libs/chunks/4256.min.js
/usr/share/jitsi-meet/libs/chunks/6675.min.js
/usr/share/jitsi-meet/libs/chunks/2130.min.js
/usr/share/jitsi-meet/libs/chunks/5628.min.js.map
/usr/share/jitsi-meet/libs/chunks/7690.min.js.map
/usr/share/jitsi-meet/libs/chunks/8032.min.js
/usr/share/jitsi-meet/libs/chunks/5950.min.js
/usr/share/jitsi-meet/libs/chunks/4256.min.js.map
/usr/share/jitsi-meet/libs/chunks/4226.min.js
/usr/share/jitsi-meet/libs/chunks/971.min.js
/usr/share/jitsi-meet/libs/chunks/5388.min.js
/usr/share/jitsi-meet/libs/chunks/8298.min.js
/usr/share/jitsi-meet/libs/chunks/4130.min.js
/usr/share/jitsi-meet/libs/chunks/796.min.js
/usr/share/jitsi-meet/libs/chunks/8146.min.js.map
/usr/share/jitsi-meet/libs/chunks/6770.min.js.map
/usr/share/jitsi-meet/libs/chunks/5713.min.js.map
/usr/share/jitsi-meet/libs/chunks/4337.min.js
/usr/share/jitsi-meet/libs/chunks/4337.min.js.LICENSE.txt
/usr/share/jitsi-meet/libs/chunks/8890.min.js
/usr/share/jitsi-meet/libs/chunks/7185.min.js.map
/usr/share/jitsi-meet/libs/chunks/4207.min.js
/usr/share/jitsi-meet/libs/chunks/2803.min.js
/usr/share/jitsi-meet/libs/chunks/7690.min.js
/usr/share/jitsi-meet/libs/chunks/4073.min.js.map
/usr/share/jitsi-meet/libs/chunks/475.min.js.LICENSE.txt
/usr/share/jitsi-meet/libs/chunks/5713.min.js
/usr/share/jitsi-meet/libs/chunks/4695.min.js
/usr/share/jitsi-meet/libs/chunks/2603.min.js
/usr/share/jitsi-meet/libs/chunks/247.min.js.map
/usr/share/jitsi-meet/libs/chunks/2886.min.js.map
/usr/share/jitsi-meet/libs/chunks/5114.min.js
/usr/share/jitsi-meet/libs/chunks/8989.min.js.map
/usr/share/jitsi-meet/libs/chunks/8005.min.js.map
/usr/share/jitsi-meet/libs/chunks/3417.min.js.map
/usr/share/jitsi-meet/libs/chunks/971.min.js.map
/usr/share/jitsi-meet/libs/chunks/1987.min.js.map
/usr/share/jitsi-meet/libs/chunks/3259.min.js
/usr/share/jitsi-meet/libs/chunks/3659.min.js.map
/usr/share/jitsi-meet/libs/chunks/2725.min.js.map
/usr/share/jitsi-meet/libs/chunks/4259.min.js.map
/usr/share/jitsi-meet/libs/chunks/9013.min.js
/usr/share/jitsi-meet/libs/chunks/5860.min.js.map
/usr/share/jitsi-meet/libs/chunks/9612.min.js
/usr/share/jitsi-meet/libs/chunks/1489.min.js
/usr/share/jitsi-meet/libs/chunks/9976.min.js
/usr/share/jitsi-meet/libs/chunks/3567.min.js.map
/usr/share/jitsi-meet/libs/chunks/1455.min.js.map
/usr/share/jitsi-meet/libs/chunks/7115.min.js.map
/usr/share/jitsi-meet/libs/chunks/7185.min.js
/usr/share/jitsi-meet/libs/chunks/2886.min.js
/usr/share/jitsi-meet/libs/chunks/1818.min.js.LICENSE.txt
/usr/share/jitsi-meet/libs/chunks/3645.min.js
/usr/share/jitsi-meet/libs/face-landmarks-worker.min.js
/usr/share/jitsi-meet/libs/selfie_segmentation_landscape.tflite
/usr/share/jitsi-meet/libs/external_api.min.js
/usr/share/jitsi-meet/libs/vb-inference-worker.min.js
/usr/share/jitsi-meet/libs/excalidraw
/usr/share/jitsi-meet/libs/excalidraw/fonts
/usr/share/jitsi-meet/libs/excalidraw/fonts/Excalifont
/usr/share/jitsi-meet/libs/excalidraw/fonts/ComicShanns
/usr/share/jitsi-meet/libs/excalidraw/fonts/Lilita
/usr/share/jitsi-meet/libs/excalidraw/fonts/Cascadia
/usr/share/jitsi-meet/libs/excalidraw/fonts/Nunito
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai
/usr/share/jitsi-meet/libs/excalidraw/fonts/Assistant
/usr/share/jitsi-meet/libs/excalidraw/fonts/Virgil
/usr/share/jitsi-meet/libs/excalidraw/fonts/Liberation
/usr/share/jitsi-meet/libs/emotion.json
/usr/share/jitsi-meet/libs/screenshot-capture-worker.min.js.map
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.js.LICENSE.txt
/usr/share/jitsi-meet/libs/face-landmarks-worker.min.js.map
/usr/share/jitsi-meet/libs/tfjs-backend-wasm-simd.wasm
/usr/share/jitsi-meet/libs/app.bundle.min.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_wasm_bin.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_simd_wasm_bin.wasm
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_simd_wasm_bin.data
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_landscape.tflite
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation.tflite
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_simd_wasm_bin.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_wasm_bin.wasm
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation.binarypb
/usr/share/jitsi-meet/libs/noise-suppressor-worklet.min.js.map
/usr/share/jitsi-meet/libs/lib-jitsi-meet.e2ee-worker.js
/usr/share/jitsi-meet/libs/vb-inference-worker.min.js.map
/usr/share/jitsi-meet/libs/alwaysontop.min.js
/usr/share/jitsi-meet/libs/alwaysontop.min.js.map
/usr/share/jitsi-meet/libs/rnnoise.wasm
/usr/share/jitsi-meet/libs/tflite.wasm


## Package


```text
$ dpkg -L jitsi-meet 2>/dev/null || true
```
/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/jitsi-meet
/usr/share/doc/jitsi-meet/changelog.Debian.gz
/usr/share/doc/jitsi-meet/copyright


## Configuration


```text
$ find /etc/jitsi -maxdepth 4 -type f -print 2>/dev/null | sort
```
/etc/jitsi/jicofo/config
/etc/jitsi/jicofo/jicofo.conf
/etc/jitsi/jicofo/logging.properties
/etc/jitsi/meet/meet.civitas.local-config.js
/etc/jitsi/videobridge/config
/etc/jitsi/videobridge/jvb.conf
/etc/jitsi/videobridge/logging.properties


## Fichiers JavaScript


```text
$ find /usr/share/jitsi-meet -type f 2>/dev/null | grep -Ei "\.js$|config|interface_config|external_api" | head -500
```
/usr/share/jitsi-meet/pwa-worker.js
/usr/share/jitsi-meet/static/close3.js
/usr/share/jitsi-meet/static/close.js
/usr/share/jitsi-meet/interface_config.js
/usr/share/jitsi-meet/lang/update-translation.js
/usr/share/jitsi-meet/libs/noise-suppressor-worklet.min.js
/usr/share/jitsi-meet/libs/external_api.min.js.map
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.js
/usr/share/jitsi-meet/libs/screenshot-capture-worker.min.js
/usr/share/jitsi-meet/libs/close3.min.js
/usr/share/jitsi-meet/libs/chunks/6770.min.js
/usr/share/jitsi-meet/libs/chunks/1455.min.js
/usr/share/jitsi-meet/libs/chunks/9828.min.js
/usr/share/jitsi-meet/libs/chunks/1987.min.js
/usr/share/jitsi-meet/libs/chunks/1689.min.js
/usr/share/jitsi-meet/libs/chunks/2725.min.js
/usr/share/jitsi-meet/libs/chunks/5544.min.js
/usr/share/jitsi-meet/libs/chunks/3687.min.js
/usr/share/jitsi-meet/libs/chunks/9596.min.js
/usr/share/jitsi-meet/libs/chunks/8846.min.js
/usr/share/jitsi-meet/libs/chunks/8005.min.js
/usr/share/jitsi-meet/libs/chunks/1080.min.js
/usr/share/jitsi-meet/libs/chunks/239.min.js
/usr/share/jitsi-meet/libs/chunks/5301.min.js
/usr/share/jitsi-meet/libs/chunks/6322.min.js
/usr/share/jitsi-meet/libs/chunks/8528.min.js
/usr/share/jitsi-meet/libs/chunks/8146.min.js
/usr/share/jitsi-meet/libs/chunks/3292.min.js
/usr/share/jitsi-meet/libs/chunks/7897.min.js
/usr/share/jitsi-meet/libs/chunks/8024.min.js
/usr/share/jitsi-meet/libs/chunks/6220.min.js
/usr/share/jitsi-meet/libs/chunks/9706.min.js
/usr/share/jitsi-meet/libs/chunks/544.min.js
/usr/share/jitsi-meet/libs/chunks/5860.min.js
/usr/share/jitsi-meet/libs/chunks/1329.min.js
/usr/share/jitsi-meet/libs/chunks/7256.min.js
/usr/share/jitsi-meet/libs/chunks/3567.min.js
/usr/share/jitsi-meet/libs/chunks/475.min.js
/usr/share/jitsi-meet/libs/chunks/7134.min.js
/usr/share/jitsi-meet/libs/chunks/6625.min.js
/usr/share/jitsi-meet/libs/chunks/4259.min.js
/usr/share/jitsi-meet/libs/chunks/3659.min.js
/usr/share/jitsi-meet/libs/chunks/493.min.js
/usr/share/jitsi-meet/libs/chunks/247.min.js
/usr/share/jitsi-meet/libs/chunks/8882.min.js
/usr/share/jitsi-meet/libs/chunks/1060.min.js
/usr/share/jitsi-meet/libs/chunks/9698.min.js
/usr/share/jitsi-meet/libs/chunks/547.min.js
/usr/share/jitsi-meet/libs/chunks/5628.min.js
/usr/share/jitsi-meet/libs/chunks/167.min.js
/usr/share/jitsi-meet/libs/chunks/8090.min.js
/usr/share/jitsi-meet/libs/chunks/5857.min.js
/usr/share/jitsi-meet/libs/chunks/3138.min.js
/usr/share/jitsi-meet/libs/chunks/4073.min.js
/usr/share/jitsi-meet/libs/chunks/3471.min.js
/usr/share/jitsi-meet/libs/chunks/2144.min.js
/usr/share/jitsi-meet/libs/chunks/2775.min.js
/usr/share/jitsi-meet/libs/chunks/8989.min.js
/usr/share/jitsi-meet/libs/chunks/1121.min.js
/usr/share/jitsi-meet/libs/chunks/5322.min.js
/usr/share/jitsi-meet/libs/chunks/3417.min.js
/usr/share/jitsi-meet/libs/chunks/7358.min.js
/usr/share/jitsi-meet/libs/chunks/2203.min.js
/usr/share/jitsi-meet/libs/chunks/922.min.js
/usr/share/jitsi-meet/libs/chunks/5163.min.js
/usr/share/jitsi-meet/libs/chunks/1818.min.js
/usr/share/jitsi-meet/libs/chunks/7115.min.js
/usr/share/jitsi-meet/libs/chunks/4762.min.js
/usr/share/jitsi-meet/libs/chunks/9890.min.js
/usr/share/jitsi-meet/libs/chunks/9105.min.js
/usr/share/jitsi-meet/libs/chunks/3347.min.js
/usr/share/jitsi-meet/libs/chunks/4106.min.js
/usr/share/jitsi-meet/libs/chunks/3207.min.js
/usr/share/jitsi-meet/libs/chunks/8995.min.js
/usr/share/jitsi-meet/libs/chunks/141.min.js
/usr/share/jitsi-meet/libs/chunks/4104.min.js
/usr/share/jitsi-meet/libs/chunks/4564.min.js
/usr/share/jitsi-meet/libs/chunks/7899.min.js
/usr/share/jitsi-meet/libs/chunks/4690.min.js
/usr/share/jitsi-meet/libs/chunks/2783.min.js
/usr/share/jitsi-meet/libs/chunks/3760.min.js
/usr/share/jitsi-meet/libs/chunks/6586.min.js
/usr/share/jitsi-meet/libs/chunks/4256.min.js
/usr/share/jitsi-meet/libs/chunks/6675.min.js
/usr/share/jitsi-meet/libs/chunks/2130.min.js
/usr/share/jitsi-meet/libs/chunks/8032.min.js
/usr/share/jitsi-meet/libs/chunks/5950.min.js
/usr/share/jitsi-meet/libs/chunks/4226.min.js
/usr/share/jitsi-meet/libs/chunks/971.min.js
/usr/share/jitsi-meet/libs/chunks/5388.min.js
/usr/share/jitsi-meet/libs/chunks/8298.min.js
/usr/share/jitsi-meet/libs/chunks/4130.min.js
/usr/share/jitsi-meet/libs/chunks/796.min.js
/usr/share/jitsi-meet/libs/chunks/4337.min.js
/usr/share/jitsi-meet/libs/chunks/8890.min.js
/usr/share/jitsi-meet/libs/chunks/4207.min.js
/usr/share/jitsi-meet/libs/chunks/2803.min.js
/usr/share/jitsi-meet/libs/chunks/7690.min.js
/usr/share/jitsi-meet/libs/chunks/5713.min.js
/usr/share/jitsi-meet/libs/chunks/4695.min.js
/usr/share/jitsi-meet/libs/chunks/2603.min.js
/usr/share/jitsi-meet/libs/chunks/5114.min.js
/usr/share/jitsi-meet/libs/chunks/3259.min.js
/usr/share/jitsi-meet/libs/chunks/9013.min.js
/usr/share/jitsi-meet/libs/chunks/9612.min.js
/usr/share/jitsi-meet/libs/chunks/1489.min.js
/usr/share/jitsi-meet/libs/chunks/9976.min.js
/usr/share/jitsi-meet/libs/chunks/7185.min.js
/usr/share/jitsi-meet/libs/chunks/2886.min.js
/usr/share/jitsi-meet/libs/chunks/3645.min.js
/usr/share/jitsi-meet/libs/face-landmarks-worker.min.js
/usr/share/jitsi-meet/libs/external_api.min.js
/usr/share/jitsi-meet/libs/vb-inference-worker.min.js
/usr/share/jitsi-meet/libs/app.bundle.min.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_wasm_bin.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_simd_wasm_bin.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation.js
/usr/share/jitsi-meet/libs/lib-jitsi-meet.e2ee-worker.js
/usr/share/jitsi-meet/libs/alwaysontop.min.js



---

# 8. NGINX

**Date :** 2026-08-08 06:56:25 EDT


## Status


```text
$ systemctl status nginx --no-pager
```
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: enabled)
     Active: active (running) since Fri 2026-08-07 05:25:31 EDT; 1 day 1h ago
 Invocation: 3ddfc18dbb1b46a7b05da931eb39030d
       Docs: man:nginx(8)
    Process: 1160 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Process: 1189 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
   Main PID: 1194 (nginx)
      Tasks: 5 (limit: 11719)
     Memory: 10M (peak: 10.7M)
        CPU: 225ms
     CGroup: /system.slice/nginx.service
             ├─1194 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             ├─1195 "nginx: worker process"
             ├─1197 "nginx: worker process"
             ├─1198 "nginx: worker process"
             └─1199 "nginx: worker process"

Aug 07 05:25:31 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Aug 07 05:25:31 meet.civitas.local nginx[1160]: 2026/08/07 05:25:31 [warn] 1160#1160: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 07 05:25:31 meet.civitas.local nginx[1160]: 2026/08/07 05:25:31 [warn] 1160#1160: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 07 05:25:31 meet.civitas.local nginx[1160]: 2026/08/07 05:25:31 [warn] 1160#1160: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 07 05:25:31 meet.civitas.local nginx[1189]: 2026/08/07 05:25:31 [warn] 1189#1189: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Aug 07 05:25:31 meet.civitas.local nginx[1189]: 2026/08/07 05:25:31 [warn] 1189#1189: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Aug 07 05:25:31 meet.civitas.local nginx[1189]: 2026/08/07 05:25:31 [warn] 1189#1189: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Aug 07 05:25:31 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.


## Configuration


```text
$ find /etc/nginx -type f -print 2>/dev/null | sort
```
/etc/nginx/fastcgi.conf
/etc/nginx/fastcgi_params
/etc/nginx/koi-utf
/etc/nginx/koi-win
/etc/nginx/mime.types
/etc/nginx/nginx.conf
/etc/nginx/proxy_params
/etc/nginx/scgi_params
/etc/nginx/sites-available/default
/etc/nginx/sites-available/meet.civitas.local
/etc/nginx/sites-available/meet.civitas.local.conf
/etc/nginx/snippets/fastcgi-php.conf
/etc/nginx/snippets/snakeoil.conf
/etc/nginx/uwsgi_params
/etc/nginx/win-utf


## Sites


```text
$ find /etc/nginx/sites-enabled /etc/nginx/sites-available -type f -maxdepth 2 -print 2>/dev/null | sort
```
/etc/nginx/sites-available/default
/etc/nginx/sites-available/meet.civitas.local
/etc/nginx/sites-available/meet.civitas.local.conf


## Recherche Jitsi


```text
$ grep -RniE "jitsi|prosody|xmpp|websocket|colibri|bosh|focus|meet" /etc/nginx 2>/dev/null || true
```
/etc/nginx/sites-available/meet.civitas.local:3:    server_name meet.civitas.local;
/etc/nginx/sites-available/meet.civitas.local:9:    server_name meet.civitas.local;
/etc/nginx/sites-available/meet.civitas.local:16:    include /etc/nginx/sites-available/meet.civitas.local.bak;
/etc/nginx/sites-available/meet.civitas.local.conf:8:upstream prosody {
/etc/nginx/sites-available/meet.civitas.local.conf:18:map $arg_vnode $prosody_node {
/etc/nginx/sites-available/meet.civitas.local.conf:19:    default prosody;
/etc/nginx/sites-available/meet.civitas.local.conf:32:    server_name meet.civitas.local;
/etc/nginx/sites-available/meet.civitas.local.conf:36:        root         /usr/share/jitsi-meet;
/etc/nginx/sites-available/meet.civitas.local.conf:48:    server_name meet.civitas.local;
/etc/nginx/sites-available/meet.civitas.local.conf:62:    set $config_js_location /etc/jitsi/meet/meet.civitas.local-config.js;
/etc/nginx/sites-available/meet.civitas.local.conf:64:    ssl_certificate /etc/ssl/meet.civitas.local.crt;
/etc/nginx/sites-available/meet.civitas.local.conf:65:    ssl_certificate_key /etc/ssl/meet.civitas.local.key;
/etc/nginx/sites-available/meet.civitas.local.conf:67:    root /usr/share/jitsi-meet;
/etc/nginx/sites-available/meet.civitas.local.conf:82:    include /etc/jitsi/meet/jaas/*.conf;
/etc/nginx/sites-available/meet.civitas.local.conf:89:        alias /usr/share/jitsi-meet/libs/external_api.min.js;
/etc/nginx/sites-available/meet.civitas.local.conf:93:        proxy_pass http://prosody/room-info?prefix=$prefix&$args;
/etc/nginx/sites-available/meet.civitas.local.conf:101:        alias /etc/jitsi/meet/public/$1;
/etc/nginx/sites-available/meet.civitas.local.conf:108:        alias /usr/share/jitsi-meet/$1/$2;
/etc/nginx/sites-available/meet.civitas.local.conf:116:    # BOSH
/etc/nginx/sites-available/meet.civitas.local.conf:118:        proxy_pass http://$prosody_node/http-bind?prefix=$prefix&$args;
/etc/nginx/sites-available/meet.civitas.local.conf:125:    # xmpp websockets
/etc/nginx/sites-available/meet.civitas.local.conf:126:    location = /xmpp-websocket {
/etc/nginx/sites-available/meet.civitas.local.conf:127:        proxy_pass http://$prosody_node/xmpp-websocket?prefix=$prefix&$args;
/etc/nginx/sites-available/meet.civitas.local.conf:135:    # colibri (JVB) websockets for jvb1
/etc/nginx/sites-available/meet.civitas.local.conf:136:    location ~ ^/colibri-ws/default-id/(.*) {
/etc/nginx/sites-available/meet.civitas.local.conf:137:        proxy_pass http://jvb1/colibri-ws/default-id/$1$is_args$args;
/etc/nginx/sites-available/meet.civitas.local.conf:150:    #    alias /usr/share/jitsi-meet/load-test/libs/$1;
/etc/nginx/sites-available/meet.civitas.local.conf:194:    # BOSH for subdomains
/etc/nginx/sites-available/meet.civitas.local.conf:203:    # websockets for subdomains
/etc/nginx/sites-available/meet.civitas.local.conf:204:    location ~ ^/([^/?&:'"]+)/xmpp-websocket {
/etc/nginx/sites-available/meet.civitas.local.conf:209:        rewrite ^/(.*)$ /xmpp-websocket;
/etc/nginx/sites-enabled/meet.civitas.local.conf:8:upstream prosody {
/etc/nginx/sites-enabled/meet.civitas.local.conf:18:map $arg_vnode $prosody_node {
/etc/nginx/sites-enabled/meet.civitas.local.conf:19:    default prosody;
/etc/nginx/sites-enabled/meet.civitas.local.conf:32:    server_name meet.civitas.local;
/etc/nginx/sites-enabled/meet.civitas.local.conf:36:        root         /usr/share/jitsi-meet;
/etc/nginx/sites-enabled/meet.civitas.local.conf:48:    server_name meet.civitas.local;
/etc/nginx/sites-enabled/meet.civitas.local.conf:62:    set $config_js_location /etc/jitsi/meet/meet.civitas.local-config.js;
/etc/nginx/sites-enabled/meet.civitas.local.conf:64:    ssl_certificate /etc/ssl/meet.civitas.local.crt;
/etc/nginx/sites-enabled/meet.civitas.local.conf:65:    ssl_certificate_key /etc/ssl/meet.civitas.local.key;
/etc/nginx/sites-enabled/meet.civitas.local.conf:67:    root /usr/share/jitsi-meet;
/etc/nginx/sites-enabled/meet.civitas.local.conf:82:    include /etc/jitsi/meet/jaas/*.conf;
/etc/nginx/sites-enabled/meet.civitas.local.conf:89:        alias /usr/share/jitsi-meet/libs/external_api.min.js;
/etc/nginx/sites-enabled/meet.civitas.local.conf:93:        proxy_pass http://prosody/room-info?prefix=$prefix&$args;
/etc/nginx/sites-enabled/meet.civitas.local.conf:101:        alias /etc/jitsi/meet/public/$1;
/etc/nginx/sites-enabled/meet.civitas.local.conf:108:        alias /usr/share/jitsi-meet/$1/$2;
/etc/nginx/sites-enabled/meet.civitas.local.conf:116:    # BOSH
/etc/nginx/sites-enabled/meet.civitas.local.conf:118:        proxy_pass http://$prosody_node/http-bind?prefix=$prefix&$args;
/etc/nginx/sites-enabled/meet.civitas.local.conf:125:    # xmpp websockets
/etc/nginx/sites-enabled/meet.civitas.local.conf:126:    location = /xmpp-websocket {
/etc/nginx/sites-enabled/meet.civitas.local.conf:127:        proxy_pass http://$prosody_node/xmpp-websocket?prefix=$prefix&$args;
/etc/nginx/sites-enabled/meet.civitas.local.conf:135:    # colibri (JVB) websockets for jvb1
/etc/nginx/sites-enabled/meet.civitas.local.conf:136:    location ~ ^/colibri-ws/default-id/(.*) {
/etc/nginx/sites-enabled/meet.civitas.local.conf:137:        proxy_pass http://jvb1/colibri-ws/default-id/$1$is_args$args;
/etc/nginx/sites-enabled/meet.civitas.local.conf:150:    #    alias /usr/share/jitsi-meet/load-test/libs/$1;
/etc/nginx/sites-enabled/meet.civitas.local.conf:194:    # BOSH for subdomains
/etc/nginx/sites-enabled/meet.civitas.local.conf:203:    # websockets for subdomains
/etc/nginx/sites-enabled/meet.civitas.local.conf:204:    location ~ ^/([^/?&:'"]+)/xmpp-websocket {
/etc/nginx/sites-enabled/meet.civitas.local.conf:209:        rewrite ^/(.*)$ /xmpp-websocket;


## Configuration complète


```text
$ nginx -T
```
2026/08/08 06:56:25 [warn] 92618#92618: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
2026/08/08 06:56:25 [warn] 92618#92618: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
2026/08/08 06:56:25 [warn] 92618#92618: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
# configuration file /etc/nginx/nginx.conf:
user www-data;
worker_processes auto;
worker_cpu_affinity auto;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	types_hash_max_size 2048;
	server_tokens off; # Recommended practice is to turn this off

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##

	ssl_protocols TLSv1.2 TLSv1.3; # Dropping SSLv3 (POODLE), TLS 1.0, 1.1
	ssl_prefer_server_ciphers off; # Don't force server cipher order.

	##
	# Logging Settings
	##

	access_log /var/log/nginx/access.log;

	##
	# Gzip Settings
	##

	gzip on;

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

	##
	# Virtual Host Configs
	##

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}


#mail {
#	# See sample authentication script at:
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
#
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
#
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
#
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}

# configuration file /etc/nginx/mime.types:
types {
    text/html                                        html htm shtml;
    text/css                                         css;
    text/xml                                         xml;
    image/gif                                        gif;
    image/jpeg                                       jpeg jpg;
    application/javascript                           js;
    application/atom+xml                             atom;
    application/rss+xml                              rss;

    text/mathml                                      mml;
    text/plain                                       txt;
    text/vnd.sun.j2me.app-descriptor                 jad;
    text/vnd.wap.wml                                 wml;
    text/x-component                                 htc;

    image/avif                                       avif;
    image/png                                        png;
    image/svg+xml                                    svg svgz;
    image/tiff                                       tif tiff;
    image/vnd.wap.wbmp                               wbmp;
    image/webp                                       webp;
    image/x-icon                                     ico;
    image/x-jng                                      jng;
    image/x-ms-bmp                                   bmp;

    font/woff                                        woff;
    font/woff2                                       woff2;

    application/java-archive                         jar war ear;
    application/json                                 json;
    application/mac-binhex40                         hqx;
    application/msword                               doc;
    application/pdf                                  pdf;
    application/postscript                           ps eps ai;
    application/rtf                                  rtf;
    application/vnd.apple.mpegurl                    m3u8;
    application/vnd.google-earth.kml+xml             kml;
    application/vnd.google-earth.kmz                 kmz;
    application/vnd.ms-excel                         xls;
    application/vnd.ms-fontobject                    eot;
    application/vnd.ms-powerpoint                    ppt;
    application/vnd.oasis.opendocument.graphics      odg;
    application/vnd.oasis.opendocument.presentation  odp;
    application/vnd.oasis.opendocument.spreadsheet   ods;
    application/vnd.oasis.opendocument.text          odt;
    application/vnd.openxmlformats-officedocument.presentationml.presentation
                                                     pptx;
    application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
                                                     xlsx;
    application/vnd.openxmlformats-officedocument.wordprocessingml.document
                                                     docx;
    application/vnd.wap.wmlc                         wmlc;
    application/wasm                                 wasm;
    application/x-7z-compressed                      7z;
    application/x-cocoa                              cco;
    application/x-java-archive-diff                  jardiff;
    application/x-java-jnlp-file                     jnlp;
    application/x-makeself                           run;
    application/x-perl                               pl pm;
    application/x-pilot                              prc pdb;
    application/x-rar-compressed                     rar;
    application/x-redhat-package-manager             rpm;
    application/x-sea                                sea;
    application/x-shockwave-flash                    swf;
    application/x-stuffit                            sit;
    application/x-tcl                                tcl tk;
    application/x-x509-ca-cert                       der pem crt;
    application/x-xpinstall                          xpi;
    application/xhtml+xml                            xhtml;
    application/xslt+xml                             xsl xslt;
    application/xspf+xml                             xspf;
    application/zip                                  zip;

    application/octet-stream                         bin exe dll;
    application/octet-stream                         deb;
    application/octet-stream                         dmg;
    application/octet-stream                         iso img;
    application/octet-stream                         msi msp msm;

    audio/midi                                       mid midi kar;
    audio/mpeg                                       mp3;
    audio/ogg                                        ogg;
    audio/x-m4a                                      m4a;
    audio/x-realaudio                                ra;

    video/3gpp                                       3gpp 3gp;
    video/mp2t                                       ts;
    video/mp4                                        mp4;
    video/mpeg                                       mpeg mpg;
    video/ogg                                        ogv;
    video/quicktime                                  mov;
    video/webm                                       webm;
    video/x-flv                                      flv;
    video/x-m4v                                      m4v;
    video/x-matroska                                 mkv;
    video/x-mng                                      mng;
    video/x-ms-asf                                   asx asf;
    video/x-ms-wmv                                   wmv;
    video/x-msvideo                                  avi;
}

# configuration file /etc/nginx/sites-enabled/default:
##
# You should look at the following URL's in order to grasp a solid understanding
# of Nginx configuration files in order to fully unleash the power of Nginx.
# https://www.nginx.com/resources/wiki/start/
# https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/
# https://wiki.debian.org/Nginx/DirectoryStructure
#
# In most cases, administrators will remove this file from sites-enabled/ and
# leave it as reference inside of sites-available where it will continue to be
# updated by the nginx packaging team.
#
# This file will automatically load configuration files provided by other
# applications, such as Drupal or Wordpress. These applications will be made
# available underneath a path with that package name, such as /drupal8.
#
# Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
##

# Default server configuration
#
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	# SSL configuration
	#
	# listen 443 ssl default_server;
	# listen [::]:443 ssl default_server;
	#
	# Note: You should disable gzip for SSL traffic.
	# See: https://bugs.debian.org/773332
	#
	# Read up on ssl_ciphers to ensure a secure configuration.
	# See: https://bugs.debian.org/765782
	#
	# Self signed certs generated by the ssl-cert package
	# Don't use them in a production server!
	#
	# include snippets/snakeoil.conf;

	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}

	# pass PHP scripts to FastCGI server
	#
	#location ~ \.php$ {
	#	include snippets/fastcgi-php.conf;
	#
	#	# With php-fpm (or other unix sockets):
	#	fastcgi_pass unix:/run/php/php7.4-fpm.sock;
	#	# With php-cgi (or other tcp sockets):
	#	fastcgi_pass 127.0.0.1:9000;
	#}

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#	deny all;
	#}
}


# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#	listen 80;
#	listen [::]:80;
#
#	server_name example.com;
#
#	root /var/www/example.com;
#	index index.html;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}

# configuration file /etc/nginx/sites-enabled/meet.civitas.local.conf:
server_names_hash_bucket_size 64;

types {
# nginx's default mime.types doesn't include a mapping for wasm or wav.
    application/wasm     wasm;
    audio/wav            wav;
}
upstream prosody {
    zone upstreams 64K;
    server 127.0.0.1:5280;
    keepalive 2;
}
upstream jvb1 {
    zone upstreams 64K;
    server 127.0.0.1:9090;
    keepalive 2;
}
map $arg_vnode $prosody_node {
    default prosody;
    v1 v1;
    v2 v2;
    v3 v3;
    v4 v4;
    v5 v5;
    v6 v6;
    v7 v7;
    v8 v8;
}
server {
    listen 80;
    listen [::]:80;
    server_name meet.civitas.local;

    location ^~ /.well-known/acme-challenge/ {
        default_type "text/plain";
        root         /usr/share/jitsi-meet;
    }
    location = /.well-known/acme-challenge/ {
        return 404;
    }
    location / {
        return 301 https://$host$request_uri;
    }
}
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name meet.civitas.local;

    # Mozilla Guideline v5.4, nginx 1.17.7, OpenSSL 1.1.1d, intermediate configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;

    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:10m;  # about 40000 sessions
    ssl_session_tickets off;

    add_header Strict-Transport-Security "max-age=63072000" always;
    set $prefix "";
    set $custom_index "";
    set $config_js_location /etc/jitsi/meet/meet.civitas.local-config.js;

    ssl_certificate /etc/ssl/meet.civitas.local.crt;
    ssl_certificate_key /etc/ssl/meet.civitas.local.key;

    root /usr/share/jitsi-meet;

    # ssi on with javascript for multidomain variables in config.js
    ssi on;
    ssi_types application/x-javascript application/javascript;

    index index.html index.htm;
    error_page 404 /static/404.html;

    gzip on;
    gzip_types text/plain text/css application/javascript application/json image/x-icon application/octet-stream application/wasm;
    gzip_vary on;
    gzip_proxied no-cache no-store private expired auth;
    gzip_min_length 512;

    include /etc/jitsi/meet/jaas/*.conf;

    location = /config.js {
        alias $config_js_location;
    }

    location = /external_api.js {
        alias /usr/share/jitsi-meet/libs/external_api.min.js;
    }

    location = /_api/room-info {
        proxy_pass http://prosody/room-info?prefix=$prefix&$args;
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header Host $http_host;
    }

    location ~ ^/_api/public/(.*)$ {
        autoindex off;
        alias /etc/jitsi/meet/public/$1;
    }

    # ensure all static content can always be found first
    location ~ ^/(libs|css|static|images|fonts|lang|sounds|.well-known)/(.*)$
    {
        add_header 'Access-Control-Allow-Origin' '*';
        alias /usr/share/jitsi-meet/$1/$2;

        # cache all versioned files
        if ($arg_v) {
            expires 1y;
        }
    }

    # BOSH
    location = /http-bind {
        proxy_pass http://$prosody_node/http-bind?prefix=$prefix&$args;
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header Host $http_host;
        proxy_set_header Connection "";
    }

    # xmpp websockets
    location = /xmpp-websocket {
        proxy_pass http://$prosody_node/xmpp-websocket?prefix=$prefix&$args;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $http_host;
        tcp_nodelay on;
    }

    # colibri (JVB) websockets for jvb1
    location ~ ^/colibri-ws/default-id/(.*) {
        proxy_pass http://jvb1/colibri-ws/default-id/$1$is_args$args;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        tcp_nodelay on;
    }

    # load test minimal client, uncomment when used
    #location ~ ^/_load-test/([^/?&:'"]+)$ {
    #    rewrite ^/_load-test/(.*)$ /load-test/index.html break;
    #}
    #location ~ ^/_load-test/libs/(.*)$ {
    #    add_header 'Access-Control-Allow-Origin' '*';
    #    alias /usr/share/jitsi-meet/load-test/libs/$1;
    #}

    location = /_unlock {
        add_header 'Access-Control-Allow-Origin' '*';
        add_header Strict-Transport-Security 'max-age=63072000; includeSubDomains';
        add_header "Cache-Control" "no-cache, no-store";
    }

    location ~ ^/conference-request/v1(\/.*)?$ {
        proxy_pass http://127.0.0.1:8888/conference-request/v1$1;
        add_header "Cache-Control" "no-cache, no-store";
        add_header 'Access-Control-Allow-Origin' '*';
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
        add_header 'Access-Control-Allow-Headers' 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Content-Type';
    }
    location ~ ^/([^/?&:'"]+)/conference-request/v1(\/.*)?$ {
        rewrite ^/([^/?&:'"]+)/conference-request/v1(\/.*)?$ /conference-request/v1$2;
    }

    location ~ ^/([^/?&:'"]+)$ {
        set $roomname "$1";
        try_files $uri @root_path;
    }

    location @root_path {
        rewrite ^/(.*)$ /$custom_index break;
    }

    location ~ ^/([^/?&:'"]+)/config.js$
    {
        set $subdomain "$1.";
        set $subdir "$1/";

        alias $config_js_location;
    }

    # Matches /(TENANT)/pwa-worker.js or /(TENANT)/manifest.json to rewrite to / and look for file
    location ~ ^/([^/?&:'"]+)/(pwa-worker.js|manifest.json)$ {
        set $subdomain "$1.";
        set $subdir "$1/";
        rewrite ^/([^/?&:'"]+)/(pwa-worker.js|manifest.json)$ /$2;
    }

    # BOSH for subdomains
    location ~ ^/([^/?&:'"]+)/http-bind {
        set $subdomain "$1.";
        set $subdir "$1/";
        set $prefix "$1";

        rewrite ^/(.*)$ /http-bind;
    }

    # websockets for subdomains
    location ~ ^/([^/?&:'"]+)/xmpp-websocket {
        set $subdomain "$1.";
        set $subdir "$1/";
        set $prefix "$1";

        rewrite ^/(.*)$ /xmpp-websocket;
    }

    location ~ ^/([^/?&:'"]+)/_api/room-info {
        set $subdomain "$1.";
        set $subdir "$1/";
        set $prefix "$1";

        rewrite ^/(.*)$ /_api/room-info;
    }

    # Anything that didn't match above, and isn't a real file, assume it's a room name and redirect to /
    location ~ ^/([^/?&:'"]+)/(.*)$ {
        set $subdomain "$1.";
        set $subdir "$1/";
        rewrite ^/([^/?&:'"]+)/(.*)$ /$2;
    }
}




---

# 9. CERTIFICATS TLS

**Date :** 2026-08-08 06:56:25 EDT


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

**Date :** 2026-08-08 06:56:25 EDT


## Paquet


```text
$ dpkg -l 2>/dev/null | grep -Ei "coturn|turnserver" || true
```
ii  coturn                                              4.6.1-2                              amd64        TURN and STUN server for VoIP
ii  jitsi-meet-turnserver                               1.0.9365-1                           all          Configures coturn to be used with Jitsi Meet


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
# jitsi-meet coturn config. Do not modify this line
use-auth-secret
keep-address-family
static-auth-secret=2eOgmgMf5Gq6E4LE
realm=meet.civitas.local
cert=/etc/ssl/meet.civitas.local.crt
pkey=/etc/ssl/meet.civitas.local.key
no-multicast-peers
no-cli
no-loopback-peers
no-tcp-relay
no-tcp
no-dtls
listening-port=3478
tls-listening-port=5349
no-tlsv1
no-tlsv1_1
# https://ssl-config.mozilla.org/#server=haproxy&version=2.1&config=intermediate&openssl=1.1.0g&guideline=5.4
cipher-list=ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
# without it there are errors when running on Ubuntu 20.04
dh2066
# jitsi-meet coturn relay disable config. Do not modify this line
denied-peer-ip=0.0.0.0-0.255.255.255
denied-peer-ip=10.0.0.0-10.255.255.255
denied-peer-ip=100.64.0.0-100.127.255.255
denied-peer-ip=127.0.0.0-127.255.255.255
denied-peer-ip=169.254.0.0-169.254.255.255
denied-peer-ip=127.0.0.0-127.255.255.255
denied-peer-ip=172.16.0.0-172.31.255.255
denied-peer-ip=192.0.0.0-192.0.0.255
denied-peer-ip=192.0.2.0-192.0.2.255
denied-peer-ip=192.88.99.0-192.88.99.255
denied-peer-ip=192.168.0.0-192.168.255.255
denied-peer-ip=198.18.0.0-198.19.255.255
denied-peer-ip=198.51.100.0-198.51.100.255
denied-peer-ip=203.0.113.0-203.0.113.255
denied-peer-ip=240.0.0.0-255.255.255.255
denied-peer-ip=::1
denied-peer-ip=64:ff9b::-64:ff9b::ffff:ffff
denied-peer-ip=::ffff:0.0.0.0-::ffff:255.255.255.255
denied-peer-ip=100::-100::ffff:ffff:ffff:ffff
denied-peer-ip=2001::-2001:1ff:ffff:ffff:ffff:ffff:ffff:ffff
denied-peer-ip=2002::-2002:ffff:ffff:ffff:ffff:ffff:ffff:ffff
denied-peer-ip=fc00::-fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
denied-peer-ip=fe80::-febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff
syslog


## Systemd


```text
$ systemctl status coturn --no-pager
```
× coturn.service - coTURN STUN/TURN Server
     Loaded: loaded (/usr/lib/systemd/system/coturn.service; enabled; preset: enabled)
     Active: failed (Result: exit-code) since Fri 2026-08-07 05:25:29 EDT; 1 day 1h ago
 Invocation: bbf5ccc9e1d84d7f932b7407b0480faa
       Docs: man:coturn(1)
             man:turnadmin(1)
             man:turnserver(1)
    Process: 1056 ExecStart=/usr/bin/turnserver -c /etc/turnserver.conf --pidfile= (code=exited, status=255/EXCEPTION)
   Main PID: 1056 (code=exited, status=255/EXCEPTION)

Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot start TLS and DTLS listeners because private key file is not set properly
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : NO EXPLICIT LISTENER ADDRESS(ES) ARE CONFIGURED
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : ===========Discovering listener addresses: =========
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Listener address to use: 127.0.0.1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Listener address to use: ::1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : ERROR: main: Cannot configure any meaningful IP listener address
Aug 07 05:25:29 meet.civitas.local systemd[1]: coturn.service: Scheduled restart job, restart counter is at 5.
Aug 07 05:25:29 meet.civitas.local systemd[1]: coturn.service: Start request repeated too quickly.
Aug 07 05:25:29 meet.civitas.local systemd[1]: coturn.service: Failed with result 'exit-code'.
Aug 07 05:25:29 meet.civitas.local systemd[1]: Failed to start coturn.service - coTURN STUN/TURN Server.


```text
$ systemctl status turnserver --no-pager
```
Unit turnserver.service could not be found.



---

# 11. PORTS RÉSEAU

**Date :** 2026-08-08 06:56:25 EDT


## Tous les ports en écoute


```text
$ ss -lntup
```
Netid State  Recv-Q Send-Q         Local Address:Port  Peer Address:PortProcess                                                                                                                         
udp   UNCONN 0      0                    0.0.0.0:47640      0.0.0.0:*    users:(("kdeconnectd",pid=6278,fd=25))                                                                                         
udp   UNCONN 0      0                  127.0.0.1:53         0.0.0.0:*    users:(("dnsmasq",pid=1141,fd=4))                                                                                              
udp   UNCONN 0      0                    0.0.0.0:60057      0.0.0.0:*    users:(("avahi-daemon",pid=740,fd=14))                                                                                         
udp   UNCONN 0      0                    0.0.0.0:44613      0.0.0.0:*    users:(("kdeconnectd",pid=6278,fd=24))                                                                                         
udp   UNCONN 0      0                    0.0.0.0:5353       0.0.0.0:*    users:(("kdeconnectd",pid=6278,fd=21))                                                                                         
udp   UNCONN 0      0                    0.0.0.0:5353       0.0.0.0:*    users:(("avahi-daemon",pid=740,fd=12))                                                                                         
udp   UNCONN 0      0                          *:55990            *:*    users:(("kdeconnectd",pid=6278,fd=39))                                                                                         
udp   UNCONN 0      0                          *:56739            *:*    users:(("kdeconnectd",pid=6278,fd=23))                                                                                         
udp   UNCONN 0      0                          *:56979            *:*    users:(("kdeconnectd",pid=6278,fd=34))                                                                                         
udp   UNCONN 0      0                      [::1]:53            [::]:*    users:(("dnsmasq",pid=1141,fd=6))                                                                                              
udp   UNCONN 0      0                          *:49632            *:*    users:(("kdeconnectd",pid=6278,fd=26))                                                                                         
udp   UNCONN 0      0                          *:41730            *:*    users:(("kdeconnectd",pid=6278,fd=33))                                                                                         
udp   UNCONN 0      0                          *:41799            *:*    users:(("kdeconnectd",pid=6278,fd=29))                                                                                         
udp   UNCONN 0      0                          *:34007            *:*    users:(("kdeconnectd",pid=6278,fd=30))                                                                                         
udp   UNCONN 0      0                          *:1716             *:*    users:(("kdeconnectd",pid=6278,fd=19))                                                                                         
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=143))                                                                                               
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=142))                                                                                               
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=141))                                                                                               
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=140))                                                                                               
udp   UNCONN 0      0                          *:42780            *:*    users:(("kdeconnectd",pid=6278,fd=32))                                                                                         
udp   UNCONN 0      0                          *:59165            *:*    users:(("kdeconnectd",pid=6278,fd=28))                                                                                         
udp   UNCONN 0      0                       [::]:43355         [::]:*    users:(("avahi-daemon",pid=740,fd=15))                                                                                         
udp   UNCONN 0      0                          *:44486            *:*    users:(("kdeconnectd",pid=6278,fd=31))                                                                                         
udp   UNCONN 0      0                          *:44706            *:*    users:(("kdeconnectd",pid=6278,fd=35))                                                                                         
udp   UNCONN 0      0                          *:54140            *:*    users:(("kdeconnectd",pid=6278,fd=36))                                                                                         
udp   UNCONN 0      0                          *:54332            *:*    users:(("kdeconnectd",pid=6278,fd=27))                                                                                         
udp   UNCONN 0      0                       [::]:5353          [::]:*    users:(("avahi-daemon",pid=740,fd=13))                                                                                         
udp   UNCONN 0      0                          *:5353             *:*    users:(("kdeconnectd",pid=6278,fd=22))                                                                                         
udp   UNCONN 0      0                          *:46639            *:*    users:(("kdeconnectd",pid=6278,fd=38))                                                                                         
udp   UNCONN 0      0                          *:55084            *:*    users:(("kdeconnectd",pid=6278,fd=37))                                                                                         
tcp   LISTEN 0      128                127.0.0.1:5280       0.0.0.0:*    users:(("lua5.4",pid=1161,fd=19))                                                                                              
tcp   LISTEN 0      4096                 0.0.0.0:9308       0.0.0.0:*    users:(("dockerd",pid=1159,fd=21))                                                                                             
tcp   LISTEN 0      4096                 0.0.0.0:9092       0.0.0.0:*    users:(("dockerd",pid=1159,fd=84))                                                                                             
tcp   LISTEN 0      4096                 0.0.0.0:9091       0.0.0.0:*    users:(("dockerd",pid=1159,fd=105))                                                                                            
tcp   LISTEN 0      128                  0.0.0.0:22         0.0.0.0:*    users:(("sshd",pid=1018,fd=6))                                                                                                 
tcp   LISTEN 0      511                  0.0.0.0:80         0.0.0.0:*    users:(("nginx",pid=1199,fd=5),("nginx",pid=1198,fd=5),("nginx",pid=1197,fd=5),("nginx",pid=1195,fd=5),("nginx",pid=1194,fd=5))
tcp   LISTEN 0      511                  0.0.0.0:443        0.0.0.0:*    users:(("nginx",pid=1199,fd=7),("nginx",pid=1198,fd=7),("nginx",pid=1197,fd=7),("nginx",pid=1195,fd=7),("nginx",pid=1194,fd=7))
tcp   LISTEN 0      4096                 0.0.0.0:3100       0.0.0.0:*    users:(("dockerd",pid=1159,fd=148))                                                                                            
tcp   LISTEN 0      4096                 0.0.0.0:3000       0.0.0.0:*    users:(("dockerd",pid=1159,fd=91))                                                                                             
tcp   LISTEN 0      128                  0.0.0.0:5269       0.0.0.0:*    users:(("lua5.4",pid=1161,fd=14))                                                                                              
tcp   LISTEN 0      128                  0.0.0.0:5281       0.0.0.0:*    users:(("lua5.4",pid=1161,fd=21))                                                                                              
tcp   LISTEN 0      128                  0.0.0.0:5222       0.0.0.0:*    users:(("lua5.4",pid=1161,fd=17))                                                                                              
tcp   LISTEN 0      4096               127.0.0.1:631        0.0.0.0:*    users:(("cupsd",pid=49780,fd=7))                                                                                               
tcp   LISTEN 0      32                 127.0.0.1:53         0.0.0.0:*    users:(("dnsmasq",pid=1141,fd=5))                                                                                              
tcp   LISTEN 0      4096                 0.0.0.0:8090       0.0.0.0:*    users:(("dockerd",pid=1159,fd=83))                                                                                             
tcp   LISTEN 0      4096                 0.0.0.0:8100       0.0.0.0:*    users:(("dockerd",pid=1159,fd=113))                                                                                            
tcp   LISTEN 0      4096                 0.0.0.0:8002       0.0.0.0:*    users:(("dockerd",pid=1159,fd=123))                                                                                            
tcp   LISTEN 0      4096                 0.0.0.0:8010       0.0.0.0:*    users:(("dockerd",pid=1159,fd=93))                                                                                             
tcp   LISTEN 0      4096                 0.0.0.0:8011       0.0.0.0:*    users:(("dockerd",pid=1159,fd=87))                                                                                             
tcp   LISTEN 0      50                         *:1716             *:*    users:(("kdeconnectd",pid=6278,fd=20))                                                                                         
tcp   LISTEN 0      50                         *:9090             *:*    users:(("java",pid=1162,fd=148))                                                                                               
tcp   LISTEN 0      128                     [::]:22            [::]:*    users:(("sshd",pid=1018,fd=7))                                                                                                 
tcp   LISTEN 0      511                     [::]:80            [::]:*    users:(("nginx",pid=1199,fd=6),("nginx",pid=1198,fd=6),("nginx",pid=1197,fd=6),("nginx",pid=1195,fd=6),("nginx",pid=1194,fd=6))
tcp   LISTEN 0      511                     [::]:443           [::]:*    users:(("nginx",pid=1199,fd=8),("nginx",pid=1198,fd=8),("nginx",pid=1197,fd=8),("nginx",pid=1195,fd=8),("nginx",pid=1194,fd=8))
tcp   LISTEN 0      32                     [::1]:53            [::]:*    users:(("dnsmasq",pid=1141,fd=7))                                                                                              
tcp   LISTEN 0      50        [::ffff:127.0.0.1]:8080             *:*    users:(("java",pid=1162,fd=155))                                                                                               
tcp   LISTEN 0      4096                   [::1]:631           [::]:*    users:(("cupsd",pid=49780,fd=6))                                                                                               
tcp   LISTEN 0      128                     [::]:5269          [::]:*    users:(("lua5.4",pid=1161,fd=13))                                                                                              
tcp   LISTEN 0      128                     [::]:5281          [::]:*    users:(("lua5.4",pid=1161,fd=20))                                                                                              
tcp   LISTEN 0      128                     [::]:5222          [::]:*    users:(("lua5.4",pid=1161,fd=16))                                                                                              
tcp   LISTEN 0      4096      [::ffff:127.0.0.1]:8888             *:*    users:(("java",pid=786,fd=116))                                                                                                
tcp   LISTEN 0      128                    [::1]:5280          [::]:*    users:(("lua5.4",pid=1161,fd=18))                                                                                              


## Ports Jitsi connus


```text
$ ss -lntup 2>/dev/null | grep -E ":80 |:443 |:5222 |:5269 |:5347 |:3478 |:5349 |:10000 |:4443 |:8080 |:8888 |:8443 " || true
```
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=143))                                                                                               
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=142))                                                                                               
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=141))                                                                                               
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=140))                                                                                               
tcp   LISTEN 0      511                  0.0.0.0:80         0.0.0.0:*    users:(("nginx",pid=1199,fd=5),("nginx",pid=1198,fd=5),("nginx",pid=1197,fd=5),("nginx",pid=1195,fd=5),("nginx",pid=1194,fd=5))
tcp   LISTEN 0      511                  0.0.0.0:443        0.0.0.0:*    users:(("nginx",pid=1199,fd=7),("nginx",pid=1198,fd=7),("nginx",pid=1197,fd=7),("nginx",pid=1195,fd=7),("nginx",pid=1194,fd=7))
tcp   LISTEN 0      128                  0.0.0.0:5269       0.0.0.0:*    users:(("lua5.4",pid=1161,fd=14))                                                                                              
tcp   LISTEN 0      128                  0.0.0.0:5222       0.0.0.0:*    users:(("lua5.4",pid=1161,fd=17))                                                                                              
tcp   LISTEN 0      511                     [::]:80            [::]:*    users:(("nginx",pid=1199,fd=6),("nginx",pid=1198,fd=6),("nginx",pid=1197,fd=6),("nginx",pid=1195,fd=6),("nginx",pid=1194,fd=6))
tcp   LISTEN 0      511                     [::]:443           [::]:*    users:(("nginx",pid=1199,fd=8),("nginx",pid=1198,fd=8),("nginx",pid=1197,fd=8),("nginx",pid=1195,fd=8),("nginx",pid=1194,fd=8))
tcp   LISTEN 0      50        [::ffff:127.0.0.1]:8080             *:*    users:(("java",pid=1162,fd=155))                                                                                               
tcp   LISTEN 0      128                     [::]:5269          [::]:*    users:(("lua5.4",pid=1161,fd=13))                                                                                              
tcp   LISTEN 0      128                     [::]:5222          [::]:*    users:(("lua5.4",pid=1161,fd=16))                                                                                              
tcp   LISTEN 0      4096      [::ffff:127.0.0.1]:8888             *:*    users:(("java",pid=786,fd=116))                                                                                                


## Processus liés aux ports


```text
$ lsof -nP -iTCP -sTCP:LISTEN 2>/dev/null | grep -Ei "java|prosody|nginx|turn|jitsi|node" || true
```
COMMAND     PID     USER  FD   TYPE DEVICE SIZE/OFF NODE NAME
java        786   jicofo 116u  IPv6   7943      0t0  TCP 127.0.0.1:8888 (LISTEN)
lua5.4     1161  prosody  13u  IPv6   9083      0t0  TCP *:5269 (LISTEN)
lua5.4     1161  prosody  14u  IPv4   9084      0t0  TCP *:5269 (LISTEN)
lua5.4     1161  prosody  16u  IPv6  10664      0t0  TCP *:5222 (LISTEN)
lua5.4     1161  prosody  17u  IPv4  10665      0t0  TCP *:5222 (LISTEN)
lua5.4     1161  prosody  18u  IPv6  10666      0t0  TCP [::1]:5280 (LISTEN)
lua5.4     1161  prosody  19u  IPv4  10667      0t0  TCP 127.0.0.1:5280 (LISTEN)
lua5.4     1161  prosody  20u  IPv6  10668      0t0  TCP *:5281 (LISTEN)
lua5.4     1161  prosody  21u  IPv4  10669      0t0  TCP *:5281 (LISTEN)
java       1162      jvb 148u  IPv6  13364      0t0  TCP *:9090 (LISTEN)
java       1162      jvb 155u  IPv6  11184      0t0  TCP 127.0.0.1:8080 (LISTEN)
nginx      1194     root   5u  IPv4   9063      0t0  TCP *:80 (LISTEN)
nginx      1194     root   6u  IPv6   9064      0t0  TCP *:80 (LISTEN)
nginx      1194     root   7u  IPv4   9065      0t0  TCP *:443 (LISTEN)
nginx      1194     root   8u  IPv6   9066      0t0  TCP *:443 (LISTEN)
nginx      1195 www-data   5u  IPv4   9063      0t0  TCP *:80 (LISTEN)
nginx      1195 www-data   6u  IPv6   9064      0t0  TCP *:80 (LISTEN)
nginx      1195 www-data   7u  IPv4   9065      0t0  TCP *:443 (LISTEN)
nginx      1195 www-data   8u  IPv6   9066      0t0  TCP *:443 (LISTEN)
nginx      1197 www-data   5u  IPv4   9063      0t0  TCP *:80 (LISTEN)
nginx      1197 www-data   6u  IPv6   9064      0t0  TCP *:80 (LISTEN)
nginx      1197 www-data   7u  IPv4   9065      0t0  TCP *:443 (LISTEN)
nginx      1197 www-data   8u  IPv6   9066      0t0  TCP *:443 (LISTEN)
nginx      1198 www-data   5u  IPv4   9063      0t0  TCP *:80 (LISTEN)
nginx      1198 www-data   6u  IPv6   9064      0t0  TCP *:80 (LISTEN)
nginx      1198 www-data   7u  IPv4   9065      0t0  TCP *:443 (LISTEN)
nginx      1198 www-data   8u  IPv6   9066      0t0  TCP *:443 (LISTEN)
nginx      1199 www-data   5u  IPv4   9063      0t0  TCP *:80 (LISTEN)
nginx      1199 www-data   6u  IPv6   9064      0t0  TCP *:80 (LISTEN)
nginx      1199 www-data   7u  IPv4   9065      0t0  TCP *:443 (LISTEN)
nginx      1199 www-data   8u  IPv6   9066      0t0  TCP *:443 (LISTEN)



---

# 12. PROCESSUS

**Date :** 2026-08-08 06:56:26 EDT


## Processus Jitsi


```text
$ ps auxww | grep -Ei "jitsi|prosody|jicofo|videobridge|jvb|turnserver|coturn|nginx" | grep -v grep || true
```
jicofo       786  0.3  2.1 6870052 216248 ?      Sl   02:22   0:51 java -Xmx3072m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=jicofo -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/jicofo/logging.properties -Dconfig.file=/etc/jitsi/jicofo/jicofo.conf -cp /usr/share/jicofo/jicofo.jar:/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar:/usr/share/jicofo/lib/annotations-23.0.0.jar:/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar:/usr/share/jicofo/lib/commons-lang3-3.12.0.jar:/usr/share/jicofo/lib/config-1.4.3.jar:/usr/share/jicofo/lib/gson-2.8.5.jar:/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar:/usr/share/jicofo/lib/jackson-core-2.18.0.jar:/usr/share/jicofo/lib/jackson-databind-2.18.0.jar:/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar:/usr/share/jicofo/lib/jansi-2.4.1.jar:/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar:/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar:/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar:/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar:/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar:/usr/share/jicofo/lib/jjwt-api-0.12.6.jar:/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar:/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar:/usr/share/jicofo/lib/jna-5.9.0.jar:/usr/share/jicofo/lib/jsr305-3.0.2.jar:/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar:/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar:/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar:/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar:/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar:/usr/share/jicofo/lib/minidns-core-1.0.5.jar:/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar:/usr/share/jicofo/lib/precis-1.1.0.jar:/usr/share/jicofo/lib/sentry-5.4.0.jar:/usr/share/jicofo/lib/simpleclient-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar:/usr/share/jicofo/lib/slf4j-api-1.7.32.jar:/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar:/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar org.jitsi.jicofo.Main
prosody     1161  0.3  0.2  68968 29564 ?        Ss   02:22   1:05 lua5.4 /usr/bin/prosody -F
jvb         1162  0.4  2.5 6887016 252844 ?      Ssl  02:22   1:20 java -Xmx3072m -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dconfig.file=/etc/jitsi/videobridge/jvb.conf -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=videobridge -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/videobridge/logging.properties -cp /usr/share/jitsi-videobridge/jitsi-videobridge.jar:/usr/share/jitsi-videobridge/lib/* org.jitsi.videobridge.MainKt
root        1194  0.0  0.0  26028  3132 ?        Ss   02:22   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    1195  0.0  0.1  27980 10912 ?        S    02:22   0:00 nginx: worker process
www-data    1197  0.0  0.0  27608  9636 ?        S    02:22   0:00 nginx: worker process
www-data    1198  0.0  0.1  27872 10816 ?        S    02:22   0:00 nginx: worker process
www-data    1199  0.0  0.0  27448  9688 ?        S    02:22   0:00 nginx: worker process
civitas     6280  0.0  1.5 1513564 154100 ?      Ssl  02:24   0:00 /usr/bin/xwaylandvideobridge
root       91754  1.3  0.0  21812  7996 pts/2    S+   06:56   0:00 sudo /opt/civitas/jitsi-infrastructure-audit.sh
root       91756  0.0  0.0  21812  2692 pts/3    Ss   06:56   0:00 sudo /opt/civitas/jitsi-infrastructure-audit.sh
root       91757  7.3  0.0   7208  3464 pts/3    S+   06:56   0:00 bash /opt/civitas/jitsi-infrastructure-audit.sh
root       92830  0.0  0.0   5576  1960 pts/3    S+   06:56   0:00 tee -a /opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md


## Processus Java


```text
$ ps auxww | grep java | grep -v grep || true
```
jicofo       786  0.3  2.1 6870052 216248 ?      Sl   02:22   0:51 java -Xmx3072m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=jicofo -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/jicofo/logging.properties -Dconfig.file=/etc/jitsi/jicofo/jicofo.conf -cp /usr/share/jicofo/jicofo.jar:/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar:/usr/share/jicofo/lib/annotations-23.0.0.jar:/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar:/usr/share/jicofo/lib/commons-lang3-3.12.0.jar:/usr/share/jicofo/lib/config-1.4.3.jar:/usr/share/jicofo/lib/gson-2.8.5.jar:/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar:/usr/share/jicofo/lib/jackson-core-2.18.0.jar:/usr/share/jicofo/lib/jackson-databind-2.18.0.jar:/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar:/usr/share/jicofo/lib/jansi-2.4.1.jar:/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar:/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar:/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar:/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar:/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar:/usr/share/jicofo/lib/jjwt-api-0.12.6.jar:/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar:/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar:/usr/share/jicofo/lib/jna-5.9.0.jar:/usr/share/jicofo/lib/jsr305-3.0.2.jar:/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar:/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar:/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar:/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar:/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar:/usr/share/jicofo/lib/minidns-core-1.0.5.jar:/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar:/usr/share/jicofo/lib/precis-1.1.0.jar:/usr/share/jicofo/lib/sentry-5.4.0.jar:/usr/share/jicofo/lib/simpleclient-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar:/usr/share/jicofo/lib/slf4j-api-1.7.32.jar:/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar:/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar org.jitsi.jicofo.Main
jvb         1162  0.4  2.5 6887016 252844 ?      Ssl  02:22   1:20 java -Xmx3072m -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dconfig.file=/etc/jitsi/videobridge/jvb.conf -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=videobridge -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/videobridge/logging.properties -cp /usr/share/jitsi-videobridge/jitsi-videobridge.jar:/usr/share/jitsi-videobridge/lib/* org.jitsi.videobridge.MainKt
dhcpcd      2124  0.4  3.4 4291708 350048 ?      Ssl  02:22   1:11 java --add-opens java.rmi/javax.rmi.ssl=ALL-UNNAMED -jar kafka-ui-api.jar
civitas     2136  2.4  7.6 6436376 767852 ?      Ssl  02:22   6:44 java -Xmx1G -Xms1G -server -XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent -XX:MaxInlineLevel=15 -Djava.awt.headless=true -Xlog:gc*:file=/var/log/kafka/kafkaServer-gc.log:time,tags:filecount=10,filesize=100M -Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dkafka.logs.dir=/var/log/kafka -Dlog4j.configuration=file:/etc/kafka/log4j.properties -cp /usr/bin/../share/java/kafka/*:/usr/bin/../share/java/confluent-telemetry/* kafka.Kafka /etc/kafka/kafka.properties


## Processus Prosody


```text
$ ps auxww | grep prosody | grep -v grep || true
```
prosody     1161  0.3  0.2  68968 29564 ?        Ss   02:22   1:05 lua5.4 /usr/bin/prosody -F



---

# 13. RECHERCHE GLOBALE DES FICHIERS JITSI

**Date :** 2026-08-08 06:56:26 EDT


## Noms contenant jitsi


```text
$ find / -xdev \( -iname "*jitsi*" -o -iname "*jicofo*" -o -iname "*videobridge*" -o -iname "*prosody*" \) -print 2>/dev/null | sort
```
/etc/apt/keyrings/jitsi.gpg
/etc/apt/sources.list.d/jitsi-stable.list
/etc/init.d/jicofo
/etc/init.d/jitsi-videobridge2
/etc/init.d/prosody
/etc/jitsi
/etc/jitsi/jicofo
/etc/jitsi/jicofo/jicofo.conf
/etc/jitsi/videobridge
/etc/logrotate.d/jicofo
/etc/logrotate.d/jitsi-videobridge
/etc/logrotate.d/prosody
/etc/prosody
/etc/prosody/prosody.cfg.lua
/etc/rc0.d/K01jicofo
/etc/rc0.d/K01prosody
/etc/rc1.d/K01jicofo
/etc/rc1.d/K01prosody
/etc/rc2.d/S01jicofo
/etc/rc2.d/S01prosody
/etc/rc3.d/S01jicofo
/etc/rc3.d/S01prosody
/etc/rc4.d/S01jicofo
/etc/rc4.d/S01prosody
/etc/rc5.d/S01jicofo
/etc/rc5.d/S01prosody
/etc/rc6.d/K01jicofo
/etc/rc6.d/K01prosody
/etc/systemd/system/jitsi-videobridge2.service.d
/etc/systemd/system/multi-user.target.wants/jitsi-videobridge2.service
/etc/systemd/system/multi-user.target.wants/prosody.service
/etc/xdg/autostart/org.kde.xwaylandvideobridge.desktop
/home/civitas/.cache/xwaylandvideobridge
/home/civitas/ystemctl restart jitsi-videobridge2
/opt/civitas/jitsi
/opt/civitas/jitsi-audit
/opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md
/opt/civitas/jitsi-infrastructure-audit.sh
/opt/civitas/PLAN_SYNCHRONISATION_ROOMS_JITSI.md
/opt/civitas/scripts/jitsi_boot.sh
/opt/civitas/scripts/jitsi_stop.sh
/opt/civitas/scripts/lib/jitsi_common.sh
/opt/civitas/services/peer/event-jitsi.txt
/usr/bin/ejabberd2prosody
/usr/bin/prosody
/usr/bin/prosodyctl
/usr/bin/prosody-migrator
/usr/bin/xwaylandvideobridge
/usr/lib/prosody
/usr/lib/prosody/prosody.version
/usr/lib/prosody/util/prosodyctl
/usr/lib/prosody/util/prosodyctl.lua
/usr/lib/systemd/system/jitsi-videobridge2.service
/usr/lib/systemd/system/prosody.service
/usr/local/lib/prosody
/usr/share/applications/org.kde.xwaylandvideobridge.desktop
/usr/share/doc/jicofo
/usr/share/doc/jitsi-meet
/usr/share/doc/jitsi-meet-prosody
/usr/share/doc/jitsi-meet-turnserver
/usr/share/doc/jitsi-meet-web
/usr/share/doc/jitsi-meet-web-config
/usr/share/doc/jitsi-videobridge2
/usr/share/doc/prosody
/usr/share/doc/xwaylandvideobridge
/usr/share/icons/hicolor/scalable/apps/xwaylandvideobridge.svg
/usr/share/jicofo
/usr/share/jicofo/jicofo.jar
/usr/share/jicofo/jicofo.sh
/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar
/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar
/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar
/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar
/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar
/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar
/usr/share/jitsi-meet
/usr/share/jitsi-meet/images/jitsilogo.png
/usr/share/jitsi-meet/libs/lib-jitsi-meet.e2ee-worker.js
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.js
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.js.LICENSE.txt
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.map
/usr/share/jitsi-meet-prosody
/usr/share/jitsi-meet/prosody-plugins
/usr/share/jitsi-meet/prosody-plugins/luajwtjitsi.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_jitsi-anonymous.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_jitsi-shared-secret.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jitsi_permissions.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jitsi_session.lua
/usr/share/jitsi-meet-prosody/prosody.cfg.lua-jvb.example
/usr/share/jitsi-meet-turnserver
/usr/share/jitsi-meet-turnserver/jitsi-meet.conf
/usr/share/jitsi-meet-web-config
/usr/share/jitsi-meet-web-config/jitsi-meet.example
/usr/share/jitsi-meet-web-config/jitsi-meet.example-apache
/usr/share/jitsi-videobridge
/usr/share/jitsi-videobridge/jitsi-videobridge.jar
/usr/share/jitsi-videobridge/lib/jain-sip-ri-ossonly-1.2.279-jitsi-oss1.jar
/usr/share/jitsi-videobridge/lib/jitsi-dcsctp-1.0-7-gb548df2.jar
/usr/share/jitsi-videobridge/lib/jitsi-media-transform-2.3-307-g4bb0aead1.jar
/usr/share/jitsi-videobridge/lib/jitsi-metaconfig-1.0-11-g8cf950e.jar
/usr/share/jitsi-videobridge/lib/jitsi-srtp-1.1-23-gaf3cd06.jar
/usr/share/jitsi-videobridge/lib/jitsi-utils-1.0-150-g4ab9a3b.jar
/usr/share/jitsi-videobridge/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar
/usr/share/jitsi-videobridge/lib/smack-core-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-extensions-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-im-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-java8-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-resolver-javax-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-sasl-javax-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-streammanagement-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-tcp-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-xmlparser-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/videobridge.rc
/usr/share/lintian/overrides/prosody
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
/usr/share/man/man1/prosodyctl.1.gz
/usr/share/man/man8/ejabberd2prosody.8.gz
/usr/share/man/man8/prosody.8.gz
/usr/share/man/man8/prosody-migrator.8.gz
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
/var/cache/apt/archives/prosody_13.0.1-1_amd64.deb
/var/cache/apt/archives/prosody_13.0.1-1+deb131u_amd64.deb
/var/lib/apt/lists/download.jitsi.org_stable_InRelease
/var/lib/apt/lists/download.jitsi.org_stable_Packages
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.chat.events-0
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.chat.events-1
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.chat.events-2
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.participant.events-0
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.participant.events-1
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.participant.events-2
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.room.events-0
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.room.events-1
/var/lib/docker/volumes/kafka_kafka-data/_data/jitsi.room.events-2
/var/lib/dpkg/info/jicofo.conffiles
/var/lib/dpkg/info/jicofo.list
/var/lib/dpkg/info/jicofo.md5sums
/var/lib/dpkg/info/jicofo.postinst
/var/lib/dpkg/info/jicofo.postrm
/var/lib/dpkg/info/jicofo.preinst
/var/lib/dpkg/info/jicofo.prerm
/var/lib/dpkg/info/jicofo.templates
/var/lib/dpkg/info/jitsi-meet.list
/var/lib/dpkg/info/jitsi-meet.md5sums
/var/lib/dpkg/info/jitsi-meet.postinst
/var/lib/dpkg/info/jitsi-meet.postrm
/var/lib/dpkg/info/jitsi-meet-prosody.list
/var/lib/dpkg/info/jitsi-meet-prosody.md5sums
/var/lib/dpkg/info/jitsi-meet-prosody.postinst
/var/lib/dpkg/info/jitsi-meet-prosody.postrm
/var/lib/dpkg/info/jitsi-meet-prosody.templates
/var/lib/dpkg/info/jitsi-meet-prosody.triggers
/var/lib/dpkg/info/jitsi-meet-turnserver.list
/var/lib/dpkg/info/jitsi-meet-turnserver.md5sums
/var/lib/dpkg/info/jitsi-meet-turnserver.postinst
/var/lib/dpkg/info/jitsi-meet-turnserver.postrm
/var/lib/dpkg/info/jitsi-meet-turnserver.templates
/var/lib/dpkg/info/jitsi-meet-web-config.list
/var/lib/dpkg/info/jitsi-meet-web-config.md5sums
/var/lib/dpkg/info/jitsi-meet-web-config.postinst
/var/lib/dpkg/info/jitsi-meet-web-config.postrm
/var/lib/dpkg/info/jitsi-meet-web-config.templates
/var/lib/dpkg/info/jitsi-meet-web.list
/var/lib/dpkg/info/jitsi-meet-web.md5sums
/var/lib/dpkg/info/jitsi-videobridge2.conffiles
/var/lib/dpkg/info/jitsi-videobridge2.config
/var/lib/dpkg/info/jitsi-videobridge2.list
/var/lib/dpkg/info/jitsi-videobridge2.md5sums
/var/lib/dpkg/info/jitsi-videobridge2.postinst
/var/lib/dpkg/info/jitsi-videobridge2.postrm
/var/lib/dpkg/info/jitsi-videobridge2.prerm
/var/lib/dpkg/info/jitsi-videobridge2.templates
/var/lib/dpkg/info/prosody.conffiles
/var/lib/dpkg/info/prosody.list
/var/lib/dpkg/info/prosody.md5sums
/var/lib/dpkg/info/prosody.postinst
/var/lib/dpkg/info/prosody.postrm
/var/lib/dpkg/info/prosody.preinst
/var/lib/dpkg/info/prosody.prerm
/var/lib/dpkg/info/xwaylandvideobridge.conffiles
/var/lib/dpkg/info/xwaylandvideobridge.list
/var/lib/dpkg/info/xwaylandvideobridge.md5sums
/var/lib/prosody
/var/lib/prosody/prosody.sock
/var/lib/swcatalog/icons/debian-trixie-main/128x128/xwaylandvideobridge_xwaylandvideobridge.png
/var/lib/swcatalog/icons/debian-trixie-main/48x48/xwaylandvideobridge_xwaylandvideobridge.png
/var/lib/swcatalog/icons/debian-trixie-main/64x64/xwaylandvideobridge_xwaylandvideobridge.png
/var/lib/systemd/deb-systemd-helper-enabled/jitsi-videobridge2.service.dsh-also
/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants/jitsi-videobridge2.service
/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants/prosody.service
/var/lib/systemd/deb-systemd-helper-enabled/prosody.service.dsh-also
/var/log/jitsi
/var/log/jitsi/jicofo.log
/var/log/jitsi/jicofo.log.1
/var/log/jitsi/jicofo.log.2.gz
/var/log/jitsi/jicofo.log.3.gz
/var/log/jitsi/jicofo.log.4.gz
/var/log/jitsi/jicofo.log.5.gz
/var/log/jitsi/jicofo.log.6.gz
/var/log/jitsi/jicofo.log.7.gz
/var/log/prosody
/var/log/prosody/prosody.err
/var/log/prosody/prosody.err.1
/var/log/prosody/prosody.err.2.gz
/var/log/prosody/prosody.err.3.gz
/var/log/prosody/prosody.err.4.gz
/var/log/prosody/prosody.log
/var/log/prosody/prosody.log.1
/var/log/prosody/prosody.log.2.gz
/var/log/prosody/prosody.log.3.gz
/var/log/prosody/prosody.log.4.gz


## Configurations


```text
$ find /etc -xdev -type f 2>/dev/null | grep -Ei "jitsi|jicofo|videobridge|prosody|turnserver" | sort
```
/etc/apt/keyrings/jitsi.gpg
/etc/apt/sources.list.d/jitsi-stable.list
/etc/init.d/jicofo
/etc/init.d/jitsi-videobridge2
/etc/init.d/prosody
/etc/jitsi/jicofo/config
/etc/jitsi/jicofo/jicofo.conf
/etc/jitsi/jicofo/logging.properties
/etc/jitsi/meet/meet.civitas.local-config.js
/etc/jitsi/videobridge/config
/etc/jitsi/videobridge/jvb.conf
/etc/jitsi/videobridge/logging.properties
/etc/logrotate.d/jicofo
/etc/logrotate.d/jitsi-videobridge
/etc/logrotate.d/prosody
/etc/prosody/conf.avail/example.com.cfg.lua
/etc/prosody/conf.avail/jaas.cfg.lua
/etc/prosody/conf.avail/localhost.cfg.lua
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua
/etc/prosody/conf.d/meet.civitas.local.cfg.lua
/etc/prosody/migrator.cfg.lua
/etc/prosody/prosody.cfg.lua
/etc/prosody/README
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf
/etc/turnserver.conf
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
/lib/systemd/system/jitsi-videobridge2.service
/lib/systemd/system/prosody.service
/usr/lib/systemd/system/coturn.service
/usr/lib/systemd/system/jitsi-videobridge2.service
/usr/lib/systemd/system/prosody.service



---

# 14. /ETC/JITSI

**Date :** 2026-08-08 06:56:35 EDT


```text
$ find /etc/jitsi -print 2>/dev/null | sort || true
```
/etc/jitsi
/etc/jitsi/jicofo
/etc/jitsi/jicofo/config
/etc/jitsi/jicofo/jicofo.conf
/etc/jitsi/jicofo/logging.properties
/etc/jitsi/meet
/etc/jitsi/meet/meet.civitas.local-config.js
/etc/jitsi/videobridge
/etc/jitsi/videobridge/config
/etc/jitsi/videobridge/jvb.conf
/etc/jitsi/videobridge/logging.properties



---

# 15. DONNÉES /VAR/LIB

**Date :** 2026-08-08 06:56:35 EDT


```text
$ find /var/lib -maxdepth 4 \( -iname "*jitsi*" -o -iname "*prosody*" -o -iname "*jicofo*" \) -print 2>/dev/null | sort
```
/var/lib/apt/lists/download.jitsi.org_stable_InRelease
/var/lib/apt/lists/download.jitsi.org_stable_Packages
/var/lib/dpkg/info/jicofo.conffiles
/var/lib/dpkg/info/jicofo.list
/var/lib/dpkg/info/jicofo.md5sums
/var/lib/dpkg/info/jicofo.postinst
/var/lib/dpkg/info/jicofo.postrm
/var/lib/dpkg/info/jicofo.preinst
/var/lib/dpkg/info/jicofo.prerm
/var/lib/dpkg/info/jicofo.templates
/var/lib/dpkg/info/jitsi-meet.list
/var/lib/dpkg/info/jitsi-meet.md5sums
/var/lib/dpkg/info/jitsi-meet.postinst
/var/lib/dpkg/info/jitsi-meet.postrm
/var/lib/dpkg/info/jitsi-meet-prosody.list
/var/lib/dpkg/info/jitsi-meet-prosody.md5sums
/var/lib/dpkg/info/jitsi-meet-prosody.postinst
/var/lib/dpkg/info/jitsi-meet-prosody.postrm
/var/lib/dpkg/info/jitsi-meet-prosody.templates
/var/lib/dpkg/info/jitsi-meet-prosody.triggers
/var/lib/dpkg/info/jitsi-meet-turnserver.list
/var/lib/dpkg/info/jitsi-meet-turnserver.md5sums
/var/lib/dpkg/info/jitsi-meet-turnserver.postinst
/var/lib/dpkg/info/jitsi-meet-turnserver.postrm
/var/lib/dpkg/info/jitsi-meet-turnserver.templates
/var/lib/dpkg/info/jitsi-meet-web-config.list
/var/lib/dpkg/info/jitsi-meet-web-config.md5sums
/var/lib/dpkg/info/jitsi-meet-web-config.postinst
/var/lib/dpkg/info/jitsi-meet-web-config.postrm
/var/lib/dpkg/info/jitsi-meet-web-config.templates
/var/lib/dpkg/info/jitsi-meet-web.list
/var/lib/dpkg/info/jitsi-meet-web.md5sums
/var/lib/dpkg/info/jitsi-videobridge2.conffiles
/var/lib/dpkg/info/jitsi-videobridge2.config
/var/lib/dpkg/info/jitsi-videobridge2.list
/var/lib/dpkg/info/jitsi-videobridge2.md5sums
/var/lib/dpkg/info/jitsi-videobridge2.postinst
/var/lib/dpkg/info/jitsi-videobridge2.postrm
/var/lib/dpkg/info/jitsi-videobridge2.prerm
/var/lib/dpkg/info/jitsi-videobridge2.templates
/var/lib/dpkg/info/prosody.conffiles
/var/lib/dpkg/info/prosody.list
/var/lib/dpkg/info/prosody.md5sums
/var/lib/dpkg/info/prosody.postinst
/var/lib/dpkg/info/prosody.postrm
/var/lib/dpkg/info/prosody.preinst
/var/lib/dpkg/info/prosody.prerm
/var/lib/prosody
/var/lib/prosody/prosody.sock
/var/lib/systemd/deb-systemd-helper-enabled/jitsi-videobridge2.service.dsh-also
/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants/jitsi-videobridge2.service
/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants/prosody.service
/var/lib/systemd/deb-systemd-helper-enabled/prosody.service.dsh-also



---

# 16. LOGS

**Date :** 2026-08-08 06:56:35 EDT


## Répertoires


```text
$ find /var/log -maxdepth 4 \( -iname "*jitsi*" -o -iname "*prosody*" -o -iname "*jicofo*" -o -iname "*videobridge*" -o -iname "*turn*" \) -print 2>/dev/null | sort
```
/var/log/jitsi
/var/log/jitsi/jicofo.log
/var/log/jitsi/jicofo.log.1
/var/log/jitsi/jicofo.log.2.gz
/var/log/jitsi/jicofo.log.3.gz
/var/log/jitsi/jicofo.log.4.gz
/var/log/jitsi/jicofo.log.5.gz
/var/log/jitsi/jicofo.log.6.gz
/var/log/jitsi/jicofo.log.7.gz
/var/log/prosody
/var/log/prosody/prosody.err
/var/log/prosody/prosody.err.1
/var/log/prosody/prosody.err.2.gz
/var/log/prosody/prosody.err.3.gz
/var/log/prosody/prosody.err.4.gz
/var/log/prosody/prosody.log
/var/log/prosody/prosody.log.1
/var/log/prosody/prosody.log.2.gz
/var/log/prosody/prosody.log.3.gz
/var/log/prosody/prosody.log.4.gz
/var/log/turnserver
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
/var/log/turnserver/turn_920_2026-07-28.log
/var/log/turnserver/turn_925_2026-07-28.log
/var/log/turnserver/turn_926_2026-07-30.log
/var/log/turnserver/turn_934_2026-07-28.log
/var/log/turnserver/turn_961_2026-07-28.log
/var/log/turnserver/turn_964_2026-07-28.log
/var/log/turnserver/turn_966_2026-07-30.log
/var/log/turnserver/turn_971_2026-07-28.log
/var/log/turnserver/turn_973_2026-07-28.log
/var/log/turnserver/turn_977_2026-07-27.log
/var/log/turnserver/turn_979_2026-07-28.log
/var/log/turnserver/turn_979_2026-07-30.log
/var/log/turnserver/turn_981_2026-07-28.log
/var/log/turnserver/turn_984_2026-07-28.log
/var/log/turnserver/turn_984_2026-07-30.log
/var/log/turnserver/turn_985_2026-07-28.log
/var/log/turnserver/turn_985_2026-08-03.log
/var/log/turnserver/turn_988_2026-07-28.log
/var/log/turnserver/turn_990_2026-07-28.log
/var/log/turnserver/turn_990_2026-07-30.log
/var/log/turnserver/turn_993_2026-08-07.log
/var/log/turnserver/turn_996_2026-07-28.log
/var/log/turnserver/turn_998_2026-07-30.log
/var/log/turnserver/turn.log


## Journalctl


```text
$ journalctl -u jicofo --no-pager -n 300 2>/dev/null || true
```
Mar 22 20:12:32 meet.civitas.local jicofo[14942]: Starting jicofo: jicofo started.
Mar 22 20:12:32 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:20:07 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:20:07 meet.civitas.local jicofo[94489]: Stopping jicofo: jicofo stopped.
Mar 22 22:20:07 meet.civitas.local systemd[1]: jicofo.service: Deactivated successfully.
Mar 22 22:20:07 meet.civitas.local systemd[1]: jicofo.service: Unit process 14951 (java) remains running after unit stopped.
Mar 22 22:20:07 meet.civitas.local systemd[1]: Stopped jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:20:07 meet.civitas.local systemd[1]: jicofo.service: Consumed 2min 20.794s CPU time, 353.7M memory peak.
Mar 22 22:20:07 meet.civitas.local systemd[1]: jicofo.service: Found left-over process 14951 (java) in control group while starting unit. Ignoring.
Mar 22 22:20:07 meet.civitas.local systemd[1]: jicofo.service: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Mar 22 22:20:07 meet.civitas.local systemd[1]: Starting jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:20:07 meet.civitas.local jicofo[94497]: Starting jicofo: jicofo started.
Mar 22 22:20:07 meet.civitas.local systemd[1]: Started jicofo.service - LSB: Jitsi conference Focus.
Mar 22 22:26:53 meet.civitas.local systemd[1]: Stopping jicofo.service - LSB: Jitsi conference Focus...
Mar 22 22:26:53 meet.civitas.local jicofo[97404]: Stopping jicofo: jicofo stopped.
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


```text
$ journalctl -u jitsi-videobridge2 --no-pager -n 300 2>/dev/null || true
```
Mar 22 20:12:01 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:12:01 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
Mar 22 20:12:01 meet.civitas.local systemd[1]: /usr/lib/systemd/system/jitsi-videobridge2.service:17: PIDFile= references a path below legacy directory /var/run/, updating /var/run/jitsi-videobridge/jitsi-videobridge.pid → /run/jitsi-videobridge/jitsi-videobridge.pid; please update the unit file accordingly.
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


```text
$ journalctl -u prosody --no-pager -n 300 2>/dev/null || true
```
Mar 22 22:01:16 meet.civitas.local prosody[83764]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 22 22:01:16 meet.civitas.local prosody[83764]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 22 22:01:16 meet.civitas.local prosody[83764]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 22 22:06:05 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 22 22:06:05 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 22 22:06:05 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 22 22:06:05 meet.civitas.local systemd[1]: prosody.service: Consumed 6.894s CPU time, 17.4M memory peak.
Mar 22 22:06:05 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 22 22:06:05 meet.civitas.local prosody[86611]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 22 22:06:05 meet.civitas.local prosody[86611]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 22 22:06:05 meet.civitas.local prosody[86611]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 22 22:06:05 meet.civitas.local prosody[86611]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 22 22:15:47 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 22 22:15:47 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 22 22:15:47 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 22 22:15:47 meet.civitas.local systemd[1]: prosody.service: Consumed 12.284s CPU time, 19.1M memory peak.
Mar 22 22:15:47 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 22 22:15:48 meet.civitas.local prosody[92214]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 22 22:15:48 meet.civitas.local prosody[92214]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 22 22:15:48 meet.civitas.local prosody[92214]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 22 22:15:48 meet.civitas.local prosody[92214]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 22 22:29:15 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
Mar 22 22:29:15 meet.civitas.local systemd[1]: prosody.service: Deactivated successfully.
Mar 22 22:29:15 meet.civitas.local systemd[1]: Stopped prosody.service - Prosody XMPP Server.
Mar 22 22:29:15 meet.civitas.local systemd[1]: prosody.service: Consumed 14.694s CPU time, 17.8M memory peak.
Mar 22 22:29:15 meet.civitas.local systemd[1]: Started prosody.service - Prosody XMPP Server.
Mar 22 22:29:15 meet.civitas.local prosody[98796]: meet.civitas.local:conference_duration: lobby not enabled missing main_muc config
Mar 22 22:29:15 meet.civitas.local prosody[98796]: meet.civitas.local:muc_breakout_rooms: breakout rooms not enabled missing main_muc config
Mar 22 22:29:15 meet.civitas.local prosody[98796]: meet.civitas.local:end_conference: No muc_component specified. No muc to operate on!
Mar 22 22:29:15 meet.civitas.local prosody[98796]: modulemanager: Unable to load module 'muc_lobby': /usr/lib/prosody/modules/share/lua/5.4/mod_muc_lobby/mod_muc_lobby.lua: No such file or directory
Mar 22 22:39:31 meet.civitas.local systemd[1]: Stopping prosody.service - Prosody XMPP Server...
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


```text
$ journalctl -u coturn --no-pager -n 300 2>/dev/null || true
```
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This database can be used for long-term credentials mechanism users,
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 and it can store the secret value(s) for secret-based timed authentication in TURN REST API.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 See http://www.postgresql.org/docs/8.4/static/libpq-connect.html for 8.x PostgreSQL
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 versions format, see
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 http://www.postgresql.org/docs/9.2/static/libpq-connect.html#LIBPQ-CONNSTRING
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 for 9.x and newer connection string formats.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -M, --mysql-userdb        <connection-string>        MySQL database connection string, if used (default - empty, no MySQL DB used).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This database can be used for long-term credentials mechanism users,
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 and it can store the secret value(s) for secret-based timed authentication in TURN REST API.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 The connection string my be space-separated list of parameters:
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 192.0.2.0-192.0.2.255
Aug 07 05:25:29 meet.civitas.local systemd[1]: Failed to start coturn.service - coTURN STUN/TURN Server.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                   "host=<ip-addr> dbname=<database-name> user=<database-user> \
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                         password=<database-user-password> port=<db-port> connect_timeout=<seconds> read_timeout=<seconds>".
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 The connection string parameters for the secure communications (SSL):
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 ca, capath, cert, key, cipher
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 (see http://dev.mysql.com/doc/refman/5.1/en/ssl-options.html for the
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 command options description).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                   All connection-string parameters are optional.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --secret-key-file        <filename>                This is the file path which contain secret key of aes encryption while using MySQL password encryption.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 If you want to use in the MySQL connection string the password in encrypted format,
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 then set in this option the file path of the secret key. The key which is used to encrypt MySQL password.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Warning: If this option is set, then MySQL password must be set in "mysql-userdb" option in encrypted format!
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 If you want to use cleartext password then do not set this option!
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -N, --redis-userdb        <connection-string>        Redis user database connection string, if used (default - empty, no Redis DB used).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This database can be used for long-term credentials mechanism users,
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 and it can store the secret value(s) for secret-based timed authentication in TURN REST API.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 The connection string my be space-separated list of parameters:
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                   "host=<ip-addr> dbname=<db-number> \
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                                 password=<database-user-password> port=<db-port> connect_timeout=<seconds>".
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                   All connection-string parameters are optional.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -O, --redis-statsdb        <connection-string>        Redis status and statistics database connection string, if used
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 (default - empty, no Redis stats DB used).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This database keeps allocations status information, and it can be also used for publishing
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 and delivering traffic and allocation event notifications.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 192.88.99.0-192.88.99.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 The connection string has the same parameters as redis-userdb connection string.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --use-auth-secret                                TURN REST API flag.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Flag that sets a special authorization option that is based upon authentication secret
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 (TURN Server REST API, see TURNServerRESTAPI.pdf). This option is used with timestamp.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --static-auth-secret                <secret>        'Static' authentication secret value (a string) for TURN REST API only.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 If not set, then the turn server will try to use the 'dynamic' value
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 in turn_secret table in user database (if present).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 That database value can be changed on-the-fly
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 by a separate program, so this is why it is 'dynamic'.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Multiple shared secrets can be used (both in the database and in the "static" fashion).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-auth-pings                                Disable periodic health checks to 'dynamic' auth secret tables.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-dynamic-ip-list                                Do not use dynamic allowed/denied peer ip list.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-dynamic-realms                                Do not use dynamic realm assignment and options.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --server-name                                        Server name used for
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 the oAuth authentication purposes.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 The default value is the realm name.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --oauth                                        Support oAuth authentication.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -n                                                Do not use configuration file, take all parameters from the command line only.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --cert                        <filename>                Certificate file, PEM format. Same file search rules
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 applied as for the configuration file.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 If both --no-tls and --no_dtls options
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 are specified, then this parameter is not needed.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --pkey                        <filename>                Private key file, PEM format. Same file search rules
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 applied as for the configuration file.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 If both --no-tls and --no-dtls options
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --pkey-pwd                <password>                If the private key file is encrypted, then this password to be used.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --cipher-list        <"cipher-string">                Allowed OpenSSL cipher list for TLS/DTLS connections.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Default value is "DEFAULT".
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --CA-file                <filename>                CA file in OpenSSL format.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Forces TURN server to verify the client SSL certificates.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 By default, no CA is set and no client certificate check is performed.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 192.168.0.0-192.168.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --ec-curve-name        <curve-name>                Curve name for EC ciphers, if supported by OpenSSL
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 library (TLS and DTLS). The default value is prime256v1,
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 if pre-OpenSSL 1.0.2 is used. With OpenSSL 1.0.2+,
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 an optimal curve will be automatically calculated, if not defined
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 by this option.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --dh566                                        Use 566 bits predefined DH TLS key. Default size of the predefined key is 2066.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --dh1066                                        Use 1066 bits predefined DH TLS key. Default size of the predefined key is 2066.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --dh-file        <dh-file-name>                        Use custom DH TLS key, stored in PEM format in the file.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Flags --dh566 and --dh1066 are ignored when the DH key is taken from a file.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-tlsv1                                        Do not allow TLSv1/DTLSv1 protocol.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-tlsv1_1                                        Do not allow TLSv1.1 protocol.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-tlsv1_2                                        Do not allow TLSv1.2/DTLSv1.2 protocol.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-udp                                        Do not start UDP client listeners.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-tcp                                        Do not start TCP client listeners.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-tls                                        Do not start TLS client listeners.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-dtls                                        Do not start DTLS client listeners.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-udp-relay                                        Do not allow UDP relay endpoints, use only TCP relay option.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-tcp-relay                                        Do not allow TCP relay endpoints, use only UDP relay options.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -l, --log-file                <filename>                Option to set the full path name of the log file.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 By default, the turnserver tries to open a log file in
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 /var/log/turnserver/, /var/log, /var/tmp, /tmp and . (current) directories
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 (which open operation succeeds first that file will be used).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 With this option you can set the definite log file name.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 The special names are "stdout" and "-" - they will force everything
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 to the stdout; and "syslog" name will force all output to the syslog.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-stdout-log                                Flag to prevent stdout log messages.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 By default, all log messages are going to both stdout and to
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 a log file. With this option everything will be going to the log file only
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 (unless the log file itself is stdout).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --syslog                                        Output all log information into the system log (syslog), do not use the file output.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 198.18.0.0-198.19.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --syslog-facility             <value>          Set syslog facility for syslog messages. Default is ''.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --simple-log                                        This flag means that no log file rollover will be used, and the log file
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 name will be constructed as-is, without PID and date appendage.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This option can be used, for example, together with the logrotate tool.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --new-log-timestamp                                Enable full ISO-8601 timestamp in all logs.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --new-log-timestamp-format            <format>        Set timestamp format (in strftime(1) format). Depends on --new-log-timestamp to be enabled.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --log-binding                                        Log STUN binding request. It is now disabled by default to avoid DoS attacks.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --stale-nonce[=<value>]                        Use extra security with nonce value having limited lifetime (default 600 secs).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --max-allocate-lifetime        <value>                Set the maximum value for the allocation lifetime. Default to 3600 secs.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --channel-lifetime                <value>                Set the lifetime for channel binding, default to 600 secs.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This value MUST not be changed for production purposes.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --permission-lifetime                <value>                Set the value for the lifetime of the permission. Default to 300 secs.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This MUST not be changed for production purposes.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -S, --stun-only                                Option to set standalone STUN operation only, all TURN requests will be ignored.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:      --no-stun                                        Option to suppress STUN functionality, only TURN requests will be processed.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --alternate-server                <ip:port>        Set the TURN server to redirect the allocate requests (UDP and TCP services).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Multiple alternate-server options can be set for load balancing purposes.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 See the docs for more information.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --tls-alternate-server        <ip:port>                Set the TURN server to redirect the allocate requests (DTLS and TLS services).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Multiple alternate-server options can be set for load balancing purposes.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 See the docs for more information.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -C, --rest-api-separator        <SYMBOL>        This is the timestamp/username separator symbol (character) in TURN REST API.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 The default value is ':'.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 198.51.100.0-198.51.100.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --max-allocate-timeout=<seconds>                Max time, in seconds, allowed for full allocation establishment. Default is 60.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --allowed-peer-ip=<ip[-ip]>                         Specifies an ip or range of ips that are explicitly allowed to connect to the
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 turn server. Multiple allowed-peer-ip can be set.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --denied-peer-ip=<ip[-ip]>                         Specifies an ip or range of ips that are not allowed to connect to the turn server.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Multiple denied-peer-ip can be set.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --pidfile <"pid-file-name">                        File name to store the pid of the process.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Default is /var/run/turnserver.pid (if superuser account is used) or
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 /var/tmp/turnserver.pid .
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --acme-redirect <URL>                                Redirect ACME, i.e. HTTP GET requests matching '^/.well-known/acme-challenge/(.*)' to '<URL>$1'.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Default is '', i.e. no special handling for such requests.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --secure-stun                                        Require authentication of the STUN Binding request.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 By default, the clients are allowed anonymous access to the STUN Binding functionality.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --proc-user <user-name>                        User name to run the turnserver process.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 After the initialization, the turnserver process
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 will make an attempt to change the current user ID to that user.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --proc-group <group-name>                        Group name to run the turnserver process.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 After the initialization, the turnserver process
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 will make an attempt to change the current group ID to that group.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --mobility                                        Mobility with ICE (MICE) specs support.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -K, --keep-address-family                        Deprecated in favor of --allocation-default-address-family!!
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 TURN server allocates address family according TURN
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Client <=> Server communication address family.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 !! It breaks RFC6156 section-4.2 (violates default IPv4) !!
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -A --allocation-default-address-family=<ipv4|ipv6|keep>                 Default is IPv4
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 TURN server allocates address family according TURN client requested address family.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 If address family is not requested explicitly by client, then it falls back to this default.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 The standard RFC explicitly define actually that this default must be IPv4,
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 203.0.113.0-203.0.113.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                        so use other option values with care!
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-cli                                        Turn OFF the CLI support. By default it is always ON.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --cli-ip=<IP>                                        Local system IP address to be used for CLI server endpoint. Default value
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 is 127.0.0.1.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --cli-port=<port>                                CLI server port. Default is 5766.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --cli-password=<password>                        CLI access password. Default is empty (no password).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 For the security reasons, it is recommended to use the encrypted
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 for of the password (see the -P command in the turnadmin utility).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 The dollar signs in the encrypted form must be escaped.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --web-admin                                        Enable Turn Web-admin support. By default it is disabled.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --web-admin-ip=<IP>                                Local system IP address to be used for Web-admin server endpoint. Default value
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 is 127.0.0.1.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --web-admin-port=<port>                        Web-admin server port. Default is 8080.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --web-admin-listen-on-workers                        Enable for web-admin server to listens on STUN/TURN workers STUN/TURN ports.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 By default it is disabled for security reasons!
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 (This behavior used to be the default behavior, and was enabled by default.)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --server-relay                                        Server relay. NON-STANDARD AND DANGEROUS OPTION. Only for those applications
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 when we want to run server applications on the relay endpoints.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This option eliminates the IP permissions check on the packets
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 incoming to the relay endpoints.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --cli-max-output-sessions                        Maximum number of output sessions in ps CLI command.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This value can be changed on-the-fly in CLI. The default value is 256.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --ne=[1|2|3]                                        Set network engine type for the process (for internal purposes).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-rfc5780                                        Disable RFC5780 (NAT behavior discovery).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Originally, if there are more than one listener address from the same
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 address family, then by default the NAT behavior discovery feature enabled.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 This option disables this original behavior, because the NAT behavior discovery
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 adds attributes to response, and this increase the possibility of an amplification attack.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 240.0.0.0-255.255.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 Strongly encouraged to use this option to decrease gain factor in STUN binding responses.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --no-stun-backward-compatibility                Disable handling old STUN Binding requests and disable MAPPED-ADDRESS attribute
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:                                                 in binding response (use only the XOR-MAPPED-ADDRESS).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --response-origin-only-with-rfc5780                Only send RESPONSE-ORIGIN attribute in binding response if RFC5780 is enabled.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  --version                                        Print version (and exit).
Aug 07 05:25:29 meet.civitas.local turnserver[1056]:  -h                                                Help
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Bad configuration format: no-loopback-peers
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : log file opened: /var/log/turnserver/turn_1056_2026-08-07.log
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Bad configuration format: dh2066
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Bad configuration format: no-loopback-peers
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Bad configuration format: dh2066
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 0.0.0.0-0.255.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 10.0.0.0-10.255.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 100.64.0.0-100.127.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 127.0.0.0-127.255.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 169.254.0.0-169.254.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 127.0.0.0-127.255.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 172.16.0.0-172.31.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 192.0.0.0-192.0.0.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 192.0.2.0-192.0.2.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 192.88.99.0-192.88.99.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 192.168.0.0-192.168.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 198.18.0.0-198.19.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 198.51.100.0-198.51.100.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 203.0.113.0-203.0.113.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 240.0.0.0-255.255.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: ::1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 64:ff9b::-64:ff9b::ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: ::ffff:0.0.0.0-::ffff:255.255.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 100::-100::ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 2001::-2001:1ff:ffff:ffff:ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 2002::-2002:ffff:ffff:ffff:ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: fc00::-fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: fe80::-febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Bad configuration format: no-loopback-peers
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Bad configuration format: dh2066
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: :
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: RFC 3489/5389/5766/5780/6062/6156 STUN/TURN Server
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: Version Coturn-4.6.1 'Gorst'
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: :
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: ::1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: Max number of open files/sockets allowed for this process: 524288
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: :
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: Due to the open files/sockets limitation,
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: max supported number of TURN Sessions possible is: 262000 (approximately)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: :
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: ==== Show him the instruments, Practical Frost: ====
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : TLS supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : DTLS supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : DTLS 1.2 supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : TURN/STUN ALPN supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Third-party authorization (oAuth) supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : GCM (AEAD) supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : OpenSSL compile-time version: OpenSSL 3.2.2-dev  (0x30200020)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: :
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : SQLite supported, default database location is /var/lib/turn/turndb
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Redis supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : PostgreSQL supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : MySQL supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : MongoDB is not supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: :
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Default Net Engine version: 3 (UDP thread per CPU core)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: =====================================================
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Domain name:
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Default realm: meet.civitas.local
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: :
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: CONFIG: --no-tcp-relay: TCP relay endpoints are not allowed.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot find certificate file: /etc/ssl/meet.civitas.local.crt (1)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot start TLS and DTLS listeners because certificate file is not set properly
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot find private key file: /etc/ssl/meet.civitas.local.key (1)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot start TLS and DTLS listeners because private key file is not set properly
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : NO EXPLICIT LISTENER ADDRESS(ES) ARE CONFIGURED
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : ===========Discovering listener addresses: =========
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Listener address to use: 127.0.0.1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Listener address to use: ::1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : ERROR: main: Cannot configure any meaningful IP listener address
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 64:ff9b::-64:ff9b::ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: ::ffff:0.0.0.0-::ffff:255.255.255.255
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 100::-100::ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 2001::-2001:1ff:ffff:ffff:ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: 2002::-2002:ffff:ffff:ffff:ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: fc00::-fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Black listing: fe80::-febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Bad configuration format: no-loopback-peers
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Bad configuration format: dh2066
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : 
                                                     RFC 3489/5389/5766/5780/6062/6156 STUN/TURN Server
                                                     Version Coturn-4.6.1 'Gorst'
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : 
                                                     Max number of open files/sockets allowed for this process: 524288
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : 
                                                     Due to the open files/sockets limitation,
                                                     max supported number of TURN Sessions possible is: 262000 (approximately)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : 
                                                     
                                                     ==== Show him the instruments, Practical Frost: ====
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : TLS supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : DTLS supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : DTLS 1.2 supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : TURN/STUN ALPN supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Third-party authorization (oAuth) supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : GCM (AEAD) supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : OpenSSL compile-time version: OpenSSL 3.2.2-dev  (0x30200020)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: :
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : SQLite supported, default database location is /var/lib/turn/turndb
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Redis supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : PostgreSQL supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : MySQL supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : MongoDB is not supported
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: :
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Default Net Engine version: 3 (UDP thread per CPU core)
                                                     
                                                     =====================================================
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Domain name:
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Default realm: meet.civitas.local
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : 
                                                     CONFIG: --no-tcp-relay: TCP relay endpoints are not allowed.
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot find certificate file: /etc/ssl/meet.civitas.local.crt (1)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot start TLS and DTLS listeners because certificate file is not set properly
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot find private key file: /etc/ssl/meet.civitas.local.key (1)
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : WARNING: cannot start TLS and DTLS listeners because private key file is not set properly
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : NO EXPLICIT LISTENER ADDRESS(ES) ARE CONFIGURED
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : ===========Discovering listener addresses: =========
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Listener address to use: 127.0.0.1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : Listener address to use: ::1
Aug 07 05:25:29 meet.civitas.local turnserver[1056]: 0: : ERROR: main: Cannot configure any meaningful IP listener address
Aug 07 05:25:29 meet.civitas.local systemd[1]: coturn.service: Scheduled restart job, restart counter is at 5.
Aug 07 05:25:29 meet.civitas.local systemd[1]: coturn.service: Start request repeated too quickly.
Aug 07 05:25:29 meet.civitas.local systemd[1]: coturn.service: Failed with result 'exit-code'.
Aug 07 05:25:29 meet.civitas.local systemd[1]: Failed to start coturn.service - coTURN STUN/TURN Server.


```text
$ journalctl -u nginx --no-pager -n 300 2>/dev/null || true
```
Mar 22 20:21:51 meet.civitas.local systemd[1]: Reloaded nginx.service - A high performance web server and a reverse proxy server.
Mar 22 22:29:15 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 22 22:29:15 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 22 22:29:15 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Mar 22 22:29:15 meet.civitas.local systemd[1]: nginx.service: Consumed 2.416s CPU time, 11.7M memory peak.
Mar 22 22:29:15 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 22 22:29:15 meet.civitas.local nginx[98803]: 2026/03/22 22:29:15 [warn] 98803#98803: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 22 22:29:15 meet.civitas.local nginx[98803]: 2026/03/22 22:29:15 [warn] 98803#98803: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 22 22:29:15 meet.civitas.local nginx[98803]: 2026/03/22 22:29:15 [warn] 98803#98803: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 22 22:29:15 meet.civitas.local nginx[98811]: 2026/03/22 22:29:15 [warn] 98811#98811: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 22 22:29:15 meet.civitas.local nginx[98811]: 2026/03/22 22:29:15 [warn] 98811#98811: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 22 22:29:15 meet.civitas.local nginx[98811]: 2026/03/22 22:29:15 [warn] 98811#98811: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 22 22:29:15 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
Mar 23 12:45:46 meet.civitas.local systemd[1]: Stopping nginx.service - A high performance web server and a reverse proxy server...
Mar 23 12:45:46 meet.civitas.local systemd[1]: nginx.service: Deactivated successfully.
Mar 23 12:45:46 meet.civitas.local systemd[1]: Stopped nginx.service - A high performance web server and a reverse proxy server.
Mar 23 12:45:46 meet.civitas.local systemd[1]: nginx.service: Consumed 10.038s CPU time, 17.4M memory peak.
-- Boot 9286f364297e4b8c9fe1cccd67828118 --
Mar 23 16:59:56 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 23 16:59:56 meet.civitas.local nginx[1021]: 2026/03/23 16:59:56 [warn] 1021#1021: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 23 16:59:56 meet.civitas.local nginx[1021]: 2026/03/23 16:59:56 [warn] 1021#1021: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 23 16:59:56 meet.civitas.local nginx[1021]: 2026/03/23 16:59:56 [warn] 1021#1021: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 23 16:59:56 meet.civitas.local nginx[1030]: 2026/03/23 16:59:56 [warn] 1030#1030: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 23 16:59:56 meet.civitas.local nginx[1030]: 2026/03/23 16:59:56 [warn] 1030#1030: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 23 16:59:56 meet.civitas.local nginx[1030]: 2026/03/23 16:59:56 [warn] 1030#1030: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 23 16:59:56 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
-- Boot 4ae73edac0c84a74baf7f2914fe6b03d --
Mar 24 15:32:04 meet.civitas.local systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Mar 24 15:32:04 meet.civitas.local nginx[1139]: 2026/03/24 15:32:04 [warn] 1139#1139: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 24 15:32:04 meet.civitas.local nginx[1139]: 2026/03/24 15:32:04 [warn] 1139#1139: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 24 15:32:04 meet.civitas.local nginx[1139]: 2026/03/24 15:32:04 [warn] 1139#1139: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 24 15:32:04 meet.civitas.local nginx[1146]: 2026/03/24 15:32:04 [warn] 1146#1146: duplicate extension "wasm", content type: "application/wasm", previous content type: "application/wasm" in /etc/nginx/sites-enabled/meet.civitas.local.conf:5
Mar 24 15:32:04 meet.civitas.local nginx[1146]: 2026/03/24 15:32:04 [warn] 1146#1146: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:46
Mar 24 15:32:04 meet.civitas.local nginx[1146]: 2026/03/24 15:32:04 [warn] 1146#1146: the "listen ... http2" directive is deprecated, use the "http2" directive instead in /etc/nginx/sites-enabled/meet.civitas.local.conf:47
Mar 24 15:32:04 meet.civitas.local systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
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



---

# 17. UTILISATEURS ET GROUPES

**Date :** 2026-08-08 06:56:36 EDT


## Utilisateurs Jitsi


```text
$ getent passwd | grep -Ei "jitsi|prosody|jicofo|turn" || true
```
jvb:x:997:1001::/usr/share/jitsi-videobridge:/bin/bash
jicofo:x:996:1001::/usr/share/jicofo:/bin/bash
prosody:x:111:115:Prosody XMPP Server:/var/lib/prosody:/usr/sbin/nologin
turnserver:x:112:116:turnserver daemon:/:/bin/false


## Groupes


```text
$ getent group | grep -Ei "jitsi|prosody|jicofo|turn" || true
```
jitsi:x:1001:
prosody:x:115:
turnserver:x:116:


## Home directories


```text
$ for u in jitsi jicofo prosody turnserver; do getent passwd "$u" 2>/dev/null; done
```
jicofo:x:996:1001::/usr/share/jicofo:/bin/bash
prosody:x:111:115:Prosody XMPP Server:/var/lib/prosody:/usr/sbin/nologin
turnserver:x:112:116:turnserver daemon:/:/bin/false



---

# 18. JAVA

**Date :** 2026-08-08 06:56:36 EDT


```text
$ java -version 2>&1 || true
```
openjdk version "21.0.11" 2026-04-21
OpenJDK Runtime Environment (build 21.0.11+10-1-deb13u2-Debian)
OpenJDK 64-Bit Server VM (build 21.0.11+10-1-deb13u2-Debian, mixed mode, sharing)


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
ii  jitsi-meet                                          2.0.11146-1                          all          WebRTC JavaScript video conferences
ii  jitsi-meet-web                                      1.0.9365-1                           all          WebRTC JavaScript video conferences
ii  libduktape207:amd64                                 2.7.0-2+b2                           amd64        embeddable Javascript engine, library
ii  libjavascriptcoregtk-4.1-0:amd64                    2.52.5-1~deb13u1                     amd64        JavaScript engine library from WebKitGTK
ii  libjs-jquery                                        3.6.1+dfsg+~3.5.14-1                 all          JavaScript library for dynamic web applications
ii  libjs-underscore                                    1.13.4~dfsg+~1.11.4-3                all          JavaScript's functional programming helper library
ii  openjdk-17-jre-headless                             17.999                               all          Fake openjdk-17 satisfied by openjdk-21
ii  openjdk-21-jre-headless:amd64                       21.0.11+10-1~deb13u2                 amd64        OpenJDK Java runtime, using Hotspot JIT (headless)



---

# 19. NODE.JS

**Date :** 2026-08-08 06:56:36 EDT


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

**Date :** 2026-08-08 06:56:36 EDT


```text
$ lua -v 2>&1 || true
```
Lua 5.4.7  Copyright (C) 1994-2024 Lua.org, PUC-Rio


```text
$ dpkg -l 2>/dev/null | grep -Ei "lua|prosody" || true
```
ii  jitsi-meet-prosody                                  1.0.9365-1                           all          Prosody configuration for Jitsi Meet
ii  liblua5.2-0:amd64                                   5.2.4-3+b3                           amd64        Shared library for the Lua interpreter version 5.2
ii  liblua5.4-0:amd64                                   5.4.7-1+b2                           amd64        Shared library for the Lua interpreter version 5.4
ii  lua-basexx                                          0.4.1-jitsi1                         all          baseXX encoding/decoding library for Lua
ii  lua-bit32:amd64                                     5.3.0-6                              amd64        Backport of the Lua 5.2 bit32 library to Lua 5.1
ii  lua-bitop:amd64                                     1.0.2-7+b2                           amd64        fast bit manipulation library for the Lua language
ii  lua-cjson:amd64                                     2.1.0.10-jitsi1                      amd64        JSON parser/encoder for Lua
ii  lua-event:amd64                                     0.4.6-2+b3                           amd64        asynchronous event notification library for Lua
ii  lua-expat:amd64                                     1.5.2-1+b1                           amd64        libexpat bindings for the Lua language
ii  lua-filesystem:amd64                                1.8.0-3+b2                           amd64        luafilesystem library for the Lua language
ii  lua-inspect                                         3.1.1-2                              all          Lua table visualizer, ideal for debugging
ii  lua-luaossl:amd64                                   20220711-2+b1                        amd64        OpenSSL bindings for Lua
ii  lua-posix:amd64                                     36.3-1                               amd64        posix library for the Lua language
ii  lua-readline:amd64                                  3.3-3+b3                             amd64        readline library for the Lua language
ii  lua-sec:amd64                                       1.3.2-2+b2                           amd64        SSL socket library for the Lua language
ii  lua-socket:amd64                                    3.1.0-1+b2                           amd64        TCP/UDP socket library for the Lua language
ii  lua-unbound:amd64                                   1.0.0-2+b2                           amd64        Unbound bindings for the Lua language
ii  lua5.4                                              5.4.7-1+b2                           amd64        Simple, extensible, embeddable programming language
ii  prosody                                             13.0.1-1+deb131u                     amd64        Lightweight Jabber/XMPP server


```text
$ find /usr/lib /usr/share -type f 2>/dev/null | grep -Ei "/lua/|prosody" | head -1000 || true
```
/usr/lib/prosody/net/dns.lua
/usr/lib/prosody/net/server.lua
/usr/lib/prosody/net/adns.lua
/usr/lib/prosody/net/http/parser.lua
/usr/lib/prosody/net/http/server.lua
/usr/lib/prosody/net/http/errors.lua
/usr/lib/prosody/net/http/files.lua
/usr/lib/prosody/net/http/codes.lua
/usr/lib/prosody/net/server_epoll.lua
/usr/lib/prosody/net/server_event.lua
/usr/lib/prosody/net/server_select.lua
/usr/lib/prosody/net/connect.lua
/usr/lib/prosody/net/stun.lua
/usr/lib/prosody/net/tls_luasec.lua
/usr/lib/prosody/net/cqueues.lua
/usr/lib/prosody/net/unbound.lua
/usr/lib/prosody/net/websocket/frames.lua
/usr/lib/prosody/net/websocket.lua
/usr/lib/prosody/net/resolvers/service.lua
/usr/lib/prosody/net/resolvers/basic.lua
/usr/lib/prosody/net/resolvers/chain.lua
/usr/lib/prosody/net/resolvers/manual.lua
/usr/lib/prosody/net/http.lua
/usr/lib/prosody/core/moduleapi.lua
/usr/lib/prosody/core/hostmanager.lua
/usr/lib/prosody/core/storagemanager.lua
/usr/lib/prosody/core/modulemanager.lua
/usr/lib/prosody/core/loggingmanager.lua
/usr/lib/prosody/core/stanza_router.lua
/usr/lib/prosody/core/portmanager.lua
/usr/lib/prosody/core/rostermanager.lua
/usr/lib/prosody/core/statsmanager.lua
/usr/lib/prosody/core/sessionmanager.lua
/usr/lib/prosody/core/features.lua
/usr/lib/prosody/core/s2smanager.lua
/usr/lib/prosody/core/configmanager.lua
/usr/lib/prosody/core/certmanager.lua
/usr/lib/prosody/core/usermanager.lua
/usr/lib/prosody/modules/mod_vcard.lua
/usr/lib/prosody/modules/mod_muc_mam.lua
/usr/lib/prosody/modules/mod_admin_adhoc.lua
/usr/lib/prosody/modules/mod_uptime.lua
/usr/lib/prosody/modules/mod_http.lua
/usr/lib/prosody/modules/mod_csi_simple.lua
/usr/lib/prosody/modules/mod_http_files.lua
/usr/lib/prosody/modules/mod_http_altconnect.lua
/usr/lib/prosody/modules/mod_storage_xep0227.lua
/usr/lib/prosody/modules/mod_vcard4.lua
/usr/lib/prosody/modules/mod_account_activity.lua
/usr/lib/prosody/modules/mod_flags.lua
/usr/lib/prosody/modules/mod_dialback.lua
/usr/lib/prosody/modules/mod_version.lua
/usr/lib/prosody/modules/mod_announce.lua
/usr/lib/prosody/modules/mod_net_multiplex.lua
/usr/lib/prosody/modules/mod_blocklist.lua
/usr/lib/prosody/modules/mod_time.lua
/usr/lib/prosody/modules/mod_tls.lua
/usr/lib/prosody/modules/mod_saslauth.lua
/usr/lib/prosody/modules/mod_proxy65.lua
/usr/lib/prosody/modules/mod_tokenauth.lua
/usr/lib/prosody/modules/mod_admin_socket.lua
/usr/lib/prosody/modules/mod_storage_memory.lua
/usr/lib/prosody/modules/mod_bosh.lua
/usr/lib/prosody/modules/mod_roster.lua
/usr/lib/prosody/modules/muc/hidden.lib.lua
/usr/lib/prosody/modules/muc/subject.lib.lua
/usr/lib/prosody/modules/muc/name.lib.lua
/usr/lib/prosody/modules/muc/whois.lib.lua
/usr/lib/prosody/modules/muc/history.lib.lua
/usr/lib/prosody/modules/muc/mod_muc.lua
/usr/lib/prosody/modules/muc/hats.lib.lua
/usr/lib/prosody/modules/muc/config_form_sections.lib.lua
/usr/lib/prosody/modules/muc/occupant_id.lib.lua
/usr/lib/prosody/modules/muc/moderated.lib.lua
/usr/lib/prosody/modules/muc/persistent.lib.lua
/usr/lib/prosody/modules/muc/language.lib.lua
/usr/lib/prosody/modules/muc/presence_broadcast.lib.lua
/usr/lib/prosody/modules/muc/request.lib.lua
/usr/lib/prosody/modules/muc/password.lib.lua
/usr/lib/prosody/modules/muc/vcard.lib.lua
/usr/lib/prosody/modules/muc/members_only.lib.lua
/usr/lib/prosody/modules/muc/description.lib.lua
/usr/lib/prosody/modules/muc/util.lib.lua
/usr/lib/prosody/modules/muc/lock.lib.lua
/usr/lib/prosody/modules/muc/register.lib.lua
/usr/lib/prosody/modules/muc/occupant.lib.lua
/usr/lib/prosody/modules/muc/restrict_pm.lib.lua
/usr/lib/prosody/modules/muc/muc.lib.lua
/usr/lib/prosody/modules/mod_auth_anonymous.lua
/usr/lib/prosody/modules/mod_authz_internal.lua
/usr/lib/prosody/modules/mod_carbons.lua
/usr/lib/prosody/modules/mod_auth_insecure.lua
/usr/lib/prosody/modules/mod_mimicking.lua
/usr/lib/prosody/modules/mod_groups.lua
/usr/lib/prosody/modules/mod_s2s_auth_certs.lua
/usr/lib/prosody/modules/mod_smacks.lua
/usr/lib/prosody/modules/mod_cron.lua
/usr/lib/prosody/modules/mod_unknown.lua
/usr/lib/prosody/modules/mod_s2s.lua
/usr/lib/prosody/modules/mod_http_errors.lua
/usr/lib/prosody/modules/mod_windows.lua
/usr/lib/prosody/modules/mod_server_contact_info.lua
/usr/lib/prosody/modules/mod_storage_sql.lua
/usr/lib/prosody/modules/mod_component.lua
/usr/lib/prosody/modules/mod_turn_external.lua
/usr/lib/prosody/modules/mod_storage_none.lua
/usr/lib/prosody/modules/mod_pep.lua
/usr/lib/prosody/modules/mod_vcard_legacy.lua
/usr/lib/prosody/modules/mod_lastactivity.lua
/usr/lib/prosody/modules/mod_auth_internal_plain.lua
/usr/lib/prosody/modules/mod_debug_reset.lua
/usr/lib/prosody/modules/mod_storage_internal.lua
/usr/lib/prosody/modules/mod_scansion_record.lua
/usr/lib/prosody/modules/mod_disco.lua
/usr/lib/prosody/modules/mod_invites.lua
/usr/lib/prosody/modules/mod_s2s_bidi.lua
/usr/lib/prosody/modules/mod_s2s_auth_dane_in.lua
/usr/lib/prosody/modules/mod_http_file_share.lua
/usr/lib/prosody/modules/mod_auth_ldap.lua
/usr/lib/prosody/modules/mod_ping.lua
/usr/lib/prosody/modules/mod_cloud_notify.lua
/usr/lib/prosody/modules/mod_http_openmetrics.lua
/usr/lib/prosody/modules/mod_iq.lua
/usr/lib/prosody/modules/mod_message.lua
/usr/lib/prosody/modules/mod_register.lua
/usr/lib/prosody/modules/mod_legacyauth.lua
/usr/lib/prosody/modules/mod_pep_simple.lua
/usr/lib/prosody/modules/mod_invites_adhoc.lua
/usr/lib/prosody/modules/mod_stanza_debug.lua
/usr/lib/prosody/modules/mod_welcome.lua
/usr/lib/prosody/modules/mod_register_ibr.lua
/usr/lib/prosody/modules/mod_server_info.lua
/usr/lib/prosody/modules/mod_muc_unique.lua
/usr/lib/prosody/modules/adhoc/adhoc.lib.lua
/usr/lib/prosody/modules/adhoc/mod_adhoc.lua
/usr/lib/prosody/modules/mod_pubsub/pubsub.lib.lua
/usr/lib/prosody/modules/mod_pubsub/commands.lib.lua
/usr/lib/prosody/modules/mod_pubsub/mod_pubsub.lua
/usr/lib/prosody/modules/mod_c2s.lua
/usr/lib/prosody/modules/mod_motd.lua
/usr/lib/prosody/modules/mod_websocket.lua
/usr/lib/prosody/modules/mod_debug_stanzas/watcher.lib.lua
/usr/lib/prosody/modules/mod_watchregistrations.lua
/usr/lib/prosody/modules/mod_user_account_management.lua
/usr/lib/prosody/modules/mod_admin_telnet.lua
/usr/lib/prosody/modules/mod_posix.lua
/usr/lib/prosody/modules/mod_offline.lua
/usr/lib/prosody/modules/mod_admin_shell.lua
/usr/lib/prosody/modules/mod_auth_internal_hashed.lua
/usr/lib/prosody/modules/mod_private.lua
/usr/lib/prosody/modules/mod_tombstones.lua
/usr/lib/prosody/modules/mod_bookmarks.lua
/usr/lib/prosody/modules/mod_pep_plus.lua
/usr/lib/prosody/modules/mod_external_services.lua
/usr/lib/prosody/modules/mod_limits.lua
/usr/lib/prosody/modules/mod_csi.lua
/usr/lib/prosody/modules/mod_presence.lua
/usr/lib/prosody/modules/mod_invites_register.lua
/usr/lib/prosody/modules/mod_debug_sql.lua
/usr/lib/prosody/modules/mod_mam/mamprefs.lib.lua
/usr/lib/prosody/modules/mod_mam/mamprefsxml.lib.lua
/usr/lib/prosody/modules/mod_mam/mod_mam.lua
/usr/lib/prosody/modules/mod_register_limits.lua
/usr/lib/prosody/prosody.version
/usr/lib/prosody/util/dataforms.lua
/usr/lib/prosody/util/timer.lua
/usr/lib/prosody/util/rsm.lua
/usr/lib/prosody/util/xtemplate.lua
/usr/lib/prosody/util/stanza.lua
/usr/lib/prosody/util/template.lua
/usr/lib/prosody/util/openmetrics.lua
/usr/lib/prosody/util/openssl.lua
/usr/lib/prosody/util/jsonpointer.lua
/usr/lib/prosody/util/dns.lua
/usr/lib/prosody/util/array.lua
/usr/lib/prosody/util/statistics.lua
/usr/lib/prosody/util/roles.lua
/usr/lib/prosody/util/gc.lua
/usr/lib/prosody/util/signal.so
/usr/lib/prosody/util/paseto.lua
/usr/lib/prosody/util/sql.lua
/usr/lib/prosody/util/envload.lua
/usr/lib/prosody/util/datamapper.lua
/usr/lib/prosody/util/smqueue.lua
/usr/lib/prosody/util/iterators.lua
/usr/lib/prosody/util/paths.lua
/usr/lib/prosody/util/events.lua
/usr/lib/prosody/util/sslconfig.lua
/usr/lib/prosody/util/poll.so
/usr/lib/prosody/util/mathcompat.lua
/usr/lib/prosody/util/sqlite3.lua
/usr/lib/prosody/util/net.so
/usr/lib/prosody/util/hashring.lua
/usr/lib/prosody/util/human/io.lua
/usr/lib/prosody/util/human/units.lua
/usr/lib/prosody/util/id.lua
/usr/lib/prosody/util/throttle.lua
/usr/lib/prosody/util/argparse.lua
/usr/lib/prosody/util/promise.lua
/usr/lib/prosody/util/bit53.lua
/usr/lib/prosody/util/format.lua
/usr/lib/prosody/util/debug.lua
/usr/lib/prosody/util/bitcompat.lua
/usr/lib/prosody/util/session.lua
/usr/lib/prosody/util/table.so
/usr/lib/prosody/util/dnsregistry.lua
/usr/lib/prosody/util/dbuffer.lua
/usr/lib/prosody/util/hex.lua
/usr/lib/prosody/util/async.lua
/usr/lib/prosody/util/pluginloader.lua
/usr/lib/prosody/util/time.so
/usr/lib/prosody/util/xml.lua
/usr/lib/prosody/util/queue.lua
/usr/lib/prosody/util/startup.lua
/usr/lib/prosody/util/hashes.so
/usr/lib/prosody/util/xpcall.lua
/usr/lib/prosody/util/set.lua
/usr/lib/prosody/util/caps.lua
/usr/lib/prosody/util/prosodyctl.lua
/usr/lib/prosody/util/multitable.lua
/usr/lib/prosody/util/crypto.so
/usr/lib/prosody/util/compat.so
/usr/lib/prosody/util/presence.lua
/usr/lib/prosody/util/ringbuffer.so
/usr/lib/prosody/util/erlparse.lua
/usr/lib/prosody/util/interpolation.lua
/usr/lib/prosody/util/logger.lua
/usr/lib/prosody/util/serialization.lua
/usr/lib/prosody/util/xmppstream.lua
/usr/lib/prosody/util/x509.lua
/usr/lib/prosody/util/sasl/external.lua
/usr/lib/prosody/util/sasl/oauthbearer.lua
/usr/lib/prosody/util/sasl/anonymous.lua
/usr/lib/prosody/util/sasl/plain.lua
/usr/lib/prosody/util/sasl/scram.lua
/usr/lib/prosody/util/watchdog.lua
/usr/lib/prosody/util/pposix.so
/usr/lib/prosody/util/random.lua
/usr/lib/prosody/util/json.lua
/usr/lib/prosody/util/mercurial.lua
/usr/lib/prosody/util/jsonschema.lua
/usr/lib/prosody/util/fsm.lua
/usr/lib/prosody/util/jwt.lua
/usr/lib/prosody/util/hmac.lua
/usr/lib/prosody/util/import.lua
/usr/lib/prosody/util/cache.lua
/usr/lib/prosody/util/adminstream.lua
/usr/lib/prosody/util/jid.lua
/usr/lib/prosody/util/error.lua
/usr/lib/prosody/util/indexedbheap.lua
/usr/lib/prosody/util/prosodyctl/cert.lua
/usr/lib/prosody/util/prosodyctl/shell.lua
/usr/lib/prosody/util/prosodyctl/check.lua
/usr/lib/prosody/util/termcolours.lua
/usr/lib/prosody/util/adhoc.lua
/usr/lib/prosody/util/filters.lua
/usr/lib/prosody/util/pubsub.lua
/usr/lib/prosody/util/helpers.lua
/usr/lib/prosody/util/statsd.lua
/usr/lib/prosody/util/dependencies.lua
/usr/lib/prosody/util/sasl.lua
/usr/lib/prosody/util/uuid.lua
/usr/lib/prosody/util/datetime.lua
/usr/lib/prosody/util/encodings.so
/usr/lib/prosody/util/datamanager.lua
/usr/lib/prosody/util/struct.so
/usr/lib/prosody/util/ip.lua
/usr/lib/prosody/util/strbitop.so
/usr/lib/prosody/util/http.lua
/usr/lib/prosody/loader.lua
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
/usr/lib/systemd/system/prosody.service
/usr/share/lua/5.1/openssl.lua
/usr/share/lua/5.1/posix/_base.lua
/usr/share/lua/5.1/posix/init.lua
/usr/share/lua/5.1/posix/util.lua
/usr/share/lua/5.1/posix/deprecated.lua
/usr/share/lua/5.1/posix/_bitwise.lua
/usr/share/lua/5.1/posix/sys.lua
/usr/share/lua/5.1/posix/compat.lua
/usr/share/lua/5.1/posix/_strict.lua
/usr/share/lua/5.1/posix/version.lua
/usr/share/lua/5.1/openssl/x509/store.lua
/usr/share/lua/5.1/openssl/x509/verify_param.lua
/usr/share/lua/5.1/openssl/x509/name.lua
/usr/share/lua/5.1/openssl/x509/extension.lua
/usr/share/lua/5.1/openssl/x509/csr.lua
/usr/share/lua/5.1/openssl/x509/altname.lua
/usr/share/lua/5.1/openssl/x509/chain.lua
/usr/share/lua/5.1/openssl/x509/crl.lua
/usr/share/lua/5.1/openssl/bignum.lua
/usr/share/lua/5.1/openssl/des.lua
/usr/share/lua/5.1/openssl/auxlib.lua
/usr/share/lua/5.1/openssl/kdf.lua
/usr/share/lua/5.1/openssl/pkey.lua
/usr/share/lua/5.1/openssl/cipher.lua
/usr/share/lua/5.1/openssl/digest.lua
/usr/share/lua/5.1/openssl/ssl/context.lua
/usr/share/lua/5.1/openssl/pkcs12.lua
/usr/share/lua/5.1/openssl/ssl.lua
/usr/share/lua/5.1/openssl/pubkey.lua
/usr/share/lua/5.1/openssl/x509.lua
/usr/share/lua/5.1/openssl/hmac.lua
/usr/share/lua/5.1/openssl/rand.lua
/usr/share/lua/5.1/openssl/ocsp/basic.lua
/usr/share/lua/5.1/openssl/ocsp/response.lua
/usr/share/lua/5.1/cjson/util.lua
/usr/share/lua/5.1/ltn12.lua
/usr/share/lua/5.1/luaevent.lua
/usr/share/lua/5.1/socket.lua
/usr/share/lua/5.1/readline.lua
/usr/share/lua/5.1/ssl/https.lua
/usr/share/lua/5.1/ssl/options.lua
/usr/share/lua/5.1/ssl.lua
/usr/share/lua/5.1/socket/mbox.lua
/usr/share/lua/5.1/socket/headers.lua
/usr/share/lua/5.1/socket/ftp.lua
/usr/share/lua/5.1/socket/smtp.lua
/usr/share/lua/5.1/socket/tp.lua
/usr/share/lua/5.1/socket/url.lua
/usr/share/lua/5.1/socket/http.lua
/usr/share/lua/5.1/mime.lua
/usr/share/lua/5.1/basexx.lua
/usr/share/lua/5.1/inspect.lua
/usr/share/lua/5.1/lxp/totable.lua
/usr/share/lua/5.1/lxp/threat.lua
/usr/share/lua/5.1/lxp/lom.lua
/usr/share/man/man1/prosodyctl.1.gz
/usr/share/man/man8/prosody-migrator.8.gz
/usr/share/man/man8/ejabberd2prosody.8.gz
/usr/share/man/man8/prosody.8.gz
/usr/share/jitsi-meet-prosody/jaas.cfg.lua
/usr/share/jitsi-meet-prosody/prosody.cfg.lua-jvb.example
/usr/share/lintian/overrides/prosody
/usr/share/doc/prosody/AUTHORS
/usr/share/doc/prosody/README
/usr/share/doc/prosody/changelog.Debian.gz
/usr/share/doc/prosody/copyright
/usr/share/doc/prosody/doc/roster_format.txt
/usr/share/doc/prosody/doc/names.txt
/usr/share/doc/prosody/doc/session.txt
/usr/share/doc/prosody/doc/net.server.lua.gz
/usr/share/doc/prosody/doc/hgrc.ini
/usr/share/doc/prosody/doc/stanza_routing.txt
/usr/share/doc/prosody/doc/coding_style.md.gz
/usr/share/doc/prosody/doc/stanza.txt
/usr/share/doc/prosody/doc/hgrc-email.ini
/usr/share/doc/prosody/doc/doap.xml.gz
/usr/share/doc/prosody/HACKERS
/usr/share/doc/prosody/changelog.gz
/usr/share/doc/jitsi-meet-prosody/README
/usr/share/doc/jitsi-meet-prosody/changelog.Debian.gz
/usr/share/doc/jitsi-meet-prosody/README.Debian
/usr/share/doc/jitsi-meet-prosody/copyright
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
/usr/share/jitsi-meet/prosody-plugins/mod_measure_message_count.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jitsi_session.lua
/usr/share/jitsi-meet/prosody-plugins/luajwtjitsi.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_conference_duration.lua
/usr/share/jitsi-meet/prosody-plugins/mod_speakerstats_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_token_verification.lua
/usr/share/jitsi-meet/prosody-plugins/mod_test_observer_http.lua
/usr/share/jitsi-meet/prosody-plugins/mod_visitors.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_census.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_resource_validate.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_jitsi-anonymous.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_meeting_id.lua
/usr/share/jitsi-meet/prosody-plugins/mod_system_chat_message.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jiconop.lua
/usr/share/jitsi-meet/prosody-plugins/mod_turncredentials_http.lua
/usr/share/jitsi-meet/prosody-plugins/mod_features_identity.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_password_check.lua
/usr/share/jitsi-meet/prosody-plugins/mod_s2s_whitelist.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_flip.lua
/usr/share/jitsi-meet/prosody-plugins/mod_short_lived_token.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_webhook.lua
/usr/share/jitsi-meet/prosody-plugins/mod_limits_exception.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filter_messages.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filter_iq_jibri.lua
/usr/share/jitsi-meet/prosody-plugins/mod_secure_interfaces.lua
/usr/share/jitsi-meet/prosody-plugins/mod_certs_s2soutinjection.lua
/usr/share/jitsi-meet/prosody-plugins/mod_room_metadata_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_kick_participant.lua
/usr/share/jitsi-meet/prosody-plugins/mod_roster_command.patch
/usr/share/jitsi-meet/prosody-plugins/mod_muc_domain_mapper.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jibri_session.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filesharing_component.lua
/usr/share/jitsi-meet/prosody-plugins/muc_owner_allow_kick-0.12.patch
/usr/share/jitsi-meet/prosody-plugins/README.md
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/actions.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/marks.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/definitions.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/test.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/mod_firewall.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/conditions.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_debug_traceback.lua
/usr/share/jitsi-meet/prosody-plugins/mod_room_destroy.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_hide_all.lua
/usr/share/jitsi-meet/prosody-plugins/mod_test_observer.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_cleanup_backend_services.lua
/usr/share/jitsi-meet/prosody-plugins/mod_polls_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_roster_command.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_lobby_rooms.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_jitsi-shared-secret.lua
/usr/share/jitsi-meet/prosody-plugins/token/jwk.lib.lua
/usr/share/jitsi-meet/prosody-plugins/token/util.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_token.lua
/usr/share/jitsi-meet/prosody-plugins/mod_av_moderation_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_end_conference.lua
/usr/share/jitsi-meet/prosody-plugins/mod_reservations.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_size.lua
/usr/share/jitsi-meet/prosody-plugins/util.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_log_ringbuffer.lua
/usr/share/jitsi-meet/prosody-plugins/mod_visitors_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_wait_for_host.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jitsi_permissions.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_end_meeting.lua
/usr/share/jitsi-meet/prosody-plugins/mod_fmuc.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_breakout_rooms.lua
/usr/share/jitsi-meet/prosody-plugins/mod_rate_limit.lua
/usr/share/jitsi-meet/prosody-plugins/mod_measure_stanza_counts.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_filter_access.lua
/usr/share/jitsi-meet/prosody-plugins/mod_persistent_lobby.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_displayname.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_password_whitelist.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_allowners.lua
/usr/share/jitsi-meet/prosody-plugins/mod_audio_translation_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_token_affiliation.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filter_iq_rayo.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_rate_limit.lua
/usr/share/jitsi-meet/prosody-plugins/mod_presence_identity.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_jigasi_invite.lua
/usr/share/jitsi-meet/prosody-plugins/mod_s2sout_override.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_limit_messages.lua
/usr/share/jitsi-meet/prosody-plugins/stanza_router_no-log.patch
/usr/share/jitsi-meet/prosody-plugins/mod_muc_max_occupants.lua
/usr/share/jitsi-meet/prosody-plugins/mod_client_proxy.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_auth_ban.lua
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

**Date :** 2026-08-08 06:56:36 EDT


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
-A DOCKER -d 172.20.0.14/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8100 -j ACCEPT
-A DOCKER -d 172.20.0.4/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8011 -j ACCEPT
-A DOCKER -d 172.20.0.6/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8010 -j ACCEPT
-A DOCKER -d 172.20.0.8/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 9308 -j ACCEPT
-A DOCKER -d 172.20.0.13/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 9090 -j ACCEPT
-A DOCKER -d 172.20.0.11/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 3100 -j ACCEPT
-A DOCKER -d 172.20.0.10/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8002 -j ACCEPT
-A DOCKER -d 172.20.0.9/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 8090 -j ACCEPT
-A DOCKER -d 172.20.0.5/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 3000 -j ACCEPT
-A DOCKER -d 172.20.0.3/32 ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -p tcp -m tcp --dport 9092 -j ACCEPT
-A DOCKER ! -i br-c8ba5432ed86 -o br-c8ba5432ed86 -j DROP
-A DOCKER ! -i docker0 -o docker0 -j DROP
-A DOCKER-BRIDGE -o br-c8ba5432ed86 -j DOCKER
-A DOCKER-BRIDGE -o docker0 -j DOCKER
-A DOCKER-CT -o br-c8ba5432ed86 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A DOCKER-CT -o docker0 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A DOCKER-FORWARD -j DOCKER-CT
-A DOCKER-FORWARD -j DOCKER-INTERNAL
-A DOCKER-FORWARD -j DOCKER-BRIDGE
-A DOCKER-FORWARD -i br-c8ba5432ed86 -j ACCEPT
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
-A POSTROUTING -o br-c8ba5432ed86 -m addrtype --src-type LOCAL -j MASQUERADE
-A POSTROUTING -s 172.20.0.0/16 ! -o br-c8ba5432ed86 -j MASQUERADE
-A POSTROUTING -s 172.20.0.3/32 -d 172.20.0.3/32 -p tcp -m tcp --dport 9092 -j MASQUERADE
-A POSTROUTING -s 172.20.0.5/32 -d 172.20.0.5/32 -p tcp -m tcp --dport 3000 -j MASQUERADE
-A POSTROUTING -s 172.20.0.9/32 -d 172.20.0.9/32 -p tcp -m tcp --dport 8090 -j MASQUERADE
-A POSTROUTING -s 172.20.0.10/32 -d 172.20.0.10/32 -p tcp -m tcp --dport 8002 -j MASQUERADE
-A POSTROUTING -s 172.20.0.11/32 -d 172.20.0.11/32 -p tcp -m tcp --dport 3100 -j MASQUERADE
-A POSTROUTING -s 172.20.0.13/32 -d 172.20.0.13/32 -p tcp -m tcp --dport 9090 -j MASQUERADE
-A POSTROUTING -s 172.20.0.8/32 -d 172.20.0.8/32 -p tcp -m tcp --dport 9308 -j MASQUERADE
-A POSTROUTING -s 172.20.0.6/32 -d 172.20.0.6/32 -p tcp -m tcp --dport 8010 -j MASQUERADE
-A POSTROUTING -s 172.20.0.4/32 -d 172.20.0.4/32 -p tcp -m tcp --dport 8011 -j MASQUERADE
-A POSTROUTING -s 172.20.0.14/32 -d 172.20.0.14/32 -p tcp -m tcp --dport 8100 -j MASQUERADE
-A DOCKER -p tcp -m tcp --dport 9092 -j DNAT --to-destination 172.20.0.3:9092
-A DOCKER -p tcp -m tcp --dport 3000 -j DNAT --to-destination 172.20.0.5:3000
-A DOCKER -p tcp -m tcp --dport 8090 -j DNAT --to-destination 172.20.0.9:8090
-A DOCKER -p tcp -m tcp --dport 8002 -j DNAT --to-destination 172.20.0.10:8002
-A DOCKER -p tcp -m tcp --dport 3100 -j DNAT --to-destination 172.20.0.11:3100
-A DOCKER -p tcp -m tcp --dport 9091 -j DNAT --to-destination 172.20.0.13:9090
-A DOCKER -p tcp -m tcp --dport 9308 -j DNAT --to-destination 172.20.0.8:9308
-A DOCKER -p tcp -m tcp --dport 8010 -j DNAT --to-destination 172.20.0.6:8010
-A DOCKER -p tcp -m tcp --dport 8011 -j DNAT --to-destination 172.20.0.4:8011
-A DOCKER -p tcp -m tcp --dport 8100 -j DNAT --to-destination 172.20.0.14:8100


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
		iifname "lo" counter packets 88042 bytes 51034798 accept
		ct state related,established counter packets 19676 bytes 7183797 accept
		ct state invalid counter packets 0 bytes 0 jump ufw-logging-deny
		ct state invalid counter packets 0 bytes 0 drop
		ip protocol icmp icmp type destination-unreachable counter packets 0 bytes 0 accept
		ip protocol icmp icmp type time-exceeded counter packets 0 bytes 0 accept
		ip protocol icmp icmp type parameter-problem counter packets 0 bytes 0 accept
		ip protocol icmp icmp type echo-request counter packets 0 bytes 0 accept
		udp sport 67 udp dport 68 counter packets 10 bytes 3140 accept
		counter packets 5372 bytes 1022202 jump ufw-not-local
		ip daddr 224.0.0.251 udp dport 5353 counter packets 2893 bytes 507143 accept
		ip daddr 239.255.255.250 udp dport 1900 counter packets 0 bytes 0 accept
		counter packets 2479 bytes 515059 jump ufw-user-input
	}

	chain ufw-before-output {
		oifname "lo" counter packets 92556 bytes 51442873 accept
		ct state related,established counter packets 18677 bytes 2585543 accept
		counter packets 815 bytes 68067 jump ufw-user-output
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
		udp dport 137 counter packets 14 bytes 1092 jump ufw-skip-to-policy-input
		udp dport 138 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		tcp dport 139 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		tcp dport 445 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		udp dport 67 counter packets 31 bytes 10165 jump ufw-skip-to-policy-input
		udp dport 68 counter packets 0 bytes 0 jump ufw-skip-to-policy-input
		fib daddr type broadcast counter packets 2412 bytes 498358 jump ufw-skip-to-policy-input
	}

	chain ufw-after-output {
	}

	chain ufw-after-forward {
	}

	chain ufw-after-logging-input {
		limit rate 3/minute burst 10 packets counter packets 15 bytes 5024 log prefix "[UFW BLOCK] "
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
		ip protocol tcp ct state new counter packets 110 bytes 6600 accept
		ip protocol udp ct state new counter packets 699 bytes 61195 accept
	}

	chain ufw-track-forward {
	}

	chain INPUT {
		type filter hook input priority filter; policy drop;
		counter packets 113100 bytes 59243937 jump ufw-before-logging-input
		counter packets 113100 bytes 59243937 jump ufw-before-input
		counter packets 2478 bytes 514999 jump ufw-after-input
		counter packets 21 bytes 5384 jump ufw-after-logging-input
		counter packets 21 bytes 5384 jump ufw-reject-input
		counter packets 21 bytes 5384 jump ufw-track-input
	}

	chain OUTPUT {
		type filter hook output priority filter; policy accept;
		counter packets 112048 bytes 54096483 jump ufw-before-logging-output
		counter packets 112048 bytes 54096483 jump ufw-before-output
		counter packets 815 bytes 68067 jump ufw-after-output
		counter packets 815 bytes 68067 jump ufw-after-logging-output
		counter packets 815 bytes 68067 jump ufw-reject-output
		counter packets 815 bytes 68067 jump ufw-track-output
	}

	chain FORWARD {
		type filter hook forward priority filter; policy drop;
		counter packets 721477 bytes 188795887 jump DOCKER-USER
		counter packets 721477 bytes 188795887 jump DOCKER-FORWARD
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
		counter packets 2457 bytes 509615 drop
	}

	chain ufw-skip-to-policy-output {
		counter packets 0 bytes 0 accept
	}

	chain ufw-skip-to-policy-forward {
		counter packets 0 bytes 0 drop
	}

	chain ufw-not-local {
		fib daddr type local counter packets 35 bytes 6504 return
		fib daddr type multicast counter packets 2894 bytes 507175 return
		fib daddr type broadcast counter packets 2443 bytes 508523 return
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
		ip daddr 172.20.0.14 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8100 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.4 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8011 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.6 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8010 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.8 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 9308 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.13 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 9090 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.11 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 3100 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.10 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8002 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.9 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 8090 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.5 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 3000 counter packets 0 bytes 0 accept
		ip daddr 172.20.0.3 iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" tcp dport 9092 counter packets 0 bytes 0 accept
		iifname != "br-c8ba5432ed86" oifname "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		iifname != "docker0" oifname "docker0" counter packets 0 bytes 0 drop
	}

	chain DOCKER-FORWARD {
		counter packets 721477 bytes 188795887 jump DOCKER-CT
		counter packets 29563 bytes 37356739 jump DOCKER-INTERNAL
		counter packets 29563 bytes 37356739 jump DOCKER-BRIDGE
		iifname "br-c8ba5432ed86" counter packets 29563 bytes 37356739 accept
		iifname "docker0" counter packets 0 bytes 0 accept
	}

	chain DOCKER-BRIDGE {
		oifname "br-c8ba5432ed86" counter packets 2292 bytes 137520 jump DOCKER
		oifname "docker0" counter packets 0 bytes 0 jump DOCKER
	}

	chain DOCKER-CT {
		oifname "br-c8ba5432ed86" ct state related,established counter packets 691914 bytes 151439148 accept
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
		iifname "lo" counter packets 26 bytes 1832 accept
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
		meta l4proto ipv6-icmp icmpv6 type nd-router-advert ip6 hoplimit 255 counter packets 83 bytes 7440 accept
		meta l4proto ipv6-icmp icmpv6 type nd-neighbor-solicit ip6 hoplimit 255 counter packets 2194 bytes 157968 accept
		meta l4proto ipv6-icmp icmpv6 type nd-neighbor-advert ip6 hoplimit 255 counter packets 298 bytes 19072 accept
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
		ip6 daddr ff02::fb udp dport 5353 counter packets 3303 bytes 606368 accept
		ip6 daddr ff02::f udp dport 1900 counter packets 0 bytes 0 accept
		counter packets 0 bytes 0 jump ufw6-user-input
	}

	chain ufw6-before-output {
		oifname "lo" counter packets 26 bytes 1832 accept
		rt type 0 counter packets 0 bytes 0 drop
		ct state related,established counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type destination-unreachable counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type packet-too-big counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type time-exceeded counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type parameter-problem counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type echo-request counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type echo-reply counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp icmpv6 type nd-router-solicit ip6 hoplimit 255 counter packets 207 bytes 11544 accept
		meta l4proto ipv6-icmp icmpv6 type nd-neighbor-advert ip6 hoplimit 255 counter packets 2194 bytes 140456 accept
		meta l4proto ipv6-icmp icmpv6 type nd-neighbor-solicit ip6 hoplimit 255 counter packets 336 bytes 24192 accept
		meta l4proto ipv6-icmp icmpv6 type nd-router-advert ip6 hoplimit 255 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp icmpv6 type mld-listener-query counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp icmpv6 type mld-listener-report counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp icmpv6 type mld-listener-done counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" counter packets 98 bytes 8128 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 255 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 1 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 1 counter packets 0 bytes 0 accept
		ip6 saddr fe80::/10 meta l4proto ipv6-icmp xt match "icmp6" ip6 hoplimit 1 counter packets 0 bytes 0 accept
		counter packets 671 bytes 72578 jump ufw6-user-output
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
		meta l4proto udp ct state new counter packets 598 bytes 66890 accept
	}

	chain ufw6-track-forward {
	}

	chain INPUT {
		type filter hook input priority filter; policy drop;
		counter packets 5904 bytes 792680 jump ufw6-before-logging-input
		counter packets 5904 bytes 792680 jump ufw6-before-input
		counter packets 0 bytes 0 jump ufw6-after-input
		counter packets 0 bytes 0 jump ufw6-after-logging-input
		counter packets 0 bytes 0 jump ufw6-reject-input
		counter packets 0 bytes 0 jump ufw6-track-input
	}

	chain OUTPUT {
		type filter hook output priority filter; policy accept;
		counter packets 3532 bytes 258730 jump ufw6-before-logging-output
		counter packets 3532 bytes 258730 jump ufw6-before-output
		counter packets 671 bytes 72578 jump ufw6-after-output
		counter packets 671 bytes 72578 jump ufw6-after-logging-output
		counter packets 671 bytes 72578 jump ufw6-reject-output
		counter packets 671 bytes 72578 jump ufw6-track-output
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
		tcp dport 9092 counter packets 0 bytes 0 dnat to 172.20.0.3:9092
		tcp dport 3000 counter packets 1 bytes 60 dnat to 172.20.0.5:3000
		tcp dport 8090 counter packets 0 bytes 0 dnat to 172.20.0.9:8090
		tcp dport 8002 counter packets 0 bytes 0 dnat to 172.20.0.10:8002
		tcp dport 3100 counter packets 0 bytes 0 dnat to 172.20.0.11:3100
		tcp dport 9091 counter packets 0 bytes 0 dnat to 172.20.0.13:9090
		tcp dport 9308 counter packets 0 bytes 0 dnat to 172.20.0.8:9308
		tcp dport 8010 counter packets 7 bytes 420 dnat to 172.20.0.6:8010
		tcp dport 8011 counter packets 0 bytes 0 dnat to 172.20.0.4:8011
		tcp dport 8100 counter packets 9 bytes 540 dnat to 172.20.0.14:8100
	}

	chain PREROUTING {
		type nat hook prerouting priority dstnat; policy accept;
		fib daddr type local counter packets 35 bytes 6504 jump DOCKER
	}

	chain OUTPUT {
		type nat hook output priority dstnat; policy accept;
		fib daddr type local counter packets 95 bytes 7042 jump DOCKER
	}

	chain POSTROUTING {
		type nat hook postrouting priority srcnat; policy accept;
		oifname "docker0" fib saddr type local counter packets 21 bytes 1523 masquerade
		ip saddr 172.17.0.0/16 oifname != "docker0" counter packets 2 bytes 568 masquerade
		oifname "br-c8ba5432ed86" fib saddr type local counter packets 40 bytes 2706 masquerade
		ip saddr 172.20.0.0/16 oifname != "br-c8ba5432ed86" counter packets 1151 bytes 70900 masquerade
		ip saddr 172.20.0.3 ip daddr 172.20.0.3 tcp dport 9092 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.5 ip daddr 172.20.0.5 tcp dport 3000 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.9 ip daddr 172.20.0.9 tcp dport 8090 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.10 ip daddr 172.20.0.10 tcp dport 8002 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.11 ip daddr 172.20.0.11 tcp dport 3100 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.13 ip daddr 172.20.0.13 tcp dport 9090 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.8 ip daddr 172.20.0.8 tcp dport 9308 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.6 ip daddr 172.20.0.6 tcp dport 8010 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.4 ip daddr 172.20.0.4 tcp dport 8011 counter packets 0 bytes 0 masquerade
		ip saddr 172.20.0.14 ip daddr 172.20.0.14 tcp dport 8100 counter packets 0 bytes 0 masquerade
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
		fib daddr type local counter packets 12 bytes 960 jump DOCKER
	}
}
table ip raw {
	chain PREROUTING {
		type filter hook prerouting priority raw; policy accept;
		ip daddr 172.20.0.2 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.3 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.5 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.7 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.9 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.10 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.11 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.12 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.13 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.8 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.6 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.4 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
		ip daddr 172.20.0.14 iifname != "br-c8ba5432ed86" counter packets 0 bytes 0 drop
	}
}



---

# 22. CRON / TIMERS

**Date :** 2026-08-08 06:56:37 EDT


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
NEXT                             LEFT LAST                              PASSED UNIT                         ACTIVATES
Sat 2026-08-08 06:59:19 EDT  2min 42s Sat 2026-08-08 05:47:31 EDT  1h 9min ago fwupd-refresh.timer          fwupd-refresh.service
Sat 2026-08-08 07:31:56 EDT     35min Sat 2026-08-08 02:37:19 EDT 2h 18min ago anacron.timer                anacron.service
Sat 2026-08-08 09:48:56 EDT  2h 52min Fri 2026-08-07 09:03:34 EDT 3h 17min ago man-db.timer                 man-db.service
Sat 2026-08-08 16:54:54 EDT        9h Sat 2026-08-08 02:39:03 EDT 2h 16min ago apt-daily.timer              apt-daily.service
Sun 2026-08-09 00:00:00 EDT       17h Sat 2026-08-08 02:37:19 EDT 2h 18min ago dpkg-db-backup.timer         dpkg-db-backup.service
Sun 2026-08-09 00:59:38 EDT       18h Sat 2026-08-08 02:37:19 EDT 2h 18min ago logrotate.timer              logrotate.service
Sun 2026-08-09 02:37:28 EDT       19h Fri 2026-08-07 05:40:20 EDT 4h 19min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Sun 2026-08-09 03:10:30 EDT       20h Mon 2026-08-03 10:26:10 EDT            - e2scrub_all.timer            e2scrub_all.service
Sun 2026-08-09 06:48:31 EDT       23h Sat 2026-08-08 06:45:58 EDT    10min ago apt-daily-upgrade.timer      apt-daily-upgrade.service
Mon 2026-08-10 00:14:14 EDT 1 day 17h Mon 2026-08-03 10:33:03 EDT            - fstrim.timer                 fstrim.service

10 timers listed.



---

# 23. CERTBOT

**Date :** 2026-08-08 06:56:37 EDT


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

**Date :** 2026-08-08 06:56:37 EDT


```text
$ docker --version 2>/dev/null || true
```
Docker version 29.7.1, build e9452d6


```text
$ docker ps -a 2>/dev/null || true
```
CONTAINER ID   IMAGE                             COMMAND                  CREATED        STATUS                  PORTS                              NAMES
3932edd222d1   event-bridge-event-bridge         "uvicorn main:app --…"   26 hours ago   Up 25 hours             0.0.0.0:8100->8100/tcp             civitas-event-bridge
d92d616d2990   room-spawner-room-spawner         "uvicorn app.main:ap…"   26 hours ago   Up 26 hours             0.0.0.0:8011->8011/tcp             civitas-room-spawner
2cee96f0ba4c   room-config-room-config           "uvicorn app.main:ap…"   26 hours ago   Up 26 hours             0.0.0.0:8010->8010/tcp             civitas-room-config
16f8ba74b65a   peer-peer                         "uvicorn app.main:ap…"   4 days ago     Up 26 hours             0.0.0.0:8002->8002/tcp             civitas-peer
3a9798a8b909   postgres:16-alpine                "docker-entrypoint.s…"   4 days ago     Up 26 hours (healthy)   5432/tcp                           civitas-postgres
687556bee681   grafana/grafana:latest            "/run.sh"                4 days ago     Up 26 hours             0.0.0.0:3000->3000/tcp             civitas-grafana
b2e0767cd32b   prom/prometheus:latest            "/bin/prometheus --c…"   4 days ago     Up 26 hours             0.0.0.0:9091->9090/tcp             civitas-prometheus
c7db2210598d   grafana/loki:2.9.0                "/usr/bin/loki -conf…"   4 days ago     Up 26 hours             0.0.0.0:3100->3100/tcp             civitas-loki
459431144a5c   prom/node-exporter:latest         "/bin/node_exporter …"   4 days ago     Up 26 hours             9100/tcp                           civitas-node-exporter
622a0f470a23   grafana/promtail:2.9.0            "/usr/bin/promtail -…"   4 days ago     Up 26 hours                                                civitas-promtail
4eedbee991f0   danielqsj/kafka-exporter:latest   "/bin/kafka_exporter…"   4 days ago     Up 26 hours             0.0.0.0:9308->9308/tcp             civitas-kafka-exporter
ddc51b51c5aa   provectuslabs/kafka-ui:latest     "/bin/sh -c 'java --…"   4 days ago     Up 26 hours             8080/tcp, 0.0.0.0:8090->8090/tcp   civitas-kafka-ui
9e3c2133184a   confluentinc/cp-kafka:7.6.0       "/etc/confluent/dock…"   4 days ago     Up 26 hours (healthy)   0.0.0.0:9092->9092/tcp             civitas-kafka


```text
$ docker images 2>/dev/null || true
```
IMAGE                              ID             DISK USAGE   CONTENT SIZE   EXTRA
confluentinc/cp-kafka:7.6.0        d87a8d474634        806MB             0B   U    
danielqsj/kafka-exporter:latest    a3e635c3de94       27.5MB             0B   U    
event-bridge-event-bridge:latest   9442fc5ae0d1        173MB             0B   U    
grafana/grafana:latest             beafdfed0240        761MB             0B   U    
grafana/loki:2.9.0                 21abbe8487a0       74.8MB             0B   U    
grafana/promtail:2.9.0             e48aaa4dcb3b        198MB             0B   U    
peer-peer:latest                   86622084b479       1.46GB             0B   U    
postgres:16-alpine                 108b27c919e6        276MB             0B   U    
prom/node-exporter:latest          696e69e899e0       25.7MB             0B   U    
prom/prometheus:latest             5a2c7fe42427        390MB             0B   U    
provectuslabs/kafka-ui:latest      99307ab28a49        291MB             0B   U    
room-config-room-config:latest     f19f4ea966fb        208MB             0B   U    
room-spawner-room-spawner:latest   9187e5b5b12f        174MB             0B   U    


```text
$ docker compose version 2>/dev/null || true
```
Docker Compose version v5.4.0



---

# 25. DNS / HOSTNAME

**Date :** 2026-08-08 06:56:37 EDT


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
/etc/jitsi/meet/meet.civitas.local-config.js:3:        domain: 'meet.civitas.local',
/etc/jitsi/meet/meet.civitas.local-config.js:4:        muc: 'conference.meet.civitas.local',
/etc/jitsi/meet/meet.civitas.local-config.js:5:        focus: 'focus.meet.civitas.local',
/etc/jitsi/meet/meet.civitas.local-config.js:7:    bosh: '//meet.civitas.local/http-bind',
/etc/jitsi/meet/meet.civitas.local-config.js:8:    websocket: 'wss://meet.civitas.local/xmpp-websocket',
/etc/jitsi/meet/meet.civitas.local-config.js:12:            { urls: 'stun:meet.civitas.local:3478' },
/etc/jitsi/meet/meet.civitas.local-config.js:20:            'turn:meet.civitas.local:3478?transport=udp',
/etc/jitsi/meet/meet.civitas.local-config.js:21:            'turn:meet.civitas.local:3478?transport=tcp',
/etc/jitsi/meet/meet.civitas.local-config.js:22:            'turns:meet.civitas.local:5349?transport=tcp',
/etc/jitsi/jicofo/config:2:JAVA_SYS_PROPS="-Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=jicofo -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/jicofo/logging.properties"
/etc/jitsi/jicofo/logging.properties:4:# Handlers with XMPP debug enabled:
/etc/jitsi/jicofo/logging.properties:5:#handlers= java.util.logging.ConsoleHandler, org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler
/etc/jitsi/jicofo/logging.properties:11:java.util.logging.ConsoleHandler.formatter = org.jitsi.utils.logging2.JitsiLogFormatter
/etc/jitsi/jicofo/logging.properties:12:java.util.logging.ConsoleHandler.filter = org.jitsi.impl.protocol.xmpp.log.ExcludeXmppPackets
/etc/jitsi/jicofo/logging.properties:14:org.jitsi.utils.logging2.JitsiLogFormatter.programname=Jicofo
/etc/jitsi/jicofo/logging.properties:17:# To enable XMPP packets logging add XmppPacketsFileHandler to the handlers property
/etc/jitsi/jicofo/logging.properties:18:org.jitsi.impl.protocol.xmpp.log.PacketDebugger.level=ALL
/etc/jitsi/jicofo/logging.properties:19:org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.pattern=/var/log/jitsi/jicofo-xmpp.log
/etc/jitsi/jicofo/logging.properties:20:org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.append=true
/etc/jitsi/jicofo/logging.properties:21:org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.limit=200000000
/etc/jitsi/jicofo/logging.properties:22:org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.count=3
/etc/jitsi/jicofo/logging.properties:28:#org.jitsi.impl.protocol.xmpp.colibri.level=ALL
/etc/jitsi/jicofo/jicofo.conf:2:  xmpp: {
/etc/jitsi/jicofo/jicofo.conf:4:      client-proxy: "focus.meet.civitas.local"
/etc/jitsi/jicofo/jicofo.conf:5:      xmpp-domain: "meet.civitas.local"
/etc/jitsi/jicofo/jicofo.conf:6:      domain: "auth.meet.civitas.local"
/etc/jitsi/jicofo/jicofo.conf:12:      domain: "meet.civitas.local"
/etc/jitsi/jicofo/jicofo.conf:15:    trusted-domains: [ "recorder.meet.civitas.local" ]
/etc/jitsi/jicofo/jicofo.conf:18:    brewery-jid: "JvbBrewery@internal.auth.meet.civitas.local"
/etc/jitsi/videobridge/jvb.conf:9:        domain = "meet.civitas.local:443"
/etc/jitsi/videobridge/jvb.conf:12:    apis.xmpp-client.configs {
/etc/jitsi/videobridge/jvb.conf:15:            DOMAIN="auth.meet.civitas.local"
/etc/jitsi/videobridge/jvb.conf:18:            MUC_JIDS="jvbbrewery@internal.auth.meet.civitas.local"
/etc/jitsi/videobridge/jvb.conf:30:                addresses = ["meet-jit-si-turnrelay.jitsi.net:443"]
/etc/jitsi/videobridge/config:3:JAVA_SYS_PROPS="-Dconfig.file=/etc/jitsi/videobridge/jvb.conf -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=videobridge -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/videobridge/logging.properties"
/etc/jitsi/videobridge/logging.properties:5:java.util.logging.ConsoleHandler.formatter = org.jitsi.utils.logging2.JitsiLogFormatter
/etc/jitsi/videobridge/logging.properties:7:org.jitsi.utils.logging2.JitsiLogFormatter.programname=JVB
/etc/prosody/migrator.cfg.lua:35:		["conference.example.com"] = muc;
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:3:plugin_paths = { "/usr/share/jitsi-meet/prosody-plugins/" }
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:5:muc_mapper_domain_base = "meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:9:    { type = "stun", host = "meet.civitas.local", port = 3478 },
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:10:    { type = "turn", host = "meet.civitas.local", port = 3478, transport = "udp", secret = true, ttl = 86400, algorithm = "turn" },
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:11:    { type = "turns", host = "meet.civitas.local", port = 5349, transport = "tcp", secret = true, ttl = 86400, algorithm = "turn" }
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:19:    "focus@auth.meet.civitas.local",
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:20:    "jvb@auth.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:23:VirtualHost "meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:24:    authentication = "jitsi-anonymous"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:41:VirtualHost "auth.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:44:Component "conference.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:54:    admins = { "focus@auth.meet.civitas.local" }
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:58:Component "internal.auth.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:61:    admins = { "focus@auth.meet.civitas.local", "jvb@auth.meet.civitas.local" }
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:65:Component "focus.meet.civitas.local" "client_proxy"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:66:    target_address = "focus@auth.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:68:Component "speakerstats.meet.civitas.local" "speakerstats_component"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:69:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:71:Component "endconference.meet.civitas.local" "end_conference"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:72:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:74:Component "muc.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:77:Component "breakout.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:84:    admins = { "focus@auth.meet.civitas.local" }
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:88:Component "lobby.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:95:Component "metadata.meet.civitas.local" "room_metadata_component"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:96:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:98:Component "avmoderation.meet.civitas.local" "av_moderation_component"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:99:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:101:Component "polls.meet.civitas.local" "polls_component"
/etc/prosody/conf.avail/example.com.cfg.lua:20:-- Set up a MUC (multi-user chat) room server on conference.example.com:
/etc/prosody/conf.avail/example.com.cfg.lua:21:Component "conference.example.com" "muc"
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:2:unlimited_jids = { "focus@auth.meet.civitas.local", "jvb@auth.meet.civitas.local" }
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:6:Component "conference.meet.civitas.local" "muc"
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:19:Component "internal.auth.meet.civitas.local" "muc"
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:22:    admins = { "focus@auth.meet.civitas.local", "jvb@auth.meet.civitas.local" }
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:26:Component "polls.meet.civitas.local" "polls_component"
/etc/prosody/conf.avail/jaas.cfg.lua:1:-- Enables dial-in for Jitsi meet components customers
/etc/prosody/conf.avail/jaas.cfg.lua:2:VirtualHost "jigasi.meet.jitsi"
/etc/prosody/conf.avail/jaas.cfg.lua:9:    app_id = "jitsi";
/etc/prosody/conf.avail/jaas.cfg.lua:10:    asap_key_server = "https://jaas-public-keys.jitsi.net/jitsi-components/prod-8x8"
/etc/prosody/conf.avail/jaas.cfg.lua:12:    asap_accepted_audiences = { "jigasi.meet.civitas.local" }
/etc/prosody/prosody.cfg.lua:33:plugin_paths = { "/usr/local/lib/prosody/modules", "/usr/share/jitsi-meet/prosody-plugins/" }
/etc/prosody/prosody.cfg.lua:50:		"limits"; -- Enable bandwidth limiting for XMPP connections
/etc/prosody/prosody.cfg.lua:64:		"ping"; -- Replies to XMPP pings with pongs
/etc/prosody/prosody.cfg.lua:73:		"admin_adhoc"; -- Allows administration via an XMPP client that supports ad-hoc commands
/etc/prosody/prosody.cfg.lua:79:		"websocket"; -- XMPP over WebSockets
/etc/prosody/prosody.cfg.lua:187:-- Specify the address of the TURN service (you may use the same domain as XMPP)
/etc/prosody/prosody.cfg.lua:248:---Set up a MUC (multi-user chat) room server on conference.example.com:
/etc/prosody/prosody.cfg.lua:249:--Component "conference.example.com" "muc"
/etc/prosody/prosody.cfg.lua:259:-- bridges to non-XMPP networks and services. For more info



---

# 26. RÉSEAU

**Date :** 2026-08-08 06:56:37 EDT


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
       valid_lft 86077sec preferred_lft 86077sec
    inet6 fe80::a00:27ff:fe59:54fd/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
5: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 4e:1c:40:fa:71:34 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
6: br-c8ba5432ed86: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 76:3b:11:e4:56:38 brd ff:ff:ff:ff:ff:ff
    inet 172.20.0.1/16 brd 172.20.255.255 scope global br-c8ba5432ed86
       valid_lft forever preferred_lft forever
    inet6 fe80::743b:11ff:fee4:5638/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
7: vethc482531@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 56:b6:3f:d7:ef:1a brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::54b6:3fff:fed7:ef1a/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
8: veth43c9e99@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 26:97:54:ad:0d:ba brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::2497:54ff:fead:dba/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
10: veth272b590@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether ee:06:ef:59:f8:8a brd ff:ff:ff:ff:ff:ff link-netnsid 3
    inet6 fe80::ec06:efff:fe59:f88a/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
12: veth769ba64@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether da:5f:a9:dd:29:40 brd ff:ff:ff:ff:ff:ff link-netnsid 5
    inet6 fe80::d85f:a9ff:fedd:2940/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
14: vetha289142@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 3a:00:10:56:3a:fe brd ff:ff:ff:ff:ff:ff link-netnsid 7
    inet6 fe80::3800:10ff:fe56:3afe/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
15: veth88ecfbd@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether ca:29:ac:27:f5:62 brd ff:ff:ff:ff:ff:ff link-netnsid 8
    inet6 fe80::c829:acff:fe27:f562/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
16: veth8139db8@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 06:b7:6e:6c:27:21 brd ff:ff:ff:ff:ff:ff link-netnsid 9
    inet6 fe80::4b7:6eff:fe6c:2721/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
17: vethbf38ab7@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 4e:68:db:48:f7:6a brd ff:ff:ff:ff:ff:ff link-netnsid 10
    inet6 fe80::4c68:dbff:fe48:f76a/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
18: vetheb22e79@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether ee:d9:35:71:62:86 brd ff:ff:ff:ff:ff:ff link-netnsid 11
    inet6 fe80::ecd9:35ff:fe71:6286/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
50: veth3a23079@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 7e:86:92:e2:e0:93 brd ff:ff:ff:ff:ff:ff link-netnsid 6
    inet6 fe80::7c86:92ff:fee2:e093/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
53: veth8cb2f90@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 52:48:48:f1:f4:fb brd ff:ff:ff:ff:ff:ff link-netnsid 4
    inet6 fe80::5048:48ff:fef1:f4fb/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
55: veth4fbdd59@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether 02:0f:29:f1:3f:94 brd ff:ff:ff:ff:ff:ff link-netnsid 2
    inet6 fe80::f:29ff:fef1:3f94/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
57: vethdc71bba@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c8ba5432ed86 state UP group default 
    link/ether f2:1f:e5:b9:69:ca brd ff:ff:ff:ff:ff:ff link-netnsid 12
    inet6 fe80::f01f:e5ff:feb9:69ca/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever


```text
$ ip route
```
default via 192.168.1.254 dev enp0s9 proto dhcp src 192.168.1.64 metric 100 
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
172.20.0.0/16 dev br-c8ba5432ed86 proto kernel scope link src 172.20.0.1 
192.168.1.0/24 dev enp0s9 proto kernel scope link src 192.168.1.64 metric 100 


```text
$ ip -6 route
```
fe80::/64 dev vethc482531 proto kernel metric 256 pref medium
fe80::/64 dev br-c8ba5432ed86 proto kernel metric 256 pref medium
fe80::/64 dev veth43c9e99 proto kernel metric 256 pref medium
fe80::/64 dev veth272b590 proto kernel metric 256 pref medium
fe80::/64 dev veth769ba64 proto kernel metric 256 pref medium
fe80::/64 dev vetha289142 proto kernel metric 256 pref medium
fe80::/64 dev veth88ecfbd proto kernel metric 256 pref medium
fe80::/64 dev veth8139db8 proto kernel metric 256 pref medium
fe80::/64 dev vethbf38ab7 proto kernel metric 256 pref medium
fe80::/64 dev vetheb22e79 proto kernel metric 256 pref medium
fe80::/64 dev veth3a23079 proto kernel metric 256 pref medium
fe80::/64 dev veth8cb2f90 proto kernel metric 256 pref medium
fe80::/64 dev veth4fbdd59 proto kernel metric 256 pref medium
fe80::/64 dev vethdc71bba proto kernel metric 256 pref medium
fe80::/64 dev enp0s9 proto kernel metric 1024 pref medium


## NetworkManager / systemd-networkd


```text
$ nmcli connection show 2>/dev/null || true
```
NAME                UUID                                  TYPE      DEVICE          
Wired connection 1  e40cfa8b-9095-44bb-a153-ad58dc706b95  ethernet  enp0s9          
br-c8ba5432ed86     d85fb901-8a19-45b8-856f-b0c34f973259  bridge    br-c8ba5432ed86 
lo                  6e27b471-eb88-4f15-8524-96c83b0307b7  loopback  lo              
docker0             d7c8c931-dd92-40b6-9e60-a100d5eef013  bridge    docker0         


```text
$ networkctl list 2>/dev/null || true
```
IDX LINK            TYPE     OPERATIONAL SETUP
  1 lo              loopback -           unmanaged
  2 enp0s3          ether    -           unmanaged
  3 enp0s8          ether    -           unmanaged
  4 enp0s9          ether    -           unmanaged
  5 docker0         bridge   -           unmanaged
  6 br-c8ba5432ed86 bridge   -           unmanaged
  7 vethc482531     ether    -           unmanaged
  8 veth43c9e99     ether    -           unmanaged
 10 veth272b590     ether    -           unmanaged
 12 veth769ba64     ether    -           unmanaged
 14 vetha289142     ether    -           unmanaged
 15 veth88ecfbd     ether    -           unmanaged
 16 veth8139db8     ether    -           unmanaged
 17 vethbf38ab7     ether    -           unmanaged
 18 vetheb22e79     ether    -           unmanaged
 50 veth3a23079     ether    -           unmanaged
 53 veth8cb2f90     ether    -           unmanaged
 55 veth4fbdd59     ether    -           unmanaged
 57 vethdc71bba     ether    -           unmanaged

19 links listed.



---

# 27. VARIABLES D'ENVIRONNEMENT

**Date :** 2026-08-08 06:56:38 EDT


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
SUDO_COMMAND=/opt/civitas/jitsi-infrastructure-audit.sh
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
SUDO_COMMAND=/opt/civitas/jitsi-infrastructure-audit.sh



---

# 28. FICHIERS ENVIRONNEMENT

**Date :** 2026-08-08 06:56:38 EDT


```text
$ find /etc /opt /var/lib /usr/local -type f \( -name ".env" -o -name "*.env" \) -print 2>/dev/null | sort
```
/opt/civitas/services/peer/.env
/opt/civitas/services/room-config/.env
/opt/civitas/services/room-spawner/.env



---

# 29. RECHERCHE DE MOTS-CLÉS JITSI

**Date :** 2026-08-08 06:56:38 EDT


## Configuration globale


```text
$ grep -RniE "jitsi|jicofo|videobridge|prosody|xmpp|colibri|bosh|conference\.|focus\." /etc 2>/dev/null | head -5000 || true
```
/etc/xdg/autostart/org.kde.xwaylandvideobridge.desktop:60:Icon=xwaylandvideobridge
/etc/xdg/autostart/org.kde.xwaylandvideobridge.desktop:61:Exec=xwaylandvideobridge
/etc/services:225:xmpp-client	5222/tcp	jabber-client	# Jabber Client Connection
/etc/services:226:xmpp-server	5269/tcp	jabber-server	# Jabber Server Connection
/etc/prosody/README:1:Prosody configuration directory
/etc/prosody/README:4:The configuration file /etc/prosody/prosody.cfg.lua should contain
/etc/prosody/README:7:Per-host configuration files should be placed in /etc/prosody/conf.avail/,
/etc/prosody/README:8:and the active ones should be linked in /etc/prosody/conf.d/
/etc/prosody/migrator.cfg.lua:1:local data_path = '/var/lib/prosody';
/etc/prosody/migrator.cfg.lua:35:		["conference.example.com"] = muc;
/etc/prosody/migrator.cfg.lua:45:	database = data_path.."/prosody.sqlite";
/etc/prosody/migrator.cfg.lua:57:	database = data_path.."/prosody.sqlite";
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:3:plugin_paths = { "/usr/share/jitsi-meet/prosody-plugins/" }
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:14:cross_domain_bosh = false
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:15:consider_bosh_secure = true
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:24:    authentication = "jitsi-anonymous"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:26:        "bosh";
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:44:Component "conference.meet.civitas.local" "muc"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:65:Component "focus.meet.civitas.local" "client_proxy"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:69:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:71:Component "endconference.meet.civitas.local" "end_conference"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:72:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:96:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.d/meet.civitas.local.cfg.lua:99:    muc_component = "conference.meet.civitas.local"
/etc/prosody/conf.avail/example.com.cfg.lua:11:		key = "/etc/prosody/certs/example.com.key";
/etc/prosody/conf.avail/example.com.cfg.lua:12:		certificate = "/etc/prosody/certs/example.com.crt";
/etc/prosody/conf.avail/example.com.cfg.lua:18:-- For more information on components, see http://prosody.im/doc/components
/etc/prosody/conf.avail/example.com.cfg.lua:20:-- Set up a MUC (multi-user chat) room server on conference.example.com:
/etc/prosody/conf.avail/example.com.cfg.lua:21:Component "conference.example.com" "muc"
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:3:-- CIVITAS — Prosody webhooks
/etc/prosody/conf.avail/meet.civitas.local.cfg.lua:6:Component "conference.meet.civitas.local" "muc"
/etc/prosody/conf.avail/jaas.cfg.lua:1:-- Enables dial-in for Jitsi meet components customers
/etc/prosody/conf.avail/jaas.cfg.lua:2:VirtualHost "jigasi.meet.jitsi"
/etc/prosody/conf.avail/jaas.cfg.lua:5:        "bosh";
/etc/prosody/conf.avail/jaas.cfg.lua:9:    app_id = "jitsi";
/etc/prosody/conf.avail/jaas.cfg.lua:10:    asap_key_server = "https://jaas-public-keys.jitsi.net/jitsi-components/prod-8x8"
/etc/prosody/prosody.cfg.lua:1:-- Prosody Example Configuration File
/etc/prosody/prosody.cfg.lua:3:-- Information on configuring Prosody can be found on our
/etc/prosody/prosody.cfg.lua:4:-- website at https://prosody.im/doc/configure
/etc/prosody/prosody.cfg.lua:8:--     prosodyctl check config
/etc/prosody/prosody.cfg.lua:12:-- Upgrading from a previous release? Check https://prosody.im/doc/upgrading
/etc/prosody/prosody.cfg.lua:24:-- (see https://prosody.im/doc/creating_accounts for info)
/etc/prosody/prosody.cfg.lua:28:-- This option allows you to specify additional locations where Prosody
/etc/prosody/prosody.cfg.lua:30:-- the community module repository at https://modules.prosody.im/
/etc/prosody/prosody.cfg.lua:33:plugin_paths = { "/usr/local/lib/prosody/modules", "/usr/share/jitsi-meet/prosody-plugins/" }
/etc/prosody/prosody.cfg.lua:35:-- This is the list of modules Prosody will load on startup.
/etc/prosody/prosody.cfg.lua:36:-- Documentation for bundled modules can be found at: https://prosody.im/doc/modules
/etc/prosody/prosody.cfg.lua:50:		"limits"; -- Enable bandwidth limiting for XMPP connections
/etc/prosody/prosody.cfg.lua:64:		"ping"; -- Replies to XMPP pings with pongs
/etc/prosody/prosody.cfg.lua:73:		"admin_adhoc"; -- Allows administration via an XMPP client that supports ad-hoc commands
/etc/prosody/prosody.cfg.lua:74:		"admin_shell"; -- Allow secure administration via 'prosodyctl shell'
/etc/prosody/prosody.cfg.lua:77:		"bosh"; -- Enable BOSH clients, aka "Jabber over HTTP"
/etc/prosody/prosody.cfg.lua:79:		"websocket"; -- XMPP over WebSockets
/etc/prosody/prosody.cfg.lua:104:--   Please, don't change this option since /run/prosody/
/etc/prosody/prosody.cfg.lua:105:--   is one of the few directories Prosody is allowed to write to
/etc/prosody/prosody.cfg.lua:107:pidfile = "/run/prosody/prosody.pid";
/etc/prosody/prosody.cfg.lua:143:-- use Prosody's configured data storage to store the authentication data.
/etc/prosody/prosody.cfg.lua:144:-- For more information see https://prosody.im/doc/authentication
/etc/prosody/prosody.cfg.lua:149:-- create user accounts via Prosody's admin interfaces. For details, see the
/etc/prosody/prosody.cfg.lua:150:-- documentation at https://prosody.im/doc/creating_accounts
/etc/prosody/prosody.cfg.lua:154:-- Select the storage backend to use. By default Prosody uses flat files
/etc/prosody/prosody.cfg.lua:157:-- additional dependencies. See https://prosody.im/doc/storage for more info.
/etc/prosody/prosody.cfg.lua:163:--sql = { driver = "SQLite3", database = "prosody.sqlite" } -- Default. 'database' is the filename.
/etc/prosody/prosody.cfg.lua:164:--sql = { driver = "MySQL", database = "prosody", username = "prosody", password = "secret", host = "localhost" }
/etc/prosody/prosody.cfg.lua:165:--sql = { driver = "PostgreSQL", database = "prosody", username = "prosody", password = "secret", host = "localhost" }
/etc/prosody/prosody.cfg.lua:169:-- If mod_mam is enabled, Prosody will store a copy of every message. This
/etc/prosody/prosody.cfg.lua:171:-- they are offline. This setting controls how long Prosody will keep
/etc/prosody/prosody.cfg.lua:177:-- archiving options, see https://prosody.im/doc/modules/mod_mam
/etc/prosody/prosody.cfg.lua:185:-- Find more information at https://prosody.im/doc/turn
/etc/prosody/prosody.cfg.lua:187:-- Specify the address of the TURN service (you may use the same domain as XMPP)
/etc/prosody/prosody.cfg.lua:190:-- This secret must be set to the same value in both Prosody and the TURN server
/etc/prosody/prosody.cfg.lua:195:-- For advanced logging see https://prosody.im/doc/logging
/etc/prosody/prosody.cfg.lua:202:	info = "/var/log/prosody/prosody.log";
/etc/prosody/prosody.cfg.lua:203:	error = "/var/log/prosody/prosody.err";
/etc/prosody/prosody.cfg.lua:210:-- For more info see https://prosody.im/doc/statistics
/etc/prosody/prosody.cfg.lua:216:-- servers can securely verify its identity. Prosody will automatically load
/etc/prosody/prosody.cfg.lua:218:-- For more information, including how to use 'prosodyctl' to auto-import certificates
/etc/prosody/prosody.cfg.lua:219:-- (from e.g. Let's Encrypt) see https://prosody.im/doc/certificates
/etc/prosody/prosody.cfg.lua:225:-- You need to add a VirtualHost entry for each domain you wish Prosody to serve.
/etc/prosody/prosody.cfg.lua:228:-- under /etc/prosody/conf.d/ directory. Examples of such config files can
/etc/prosody/prosody.cfg.lua:229:-- be found in /etc/prosody/conf.avail/ directory.
/etc/prosody/prosody.cfg.lua:234:-- all config files in /etc/prosody/conf.d/
/etc/prosody/prosody.cfg.lua:237:-- Prosody requires at least one enabled VirtualHost to function. You can
/etc/prosody/prosody.cfg.lua:246:-- For more information on components, see https://prosody.im/doc/components
/etc/prosody/prosody.cfg.lua:248:---Set up a MUC (multi-user chat) room server on conference.example.com:
/etc/prosody/prosody.cfg.lua:249:--Component "conference.example.com" "muc"
/etc/prosody/prosody.cfg.lua:259:-- bridges to non-XMPP networks and services. For more info
/etc/prosody/prosody.cfg.lua:260:-- see: https://prosody.im/doc/components#adding_an_external_component
/etc/prosody/prosody.cfg.lua:267:---------- End of the Prosody Configuration file ----------
/etc/prosody/prosody.cfg.lua:275:-- For more information see https://prosody.im/doc/configure
/etc/libreoffice/registry/main.xcd:2417:          <prop oor:name="JumboSheets" oor:type="xs:boolean" oor:nillable="false">
/etc/libreoffice/registry/main.xcd:4784:            the focus.
/etc/passwd-:39:jvb:x:997:1001::/usr/share/jitsi-videobridge:/bin/bash
/etc/passwd-:40:jicofo:x:996:1001::/usr/share/jicofo:/bin/bash
/etc/passwd-:41:prosody:x:111:115:Prosody XMPP Server:/var/lib/prosody:/usr/sbin/nologin
/etc/turnserver.conf:1:# jitsi-meet coturn config. Do not modify this line
/etc/turnserver.conf:22:# jitsi-meet coturn relay disable config. Do not modify this line
/etc/gimp/3.0/gimprc:646:# receives the focus. This is useful for window managers using "click to
/etc/rc5.d/S01jicofo:3:# INIT script for Jitsi Conference Focus
/etc/rc5.d/S01jicofo:4:# Version: 1.0  4-Dec-2014  pawel.domas@jitsi.org
/etc/rc5.d/S01jicofo:7:# Provides:          jicofo
/etc/rc5.d/S01jicofo:12:# Short-Description: Jitsi conference Focus
/etc/rc5.d/S01jicofo:13:# Description:       Conference focus for Jitsi Meet application.
/etc/rc5.d/S01jicofo:18:# Include jicofo defaults if available
/etc/rc5.d/S01jicofo:19:if [ -f /etc/jitsi/jicofo/config ]; then
/etc/rc5.d/S01jicofo:20:    . /etc/jitsi/jicofo/config
/etc/rc5.d/S01jicofo:24:DAEMON=/usr/share/jicofo/jicofo.sh
/etc/rc5.d/S01jicofo:25:DAEMON_DIR=/usr/share/jicofo/
/etc/rc5.d/S01jicofo:26:NAME=jicofo
/etc/rc5.d/S01jicofo:27:USER=jicofo
/etc/rc5.d/S01jicofo:28:PIDFILE=/var/run/jicofo.pid
/etc/rc5.d/S01jicofo:29:LOGFILE=/var/log/jitsi/jicofo.log
/etc/rc5.d/S01jicofo:30:DESC=jicofo
/etc/rc5.d/S01jicofo:60:    export JICOFO_AUTH_PASSWORD JICOFO_MAX_MEMORY
/etc/rc5.d/S01jicofo:62:        --exec /bin/bash -- -c "cd $DAEMON_DIR; JAVA_SYS_PROPS=\"$JAVA_SYS_PROPS\" exec $DAEMON $JICOFO_OPTS < /dev/null >> $LOGFILE 2>&1"
/etc/rc5.d/S01prosody:4:# Provides:             prosody
/etc/rc5.d/S01prosody:11:# Short-Description:    Prosody XMPP Server
/etc/rc5.d/S01prosody:16:# /etc/init.d/prosody: start and stop Prosody XMPP server
/etc/rc5.d/S01prosody:18:USER=prosody
/etc/rc5.d/S01prosody:19:DAEMON=/usr/bin/prosody
/etc/rc5.d/S01prosody:20:PIDPATH=/run/prosody
/etc/rc5.d/S01prosody:21:PIDFILE="$PIDPATH"/prosody.pid
/etc/rc5.d/S01prosody:32:if [ -f /etc/default/prosody ] ; then
/etc/rc5.d/S01prosody:33:    . /etc/default/prosody
/etc/rc5.d/S01prosody:42:start_prosody () {
/etc/rc5.d/S01prosody:44:	chown prosody:adm "$(dirname $PIDFILE)"
/etc/rc5.d/S01prosody:56:stop_prosody () {
/etc/rc5.d/S01prosody:66:signal_prosody () {
/etc/rc5.d/S01prosody:78:	log_daemon_msg "Starting Prosody XMPP Server" "prosody"
/etc/rc5.d/S01prosody:79:	if start_prosody; then
/etc/rc5.d/S01prosody:86:  	log_daemon_msg "Stopping Prosody XMPP Server" "prosody"
/etc/rc5.d/S01prosody:87:  	if stop_prosody; then
/etc/rc5.d/S01prosody:94:  	log_daemon_msg "Restarting Prosody XMPP Server" "prosody"
/etc/rc5.d/S01prosody:96:  	stop_prosody
/etc/rc5.d/S01prosody:98:	if start_prosody; then
/etc/rc5.d/S01prosody:105:  	log_daemon_msg "Reloading Prosody XMPP Server" "prosody"
/etc/rc5.d/S01prosody:107:	if signal_prosody 1; then
/etc/rc5.d/S01prosody:114:	log_daemon_msg "Status of Prosody XMPP Server" "prosody "
/etc/rc5.d/S01prosody:118:  	log_action_msg "Usage: /etc/init.d/prosody {start|stop|restart|reload|status}"
/etc/mime.types:1752:application/xmpp+xml
/etc/nginx/sites-available/meet.civitas.local.conf:8:upstream prosody {
/etc/nginx/sites-available/meet.civitas.local.conf:18:map $arg_vnode $prosody_node {
/etc/nginx/sites-available/meet.civitas.local.conf:19:    default prosody;
/etc/nginx/sites-available/meet.civitas.local.conf:36:        root         /usr/share/jitsi-meet;
/etc/nginx/sites-available/meet.civitas.local.conf:62:    set $config_js_location /etc/jitsi/meet/meet.civitas.local-config.js;
/etc/nginx/sites-available/meet.civitas.local.conf:67:    root /usr/share/jitsi-meet;
/etc/nginx/sites-available/meet.civitas.local.conf:82:    include /etc/jitsi/meet/jaas/*.conf;
/etc/nginx/sites-available/meet.civitas.local.conf:89:        alias /usr/share/jitsi-meet/libs/external_api.min.js;
/etc/nginx/sites-available/meet.civitas.local.conf:93:        proxy_pass http://prosody/room-info?prefix=$prefix&$args;
/etc/nginx/sites-available/meet.civitas.local.conf:101:        alias /etc/jitsi/meet/public/$1;
/etc/nginx/sites-available/meet.civitas.local.conf:108:        alias /usr/share/jitsi-meet/$1/$2;
/etc/nginx/sites-available/meet.civitas.local.conf:116:    # BOSH
/etc/nginx/sites-available/meet.civitas.local.conf:118:        proxy_pass http://$prosody_node/http-bind?prefix=$prefix&$args;
/etc/nginx/sites-available/meet.civitas.local.conf:125:    # xmpp websockets
/etc/nginx/sites-available/meet.civitas.local.conf:126:    location = /xmpp-websocket {
/etc/nginx/sites-available/meet.civitas.local.conf:127:        proxy_pass http://$prosody_node/xmpp-websocket?prefix=$prefix&$args;
/etc/nginx/sites-available/meet.civitas.local.conf:135:    # colibri (JVB) websockets for jvb1
/etc/nginx/sites-available/meet.civitas.local.conf:136:    location ~ ^/colibri-ws/default-id/(.*) {
/etc/nginx/sites-available/meet.civitas.local.conf:137:        proxy_pass http://jvb1/colibri-ws/default-id/$1$is_args$args;
/etc/nginx/sites-available/meet.civitas.local.conf:150:    #    alias /usr/share/jitsi-meet/load-test/libs/$1;
/etc/nginx/sites-available/meet.civitas.local.conf:194:    # BOSH for subdomains
/etc/nginx/sites-available/meet.civitas.local.conf:204:    location ~ ^/([^/?&:'"]+)/xmpp-websocket {
/etc/nginx/sites-available/meet.civitas.local.conf:209:        rewrite ^/(.*)$ /xmpp-websocket;
/etc/nginx/sites-enabled/meet.civitas.local.conf:8:upstream prosody {
/etc/nginx/sites-enabled/meet.civitas.local.conf:18:map $arg_vnode $prosody_node {
/etc/nginx/sites-enabled/meet.civitas.local.conf:19:    default prosody;
/etc/nginx/sites-enabled/meet.civitas.local.conf:36:        root         /usr/share/jitsi-meet;
/etc/nginx/sites-enabled/meet.civitas.local.conf:62:    set $config_js_location /etc/jitsi/meet/meet.civitas.local-config.js;
/etc/nginx/sites-enabled/meet.civitas.local.conf:67:    root /usr/share/jitsi-meet;
/etc/nginx/sites-enabled/meet.civitas.local.conf:82:    include /etc/jitsi/meet/jaas/*.conf;
/etc/nginx/sites-enabled/meet.civitas.local.conf:89:        alias /usr/share/jitsi-meet/libs/external_api.min.js;
/etc/nginx/sites-enabled/meet.civitas.local.conf:93:        proxy_pass http://prosody/room-info?prefix=$prefix&$args;
/etc/nginx/sites-enabled/meet.civitas.local.conf:101:        alias /etc/jitsi/meet/public/$1;
/etc/nginx/sites-enabled/meet.civitas.local.conf:108:        alias /usr/share/jitsi-meet/$1/$2;
/etc/nginx/sites-enabled/meet.civitas.local.conf:116:    # BOSH
/etc/nginx/sites-enabled/meet.civitas.local.conf:118:        proxy_pass http://$prosody_node/http-bind?prefix=$prefix&$args;
/etc/nginx/sites-enabled/meet.civitas.local.conf:125:    # xmpp websockets
/etc/nginx/sites-enabled/meet.civitas.local.conf:126:    location = /xmpp-websocket {
/etc/nginx/sites-enabled/meet.civitas.local.conf:127:        proxy_pass http://$prosody_node/xmpp-websocket?prefix=$prefix&$args;
/etc/nginx/sites-enabled/meet.civitas.local.conf:135:    # colibri (JVB) websockets for jvb1
/etc/nginx/sites-enabled/meet.civitas.local.conf:136:    location ~ ^/colibri-ws/default-id/(.*) {
/etc/nginx/sites-enabled/meet.civitas.local.conf:137:        proxy_pass http://jvb1/colibri-ws/default-id/$1$is_args$args;
/etc/nginx/sites-enabled/meet.civitas.local.conf:150:    #    alias /usr/share/jitsi-meet/load-test/libs/$1;
/etc/nginx/sites-enabled/meet.civitas.local.conf:194:    # BOSH for subdomains
/etc/nginx/sites-enabled/meet.civitas.local.conf:204:    location ~ ^/([^/?&:'"]+)/xmpp-websocket {
/etc/nginx/sites-enabled/meet.civitas.local.conf:209:        rewrite ^/(.*)$ /xmpp-websocket;
/etc/rc3.d/S01jicofo:3:# INIT script for Jitsi Conference Focus
/etc/rc3.d/S01jicofo:4:# Version: 1.0  4-Dec-2014  pawel.domas@jitsi.org
/etc/rc3.d/S01jicofo:7:# Provides:          jicofo
/etc/rc3.d/S01jicofo:12:# Short-Description: Jitsi conference Focus
/etc/rc3.d/S01jicofo:13:# Description:       Conference focus for Jitsi Meet application.
/etc/rc3.d/S01jicofo:18:# Include jicofo defaults if available
/etc/rc3.d/S01jicofo:19:if [ -f /etc/jitsi/jicofo/config ]; then
/etc/rc3.d/S01jicofo:20:    . /etc/jitsi/jicofo/config
/etc/rc3.d/S01jicofo:24:DAEMON=/usr/share/jicofo/jicofo.sh
/etc/rc3.d/S01jicofo:25:DAEMON_DIR=/usr/share/jicofo/
/etc/rc3.d/S01jicofo:26:NAME=jicofo
/etc/rc3.d/S01jicofo:27:USER=jicofo
/etc/rc3.d/S01jicofo:28:PIDFILE=/var/run/jicofo.pid
/etc/rc3.d/S01jicofo:29:LOGFILE=/var/log/jitsi/jicofo.log
/etc/rc3.d/S01jicofo:30:DESC=jicofo
/etc/rc3.d/S01jicofo:60:    export JICOFO_AUTH_PASSWORD JICOFO_MAX_MEMORY
/etc/rc3.d/S01jicofo:62:        --exec /bin/bash -- -c "cd $DAEMON_DIR; JAVA_SYS_PROPS=\"$JAVA_SYS_PROPS\" exec $DAEMON $JICOFO_OPTS < /dev/null >> $LOGFILE 2>&1"
/etc/rc3.d/S01prosody:4:# Provides:             prosody
/etc/rc3.d/S01prosody:11:# Short-Description:    Prosody XMPP Server
/etc/rc3.d/S01prosody:16:# /etc/init.d/prosody: start and stop Prosody XMPP server
/etc/rc3.d/S01prosody:18:USER=prosody
/etc/rc3.d/S01prosody:19:DAEMON=/usr/bin/prosody
/etc/rc3.d/S01prosody:20:PIDPATH=/run/prosody
/etc/rc3.d/S01prosody:21:PIDFILE="$PIDPATH"/prosody.pid
/etc/rc3.d/S01prosody:32:if [ -f /etc/default/prosody ] ; then
/etc/rc3.d/S01prosody:33:    . /etc/default/prosody
/etc/rc3.d/S01prosody:42:start_prosody () {
/etc/rc3.d/S01prosody:44:	chown prosody:adm "$(dirname $PIDFILE)"
/etc/rc3.d/S01prosody:56:stop_prosody () {
/etc/rc3.d/S01prosody:66:signal_prosody () {
/etc/rc3.d/S01prosody:78:	log_daemon_msg "Starting Prosody XMPP Server" "prosody"
/etc/rc3.d/S01prosody:79:	if start_prosody; then
/etc/rc3.d/S01prosody:86:  	log_daemon_msg "Stopping Prosody XMPP Server" "prosody"
/etc/rc3.d/S01prosody:87:  	if stop_prosody; then
/etc/rc3.d/S01prosody:94:  	log_daemon_msg "Restarting Prosody XMPP Server" "prosody"
/etc/rc3.d/S01prosody:96:  	stop_prosody
/etc/rc3.d/S01prosody:98:	if start_prosody; then
/etc/rc3.d/S01prosody:105:  	log_daemon_msg "Reloading Prosody XMPP Server" "prosody"
/etc/rc3.d/S01prosody:107:	if signal_prosody 1; then
/etc/rc3.d/S01prosody:114:	log_daemon_msg "Status of Prosody XMPP Server" "prosody "
/etc/rc3.d/S01prosody:118:  	log_action_msg "Usage: /etc/init.d/prosody {start|stop|restart|reload|status}"
/etc/gshadow-:68:jitsi:!::
/etc/gshadow-:69:prosody:!::
/etc/shadow:40:jicofo:!:20535::::::
/etc/shadow:41:prosody:!:20535::::::
/etc/ufw/applications.d/ufw-chat:31:[XMPP]
/etc/ufw/applications.d/ufw-chat:32:title=XMPP Chat
/etc/ufw/applications.d/ufw-chat:33:description=XMPP protocol (Jabber and Google Talk)
/etc/rc4.d/S01jicofo:3:# INIT script for Jitsi Conference Focus
/etc/rc4.d/S01jicofo:4:# Version: 1.0  4-Dec-2014  pawel.domas@jitsi.org
/etc/rc4.d/S01jicofo:7:# Provides:          jicofo
/etc/rc4.d/S01jicofo:12:# Short-Description: Jitsi conference Focus
/etc/rc4.d/S01jicofo:13:# Description:       Conference focus for Jitsi Meet application.
/etc/rc4.d/S01jicofo:18:# Include jicofo defaults if available
/etc/rc4.d/S01jicofo:19:if [ -f /etc/jitsi/jicofo/config ]; then
/etc/rc4.d/S01jicofo:20:    . /etc/jitsi/jicofo/config
/etc/rc4.d/S01jicofo:24:DAEMON=/usr/share/jicofo/jicofo.sh
/etc/rc4.d/S01jicofo:25:DAEMON_DIR=/usr/share/jicofo/
/etc/rc4.d/S01jicofo:26:NAME=jicofo
/etc/rc4.d/S01jicofo:27:USER=jicofo
/etc/rc4.d/S01jicofo:28:PIDFILE=/var/run/jicofo.pid
/etc/rc4.d/S01jicofo:29:LOGFILE=/var/log/jitsi/jicofo.log
/etc/rc4.d/S01jicofo:30:DESC=jicofo
/etc/rc4.d/S01jicofo:60:    export JICOFO_AUTH_PASSWORD JICOFO_MAX_MEMORY
/etc/rc4.d/S01jicofo:62:        --exec /bin/bash -- -c "cd $DAEMON_DIR; JAVA_SYS_PROPS=\"$JAVA_SYS_PROPS\" exec $DAEMON $JICOFO_OPTS < /dev/null >> $LOGFILE 2>&1"
/etc/rc4.d/S01prosody:4:# Provides:             prosody
/etc/rc4.d/S01prosody:11:# Short-Description:    Prosody XMPP Server
/etc/rc4.d/S01prosody:16:# /etc/init.d/prosody: start and stop Prosody XMPP server
/etc/rc4.d/S01prosody:18:USER=prosody
/etc/rc4.d/S01prosody:19:DAEMON=/usr/bin/prosody
/etc/rc4.d/S01prosody:20:PIDPATH=/run/prosody
/etc/rc4.d/S01prosody:21:PIDFILE="$PIDPATH"/prosody.pid
/etc/rc4.d/S01prosody:32:if [ -f /etc/default/prosody ] ; then
/etc/rc4.d/S01prosody:33:    . /etc/default/prosody
/etc/rc4.d/S01prosody:42:start_prosody () {
/etc/rc4.d/S01prosody:44:	chown prosody:adm "$(dirname $PIDFILE)"
/etc/rc4.d/S01prosody:56:stop_prosody () {
/etc/rc4.d/S01prosody:66:signal_prosody () {
/etc/rc4.d/S01prosody:78:	log_daemon_msg "Starting Prosody XMPP Server" "prosody"
/etc/rc4.d/S01prosody:79:	if start_prosody; then
/etc/rc4.d/S01prosody:86:  	log_daemon_msg "Stopping Prosody XMPP Server" "prosody"
/etc/rc4.d/S01prosody:87:  	if stop_prosody; then
/etc/rc4.d/S01prosody:94:  	log_daemon_msg "Restarting Prosody XMPP Server" "prosody"
/etc/rc4.d/S01prosody:96:  	stop_prosody
/etc/rc4.d/S01prosody:98:	if start_prosody; then
/etc/rc4.d/S01prosody:105:  	log_daemon_msg "Reloading Prosody XMPP Server" "prosody"
/etc/rc4.d/S01prosody:107:	if signal_prosody 1; then
/etc/rc4.d/S01prosody:114:	log_daemon_msg "Status of Prosody XMPP Server" "prosody "
/etc/rc4.d/S01prosody:118:  	log_action_msg "Usage: /etc/init.d/prosody {start|stop|restart|reload|status}"
/etc/init.d/prosody:4:# Provides:             prosody
/etc/init.d/prosody:11:# Short-Description:    Prosody XMPP Server
/etc/init.d/prosody:16:# /etc/init.d/prosody: start and stop Prosody XMPP server
/etc/init.d/prosody:18:USER=prosody
/etc/init.d/prosody:19:DAEMON=/usr/bin/prosody
/etc/init.d/prosody:20:PIDPATH=/run/prosody
/etc/init.d/prosody:21:PIDFILE="$PIDPATH"/prosody.pid
/etc/init.d/prosody:32:if [ -f /etc/default/prosody ] ; then
/etc/init.d/prosody:33:    . /etc/default/prosody
/etc/init.d/prosody:42:start_prosody () {
/etc/init.d/prosody:44:	chown prosody:adm "$(dirname $PIDFILE)"
/etc/init.d/prosody:56:stop_prosody () {
/etc/init.d/prosody:66:signal_prosody () {
/etc/init.d/prosody:78:	log_daemon_msg "Starting Prosody XMPP Server" "prosody"
/etc/init.d/prosody:79:	if start_prosody; then
/etc/init.d/prosody:86:  	log_daemon_msg "Stopping Prosody XMPP Server" "prosody"
/etc/init.d/prosody:87:  	if stop_prosody; then
/etc/init.d/prosody:94:  	log_daemon_msg "Restarting Prosody XMPP Server" "prosody"
/etc/init.d/prosody:96:  	stop_prosody
/etc/init.d/prosody:98:	if start_prosody; then
/etc/init.d/prosody:105:  	log_daemon_msg "Reloading Prosody XMPP Server" "prosody"
/etc/init.d/prosody:107:	if signal_prosody 1; then
/etc/init.d/prosody:114:	log_daemon_msg "Status of Prosody XMPP Server" "prosody "
/etc/init.d/prosody:118:  	log_action_msg "Usage: /etc/init.d/prosody {start|stop|restart|reload|status}"
/etc/init.d/jicofo:3:# INIT script for Jitsi Conference Focus
/etc/init.d/jicofo:4:# Version: 1.0  4-Dec-2014  pawel.domas@jitsi.org
/etc/init.d/jicofo:7:# Provides:          jicofo
/etc/init.d/jicofo:12:# Short-Description: Jitsi conference Focus
/etc/init.d/jicofo:13:# Description:       Conference focus for Jitsi Meet application.
/etc/init.d/jicofo:18:# Include jicofo defaults if available
/etc/init.d/jicofo:19:if [ -f /etc/jitsi/jicofo/config ]; then
/etc/init.d/jicofo:20:    . /etc/jitsi/jicofo/config
/etc/init.d/jicofo:24:DAEMON=/usr/share/jicofo/jicofo.sh
/etc/init.d/jicofo:25:DAEMON_DIR=/usr/share/jicofo/
/etc/init.d/jicofo:26:NAME=jicofo
/etc/init.d/jicofo:27:USER=jicofo
/etc/init.d/jicofo:28:PIDFILE=/var/run/jicofo.pid
/etc/init.d/jicofo:29:LOGFILE=/var/log/jitsi/jicofo.log
/etc/init.d/jicofo:30:DESC=jicofo
/etc/init.d/jicofo:60:    export JICOFO_AUTH_PASSWORD JICOFO_MAX_MEMORY
/etc/init.d/jicofo:62:        --exec /bin/bash -- -c "cd $DAEMON_DIR; JAVA_SYS_PROPS=\"$JAVA_SYS_PROPS\" exec $DAEMON $JICOFO_OPTS < /dev/null >> $LOGFILE 2>&1"
/etc/init.d/jitsi-videobridge2:3:# INIT script for Jitsi Videobridge
/etc/init.d/jitsi-videobridge2:7:# Provides:          jitsi-videobridge
/etc/init.d/jitsi-videobridge2:12:# Short-Description: Jitsi Videobridge
/etc/init.d/jitsi-videobridge2:18:# Include videobridge defaults if available
/etc/init.d/jitsi-videobridge2:19:if [ -f /etc/jitsi/videobridge/config ]; then
/etc/init.d/jitsi-videobridge2:20:    . /etc/jitsi/videobridge/config
/etc/init.d/jitsi-videobridge2:24:DAEMON=/usr/share/jitsi-videobridge/jvb.sh
/etc/init.d/jitsi-videobridge2:29:TMPPATH=/var/run/jitsi-videobridge
/etc/init.d/jitsi-videobridge2:30:PIDFILE=/var/run/jitsi-videobridge.pid
/etc/init.d/jitsi-videobridge2:31:LOGFILE=/var/log/jitsi/jvb.log
/etc/init.d/jitsi-videobridge2:32:DESC=jitsi-videobridge
/etc/group-:68:jitsi:x:1001:
/etc/group-:69:prosody:x:115:
/etc/ssl/certs/ca-certificates.crt:3476:yKsi2XMPpfRaAok/T54igu6idFMqPVMnaR1sjjIsZAAmY2E2TqNGtz99sy2sbZCi
/etc/ssl/certs/TWCA_Global_Root_CA.pem:13:yKsi2XMPpfRaAok/T54igu6idFMqPVMnaR1sjjIsZAAmY2E2TqNGtz99sy2sbZCi
/etc/ssl/certs/5f15c80c.0:13:yKsi2XMPpfRaAok/T54igu6idFMqPVMnaR1sjjIsZAAmY2E2TqNGtz99sy2sbZCi
/etc/gshadow:68:jitsi:!::
/etc/gshadow:69:prosody:!::
/etc/fail2ban/action.d/firewallcmd-common.conf:45:#          telnet tftp tftp-client tinc tor-socks transmission-client vdsm vnc-server wbem-https xmpp-bosh xmpp-client xmpp-local xmpp-server
/etc/jitsi/meet/meet.civitas.local-config.js:4:        muc: 'conference.meet.civitas.local',
/etc/jitsi/meet/meet.civitas.local-config.js:5:        focus: 'focus.meet.civitas.local',
/etc/jitsi/meet/meet.civitas.local-config.js:7:    bosh: '//meet.civitas.local/http-bind',
/etc/jitsi/meet/meet.civitas.local-config.js:8:    websocket: 'wss://meet.civitas.local/xmpp-websocket',
/etc/jitsi/jicofo/config:1:# adds java system props that are passed to jicofo (default are for home and logging config file)
/etc/jitsi/jicofo/config:2:JAVA_SYS_PROPS="-Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=jicofo -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/jicofo/logging.properties"
/etc/jitsi/jicofo/logging.properties:4:# Handlers with XMPP debug enabled:
/etc/jitsi/jicofo/logging.properties:5:#handlers= java.util.logging.ConsoleHandler, org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler
/etc/jitsi/jicofo/logging.properties:11:java.util.logging.ConsoleHandler.formatter = org.jitsi.utils.logging2.JitsiLogFormatter
/etc/jitsi/jicofo/logging.properties:12:java.util.logging.ConsoleHandler.filter = org.jitsi.impl.protocol.xmpp.log.ExcludeXmppPackets
/etc/jitsi/jicofo/logging.properties:14:org.jitsi.utils.logging2.JitsiLogFormatter.programname=Jicofo
/etc/jitsi/jicofo/logging.properties:17:# To enable XMPP packets logging add XmppPacketsFileHandler to the handlers property
/etc/jitsi/jicofo/logging.properties:18:org.jitsi.impl.protocol.xmpp.log.PacketDebugger.level=ALL
/etc/jitsi/jicofo/logging.properties:19:org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.pattern=/var/log/jitsi/jicofo-xmpp.log
/etc/jitsi/jicofo/logging.properties:20:org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.append=true
/etc/jitsi/jicofo/logging.properties:21:org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.limit=200000000
/etc/jitsi/jicofo/logging.properties:22:org.jitsi.impl.protocol.xmpp.log.XmppPacketsFileHandler.count=3
/etc/jitsi/jicofo/logging.properties:27:# uncomment to see how Jicofo talks to the JVB
/etc/jitsi/jicofo/logging.properties:28:#org.jitsi.impl.protocol.xmpp.colibri.level=ALL
/etc/jitsi/jicofo/jicofo.conf:1:jicofo {
/etc/jitsi/jicofo/jicofo.conf:2:  xmpp: {
/etc/jitsi/jicofo/jicofo.conf:4:      client-proxy: "focus.meet.civitas.local"
/etc/jitsi/jicofo/jicofo.conf:5:      xmpp-domain: "meet.civitas.local"
/etc/jitsi/videobridge/jvb.conf:1:videobridge {
/etc/jitsi/videobridge/jvb.conf:12:    apis.xmpp-client.configs {
/etc/jitsi/videobridge/jvb.conf:30:                addresses = ["meet-jit-si-turnrelay.jitsi.net:443"]
/etc/jitsi/videobridge/config:3:JAVA_SYS_PROPS="-Dconfig.file=/etc/jitsi/videobridge/jvb.conf -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=videobridge -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/videobridge/logging.properties"
/etc/jitsi/videobridge/logging.properties:5:java.util.logging.ConsoleHandler.formatter = org.jitsi.utils.logging2.JitsiLogFormatter
/etc/jitsi/videobridge/logging.properties:7:org.jitsi.utils.logging2.JitsiLogFormatter.programname=JVB
/etc/rc2.d/S01jicofo:3:# INIT script for Jitsi Conference Focus
/etc/rc2.d/S01jicofo:4:# Version: 1.0  4-Dec-2014  pawel.domas@jitsi.org
/etc/rc2.d/S01jicofo:7:# Provides:          jicofo
/etc/rc2.d/S01jicofo:12:# Short-Description: Jitsi conference Focus
/etc/rc2.d/S01jicofo:13:# Description:       Conference focus for Jitsi Meet application.
/etc/rc2.d/S01jicofo:18:# Include jicofo defaults if available
/etc/rc2.d/S01jicofo:19:if [ -f /etc/jitsi/jicofo/config ]; then
/etc/rc2.d/S01jicofo:20:    . /etc/jitsi/jicofo/config
/etc/rc2.d/S01jicofo:24:DAEMON=/usr/share/jicofo/jicofo.sh
/etc/rc2.d/S01jicofo:25:DAEMON_DIR=/usr/share/jicofo/
/etc/rc2.d/S01jicofo:26:NAME=jicofo
/etc/rc2.d/S01jicofo:27:USER=jicofo
/etc/rc2.d/S01jicofo:28:PIDFILE=/var/run/jicofo.pid
/etc/rc2.d/S01jicofo:29:LOGFILE=/var/log/jitsi/jicofo.log
/etc/rc2.d/S01jicofo:30:DESC=jicofo
/etc/rc2.d/S01jicofo:60:    export JICOFO_AUTH_PASSWORD JICOFO_MAX_MEMORY
/etc/rc2.d/S01jicofo:62:        --exec /bin/bash -- -c "cd $DAEMON_DIR; JAVA_SYS_PROPS=\"$JAVA_SYS_PROPS\" exec $DAEMON $JICOFO_OPTS < /dev/null >> $LOGFILE 2>&1"
/etc/rc2.d/S01prosody:4:# Provides:             prosody
/etc/rc2.d/S01prosody:11:# Short-Description:    Prosody XMPP Server
/etc/rc2.d/S01prosody:16:# /etc/init.d/prosody: start and stop Prosody XMPP server
/etc/rc2.d/S01prosody:18:USER=prosody
/etc/rc2.d/S01prosody:19:DAEMON=/usr/bin/prosody
/etc/rc2.d/S01prosody:20:PIDPATH=/run/prosody
/etc/rc2.d/S01prosody:21:PIDFILE="$PIDPATH"/prosody.pid
/etc/rc2.d/S01prosody:32:if [ -f /etc/default/prosody ] ; then
/etc/rc2.d/S01prosody:33:    . /etc/default/prosody
/etc/rc2.d/S01prosody:42:start_prosody () {
/etc/rc2.d/S01prosody:44:	chown prosody:adm "$(dirname $PIDFILE)"
/etc/rc2.d/S01prosody:56:stop_prosody () {
/etc/rc2.d/S01prosody:66:signal_prosody () {
/etc/rc2.d/S01prosody:78:	log_daemon_msg "Starting Prosody XMPP Server" "prosody"
/etc/rc2.d/S01prosody:79:	if start_prosody; then
/etc/rc2.d/S01prosody:86:  	log_daemon_msg "Stopping Prosody XMPP Server" "prosody"
/etc/rc2.d/S01prosody:87:  	if stop_prosody; then
/etc/rc2.d/S01prosody:94:  	log_daemon_msg "Restarting Prosody XMPP Server" "prosody"
/etc/rc2.d/S01prosody:96:  	stop_prosody
/etc/rc2.d/S01prosody:98:	if start_prosody; then
/etc/rc2.d/S01prosody:105:  	log_daemon_msg "Reloading Prosody XMPP Server" "prosody"
/etc/rc2.d/S01prosody:107:	if signal_prosody 1; then
/etc/rc2.d/S01prosody:114:	log_daemon_msg "Status of Prosody XMPP Server" "prosody "
/etc/rc2.d/S01prosody:118:  	log_action_msg "Usage: /etc/init.d/prosody {start|stop|restart|reload|status}"
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf:2:# S'assurer que Prosody et le réseau sont prêts avant JVB
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf:3:After=network-online.target prosody.service jicofo.service
/etc/systemd/system/jitsi-videobridge2.service.d/override.conf:4:Requires=network-online.target prosody.service
/etc/systemd/system/civitas.service:3:After=network-online.target jitsi-videobridge2.service jicofo.service prosody.service docker.service
/etc/systemd/system/civitas.service:5:Wants=jitsi-videobridge2.service jicofo.service
/etc/systemd/system/multi-user.target.wants/jitsi-videobridge2.service:2:Description=Jitsi Videobridge
/etc/systemd/system/multi-user.target.wants/jitsi-videobridge2.service:12:EnvironmentFile=/etc/jitsi/videobridge/config
/etc/systemd/system/multi-user.target.wants/jitsi-videobridge2.service:13:Environment=LOGFILE=/var/log/jitsi/jvb.log
/etc/systemd/system/multi-user.target.wants/jitsi-videobridge2.service:15:RuntimeDirectory=jitsi-videobridge
/etc/systemd/system/multi-user.target.wants/jitsi-videobridge2.service:17:PIDFile=/var/run/jitsi-videobridge/jitsi-videobridge.pid
/etc/systemd/system/multi-user.target.wants/jitsi-videobridge2.service:23:ExecStart=/bin/bash -c "exec /usr/share/jitsi-videobridge/jvb.sh ${JVB_OPTS} < /dev/null >> ${LOGFILE} 2>&1"
/etc/systemd/system/multi-user.target.wants/jitsi-videobridge2.service:24:ExecStartPost=/bin/bash -c "echo $MAINPID > /var/run/jitsi-videobridge/jitsi-videobridge.pid"
/etc/systemd/system/multi-user.target.wants/prosody.service:3:Description=Prosody XMPP Server
/etc/systemd/system/multi-user.target.wants/prosody.service:6:Documentation=https://prosody.im/doc
/etc/systemd/system/multi-user.target.wants/prosody.service:11:# so Prosody should be configured with daemonize = false
/etc/systemd/system/multi-user.target.wants/prosody.service:15:RuntimeDirectory=prosody
/etc/systemd/system/multi-user.target.wants/prosody.service:16:PIDFile=/run/prosody/prosody.pid
/etc/systemd/system/multi-user.target.wants/prosody.service:19:# Note: -F option requires Prosody 0.11.5 or later
/etc/systemd/system/multi-user.target.wants/prosody.service:20:ExecStart=/usr/bin/prosody -F
/etc/systemd/system/multi-user.target.wants/prosody.service:32:WorkingDirectory=/var/lib/prosody
/etc/systemd/system/multi-user.target.wants/prosody.service:34:User=prosody
/etc/systemd/system/multi-user.target.wants/prosody.service:35:Group=prosody
/etc/systemd/system/multi-user.target.wants/prosody.service:39:# Set stdin to /dev/null since Prosody does not need it
/etc/systemd/system/multi-user.target.wants/prosody.service:52:# Needs read access to /etc/prosody for config
/etc/systemd/system/multi-user.target.wants/prosody.service:53:# Needs write access to /var/lib/prosody for storing data (for internal storage)
/etc/systemd/system/multi-user.target.wants/prosody.service:54:# Needs write access to /var/log/prosody for writing logs (depending on config)
/etc/systemd/system/multi-user.target.wants/prosody.service:57:# ReadWriteDirectories=/var/lib/prosody /var/log/prosody
/etc/systemd/system/multi-user.target.wants/prosody.service:59:# ReadOnlyDirectories=/usr /etc/prosody
/etc/systemd/system/multi-user.target.wants/civitas.service:3:After=network-online.target jitsi-videobridge2.service jicofo.service prosody.service docker.service
/etc/systemd/system/multi-user.target.wants/civitas.service:5:Wants=jitsi-videobridge2.service jicofo.service
/etc/passwd:39:jvb:x:997:1001::/usr/share/jitsi-videobridge:/bin/bash
/etc/passwd:40:jicofo:x:996:1001::/usr/share/jicofo:/bin/bash
/etc/passwd:41:prosody:x:111:115:Prosody XMPP Server:/var/lib/prosody:/usr/sbin/nologin
/etc/shadow-:40:jicofo:!:20535::::::
/etc/shadow-:41:prosody:!:20535::::::
/etc/dictionaries-common/words:10503:bosh
/etc/dictionaries-common/words:10504:bosh's
/etc/dictionaries-common/words:50443:kibosh
/etc/dictionaries-common/words:50444:kibosh's
/etc/dictionaries-common/words:72708:prosody
/etc/dictionaries-common/words:72709:prosody's
/etc/group:68:jitsi:x:1001:
/etc/group:69:prosody:x:115:
/etc/rc1.d/K01jicofo:3:# INIT script for Jitsi Conference Focus
/etc/rc1.d/K01jicofo:4:# Version: 1.0  4-Dec-2014  pawel.domas@jitsi.org
/etc/rc1.d/K01jicofo:7:# Provides:          jicofo
/etc/rc1.d/K01jicofo:12:# Short-Description: Jitsi conference Focus
/etc/rc1.d/K01jicofo:13:# Description:       Conference focus for Jitsi Meet application.
/etc/rc1.d/K01jicofo:18:# Include jicofo defaults if available
/etc/rc1.d/K01jicofo:19:if [ -f /etc/jitsi/jicofo/config ]; then
/etc/rc1.d/K01jicofo:20:    . /etc/jitsi/jicofo/config
/etc/rc1.d/K01jicofo:24:DAEMON=/usr/share/jicofo/jicofo.sh
/etc/rc1.d/K01jicofo:25:DAEMON_DIR=/usr/share/jicofo/
/etc/rc1.d/K01jicofo:26:NAME=jicofo
/etc/rc1.d/K01jicofo:27:USER=jicofo
/etc/rc1.d/K01jicofo:28:PIDFILE=/var/run/jicofo.pid
/etc/rc1.d/K01jicofo:29:LOGFILE=/var/log/jitsi/jicofo.log
/etc/rc1.d/K01jicofo:30:DESC=jicofo
/etc/rc1.d/K01jicofo:60:    export JICOFO_AUTH_PASSWORD JICOFO_MAX_MEMORY
/etc/rc1.d/K01jicofo:62:        --exec /bin/bash -- -c "cd $DAEMON_DIR; JAVA_SYS_PROPS=\"$JAVA_SYS_PROPS\" exec $DAEMON $JICOFO_OPTS < /dev/null >> $LOGFILE 2>&1"
/etc/rc1.d/K01prosody:4:# Provides:             prosody
/etc/rc1.d/K01prosody:11:# Short-Description:    Prosody XMPP Server
/etc/rc1.d/K01prosody:16:# /etc/init.d/prosody: start and stop Prosody XMPP server
/etc/rc1.d/K01prosody:18:USER=prosody
/etc/rc1.d/K01prosody:19:DAEMON=/usr/bin/prosody
/etc/rc1.d/K01prosody:20:PIDPATH=/run/prosody
/etc/rc1.d/K01prosody:21:PIDFILE="$PIDPATH"/prosody.pid
/etc/rc1.d/K01prosody:32:if [ -f /etc/default/prosody ] ; then
/etc/rc1.d/K01prosody:33:    . /etc/default/prosody
/etc/rc1.d/K01prosody:42:start_prosody () {
/etc/rc1.d/K01prosody:44:	chown prosody:adm "$(dirname $PIDFILE)"
/etc/rc1.d/K01prosody:56:stop_prosody () {
/etc/rc1.d/K01prosody:66:signal_prosody () {
/etc/rc1.d/K01prosody:78:	log_daemon_msg "Starting Prosody XMPP Server" "prosody"
/etc/rc1.d/K01prosody:79:	if start_prosody; then
/etc/rc1.d/K01prosody:86:  	log_daemon_msg "Stopping Prosody XMPP Server" "prosody"
/etc/rc1.d/K01prosody:87:  	if stop_prosody; then
/etc/rc1.d/K01prosody:94:  	log_daemon_msg "Restarting Prosody XMPP Server" "prosody"
/etc/rc1.d/K01prosody:96:  	stop_prosody
/etc/rc1.d/K01prosody:98:	if start_prosody; then
/etc/rc1.d/K01prosody:105:  	log_daemon_msg "Reloading Prosody XMPP Server" "prosody"
/etc/rc1.d/K01prosody:107:	if signal_prosody 1; then
/etc/rc1.d/K01prosody:114:	log_daemon_msg "Status of Prosody XMPP Server" "prosody "
/etc/rc1.d/K01prosody:118:  	log_action_msg "Usage: /etc/init.d/prosody {start|stop|restart|reload|status}"
/etc/rc0.d/K01jicofo:3:# INIT script for Jitsi Conference Focus
/etc/rc0.d/K01jicofo:4:# Version: 1.0  4-Dec-2014  pawel.domas@jitsi.org
/etc/rc0.d/K01jicofo:7:# Provides:          jicofo
/etc/rc0.d/K01jicofo:12:# Short-Description: Jitsi conference Focus
/etc/rc0.d/K01jicofo:13:# Description:       Conference focus for Jitsi Meet application.
/etc/rc0.d/K01jicofo:18:# Include jicofo defaults if available
/etc/rc0.d/K01jicofo:19:if [ -f /etc/jitsi/jicofo/config ]; then
/etc/rc0.d/K01jicofo:20:    . /etc/jitsi/jicofo/config
/etc/rc0.d/K01jicofo:24:DAEMON=/usr/share/jicofo/jicofo.sh
/etc/rc0.d/K01jicofo:25:DAEMON_DIR=/usr/share/jicofo/
/etc/rc0.d/K01jicofo:26:NAME=jicofo
/etc/rc0.d/K01jicofo:27:USER=jicofo
/etc/rc0.d/K01jicofo:28:PIDFILE=/var/run/jicofo.pid
/etc/rc0.d/K01jicofo:29:LOGFILE=/var/log/jitsi/jicofo.log
/etc/rc0.d/K01jicofo:30:DESC=jicofo
/etc/rc0.d/K01jicofo:60:    export JICOFO_AUTH_PASSWORD JICOFO_MAX_MEMORY
/etc/rc0.d/K01jicofo:62:        --exec /bin/bash -- -c "cd $DAEMON_DIR; JAVA_SYS_PROPS=\"$JAVA_SYS_PROPS\" exec $DAEMON $JICOFO_OPTS < /dev/null >> $LOGFILE 2>&1"
/etc/rc0.d/K01prosody:4:# Provides:             prosody
/etc/rc0.d/K01prosody:11:# Short-Description:    Prosody XMPP Server
/etc/rc0.d/K01prosody:16:# /etc/init.d/prosody: start and stop Prosody XMPP server
/etc/rc0.d/K01prosody:18:USER=prosody
/etc/rc0.d/K01prosody:19:DAEMON=/usr/bin/prosody
/etc/rc0.d/K01prosody:20:PIDPATH=/run/prosody
/etc/rc0.d/K01prosody:21:PIDFILE="$PIDPATH"/prosody.pid
/etc/rc0.d/K01prosody:32:if [ -f /etc/default/prosody ] ; then
/etc/rc0.d/K01prosody:33:    . /etc/default/prosody
/etc/rc0.d/K01prosody:42:start_prosody () {
/etc/rc0.d/K01prosody:44:	chown prosody:adm "$(dirname $PIDFILE)"
/etc/rc0.d/K01prosody:56:stop_prosody () {
/etc/rc0.d/K01prosody:66:signal_prosody () {
/etc/rc0.d/K01prosody:78:	log_daemon_msg "Starting Prosody XMPP Server" "prosody"
/etc/rc0.d/K01prosody:79:	if start_prosody; then
/etc/rc0.d/K01prosody:86:  	log_daemon_msg "Stopping Prosody XMPP Server" "prosody"
/etc/rc0.d/K01prosody:87:  	if stop_prosody; then
/etc/rc0.d/K01prosody:94:  	log_daemon_msg "Restarting Prosody XMPP Server" "prosody"
/etc/rc0.d/K01prosody:96:  	stop_prosody
/etc/rc0.d/K01prosody:98:	if start_prosody; then
/etc/rc0.d/K01prosody:105:  	log_daemon_msg "Reloading Prosody XMPP Server" "prosody"
/etc/rc0.d/K01prosody:107:	if signal_prosody 1; then
/etc/rc0.d/K01prosody:114:	log_daemon_msg "Status of Prosody XMPP Server" "prosody "
/etc/rc0.d/K01prosody:118:  	log_action_msg "Usage: /etc/init.d/prosody {start|stop|restart|reload|status}"
/etc/rc6.d/K01jicofo:3:# INIT script for Jitsi Conference Focus
/etc/rc6.d/K01jicofo:4:# Version: 1.0  4-Dec-2014  pawel.domas@jitsi.org
/etc/rc6.d/K01jicofo:7:# Provides:          jicofo
/etc/rc6.d/K01jicofo:12:# Short-Description: Jitsi conference Focus
/etc/rc6.d/K01jicofo:13:# Description:       Conference focus for Jitsi Meet application.
/etc/rc6.d/K01jicofo:18:# Include jicofo defaults if available
/etc/rc6.d/K01jicofo:19:if [ -f /etc/jitsi/jicofo/config ]; then
/etc/rc6.d/K01jicofo:20:    . /etc/jitsi/jicofo/config
/etc/rc6.d/K01jicofo:24:DAEMON=/usr/share/jicofo/jicofo.sh
/etc/rc6.d/K01jicofo:25:DAEMON_DIR=/usr/share/jicofo/
/etc/rc6.d/K01jicofo:26:NAME=jicofo
/etc/rc6.d/K01jicofo:27:USER=jicofo
/etc/rc6.d/K01jicofo:28:PIDFILE=/var/run/jicofo.pid
/etc/rc6.d/K01jicofo:29:LOGFILE=/var/log/jitsi/jicofo.log
/etc/rc6.d/K01jicofo:30:DESC=jicofo
/etc/rc6.d/K01jicofo:60:    export JICOFO_AUTH_PASSWORD JICOFO_MAX_MEMORY
/etc/rc6.d/K01jicofo:62:        --exec /bin/bash -- -c "cd $DAEMON_DIR; JAVA_SYS_PROPS=\"$JAVA_SYS_PROPS\" exec $DAEMON $JICOFO_OPTS < /dev/null >> $LOGFILE 2>&1"
/etc/rc6.d/K01prosody:4:# Provides:             prosody
/etc/rc6.d/K01prosody:11:# Short-Description:    Prosody XMPP Server
/etc/rc6.d/K01prosody:16:# /etc/init.d/prosody: start and stop Prosody XMPP server
/etc/rc6.d/K01prosody:18:USER=prosody
/etc/rc6.d/K01prosody:19:DAEMON=/usr/bin/prosody
/etc/rc6.d/K01prosody:20:PIDPATH=/run/prosody
/etc/rc6.d/K01prosody:21:PIDFILE="$PIDPATH"/prosody.pid
/etc/rc6.d/K01prosody:32:if [ -f /etc/default/prosody ] ; then
/etc/rc6.d/K01prosody:33:    . /etc/default/prosody
/etc/rc6.d/K01prosody:42:start_prosody () {
/etc/rc6.d/K01prosody:44:	chown prosody:adm "$(dirname $PIDFILE)"
/etc/rc6.d/K01prosody:56:stop_prosody () {
/etc/rc6.d/K01prosody:66:signal_prosody () {
/etc/rc6.d/K01prosody:78:	log_daemon_msg "Starting Prosody XMPP Server" "prosody"
/etc/rc6.d/K01prosody:79:	if start_prosody; then
/etc/rc6.d/K01prosody:86:  	log_daemon_msg "Stopping Prosody XMPP Server" "prosody"
/etc/rc6.d/K01prosody:87:  	if stop_prosody; then
/etc/rc6.d/K01prosody:94:  	log_daemon_msg "Restarting Prosody XMPP Server" "prosody"
/etc/rc6.d/K01prosody:96:  	stop_prosody
/etc/rc6.d/K01prosody:98:	if start_prosody; then
/etc/rc6.d/K01prosody:105:  	log_daemon_msg "Reloading Prosody XMPP Server" "prosody"
/etc/rc6.d/K01prosody:107:	if signal_prosody 1; then
/etc/rc6.d/K01prosody:114:	log_daemon_msg "Status of Prosody XMPP Server" "prosody "
/etc/rc6.d/K01prosody:118:  	log_action_msg "Usage: /etc/init.d/prosody {start|stop|restart|reload|status}"
/etc/logrotate.d/prosody:1:/var/log/prosody/prosody.log /var/log/prosody/prosody.err {
/etc/logrotate.d/prosody:6:	create 640 prosody adm
/etc/logrotate.d/prosody:8:		[ ! -e /run/prosody/prosody.pid ] || service prosody reload > /dev/null
/etc/logrotate.d/jicofo:1:/var/log/jitsi/jicofo.log {
/etc/logrotate.d/jicofo:9:  su jicofo jitsi
/etc/logrotate.d/jitsi-videobridge:1:/var/log/jitsi/jvb.log {
/etc/logrotate.d/jitsi-videobridge:10:  su jvb jitsi
/etc/apt/sources.list.d/jitsi-stable.list:1:deb [signed-by=/etc/apt/keyrings/jitsi.gpg] https://download.jitsi.org stable/



---

# 30. ARBRE DE L'INSTALLATION

**Date :** 2026-08-08 06:56:39 EDT


## /etc/jitsi


```text
$ tree -a -L 6 /etc/jitsi 2>/dev/null || find /etc/jitsi -maxdepth 6 -print 2>/dev/null | sort
```
/etc/jitsi
├── jicofo
│   ├── config
│   ├── jicofo.conf
│   └── logging.properties
├── meet
│   └── meet.civitas.local-config.js
└── videobridge
    ├── config
    ├── jvb.conf
    └── logging.properties

4 directories, 7 files


## /etc/prosody


```text
$ tree -a -L 6 /etc/prosody 2>/dev/null || find /etc/prosody -maxdepth 6 -print 2>/dev/null | sort
```
/etc/prosody
├── certs
│   ├── auth.meet.civitas.local.crt -> /var/lib/prosody/auth.meet.civitas.local.crt
│   ├── auth.meet.civitas.local.key -> /var/lib/prosody/auth.meet.civitas.local.key
│   ├── meet.civitas.local.crt -> /var/lib/prosody/meet.civitas.local.crt
│   └── meet.civitas.local.key -> /var/lib/prosody/meet.civitas.local.key
├── conf.avail
│   ├── example.com.cfg.lua
│   ├── jaas.cfg.lua
│   ├── localhost.cfg.lua
│   └── meet.civitas.local.cfg.lua
├── conf.d
│   ├── localhost.cfg.lua -> ../conf.avail/localhost.cfg.lua
│   └── meet.civitas.local.cfg.lua
├── migrator.cfg.lua
├── prosody.cfg.lua
└── README

4 directories, 13 files


## /usr/share/jitsi-meet


```text
$ tree -a -L 4 /usr/share/jitsi-meet 2>/dev/null || find /usr/share/jitsi-meet -maxdepth 4 -print 2>/dev/null | sort
```
/usr/share/jitsi-meet
├── base.html
├── body.html
├── css
│   └── all.css
├── fonts
│   └── .placeholder
├── fonts.html
├── head.html
├── images
│   ├── apple-touch-icon.png
│   ├── app-store-badge.png
│   ├── avatar.png
│   ├── btn_google_signin_dark_normal.png
│   ├── calendar.svg
│   ├── chromeLogo.svg
│   ├── downloadLocalRecording.png
│   ├── dropboxLogo_square.png
│   ├── favicon.svg
│   ├── f-droid-badge.png
│   ├── flags@2x.png
│   ├── flags.png
│   ├── GIPHY_icon.png
│   ├── GIPHY_logo.png
│   ├── googleLogo.svg
│   ├── google-play-badge.png
│   ├── icon-cloud.png
│   ├── icon-info.png
│   ├── icon-users.png
│   ├── jitsilogo.png
│   ├── logo-deep-linking-mobile.png
│   ├── logo-deep-linking.png
│   ├── microsoftLogo.svg
│   ├── share-audio.gif
│   ├── virtual-background
│   │   ├── background-1.jpg
│   │   ├── background-2.jpg
│   │   ├── background-3.jpg
│   │   ├── background-4.jpg
│   │   ├── background-5.jpg
│   │   ├── background-6.jpg
│   │   └── background-7.jpg
│   ├── watermark.svg
│   └── welcome-background.png
├── index.html
├── interface_config.js
├── lang
│   ├── countries-af.json
│   ├── countries-ar.json
│   ├── countries-be.json
│   ├── countries-bg.json
│   ├── countries-ca.json
│   ├── countries-cs.json
│   ├── countries-da.json
│   ├── countries-de.json
│   ├── countries-el.json
│   ├── countries-en.json
│   ├── countries-es.json
│   ├── countries-es-US.json
│   ├── countries-et.json
│   ├── countries-eu.json
│   ├── countries-fa.json
│   ├── countries-fi.json
│   ├── countries-fr-CA.json
│   ├── countries-fr.json
│   ├── countries-gl.json
│   ├── countries-he.json
│   ├── countries-hi.json
│   ├── countries-hr.json
│   ├── countries-hu.json
│   ├── countries-hy.json
│   ├── countries-id.json
│   ├── countries-is.json
│   ├── countries-it.json
│   ├── countries-ja.json
│   ├── countries-kab.json
│   ├── countries-kk.json
│   ├── countries-ko.json
│   ├── countries-lt.json
│   ├── countries-lv.json
│   ├── countries-ml.json
│   ├── countries-mn.json
│   ├── countries-nb.json
│   ├── countries-nl.json
│   ├── countries-no.json
│   ├── countries-pl.json
│   ├── countries-pt-BR.json
│   ├── countries-pt.json
│   ├── countries-ro.json
│   ├── countries-ru.json
│   ├── countries-sk.json
│   ├── countries-sl.json
│   ├── countries-sq.json
│   ├── countries-sr.json
│   ├── countries-sv.json
│   ├── countries-tr.json
│   ├── countries-uk.json
│   ├── countries-vi.json
│   ├── countries-zh-CN.json
│   ├── countries-zh-TW.json
│   ├── languages.json
│   ├── main-af.json
│   ├── main-ar.json
│   ├── main-be.json
│   ├── main-bg.json
│   ├── main-ca.json
│   ├── main-cs.json
│   ├── main-da.json
│   ├── main-de.json
│   ├── main-dsb.json
│   ├── main-el.json
│   ├── main-eo.json
│   ├── main-es.json
│   ├── main-es-US.json
│   ├── main-et.json
│   ├── main-eu.json
│   ├── main-fa.json
│   ├── main-fi.json
│   ├── main-fr-CA.json
│   ├── main-fr.json
│   ├── main-gl.json
│   ├── main-he.json
│   ├── main-hi.json
│   ├── main-hr.json
│   ├── main-hsb.json
│   ├── main-hu.json
│   ├── main-hy.json
│   ├── main-id.json
│   ├── main-is.json
│   ├── main-it.json
│   ├── main-ja.json
│   ├── main.json
│   ├── main-kab.json
│   ├── main-kk.json
│   ├── main-ko.json
│   ├── main-lt.json
│   ├── main-lv.json
│   ├── main-ml.json
│   ├── main-mn.json
│   ├── main-mr.json
│   ├── main-nb.json
│   ├── main-nl.json
│   ├── main-no.json
│   ├── main-oc.json
│   ├── main-pl.json
│   ├── main-pt-BR.json
│   ├── main-pt.json
│   ├── main-ro.json
│   ├── main-ru.json
│   ├── main-sc.json
│   ├── main-sk.json
│   ├── main-sl.json
│   ├── main-sq.json
│   ├── main-sr.json
│   ├── main-sv.json
│   ├── main-te.json
│   ├── main-tr.json
│   ├── main-uk.json
│   ├── main-vi.json
│   ├── main-zh-CN.json
│   ├── main-zh-TW.json
│   ├── readme.md
│   ├── translation-languages.json
│   └── update-translation.js
├── libs
│   ├── alwaysontop.min.js
│   ├── alwaysontop.min.js.map
│   ├── app.bundle.min.js
│   ├── app.bundle.min.js.map
│   ├── blazeface-front.bin
│   ├── blazeface-front.json
│   ├── chunks
│   │   ├── 1060.min.js
│   │   ├── 1060.min.js.map
│   │   ├── 1080.min.js
│   │   ├── 1080.min.js.map
│   │   ├── 1121.min.js
│   │   ├── 1121.min.js.map
│   │   ├── 1329.min.js
│   │   ├── 1329.min.js.map
│   │   ├── 141.min.js
│   │   ├── 141.min.js.map
│   │   ├── 1455.min.js
│   │   ├── 1455.min.js.map
│   │   ├── 1489.min.js
│   │   ├── 1489.min.js.map
│   │   ├── 167.min.js
│   │   ├── 167.min.js.map
│   │   ├── 1689.min.js
│   │   ├── 1689.min.js.map
│   │   ├── 1818.min.js
│   │   ├── 1818.min.js.LICENSE.txt
│   │   ├── 1818.min.js.map
│   │   ├── 1987.min.js
│   │   ├── 1987.min.js.map
│   │   ├── 2130.min.js
│   │   ├── 2130.min.js.map
│   │   ├── 2144.min.js
│   │   ├── 2144.min.js.map
│   │   ├── 2203.min.js
│   │   ├── 2203.min.js.map
│   │   ├── 239.min.js
│   │   ├── 239.min.js.map
│   │   ├── 247.min.js
│   │   ├── 247.min.js.map
│   │   ├── 2603.min.js
│   │   ├── 2603.min.js.map
│   │   ├── 2725.min.js
│   │   ├── 2725.min.js.map
│   │   ├── 2775.min.js
│   │   ├── 2775.min.js.map
│   │   ├── 2783.min.js
│   │   ├── 2803.min.js
│   │   ├── 2803.min.js.map
│   │   ├── 2886.min.js
│   │   ├── 2886.min.js.map
│   │   ├── 3138.min.js
│   │   ├── 3138.min.js.map
│   │   ├── 3207.min.js
│   │   ├── 3207.min.js.map
│   │   ├── 3259.min.js
│   │   ├── 3259.min.js.map
│   │   ├── 3292.min.js
│   │   ├── 3292.min.js.map
│   │   ├── 3347.min.js
│   │   ├── 3347.min.js.map
│   │   ├── 3417.min.js
│   │   ├── 3417.min.js.map
│   │   ├── 3471.min.js
│   │   ├── 3471.min.js.map
│   │   ├── 3567.min.js
│   │   ├── 3567.min.js.map
│   │   ├── 3645.min.js
│   │   ├── 3645.min.js.map
│   │   ├── 3659.min.js
│   │   ├── 3659.min.js.map
│   │   ├── 3687.min.js
│   │   ├── 3687.min.js.map
│   │   ├── 3760.min.js
│   │   ├── 4073.min.js
│   │   ├── 4073.min.js.map
│   │   ├── 4104.min.js
│   │   ├── 4104.min.js.map
│   │   ├── 4106.min.js
│   │   ├── 4106.min.js.map
│   │   ├── 4130.min.js
│   │   ├── 4130.min.js.map
│   │   ├── 4207.min.js
│   │   ├── 4207.min.js.map
│   │   ├── 4226.min.js
│   │   ├── 4226.min.js.map
│   │   ├── 4256.min.js
│   │   ├── 4256.min.js.map
│   │   ├── 4259.min.js
│   │   ├── 4259.min.js.map
│   │   ├── 4337.min.js
│   │   ├── 4337.min.js.LICENSE.txt
│   │   ├── 4337.min.js.map
│   │   ├── 4564.min.js
│   │   ├── 4564.min.js.map
│   │   ├── 4690.min.js
│   │   ├── 4690.min.js.map
│   │   ├── 4695.min.js
│   │   ├── 4695.min.js.map
│   │   ├── 475.min.js
│   │   ├── 475.min.js.LICENSE.txt
│   │   ├── 475.min.js.map
│   │   ├── 4762.min.js
│   │   ├── 4762.min.js.map
│   │   ├── 493.min.js
│   │   ├── 493.min.js.map
│   │   ├── 5114.min.js
│   │   ├── 5114.min.js.map
│   │   ├── 5163.min.js
│   │   ├── 5163.min.js.map
│   │   ├── 5301.min.js
│   │   ├── 5301.min.js.map
│   │   ├── 5322.min.js
│   │   ├── 5322.min.js.map
│   │   ├── 5388.min.js
│   │   ├── 5388.min.js.map
│   │   ├── 544.min.js
│   │   ├── 544.min.js.map
│   │   ├── 547.min.js
│   │   ├── 547.min.js.map
│   │   ├── 5544.min.js
│   │   ├── 5544.min.js.map
│   │   ├── 5628.min.js
│   │   ├── 5628.min.js.map
│   │   ├── 5713.min.js
│   │   ├── 5713.min.js.map
│   │   ├── 5857.min.js
│   │   ├── 5857.min.js.map
│   │   ├── 5860.min.js
│   │   ├── 5860.min.js.map
│   │   ├── 5950.min.js
│   │   ├── 5950.min.js.map
│   │   ├── 6220.min.js
│   │   ├── 6220.min.js.map
│   │   ├── 6322.min.js
│   │   ├── 6322.min.js.map
│   │   ├── 6586.min.js
│   │   ├── 6586.min.js.map
│   │   ├── 6625.min.js
│   │   ├── 6625.min.js.map
│   │   ├── 6675.min.js
│   │   ├── 6675.min.js.map
│   │   ├── 6770.min.js
│   │   ├── 6770.min.js.map
│   │   ├── 7115.min.js
│   │   ├── 7115.min.js.map
│   │   ├── 7134.min.js
│   │   ├── 7134.min.js.map
│   │   ├── 7185.min.js
│   │   ├── 7185.min.js.map
│   │   ├── 7256.min.js
│   │   ├── 7256.min.js.map
│   │   ├── 7358.min.js
│   │   ├── 7358.min.js.map
│   │   ├── 7690.min.js
│   │   ├── 7690.min.js.map
│   │   ├── 7897.min.js
│   │   ├── 7897.min.js.map
│   │   ├── 7899.min.js
│   │   ├── 7899.min.js.map
│   │   ├── 796.min.js
│   │   ├── 796.min.js.map
│   │   ├── 8005.min.js
│   │   ├── 8005.min.js.map
│   │   ├── 8024.min.js
│   │   ├── 8024.min.js.map
│   │   ├── 8032.min.js
│   │   ├── 8090.min.js
│   │   ├── 8090.min.js.map
│   │   ├── 8146.min.js
│   │   ├── 8146.min.js.map
│   │   ├── 8298.min.js
│   │   ├── 8298.min.js.map
│   │   ├── 8528.min.js
│   │   ├── 8528.min.js.map
│   │   ├── 8846.min.js
│   │   ├── 8846.min.js.map
│   │   ├── 8882.min.js
│   │   ├── 8882.min.js.map
│   │   ├── 8890.min.js
│   │   ├── 8890.min.js.map
│   │   ├── 8989.min.js
│   │   ├── 8989.min.js.map
│   │   ├── 8995.min.js
│   │   ├── 8995.min.js.map
│   │   ├── 9013.min.js
│   │   ├── 9013.min.js.map
│   │   ├── 9105.min.js
│   │   ├── 9105.min.js.map
│   │   ├── 922.min.js
│   │   ├── 922.min.js.map
│   │   ├── 9596.min.js
│   │   ├── 9612.min.js
│   │   ├── 9612.min.js.map
│   │   ├── 9698.min.js
│   │   ├── 9698.min.js.map
│   │   ├── 9706.min.js
│   │   ├── 9706.min.js.map
│   │   ├── 971.min.js
│   │   ├── 971.min.js.map
│   │   ├── 9828.min.js
│   │   ├── 9828.min.js.map
│   │   ├── 9890.min.js
│   │   ├── 9890.min.js.map
│   │   ├── 9976.min.js
│   │   └── 9976.min.js.map
│   ├── close3.min.js
│   ├── emotion.bin
│   ├── emotion.json
│   ├── excalidraw
│   │   └── fonts
│   │       ├── Assistant
│   │       ├── Cascadia
│   │       ├── ComicShanns
│   │       ├── Excalifont
│   │       ├── Liberation
│   │       ├── Lilita
│   │       ├── Nunito
│   │       ├── Virgil
│   │       └── Xiaolai
│   ├── external_api.min.js
│   ├── external_api.min.js.map
│   ├── face-landmarks-worker.min.js
│   ├── face-landmarks-worker.min.js.map
│   ├── lib-jitsi-meet.e2ee-worker.js
│   ├── lib-jitsi-meet.min.js
│   ├── lib-jitsi-meet.min.js.LICENSE.txt
│   ├── lib-jitsi-meet.min.map
│   ├── mediapipe-segmentation
│   │   ├── selfie_segmentation.binarypb
│   │   ├── selfie_segmentation.js
│   │   ├── selfie_segmentation_landscape.tflite
│   │   ├── selfie_segmentation_solution_simd_wasm_bin.data
│   │   ├── selfie_segmentation_solution_simd_wasm_bin.js
│   │   ├── selfie_segmentation_solution_simd_wasm_bin.wasm
│   │   ├── selfie_segmentation_solution_wasm_bin.js
│   │   ├── selfie_segmentation_solution_wasm_bin.wasm
│   │   └── selfie_segmentation.tflite
│   ├── noise-suppressor-worklet.min.js
│   ├── noise-suppressor-worklet.min.js.map
│   ├── olm.wasm
│   ├── rnnoise.wasm
│   ├── screenshot-capture-worker.min.js
│   ├── screenshot-capture-worker.min.js.map
│   ├── selfie_segmentation_landscape.tflite
│   ├── tfjs-backend-wasm-simd.wasm
│   ├── tfjs-backend-wasm-threaded-simd.wasm
│   ├── tfjs-backend-wasm.wasm
│   ├── tflite-simd.wasm
│   ├── tflite.wasm
│   ├── vb-inference-worker.min.js
│   └── vb-inference-worker.min.js.map
├── manifest.json
├── plugin.head.html
├── prosody-plugins
│   ├── luajwtjitsi.lib.lua
│   ├── mod_audio_translation_component.lua
│   ├── mod_auth_jitsi-anonymous.lua
│   ├── mod_auth_jitsi-shared-secret.lua
│   ├── mod_auth_token.lua
│   ├── mod_av_moderation_component.lua
│   ├── mod_certs_s2soutinjection.lua
│   ├── mod_client_proxy.lua
│   ├── mod_conference_duration.lua
│   ├── mod_debug_traceback.lua
│   ├── mod_end_conference.lua
│   ├── mod_features_identity.lua
│   ├── mod_filesharing_component.lua
│   ├── mod_filter_iq_jibri.lua
│   ├── mod_filter_iq_rayo.lua
│   ├── mod_filter_messages.lua
│   ├── mod_firewall
│   │   ├── actions.lib.lua
│   │   ├── conditions.lib.lua
│   │   ├── definitions.lib.lua
│   │   ├── marks.lib.lua
│   │   ├── mod_firewall.lua
│   │   └── test.lib.lua
│   ├── mod_fmuc.lua
│   ├── mod_jibri_session.lua
│   ├── mod_jiconop.lua
│   ├── mod_jitsi_permissions.lua
│   ├── mod_jitsi_session.lua
│   ├── mod_limits_exception.lua
│   ├── mod_log_ringbuffer.lua
│   ├── mod_measure_message_count.lua
│   ├── mod_measure_stanza_counts.lua
│   ├── mod_muc_allowners.lua
│   ├── mod_muc_auth_ban.lua
│   ├── mod_muc_breakout_rooms.lua
│   ├── mod_muc_census.lua
│   ├── mod_muc_cleanup_backend_services.lua
│   ├── mod_muc_displayname.lua
│   ├── mod_muc_domain_mapper.lua
│   ├── mod_muc_end_meeting.lua
│   ├── mod_muc_filter_access.lua
│   ├── mod_muc_flip.lua
│   ├── mod_muc_hide_all.lua
│   ├── mod_muc_jigasi_invite.lua
│   ├── mod_muc_kick_participant.lua
│   ├── mod_muc_limit_messages.lua
│   ├── mod_muc_lobby_rooms.lua
│   ├── mod_muc_max_occupants.lua
│   ├── mod_muc_meeting_id.lua
│   ├── mod_muc_password_check.lua
│   ├── mod_muc_password_whitelist.lua
│   ├── mod_muc_rate_limit.lua
│   ├── mod_muc_resource_validate.lua
│   ├── mod_muc_size.lua
│   ├── mod_muc_wait_for_host.lua
│   ├── mod_muc_webhook.lua
│   ├── mod_persistent_lobby.lua
│   ├── mod_polls_component.lua
│   ├── mod_presence_identity.lua
│   ├── mod_rate_limit.lua
│   ├── mod_reservations.lua
│   ├── mod_room_destroy.lua
│   ├── mod_room_metadata_component.lua
│   ├── mod_roster_command.lua
│   ├── mod_roster_command.patch
│   ├── mod_s2sout_override.lua
│   ├── mod_s2s_whitelist.lua
│   ├── mod_secure_interfaces.lua
│   ├── mod_short_lived_token.lua
│   ├── mod_speakerstats_component.lua
│   ├── mod_system_chat_message.lua
│   ├── mod_test_observer_http.lua
│   ├── mod_test_observer.lua
│   ├── mod_token_affiliation.lua
│   ├── mod_token_verification.lua
│   ├── mod_turncredentials_http.lua
│   ├── mod_visitors_component.lua
│   ├── mod_visitors.lua
│   ├── muc_owner_allow_kick-0.12.patch
│   ├── README.md
│   ├── stanza_router_no-log.patch
│   ├── token
│   │   ├── jwk.lib.lua
│   │   └── util.lib.lua
│   └── util.lib.lua
├── pwa-worker.js
├── robots.txt
├── scripts
│   ├── coturn-le-update.sh
│   ├── encode-sound.sh
│   ├── install-letsencrypt-cert.sh
│   ├── lang-sort.sh
│   ├── move-to-jaas.sh
│   ├── register-jaas-account.sh
│   ├── update-asap-daily.sh
│   ├── update-ljm.sh
│   ├── update-mobile-rnsdk-version.sh
│   ├── update-mobile-sdk-version.sh
│   └── update-mobile-version.sh
├── sounds
│   ├── asked-unmute.mp3
│   ├── asked-unmute.opus
│   ├── e2eeOff_frCA.mp3
│   ├── e2eeOff_frCA.opus
│   ├── e2eeOff_fr.mp3
│   ├── e2eeOff_fr.opus
│   ├── e2eeOff.mp3
│   ├── e2eeOff.opus
│   ├── e2eeOn_frCA.mp3
│   ├── e2eeOn_frCA.opus
│   ├── e2eeOn_fr.mp3
│   ├── e2eeOn_fr.opus
│   ├── e2eeOn.mp3
│   ├── e2eeOn.opus
│   ├── incomingMessage.mp3
│   ├── incomingMessage.opus
│   ├── incomingMessage.wav
│   ├── joined.mp3
│   ├── joined.opus
│   ├── joined.wav
│   ├── knock.mp3
│   ├── knock.opus
│   ├── left.mp3
│   ├── left.opus
│   ├── left.wav
│   ├── liveStreamingOff_frCA.mp3
│   ├── liveStreamingOff_frCA.opus
│   ├── liveStreamingOff_fr.mp3
│   ├── liveStreamingOff_fr.opus
│   ├── liveStreamingOff.mp3
│   ├── liveStreamingOff.opus
│   ├── liveStreamingOn_frCA.mp3
│   ├── liveStreamingOn_frCA.opus
│   ├── liveStreamingOn_fr.mp3
│   ├── liveStreamingOn_fr.opus
│   ├── liveStreamingOn.mp3
│   ├── liveStreamingOn.opus
│   ├── noAudioSignal.mp3
│   ├── noAudioSignal.opus
│   ├── noisyAudioInput.mp3
│   ├── noisyAudioInput.opus
│   ├── outgoingRinging.mp3
│   ├── outgoingRinging.opus
│   ├── outgoingRinging.wav
│   ├── outgoingStart.mp3
│   ├── outgoingStart.opus
│   ├── outgoingStart.wav
│   ├── reactions-applause.mp3
│   ├── reactions-applause.opus
│   ├── reactions-boo.mp3
│   ├── reactions-boo.opus
│   ├── reactions-crickets.mp3
│   ├── reactions-crickets.opus
│   ├── reactions-laughter.mp3
│   ├── reactions-laughter.opus
│   ├── reactions-love.mp3
│   ├── reactions-love.opus
│   ├── reactions-raised-hand.mp3
│   ├── reactions-raised-hand.opus
│   ├── reactions-surprise.mp3
│   ├── reactions-surprise.opus
│   ├── reactions-thumbs-up.mp3
│   ├── reactions-thumbs-up.opus
│   ├── README.md
│   ├── recordingAndTranscriptionOff_frCA.mp3
│   ├── recordingAndTranscriptionOff_frCA.opus
│   ├── recordingAndTranscriptionOff_fr.mp3
│   ├── recordingAndTranscriptionOff_fr.opus
│   ├── recordingAndTranscriptionOff.mp3
│   ├── recordingAndTranscriptionOff.opus
│   ├── recordingAndTranscriptionOn_frCA.mp3
│   ├── recordingAndTranscriptionOn_frCA.opus
│   ├── recordingAndTranscriptionOn_fr.mp3
│   ├── recordingAndTranscriptionOn_fr.opus
│   ├── recordingAndTranscriptionOn.mp3
│   ├── recordingAndTranscriptionOn.opus
│   ├── recordingOff_frCA.mp3
│   ├── recordingOff_frCA.opus
│   ├── recordingOff_fr.mp3
│   ├── recordingOff_fr.opus
│   ├── recordingOff.mp3
│   ├── recordingOff.opus
│   ├── recordingOn_frCA.mp3
│   ├── recordingOn_frCA.opus
│   ├── recordingOn_fr.mp3
│   ├── recordingOn_fr.opus
│   ├── recordingOn.mp3
│   ├── recordingOn.opus
│   ├── rejected.mp3
│   ├── rejected.opus
│   ├── rejected.wav
│   ├── ring.mp3
│   ├── ring.opus
│   ├── ring.wav
│   ├── talkWhileMuted.mp3
│   ├── talkWhileMuted.opus
│   ├── transcriptionOff_frCA.mp3
│   ├── transcriptionOff_frCA.opus
│   ├── transcriptionOff_fr.mp3
│   ├── transcriptionOff_fr.opus
│   ├── transcriptionOff.mp3
│   ├── transcriptionOff.opus
│   ├── transcriptionOn_frCA.mp3
│   ├── transcriptionOn_frCA.opus
│   ├── transcriptionOn_fr.mp3
│   ├── transcriptionOn_fr.opus
│   ├── transcriptionOn.mp3
│   └── transcriptionOn.opus
├── static
│   ├── 404.html
│   ├── close2.html
│   ├── close3.html
│   ├── close3.js
│   ├── close.html
│   ├── close.js
│   ├── dialInInfo.html
│   ├── logout.html
│   ├── msredirect.html
│   ├── oauth.html
│   ├── offline.html
│   ├── planLimit.html
│   ├── prejoin.html
│   ├── pwa
│   │   └── icons
│   │       ├── icon192.png
│   │       ├── icon512.png
│   │       └── iconMask.png
│   ├── recommendedBrowsers.html
│   ├── settingsToolbarAdditionalContent.html
│   ├── sso.html
│   ├── webrtcUnsupported.html
│   ├── welcomePageAdditionalCard.html
│   ├── welcomePageAdditionalContent.html
│   └── whiteboard.html
└── title.html

28 directories, 627 files



---

# 31. FICHIERS FOURNIS PAR LES PAQUETS

**Date :** 2026-08-08 06:56:39 EDT


## Package : jitsi-meet


```text
$ dpkg -L 'jitsi-meet' 2>/dev/null || true
```
/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/jitsi-meet
/usr/share/doc/jitsi-meet/changelog.Debian.gz
/usr/share/doc/jitsi-meet/copyright


## Package : jitsi-meet-web


```text
$ dpkg -L 'jitsi-meet-web' 2>/dev/null || true
```
/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/jitsi-meet-web
/usr/share/doc/jitsi-meet-web/README.Debian
/usr/share/doc/jitsi-meet-web/README.md
/usr/share/doc/jitsi-meet-web/changelog.Debian.gz
/usr/share/doc/jitsi-meet-web/copyright
/usr/share/jitsi-meet
/usr/share/jitsi-meet/base.html
/usr/share/jitsi-meet/body.html
/usr/share/jitsi-meet/css
/usr/share/jitsi-meet/css/all.css
/usr/share/jitsi-meet/fonts
/usr/share/jitsi-meet/fonts/.placeholder
/usr/share/jitsi-meet/fonts.html
/usr/share/jitsi-meet/head.html
/usr/share/jitsi-meet/images
/usr/share/jitsi-meet/images/GIPHY_icon.png
/usr/share/jitsi-meet/images/GIPHY_logo.png
/usr/share/jitsi-meet/images/app-store-badge.png
/usr/share/jitsi-meet/images/apple-touch-icon.png
/usr/share/jitsi-meet/images/avatar.png
/usr/share/jitsi-meet/images/btn_google_signin_dark_normal.png
/usr/share/jitsi-meet/images/calendar.svg
/usr/share/jitsi-meet/images/chromeLogo.svg
/usr/share/jitsi-meet/images/downloadLocalRecording.png
/usr/share/jitsi-meet/images/dropboxLogo_square.png
/usr/share/jitsi-meet/images/f-droid-badge.png
/usr/share/jitsi-meet/images/favicon.svg
/usr/share/jitsi-meet/images/flags.png
/usr/share/jitsi-meet/images/flags@2x.png
/usr/share/jitsi-meet/images/google-play-badge.png
/usr/share/jitsi-meet/images/googleLogo.svg
/usr/share/jitsi-meet/images/icon-cloud.png
/usr/share/jitsi-meet/images/icon-info.png
/usr/share/jitsi-meet/images/icon-users.png
/usr/share/jitsi-meet/images/jitsilogo.png
/usr/share/jitsi-meet/images/logo-deep-linking-mobile.png
/usr/share/jitsi-meet/images/logo-deep-linking.png
/usr/share/jitsi-meet/images/microsoftLogo.svg
/usr/share/jitsi-meet/images/share-audio.gif
/usr/share/jitsi-meet/images/virtual-background
/usr/share/jitsi-meet/images/virtual-background/background-1.jpg
/usr/share/jitsi-meet/images/virtual-background/background-2.jpg
/usr/share/jitsi-meet/images/virtual-background/background-3.jpg
/usr/share/jitsi-meet/images/virtual-background/background-4.jpg
/usr/share/jitsi-meet/images/virtual-background/background-5.jpg
/usr/share/jitsi-meet/images/virtual-background/background-6.jpg
/usr/share/jitsi-meet/images/virtual-background/background-7.jpg
/usr/share/jitsi-meet/images/watermark.svg
/usr/share/jitsi-meet/images/welcome-background.png
/usr/share/jitsi-meet/index.html
/usr/share/jitsi-meet/interface_config.js
/usr/share/jitsi-meet/lang
/usr/share/jitsi-meet/lang/countries-af.json
/usr/share/jitsi-meet/lang/countries-ar.json
/usr/share/jitsi-meet/lang/countries-be.json
/usr/share/jitsi-meet/lang/countries-bg.json
/usr/share/jitsi-meet/lang/countries-ca.json
/usr/share/jitsi-meet/lang/countries-cs.json
/usr/share/jitsi-meet/lang/countries-da.json
/usr/share/jitsi-meet/lang/countries-de.json
/usr/share/jitsi-meet/lang/countries-el.json
/usr/share/jitsi-meet/lang/countries-en.json
/usr/share/jitsi-meet/lang/countries-es-US.json
/usr/share/jitsi-meet/lang/countries-es.json
/usr/share/jitsi-meet/lang/countries-et.json
/usr/share/jitsi-meet/lang/countries-eu.json
/usr/share/jitsi-meet/lang/countries-fa.json
/usr/share/jitsi-meet/lang/countries-fi.json
/usr/share/jitsi-meet/lang/countries-fr-CA.json
/usr/share/jitsi-meet/lang/countries-fr.json
/usr/share/jitsi-meet/lang/countries-gl.json
/usr/share/jitsi-meet/lang/countries-he.json
/usr/share/jitsi-meet/lang/countries-hi.json
/usr/share/jitsi-meet/lang/countries-hr.json
/usr/share/jitsi-meet/lang/countries-hu.json
/usr/share/jitsi-meet/lang/countries-hy.json
/usr/share/jitsi-meet/lang/countries-id.json
/usr/share/jitsi-meet/lang/countries-is.json
/usr/share/jitsi-meet/lang/countries-it.json
/usr/share/jitsi-meet/lang/countries-ja.json
/usr/share/jitsi-meet/lang/countries-kab.json
/usr/share/jitsi-meet/lang/countries-kk.json
/usr/share/jitsi-meet/lang/countries-ko.json
/usr/share/jitsi-meet/lang/countries-lt.json
/usr/share/jitsi-meet/lang/countries-lv.json
/usr/share/jitsi-meet/lang/countries-ml.json
/usr/share/jitsi-meet/lang/countries-mn.json
/usr/share/jitsi-meet/lang/countries-nb.json
/usr/share/jitsi-meet/lang/countries-nl.json
/usr/share/jitsi-meet/lang/countries-no.json
/usr/share/jitsi-meet/lang/countries-pl.json
/usr/share/jitsi-meet/lang/countries-pt-BR.json
/usr/share/jitsi-meet/lang/countries-pt.json
/usr/share/jitsi-meet/lang/countries-ro.json
/usr/share/jitsi-meet/lang/countries-ru.json
/usr/share/jitsi-meet/lang/countries-sk.json
/usr/share/jitsi-meet/lang/countries-sl.json
/usr/share/jitsi-meet/lang/countries-sq.json
/usr/share/jitsi-meet/lang/countries-sr.json
/usr/share/jitsi-meet/lang/countries-sv.json
/usr/share/jitsi-meet/lang/countries-tr.json
/usr/share/jitsi-meet/lang/countries-uk.json
/usr/share/jitsi-meet/lang/countries-vi.json
/usr/share/jitsi-meet/lang/countries-zh-CN.json
/usr/share/jitsi-meet/lang/countries-zh-TW.json
/usr/share/jitsi-meet/lang/languages.json
/usr/share/jitsi-meet/lang/main-af.json
/usr/share/jitsi-meet/lang/main-ar.json
/usr/share/jitsi-meet/lang/main-be.json
/usr/share/jitsi-meet/lang/main-bg.json
/usr/share/jitsi-meet/lang/main-ca.json
/usr/share/jitsi-meet/lang/main-cs.json
/usr/share/jitsi-meet/lang/main-da.json
/usr/share/jitsi-meet/lang/main-de.json
/usr/share/jitsi-meet/lang/main-dsb.json
/usr/share/jitsi-meet/lang/main-el.json
/usr/share/jitsi-meet/lang/main-eo.json
/usr/share/jitsi-meet/lang/main-es-US.json
/usr/share/jitsi-meet/lang/main-es.json
/usr/share/jitsi-meet/lang/main-et.json
/usr/share/jitsi-meet/lang/main-eu.json
/usr/share/jitsi-meet/lang/main-fa.json
/usr/share/jitsi-meet/lang/main-fi.json
/usr/share/jitsi-meet/lang/main-fr-CA.json
/usr/share/jitsi-meet/lang/main-fr.json
/usr/share/jitsi-meet/lang/main-gl.json
/usr/share/jitsi-meet/lang/main-he.json
/usr/share/jitsi-meet/lang/main-hi.json
/usr/share/jitsi-meet/lang/main-hr.json
/usr/share/jitsi-meet/lang/main-hsb.json
/usr/share/jitsi-meet/lang/main-hu.json
/usr/share/jitsi-meet/lang/main-hy.json
/usr/share/jitsi-meet/lang/main-id.json
/usr/share/jitsi-meet/lang/main-is.json
/usr/share/jitsi-meet/lang/main-it.json
/usr/share/jitsi-meet/lang/main-ja.json
/usr/share/jitsi-meet/lang/main-kab.json
/usr/share/jitsi-meet/lang/main-kk.json
/usr/share/jitsi-meet/lang/main-ko.json
/usr/share/jitsi-meet/lang/main-lt.json
/usr/share/jitsi-meet/lang/main-lv.json
/usr/share/jitsi-meet/lang/main-ml.json
/usr/share/jitsi-meet/lang/main-mn.json
/usr/share/jitsi-meet/lang/main-mr.json
/usr/share/jitsi-meet/lang/main-nb.json
/usr/share/jitsi-meet/lang/main-nl.json
/usr/share/jitsi-meet/lang/main-no.json
/usr/share/jitsi-meet/lang/main-oc.json
/usr/share/jitsi-meet/lang/main-pl.json
/usr/share/jitsi-meet/lang/main-pt-BR.json
/usr/share/jitsi-meet/lang/main-pt.json
/usr/share/jitsi-meet/lang/main-ro.json
/usr/share/jitsi-meet/lang/main-ru.json
/usr/share/jitsi-meet/lang/main-sc.json
/usr/share/jitsi-meet/lang/main-sk.json
/usr/share/jitsi-meet/lang/main-sl.json
/usr/share/jitsi-meet/lang/main-sq.json
/usr/share/jitsi-meet/lang/main-sr.json
/usr/share/jitsi-meet/lang/main-sv.json
/usr/share/jitsi-meet/lang/main-te.json
/usr/share/jitsi-meet/lang/main-tr.json
/usr/share/jitsi-meet/lang/main-uk.json
/usr/share/jitsi-meet/lang/main-vi.json
/usr/share/jitsi-meet/lang/main-zh-CN.json
/usr/share/jitsi-meet/lang/main-zh-TW.json
/usr/share/jitsi-meet/lang/main.json
/usr/share/jitsi-meet/lang/readme.md
/usr/share/jitsi-meet/lang/translation-languages.json
/usr/share/jitsi-meet/lang/update-translation.js
/usr/share/jitsi-meet/libs
/usr/share/jitsi-meet/libs/alwaysontop.min.js
/usr/share/jitsi-meet/libs/alwaysontop.min.js.map
/usr/share/jitsi-meet/libs/app.bundle.min.js
/usr/share/jitsi-meet/libs/app.bundle.min.js.map
/usr/share/jitsi-meet/libs/blazeface-front.bin
/usr/share/jitsi-meet/libs/blazeface-front.json
/usr/share/jitsi-meet/libs/chunks
/usr/share/jitsi-meet/libs/chunks/1060.min.js
/usr/share/jitsi-meet/libs/chunks/1060.min.js.map
/usr/share/jitsi-meet/libs/chunks/1080.min.js
/usr/share/jitsi-meet/libs/chunks/1080.min.js.map
/usr/share/jitsi-meet/libs/chunks/1121.min.js
/usr/share/jitsi-meet/libs/chunks/1121.min.js.map
/usr/share/jitsi-meet/libs/chunks/1329.min.js
/usr/share/jitsi-meet/libs/chunks/1329.min.js.map
/usr/share/jitsi-meet/libs/chunks/141.min.js
/usr/share/jitsi-meet/libs/chunks/141.min.js.map
/usr/share/jitsi-meet/libs/chunks/1455.min.js
/usr/share/jitsi-meet/libs/chunks/1455.min.js.map
/usr/share/jitsi-meet/libs/chunks/1489.min.js
/usr/share/jitsi-meet/libs/chunks/1489.min.js.map
/usr/share/jitsi-meet/libs/chunks/167.min.js
/usr/share/jitsi-meet/libs/chunks/167.min.js.map
/usr/share/jitsi-meet/libs/chunks/1689.min.js
/usr/share/jitsi-meet/libs/chunks/1689.min.js.map
/usr/share/jitsi-meet/libs/chunks/1818.min.js
/usr/share/jitsi-meet/libs/chunks/1818.min.js.LICENSE.txt
/usr/share/jitsi-meet/libs/chunks/1818.min.js.map
/usr/share/jitsi-meet/libs/chunks/1987.min.js
/usr/share/jitsi-meet/libs/chunks/1987.min.js.map
/usr/share/jitsi-meet/libs/chunks/2130.min.js
/usr/share/jitsi-meet/libs/chunks/2130.min.js.map
/usr/share/jitsi-meet/libs/chunks/2144.min.js
/usr/share/jitsi-meet/libs/chunks/2144.min.js.map
/usr/share/jitsi-meet/libs/chunks/2203.min.js
/usr/share/jitsi-meet/libs/chunks/2203.min.js.map
/usr/share/jitsi-meet/libs/chunks/239.min.js
/usr/share/jitsi-meet/libs/chunks/239.min.js.map
/usr/share/jitsi-meet/libs/chunks/247.min.js
/usr/share/jitsi-meet/libs/chunks/247.min.js.map
/usr/share/jitsi-meet/libs/chunks/2603.min.js
/usr/share/jitsi-meet/libs/chunks/2603.min.js.map
/usr/share/jitsi-meet/libs/chunks/2725.min.js
/usr/share/jitsi-meet/libs/chunks/2725.min.js.map
/usr/share/jitsi-meet/libs/chunks/2775.min.js
/usr/share/jitsi-meet/libs/chunks/2775.min.js.map
/usr/share/jitsi-meet/libs/chunks/2783.min.js
/usr/share/jitsi-meet/libs/chunks/2803.min.js
/usr/share/jitsi-meet/libs/chunks/2803.min.js.map
/usr/share/jitsi-meet/libs/chunks/2886.min.js
/usr/share/jitsi-meet/libs/chunks/2886.min.js.map
/usr/share/jitsi-meet/libs/chunks/3138.min.js
/usr/share/jitsi-meet/libs/chunks/3138.min.js.map
/usr/share/jitsi-meet/libs/chunks/3207.min.js
/usr/share/jitsi-meet/libs/chunks/3207.min.js.map
/usr/share/jitsi-meet/libs/chunks/3259.min.js
/usr/share/jitsi-meet/libs/chunks/3259.min.js.map
/usr/share/jitsi-meet/libs/chunks/3292.min.js
/usr/share/jitsi-meet/libs/chunks/3292.min.js.map
/usr/share/jitsi-meet/libs/chunks/3347.min.js
/usr/share/jitsi-meet/libs/chunks/3347.min.js.map
/usr/share/jitsi-meet/libs/chunks/3417.min.js
/usr/share/jitsi-meet/libs/chunks/3417.min.js.map
/usr/share/jitsi-meet/libs/chunks/3471.min.js
/usr/share/jitsi-meet/libs/chunks/3471.min.js.map
/usr/share/jitsi-meet/libs/chunks/3567.min.js
/usr/share/jitsi-meet/libs/chunks/3567.min.js.map
/usr/share/jitsi-meet/libs/chunks/3645.min.js
/usr/share/jitsi-meet/libs/chunks/3645.min.js.map
/usr/share/jitsi-meet/libs/chunks/3659.min.js
/usr/share/jitsi-meet/libs/chunks/3659.min.js.map
/usr/share/jitsi-meet/libs/chunks/3687.min.js
/usr/share/jitsi-meet/libs/chunks/3687.min.js.map
/usr/share/jitsi-meet/libs/chunks/3760.min.js
/usr/share/jitsi-meet/libs/chunks/4073.min.js
/usr/share/jitsi-meet/libs/chunks/4073.min.js.map
/usr/share/jitsi-meet/libs/chunks/4104.min.js
/usr/share/jitsi-meet/libs/chunks/4104.min.js.map
/usr/share/jitsi-meet/libs/chunks/4106.min.js
/usr/share/jitsi-meet/libs/chunks/4106.min.js.map
/usr/share/jitsi-meet/libs/chunks/4130.min.js
/usr/share/jitsi-meet/libs/chunks/4130.min.js.map
/usr/share/jitsi-meet/libs/chunks/4207.min.js
/usr/share/jitsi-meet/libs/chunks/4207.min.js.map
/usr/share/jitsi-meet/libs/chunks/4226.min.js
/usr/share/jitsi-meet/libs/chunks/4226.min.js.map
/usr/share/jitsi-meet/libs/chunks/4256.min.js
/usr/share/jitsi-meet/libs/chunks/4256.min.js.map
/usr/share/jitsi-meet/libs/chunks/4259.min.js
/usr/share/jitsi-meet/libs/chunks/4259.min.js.map
/usr/share/jitsi-meet/libs/chunks/4337.min.js
/usr/share/jitsi-meet/libs/chunks/4337.min.js.LICENSE.txt
/usr/share/jitsi-meet/libs/chunks/4337.min.js.map
/usr/share/jitsi-meet/libs/chunks/4564.min.js
/usr/share/jitsi-meet/libs/chunks/4564.min.js.map
/usr/share/jitsi-meet/libs/chunks/4690.min.js
/usr/share/jitsi-meet/libs/chunks/4690.min.js.map
/usr/share/jitsi-meet/libs/chunks/4695.min.js
/usr/share/jitsi-meet/libs/chunks/4695.min.js.map
/usr/share/jitsi-meet/libs/chunks/475.min.js
/usr/share/jitsi-meet/libs/chunks/475.min.js.LICENSE.txt
/usr/share/jitsi-meet/libs/chunks/475.min.js.map
/usr/share/jitsi-meet/libs/chunks/4762.min.js
/usr/share/jitsi-meet/libs/chunks/4762.min.js.map
/usr/share/jitsi-meet/libs/chunks/493.min.js
/usr/share/jitsi-meet/libs/chunks/493.min.js.map
/usr/share/jitsi-meet/libs/chunks/5114.min.js
/usr/share/jitsi-meet/libs/chunks/5114.min.js.map
/usr/share/jitsi-meet/libs/chunks/5163.min.js
/usr/share/jitsi-meet/libs/chunks/5163.min.js.map
/usr/share/jitsi-meet/libs/chunks/5301.min.js
/usr/share/jitsi-meet/libs/chunks/5301.min.js.map
/usr/share/jitsi-meet/libs/chunks/5322.min.js
/usr/share/jitsi-meet/libs/chunks/5322.min.js.map
/usr/share/jitsi-meet/libs/chunks/5388.min.js
/usr/share/jitsi-meet/libs/chunks/5388.min.js.map
/usr/share/jitsi-meet/libs/chunks/544.min.js
/usr/share/jitsi-meet/libs/chunks/544.min.js.map
/usr/share/jitsi-meet/libs/chunks/547.min.js
/usr/share/jitsi-meet/libs/chunks/547.min.js.map
/usr/share/jitsi-meet/libs/chunks/5544.min.js
/usr/share/jitsi-meet/libs/chunks/5544.min.js.map
/usr/share/jitsi-meet/libs/chunks/5628.min.js
/usr/share/jitsi-meet/libs/chunks/5628.min.js.map
/usr/share/jitsi-meet/libs/chunks/5713.min.js
/usr/share/jitsi-meet/libs/chunks/5713.min.js.map
/usr/share/jitsi-meet/libs/chunks/5857.min.js
/usr/share/jitsi-meet/libs/chunks/5857.min.js.map
/usr/share/jitsi-meet/libs/chunks/5860.min.js
/usr/share/jitsi-meet/libs/chunks/5860.min.js.map
/usr/share/jitsi-meet/libs/chunks/5950.min.js
/usr/share/jitsi-meet/libs/chunks/5950.min.js.map
/usr/share/jitsi-meet/libs/chunks/6220.min.js
/usr/share/jitsi-meet/libs/chunks/6220.min.js.map
/usr/share/jitsi-meet/libs/chunks/6322.min.js
/usr/share/jitsi-meet/libs/chunks/6322.min.js.map
/usr/share/jitsi-meet/libs/chunks/6586.min.js
/usr/share/jitsi-meet/libs/chunks/6586.min.js.map
/usr/share/jitsi-meet/libs/chunks/6625.min.js
/usr/share/jitsi-meet/libs/chunks/6625.min.js.map
/usr/share/jitsi-meet/libs/chunks/6675.min.js
/usr/share/jitsi-meet/libs/chunks/6675.min.js.map
/usr/share/jitsi-meet/libs/chunks/6770.min.js
/usr/share/jitsi-meet/libs/chunks/6770.min.js.map
/usr/share/jitsi-meet/libs/chunks/7115.min.js
/usr/share/jitsi-meet/libs/chunks/7115.min.js.map
/usr/share/jitsi-meet/libs/chunks/7134.min.js
/usr/share/jitsi-meet/libs/chunks/7134.min.js.map
/usr/share/jitsi-meet/libs/chunks/7185.min.js
/usr/share/jitsi-meet/libs/chunks/7185.min.js.map
/usr/share/jitsi-meet/libs/chunks/7256.min.js
/usr/share/jitsi-meet/libs/chunks/7256.min.js.map
/usr/share/jitsi-meet/libs/chunks/7358.min.js
/usr/share/jitsi-meet/libs/chunks/7358.min.js.map
/usr/share/jitsi-meet/libs/chunks/7690.min.js
/usr/share/jitsi-meet/libs/chunks/7690.min.js.map
/usr/share/jitsi-meet/libs/chunks/7897.min.js
/usr/share/jitsi-meet/libs/chunks/7897.min.js.map
/usr/share/jitsi-meet/libs/chunks/7899.min.js
/usr/share/jitsi-meet/libs/chunks/7899.min.js.map
/usr/share/jitsi-meet/libs/chunks/796.min.js
/usr/share/jitsi-meet/libs/chunks/796.min.js.map
/usr/share/jitsi-meet/libs/chunks/8005.min.js
/usr/share/jitsi-meet/libs/chunks/8005.min.js.map
/usr/share/jitsi-meet/libs/chunks/8024.min.js
/usr/share/jitsi-meet/libs/chunks/8024.min.js.map
/usr/share/jitsi-meet/libs/chunks/8032.min.js
/usr/share/jitsi-meet/libs/chunks/8090.min.js
/usr/share/jitsi-meet/libs/chunks/8090.min.js.map
/usr/share/jitsi-meet/libs/chunks/8146.min.js
/usr/share/jitsi-meet/libs/chunks/8146.min.js.map
/usr/share/jitsi-meet/libs/chunks/8298.min.js
/usr/share/jitsi-meet/libs/chunks/8298.min.js.map
/usr/share/jitsi-meet/libs/chunks/8528.min.js
/usr/share/jitsi-meet/libs/chunks/8528.min.js.map
/usr/share/jitsi-meet/libs/chunks/8846.min.js
/usr/share/jitsi-meet/libs/chunks/8846.min.js.map
/usr/share/jitsi-meet/libs/chunks/8882.min.js
/usr/share/jitsi-meet/libs/chunks/8882.min.js.map
/usr/share/jitsi-meet/libs/chunks/8890.min.js
/usr/share/jitsi-meet/libs/chunks/8890.min.js.map
/usr/share/jitsi-meet/libs/chunks/8989.min.js
/usr/share/jitsi-meet/libs/chunks/8989.min.js.map
/usr/share/jitsi-meet/libs/chunks/8995.min.js
/usr/share/jitsi-meet/libs/chunks/8995.min.js.map
/usr/share/jitsi-meet/libs/chunks/9013.min.js
/usr/share/jitsi-meet/libs/chunks/9013.min.js.map
/usr/share/jitsi-meet/libs/chunks/9105.min.js
/usr/share/jitsi-meet/libs/chunks/9105.min.js.map
/usr/share/jitsi-meet/libs/chunks/922.min.js
/usr/share/jitsi-meet/libs/chunks/922.min.js.map
/usr/share/jitsi-meet/libs/chunks/9596.min.js
/usr/share/jitsi-meet/libs/chunks/9612.min.js
/usr/share/jitsi-meet/libs/chunks/9612.min.js.map
/usr/share/jitsi-meet/libs/chunks/9698.min.js
/usr/share/jitsi-meet/libs/chunks/9698.min.js.map
/usr/share/jitsi-meet/libs/chunks/9706.min.js
/usr/share/jitsi-meet/libs/chunks/9706.min.js.map
/usr/share/jitsi-meet/libs/chunks/971.min.js
/usr/share/jitsi-meet/libs/chunks/971.min.js.map
/usr/share/jitsi-meet/libs/chunks/9828.min.js
/usr/share/jitsi-meet/libs/chunks/9828.min.js.map
/usr/share/jitsi-meet/libs/chunks/9890.min.js
/usr/share/jitsi-meet/libs/chunks/9890.min.js.map
/usr/share/jitsi-meet/libs/chunks/9976.min.js
/usr/share/jitsi-meet/libs/chunks/9976.min.js.map
/usr/share/jitsi-meet/libs/close3.min.js
/usr/share/jitsi-meet/libs/emotion.bin
/usr/share/jitsi-meet/libs/emotion.json
/usr/share/jitsi-meet/libs/excalidraw
/usr/share/jitsi-meet/libs/excalidraw/fonts
/usr/share/jitsi-meet/libs/excalidraw/fonts/Assistant
/usr/share/jitsi-meet/libs/excalidraw/fonts/Assistant/Assistant-Bold.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Assistant/Assistant-Medium.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Assistant/Assistant-Regular.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Assistant/Assistant-SemiBold.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Cascadia
/usr/share/jitsi-meet/libs/excalidraw/fonts/Cascadia/CascadiaCode-Regular.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/ComicShanns
/usr/share/jitsi-meet/libs/excalidraw/fonts/ComicShanns/ComicShanns-Regular-279a7b317d12eb88de06167bd672b4b4.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/ComicShanns/ComicShanns-Regular-6e066e8de2ac57ea9283adb9c24d7f0c.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/ComicShanns/ComicShanns-Regular-dc6a8806fa96795d7b3be5026f989a17.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/ComicShanns/ComicShanns-Regular-fcb0fc02dcbee4c9846b3e2508668039.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Excalifont
/usr/share/jitsi-meet/libs/excalidraw/fonts/Excalifont/Excalifont-Regular-349fac6ca4700ffec595a7150a0d1e1d.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Excalifont/Excalifont-Regular-3f2c5db56cc93c5a6873b1361d730c16.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Excalifont/Excalifont-Regular-41b173a47b57366892116a575a43e2b6.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Excalifont/Excalifont-Regular-623ccf21b21ef6b3a0d87738f77eb071.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Excalifont/Excalifont-Regular-a88b72a24fb54c9f94e3b5fdaa7481c9.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Excalifont/Excalifont-Regular-b9dcf9d2e50a1eaf42fc664b50a3fd0d.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Excalifont/Excalifont-Regular-be310b9bcd4f1a43f571c46df7809174.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Liberation
/usr/share/jitsi-meet/libs/excalidraw/fonts/Liberation/LiberationSans-Regular.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Lilita
/usr/share/jitsi-meet/libs/excalidraw/fonts/Lilita/Lilita-Regular-i7dPIFZ9Zz-WBtRtedDbYE98RXi4EwSsbg.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Lilita/Lilita-Regular-i7dPIFZ9Zz-WBtRtedDbYEF8RXi4EwQ.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Nunito
/usr/share/jitsi-meet/libs/excalidraw/fonts/Nunito/Nunito-Regular-XRXI3I6Li01BKofiOc5wtlZ2di8HDIkhdTA3j6zbXWjgevT5.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Nunito/Nunito-Regular-XRXI3I6Li01BKofiOc5wtlZ2di8HDIkhdTQ3j6zbXWjgeg.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Nunito/Nunito-Regular-XRXI3I6Li01BKofiOc5wtlZ2di8HDIkhdTk3j6zbXWjgevT5.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Nunito/Nunito-Regular-XRXI3I6Li01BKofiOc5wtlZ2di8HDIkhdTo3j6zbXWjgevT5.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Nunito/Nunito-Regular-XRXI3I6Li01BKofiOc5wtlZ2di8HDIkhdTs3j6zbXWjgevT5.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Virgil
/usr/share/jitsi-meet/libs/excalidraw/fonts/Virgil/Virgil-Regular.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-019d66dcad46dc156b162d267f981c20.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-04b718e5623574919c8b0dea5f301444.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-069e77aac84590e2e991d0a0176d34f2.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-06c77b8c66e51ed6c63ccb502dd8b8af.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-08e0dc436ad0ad61ba5558db0674d762.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-093b9ef39a46ceae95a1df18a0a3a326.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-095c169f3314805276f603a362766abd.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-09850c4077f3fffe707905872e0e2460.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-0986d134c05864f5025962eef9f994a0.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-0b5d723fdc4e249c140f0909e87d03b4.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-0f626226ba1272e832aea87bafd9720e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-0f7fb1e0d5015bb1371343153ecf7ce3.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-0fa55a080fcd0f9dc2e0b0058b793df8.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-0facdf1ea213ba40261022f5d5ed4493.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-10a7ae9a371830a80c3d844acf1c02d7.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-112c051027b2d766c19a519f6ee1f4f7.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-11c345711937f0ba4b8f7b6b919c8440.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-12b52b58eb3df36804b9a654ec9ee194.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-13ae07ed2e272d26d59bc0691cd7117a.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-13d2887ec8ee73c43acdabc52a05af7b.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-145aa02cdd91946e67dc934e1acffe75.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-15dc6d811c9cd078f9086a740d5a1038.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-173945821411c09f70c95f98d590e697.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-1b611157cd46bb184d4fa4dae2d6a2b8.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-1e6fd68f1f3902ce48ce8c69df385622.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-1ee544f0f1dac422545c505baa788992.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-1fdc0c67ed57263a80fd108c1f6ccf24.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-203b0e569e3b14aac86a003dc3fa523e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-20cc1bbf50e7efb442756cb605672c1f.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-20e7bf72fa05de9adf7dbcc7bf51dde6.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-21430ee05a1248901da8d0de08744d47.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-23686f7f29da6e8008c36dd3a80c83d6.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-23ad2d71b280f00b1363b95b7bea94eb.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-23f228f3999c01983860012330e4be08.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-24476a126f129212beb33f66853ea151.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-24a21c1e4449222e8d1898d69ff3a404.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-25b7f38e18f035f96cb5e547bd2bd08c.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-29cec36cd205b211da97acabaa62f055.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-2a26d20a23b00898ce82f09d2ee47c3f.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-2adbc89c11e65905393d3dfc468b9d5b.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-2b7441d46298788ac94e610ffcc709b6.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-2b77e8ebfb2367ab2662396a60e7d320.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-2cf96d082d35ea3d8106851223ad0d16.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-2d43040e86ff03ba677f6f9c04cd0805.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-2e33e8dc771ef5e1d9127d60a6b73679.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-33432927cd87d40cfe393c7482bf221f.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-353f33792a8f60dc69323ddf635a269e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-36925dfe329a45086cbb7fc5c20d45ac.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-3717077e38f98d89eae729b6c14e56dc.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-3756e81d3e149cf6099163ee79944fec.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-395c35dd584b56b0789f58a0559beaf1.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-3c9de2ae0ea4bc91a510942dfa4be8d2.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-3cc70dbb64df5b21f1326cc24dee2195.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-3e1f8f654357353bf0e04ba5c34b5f7f.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-3e63ed8162808a9e425ed80a8bc79114.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-3eaa538115d76932653c21d8dc28f207.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4095eb84ef3874e2600247bee0b04026.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-41521fade99856108931b4768b1b2648.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-450da755d5bcb70906e1295e559b9602.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-452225341522a7942f0f6aab1a5c91a3.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4535823663ad81405188a528d8f2b1a2.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4806e761d750087c2d734fc64596eaff.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4a0fdb40036e87b40aa08dd30584cb85.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4a38cc3e9cf104e69ba246d37f8cf135.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4aca6a43e59aceee2166b0c7e4e85ef1.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4bfaa8ffa64c5ee560aa2daba7c9cbd3.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4dc6d5f188d5c96d44815cd1e81aa885.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4ddc14ed3eb0c3e46364317dfc0144a3.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4ee10ae43505e2e0bc62656ced49c0fa.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-4f50e5136e136527280bc902c5817561.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-51502f1206be09c565f1547c406e9558.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-51a0e808bbc8361236ac521a119758a3.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-52a84a22fd1369bffeaf21da2d6158dc.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-5330a2119a716e4e7224ed108b085dac.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-543fa46ace099a7099dad69123399400.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-544fc28abe2c5c30e62383fd4dac255f.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-54acdfc2166ad7fcbd074f75fd4a56ba.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-5572b3513ba8df57a3d5d7303ee6b11b.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-56467a5c8840c4d23a60b2f935114848.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-56a32a7689abd0326e57c10c6c069bb4.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-57862b464a55b18c7bf234ce22907d73.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-583d166e56ba0de4b77eabb47ef67839.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-5882ffa04f32584d26109137e2da4352.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-58fd02350d0bc52cf1ca3bb32ce9766e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-5935a5775af3d5c6307ac667bd9ae74e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-59e9ff77b0efaf684bc09274fb6908c9.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-5a1ce3117cfe90c48e8fb4a9a00f694d.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-5a45d991244d4c7140217e1e5f5ca4f4.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-5a7fac4b8b23a6e4e5ba0c9bf1756c91.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-5b0ed6971aaab9c8ad563230bd5471a7.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-5d2898fbc097a7e24c6f38d80587621e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-603aefd23e350ba7eb124273e3c9bcf1.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-60a3089806700d379f11827ee9843b6b.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-60a41c7e1c68f22424e6d22df544bc82.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-642b26e2e5f5fb780b51b593dbc8c851.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-66493ba5a8367f2928812f446f47b56a.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-670ba603758d94268e8606f240a42e12.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-671a2c20b1eb9e4ef8a192833940e319.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-684d65f1793cac449dde5d59cb3c47fb.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-69c09cc5fa3e55c74fc4821f76909cc3.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-6ae5b42180ad70b971c91e7eefb8eba2.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-6e092f71c1e634059ada0e52abadce67.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-6f3256af8454371776bc46670d33cc65.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-6fe5c5973cc06f74b2387a631ea36b88.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-70c2eb8d64e71a42a834eb857ea9df51.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-70e811fd7994e61f408c923de6ddd078.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7197d6fda6cba7c3874c53d6381ca239.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-72252d73220fa3cd856677888cee1635.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-72536a3d71b694a0d53dd90ddceae41e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-726303e0774b4e678bff8c2deb6ca603.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-733171b4ffcd17ea1fe1c0ba627173bf.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-739bc1a567439c7cffcd1614644593d2.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-73e309718fd16cea44b4d54a33581811.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7494dc504ae00ee9cd0505f990f88c5d.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-74e2263a91439c25b91d5132ce9f4d62.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-761d05e3cd968cf574166867998ef06a.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7718fe60986d8b42b1be9c5ace5ccf25.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-774d4f764a1299da5d28ec2f2ffe0d69.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-79d494361ae093b69e74ee9dbe65bfd4.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-79f007c1c6d07557120982951ea67998.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7a07ddc0f0c0f5f4a9bad6ee3dda66b5.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7ab2bed91166a9dca83a5ebfbe2a7f38.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7ccce86603f80a099ddb0cb21d4ae3e3.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7e4bde7e9c7f84cd34d8a845e384c746.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7e929f262f30c8ee78bf398150b1a7cd.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7eb9fffd1aa890d07d0f88cc82e6cfe4.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-7f855356ab893b0d2b9c1c83b8116f0e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-829615148e6357d826b9242eb7fbbd1e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-866fa7613df6b3fd272bcfd4530c0bb9.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-87599f94b6cc129d505b375798d0d751.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-8c2f33cee3993174f7e87c28e4bf42ee.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-8d3bcabb847b56243b16afe62adaaf21.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-8de5b863cb50dfefdd07cb11c774d579.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-8e9f97f01034820170065b2921b4fb5e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-8f476c4c99813d57cbe6eca4727388ad.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-903bb6865f3452e2fda42e3a25547bc5.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-91ddb2969bf2d31ba02ad82998d1314c.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-938d90c10ff8c20386af7f242c05d6b0.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-93fc8f28a33234bcadf1527cafabd502.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-95429962233afd82db1c27df1500a28c.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-9544732d2e62d1a429674f8ee41b5d3a.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-9592bfc861f07bcb8d75c196b370e548.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-95bfd249da4902577b4b7d76ebdd0b44.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-968cffdc8ee679da094e77ebf50f58ef.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-97f7f48ce90c9429bf32ae51469db74d.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-982b630266d87db93d2539affb1275c6.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-98f2ad84457de7f3740d9920b8fa8667.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-99a16ef6a64934d5781933dbd9c46b2e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-9cfb2a77a4e45025105ad29a1748b90d.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-9d81066dd2b337c938df6e90380a00dc.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-9eb5a99df4e76ac3363453ac9ca288b1.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-a004ddfcb26e67bd6e678c8ed19e25ce.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-a0ca5df4258213d7fc9fce80f65ce760.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-a1f916d6039285c4ffb900cd654e418f.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-a203b91dad570bf05a58c3c3ddb529bf.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-a365e82ed54697a52f27adcea1315fe8.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-a4c34be6d42152e64b0df90bc4607f64.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-a7accba310e821da5505f71c03b76bdb.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-aa0d470430e6391eca720c7cfa44446f.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-aa5c9ca6cf4fba00433b7aa3fa10671a.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-ac9ceb44437becc3e9c4dbfebab7fc2d.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-b1220a3c61f85cc0408deedb4c5f57a2.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-b358f7a51ece39a3247942b1feabdb29.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-b57aaedfd8ebdf3931f25119dc6a5eb2.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-b5c1596551c256e0e9cf02028595b092.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-b6d128682ee29e471486354d486a1b90.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-b6fd38ca30869792244804b04bc058da.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-b7d203b051eff504ff59ddca7576b6a9.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-b96d9226ce77ec94ceca043d712182e6.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-ba3de316d63c7e339987b16f41a0b879.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-bafff7a14c27403dcc6cf1432e8ea836.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-bd77e3c7f9e0b072d96af37f73d1aa32.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-be549ab72f0719d606a5c01e2c0219b6.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-c16ed9740b85badf16e86ea782a3062f.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-c1f94158256bb1f3bf665b053d895af9.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-c40533fdf4cc57177b12803598af7e59.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-c4a687ac4f0c2766eefc9f77ed99cddf.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-c69f61a4ab18d0488c8d1fc12e7028e8.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-c8b71798409ccc126ee264a00aadcf21.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-c99eda15fc26a2941579560f76c3a5cf.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-cb17fc3db95f6d139afc9d31a8e93293.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-cbaaefaaf326668277aa24dfa93c4d28.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-cd145ce4a0ea18469358df53c207bc1b.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-cdbce89e82cc1ab53a2decbf5819278f.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-ce4884f96f11589608b76b726a755803.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-cf2cc71752631e579e35b0e423bf2638.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-cf6ff4e0f491ca0cf3038187a997b9b4.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-cfb211578629b7e8153b37240de6a9d5.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-d0cf73942fea1c74edbdf0b3011f4656.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-d2666cbed13462c5dc36fa2f15c202ca.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-d3716376641d615e2995605b29bca7b6.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-dac48066b5883d8b4551fc584f0c2a3e.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-dbea1af6dcd9860be40c3d18254338f5.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-e11567fd2accf9957cd0d3c2be937d87.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-e2ead7ea7da0437f085f42ffc05f8d13.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-e3fcf5180fd466c8915c4e8069491054.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-e480d9c614742d05f0e78f274f1e69e6.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-e4bca6cfa53e499cae0a6be4894a90e9.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-e51ef413167c6e14e0c0fdcc585f2fc9.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-e5f453bb04da18eed01675eeebd88bf8.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-e656f091b9dc4709722c9f4b84d3c797.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-ec181b795ac1fb5a50d700b6e996d745.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-ee8bae97908d5147b423f77ad0d3c1bb.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-f0f13b5c60e0af5553bd359f5513be1b.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-f2b54d4e7be0eaefe1c2c56836fa5368.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-f56414bf9bced67990def8660e306759.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-f5d079153c99a25b9be5b8583c4cc8a7.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-f6032fc06eb20480f096199713f70885.woff2
/usr/share/jitsi-meet/libs/excalidraw/fonts/Xiaolai/Xiaolai-Regular-f8ee5d36068a42b51d0e4a1116cfcec1.woff2
/usr/share/jitsi-meet/libs/external_api.min.js
/usr/share/jitsi-meet/libs/external_api.min.js.map
/usr/share/jitsi-meet/libs/face-landmarks-worker.min.js
/usr/share/jitsi-meet/libs/face-landmarks-worker.min.js.map
/usr/share/jitsi-meet/libs/lib-jitsi-meet.e2ee-worker.js
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.js
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.js.LICENSE.txt
/usr/share/jitsi-meet/libs/lib-jitsi-meet.min.map
/usr/share/jitsi-meet/libs/mediapipe-segmentation
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation.binarypb
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation.tflite
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_landscape.tflite
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_simd_wasm_bin.data
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_simd_wasm_bin.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_simd_wasm_bin.wasm
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_wasm_bin.js
/usr/share/jitsi-meet/libs/mediapipe-segmentation/selfie_segmentation_solution_wasm_bin.wasm
/usr/share/jitsi-meet/libs/noise-suppressor-worklet.min.js
/usr/share/jitsi-meet/libs/noise-suppressor-worklet.min.js.map
/usr/share/jitsi-meet/libs/olm.wasm
/usr/share/jitsi-meet/libs/rnnoise.wasm
/usr/share/jitsi-meet/libs/screenshot-capture-worker.min.js
/usr/share/jitsi-meet/libs/screenshot-capture-worker.min.js.map
/usr/share/jitsi-meet/libs/selfie_segmentation_landscape.tflite
/usr/share/jitsi-meet/libs/tfjs-backend-wasm-simd.wasm
/usr/share/jitsi-meet/libs/tfjs-backend-wasm-threaded-simd.wasm
/usr/share/jitsi-meet/libs/tfjs-backend-wasm.wasm
/usr/share/jitsi-meet/libs/tflite-simd.wasm
/usr/share/jitsi-meet/libs/tflite.wasm
/usr/share/jitsi-meet/libs/vb-inference-worker.min.js
/usr/share/jitsi-meet/libs/vb-inference-worker.min.js.map
/usr/share/jitsi-meet/manifest.json
/usr/share/jitsi-meet/plugin.head.html
/usr/share/jitsi-meet/pwa-worker.js
/usr/share/jitsi-meet/robots.txt
/usr/share/jitsi-meet/scripts
/usr/share/jitsi-meet/scripts/coturn-le-update.sh
/usr/share/jitsi-meet/scripts/encode-sound.sh
/usr/share/jitsi-meet/scripts/install-letsencrypt-cert.sh
/usr/share/jitsi-meet/scripts/lang-sort.sh
/usr/share/jitsi-meet/scripts/move-to-jaas.sh
/usr/share/jitsi-meet/scripts/register-jaas-account.sh
/usr/share/jitsi-meet/scripts/update-asap-daily.sh
/usr/share/jitsi-meet/scripts/update-ljm.sh
/usr/share/jitsi-meet/scripts/update-mobile-rnsdk-version.sh
/usr/share/jitsi-meet/scripts/update-mobile-sdk-version.sh
/usr/share/jitsi-meet/scripts/update-mobile-version.sh
/usr/share/jitsi-meet/sounds
/usr/share/jitsi-meet/sounds/README.md
/usr/share/jitsi-meet/sounds/asked-unmute.mp3
/usr/share/jitsi-meet/sounds/asked-unmute.opus
/usr/share/jitsi-meet/sounds/e2eeOff.mp3
/usr/share/jitsi-meet/sounds/e2eeOff.opus
/usr/share/jitsi-meet/sounds/e2eeOff_fr.mp3
/usr/share/jitsi-meet/sounds/e2eeOff_fr.opus
/usr/share/jitsi-meet/sounds/e2eeOff_frCA.mp3
/usr/share/jitsi-meet/sounds/e2eeOff_frCA.opus
/usr/share/jitsi-meet/sounds/e2eeOn.mp3
/usr/share/jitsi-meet/sounds/e2eeOn.opus
/usr/share/jitsi-meet/sounds/e2eeOn_fr.mp3
/usr/share/jitsi-meet/sounds/e2eeOn_fr.opus
/usr/share/jitsi-meet/sounds/e2eeOn_frCA.mp3
/usr/share/jitsi-meet/sounds/e2eeOn_frCA.opus
/usr/share/jitsi-meet/sounds/incomingMessage.mp3
/usr/share/jitsi-meet/sounds/incomingMessage.opus
/usr/share/jitsi-meet/sounds/incomingMessage.wav
/usr/share/jitsi-meet/sounds/joined.mp3
/usr/share/jitsi-meet/sounds/joined.opus
/usr/share/jitsi-meet/sounds/joined.wav
/usr/share/jitsi-meet/sounds/knock.mp3
/usr/share/jitsi-meet/sounds/knock.opus
/usr/share/jitsi-meet/sounds/left.mp3
/usr/share/jitsi-meet/sounds/left.opus
/usr/share/jitsi-meet/sounds/left.wav
/usr/share/jitsi-meet/sounds/liveStreamingOff.mp3
/usr/share/jitsi-meet/sounds/liveStreamingOff.opus
/usr/share/jitsi-meet/sounds/liveStreamingOff_fr.mp3
/usr/share/jitsi-meet/sounds/liveStreamingOff_fr.opus
/usr/share/jitsi-meet/sounds/liveStreamingOff_frCA.mp3
/usr/share/jitsi-meet/sounds/liveStreamingOff_frCA.opus
/usr/share/jitsi-meet/sounds/liveStreamingOn.mp3
/usr/share/jitsi-meet/sounds/liveStreamingOn.opus
/usr/share/jitsi-meet/sounds/liveStreamingOn_fr.mp3
/usr/share/jitsi-meet/sounds/liveStreamingOn_fr.opus
/usr/share/jitsi-meet/sounds/liveStreamingOn_frCA.mp3
/usr/share/jitsi-meet/sounds/liveStreamingOn_frCA.opus
/usr/share/jitsi-meet/sounds/noAudioSignal.mp3
/usr/share/jitsi-meet/sounds/noAudioSignal.opus
/usr/share/jitsi-meet/sounds/noisyAudioInput.mp3
/usr/share/jitsi-meet/sounds/noisyAudioInput.opus
/usr/share/jitsi-meet/sounds/outgoingRinging.mp3
/usr/share/jitsi-meet/sounds/outgoingRinging.opus
/usr/share/jitsi-meet/sounds/outgoingRinging.wav
/usr/share/jitsi-meet/sounds/outgoingStart.mp3
/usr/share/jitsi-meet/sounds/outgoingStart.opus
/usr/share/jitsi-meet/sounds/outgoingStart.wav
/usr/share/jitsi-meet/sounds/reactions-applause.mp3
/usr/share/jitsi-meet/sounds/reactions-applause.opus
/usr/share/jitsi-meet/sounds/reactions-boo.mp3
/usr/share/jitsi-meet/sounds/reactions-boo.opus
/usr/share/jitsi-meet/sounds/reactions-crickets.mp3
/usr/share/jitsi-meet/sounds/reactions-crickets.opus
/usr/share/jitsi-meet/sounds/reactions-laughter.mp3
/usr/share/jitsi-meet/sounds/reactions-laughter.opus
/usr/share/jitsi-meet/sounds/reactions-love.mp3
/usr/share/jitsi-meet/sounds/reactions-love.opus
/usr/share/jitsi-meet/sounds/reactions-raised-hand.mp3
/usr/share/jitsi-meet/sounds/reactions-raised-hand.opus
/usr/share/jitsi-meet/sounds/reactions-surprise.mp3
/usr/share/jitsi-meet/sounds/reactions-surprise.opus
/usr/share/jitsi-meet/sounds/reactions-thumbs-up.mp3
/usr/share/jitsi-meet/sounds/reactions-thumbs-up.opus
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff.opus
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff_fr.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff_fr.opus
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff_frCA.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOff_frCA.opus
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn.opus
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn_fr.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn_fr.opus
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn_frCA.mp3
/usr/share/jitsi-meet/sounds/recordingAndTranscriptionOn_frCA.opus
/usr/share/jitsi-meet/sounds/recordingOff.mp3
/usr/share/jitsi-meet/sounds/recordingOff.opus
/usr/share/jitsi-meet/sounds/recordingOff_fr.mp3
/usr/share/jitsi-meet/sounds/recordingOff_fr.opus
/usr/share/jitsi-meet/sounds/recordingOff_frCA.mp3
/usr/share/jitsi-meet/sounds/recordingOff_frCA.opus
/usr/share/jitsi-meet/sounds/recordingOn.mp3
/usr/share/jitsi-meet/sounds/recordingOn.opus
/usr/share/jitsi-meet/sounds/recordingOn_fr.mp3
/usr/share/jitsi-meet/sounds/recordingOn_fr.opus
/usr/share/jitsi-meet/sounds/recordingOn_frCA.mp3
/usr/share/jitsi-meet/sounds/recordingOn_frCA.opus
/usr/share/jitsi-meet/sounds/rejected.mp3
/usr/share/jitsi-meet/sounds/rejected.opus
/usr/share/jitsi-meet/sounds/rejected.wav
/usr/share/jitsi-meet/sounds/ring.mp3
/usr/share/jitsi-meet/sounds/ring.opus
/usr/share/jitsi-meet/sounds/ring.wav
/usr/share/jitsi-meet/sounds/talkWhileMuted.mp3
/usr/share/jitsi-meet/sounds/talkWhileMuted.opus
/usr/share/jitsi-meet/sounds/transcriptionOff.mp3
/usr/share/jitsi-meet/sounds/transcriptionOff.opus
/usr/share/jitsi-meet/sounds/transcriptionOff_fr.mp3
/usr/share/jitsi-meet/sounds/transcriptionOff_fr.opus
/usr/share/jitsi-meet/sounds/transcriptionOff_frCA.mp3
/usr/share/jitsi-meet/sounds/transcriptionOff_frCA.opus
/usr/share/jitsi-meet/sounds/transcriptionOn.mp3
/usr/share/jitsi-meet/sounds/transcriptionOn.opus
/usr/share/jitsi-meet/sounds/transcriptionOn_fr.mp3
/usr/share/jitsi-meet/sounds/transcriptionOn_fr.opus
/usr/share/jitsi-meet/sounds/transcriptionOn_frCA.mp3
/usr/share/jitsi-meet/sounds/transcriptionOn_frCA.opus
/usr/share/jitsi-meet/static
/usr/share/jitsi-meet/static/404.html
/usr/share/jitsi-meet/static/close.html
/usr/share/jitsi-meet/static/close.js
/usr/share/jitsi-meet/static/close2.html
/usr/share/jitsi-meet/static/close3.html
/usr/share/jitsi-meet/static/close3.js
/usr/share/jitsi-meet/static/dialInInfo.html
/usr/share/jitsi-meet/static/logout.html
/usr/share/jitsi-meet/static/msredirect.html
/usr/share/jitsi-meet/static/oauth.html
/usr/share/jitsi-meet/static/offline.html
/usr/share/jitsi-meet/static/planLimit.html
/usr/share/jitsi-meet/static/prejoin.html
/usr/share/jitsi-meet/static/pwa
/usr/share/jitsi-meet/static/pwa/icons
/usr/share/jitsi-meet/static/pwa/icons/icon192.png
/usr/share/jitsi-meet/static/pwa/icons/icon512.png
/usr/share/jitsi-meet/static/pwa/icons/iconMask.png
/usr/share/jitsi-meet/static/recommendedBrowsers.html
/usr/share/jitsi-meet/static/settingsToolbarAdditionalContent.html
/usr/share/jitsi-meet/static/sso.html
/usr/share/jitsi-meet/static/webrtcUnsupported.html
/usr/share/jitsi-meet/static/welcomePageAdditionalCard.html
/usr/share/jitsi-meet/static/welcomePageAdditionalContent.html
/usr/share/jitsi-meet/static/whiteboard.html
/usr/share/jitsi-meet/title.html


## Package : jitsi-meet-web-config


```text
$ dpkg -L 'jitsi-meet-web-config' 2>/dev/null || true
```
/.
/etc
/etc/jitsi
/etc/jitsi/meet
/usr
/usr/share
/usr/share/doc
/usr/share/doc/jitsi-meet-web-config
/usr/share/doc/jitsi-meet-web-config/README
/usr/share/doc/jitsi-meet-web-config/changelog.Debian.gz
/usr/share/doc/jitsi-meet-web-config/copyright
/usr/share/jitsi-meet-web-config
/usr/share/jitsi-meet-web-config/8x8.vc-config.js
/usr/share/jitsi-meet-web-config/config.js
/usr/share/jitsi-meet-web-config/index-jaas.html
/usr/share/jitsi-meet-web-config/jitsi-meet.example
/usr/share/jitsi-meet-web-config/jitsi-meet.example-apache
/usr/share/jitsi-meet-web-config/nginx-jaas.conf


## Package : jitsi-meet-prosody


```text
$ dpkg -L 'jitsi-meet-prosody' 2>/dev/null || true
```
/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/jitsi-meet-prosody
/usr/share/doc/jitsi-meet-prosody/README
/usr/share/doc/jitsi-meet-prosody/README.Debian
/usr/share/doc/jitsi-meet-prosody/changelog.Debian.gz
/usr/share/doc/jitsi-meet-prosody/copyright
/usr/share/jitsi-meet
/usr/share/jitsi-meet/prosody-plugins
/usr/share/jitsi-meet/prosody-plugins/README.md
/usr/share/jitsi-meet/prosody-plugins/luajwtjitsi.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_audio_translation_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_jitsi-anonymous.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_jitsi-shared-secret.lua
/usr/share/jitsi-meet/prosody-plugins/mod_auth_token.lua
/usr/share/jitsi-meet/prosody-plugins/mod_av_moderation_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_certs_s2soutinjection.lua
/usr/share/jitsi-meet/prosody-plugins/mod_client_proxy.lua
/usr/share/jitsi-meet/prosody-plugins/mod_conference_duration.lua
/usr/share/jitsi-meet/prosody-plugins/mod_debug_traceback.lua
/usr/share/jitsi-meet/prosody-plugins/mod_end_conference.lua
/usr/share/jitsi-meet/prosody-plugins/mod_features_identity.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filesharing_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filter_iq_jibri.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filter_iq_rayo.lua
/usr/share/jitsi-meet/prosody-plugins/mod_filter_messages.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/actions.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/conditions.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/definitions.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/marks.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/mod_firewall.lua
/usr/share/jitsi-meet/prosody-plugins/mod_firewall/test.lib.lua
/usr/share/jitsi-meet/prosody-plugins/mod_fmuc.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jibri_session.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jiconop.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jitsi_permissions.lua
/usr/share/jitsi-meet/prosody-plugins/mod_jitsi_session.lua
/usr/share/jitsi-meet/prosody-plugins/mod_limits_exception.lua
/usr/share/jitsi-meet/prosody-plugins/mod_log_ringbuffer.lua
/usr/share/jitsi-meet/prosody-plugins/mod_measure_message_count.lua
/usr/share/jitsi-meet/prosody-plugins/mod_measure_stanza_counts.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_allowners.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_auth_ban.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_breakout_rooms.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_census.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_cleanup_backend_services.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_displayname.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_domain_mapper.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_end_meeting.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_filter_access.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_flip.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_hide_all.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_jigasi_invite.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_kick_participant.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_limit_messages.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_lobby_rooms.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_max_occupants.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_meeting_id.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_password_check.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_password_whitelist.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_rate_limit.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_resource_validate.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_size.lua
/usr/share/jitsi-meet/prosody-plugins/mod_muc_wait_for_host.lua
/usr/share/jitsi-meet/prosody-plugins/mod_persistent_lobby.lua
/usr/share/jitsi-meet/prosody-plugins/mod_polls_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_presence_identity.lua
/usr/share/jitsi-meet/prosody-plugins/mod_rate_limit.lua
/usr/share/jitsi-meet/prosody-plugins/mod_reservations.lua
/usr/share/jitsi-meet/prosody-plugins/mod_room_destroy.lua
/usr/share/jitsi-meet/prosody-plugins/mod_room_metadata_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_roster_command.lua
/usr/share/jitsi-meet/prosody-plugins/mod_roster_command.patch
/usr/share/jitsi-meet/prosody-plugins/mod_s2s_whitelist.lua
/usr/share/jitsi-meet/prosody-plugins/mod_s2sout_override.lua
/usr/share/jitsi-meet/prosody-plugins/mod_secure_interfaces.lua
/usr/share/jitsi-meet/prosody-plugins/mod_short_lived_token.lua
/usr/share/jitsi-meet/prosody-plugins/mod_speakerstats_component.lua
/usr/share/jitsi-meet/prosody-plugins/mod_system_chat_message.lua
/usr/share/jitsi-meet/prosody-plugins/mod_test_observer.lua
/usr/share/jitsi-meet/prosody-plugins/mod_test_observer_http.lua
/usr/share/jitsi-meet/prosody-plugins/mod_token_affiliation.lua
/usr/share/jitsi-meet/prosody-plugins/mod_token_verification.lua
/usr/share/jitsi-meet/prosody-plugins/mod_turncredentials_http.lua
/usr/share/jitsi-meet/prosody-plugins/mod_visitors.lua
/usr/share/jitsi-meet/prosody-plugins/mod_visitors_component.lua
/usr/share/jitsi-meet/prosody-plugins/muc_owner_allow_kick-0.12.patch
/usr/share/jitsi-meet/prosody-plugins/stanza_router_no-log.patch
/usr/share/jitsi-meet/prosody-plugins/token
/usr/share/jitsi-meet/prosody-plugins/token/jwk.lib.lua
/usr/share/jitsi-meet/prosody-plugins/token/util.lib.lua
/usr/share/jitsi-meet/prosody-plugins/util.lib.lua
/usr/share/jitsi-meet-prosody
/usr/share/jitsi-meet-prosody/jaas.cfg.lua
/usr/share/jitsi-meet-prosody/prosody.cfg.lua-jvb.example


## Package : jitsi-meet-turnserver


```text
$ dpkg -L 'jitsi-meet-turnserver' 2>/dev/null || true
```
/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/jitsi-meet-turnserver
/usr/share/doc/jitsi-meet-turnserver/changelog.Debian.gz
/usr/share/doc/jitsi-meet-turnserver/copyright
/usr/share/jitsi-meet-turnserver
/usr/share/jitsi-meet-turnserver/jitsi-meet.conf
/usr/share/jitsi-meet-turnserver/turnserver.conf


## Package : jicofo


```text
$ dpkg -L 'jicofo' 2>/dev/null || true
```
/.
/etc
/etc/init.d
/etc/init.d/jicofo
/etc/jitsi
/etc/jitsi/jicofo
/etc/jitsi/jicofo/logging.properties
/etc/logrotate.d
/etc/logrotate.d/jicofo
/usr
/usr/share
/usr/share/doc
/usr/share/doc/jicofo
/usr/share/doc/jicofo/README.Debian
/usr/share/doc/jicofo/changelog.Debian.gz
/usr/share/doc/jicofo/copyright
/usr/share/jicofo
/usr/share/jicofo/collect-dump-logs.sh
/usr/share/jicofo/jicofo.jar
/usr/share/jicofo/jicofo.sh
/usr/share/jicofo/lib
/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar
/usr/share/jicofo/lib/annotations-23.0.0.jar
/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar
/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar
/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar
/usr/share/jicofo/lib/commons-lang3-3.12.0.jar
/usr/share/jicofo/lib/config-1.4.3.jar
/usr/share/jicofo/lib/gson-2.8.5.jar
/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar
/usr/share/jicofo/lib/jackson-core-2.18.0.jar
/usr/share/jicofo/lib/jackson-databind-2.18.0.jar
/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar
/usr/share/jicofo/lib/jansi-2.4.1.jar
/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar
/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar
/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar
/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar
/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar
/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar
/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar
/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar
/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar
/usr/share/jicofo/lib/jjwt-api-0.12.6.jar
/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar
/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar
/usr/share/jicofo/lib/jna-5.9.0.jar
/usr/share/jicofo/lib/jsr305-3.0.2.jar
/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar
/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar
/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar
/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar
/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar
/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar
/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar
/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar
/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar
/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar
/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar
/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar
/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar
/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar
/usr/share/jicofo/lib/minidns-core-1.0.5.jar
/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar
/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar
/usr/share/jicofo/lib/precis-1.1.0.jar
/usr/share/jicofo/lib/sentry-5.4.0.jar
/usr/share/jicofo/lib/simpleclient-0.16.0.jar
/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar
/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar
/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar
/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar
/usr/share/jicofo/lib/slf4j-api-1.7.32.jar
/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar
/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar
/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar


## Package : jitsi-videobridge2


```text
$ dpkg -L 'jitsi-videobridge2' 2>/dev/null || true
```
/.
/etc
/etc/init.d
/etc/init.d/jitsi-videobridge2
/etc/jitsi
/etc/jitsi/videobridge
/etc/jitsi/videobridge/logging.properties
/etc/logrotate.d
/etc/logrotate.d/jitsi-videobridge
/etc/sysctl.d
/etc/sysctl.d/20-jvb-udp-buffers.conf
/lib
/lib/systemd
/lib/systemd/system
/lib/systemd/system/jitsi-videobridge2.service
/usr
/usr/share
/usr/share/doc
/usr/share/doc/jitsi-videobridge2
/usr/share/doc/jitsi-videobridge2/README.Debian
/usr/share/doc/jitsi-videobridge2/changelog.Debian.gz
/usr/share/doc/jitsi-videobridge2/copyright
/usr/share/jitsi-videobridge
/usr/share/jitsi-videobridge/collect-dump-logs.sh
/usr/share/jitsi-videobridge/graceful_shutdown.sh
/usr/share/jitsi-videobridge/jitsi-videobridge.jar
/usr/share/jitsi-videobridge/jvb.sh
/usr/share/jitsi-videobridge/lib
/usr/share/jitsi-videobridge/lib/annotations-24.1.0.jar
/usr/share/jitsi-videobridge/lib/aopalliance-repackaged-3.0.6.jar
/usr/share/jitsi-videobridge/lib/asm-9.9.1.jar
/usr/share/jitsi-videobridge/lib/asm-commons-9.9.1.jar
/usr/share/jitsi-videobridge/lib/asm-tree-9.9.1.jar
/usr/share/jitsi-videobridge/lib/bcpkix-jdk18on-1.83.jar
/usr/share/jitsi-videobridge/lib/bcprov-jdk18on-1.83.jar
/usr/share/jitsi-videobridge/lib/bctls-jdk18on-1.83.jar
/usr/share/jitsi-videobridge/lib/bcutil-jdk18on-1.83.jar
/usr/share/jitsi-videobridge/lib/cglib-nodep-2.2.jar
/usr/share/jitsi-videobridge/lib/checker-qual-3.43.0.jar
/usr/share/jitsi-videobridge/lib/commons-lang3-3.12.0.jar
/usr/share/jitsi-videobridge/lib/config-1.4.2.jar
/usr/share/jitsi-videobridge/lib/error_prone_annotations-2.36.0.jar
/usr/share/jitsi-videobridge/lib/failureaccess-1.0.2.jar
/usr/share/jitsi-videobridge/lib/guava-33.4.0-jre.jar
/usr/share/jitsi-videobridge/lib/hk2-api-3.0.6.jar
/usr/share/jitsi-videobridge/lib/hk2-locator-3.0.6.jar
/usr/share/jitsi-videobridge/lib/hk2-utils-3.0.6.jar
/usr/share/jitsi-videobridge/lib/ice4j-3.2-15-g6da2b08.jar
/usr/share/jitsi-videobridge/lib/j2objc-annotations-3.0.0.jar
/usr/share/jitsi-videobridge/lib/jackson-annotations-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jackson-core-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jackson-databind-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jackson-module-jakarta-xmlbind-annotations-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jackson-module-kotlin-2.19.4.jar
/usr/share/jitsi-videobridge/lib/jain-sip-ri-ossonly-1.2.279-jitsi-oss1.jar
/usr/share/jitsi-videobridge/lib/jakarta.activation-api-2.1.3.jar
/usr/share/jitsi-videobridge/lib/jakarta.annotation-api-2.1.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.el-api-5.0.0.jar
/usr/share/jitsi-videobridge/lib/jakarta.enterprise.cdi-api-4.0.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.enterprise.lang-model-4.0.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.inject-api-2.0.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.interceptor-api-2.1.0.jar
/usr/share/jitsi-videobridge/lib/jakarta.servlet-api-6.0.0.jar
/usr/share/jitsi-videobridge/lib/jakarta.transaction-api-2.0.1.jar
/usr/share/jitsi-videobridge/lib/jakarta.validation-api-3.0.2.jar
/usr/share/jitsi-videobridge/lib/jakarta.ws.rs-api-3.1.0.jar
/usr/share/jitsi-videobridge/lib/jakarta.xml.bind-api-4.0.2.jar
/usr/share/jitsi-videobridge/lib/java-sdp-nist-bridge-1.2.jar
/usr/share/jitsi-videobridge/lib/javassist-3.28.0-GA.jar
/usr/share/jitsi-videobridge/lib/jcl-core-2.8.jar
/usr/share/jitsi-videobridge/lib/jersey-client-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-common-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-container-jetty-http-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-container-servlet-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-container-servlet-core-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-entity-filtering-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-hk2-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-media-json-jackson-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jersey-server-3.1.11.jar
/usr/share/jitsi-videobridge/lib/jetty-alpn-client-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-client-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-annotations-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-plus-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-servlet-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-servlets-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-webapp-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-websocket-jetty-server-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-ee10-websocket-servlet-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-http-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-io-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-jndi-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-plus-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-proxy-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-rewrite-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-security-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-server-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-session-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-util-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-core-client-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-core-common-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-core-server-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-jetty-api-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-jetty-client-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-websocket-jetty-common-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jetty-xml-12.0.35.jar
/usr/share/jitsi-videobridge/lib/jicoco-config-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-health-checker-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-jetty-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-mediajson-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-metrics-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jicoco-mucclient-1.1-176-ge8384e2.jar
/usr/share/jitsi-videobridge/lib/jitsi-dcsctp-1.0-7-gb548df2.jar
/usr/share/jitsi-videobridge/lib/jitsi-media-transform-2.3-307-g4bb0aead1.jar
/usr/share/jitsi-videobridge/lib/jitsi-metaconfig-1.0-11-g8cf950e.jar
/usr/share/jitsi-videobridge/lib/jitsi-srtp-1.1-23-gaf3cd06.jar
/usr/share/jitsi-videobridge/lib/jitsi-utils-1.0-150-g4ab9a3b.jar
/usr/share/jitsi-videobridge/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar
/usr/share/jitsi-videobridge/lib/jna-5.9.0.jar
/usr/share/jitsi-videobridge/lib/jsr305-3.0.2.jar
/usr/share/jitsi-videobridge/lib/jxmpp-core-1.0.3.jar
/usr/share/jitsi-videobridge/lib/jxmpp-jid-1.0.3.jar
/usr/share/jitsi-videobridge/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar
/usr/share/jitsi-videobridge/lib/jxmpp-util-cache-1.0.3.jar
/usr/share/jitsi-videobridge/lib/kotlin-reflect-2.2.20.jar
/usr/share/jitsi-videobridge/lib/kotlin-stdlib-2.2.20.jar
/usr/share/jitsi-videobridge/lib/kotlin-stdlib-jdk7-1.9.10.jar
/usr/share/jitsi-videobridge/lib/kotlin-stdlib-jdk8-1.9.10.jar
/usr/share/jitsi-videobridge/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
/usr/share/jitsi-videobridge/lib/minidns-core-1.0.5.jar
/usr/share/jitsi-videobridge/lib/object-cloner-0.1.jar
/usr/share/jitsi-videobridge/lib/objenesis-2.1.jar
/usr/share/jitsi-videobridge/lib/osgi-resource-locator-1.0.3.jar
/usr/share/jitsi-videobridge/lib/pcap4j-core-1.8.2.jar
/usr/share/jitsi-videobridge/lib/pcap4j-packetfactory-static-1.8.2.jar
/usr/share/jitsi-videobridge/lib/precis-1.1.0.jar
/usr/share/jitsi-videobridge/lib/reflections-0.9.11.jar
/usr/share/jitsi-videobridge/lib/rtp-2.3-307-g4bb0aead1.jar
/usr/share/jitsi-videobridge/lib/sdp-api-1.0.jar
/usr/share/jitsi-videobridge/lib/sentry-7.20.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient-0.16.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient_common-0.16.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient_tracer_common-0.16.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient_tracer_otel-0.16.0.jar
/usr/share/jitsi-videobridge/lib/simpleclient_tracer_otel_agent-0.16.0.jar
/usr/share/jitsi-videobridge/lib/slf4j-api-2.0.16.jar
/usr/share/jitsi-videobridge/lib/slf4j-jdk14-2.0.16.jar
/usr/share/jitsi-videobridge/lib/smack-core-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-extensions-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-im-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-java8-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-resolver-javax-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-sasl-javax-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-streammanagement-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-tcp-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-xmlparser-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar
/usr/share/jitsi-videobridge/lib/smjni-jnigen-annotations-3.9.jar
/usr/share/jitsi-videobridge/lib/smjni-jnigen-processor-3.9.jar
/usr/share/jitsi-videobridge/lib/spotbugs-annotations-4.9.4.jar
/usr/share/jitsi-videobridge/lib/videobridge.rc
/usr/share/jitsi-videobridge/lib/weupnp-0.1.4.jar


## Package : prosody


```text
$ dpkg -L 'prosody' 2>/dev/null || true
```
/.
/etc
/etc/init.d
/etc/init.d/prosody
/etc/logrotate.d
/etc/logrotate.d/prosody
/etc/prosody
/etc/prosody/README
/etc/prosody/conf.avail
/etc/prosody/conf.avail/example.com.cfg.lua
/etc/prosody/conf.avail/localhost.cfg.lua
/etc/prosody/migrator.cfg.lua
/etc/prosody/prosody.cfg.lua
/usr
/usr/bin
/usr/bin/ejabberd2prosody
/usr/bin/prosody
/usr/bin/prosody-migrator
/usr/bin/prosodyctl
/usr/lib
/usr/lib/prosody
/usr/lib/prosody/core
/usr/lib/prosody/core/certmanager.lua
/usr/lib/prosody/core/configmanager.lua
/usr/lib/prosody/core/features.lua
/usr/lib/prosody/core/hostmanager.lua
/usr/lib/prosody/core/loggingmanager.lua
/usr/lib/prosody/core/moduleapi.lua
/usr/lib/prosody/core/modulemanager.lua
/usr/lib/prosody/core/portmanager.lua
/usr/lib/prosody/core/rostermanager.lua
/usr/lib/prosody/core/s2smanager.lua
/usr/lib/prosody/core/sessionmanager.lua
/usr/lib/prosody/core/stanza_router.lua
/usr/lib/prosody/core/statsmanager.lua
/usr/lib/prosody/core/storagemanager.lua
/usr/lib/prosody/core/usermanager.lua
/usr/lib/prosody/loader.lua
/usr/lib/prosody/modules
/usr/lib/prosody/modules/adhoc
/usr/lib/prosody/modules/adhoc/adhoc.lib.lua
/usr/lib/prosody/modules/adhoc/mod_adhoc.lua
/usr/lib/prosody/modules/mod_account_activity.lua
/usr/lib/prosody/modules/mod_admin_adhoc.lua
/usr/lib/prosody/modules/mod_admin_shell.lua
/usr/lib/prosody/modules/mod_admin_socket.lua
/usr/lib/prosody/modules/mod_admin_telnet.lua
/usr/lib/prosody/modules/mod_announce.lua
/usr/lib/prosody/modules/mod_auth_anonymous.lua
/usr/lib/prosody/modules/mod_auth_insecure.lua
/usr/lib/prosody/modules/mod_auth_internal_hashed.lua
/usr/lib/prosody/modules/mod_auth_internal_plain.lua
/usr/lib/prosody/modules/mod_auth_ldap.lua
/usr/lib/prosody/modules/mod_authz_internal.lua
/usr/lib/prosody/modules/mod_blocklist.lua
/usr/lib/prosody/modules/mod_bookmarks.lua
/usr/lib/prosody/modules/mod_bosh.lua
/usr/lib/prosody/modules/mod_c2s.lua
/usr/lib/prosody/modules/mod_carbons.lua
/usr/lib/prosody/modules/mod_cloud_notify.lua
/usr/lib/prosody/modules/mod_component.lua
/usr/lib/prosody/modules/mod_cron.lua
/usr/lib/prosody/modules/mod_csi.lua
/usr/lib/prosody/modules/mod_csi_simple.lua
/usr/lib/prosody/modules/mod_debug_reset.lua
/usr/lib/prosody/modules/mod_debug_sql.lua
/usr/lib/prosody/modules/mod_debug_stanzas
/usr/lib/prosody/modules/mod_debug_stanzas/watcher.lib.lua
/usr/lib/prosody/modules/mod_dialback.lua
/usr/lib/prosody/modules/mod_disco.lua
/usr/lib/prosody/modules/mod_external_services.lua
/usr/lib/prosody/modules/mod_flags.lua
/usr/lib/prosody/modules/mod_groups.lua
/usr/lib/prosody/modules/mod_http.lua
/usr/lib/prosody/modules/mod_http_altconnect.lua
/usr/lib/prosody/modules/mod_http_errors.lua
/usr/lib/prosody/modules/mod_http_file_share.lua
/usr/lib/prosody/modules/mod_http_files.lua
/usr/lib/prosody/modules/mod_http_openmetrics.lua
/usr/lib/prosody/modules/mod_invites.lua
/usr/lib/prosody/modules/mod_invites_adhoc.lua
/usr/lib/prosody/modules/mod_invites_register.lua
/usr/lib/prosody/modules/mod_iq.lua
/usr/lib/prosody/modules/mod_lastactivity.lua
/usr/lib/prosody/modules/mod_legacyauth.lua
/usr/lib/prosody/modules/mod_limits.lua
/usr/lib/prosody/modules/mod_mam
/usr/lib/prosody/modules/mod_mam/mamprefs.lib.lua
/usr/lib/prosody/modules/mod_mam/mamprefsxml.lib.lua
/usr/lib/prosody/modules/mod_mam/mod_mam.lua
/usr/lib/prosody/modules/mod_message.lua
/usr/lib/prosody/modules/mod_mimicking.lua
/usr/lib/prosody/modules/mod_motd.lua
/usr/lib/prosody/modules/mod_muc_mam.lua
/usr/lib/prosody/modules/mod_muc_unique.lua
/usr/lib/prosody/modules/mod_net_multiplex.lua
/usr/lib/prosody/modules/mod_offline.lua
/usr/lib/prosody/modules/mod_pep.lua
/usr/lib/prosody/modules/mod_pep_plus.lua
/usr/lib/prosody/modules/mod_pep_simple.lua
/usr/lib/prosody/modules/mod_ping.lua
/usr/lib/prosody/modules/mod_posix.lua
/usr/lib/prosody/modules/mod_presence.lua
/usr/lib/prosody/modules/mod_private.lua
/usr/lib/prosody/modules/mod_proxy65.lua
/usr/lib/prosody/modules/mod_pubsub
/usr/lib/prosody/modules/mod_pubsub/commands.lib.lua
/usr/lib/prosody/modules/mod_pubsub/mod_pubsub.lua
/usr/lib/prosody/modules/mod_pubsub/pubsub.lib.lua
/usr/lib/prosody/modules/mod_register.lua
/usr/lib/prosody/modules/mod_register_ibr.lua
/usr/lib/prosody/modules/mod_register_limits.lua
/usr/lib/prosody/modules/mod_roster.lua
/usr/lib/prosody/modules/mod_s2s.lua
/usr/lib/prosody/modules/mod_s2s_auth_certs.lua
/usr/lib/prosody/modules/mod_s2s_auth_dane_in.lua
/usr/lib/prosody/modules/mod_s2s_bidi.lua
/usr/lib/prosody/modules/mod_saslauth.lua
/usr/lib/prosody/modules/mod_scansion_record.lua
/usr/lib/prosody/modules/mod_server_contact_info.lua
/usr/lib/prosody/modules/mod_server_info.lua
/usr/lib/prosody/modules/mod_smacks.lua
/usr/lib/prosody/modules/mod_stanza_debug.lua
/usr/lib/prosody/modules/mod_storage_internal.lua
/usr/lib/prosody/modules/mod_storage_memory.lua
/usr/lib/prosody/modules/mod_storage_none.lua
/usr/lib/prosody/modules/mod_storage_sql.lua
/usr/lib/prosody/modules/mod_storage_xep0227.lua
/usr/lib/prosody/modules/mod_time.lua
/usr/lib/prosody/modules/mod_tls.lua
/usr/lib/prosody/modules/mod_tokenauth.lua
/usr/lib/prosody/modules/mod_tombstones.lua
/usr/lib/prosody/modules/mod_turn_external.lua
/usr/lib/prosody/modules/mod_unknown.lua
/usr/lib/prosody/modules/mod_uptime.lua
/usr/lib/prosody/modules/mod_user_account_management.lua
/usr/lib/prosody/modules/mod_vcard.lua
/usr/lib/prosody/modules/mod_vcard4.lua
/usr/lib/prosody/modules/mod_vcard_legacy.lua
/usr/lib/prosody/modules/mod_version.lua
/usr/lib/prosody/modules/mod_watchregistrations.lua
/usr/lib/prosody/modules/mod_websocket.lua
/usr/lib/prosody/modules/mod_welcome.lua
/usr/lib/prosody/modules/mod_windows.lua
/usr/lib/prosody/modules/muc
/usr/lib/prosody/modules/muc/config_form_sections.lib.lua
/usr/lib/prosody/modules/muc/description.lib.lua
/usr/lib/prosody/modules/muc/hats.lib.lua
/usr/lib/prosody/modules/muc/hidden.lib.lua
/usr/lib/prosody/modules/muc/history.lib.lua
/usr/lib/prosody/modules/muc/language.lib.lua
/usr/lib/prosody/modules/muc/lock.lib.lua
/usr/lib/prosody/modules/muc/members_only.lib.lua
/usr/lib/prosody/modules/muc/mod_muc.lua
/usr/lib/prosody/modules/muc/moderated.lib.lua
/usr/lib/prosody/modules/muc/muc.lib.lua
/usr/lib/prosody/modules/muc/name.lib.lua
/usr/lib/prosody/modules/muc/occupant.lib.lua
/usr/lib/prosody/modules/muc/occupant_id.lib.lua
/usr/lib/prosody/modules/muc/password.lib.lua
/usr/lib/prosody/modules/muc/persistent.lib.lua
/usr/lib/prosody/modules/muc/presence_broadcast.lib.lua
/usr/lib/prosody/modules/muc/register.lib.lua
/usr/lib/prosody/modules/muc/request.lib.lua
/usr/lib/prosody/modules/muc/restrict_pm.lib.lua
/usr/lib/prosody/modules/muc/subject.lib.lua
/usr/lib/prosody/modules/muc/util.lib.lua
/usr/lib/prosody/modules/muc/vcard.lib.lua
/usr/lib/prosody/modules/muc/whois.lib.lua
/usr/lib/prosody/net
/usr/lib/prosody/net/adns.lua
/usr/lib/prosody/net/connect.lua
/usr/lib/prosody/net/cqueues.lua
/usr/lib/prosody/net/dns.lua
/usr/lib/prosody/net/http
/usr/lib/prosody/net/http/codes.lua
/usr/lib/prosody/net/http/errors.lua
/usr/lib/prosody/net/http/files.lua
/usr/lib/prosody/net/http/parser.lua
/usr/lib/prosody/net/http/server.lua
/usr/lib/prosody/net/http.lua
/usr/lib/prosody/net/resolvers
/usr/lib/prosody/net/resolvers/basic.lua
/usr/lib/prosody/net/resolvers/chain.lua
/usr/lib/prosody/net/resolvers/manual.lua
/usr/lib/prosody/net/resolvers/service.lua
/usr/lib/prosody/net/server.lua
/usr/lib/prosody/net/server_epoll.lua
/usr/lib/prosody/net/server_event.lua
/usr/lib/prosody/net/server_select.lua
/usr/lib/prosody/net/stun.lua
/usr/lib/prosody/net/tls_luasec.lua
/usr/lib/prosody/net/unbound.lua
/usr/lib/prosody/net/websocket
/usr/lib/prosody/net/websocket/frames.lua
/usr/lib/prosody/net/websocket.lua
/usr/lib/prosody/prosody.version
/usr/lib/prosody/util
/usr/lib/prosody/util/adhoc.lua
/usr/lib/prosody/util/adminstream.lua
/usr/lib/prosody/util/argparse.lua
/usr/lib/prosody/util/array.lua
/usr/lib/prosody/util/async.lua
/usr/lib/prosody/util/bit53.lua
/usr/lib/prosody/util/bitcompat.lua
/usr/lib/prosody/util/cache.lua
/usr/lib/prosody/util/caps.lua
/usr/lib/prosody/util/compat.so
/usr/lib/prosody/util/crypto.so
/usr/lib/prosody/util/dataforms.lua
/usr/lib/prosody/util/datamanager.lua
/usr/lib/prosody/util/datamapper.lua
/usr/lib/prosody/util/datetime.lua
/usr/lib/prosody/util/dbuffer.lua
/usr/lib/prosody/util/debug.lua
/usr/lib/prosody/util/dependencies.lua
/usr/lib/prosody/util/dns.lua
/usr/lib/prosody/util/dnsregistry.lua
/usr/lib/prosody/util/encodings.so
/usr/lib/prosody/util/envload.lua
/usr/lib/prosody/util/erlparse.lua
/usr/lib/prosody/util/error.lua
/usr/lib/prosody/util/events.lua
/usr/lib/prosody/util/filters.lua
/usr/lib/prosody/util/format.lua
/usr/lib/prosody/util/fsm.lua
/usr/lib/prosody/util/gc.lua
/usr/lib/prosody/util/hashes.so
/usr/lib/prosody/util/hashring.lua
/usr/lib/prosody/util/helpers.lua
/usr/lib/prosody/util/hex.lua
/usr/lib/prosody/util/hmac.lua
/usr/lib/prosody/util/http.lua
/usr/lib/prosody/util/human
/usr/lib/prosody/util/human/io.lua
/usr/lib/prosody/util/human/units.lua
/usr/lib/prosody/util/id.lua
/usr/lib/prosody/util/import.lua
/usr/lib/prosody/util/indexedbheap.lua
/usr/lib/prosody/util/interpolation.lua
/usr/lib/prosody/util/ip.lua
/usr/lib/prosody/util/iterators.lua
/usr/lib/prosody/util/jid.lua
/usr/lib/prosody/util/json.lua
/usr/lib/prosody/util/jsonpointer.lua
/usr/lib/prosody/util/jsonschema.lua
/usr/lib/prosody/util/jwt.lua
/usr/lib/prosody/util/logger.lua
/usr/lib/prosody/util/mathcompat.lua
/usr/lib/prosody/util/mercurial.lua
/usr/lib/prosody/util/multitable.lua
/usr/lib/prosody/util/net.so
/usr/lib/prosody/util/openmetrics.lua
/usr/lib/prosody/util/openssl.lua
/usr/lib/prosody/util/paseto.lua
/usr/lib/prosody/util/paths.lua
/usr/lib/prosody/util/pluginloader.lua
/usr/lib/prosody/util/poll.so
/usr/lib/prosody/util/pposix.so
/usr/lib/prosody/util/presence.lua
/usr/lib/prosody/util/promise.lua
/usr/lib/prosody/util/prosodyctl
/usr/lib/prosody/util/prosodyctl/cert.lua
/usr/lib/prosody/util/prosodyctl/check.lua
/usr/lib/prosody/util/prosodyctl/shell.lua
/usr/lib/prosody/util/prosodyctl.lua
/usr/lib/prosody/util/pubsub.lua
/usr/lib/prosody/util/queue.lua
/usr/lib/prosody/util/random.lua
/usr/lib/prosody/util/ringbuffer.so
/usr/lib/prosody/util/roles.lua
/usr/lib/prosody/util/rsm.lua
/usr/lib/prosody/util/sasl
/usr/lib/prosody/util/sasl/anonymous.lua
/usr/lib/prosody/util/sasl/external.lua
/usr/lib/prosody/util/sasl/oauthbearer.lua
/usr/lib/prosody/util/sasl/plain.lua
/usr/lib/prosody/util/sasl/scram.lua
/usr/lib/prosody/util/sasl.lua
/usr/lib/prosody/util/serialization.lua
/usr/lib/prosody/util/session.lua
/usr/lib/prosody/util/set.lua
/usr/lib/prosody/util/signal.so
/usr/lib/prosody/util/smqueue.lua
/usr/lib/prosody/util/sql.lua
/usr/lib/prosody/util/sqlite3.lua
/usr/lib/prosody/util/sslconfig.lua
/usr/lib/prosody/util/stanza.lua
/usr/lib/prosody/util/startup.lua
/usr/lib/prosody/util/statistics.lua
/usr/lib/prosody/util/statsd.lua
/usr/lib/prosody/util/strbitop.so
/usr/lib/prosody/util/struct.so
/usr/lib/prosody/util/table.so
/usr/lib/prosody/util/template.lua
/usr/lib/prosody/util/termcolours.lua
/usr/lib/prosody/util/throttle.lua
/usr/lib/prosody/util/time.so
/usr/lib/prosody/util/timer.lua
/usr/lib/prosody/util/uuid.lua
/usr/lib/prosody/util/watchdog.lua
/usr/lib/prosody/util/x509.lua
/usr/lib/prosody/util/xml.lua
/usr/lib/prosody/util/xmppstream.lua
/usr/lib/prosody/util/xpcall.lua
/usr/lib/prosody/util/xtemplate.lua
/usr/lib/systemd
/usr/lib/systemd/system
/usr/lib/systemd/system/prosody.service
/usr/share
/usr/share/doc
/usr/share/doc/prosody
/usr/share/doc/prosody/AUTHORS
/usr/share/doc/prosody/HACKERS
/usr/share/doc/prosody/README
/usr/share/doc/prosody/changelog.Debian.gz
/usr/share/doc/prosody/changelog.gz
/usr/share/doc/prosody/copyright
/usr/share/doc/prosody/doc
/usr/share/doc/prosody/doc/coding_style.md.gz
/usr/share/doc/prosody/doc/doap.xml.gz
/usr/share/doc/prosody/doc/hgrc-email.ini
/usr/share/doc/prosody/doc/hgrc.ini
/usr/share/doc/prosody/doc/names.txt
/usr/share/doc/prosody/doc/net.server.lua.gz
/usr/share/doc/prosody/doc/roster_format.txt
/usr/share/doc/prosody/doc/session.txt
/usr/share/doc/prosody/doc/stanza.txt
/usr/share/doc/prosody/doc/stanza_routing.txt
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/prosody
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/prosodyctl.1.gz
/usr/share/man/man8
/usr/share/man/man8/ejabberd2prosody.8.gz
/usr/share/man/man8/prosody-migrator.8.gz
/usr/share/man/man8/prosody.8.gz


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
/.
/usr
/usr/sbin
/usr/sbin/nginx
/usr/share
/usr/share/doc
/usr/share/doc/nginx
/usr/share/doc/nginx/changelog.Debian.gz
/usr/share/doc/nginx/changelog.gz
/usr/share/doc/nginx/copyright
/usr/share/man
/usr/share/man/man8
/usr/share/man/man8/nginx.8.gz



---

# 32. DÉPENDANCES DES PAQUETS

**Date :** 2026-08-08 06:56:40 EDT


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

**Date :** 2026-08-08 06:56:41 EDT


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
openjdk version "21.0.11" 2026-04-21
OpenJDK Runtime Environment (build 21.0.11+10-1-deb13u2-Debian)
OpenJDK 64-Bit Server VM (build 21.0.11+10-1-deb13u2-Debian, mixed mode, sharing)


```text
$ node -v 2>/dev/null || true
```


```text
$ prosodyctl --version 2>/dev/null || true
```
prosodyctl - Manage a Prosody server

Usage: /usr/bin/prosodyctl COMMAND [OPTIONS]

Where COMMAND may be one of:

Process management:
 reload            Reload Prosody's configuration and re-open log files
 status            Reports the running status of Prosody
 shell             Interact with a running Prosody

User management:
 adduser JID       Create the specified user account in Prosody
 passwd JID        Set the password for the specified user account in Prosody
 deluser JID       Permanently remove the specified user account from Prosody

Plugin management:
 install           Installs a prosody/luarocks plugin
 remove            Removes a module installed in the working directory's plugins folder
 list              Shows installed rocks

Informative:
 check             Perform basic checks on your Prosody installation
 version [-v]      Show current Prosody version, or more

Other:
 cert              Certificate management commands
 about             Show information about this Prosody installation



---

# 34. RÉSUMÉ AUTOMATIQUE

**Date :** 2026-08-08 06:56:41 EDT


## Services détectés


```text
$ systemctl list-unit-files 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|jvb|coturn|turnserver|nginx" || true
```
coturn.service                                                                enabled         enabled
jicofo.service                                                                generated       -
jitsi-videobridge2.service                                                    enabled         enabled
nginx.service                                                                 enabled         enabled
prosody.service                                                               enabled         enabled


## Ports détectés


```text
$ ss -lntup 2>/dev/null | grep -Ei "java|prosody|nginx|turn|jitsi|node" || true
```
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=143))                                                                                               
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=142))                                                                                               
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=141))                                                                                               
udp   UNCONN 0      0      [::ffff:192.168.1.64]:10000            *:*    users:(("java",pid=1162,fd=140))                                                                                               
tcp   LISTEN 0      511                  0.0.0.0:80         0.0.0.0:*    users:(("nginx",pid=1199,fd=5),("nginx",pid=1198,fd=5),("nginx",pid=1197,fd=5),("nginx",pid=1195,fd=5),("nginx",pid=1194,fd=5))
tcp   LISTEN 0      511                  0.0.0.0:443        0.0.0.0:*    users:(("nginx",pid=1199,fd=7),("nginx",pid=1198,fd=7),("nginx",pid=1197,fd=7),("nginx",pid=1195,fd=7),("nginx",pid=1194,fd=7))
tcp   LISTEN 0      50                         *:9090             *:*    users:(("java",pid=1162,fd=148))                                                                                               
tcp   LISTEN 0      511                     [::]:80            [::]:*    users:(("nginx",pid=1199,fd=6),("nginx",pid=1198,fd=6),("nginx",pid=1197,fd=6),("nginx",pid=1195,fd=6),("nginx",pid=1194,fd=6))
tcp   LISTEN 0      511                     [::]:443           [::]:*    users:(("nginx",pid=1199,fd=8),("nginx",pid=1198,fd=8),("nginx",pid=1197,fd=8),("nginx",pid=1195,fd=8),("nginx",pid=1194,fd=8))
tcp   LISTEN 0      50        [::ffff:127.0.0.1]:8080             *:*    users:(("java",pid=1162,fd=155))                                                                                               
tcp   LISTEN 0      4096      [::ffff:127.0.0.1]:8888             *:*    users:(("java",pid=786,fd=116))                                                                                                


## Processus détectés


```text
$ ps auxww 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|jvb|turnserver|coturn|nginx" | grep -v grep || true
```
jicofo       786  0.3  2.1 6870052 216248 ?      Sl   02:22   0:51 java -Xmx3072m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=jicofo -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/jicofo/logging.properties -Dconfig.file=/etc/jitsi/jicofo/jicofo.conf -cp /usr/share/jicofo/jicofo.jar:/usr/share/jicofo/lib/alpn-api-1.1.3.v20160715.jar:/usr/share/jicofo/lib/annotations-23.0.0.jar:/usr/share/jicofo/lib/bcpkix-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcprov-jdk18on-1.83.jar:/usr/share/jicofo/lib/bcutil-jdk18on-1.83.jar:/usr/share/jicofo/lib/commons-lang3-3.12.0.jar:/usr/share/jicofo/lib/config-1.4.3.jar:/usr/share/jicofo/lib/gson-2.8.5.jar:/usr/share/jicofo/lib/jackson-annotations-2.19.0.jar:/usr/share/jicofo/lib/jackson-core-2.18.0.jar:/usr/share/jicofo/lib/jackson-databind-2.18.0.jar:/usr/share/jicofo/lib/jackson-module-kotlin-2.19.0.jar:/usr/share/jicofo/lib/jansi-2.4.1.jar:/usr/share/jicofo/lib/jicoco-config-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-health-checker-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-jwt-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicoco-metrics-1.1-171-gb3b9e1f.jar:/usr/share/jicofo/lib/jicofo-common-1.0-1189.jar:/usr/share/jicofo/lib/jicofo-selector-1.0-1189.jar:/usr/share/jicofo/lib/jitsi-metaconfig-1.0-9-g5e1b624.jar:/usr/share/jicofo/lib/jitsi-utils-1.0-150-g4ab9a3b.jar:/usr/share/jicofo/lib/jitsi-xmpp-extensions-1.0-116-gc47d314.jar:/usr/share/jicofo/lib/jjwt-api-0.12.6.jar:/usr/share/jicofo/lib/jjwt-impl-0.12.6.jar:/usr/share/jicofo/lib/jjwt-jackson-0.12.6.jar:/usr/share/jicofo/lib/jna-5.9.0.jar:/usr/share/jicofo/lib/jsr305-3.0.2.jar:/usr/share/jicofo/lib/jxmpp-core-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-jid-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-stringprep-rocksxmppprecis-1.0.3.jar:/usr/share/jicofo/lib/jxmpp-util-cache-1.0.3.jar:/usr/share/jicofo/lib/kotlin-reflect-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-2.0.20.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk7-1.9.10.jar:/usr/share/jicofo/lib/kotlin-stdlib-jdk8-1.9.10.jar:/usr/share/jicofo/lib/kotlinx-coroutines-core-jvm-1.9.0.jar:/usr/share/jicofo/lib/kotlinx-io-bytestring-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-io-core-jvm-0.5.4.jar:/usr/share/jicofo/lib/kotlinx-serialization-core-jvm-1.7.3.jar:/usr/share/jicofo/lib/ktor-events-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-cio-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-http-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-io-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-network-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jackson-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-serialization-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-content-negotiation-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-core-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-netty-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-server-status-pages-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-utils-jvm-3.0.0.jar:/usr/share/jicofo/lib/ktor-websockets-jvm-3.0.0.jar:/usr/share/jicofo/lib/minidns-core-1.0.5.jar:/usr/share/jicofo/lib/netty-buffer-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http2-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-codec-http-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-common-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-handler-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-resolver-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-classes-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-epoll-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-kqueue-4.1.114.Final.jar:/usr/share/jicofo/lib/netty-transport-native-unix-common-4.1.114.Final.jar:/usr/share/jicofo/lib/precis-1.1.0.jar:/usr/share/jicofo/lib/sentry-5.4.0.jar:/usr/share/jicofo/lib/simpleclient-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_common-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel-0.16.0.jar:/usr/share/jicofo/lib/simpleclient_tracer_otel_agent-0.16.0.jar:/usr/share/jicofo/lib/slf4j-api-1.7.32.jar:/usr/share/jicofo/lib/slf4j-jdk14-1.7.32.jar:/usr/share/jicofo/lib/smack-core-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-extensions-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-im-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-java8-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-resolver-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-sasl-javax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-streammanagement-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-tcp-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/smack-xmlparser-stax-4.4.8-jitsi-4.jar:/usr/share/jicofo/lib/spotbugs-annotations-4.8.6.jar org.jitsi.jicofo.Main
prosody     1161  0.3  0.2  68968 29564 ?        Ss   02:22   1:05 lua5.4 /usr/bin/prosody -F
jvb         1162  0.4  2.5 6887016 252912 ?      Ssl  02:22   1:20 java -Xmx3072m -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp -Djdk.tls.ephemeralDHKeySize=2048 -Dconfig.file=/etc/jitsi/videobridge/jvb.conf -Dnet.java.sip.communicator.SC_HOME_DIR_LOCATION=/etc/jitsi -Dnet.java.sip.communicator.SC_HOME_DIR_NAME=videobridge -Dnet.java.sip.communicator.SC_LOG_DIR_LOCATION=/var/log/jitsi -Djava.util.logging.config.file=/etc/jitsi/videobridge/logging.properties -cp /usr/share/jitsi-videobridge/jitsi-videobridge.jar:/usr/share/jitsi-videobridge/lib/* org.jitsi.videobridge.MainKt
root        1194  0.0  0.0  26028  3132 ?        Ss   02:22   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    1195  0.0  0.1  27980 10912 ?        S    02:22   0:00 nginx: worker process
www-data    1197  0.0  0.0  27608  9636 ?        S    02:22   0:00 nginx: worker process
www-data    1198  0.0  0.1  27872 10816 ?        S    02:22   0:00 nginx: worker process
www-data    1199  0.0  0.0  27448  9688 ?        S    02:22   0:00 nginx: worker process
civitas     6280  0.0  1.5 1513564 154100 ?      Ssl  02:24   0:00 /usr/bin/xwaylandvideobridge
root       91754  0.3  0.0  21812  8004 pts/2    S+   06:56   0:00 sudo /opt/civitas/jitsi-infrastructure-audit.sh
root       91756  0.0  0.0  21812  2692 pts/3    Ss   06:56   0:00 sudo /opt/civitas/jitsi-infrastructure-audit.sh
root       91757  2.3  0.0   7208  3468 pts/3    S+   06:56   0:00 bash /opt/civitas/jitsi-infrastructure-audit.sh
root       94222  0.0  0.0   5576  1904 pts/3    S+   06:56   0:00 tee -a /opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md


---

# FIN DE L'AUDIT

**Date de fin :** 2026-08-08 06:56:42 EDT

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

