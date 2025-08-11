# -------------------------------------------------------------------
# DorkMaster.py - VERSIÓN 0.3
# Por: TomDoe (basado en el script original)
# Fecha de revisión: 2025-08-11
# -------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, Listbox, MULTIPLE, END
import webbrowser
import json
import time
from datetime import datetime
import re
import urllib.parse
import threading

# ===================================================================
# DORKS CATEGORIZADOS - CORREGIDOS Y AMPLIADOS PARA MEJOR FUNCIONAMIENTO
# ===================================================================
DORKS_CATEGORIZADOS = {
    "Redes Sociales": [
        'site:linkedin.com/in "{nombre} {apellido}"',
        'site:linkedin.com/pub "{nombre} {apellido}"',
        'site:facebook.com "{nombre} {apellido}"',
        'site:facebook.com "{nombre} {apellido}" {ciudad}',
        'site:facebook.com "{nombre} {apellido}" {pais}',
        'site:twitter.com "{nombre} {apellido}"',
        'site:instagram.com "{nombre} {apellido}"',
        'site:tiktok.com "{nombre} {apellido}"',
        'site:youtube.com "{nombre} {apellido}"',
        'site:pinterest.com "{nombre} {apellido}"',
        'site:reddit.com "{nombre} {apellido}"',
        'site:vk.com "{nombre} {apellido}"',
        'site:ok.ru "{nombre} {apellido}"',
        'site:tumblr.com "{nombre} {apellido}"',
        'site:flickr.com "{nombre} {apellido}"',
        'site:about.me "{nombre} {apellido}"',
        'site:slideshare.net "{nombre} {apellido}"',
        'site:medium.com "{nombre} {apellido}"',
        'site:quora.com "{nombre} {apellido}"',
        'site:behance.net "{nombre} {apellido}"',
        'site:dribbble.com "{nombre} {apellido}"',
        'site:xing.com "{nombre} {apellido}"',
        'site:viadeo.com "{nombre} {apellido}"',
        '"{nombre} {apellido}" site:plus.google.com',
        'allintext:"{nombre} {apellido}" site:facebook.com/groups',
        'allintext:"{nombre} {apellido}" site:twitter.com/lists',
        'allintext:"{nombre} {apellido}" site:reddit.com/r/',
        'site:soundcloud.com "{nombre} {apellido}"',
        'site:vimeo.com "{nombre} {apellido}"',
        'site:myspace.com "{nombre} {apellido}"',
        'site:last.fm "{nombre} {apellido}"',
        'site:devianart.com "{nombre} {apellido}"',
        'site:steamcommunity.com/id/ "{alias1}"',
        'site:steamcommunity.com/search/users "{nombre} {apellido}"',
        'site:twitch.tv "{nombre} {apellido}"',
        'site:ask.fm "{nombre} {apellido}"',
        'site:gravatar.com "{email}"',
        'site:telegram.me "{alias1}"',
        'site:t.me/s/ "{alias1}"',
        'site:keybase.io "{nombre} {apellido}"',
        '"{nombre} {apellido}" site:facebook.com "posts"',
        '"{nombre} {apellido}" site:twitter.com "status"',
        '"{nombre} {apellido}" site:instagram.com "post"',
        '"{nombre} {apellido}" site:disqus.com',
        '"{nombre} {apellido}" site:wattpad.com',
        '"{nombre} {apellido}" site:goodreads.com',
        '"{nombre} {apellido}" site:meetup.com',
        '"{nombre} {apellido}" site:classmates.com',
        '"{nombre} {apellido}" site:bandcamp.com',
        '"{nombre} {apellido}" site:weibo.com',
        '"{nombre} {apellido}" site:douban.com',
        '"{nombre} {apellido}" site:renren.com'
    ],
    "Email y Contacto": [
        'intext:{email}',
        'intitle:{email}',
        'inurl:{email}',
        '{email} site:pastebin.com',
        '{email} site:github.com',
        '{email} site:gitlab.com',
        '{email} (breach OR leak OR dump)',
        '{telefono} (contact OR phone OR mobile)',
        'intext:{telefono}',
        '"{nombre} {apellido}" (email OR mail OR contact)',
        '{email} filetype:sql "pass"',
        '{email} filetype:log',
        '"{nombre} {apellido}" filetype:vcf',
        '"{nombre} {apellido}" filetype:vcard',
        'intext:"{email}" "BEGIN PGP PUBLIC KEY BLOCK"',
        '"{nombre} {apellido}" "contact information"',
        '{email} site:trello.com',
        '{email} site:*.atlassian.net',
        '{email} "mailing list"',
        '"{telefono}" "who called me"',
        'intext:"{telefono}" filetype:pdf',
        '{email} site:docs.google.com "sharing"',
        '"{nombre} {apellido}" "contact us"',
        '{email} "sent from my"',
        'allintext:{email} "password" site:pastebin.com',
        '"{telefono}" (spam OR scam)',
        '{email} filetype:csv',
        'site:ycombinator.com "{email}"',
        'site:news.ycombinator.com "{email}"',
        '{email} "email signature"',
        '"{nombre} {apellido}" "phone number"',
        'intext:"{email}" ext:eml',
        'intext:"{email}" ext:mbox',
        '{email} site:groups.google.com',
        '{email} filetype:txt "passwords"',
        '"{telefono}" "business card"',
        'site:domain.com/uploads/ "{email}"',
        'site:scribd.com "{email}"',
        'site:issuu.com "{email}"',
        '{email} intitle:"contact"',
        'inurl:/contact {telefono}',
        '"{nombre} {apellido}" "contact details"',
        '"{nombre} {apellido}" intitle:"staff directory"',
        '"{nombre} {apellido}" "email address"',
        '{email} "User:"',
        '{email} inurl:author',
        '{email} inurl:member',
        '{email} inurl:profile',
        '"{telefono}" "emergency contact"',
        '"{nombre} {apellido}" "get in touch"',
        '"{email}" "webmaster"'
    ],
    "Documentos y Archivos": [
        '"{nombre} {apellido}" filetype:pdf',
        '"{nombre} {apellido}" filetype:xls',
        '"{nombre} {apellido}" filetype:xlsx',
        '"{nombre} {apellido}" filetype:doc',
        '"{nombre} {apellido}" filetype:docx',
        '"{nombre} {apellido}" filetype:ppt',
        '"{nombre} {apellido}" filetype:pptx',
        '"{nombre} {apellido}" filetype:txt',
        '{email} filetype:pdf',
        '"{nombre} {apellido}" (CV OR resume OR curriculum)',
        '"{nombre} {apellido}" filetype:rtf',
        '"{nombre} {apellido}" filetype:odt',
        '"{nombre} {apellido}" filetype:odp',
        '"{nombre} {apellido}" filetype:ods',
        '"{nombre} {apellido}" filetype:csv',
        '"{nombre} {apellido}" filetype:tex',
        '"{nombre} {apellido}" filetype:ps',
        '"{nombre} {apellido}" filetype:wpd',
        '"{nombre} {apellido}" filetype:wps',
        '"{nombre} {apellido}" filetype:ans',
        'site:docs.google.com "{nombre} {apellido}"',
        'site:scribd.com "{nombre} {apellido}"',
        'site:academia.edu "{nombre} {apellido}"',
        'site:slideshare.net "{nombre} {apellido}"',
        'site:prezi.com "{nombre} {apellido}"',
        '"{nombre} {apellido}" "minutes of meeting" filetype:pdf',
        '"{nombre} {apellido}" "internal memo" filetype:pdf',
        '"{nombre} {apellido}" "report" filetype:pdf',
        '"{nombre} {apellido}" "presentation" filetype:ppt',
        '"{nombre} {apellido}" "spreadsheet" filetype:xls',
        '"{nombre} {apellido}" "salary" filetype:xls',
        '"{nombre} {apellido}" "budget" filetype:xlsx',
        '"{nombre} {apellido}" "contract" filetype:doc',
        '"{nombre} {apellido}" "agreement" filetype:docx',
        '"{nombre} {apellido}" "invoice" filetype:pdf',
        '"{nombre} {apellido}" "form" filetype:pdf',
        '"{nombre} {apellido}" "application" filetype:pdf',
        '"{nombre} {apellido}" "list" filetype:csv',
        '"{nombre} {apellido}" "directory" filetype:doc',
        '"{nombre} {apellido}" "proposal" filetype:pdf',
        '"{nombre} {apellido}" "manual" filetype:pdf',
        '"{nombre} {apellido}" "archive" filetype:zip',
        '"{nombre} {apellido}" "backup" filetype:bak',
        '"{nombre} {apellido}" "database" filetype:sql',
        '"{nombre} {apellido}" "transcript" filetype:pdf',
        '"{nombre} {apellido}" "certificate" filetype:pdf',
        '"{nombre} {apellido}" "publication" filetype:pdf',
        '"{nombre} {apellido}" "thesis" filetype:pdf',
        '"{nombre} {apellido}" "dissertation" filetype:pdf',
        '"{nombre} {apellido}" "biography" filetype:pdf'
    ],
    "Índices y Directorios": [
        'intitle:"index of" "{nombre} {apellido}"',
        'intitle:"index of" {email}',
        'intitle:"index of" CV "{nombre} {apellido}"',
        'intitle:"index of" resume "{nombre} {apellido}"',
        'intitle:"directory listing" "{nombre} {apellido}"',
        'intitle:"parent directory" "{nombre} {apellido}"',
        'intitle:"index of" "private"',
        'intitle:"index of" "backup"',
        'intitle:"index of" "confidential"',
        'intitle:"index of" "passwords"',
        'intitle:"index of" "mail"',
        'intitle:"index of" "personal"',
        'intitle:"index of" "photos"',
        'intitle:"index of" "contacts"',
        'intitle:"index of" "documents"',
        'intitle:"index of" "uploads"',
        'intitle:"index of" "downloads"',
        'intitle:"index of" "logs"',
        'intitle:"index of" "db"',
        'intitle:"index of" "sql"',
        'intitle:"index of" "secret"',
        'intitle:"index of" /admin/',
        'intitle:"index of" /config/',
        'intitle:"index of" /backups/',
        'intitle:"index of" /data/',
        'intitle:"index of" "database"',
        'intitle:"index of" /etc/',
        'intitle:"index of" /home/',
        'intitle:"index of" /user/',
        'intitle:"index of" /users/',
        'intitle:"index of" /tmp/',
        'intitle:"index of" /private/ "{nombre} {apellido}"',
        'intitle:"index of" "contacts.csv"',
        'intitle:"index of" "pwd.txt"',
        'intitle:"index of" "user.txt"',
        'intitle:"index of" "id_rsa"',
        'intitle:"index of" ".ssh"',
        'intitle:"index of" ".aws"',
        'intitle:"index of" "wp-content"',
        'intitle:"index of" "C:/Users/"',
        'intitle:"index of" "sensitive"',
        'intitle:"index of" "internal"',
        'intitle:"index of" "top secret"'
    ],
    "Información Profesional": [
        '"{nombre} {apellido}" (work OR job OR employee OR staff)',
        '"{nombre} {apellido}" (company OR corporation OR business)',
        '"{nombre} {apellido}" (title OR position OR role)',
        '"{nombre} {apellido}" (university OR college OR school)',
        '"{nombre} {apellido}" (degree OR graduation OR diploma)',
        'site:crunchbase.com "{nombre} {apellido}"',
        'site:bloomberg.com "{nombre} {apellido}"',
        'site:zoominfo.com "{nombre} {apellido}"',
        'site:rocketreach.co "{nombre} {apellido}"',
        'site:apollo.io "{nombre} {apellido}"',
        'site:owler.com "{nombre} {apellido}"',
        'site:glassdoor.com "{nombre} {apellido}" "review"',
        'site:indeed.com "{nombre} {apellido}" "resume"',
        'site:theorg.com "{nombre} {apellido}"',
        'site:researchgate.net "{nombre} {apellido}"',
        'site:scholar.google.com "{nombre} {apellido}"',
        '"{nombre} {apellido}" "author"',
        '"{nombre} {apellido}" "speaker"',
        '"{nombre} {apellido}" "consultant"',
        '"{nombre} {apellido}" "board of directors"',
        '"{nombre} {apellido}" "team member"',
        '"{nombre} {apellido}" "staff profile"',
        '"{nombre} {apellido}" "about us"',
        '"{nombre} {apellido}" "professional profile"',
        '"{nombre} {apellido}" "expertise"',
        '"{nombre} {apellido}" "patent"',
        '"{nombre} {apellido}" "publication"',
        '"{nombre} {apellido}" "conference"',
        '"{nombre} {apellido}" "webinar"',
        '"{nombre} {apellido}" "case study"',
        '"{nombre} {apellido}" "white paper"',
        '"{nombre} {apellido}" "alumni"',
        '"{nombre} {apellido}" "faculty"',
        '"{nombre} {apellido}" "department of"',
        '"{nombre} {apellido}" "LLC"',
        '"{nombre} {apellido}" "Inc."',
        '"{nombre} {apellido}" "founder"',
        '"{nombre} {apellido}" "CEO"',
        '"{nombre} {apellido}" "executive"',
        '"{nombre} {apellido}" "biography"',
        '"{nombre} {apellido}" "career"',
        '"{nombre} {apellido}" "industry"',
        '"{nombre} {apellido}" "project"',
        '"{nombre} {apellido}" "portfolio"',
        '"{nombre} {apellido}" "testimonial"',
        '"{nombre} {apellido}" "employee directory"',
        '"{nombre} {apellido}" "org chart"',
        '"{nombre} {apellido}" "business license"',
        '"{nombre} {apellido}" "corporate registration"'
    ],
    "Información Personal": [
        '"{nombre} {apellido}" (age OR born OR birth)',
        '"{nombre} {apellido}" (address OR location OR lives)',
        '"{nombre} {apellido}" (family OR spouse OR married)',
        '"{nombre} {apellido}" {ciudad} {pais}',
        '"{nombre} {apellido}" (phone OR mobile OR contact)',
        '"{nombre} {apellido}" (interests OR hobbies OR likes)',
        '"{nombre} {apellido}" "date of birth"',
        '"{nombre} {apellido}" "hometown"',
        '"{nombre} {apellido}" "obituary"',
        '"{nombre} {apellido}" "wedding announcement"',
        '"{nombre} {apellido}" "birth announcement"',
        '"{nombre} {apellido}" "engagement"',
        '"{nombre} {apellido}" "divorce records"',
        '"{nombre} {apellido}" "genealogy"',
        '"{nombre} {apellido}" "family tree"',
        '"{nombre} {apellido}" "maiden name"',
        '"{nombre} {apellido}" "blog"',
        '"{nombre} {apellido}" "personal website"',
        '"{nombre} {apellido}" inurl:blog',
        '"{nombre} {apellido}" inurl:profile',
        '"{nombre} {apellido}" "about me"',
        '"{nombre} {apellido}" {telefono}',
        '"{nombre} {apellido}" "{ciudad}"',
        '"{nombre} {apellido}" "{pais}"',
        '"{nombre} {apellido}" "donations"',
        '"{nombre} {apellido}" "political contributions"',
        '"{nombre} {apellido}" "marathon results"',
        '"{nombre} {apellido}" "runner"',
        '"{nombre} {apellido}" "athlete"',
        '"{nombre} {apellido}" "church"',
        '"{nombre} {apellido}" "parish"',
        '"{nombre} {apellido}" "club member"',
        '"{nombre} {apellido}" "volunteer"',
        '"{nombre} {apellido}" "guestbook"',
        '"{nombre} {apellido}" "forum posts"',
        '"{nombre} {apellido}" "member list"',
        '"{nombre} {apellido}" "travel"',
        '"{nombre} {apellido}" "wishlist" site:amazon.com',
        '"{nombre} {apellido}" "review" site:yelp.com',
        '"{nombre} {apellido}" "review" site:tripadvisor.com',
        '"{nombre} {apellido}" "vehicle registration"',
        '"{nombre} {apellido}" "property records"',
        '"{nombre} {apellido}" "voter registration"',
        '"{nombre} {apellido}" "attended"',
        '"{nombre} {apellido}" "favorite"',
        '"{nombre} {apellido}" "I love"',
        '"{nombre} {apellido}" "my favorite"',
        '"{nombre} {apellido}" "childhood"',
        '"{nombre} {apellido}" "high school"',
        '"{nombre} {apellido}" "class of"'
    ],
    "Registros Públicos": [
        '"{nombre} {apellido}" (court OR legal OR lawsuit)',
        '"{nombre} {apellido}" (arrest OR criminal OR police)',
        '"{nombre} {apellido}" (property OR "real estate" OR house)',
        '"{nombre} {apellido}" (license OR permit OR registration)',
        '"{nombre} {apellido}" (bankruptcy OR debt OR financial)',
        'site:whitepages.com "{nombre} {apellido}"',
        '"{nombre} {apellido}" "public records"',
        '"{nombre} {apellido}" "court case"',
        '"{nombre} {apellido}" "case number"',
        '"{nombre} {apellido}" "docket"',
        '"{nombre} {apellido}" "plaintiff"',
        '"{nombre} {apellido}" "defendant"',
        '"{nombre} {apellido}" "mugshot"',
        '"{nombre} {apellido}" "warrant"',
        '"{nombre} {apellido}" "felony"',
        '"{nombre} {apellido}" "misdemeanor"',
        '"{nombre} {apellido}" "citation"',
        '"{nombre} {apellido}" "traffic violation"',
        '"{nombre} {apellido}" "property tax"',
        '"{nombre} {apellido}" "deed"',
        '"{nombre} {apellido}" "parcel number"',
        '"{nombre} {apellido}" "assessor"',
        '"{nombre} {apellido}" "voter records"',
        '"{nombre} {apellido}" site:.gov "license"',
        '"{nombre} {apellido}" "professional license"',
        '"{nombre} {apellido}" "business permit"',
        '"{nombre} {apellido}" "UCC filing"',
        '"{nombre} {apellido}" "lien"',
        '"{nombre} {apellido}" "foreclosure"',
        '"{nombre} {apellido}" "SEC filing"',
        '"{nombre} {apellido}" "political donation" site:fec.gov',
        '"{nombre} {apellido}" "pilot license" site:faa.gov',
        '"{nombre} {apellido}" "medical license"',
        '"{nombre} {apellido}" "hunting license"',
        '"{nombre} {apellido}" "fishing license"',
        '"{nombre} {apellido}" "unclaimed property"',
        '"{nombre} {apellido}" "corporate registration"',
        '"{nombre} {apellido}" "DBA" ("doing business as")',
        '"{nombre} {apellido}" "notary public"',
        '"{nombre} {apellido}" "trademark"',
        '"{nombre} {apellido}" "patent filing"',
        '"{nombre} {apellido}" "obituary"',
        '"{nombre} {apellido}" "cemetery records"',
        '"{nombre} {apellido}" "social security death index"',
        '"{nombre} {apellido}" "marriage license"',
        '"{nombre} {apellido}" "birth certificate index"',
        '"{nombre} {apellido}" "divorce decree"',
        '"{nombre} {apellido}" "military records"',
        '"{nombre} {apellido}" "government contract"'
    ],
    "Noticias y Menciones": [
        '"{nombre} {apellido}" (news OR article OR story)',
        '"{nombre} {apellido}" (press OR media OR interview)',
        '"{nombre} {apellido}" (event OR conference OR meeting)',
        '"{nombre} {apellido}" (award OR recognition OR honor)',
        'site:news.google.com "{nombre} {apellido}"',
        '"{nombre} {apellido}" (mentioned OR quoted OR featured)',
        '"{nombre} {apellido}" "press release"',
        '"{nombre} {apellido}" "in the news"',
        '"{nombre} {apellido}" "interview with"',
        '"{nombre} {apellido}" "profile of"',
        '"{nombre} {apellido}" "spoke with"',
        '"{nombre} {apellido}" "announced by"',
        '"{nombre} {apellido}" "according to"',
        '"{nombre} {apellido}" "letter to the editor"',
        '"{nombre} {apellido}" "op-ed"',
        '"{nombre} {apellido}" site:*.blogs.com',
        '"{nombre} {apellido}" site:*.wordpress.com',
        '"{nombre} {apellido}" site:medium.com',
        '"{nombre} {apellido}" inurl:2023',
        '"{nombre} {apellido}" inurl:2024',
        '"{nombre} {apellido}" after:2023-01-01',
        '"{nombre} {apellido}" before:2024-12-31',
        '"{nombre} {apellido}" "local news"',
        '"{nombre} {apellido}" "community news"',
        '"{nombre} {apellido}" "{ciudad} news"',
        '"{nombre} {apellido}" "hometown hero"',
        '"{nombre} {apellido}" "police blotter"',
        '"{nombre} {apellido}" "achievements"',
        '"{nombre} {apellido}" "dean\'s list"',
        '"{nombre} {apellido}" "honor roll"',
        '"{nombre} {apellido}" "scholarship"',
        '"{nombre} {apellido}" "alumni news"',
        '"{nombre} {apellido}" "club newsletter"',
        '"{nombre} {apellido}" "company newsletter"',
        '"{nombre} {apellido}" "charity event"',
        '"{nombre} {apellido}" "fundraiser"',
        '"{nombre} {apellido}" "guest speaker"',
        '"{nombre} {apellido}" "panelist"',
        '"{nombre} {apellido}" "winner"',
        '"{nombre} {apellido}" "laureate"',
        '"{nombre} {apellido}" "public statement"',
        '"{nombre} {apellido}" "obituary notice"',
        '"{nombre} {apellido}" "wedding announcement"',
        '"{nombre} {apellido}" "engagement announcement"'
    ],
    "Tecnología y Desarrollo": [
        'site:github.com "{nombre} {apellido}"',
        'site:gitlab.com "{nombre} {apellido}"',
        'site:stackoverflow.com "{nombre} {apellido}"',
        'site:bitbucket.org "{nombre} {apellido}"',
        '{email} (github OR git OR code OR programming)',
        '"{nombre} {apellido}" (developer OR programmer OR coder)',
        'site:sourceforge.net "{nombre} {apellido}"',
        'site:launchpad.net "{nombre} {apellido}"',
        'site:coderwall.com "{nombre} {apellido}"',
        'site:npmjs.com/~"{alias1}"',
        'site:pypi.org/user/ "{alias1}"',
        'site:hub.docker.com/u/ "{alias1}"',
        'site:dev.to "{nombre} {apellido}"',
        'site:hashnode.com "{nombre} {apellido}"',
        'site:hackernoon.com "{nombre} {apellido}"',
        'site:kaggle.com "{nombre} {apellido}"',
        'site:producthunt.com "{nombre} {apellido}"',
        'site:angellist.co "{nombre} {apellido}"',
        'site:ycombinator.com "{nombre} {apellido}"',
        'site:toptal.com "{nombre} {apellido}"',
        'site:upwork.com "{nombre} {apellido}"',
        '"{nombre} {apellido}" "technical blog"',
        '"{nombre} {apellido}" "tutorial"',
        '"{nombre} {apellido}" "open source contribution"',
        '"{nombre} {apellido}" "commit message"',
        '"{nombre} {apellido}" "pull request"',
        '"{nombre} {apellido}" "issue tracker"',
        '"{nombre} {apellido}" "bug report"',
        '"{email}" "GPG key"',
        '"{email}" "PGP public key"',
        '"{nombre} {apellido}" "dotfiles"',
        '"{nombre} {apellido}" "config file"',
        '"{nombre} {apellido}" "code snippet"',
        '"{nombre} {apellido}" "gist"',
        '"{nombre} {apellido}" "hackathon"',
        '"{nombre} {apellido}" "tech talk"',
        '"{nombre} {apellido}" "screencast"',
        '"{nombre} {apellido}" "portfolio"',
        '"{nombre} {apellido}" "résumé" "github"',
        '{email} "BEGIN SSH2 PUBLIC KEY"',
        '{email} "BEGIN PGP PRIVATE KEY BLOCK"',
        '"{nombre} {apellido}" "stack trace"',
        '"{nombre} {apellido}" "error log"',
        'site:gitter.im "{nombre} {apellido}"',
        'site:slack.com "{email}"',
        'site:discord.com "{email}"',
        '"{nombre} {apellido}" "API documentation"',
        '"{nombre} {apellido}" "CTF writeup"'
    ],
    "Imágenes y Multimedia": [
        '"{nombre} {apellido}" (inurl:jpg OR inurl:png OR inurl:gif)',
        '"{nombre} {apellido}" (image OR photo OR picture)',
        '"{nombre} {apellido}" (video OR youtube OR vimeo)',
        '"{nombre} {apellido}" (podcast OR audio OR interview)',
        'site:flickr.com "{nombre} {apellido}"',
        'site:imgur.com "{nombre} {apellido}"',
        'site:photobucket.com "{nombre} {apellido}"',
        'site:500px.com "{nombre} {apellido}"',
        'site:smugmug.com "{nombre} {apellido}"',
        'site:deviantart.com "{nombre} {apellido}"',
        'site:pinterest.com "{nombre} {apellido}" "board"',
        'site:instagram.com "{nombre} {apellido}"',
        'site:facebook.com "{nombre} {apellido}" "photos"',
        'site:youtube.com "{nombre} {apellido}" "channel"',
        'site:vimeo.com "{nombre} {apellido}" "album"',
        'site:dailymotion.com "{nombre} {apellido}"',
        'site:soundcloud.com "{nombre} {apellido}"',
        'site:bandcamp.com "{nombre} {apellido}"',
        'site:last.fm "{nombre} {apellido}"',
        'site:spotify.com "{nombre} {apellido}"',
        '"{nombre} {apellido}" "photo gallery"',
        '"{nombre} {apellido}" "tagged in photo"',
        '"{nombre} {apellido}" "in a video with"',
        '"{nombre} {apellido}" "webcam"',
        '"{nombre} {apellido}" "livestream"',
        '"{nombre} {apellido}" "headshot"',
        '"{nombre} {apellido}" "portrait"',
        '"{nombre} {apellido}" "family photo"',
        '"{nombre} {apellido}" "event photos"',
        '"{nombre} {apellido}" "wedding photos"',
        '"{nombre} {apellido}" "vacation pictures"',
        '"{nombre} {apellido}" "profile picture"',
        '"{nombre} {apellido}" "avatar"',
        '"{nombre} {apellido}" filetype:jpg',
        '"{nombre} {apellido}" filetype:jpeg',
        '"{nombre} {apellido}" filetype:png',
        '"{nombre} {apellido}" filetype:gif',
        '"{nombre} {apellido}" filetype:bmp',
        '"{nombre} {apellido}" filetype:tiff',
        '"{nombre} {apellido}" filetype:svg',
        'inurl:uploads "{nombre} {apellido}"',
        'inurl:gallery "{nombre} {apellido}"',
        'inurl:album "{nombre} {apellido}"',
        'inurl:images "{nombre} {apellido}"',
        '"{nombre} {apellido}" "EXIF data"',
        'intitle:"index of" "DCIM"',
        'intitle:"index of" "pictures"',
        '"{nombre} {apellido}" "screencapture"',
        '"{nombre} {apellido}" "artwork"',
        '"{nombre} {apellido}" "design"'
    ],
    "Infraestructura y Seguridad": [
        'intitle:"Dashboard" "{nombre} {apellido}"',
        'intitle:"login" inurl:admin "{nombre} {apellido}"',
        'intitle:"index of" "config.php" "{nombre} {apellido}"',
        'filetype:env "{nombre} {apellido}"',
        'filetype:log "{nombre} {apellido}"',
        'filetype:bak "{nombre} {apellido}"',
        'filetype:conf "{nombre} {apellido}"',
        'site:*.git "{nombre} {apellido}"',
        'intitle:"phpinfo()" "{nombre} {apellido}"',
        '"Apache2 Ubuntu Default Page" "{nombre} {apellido}"',
        '"Welcome to nginx!" "{nombre} {apellido}"',
        '"nginx test page" "{nombre} {apellido}"',
        '"OpenSSH" "{nombre} {apellido}"',
        'inurl:"/wp-admin" "{nombre} {apellido}"',
        'inurl:"/wp-login" "{nombre} {apellido}"',
        'inurl:8080 "{nombre} {apellido}"',
        'inurl:8443 "{nombre} {apellido}"',
        'inurl:2083 "{nombre} {apellido}"',
        'inurl:2087 "{nombre} {apellido}"',
        'inurl:"/admin/login" "{nombre} {apellido}"',
        'inurl:"/administrator" "{nombre} {apellido}"',
        'inurl:"/controlpanel" "{nombre} {apellido}"',
        'inurl:"/user/login" "{nombre} {apellido}"',
        '"Powered by vBulletin" "{nombre} {apellido}"',
        '"Powered by phpBB" "{nombre} {apellido}"',
        '"Powered by MyBB" "{nombre} {apellido}"',
        '"Powered by Joomla" "{nombre} {apellido}"',
        '"Powered by Drupal" "{nombre} {apellido}"',
        '"Powered by Magento" "{nombre} {apellido}"',
        '"index of /mysql" "{nombre} {apellido}"',
        '"index of /db" "{nombre} {apellido}"',
        '"index of /database" "{nombre} {apellido}"',
        '"index of /backup" "{nombre} {apellido}"',
        '"index of /htdocs" "{nombre} {apellido}"',
        '"index of /wwwroot" "{nombre} {apellido}"',
        '"Server at" "{nombre} {apellido}"',
        'inurl:"/cgi-bin/" "{nombre} {apellido}"',
        'inurl:"/shell" "{nombre} {apellido}"',
        'inurl:"/cmd" "{nombre} {apellido}"',
        'inurl:"/remote" "{nombre} {apellido}"',
        '"It works!" Apache "{nombre} {apellido}"',
        '"site under construction" "{nombre} {apellido}"',
        'intitle:"webcamXP" "{nombre} {apellido}"',
        'intitle:"Axis 2400 Video Server" "{nombre} {apellido}"',
        'intitle:"MikroTik RouterOS" "{nombre} {apellido}"',
        'intitle:"RouterOS" "{nombre} {apellido}"',
        'intitle:"DVR Login" "{nombre} {apellido}"',
        'intext:"{email}" filetype:log "error"',
        'intext:"{email}" "stack trace"',
        'intext:"{nombre} {apellido}" filetype:config',
        'intext:"{nombre} {apellido}" "BEGIN CERTIFICATE"',
        'intitle:"Jira" intext:"{nombre} {apellido}"',
        'intitle:"Confluence" intext:"{nombre} {apellido}"',
        'inurl:jenkins intext:"{nombre} {apellido}"',
        'intext:"humans.txt" "{nombre} {apellido}"',
        'inurl:"/server-status" "{nombre} {apellido}"',
        'filetype:pem intext:"PRIVATE KEY" "{nombre} {apellido}"',
        'filetype:ppk intext:"PuTTY-User-Key-File-2"',
        'inurl:show_bug.cgi?id= "{email}"'
    ],
    "Fugas y Leaks": [
        '{email} site:pastebin.com',
        '{email} site:ghostbin.com',
        '{email} site:controlc.com',
        '{email} site:hastebin.com',
        '{email} site:jsfiddle.net',
        '{email} site:codepen.io',
        '{email} site:repl.it',
        '{email} site:ideone.com',
        '{email} site:github.com "password"',
        '{email} site:gitlab.com "token"',
        '{email} site:bitbucket.org "key"',
        '{email} "aws_access_key_id"',
        '{email} "ssh-rsa"',
        '{email} "BEGIN RSA PRIVATE KEY"',
        '{email} "BEGIN OPENSSH PRIVATE KEY"',
        '{email} "DB_PASSWORD"',
        '{email} "MYSQL_PASSWORD"',
        '{email} "POSTGRES_PASSWORD"',
        '{email} "db_pass"',
        '{email} "slack_api_token"',
        '{email} "xoxb-"',
        '{email} "xoxp-"',
        '{email} "sendgrid_api_key"',
        '{email} "api_secret"',
        '{email} "client_secret"',
        '{email} "PRIVATE_KEY"',
        '{email} "ftp_password"',
        '{email} "smtp_password"',
        '{email} "github_token"',
        '{email} "gitlab_token"',
        '{email} "bitbucket_token"',
        '{email} "api_key"',
        '{email} "secret_key"',
        '{email} "auth_token"',
        '{email} "refresh_token"',
        '{email} "password123"',
        '{email} "passwd"',
        '{email} "pwd"',
        '{email} "access_token"',
        '{email} "bearer_token"',
        '{email} "jwt_secret"',
        '{email} "secret_jwt"',
        '{email} "db_username"',
        '{email} "db_user"',
        '{email} "root_password"',
        '{email} "root_pass"',
        '{email} site:s3.amazonaws.com',
        '"{nombre} {apellido}" site:pastebin.com "password"',
        '{email} "HEROKU_API_KEY"',
        '{email} "STRIPE_API_KEY"',
        '{email} "TWILIO_ACCOUNT_SID"',
        '{email} filetype:sql "Dumping data for table"',
        '{email} "Index of" backup.zip',
        '{email} site:trello.com "password"',
        '{email} site:*.atlassian.net "credentials"',
        '{email} "MONGODB_URI"',
        '{email} "REDIS_URL"',
        '{email} "encryption key"',
        '{email} "secretkey"',
        '{email} "authkey"',
        '{email} "accesskey"'
    ],
    "Documentos Sensibles": [
        'filetype:pdf "{nombre} {apellido}" site:gov',
        'filetype:pdf "{nombre} {apellido}" site:mil',
        'filetype:xls "{nombre} {apellido}" "confidential"',
        'filetype:xlsx "{nombre} {apellido}" "restricted"',
        'filetype:doc "{nombre} {apellido}" "internal use only"',
        'filetype:docx "{nombre} {apellido}" "not for distribution"',
        'filetype:ppt "{nombre} {apellido}" "proprietary"',
        'filetype:pptx "{nombre} {apellido}" "sensitive"',
        'filetype:txt "{nombre} {apellido}" "password"',
        'filetype:log "{nombre} {apellido}"',
        'filetype:cfg "{nombre} {apellido}"',
        'filetype:conf "{nombre} {apellido}"',
        'filetype:xml "{nombre} {apellido}" "config"',
        'filetype:json "{nombre} {apellido}" "key"',
        'filetype:ini "{nombre} {apellido}"',
        'filetype:bak "{nombre} {apellido}"',
        'filetype:old "{nombre} {apellido}"',
        'filetype:sql "{nombre} {apellido}"',
        'filetype:db "{nombre} {apellido}"',
        'filetype:tar "{nombre} {apellido}"',
        'filetype:gz "{nombre} {apellido}"',
        'filetype:zip "{nombre} {apellido}"',
        'filetype:rar "{nombre} {apellido}"',
        'filetype:7z "{nombre} {apellido}"',
        '"index of" "confidential" "{nombre} {apellido}"',
        '"index of" "proprietary" "{nombre} {apellido}"',
        '"index of" "sensitive" "{nombre} {apellido}"',
        '"index of" "internal" "{nombre} {apellido}"',
        '"index of" "classified" "{nombre} {apellido}"',
        '"index of" "documents" "{nombre} {apellido}"',
        '"index of" "docs" "{nombre} {apellido}"',
        '"index of" "reports" "{nombre} {apellido}"',
        '"index of" "plans" "{nombre} {apellido}"',
        '"index of" "blueprints" "{nombre} {apellido}"',
        '"index of" "drawings" "{nombre} {apellido}"',
        '"index of" "designs" "{nombre} {apellido}"',
        '"index of" "presentations" "{nombre} {apellido}"',
        '"index of" "slides" "{nombre} {apellido}"',
        '"index of" "spreadsheets" "{nombre} {apellido}"',
        '"index of" "financials" "{nombre} {apellido}"',
        '"index of" "budgets" "{nombre} {apellido}"',
        '"index of" "forecasts" "{nombre} {apellido}"',
        '"{nombre} {apellido}" "Top Secret" filetype:pdf',
        '"{nombre} {apellido}" "For Official Use Only" filetype:pdf',
        '"{nombre} {apellido}" "Company Confidential" filetype:ppt',
        '"{nombre} {apellido}" "Secret" filetype:doc',
        '"{nombre} {apellido}" "trade secret"',
        '"{nombre} {apellido}" "NDA" filetype:pdf',
        '"{nombre} {apellido}" "non-disclosure agreement"',
        '"{nombre} {apellido}" "meeting minutes" "confidential"',
        '"{nombre} {apellido}" filetype:eml "confidential"',
        '"{nombre} {apellido}" "salary list" filetype:xls',
        '"{nombre} {apellido}" "HR records" filetype:pdf',
        '"{nombre} {apellido}" "employee data" filetype:csv',
        'site:s3.amazonaws.com "{nombre} {apellido}" "private"'
    ],
    "Indexaciones Abiertas": [
        'intitle:"index of /" "{nombre} {apellido}"',
        'intitle:"index of" "ftp" "{nombre} {apellido}"',
        'intitle:"index of" "smb" "{nombre} {apellido}"',
        'intitle:"index of" "webdav" "{nombre} {apellido}"',
        'intitle:"index of" "nfs" "{nombre} {apellido}"',
        'intitle:"index of" "afs" "{nombre} {apellido}"',
        'intitle:"index of" "rsync" "{nombre} {apellido}"',
        'intitle:"index of" "cvs" "{nombre} {apellido}"',
        'intitle:"index of" "svn" "{nombre} {apellido}"',
        'intitle:"index of" "hg" "{nombre} {apellido}"',
        'intitle:"index of" "bzr" "{nombre} {apellido}"',
        'intitle:"index of" "docker" "{nombre} {apellido}"',
        'intitle:"index of" "k8s" "{nombre} {apellido}"',
        'intitle:"index of" "helm" "{nombre} {apellido}"',
        'intitle:"index of" "charts" "{nombre} {apellido}"',
        'intitle:"index of" "images" "{nombre} {apellido}"',
        'intitle:"index of" "videos" "{nombre} {apellido}"',
        'intitle:"index of" "audio" "{nombre} {apellido}"',
        'intitle:"index of" "photos" "{nombre} {apellido}"',
        'intitle:"index of" "music" "{nombre} {apellido}"',
        'intitle:"index of" "ebooks" "{nombre} {apellido}"',
        'intitle:"index of" "books" "{nombre} {apellido}"',
        'intitle:"index of" "magazines" "{nombre} {apellido}"',
        'intitle:"index of" "journals" "{nombre} {apellido}"',
        'intitle:"index of" "archives" "{nombre} {apellido}"',
        'intitle:"index of" "backups" "{nombre} {apellido}"',
        'intitle:"index of" "old" "{nombre} {apellido}"',
        'intitle:"index of" "tmp" "{nombre} {apellido}"',
        'intitle:"index of" "temp" "{nombre} {apellido}"',
        'intitle:"index of" "cache" "{nombre} {apellido}"',
        'intitle:"index of" "var" "{nombre} {apellido}"',
        'intitle:"index of" "usr" "{nombre} {apellido}"',
        'intitle:"index of" "etc" "{nombre} {apellido}"',
        'intitle:"index of" "bin" "{nombre} {apellido}"',
        'intitle:"index of" "sbin" "{nombre} {apellido}"',
        'intitle:"index of" "opt" "{nombre} {apellido}"',
        'intitle:"index of" "home" "{nombre} {apellido}"',
        'intitle:"index of" "root" "{nombre} {apellido}"',
        'intitle:"index of" "mnt" "{nombre} {apellido}"',
        'intitle:"index of" "private" "{nombre} {apellido}"',
        'intitle:"index of" "secret" "{nombre} {apellido}"',
        'intitle:"index of" "personal" "{nombre} {apellido}"',
        'intitle:"index of" "confidential" "{nombre} {apellido}"',
        'intitle:"index of" "passwords" "{nombre} {apellido}"',
        'intitle:"index of" "contacts" "{nombre} {apellido}"',
        'intitle:"index of" "mail" "{nombre} {apellido}"',
        'intitle:"index of" "logs" "{nombre} {apellido}"',
        'intitle:"index of" "configs" "{nombre} {apellido}"',
        'intitle:"index of" "exports" "{nombre} {apellido}"',
        'intitle:"index of" "imports" "{nombre} {apellido}"',
        'intitle:"index of" "share" "{nombre} {apellido}"',
        'intitle:"index of" "dump" "{nombre} {apellido}"',
        'intitle:"index of" "db_backup" "{nombre} {apellido}"',
        'intitle:"index of" "site_backup" "{nombre} {apellido}"'
    ],
    "Datos Corporativos": [
        '"{nombre} {apellido}" site:crunchbase.com',
        '"{nombre} {apellido}" site:rocketreach.co',
        '"{nombre} {apellido}" site:zoominfo.com',
        '"{nombre} {apellido}" site:owler.com',
        '"{nombre} {apellido}" site:glassdoor.com',
        '"{nombre} {apellido}" site:indeed.com',
        '"{nombre} {apellido}" site:angel.co',
        '"{nombre} {apellido}" site:dealroom.co',
        '"{nombre} {apellido}" site:linkedin.com/company',
        '"{nombre} {apellido}" "company profile"',
        '"{nombre} {apellido}" "annual report"',
        '"{nombre} {apellido}" "financial statement"',
        '"{nombre} {apellido}" "earnings report"',
        '"{nombre} {apellido}" "SEC filing"',
        '"{nombre} {apellido}" "10-K"',
        '"{nombre} {apellido}" "10-Q"',
        '"{nombre} {apellido}" "8-K"',
        '"{nombre} {apellido}" "shareholder letter"',
        '"{nombre} {apellido}" "press release"',
        '"{nombre} {apellido}" "IPO prospectus"',
        '"{nombre} {apellido}" "investor presentation"',
        '"{nombre} {apellido}" "roadshow"',
        '"{nombre} {apellido}" "M&A"',
        '"{nombre} {apellido}" "acquisition"',
        '"{nombre} {apellido}" "merger"',
        '"{nombre} {apellido}" "joint venture"',
        '"{nombre} {apellido}" "partnership"',
        '"{nombre} {apellido}" "strategic alliance"',
        '"{nombre} {apellido}" "subsidiary"',
        '"{nombre} {apellido}" "branch"',
        '"{nombre} {apellido}" "division"',
        '"{nombre} {apellido}" "business unit"',
        '"{nombre} {apellido}" "board of directors"',
        '"{nombre} {apellido}" "executive team"',
        '"{nombre} {apellido}" "management team"',
        '"{nombre} {apellido}" "org chart"',
        '"{nombre} {apellido}" "corporate governance"',
        '"{nombre} {apellido}" "CSR report"',
        '"{nombre} {apellido}" "ESG report"',
        '"{nombre} {apellido}" "sustainability report"',
        '"{nombre} {apellido}" "green initiative"',
        '"{nombre} {apellido}" site:dnb.com',
        '"{nombre} {apellido}" site:hoovers.com',
        '"{nombre} {apellido}" "business registration"',
        '"{nombre} {apellido}" "tax ID"',
        '"{nombre} {apellido}" "corporate filing"',
        '"{nombre} {apellido}" "advisory board"',
        '"{nombre} {apellido}" "investor"',
        '"{nombre} {apellido}" "founder"',
        '"{nombre} {apellido}" "co-founder"',
        '"{nombre} {apellido}" "company directory"',
        '"{nombre} {apellido}" "leadership"',
        '"{nombre} {apellido}" "corporate announcement"',
        '"{nombre} {apellido}" "stock options"',
        '"{nombre} {apellido}" "shareholder"'
    ],
    "Búsquedas Avanzadas de Personas": [
        '"{nombre} {apellido}" site:familysearch.org',
        '"{nombre} {apellido}" site:findagrave.com',
        '"{nombre} {apellido}" site:ancestry.com',
        '"{nombre} {apellido}" site:geneanet.org',
        '"{nombre} {apellido}" site:myheritage.com',
        '"{nombre} {apellido}" site:forebears.io',
        '"{nombre} {apellido}" site:wikitree.com',
        '"{nombre} {apellido}" site:geni.com',
        '"{nombre} {apellido}" site:archives.com',
        '"{nombre} {apellido}" site:peoplefinders.com',
        '"{nombre} {apellido}" site:spokeo.com',
        '"{nombre} {apellido}" site:whitepages.com',
        '"{nombre} {apellido}" site:411.com',
        '"{nombre} {apellido}" site:fastpeoplesearch.com',
        '"{nombre} {apellido}" site:thatsthem.com',
        '"{nombre} {apellido}" site:radaris.com',
        '"{nombre} {apellido}" site:beenverified.com',
        '"{nombre} {apellido}" site:intelius.com',
        '"{nombre} {apellido}" site:peoplelookup.com',
        '"{nombre} {apellido}" site:veripages.com',
        '"{nombre} {apellido}" site:publicrecords.directory',
        '"{nombre} {apellido}" site:peoplesmart.com',
        '"{nombre} {apellido}" site:ussearch.com',
        '"{nombre} {apellido}" site:peoplerecords.com',
        '"{nombre} {apellido}" site:privateeye.com',
        '"{nombre} {apellido}" site:peekyou.com',
        '"{nombre} {apellido}" site:searchpeoplefree.com',
        '"{nombre} {apellido}" site:personlookup.com',
        '"{nombre} {apellido}" site:findpeoplefree.com',
        '"{nombre} {apellido}" site:advancedbackgroundchecks.com',
        '"{nombre} {apellido}" site:publicbackgroundchecks.com',
        '"{nombre} {apellido}" site:truthfinder.com',
        '"{nombre} {apellido}" site:checkpeople.com',
        '"{nombre} {apellido}" site:instantcheckmate.com',
        '"{nombre} {apellido}" site:peoplelooker.com',
        '"{nombre} {apellido}" site:peoplefindfast.com',
        '"{nombre} {apellido}" site:peoplefastfind.com',
        '"{nombre} {apellido}" site:findpeoplesearch.com',
        '"{nombre} {apellido}" site:freepeoplesearch.com',
        '"{nombre} {apellido}" site:findpeopleeasy.com',
        '"{nombre} {apellido}" site:zabasearch.com',
        '"{nombre} {apellido}" site:pipl.com',
        '"{nombre} {apellido}" site:yasni.com',
        '"{nombre} {apellido}" site:192.com',
        '"{nombre} {apellido}" site:pagesjaunes.fr',
        '"{nombre} {apellido}" site:dastelefonbuch.de',
        '"{nombre} {apellido}" site:paginasamarillas.es',
        '"{nombre} {apellido}" site:paginebianche.it',
        '"{nombre} {apellido}" site:yandex.ru/people',
        '"{nombre} {apellido}" site:truepeoplesearch.com',
        '"{nombre} {apellido}" site:canada411.ca',
        '"{nombre} {apellido}" site:search.ch',
        '"{nombre} {apellido}" site:infobel.com',
        '"{nombre} {apellido}" site:personfinder.google.org'
    ],
    "Alias": [
        'site:linkedin.com/in "{alias1}"',
        'site:linkedin.com/pub "{alias1}"',
        'site:facebook.com "{alias1}"',
        'site:twitter.com "{alias1}"',
        'site:instagram.com "{alias1}"',
        'site:tiktok.com "{alias1}"',
        'site:youtube.com "{alias1}"',
        'site:pinterest.com "{alias1}"',
        'site:reddit.com "{alias1}"',
        'site:github.com "{alias1}"',
        'site:gitlab.com "{alias1}"',
        'site:stackoverflow.com "{alias1}"',
        'site:bitbucket.org "{alias1}"',
        'site:pastebin.com "{alias1}"',
        'site:ghostbin.com "{alias1}"',
        'site:controlc.com "{alias1}"',
        'site:hastebin.com "{alias1}"',
        'site:codepen.io "{alias1}"',
        'site:repl.it "{alias1}"',
        'site:ideone.com "{alias1}"',
        'site:dev.to "{alias1}"',
        'site:medium.com "{alias1}"',
        'site:wordpress.com "{alias1}"',
        'site:blogspot.com "{alias1}"',
        'site:tumblr.com "{alias1}"',
        'site:patreon.com "{alias1}"',
        'site:onlyfans.com "{alias1}"',
        'site:buymeacoffee.com "{alias1}"',
        'site:ko-fi.com "{alias1}"',
        '"{alias1}" filetype:pdf',
        '"{alias1}" filetype:doc',
        '"{alias1}" filetype:docx',
        '"{alias1}" filetype:xls',
        '"{alias1}" filetype:xlsx',
        '"{alias1}" filetype:ppt',
        '"{alias1}" filetype:pptx',
        '"{alias1}" filetype:txt',
        '"{alias1}" filetype:log',
        '"{alias1}" filetype:sql',
        '"{alias1}" filetype:xml',
        '"{alias1}" filetype:json',
        '"{alias1}" filetype:ini',
        '"{alias1}" filetype:bak',
        '"{alias1}" filetype:old',
        'intitle:"index of" "{alias1}"',
        'inurl:"/user/{alias1}"',
        'inurl:"/u/{alias1}"',
        'inurl:"/profile/{alias1}"',
        'inurl:"/members/{alias1}"',
        'inurl:"/account/{alias1}"',
        'inurl:"/id/{alias1}"',
        'inurl:"/channel/{alias1}"',
        'inurl:"/c/{alias1}"',
        'inurl:"/v/{alias1}"',
        '"{alias1}" (username OR handle)',
        '"{alias1}" (nickname OR alias)',
        '"{alias1}" (account OR profile)',
        '"{alias1}" (bio OR biography)',
        '"{alias1}" (forum OR post)',
        '"{alias1}" (comment OR reply)',
        '"{alias1}" (tweet OR retweet)',
        '"{alias1}" (photo OR picture)',
        '"{alias1}" (video OR clip)',
        '"{alias1}" (stream OR live)',
        '"{alias1}" (podcast OR audio)',
        '"{alias1}" (article OR blog)',
        '"{alias1}" (review OR opinion)',
        '"{alias1}" (project OR repo)',
        '"{alias1}" (commit OR push)',
        '"{alias1}" (issue OR bug)',
        '"{alias1}" (pull request OR PR)',
        '"{alias1}" (gist OR snippet)',
        '"{alias1}" (package OR library)',
        '"{alias1}" (theme OR template)',
        '"{alias1}" (plugin OR extension)',
        '"{alias1}" (script OR code)',
        '"{alias1}" (config OR settings)',
        '"{alias1}" (password OR pass)',
        '"{alias1}" (email OR contact)',
        '"{alias1}" (phone OR mobile)',
        '"{alias1}" (address OR location)',
        '"{alias1}" (IP OR host)',
        '"{alias1}" (domain OR website)',
        '"{alias1}" (server OR VPS)',
        '"{alias1}" (SSH OR RDP)',
        '"{alias1}" (FTP OR SFTP)',
        '"{alias1}" (database OR DB)',
        '"{alias1}" (mysql OR postgres)',
        '"{alias1}" (admin OR root)',
        '"{alias1}" (login OR signin)',
        '"{alias1}" (register OR signup)',
        '"{alias1}" (token OR key)',
        '"{alias1}" (API OR endpoint)',
        '"{alias1}" (AWS OR cloud)',
        '"{alias1}" (Azure OR GCP)',
        'site:keybase.io "{alias1}"',
        'site:steamcommunity.com "{alias1}"',
        'site:twitch.tv "{alias1}"',
        'site:deviantart.com "{alias1}"',
        'site:soundcloud.com "{alias1}"',
        'site:vimeo.com "{alias1}"',
        'site:last.fm "{alias1}"',
        'site:gravatar.com "{alias1}"',
        'site:t.me/s/ "{alias1}"',
        'site:*.slack.com "{alias1}"'
    ]
}


