# mirror
======

Reflecting relational databases into client-rich web apps.

----------------

### A demo

1. Install the requisite python libraries:

	$ pip install -r requirements.txt

2. Edit the database URI in settings.py to point to the database you want to expose via REST API. In my case, I exposed an existing WordPress database by setting the DB URI to ""

3. Run the server process:

	$ ./app.py

Go to town:

	$ curl http://localhost:5000/site-map
	{"/api/wp_term_relationships": "wp_term_relationshipsapi0.wp_term_relationshipsapi", "/api/wp_options": "wp_optionsapi0.wp_optionsapi", "/api/wp_comments": "wp_commentsapi0.wp_commentsapi", "/api/wp_users": "wp_usersapi0.wp_usersapi", "/api/wp_term_taxonomy": "wp_term_taxonomyapi0.wp_term_taxonomyapi", "/api/wp_posts": "wp_postsapi0.wp_postsapi", "/api/wp_usermeta": "wp_usermetaapi0.wp_usermetaapi", "/api/wp_commentmeta": "wp_commentmetaapi0.wp_commentmetaapi", "/api/wp_terms": "wp_termsapi0.wp_termsapi", "/api/wp_postmeta": "wp_postmetaapi0.wp_postmetaapi", "/api/wp_links": "wp_linksapi0.wp_linksapi"}
	$
	$ curl http://localhost:5000/api/wp_posts
	...wp_posts.json...

[Mirror](https://github.com/mmautner/mirror) aims to be a library 
for literally "generating" applications from database schema ,while 
retaining the ability to rapidly iterate on the schema's design.

The ideal:

    Given an existing relational database, the *schema* of the 
    existing relations can be serialized to a data format 
    (e.g. YAML, JSON, XML). This serialized copy of the 
    schema can be used for several purposes:

        1. Easier *database migrations*.

        2. Simpler *version-controlling the DB schema* in a single
        place--no more changing 3 ORM's table definitions to reflect 
        a database schema change.

        3. *All parts of your stack that reference the database schema 
        can share a common/implementation-agnostic definition of it*.
        This can drastically reduce "adoption costs" for client software,
        by allowing client software to merely "reflect" a new schema.

    Client libraries can be created for different programming languages to 
    parse such serialized schemas into the ORM/SQL abstraction layer 
    libraries of choice, e.g. ActiveRecord (ruby), SQLAlchemy (python).



-------
Related projects:

- [ActiveRecord](http://guides.rubyonrails.org/active_record_basics.html) (Ruby ORM)
- [SQLAlchemy](http://www.sqlalchemy.org/) (Python ORM/SQL abstraction library),
- [Backbone.js](http://backbonejs.org/) (Javascript MVC), 
- [Andromeda](http://www.andromeda-project.org/) (DB->webapp generation library), 
- [Pyrseas](https://geithub.com/perseas/Pyrseas) (PostgreSQL-specific schema serialization library) 
