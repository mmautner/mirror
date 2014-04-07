#!/usr/bin/env python

import sys
import json
from flask import Flask
from flask import render_template
from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask.ext.restless import APIManager

app = Flask(__name__)

if len(sys.argv) > 1:
    engine = create_engine(sys.argv[1], convert_unicode=True)
else:
    app.config.from_object("settings")
    engine = create_engine(app.config["SQLALCHEMY_DB_URI"], convert_unicode=True)

Base = declarative_base()
Base.metadata.reflect(engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(Session)

manager = APIManager(app, session=session)

def sqlalchemy_class_factory(tablename, BaseObj):
    """create a class that inherits from a SQLAlchemy declarative base"""
    class_name = str(''.join([t[0].upper() + t[1:] for t in table.split('_')]))
    class_attrs = {
        '__tablename__': str(table),
        '__table__': BaseObj.metadata.tables[table]
    }
    return type(class_name, (BaseObj,), class_attrs)

for table in Base.metadata.tables.keys():
    blue_print = manager.create_api(sqlalchemy_class_factory(table, Base),
                                    methods=['GET', 'POST', 'DELETE', 'PUT'])

@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser and rules that require parameters
        if "GET" in rule.methods and rule.defaults and len(rule.defaults) >= len(rule.arguments):
            links.append(url_for(rule.endpoint))
    return json.dumps(links, indent=2)

app.run(debug=True)
