# mrutools

Desktop Linux MRU Forensic Tool

MRUTools is a plugin based tool for desktop linux (kde, gnome, ...).

Each plugin extracts MRU information from certain applications or desktops.

The application is yet on (early) active development. 

Available features:
- Three actual plugins written: kde, gwenview and dragonplayer
- PDF output
- stdout output

Some of the future features will be:

- Several output formats (txt, csv, xml, etc).
- Both forensic (information gathering and retrieval) and antiforensic (information tampering) modes.
- Timeline charts, even plaso compatibility.
- setup.py install script (automagic dependencies install)
- Plugins, plugins for everything: vlc, kate, gnome apps (I'm more a kde user myself :P).

##How does it work?

MRUTools is built upon a simple plugin structure. I know there are more serious and complex plugin architectures out there, but for our purposes (and for now) this will work.
Each plugin resides in a folder named after itself, in the plugins folder.
The main class loads and executes the \__init__.py file found inside each folder, while passing it a dictionary with the information that has been found at the moment.
The loaded plugin then extracts the MRU information, appends it to the current list, adds the new key:list pair to the dictionary and finishes execution.

Once every plugin has been executed, the main class processes the gathered information and renders the desired output.

If you like the idea, suggest or write a plugin, new feature/whatever and pull request!

##Example output
```
n0w@nLap:~/Documents/LiClipse Workspace/mrutools/src$ python mrutools.py --stdout
MRUTools - v0.3
           Angel Suarez-B (n0w) 

[+] Found 2 plugin(s)!
 |---> kde... running... [OK: retrieved 10 elements]
 |---> gwenview... running... [OK: retrieved 13 elements]
 |  Name: Boardwalk.Empire.S01E03.Broadway.Limited.HDTV.XviD-FQM.avi
 |  Last Access Date: 2015-04-06 22:29:11.441080
 |  Last Modification Date: 2015-04-06 22:29:11.433084
 |  URL: file://$HOME/Boardwalk.Empire.S01E03.Broadway.Limited.HDTV.XviD-FQM.avi
 |  Last opened with: kfilemodule
 |
 |  Name: Boardwalk.Empire.S01E03.Broadway.Limited.HDTV.XviD-FQM.avi
 |  Last Access Date: 2015-04-06 22:42:54.008550
 |  Last Modification Date: 2015-04-06 22:42:53.508550
 |  URL: file://$HOME/Boardwalk.Empire.S01E03.Broadway.Limited.HDTV.XviD-FQM.avi
 |  Last opened with: vlc
 |
 |  Name: Boardwalk.Empire.S01E02.The.Ivory.Tower.HDTV.XviD-FQM.avi
 |  Last Access Date: 2015-04-07 17:34:39.909199
 |  Last Modification Date: 2015-04-06 15:59:13.710573
 |  URL: file://$HOME/Boardwalk.Empire.S01E02.The.Ivory.Tower.HDTV.XviD-FQM.avi
 |  Last opened with: vlc
 |
 |  Name: Memoria de Actividades.pdf
 |  Last Access Date: 2015-04-07 17:37:00.565192
 |  Last Modification Date: 2015-04-07 17:37:00.561193
 |  URL: file://$HOME/Public/Memoria%20de%20Actividades.pdf
 |  Last opened with: okularapplication_pdf
 |
 |  Name: Boardwalk.Empire.S01E04.HDTV.XviD-2HD.avi
 |  Last Access Date: 2015-04-06 22:29:31.235177
 |  Last Modification Date: 2015-04-06 22:29:31.231179
 |  URL: file://$HOME/Boardwalk.Empire.S01E04.HDTV.XviD-2HD.avi
 |  Last opened with: kfilemodule
 |
 |  Name: Boardwalk.Empire.S01E02.The.Ivory.Tower.HDTV.XviD-FQM.avi
 |  Last Access Date: 2015-04-07 17:34:39.909199
 |  Last Modification Date: 2015-04-06 15:58:51.649610
 |  URL: file://$HOME/Boardwalk.Empire.S01E02.The.Ivory.Tower.HDTV.XviD-FQM.avi
 |  Last opened with: kfilemodule
 |
 |  Name: MRUtools report Tue Apr  7 18:01:05 2015
 |  Last Access Date: 2015-04-07 18:01:32.733124
 |  Last Modification Date: 2015-04-07 18:01:32.729125
 |  URL: file://$HOME/Documents/LiClipse%20Workspace/mrutools/src/MRUtools%20report%20Tue%20Apr%20%207%2018:01:05%202015
 |  Last opened with: okularapplication_pdf
 |
 |  Name: angel.png
 |  Last Access Date: 2015-04-07 17:34:39.913199
 |  Last Modification Date: 2015-04-07 17:34:39.909199
 |  URL: file://$HOME/Public/angel.png
 |  Last opened with: ksnapshot
 |
 |  Name: Boardwalk.Empire.S01E01.Boardwalk.Empire.HDTV.XviD-FQM.avi
 |  Last Access Date: 2015-04-07 17:34:39.909199
 |  Last Modification Date: 2015-04-06 15:24:05.831033
 |  URL: file://$HOME/Boardwalk.Empire.S01E01.Boardwalk.Empire.HDTV.XviD-FQM.avi
 |  Last opened with: vlc
 |
 |  Name: Dropbox
 |  Last Access Date: 2015-04-07 17:34:39.909199
 |  Last Modification Date: 2015-04-06 15:20:01.115044
 |  URL: file://$HOME/Dropbox
 |  Last opened with: dolphin
 |
 |  Last Access Date: 2015-01-03 13:20:52
 |  URL: file:///home/n0w/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2014-12-01 20:16:12
 |  URL: file:///home/n0w/Downloads/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2014-11-15 14:20:46
 |  URL: file:///home/n0w/Pictures/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2015-03-21 21:32:09
 |  URL: file:///home/n0w/Master/Analisis%20Forense/Screenshots_evaluacion/Lab6%20-%20lin/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2015-01-18 20:51:49
 |  URL: file:///home/n0w/BQ_Datos_13Dec2014/Backup_Datos/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2014-12-25 21:54:32
 |  URL: file:///home/n0w/Dropbox/PFM/Andres%20Info1/Capturas_Tacno_IoT_Book/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2014-12-01 21:12:23
 |  URL: file:///home/n0w/Public/Regin/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2014-12-01 16:05:07
 |  URL: file:///home/n0w/Master/Analisis%20Forense/Screenshots_evaluacion/Lab1/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2015-01-15 17:32:57
 |  URL: file:///home/n0w/Downloads/Ficha_proyecto/Ejemplo/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2014-12-28 20:47:46
 |  URL: file:///home/n0w/Dropbox/PFM/EDUP/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2014-11-11 21:14:20
 |  URL: file:///home/n0w/Trabajo/Incidente%20Correo%2011-11-2014/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2015-04-05 00:08:19
 |  URL: file:///home/n0w/Fotos%20Irene/DCIM/100PHOTO/
 |  Last opened with: gwenview
 |
 |  Last Access Date: 2015-03-21 20:21:02
 |  URL: file:///home/n0w/Master/Analisis%20Forense/Linux/screenshots/
 |  Last opened with: gwenview
```