class OsintApp:
    """
    Herramienta OSINT mejorada con interfaz gráfica moderna,
    manejo de errores robusto y funcionalidades avanzadas.
    """
    
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("OSINT All-in-One Tool - Versión Corregida v2.0")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        
        # Configuración de estilo moderno
        self._configurar_estilos()
        
        # Variables de estado
        self.datos = {
            "nombre": "",
            "apellido": "",
            "email": "",
            "telefono": "",
            "pais": "",
            "ciudad": "",
            "alias1": "",
            "alias2": "",
            "alias3": ""
        }
        self.resultados_log = []
        self.ejecutando = False
        
        # Crear interfaz
        self._crear_widgets()
        self._configurar_eventos()
        
        # Log inicial
        self.log("OSINT Tool iniciada correctamente", "INFO")

    def _configurar_estilos(self):
        """Configura estilos modernos para la interfaz."""
        style = ttk.Style()
        
        # Configurar tema
        try:
            style.theme_use('clam')
        except:
            pass
            
        # Estilos personalizados
        style.configure("Title.TLabel", font=("Arial", 12, "bold"))
        style.configure("Accent.TButton", 
                       font=("Arial", 10, "bold"),
                       foreground="white")
        style.map("Accent.TButton",
                 background=[('active', '#0078d4'), ('!active', '#106ebe')])

    def _crear_widgets(self):
        """Construye la interfaz gráfica completa."""
        # Frame principal con padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(expand=True, fill="both")
        
        # Configurar grid weights para responsividad
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        # === PANEL IZQUIERDO ===
        self._crear_panel_izquierdo(main_frame)
        
        # === PANEL DERECHO ===
        self._crear_panel_derecho(main_frame)
        
        # === BARRA DE ESTADO ===
        self._crear_barra_estado()

    def _crear_panel_izquierdo(self, parent):
        """Crea el panel izquierdo con controles."""
        left_frame = ttk.Frame(parent)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        left_frame.configure(width=350)
        
        # Panel de datos del objetivo
        self._crear_panel_datos(left_frame)
        
        # Panel de control
        self._crear_panel_control(left_frame)
        
        # Panel de acciones
        self._crear_panel_acciones(left_frame)

    def _crear_panel_datos(self, parent):
        """Crea el panel de entrada de datos."""
        datos_frame = ttk.LabelFrame(parent, text="📋 Datos del Objetivo", 
                                   style="Title.TLabel")
        datos_frame.pack(fill="x", pady=(0, 15))
        datos_frame.configure(padding="10")
        
        self.entradas = {}
        labels = {
            "nombre": "Nombre:",
            "apellido": "Apellido:",
            "email": "Email:",
            "telefono": "Teléfono:",
            "pais": "País:",
            "ciudad": "Ciudad:",
            "alias1": "Alias 1:",
            "alias2": "Alias 2:",
            "alias3": "Alias 3:"
        }
        
        for idx, (campo, label_text) in enumerate(labels.items()):
            # Label
            ttk.Label(datos_frame, text=label_text).grid(
                row=idx, column=0, padx=5, pady=5, sticky="w"
            )
            
            # Entry con validación
            entry = ttk.Entry(datos_frame, width=25)
            entry.grid(row=idx, column=1, padx=5, pady=5, sticky="ew")
            entry.bind('<KeyRelease>', self._validar_datos)
            self.entradas[campo] = entry
        
        datos_frame.columnconfigure(1, weight=1)

    def _crear_panel_control(self, parent):
        """Crea el panel de control de búsqueda."""
        control_frame = ttk.LabelFrame(parent, text="⚙️ Control de Búsqueda")
        control_frame.pack(fill="x", pady=(0, 15))
        control_frame.configure(padding="10")
        
        # Selector de categoría
        ttk.Label(control_frame, text="Categoría:").pack(anchor="w", pady=(0, 5))
        self.categoria_var = tk.StringVar()
        self.categoria_combo = ttk.Combobox(
            control_frame, 
            textvariable=self.categoria_var,
            values=list(DORKS_CATEGORIZADOS.keys()), 
            state="readonly"
        )
        self.categoria_combo.pack(fill="x", pady=(0, 10))
        self.categoria_combo.bind("<<ComboboxSelected>>", self._actualizar_dorks)
        
        # Control de retardo
        ttk.Label(control_frame, text="Retardo entre búsquedas:").pack(anchor="w")
        delay_frame = ttk.Frame(control_frame)
        delay_frame.pack(fill="x", pady=(5, 10))
        
        self.delay_var = tk.DoubleVar(value=2.0)
        delay_scale = ttk.Scale(
            delay_frame, 
            from_=0.5, 
            to=10.0, 
            orient="horizontal",
            variable=self.delay_var
        )
        delay_scale.pack(side="left", fill="x", expand=True)
        
        self.delay_label = ttk.Label(delay_frame, text="2.0s")
        self.delay_label.pack(side="right", padx=(10, 0))
        delay_scale.configure(command=self._actualizar_delay_label)
        
        # Motor de búsqueda
        ttk.Label(control_frame, text="Motor de búsqueda:").pack(anchor="w", pady=(5, 5))
        self.motor_var = tk.StringVar(value="Google")
        motor_combo = ttk.Combobox(
            control_frame,
            textvariable=self.motor_var,
            values=["Google", "DuckDuckGo", "Bing", "Yandex", "baidu"],
            state="readonly"
        )
        motor_combo.pack(fill="x")

    def _crear_panel_acciones(self, parent):
        """Crea el panel de botones de acción."""
        acciones_frame = ttk.LabelFrame(parent, text="🚀 Acciones")
        acciones_frame.pack(fill="x")
        acciones_frame.configure(padding="10")
        
        # Botón principal de ejecución
        self.btn_ejecutar = ttk.Button(
            acciones_frame,
            text="▶️ Ejecutar Búsquedas",
            command=self._ejecutar_busquedas_hilo,
            style="Accent.TButton"
        )
        self.btn_ejecutar.pack(fill="x", pady=(0, 10), ipady=5)
        
        # Botones secundarios
        btn_frame = ttk.Frame(acciones_frame)
        btn_frame.pack(fill="x")
        
        ttk.Button(
            btn_frame,
            text="💾 Guardar Log",
            command=self._guardar_registro
        ).pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        ttk.Button(
            btn_frame,
            text="🧹 Limpiar",
            command=self._limpiar_todo
        ).pack(side="right", fill="x", expand=True, padx=(5, 0))

    def _crear_panel_derecho(self, parent):
        """Crea el panel derecho con lista de dorks y log."""
        right_frame = ttk.Frame(parent)
        right_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.rowconfigure(0, weight=1)
        right_frame.rowconfigure(1, weight=1)
        
        # Panel de dorks
        self._crear_panel_dorks(right_frame)
        
        # Panel de log
        self._crear_panel_log(right_frame)

    def _crear_panel_dorks(self, parent):
        """Crea el panel de selección de dorks."""
        dorks_frame = ttk.LabelFrame(parent, text="📋 Dorks Disponibles")
        dorks_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        dorks_frame.rowconfigure(0, weight=1)
        dorks_frame.columnconfigure(0, weight=1)
        
        # Frame con scrollbar
        list_frame = ttk.Frame(dorks_frame)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)
        
        # Listbox con scrollbar
        self.lista_dorks = Listbox(
            list_frame,
            selectmode=MULTIPLE,
            font=("Consolas", 9),
            activestyle="none"
        )
        self.lista_dorks.grid(row=0, column=0, sticky="nsew")
        
        scrollbar_v = ttk.Scrollbar(list_frame, orient="vertical", 
                                  command=self.lista_dorks.yview)
        scrollbar_v.grid(row=0, column=1, sticky="ns")
        self.lista_dorks.configure(yscrollcommand=scrollbar_v.set)
        
        # Controles de selección
        select_frame = ttk.Frame(dorks_frame)
        select_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        ttk.Button(
            select_frame,
            text="Seleccionar Todos",
            command=self._seleccionar_todos_dorks
        ).pack(side="left")
        
        ttk.Button(
            select_frame,
            text="Deseleccionar Todos",
            command=self._deseleccionar_todos_dorks
        ).pack(side="right")

    def _crear_panel_log(self, parent):
        """Crea el panel de log de ejecución."""
        log_frame = ttk.LabelFrame(parent, text="📊 Log de Ejecución")
        log_frame.grid(row=1, column=0, sticky="nsew")
        
        # Texto con scrollbar
        self.log_texto = scrolledtext.ScrolledText(
            log_frame,
            wrap=tk.WORD,
            font=("Consolas", 9),
            state="disabled"
        )
        self.log_texto.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configurar tags para colores
        self.log_texto.tag_configure("INFO", foreground="blue")
        self.log_texto.tag_configure("SUCCESS", foreground="green", font=("Consolas", 9, "bold"))
        self.log_texto.tag_configure("WARNING", foreground="orange")
        self.log_texto.tag_configure("ERROR", foreground="red", font=("Consolas", 9, "bold"))

    def _crear_barra_estado(self):
        """Crea la barra de estado en la parte inferior."""
        self.status_bar = ttk.Frame(self.root)
        self.status_bar.pack(side="bottom", fill="x", padx=10, pady=(0, 10))
        
        self.status_var = tk.StringVar(value="Listo")
        status_label = ttk.Label(self.status_bar, textvariable=self.status_var)
        status_label.pack(side="left")
        
        self.progress = ttk.Progressbar(self.status_bar, mode='indeterminate')
        self.progress.pack(side="right", padx=(10, 0))

    def _configurar_eventos(self):
        """Configura eventos y atajos de teclado."""
        self.root.bind('<Control-Return>', lambda e: self._ejecutar_busquedas_hilo())
        self.root.bind('<F5>', lambda e: self._limpiar_todo())
        self.root.bind('<Control-s>', lambda e: self._guardar_registro())

    def _actualizar_delay_label(self, value):
        """Actualiza la etiqueta del delay."""
        self.delay_label.configure(text=f"{float(value):.1f}s")

    def _validar_datos(self, event=None):
        """Valida los datos de entrada en tiempo real."""
        # Actualizar datos
        self._guardar_datos_desde_entradas()
        
        # Contar campos completados
        campos_completados = sum(1 for v in self.datos.values() if v.strip())
        total_campos = len(self.datos)
        
        # Actualizar status
        if campos_completados == 0:
            self.status_var.set("Ingresa los datos del objetivo")
        elif campos_completados < 3:
            self.status_var.set(f"Datos incompletos ({campos_completados}/{total_campos})")
        else:
            self.status_var.set(f"Datos suficientes ({campos_completados}/{total_campos})")

    def _actualizar_dorks(self, event=None):
        """Actualiza la lista de dorks según la categoría seleccionada."""
        categoria = self.categoria_var.get()
        self.lista_dorks.delete(0, END)
        
        if categoria and categoria in DORKS_CATEGORIZADOS:
            for dork in DORKS_CATEGORIZADOS[categoria]:
                self.lista_dorks.insert(END, dork)
            
            self.log(f"Cargados {len(DORKS_CATEGORIZADOS[categoria])} dorks de '{categoria}'", "INFO")

    def _seleccionar_todos_dorks(self):
        """Selecciona todos los dorks de la lista."""
        self.lista_dorks.select_set(0, END)
        count = self.lista_dorks.size()
        self.log(f"Seleccionados {count} dorks", "INFO")

    def _deseleccionar_todos_dorks(self):
        """Deselecciona todos los dorks."""
        self.lista_dorks.select_clear(0, END)
        self.log("Dorks deseleccionados", "INFO")

    def _guardar_datos_desde_entradas(self):
        """Guarda los datos desde los campos de entrada."""
        for campo, entry in self.entradas.items():
            self.datos[campo] = entry.get().strip()

    def _generar_queries_validas(self, dorks_seleccionados):
        """Genera queries válidas filtrando por datos disponibles."""
        queries_validas = []
        queries_omitidas = []
        
        for dork in dorks_seleccionados:
            # Encontrar campos requeridos
            campos_requeridos = re.findall(r'\{(\w+)\}', dork)
            
            # Verificar si tenemos todos los datos necesarios
            datos_disponibles = all(
                self.datos.get(campo, '').strip() 
                for campo in campos_requeridos
            )
            
            if datos_disponibles and campos_requeridos:
                try:
                    # Formatear query
                    query = dork.format(**self.datos)

                    # 👇 Limpieza segura: no tocar comillas ni operadores
                    query = re.sub(r'\s+', ' ', query).strip()

                    if query:
                        queries_validas.append(query)
                except KeyError as e:
                    self.log(f"Error en plantilla: {e} en '{dork}'", "ERROR")
                    queries_omitidas.append(dork)
            else:
                if not campos_requeridos:
                    self.log(f"Dork sin campos: '{dork}'", "WARNING")
                else:
                    campos_faltantes = [
                        campo for campo in campos_requeridos 
                        if not self.datos.get(campo, '').strip()
                    ]
                    self.log(f"Faltan datos para: {', '.join(campos_faltantes)}", "WARNING")
                queries_omitidas.append(dork)
        
        if queries_omitidas:
            self.log(f"Se omitieron {len(queries_omitidas)} dorks por datos faltantes", "WARNING")
            
        return queries_validas
    
    def _q(s):
        s = (s or "").strip()
        if not s:
            return s
        # comillar si tiene espacios y no viene ya comillado
        return f'"{s}"' if (' ' in s and not (s.startswith('"') and s.endswith('"'))) else s

        datos_fmt = self.datos.copy()
        for k in ("nombre","apellido","ciudad","pais","email","telefono","alias"):
            datos_fmt[k] = _q(datos_fmt.get(k, ""))

        query = dork.format(**datos_fmt)
        query = re.sub(r'\s+', ' ', query).strip()

    def _obtener_url_motor(self, query):
        """Obtiene la URL del motor de búsqueda seleccionado."""
        # Usar quote en lugar de quote_plus para preservar espacios como %20
        # y no convertir los dos puntos y barras de los operators
        query_encoded = urllib.parse.quote_plus(query)
        
        motores = {
            "Google": f"https://www.google.com/search?q={query_encoded}",
            "DuckDuckGo": f"https://duckduckgo.com/?q={query_encoded}",
            "Bing": f"https://www.bing.com/search?q={query_encoded}",
            "Yandex": f"https://yandex.com/search/?text={query_encoded}",
            "Baidu": f"https://www.baidu.com/s?wd={query_encoded}"
        }
        
        return motores.get(self.motor_var.get(), motores["Google"])

    def _ejecutar_busquedas_hilo(self):
        """Ejecuta las búsquedas en un hilo separado."""
        if self.ejecutando:
            messagebox.showwarning("Advertencia", "Ya hay una búsqueda en ejecución")
            return
            
        # Validaciones previas
        indices_seleccionados = self.lista_dorks.curselection()
        if not indices_seleccionados:
            messagebox.showerror("Error", "Selecciona al menos un dork")
            return
        
        self._guardar_datos_desde_entradas()
        if not any(self.datos.values()):
            messagebox.showerror("Error", "Ingresa al menos un dato del objetivo")
            return
        
        # Ejecutar en hilo separado
        threading.Thread(target=self._ejecutar_busquedas, daemon=True).start()

    def _ejecutar_busquedas(self):
        """Ejecuta las búsquedas seleccionadas."""
        try:
            self.ejecutando = True
            self._actualizar_ui_ejecutando(True)
            
            # Obtener dorks seleccionados
            indices = self.lista_dorks.curselection()
            dorks_seleccionados = [self.lista_dorks.get(i) for i in indices]
            
            # Generar queries válidas
            queries = self._generar_queries_validas(dorks_seleccionados)
            
            if not queries:
                self.log("No se pudieron generar queries válidas", "ERROR")
                messagebox.showerror("Error", "No se pudieron ejecutar búsquedas con los datos proporcionados")
                return
            
            # Ejecutar búsquedas
            self.log(f"Iniciando {len(queries)} búsquedas con {self.motor_var.get()}", "INFO")
            self.resultados_log.clear()
            
            delay = self.delay_var.get()
            motor = self.motor_var.get()
            
            for i, query in enumerate(queries, 1):
                if not self.ejecutando:  # Permitir cancelación
                    break
                    
                self.log(f"[{i}/{len(queries)}] {query}", "INFO")
                
                try:
                    url = self._obtener_url_motor(query)
                    webbrowser.open(url)
                    self.resultados_log.append({
                        "query": query,
                        "motor": motor,
                        "timestamp": datetime.now().isoformat(),
                        "url": url
                    })
                    
                    if i < len(queries):  # No esperar después de la última
                        time.sleep(delay)
                        
                except Exception as e:
                    self.log(f"Error abriendo búsqueda: {e}", "ERROR")
            
            self.log(f"✅ Completadas {len(queries)} búsquedas", "SUCCESS")
            
            # Mostrar resumen
            self.root.after(0, lambda: messagebox.showinfo(
                "Búsquedas Completadas", 
                f"Se ejecutaron {len(queries)} búsquedas exitosamente"
            ))
            
        except Exception as e:
            self.log(f"Error durante la ejecución: {e}", "ERROR")
            self.root.after(0, lambda: messagebox.showerror("Error", f"Error inesperado: {e}"))
            
        finally:
            self.ejecutando = False
            self.root.after(0, lambda: self._actualizar_ui_ejecutando(False))

    def _actualizar_ui_ejecutando(self, ejecutando):
        """Actualiza la UI según el estado de ejecución."""
        if ejecutando:
            self.btn_ejecutar.configure(text="⏹️ Ejecutando...", state="disabled")
            self.progress.start(10)
            self.status_var.set("Ejecutando búsquedas...")
        else:
            self.btn_ejecutar.configure(text="▶️ Ejecutar Búsquedas", state="normal")
            self.progress.stop()
            self.status_var.set("Listo")

    def _guardar_registro(self):
        """Guarda el registro de la sesión."""
        if not self.resultados_log:
            messagebox.showwarning("Advertencia", "No hay búsquedas que guardar")
            return
        
        try:
            self._guardar_datos_desde_entradas()
            
            registro = {
                "metadata": {
                    "fecha": datetime.now().isoformat(),
                    "version": "2.0",
                    "total_busquedas": len(self.resultados_log)
                },
                "datos_objetivo": self.datos,
                "busquedas": self.resultados_log
            }
            
            # Generar nombre de archivo único
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_registro_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(registro, f, ensure_ascii=False, indent=2)
            
            self.log(f"📁 Registro guardado: {filename}", "SUCCESS")
            messagebox.showinfo("Guardado", f"Registro guardado como:\n{filename}")
            
        except Exception as e:
            self.log(f"Error guardando registro: {e}", "ERROR")
            messagebox.showerror("Error", f"No se pudo guardar el registro:\n{e}")

    def _limpiar_todo(self):
        """Limpia todos los campos y reinicia la aplicación."""
        # Limpiar entradas
        for entry in self.entradas.values():
            entry.delete(0, END)
        
        # Limpiar selecciones
        self.categoria_combo.set('')
        self.lista_dorks.delete(0, END)
        self.lista_dorks.select_clear(0, END)
        
        # Limpiar log
        self.log_texto.config(state="normal")
        self.log_texto.delete(1.0, END)
        self.log_texto.config(state="disabled")
        
        # Reiniciar variables
        self.datos = {k: "" for k in self.datos.keys()}
        self.resultados_log.clear()
        
        # Resetear UI
        self.status_var.set("Listo")
        self.delay_var.set(2.0)
        self.motor_var.set("Google")
        
        self.log("🧹 Aplicación reiniciada", "INFO")

    def log(self, mensaje, tipo="INFO"):
        """Añade un mensaje al log con formato y colores."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Iconos por tipo
        iconos = {
            "INFO": "ℹ️",
            "SUCCESS": "✅", 
            "WARNING": "⚠️",
            "ERROR": "❌"
        }
        
        icono = iconos.get(tipo, "ℹ️")
        mensaje_completo = f"[{timestamp}] {icono} {mensaje}\n"
        
        # Añadir al log con colores
        def _add_to_log():
            self.log_texto.config(state="normal")
            self.log_texto.insert(END, mensaje_completo, tipo)
            self.log_texto.see(END)  # Auto-scroll
            self.log_texto.config(state="disabled")
        
        # Ejecutar en el hilo principal de la UI
        if threading.current_thread() != threading.main_thread():
            self.root.after(0, _add_to_log)
        else:
            _add_to_log()


def main():
    """Función principal para iniciar la aplicación."""
    try:
        root = tk.Tk()
        
        # Configurar icono de ventana si existe
        try:
            root.iconbitmap("osint.ico")  # Opcional
        except:
            pass
        
        # Crear aplicación
        app = OsintApp(root)
        
        # Configurar cierre limpio
        def on_closing():
            if app.ejecutando:
                if messagebox.askokcancel("Cerrar", "Hay búsquedas ejecutándose. ¿Cerrar de todas formas?"):
                    app.ejecutando = False
                    root.destroy()
            else:
                root.destroy()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Mostrar ventana centrada
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")
        
        # Iniciar loop principal
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Error Fatal", f"Error iniciando la aplicación:\n{e}")


if __name__ == "__main__":
    main()
