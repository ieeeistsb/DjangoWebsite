# ieee-website


########### FIRST TIME ############
(How to prepare your back-end and front-end environment)

#$ pipenv shell
#$ pipenv install
#$ cd static
#$ npm install
#$ npm install -g webpack-cli
#$ cd ..
#$ ./manage.py runserver
#$ exit

########### COMPILE FRONT-END #########
(if assets were added to src code, copy them to the public directory as well)

#$ cd static
#$ webpack --display-error-details


########## TO RUN ##########

#$ ./manage.y runserver


######### GIT PROCESS ########

# TO DO A NEW FEATURE
#$ git checkout -b feature/<feature-name>
	...
	... (programming, commits, ...)
	...
#$ git add .
#$ git commit -m "Featute <feature-name> done"
#$ git checkout develop
#$ git pull
#$ git merge feature/<feature-name>
#$ git push


# TO FIX A BUG
#$ git checkout -b fix/<fix-name>
	...
	... (programming, commits, ...)
	...
#$ git add .
#$ git commit -m "<fix-name> fixed"
#$ git checkout develop
#$ git pull
#$ git merge fix/<fix-name>
#$ git push

# TO CREATE A RELEASE VERSION
#$ git checkout -b release/vA.Fe.Fi    (A-Architecture changed, Fe-New features, Fi-Bugs Fixed)
	...
	... (programming, commits, ...)
	...
#$ git add .
#$ git commit -m "<fix-name> fixed"
#$ git checkout develop
#$ git pull
#$ git merge fix/<fix-name>
#$ git push

########### INITIAL PROCESS CREATION #################
(Basicallly how the project was created)

#$ pipenv shell
#$ pipenv install django
#$ pipenv install djangorestframework

#$ django-admin startproject IEEESite .
#$ django-admin startapp app

# ADDED SOME DIRECTORIES

# PREPARED Pipfile
	pipenv install pillow

# PREPARED package.json
	npm install
# PREPARED webpack.config.js
	loaders...
		.babelrc
		tsconfig.json
