# Audio

This Project is made using Python Flask framwork.

Purpose of project:
-------------------
purpose of project is to make flask based CURD(create,update,delete,read) operation,
on 3 types of Audio files :- 
(1) song
(2) podcast
(3) audiobook


Modules included:
-----------------
import json
from flask import Flask, render_template, request, url_for, redirect, Response
from flask_mysqldb import MySQL


Routes:
--------
In this project we have 4 routes:

(1) Add files:

http://localhost:5000/create 

(2) Fetch Files:

http://localhost:5000/audioFileType


http://localhost:5000/audioFileType/audioFileID

(3) Update files info:

http://localhost:5000/update/audioFileType/audioFileID


(4) Delete file info:

http://localhost:5000/delete/audioFileType/audioFileID


Database used:
--------------
It uses mysql db
"audio.sql" is include among other files you can import file into mysql DB to get started.

Extras:
-------
I hv used Apache "xampp" server as localhost for mysql Db connection

