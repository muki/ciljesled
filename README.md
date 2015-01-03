demo: http://muki.webfactional.com/ciljesled/

Ciljesled
=========

### Ciljesled je eksperiment

Ob novem letu vsi na veliko sprejemamo zaobljube, vendar jih manj kot 10% uspešno izpeljemo. Ciljesled želi pomagati.

### Ciljesled ni tečen

Zdizajnan je tako, da lahko nanj pozabiš. Vpiši svoje cilje, Ciljesled bo poskrbel za vse ostalo. Sprosti se, vse bo OK.

Ko si izbereš cilj, Ciljesledu poveš, do kdaj ga želiš doseči. Ciljesledov algoritem, inspiriran s strani sistemov za učenje novih jezikov poskrbi, da te v inboxu vsake toliko pričaka mail, s katerim te Ciljesled spomni na tvoje cilje.

### Inštalacija

Dodaj django app, ki ga najdeš v <code>ciljesled_django</code>. Zveži URLje v svojem url.py in nastavi crontask: <code>0 7 * * * curl http://link.do/ciljesled/sendemails/</code>.

Fajle iz <code>ciljesled</code> oz. <code>goalpost</code> (odvisno od jezika, ki si ga želiš) postavi nekam, kjer ti odgovarjajo in uredi linke pri ajax klicih. Ne pozabi ustvariti FB appa in spremeniti ID.

Goalpost
========

### Goalpost is an experiment

New year's resolution are back in fashion, even if less than 10% of them are followed through to the end. Goalpost is here to help.

### Goalpost is not annoying

It's designed so you can forget about it. Enter your goals and let Goalpost take care of the rest. Relax, everything will be OK.

When you set a goal, you give it a deadline. Goalpost's algorithm, inspired by some language learning practices makes sure you get an email delivered to you every now and then, reminding you of your goals.

### Installation

Add the django app found in <code>ciljesled_django</code>. Add URLs to your <code>url.py</code> and set up a crontask: <code>0 7 * * * curl http://link.to/goalpost/sendemails/</code>.

Copy files from <code>goalpost</code> and/or <code>ciljesled</code> (depending on your language preference) to a place you like and make sure to check the URLs for all the AJAX calls. Don't forget to set up a FB app and change the ID.
