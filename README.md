# Backend Django Exam CAM Fraud Detection 
Setting the serverless for the Application.

## Requirements

To work with this repo you should have preinstalled:

* Docker Desktop
* Serverless Framework
* Node Package Manager
* Make ( For windows download from https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81.exe/download?use_mirror=excellmedia&download=)

## Setup

Change `service`, `app` and `org` values in:

```
nano serverless.yml
```

Fill in secrets
```
cp .env.sample .env && nano .env
```

Set the same secrets in Serverless Dashboard
```
make db
```

Install deployment deps
```
make install-deps
```

## Development

For local development
```
make rebuild
```

For Django shell
```
make shell
```

For running migrations
```
make migrate
```

## Deployment

For remote deployment
```
make deploy
```

For remote migrations
```
make remote-migrate
make remote-migrate-logs
```

## Maintainance

When ever you need to update the requirements.txt run below code

```
sed -i '' 's/==/>=/g' requirements.txt
pip install -U -r requirements.txt
pip freeze > requirements.txt
```