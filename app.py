#!/usr/bin/env python

import json
from flask import Flask
from flask import render_template
from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config.from_object("settings")

# instantiate SQLAlchemy DB connection:
engine = create_engine(app.config["SQLALCHEMY_DB_URI"], convert_unicode=True)

Base = declarative_base()
Base.metadata.reflect(engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(Session)

# add existing DB tables as REST endpoints
manager = APIManager(app, session=session)

for table in Base.metadata.tables.keys():
    class TablePlaceholder(Base):
        __tablename__ = str(table)
        __table__ = Base.metadata.tables[table]
    blue_print = manager.create_api(TablePlaceholder, methods=['GET', 'POST', 'DELETE', 'PUT'])

@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser and rules that require parameters
        if "GET" in rule.methods and rule.defaults and len(rule.defaults) >= len(rule.arguments):
            links.append(url_for(rule.endpoint))
    return json.dumps(links, indent=2)

app.run(debug=True)
