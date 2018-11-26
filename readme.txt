1. Files *_parcer.py need for parcing *-sites and write information in *.csv as name and price columns
2. Files *_replace.csv content item names in shops and names, with which we want to work 
3. db.py is sql alchemy-file
4. db_from_csv.py get info from csv and write it to db
5. collect.py cron-script, runs *_parcer.py и db_from_csv.py
6. core_shopping_list.py main logit of project
