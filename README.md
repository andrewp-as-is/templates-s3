<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/templates-s3.svg?maxAge=3600)](https://pypi.org/project/templates-s3/)
[![](https://img.shields.io/npm/v/templates-s3.svg?maxAge=3600)](https://www.npmjs.com/package/templates-s3)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/templates-s3/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/templates-s3/actions)

### Installation
```bash
$ [sudo] pip install templates-s3
```

```bash
$ [sudo] npm i -g templates-s3
```

#### Pros
+   store templates on S3 - no need rebuild docker image

#### How it works
`templates/` hard-coded folder

scripts:
+   create full-access/read-only user and credentials
+   upload/download `templates/`

hard-coded environment variables names:
+   `AWS_S3_TEMPLATES_BUCKET`
+   `AWS_S3_TEMPLATES_USER`
+   `AWS_S3_TEMPLATES_ACCESS_KEY_ID`
+   `AWS_S3_TEMPLATES_SECRET_ACCESS_KEY`

#### Examples
`Makefile`, create env
```bash
TEMPLATES_BUCKET:=BUCKET_NAME
all:
    test -s .env.s3.templates || templates-s3-create-full-access-env $(TEMPLATES_BUCKET) > .env.s3.templates
    test -s .env.prod.templates || templates-s3-create-read-only-env $(TEMPLATES_BUCKET) > .env.prod.templates
```

upload `templates/` to S3 
```bash
set -o allexport
. .env.s3.templates || exit

templates-s3-upload
```

`Dockerfile` 
```Dockerfile
ENTRYPOINT ["/bin/sh","/entrypoint.sh"]
```

`entrypoint.sh`
```bash
templates-s3-download
...
```

`ansible-playbook.yml`
```yml
...
  tasks:
  - name: task_name
    docker_container:
      ...
      env_file: ".env.prod"
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>