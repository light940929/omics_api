
# Omics Pipe API (Version 0.0.2alpha)

[Read more words!](http://aws1niagads.org:8000/about/)

## Overview

**Omics Pipe API**: Design for user to know already module we have and then create a new pipeline recipe by yourself on version 0.0.2alpha .


## What's workflow?

1. User need login with *google oauth2*.
2. User click the **Omics Pipe API document**.
3. User would see what api we support.
4. If user see the modules we have, user could arrange a new pipeline recipe.
5. API support user to post a new pipeline recipe. If the I/O are not suitable to process, our system will send email to user.
6. If user have a new module would like to post, our system will make sure these elements will be created or not. That'll need to take time to check the environment.

## Set your settings file
#### SECURITY WARNING: keep the secret key used in production secret!

```
SECRET_KEY = 'Django secret key'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'YOUR KEY'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'YOUR SECRET'
```

##


## Requirement
* Python (2.6, 2.7)
* Django (1.8)
* Django REST framework (3.3.1)
* PyAML (3.11)
* django-oauth-toolkit(0.9.0)
* python-social-auth(0.2.13)
* django-rest-swagger(0.3.4)
* PIL(1.1.7)
* django-grappelli(2.7.2)
* django-filebrowser(3.6.1)
* djangorestframework-yaml(1.0.2)

##Request
About detail Docs: import omicspipeapi_0.0.2.yaml with http://editor.swagger.io/.
--------
<table>
 <tr>
   <th>URL</th>
   <th>Method</th>
   <th>Parameters</th>
   <th>Description</th>
 </tr>

 <tr>
  <td>/categories/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All Categories</td>
 </tr>
 <tr>
  <td>/categories/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a Category</td>
 </tr>
 <tr>
  <td>/templates/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All Templates</td>
 </tr>
 <tr>
  <td>/templates/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a Template</td>
 </tr>
 <tr>
  <td>/modules/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All Modules</td>
 </tr>
 <tr>
  <td>/modules/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a Module</td>
 </tr>
 <tr>
  <td>/pipelines/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All Pipelines</td>
 </tr>
 <tr>
  <td>/pipelines/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a Pipeline</td>
 </tr>
 <tr>
  <td>/pipelinerecipes/</td>
  <td>POST</td>
  <td>name, description, ingredients, steps, equipment, resultpath, footnote</td>
  <td>Create a New pipline recipe</td>
 </tr>
 <tr>
  <td>/pipelinerecipes/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All Pipeline recipes</td>
 </tr>
 <tr>
 <td>/pipelinerecipes/:id</td>
  <td>PATCH</td>
  <td>name, description, ingredients, steps, equipment, resultpath, footnote</td>
  <td>Update a pipeline recipe</td>
 </tr>
 <tr>
  <td>/pipelinerecipes/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a Pipeline recipe</td>
 </tr>
 <tr>
  <td>/pipelinerecipes/:id</td>
  <td>DELETE</td>
  <td></td>
  <td>Delete a pipeline recipe</td>
 </tr>
 <tr>
  <td>/modelscripts/</td>
  <td>POST</td>
  <td>name, description, inputformat, outformat, parameters, server, scriptpath</td>
  <td>Create a New modelscript</td>
 </tr>
 <tr>
  <td>/modelscripts/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All modelscripts</td>
 </tr>
 <tr>
 <td>/modelscripts/:id</td>
  <td>PATCH</td>
  <td>name, description, inputformat, outformat, parameters, server, scriptpath</td>
  <td>Update a modelscript</td>
 </tr>
 <tr>
  <td>/modelscripts/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a modelscript</td>
 </tr>
 <tr>
  <td>/modelscripts/:id</td>
  <td>DELETE</td>
  <td></td>
  <td>Delete a modelscript</td>
 </tr>
 <tr>
 <td>/ingredients/</td>
  <td>POST</td>
  <td>title, topic, server, path, format, group</td>
  <td>Create a New ingredient</td>
 </tr>
 <tr>
  <td>/ingredients/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All ingredients</td>
 </tr>
 <tr>
 <td>/ingredients/:id</td>
  <td>PATCH</td>
  <td>title, topic, server, path, format, group</td>
  <td>Update a ingredient</td>
 </tr>
 <tr>
  <td>/ingredients/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a ingredient</td>
 </tr>
 <tr>
  <td>/ingredients/:id</td>
  <td>DELETE</td>
  <td></td>
  <td>Delete a ingredient</td>
 </tr>
 <tr>
  <td>/ingredientgroups/</td>
  <td>POST</td>
  <td>name, topic, ingredients, recipes</td>
  <td>Create a New ingredientgroup</td>
 </tr>
 <tr>
  <td>/ingredientgroups/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All ingredientgroups</td>
 </tr>
 <tr>
 <td>/ingredients/:id</td>
  <td>PATCH</td>
  <td>name, topic, ingredients, recipes</td>
  <td>Update a ingredient</td>
 </tr>
 <tr>
  <td>/ingredientgroups/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a ingredientgroup</td>
 </tr>
 <tr>
  <td>/ingredientgroups/:id</td>
  <td>DELETE</td>
  <td></td>
  <td>Delete a ingredientgroup</td>
 </tr>
 <tr>
  <td>/steps/</td>
  <td>POST</td>
  <td>title, scheduler, priority, follows, group</td>
  <td>Create a New step</td>
 </tr>
 <tr>
  <td>/steps/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All steps</td>
 </tr>
 <tr>
 <td>/steps/:id</td>
  <td>PATCH</td>
  <td>title, scheduler, priority, follows, group</td>
  <td>Update a step</td>
 </tr>
 <tr>
  <td>/steps/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a step</td>
 </tr>
 <tr>
  <td>/steps/:id</td>
  <td>DELETE</td>
  <td></td>
  <td>Delete a step</td>
 </tr>
 <tr>
  <td>/stepgroups/</td>
  <td>POST</td>
  <td>name, topic, steps, recipes, functions</td>
  <td>Create a New stepgroup</td>
 </tr>
 <tr>
  <td>/stepgroups/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All stepgroups</td>
 </tr>
 <tr>
 <td>/stepgroups/:id</td>
  <td>PATCH</td>
  <td>name, topic, steps, recipes, functions</td>
  <td>Update a stepgroups</td>
 </tr>
 <tr>
  <td>/stepgroups/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a stepgroup</td>
 </tr>
 <tr>
  <td>/stepgroups/:id</td>
  <td>DELETE</td>
  <td></td>
  <td>Delete a stepgroup</td>
 </tr>
 <tr>
  <td>/userfiles/</td>
  <td>POST</td>
  <td>name, server, path, models</td>
  <td>Create a New userfile</td>
 </tr>
 <tr>
  <td>/userfiles/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All userfiles</td>
 </tr>
 <tr>
 <td>/userfiles/:id</td>
  <td>PATCH</td>
  <td>name, server, path, models</td>
  <td>Update a userfile</td>
 </tr>
 <tr>
  <td>/userfiles/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a userfile</td>
 </tr>
 <tr>
  <td>/userfiles/:id</td>
  <td>DELETE</td>
  <td></td>
  <td>Delete a userfile</td>
 </tr>
 

### New API version 0.0.3 are coming~

Follow [@light940929](https://github.com/light940929/omics_api) on Github for the latest news.
