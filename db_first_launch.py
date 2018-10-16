from db import db_session, Product
import buttons

for item in buttons.item_list:
    prod = Product(name = item)
    db_session.add(prod)
db_session.commit()
