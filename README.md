
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

###Request
About detail Docs: import omicspipeapi.yaml with http://editor.swagger.io/.
--------
<table>
 <tr>
   <th>URL</th>
   <th>Method</th>
   <th>Parameters</th>
   <th>Description</th>
 </tr>
  <tr>
  <td>/users/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All Users</td>
 </tr>
 <tr>
  <td>/users/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a User</td>
 </tr>
 <tr>
  <td>/groups/</td>
  <td>GET</td>
  <td></td>
  <td>Fetch All Groups</td>
 </tr>
 <tr>
  <td>/groups/:id</td>
  <td>GET</td>
  <td></td>
  <td>Fetch a Group</td>
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
  <td>name, description, ingredient, direction, equipment, rawdata, result, footnote</td>
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
  <td>name, description, ingredient, direction, equipment, rawdata, result, footnote</td>
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
  <td>name, description, inputformat, outformat, parameters, datapath</td>
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
  <td>name, description, inputformat, outformat, parameters, datapath</td>
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


### New API version 0.0.3 are coming~

Follow [@light940929](https://github.com/light940929/omics_api) on Github for the latest news.
